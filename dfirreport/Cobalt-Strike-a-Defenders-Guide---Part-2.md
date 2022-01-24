# Cobalt Strike, a Defender’s Guide - Part 2
### In this post, we will focus on the network traffic it produced, and provide some easy wins defenders can be on the look out for to detect beaconing activity. We cover topics such as Domain Fronting, SOCKS proxy, C2 traffic, Sigma rules, JARM, JA3/s, RITA and more.

## Information:
+ Source: The DFIR Report
+ Link: https://thedfirreport.com/2022/01/24/cobalt-strike-a-defenders-guide-part-2/
+ Date: 2022-01-24T03:03:49+00:00
+ Author: editor


## Article:
![Article Image](https://thedfirreport.com/wp-content/uploads/2022/01/Cobalt-Strike.jpg)

Our [previous article](https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/) on Cobalt Strike focused on the most frequently used capabilities that we had observed. In this post, we will focus on the network traffic it produced, and provide some easy wins defenders can be on the look out for to detect beaconing activity. We cover topics such as Domain Fronting, SOCKS proxy, C2 traffic, Sigma rules, JARM, JA3/s, RITA and more. 


As with our previous article, we will highlight the common ways we see threat actors using Cobalt Strike.


![](https://thedfirreport.com/wp-content/uploads/2022/01/image2.png)


Big shout-out to [@Kostastsale](https://twitter.com/Kostastsale/) for helping put this Part 2 together! Also thanks to [@svch0st](https://twitter.com/svch0st), [**@pigerlin**](https://twitter.com/pigerlin), and [**@0xtornado**](https://twitter.com/0xtornado) for reviewing this report. 


Even though network monitoring and detection capabilities do not come easy for many organizations, they can generally offer a high return on investment if implemented correctly. Malware has to contact its C2 server if it is to receive further instructions. This article will demonstrate how to detect this communication before threat actors accomplish their objectives. There are a couple of factors that we can utilize to fingerprint any suspicious traffic and subsequent infrastructure. Before we get into that part, we should first discuss what makes Cobalt Strike so versatile.


Cobalt Strike’s versatility comes from the ability to change the indicators with each payload. This is made possible thanks to Malleable C2 profiles. Our other post touched on Malleable C2 profiles and how threat actors use them; however, that was just some of their many applications. Below you can find information related to some of the most important fields that could throw off an analyst while investigating a Cobalt Strike network communication:


*The reference profile below is taken from Raphael Mudge’s GitHub repository.*



```
###Global Options###
set sample\_name "whatever.profile";
set sleeptime "0"; <================ # Decimal number to indicate the time the beacon will sleep for between communications in milliseconds
set jitter    "25"; <================ # A number that indicates the percentage of a random sleep time that beacon will introduce to its C2 comm
set useragent "<string>"; <================ # Custom user agent of your choice
set data\_jitter "35"; <================ # Represents the value bytes variable that would instruct Cobalt Strike to send a random string on http-get/post to match the bytes value.
set headers\_remove "<header to remove>"; <================ # Specifying headers to be removed in a comma separated manner.

####### Not much explanation is needed here, you can change the certificate information to your heart's content.#######
https-certificate {
    set C "US";
    set CN "whatever.com";
    set L "California";
    set O "whatever LLC.";
    set OU "local.org";
    set ST "CA";
    set validity "365";
}
###HTTP-Config Block###
http-config {
    set headers "<headers to include>"; <================ # Specifying the headers that you want to include.
    header "<name of the header(s)>";  <================ # Specifying the name of the header that will store the data that are transmitted to the C2 server
    set trust\_x\_forwarded\_for "<true OR false>";  <================ # If the C2 server is behind a redirector, this option would allow to forward the traffic to the correct destination 
    set block\_useragents "<user agents>";  <================ # User agents that C2 server will block and show a 404 response
    set allow\_useragents "<user agents>"  <================ # Opposite of the above
}
###HTTP-GET Block. This function and all of its fields could also exist and be customized for the HTTP-POST Block (Server communication)###
http-get {
    set uri "/<URI string>";  <================ # Specifying the URI to reference in bidirectional communication from client and server
    set verb "POST";  <================ # Setting the verb when requesting available tasks from the C2 server.	   
    client {
        header "Host" "whatever.com";  <================ # Setting the header specific to client communication with the C2. 
        header "Connection" "close";
### Metadata corresponds to the information that the beacon is sending to the C2 server about itself. The operators may choose to enable additional fields that will include data on the C2 communication. You can mix and match fields below:
    metadata {
        #base64;  <================ # Base64 encoded string
        base64url;  <================ # URL safe Base64 encoded string
        #mask;  <================ # Encrypting and encoding the data with XOR mask and random key
        #netbios;  <================ # Encoding data as netbios in lower case
        #netbiosu;  <================ # Another variation of netbios encoding 
        #prepend "TEST123";  <================ # Choosing a string to prepend to the transmitted data
        append ".php";  <================ # Choosing a string to append
     ### Termination statements: This statement tells Beacon and its server wherein the transaction to store the transformed data. You may choose one of these termination statement methods.
        parameter "file";  <================ # Adding a parameter to the URI.
        #header "Cookie";  <================ # Adding a specific string within a specific header.
        #uri-append;  <================ # Adding a specific string in the URI. 
        #print;
    }
    parameter "test1" "t
```

We added comments to the profile above to explain the numerous fields operators can change to customize the profile to their needs. All these different fields provide control and flexibility over the indicators of the C2 channel. Many free, open-source randomizer scripts exist to create a unique profile such as [Random C2 Profile Generator](https://github.com/threatexpress/random_c2_profile) by [@joevest](https://twitter.com/joevest), [Malleable-C2-Randomizer](https://github.com/bluscreenofjeff/Malleable-C2-Randomizer) by [@bluscreenofjeff](https://twitter.com/bluscreenofjeff), and [C2concealer](https://github.com/FortyNorthSecurity/C2concealer) by [@FortyNorthSec](https://twitter.com/FortyNorthSec).


Below are some of the Cobalt Strike C2 servers that we observed during intrusions. On the right column, we show the URLs that the Cobalt Strike payloads were configured to query. A trained eye could spot some of the Malleable profiles that exist on freely available resources such as Raphael Mudge’s list on his [GitHub page](https://github.com/rsmudge/Malleable-C2-Profiles). Another example is the “*jquery-3.3.1.min.js”* which is associated with [this](https://github.com/threatexpress/malleable-c2/blob/master/jquery-c2.3.11.profile) malleable C2 profile as we observed in [four intrusions](https://thedfirreport.com/?s=jquery-3.3.1).



```
+----------------------+-----------------------+
| C2 Server            |  URI queried          |
+----------------------+-----------------------+
| gawocag.com          | /nd                   |
| 190.114.254.116      | /push                 |
| 190.114.254.116      | /\_\_utm.gif            |
| kaslose.com          | /jquery-3.3.1.min.js  |
| yawero.com           | /skin.js              |
| sazoya.com           | /skin.js              |
| 192.198.86.130       | /skin.js              |
| 162.244.83.216       | /jquery-3.3.1.min.js  |
| sammitng.com         | /jquery-3.3.1.min.js  |
| 23.19.227.147        | /styles.html          |
| securityupdateav.com | /tab\_shop\_active.html |
| 108.62.118.247       | /as                   |
| windowsupdatesc.com  | /as                   |
| 212.114.52.180       | /copyright.css        |
| defenderupdateav.com | /default.css          |
| onlineworkercz[.]com | /kj                   |
| checkauj.com         | /jquery-3.3.1.min.js  |
+----------------------+-----------------------+
```

A deep dive into all available fields can be found on [this post](https://blog.zsec.uk/cobalt-strike-profiles/) from [@ZephrFish](https://twitter.com/ZephrFish). He also includes other fields related to post-exploitation beacon configuration along with network communication-related fields. Another great resource is [this article](https://posts.specterops.io/a-deep-dive-into-cobalt-strike-malleable-c2-6660e33b0e0b) released by SpecterOps.


Domain Fronting
---------------


Domain fronting is another method for concealing communication between the endpoint and the command and control servers. The main purpose of domain fronting is to connect to a restricted host while pretending to communicate with an allowed host. It essentially masks your traffic to a certain website by masquerading it as a different domain.


This technique is possible thanks to Content Delivery Networks (CDNs). Domain fronting was mostly used by web services to bypass censorship in several countries that restricted traffic (e.g., China). In recent years, attackers have started using this technique to hide their malicious infrastructure behind legitimate domains. Because domain fronting is a complicated topic to grasp, below we have included an image from the official Cobalt Strike [page](https://www.cobaltstrike.com/blog/high-reputation-redirectors-and-domain-fronting/) that discusses this technique.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/image3.png)](https://thedfirreport.com/wp-content/uploads/2022/01/image3.png)



Cobalt Strike made domain fronting possible by allowing the operators to configure related settings via the malleable C2 profiles. The following prerequisites must be met in order for domain fronting to be possible:


1. Own a domain. (e.g., infosecppl.store)
2. Pick one of the many web services that provide CDN capabilities. (e.g., cloudfront.net).
3. Setup the CDN service to create a new CDN endpoint and redirect traffic to your domain. (e.g., l33th4x0r.cloudfront.net).
4. Setup a profile to facilitate domain fronting.
5. Identify a domain that uses the same CDN to ensure that the traffic will be forwarded to the correct resource.


Step five is where things get interesting. Attackers can use legitimate domains that are registered under the same CDN provider. As demonstrated in the screenshot above, all they have to do is include their CDN endpoint domain (created in step three) in the host header of the request. In that way, the legitimate website will forward the traffic through the CDN to the original destination according to the host header.


In the screenshots below, you can see how the malleable C2 profiles are configured to allow domain fronting using the Fastly and AzureEdge CDNs:


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-3.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-3.png)


This research [paper](https://www.bamsoftware.com/papers/fronting/) released by academics from the University of California, Berkeley, is a great introduction to domain fronting. This paper inspired many researchers to expand the possibilities of this unique way of hiding the final destination server on web traffic. One of those researchers is [Vincent](https://twitter.com/vysecurity) who wrote a great [article](https://www.vincentyiu.com/red-team/domain-fronting/domain-fronting-who-am-i) on domain fronting. He explains in simple terms how it works. He also published a [Python](https://github.com/vysecurity/FindFrontableDomains) script to identify possible domains that can be leveraged for domain fronting.
Looking into our reporting, we don’t see many instances of domain fronting. This is most likely due to the complex process of setting up the necessary infrastructure. Although, based on the data we have collected regarding malicious infrastructure, domain fronting appears to be used by threat actors. According to our data from early 2021 up to now, Amazon Cloudfront takes the lead on preferable CDN used by threat actors, by a large margin.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-4.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-4.png)


The data above is available via our services. More information on this service and others can be found [here](https://thedfirreport.com/services/).


Reverse Proxy using Cobalt Strike Beacon
----------------------------------------


A technique that we come across often is a reverse proxy. We see instances where threat actors use their beacon sessions to establish RDP access through a reverse proxy. Cobalt Strike has the ability to run a SOCKS proxy server on the team server. This enables the operators to setup a listening port and leverage it to relay traffic to and from the open beacon session. The screenshot below demonstrates this implementation.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-5.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-5.png)


Image credit: [cobaltstrike.com](https://www.cobaltstrike.com/blog/reverse-port-forward-through-a-socks-proxy/)


Some of the cases we have observed threat actors using reverse proxy are:


* [Diavol Ransomware](https://thedfirreport.com/2021/12/13/diavol-ransomware/)
* [BazarLoader and the Conti Leaks](https://thedfirreport.com/2021/10/04/bazarloader-and-the-conti-leaks/)
* [Snatch Ransomware](https://thedfirreport.com/2020/06/21/snatch-ransomware/)


In most, of the above cases, the aim of the attackers was to establish a Remote Desktop session. There are numerous advantages to establishing a RDP session, including the ability to navigate using a graphical environment and easily move laterally once the necessary access has been granted.


Below, we demonstrate how attackers take advantage of this technique using [proxychains](https://github.com/haad/proxychains) from the attackers’ kali Linux host. In the first image, the attackers open a socks listening port, in this case port 8888, on the Cobalt Strike team server.[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-6.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-6.png)


*Creating the listening port (TCP port 8888)*

In this second image, we employ proxychains from the attacker’s Kali Linux host to RDP into our target’s environment via the SOCKS server. We essentially add the team server’s IP address into the proxychains configuration and connect with xfreerdp.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-7.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-7.png)*RDP into the target host using reverse proxy*


Looking into the generated artifacts, we can see that a 4624 type 3 event is created on the target host. One interesting aspect that we have also mentioned in similar cases from our reporting is that the victim’s hostname is captured in this logon event as well as the source address being 127.0.0.1.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-8.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-8.png)


*Security Event ID 4624 Type 3 shows the attacker’s hostname*

Once again, the running Cobalt Strike beacon acts as the intermediary to facilitate the Remote Desktop session via reverse proxy.


**Inside Cobalt Strike’s C2 Traffic**
-------------------------------------


This section will attempt to illustrate how the different malleable C2 profiles can affect network communication.


In some of the examples below, we simulated the malicious C2 channel to show how different malleable profile configurations can change the observed traffic. After that, we’ll examine network data associated with lateral movement and the various methods employed by Cobalt Strike operators based on our observations.


### **HTTP/HTTPS C2 traffic**


We will use a slightly modified version of the [jquery profile](https://raw.githubusercontent.com/threatexpress/malleable-c2/master/jquery-c2.3.11.profile) to illustrate how the configuration defines the various fields that make up the C2 connection. Our previous article presented this jquery profile as one of the most commonly used profiles by threat actors in the intrusions we reported.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-9.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-9.png)


As shown above, malleable C2 profiles can generate unique network traffic based on the provided configuration. A portion of the malleable C2 profile configuration is shown at the bottom half of the screenshot. At the top half of the screenshot, we show the HTTP communication between the Beacon and the Cobalt Strike server.


The malleable profile determines the content of all parameters used in GET and POST requests. Because of how simple it is to change these parameters, creating network signatures for proactive defense can be difficult. Defenders can create signatures for publicly available profiles (see Sigma section below) or profiles extracted and made available thru open-source reporting. One could search for traffic that matches known patterns (such as jquery or amazon) but the target IP/domain does not match the expected infrastructure.


### **DNS C2 traffic**


Cobalt Strike is capable of using DNS as the C2 method. Operators can choose to configure their server to respond to beacon requests in A, AAAA or TXT records. This strategy is useful for more covert operations, as the destination host could be a benign DNS server. Defenders will have to inspect the traffic data and look for suspicious DNS records.


The screenshot below is from the official Cobalt Strike [documentation page](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/listener-infrastructue_beacon-dns.htm#_Toc65482739) and shows how DNS communication works between the compromised host and the C2 server.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-10.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-10.png)


In the below example, we emulated this technique and configured the Beacon to communicate over DNS and request new tasks using A records. In the same way, we can configure the Beacon to use TXT or AAAA records for requesting tasks or sending information to the server. It is worth noting that the default method is the DNS TXT record data channel. Below is the infrastructure that we used for demonstration purposes:


* Target Host: 192.168.88.179
* Internal DNS server: 192.168.88.2
* Cobalt Strike C2 domain: [infosecppl.store](http://infosecppl.store)


We instructed the Beacon to execute the command systeminfo on the compromised host. As you can see from the screenshot below, it took 148 packets containing DNS requests and responses to finish the task and send back the data to the Cobalt Strike Server. The activity took 5 seconds to complete.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-11.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-11.png)
As with HTTP/HTTPS traffic, DNS traffic can be randomized using malleable C2 profiles. Some of the options that are available to threat actors are as follows:


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-12.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-12.png)*The above table was taken from [Cobalt Strike’s official documentation](https://www.cobaltstrike.com/help-malleable-c2#dns-beacon-bm)*


### **SMB Beacons**


Another option for threat actors is to employ SMB beacons, once they have gained access to the network. SMB beacons open a local port on the target host and listen for incoming communication from a parent beacon. The communication between the two beacons is possible thanks to named pipes.


The operators can configure the pipename on the client; however, the default pipename starts with “*msagent\_#”* for SMB beacons. For a list of default pipe names for other services including some custom profiles check out @svch0st’s post [here](https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575).


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-21.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-21.png)


SMB beacons are mostly used to make network detection harder and to get access to isolated systems where communication to the internet is prohibited. Additionally, due to SMB protocol being accessible in most internal networks, it makes for a reliable C2 method. Operators can also chain beacons and move laterally inside the network.


According to our records, SMB beacons are not frequently used. However, they’re still a powerful weapon in the hands of skilled operators. As we do not see SMB beacons used often in our intrusion cases, we took an example case from our lab to demonstrate the effectiveness of this method.


We ran a PowerShell loader on the target host, which loaded a stageless SMB beacon in memory. In our case, the SMB Beacon is communicating over the network with a parent Beacon using named pipes. For this example, we chose the named pipe “my\_pipes”.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-22.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-22.png)


As you can see from the screenshots below, windows event 4688 contains the execution of the PowerShell command.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-23.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-23.png)


As explained in our [previous Cobalt Strike](https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/) article, Sysmon events 17 and 18 can log named pipes. However, Sysmon should be explicitly configured to log named pipes. A good public Sysmon config that includes named pipes and much more is [Olaf](https://twitter.com/olafhartong)‘s [Sysmon Moduler](https://github.com/olafhartong/sysmon-modular). 


Below, you can see the named pipe created that we specified on the Cobalt Strike interface when we created the SMB listener.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-24.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-24.png)


Furthermore, the SMB Beacon will communicate over port 445 to the main beacon as we described above, which will then send the results to the C2 server. This is known as chaining beacons. The below screenshot illustrates the SMB communication between the beacon on the beachhead host and the chained beacon(s). Another way to describe the communication is a parent/child relationship.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-25.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-25.png)


The network traffic shows the target host communicating over SMB with the other compromised host running the parent HTTP Beacon. Named Pipes are used to facilitate the transition of data.


*192.168.38.102 = SMB Beacon*


*192.168.38.104 = HTTP Parent Beacon*


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-26.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-26.png)


**Detecting and Analyzing C2 Traffic**
--------------------------------------


Thanks to free, open-source tooling, investigating network traffic has become more accessible. There are specific tools that we use to analyze suspicious network traffic in our intrusion cases. We believe that no single tool can provide complete detection coverage, but we can get close by combining them. In the following section, we will look at these tools that could accelerate analysis for defenders.


### Sigma


We’ll go through a few Sigma rules that can help us detect Cobalt Strike’s network activity.


[Cobalt Strike DNS Beaconing](https://github.com/SigmaHQ/sigma/blob/master/rules/network/net_mal_dns_cobaltstrike.yml) is a rule created by [Florian Roth](https://twitter.com/cyb3rops) which looks at DNS logs to detect the default DNS C2 behavior based on the dns\_stager\_subhost, put\_output and dns\_stager\_subhost as seen above.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-27.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-27.png)


Below is a more generic [rule](https://bradleyjkemp.dev/sigmadoc/rules/network/net_dns_c2_detection.yml/) created by [@bareiss\_patrick](https://twitter.com/bareiss_patrick) which is a good example of detecting suspicious DNS traffic based on a high amount of queries for a single domain.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-28.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-28.png)


Another more generic [rule](https://github.com/SigmaHQ/sigma/blob/eb382c4a59b6d87e186ee269805fe2db2acf250e/rules/network/net_high_txt_records_requests_rate.yml) created by [Daniil Yugoslavskiy](https://twitter.com/yugoslavskiy) uses dns logs to look for 50 or more TXT records from a single source in one minute:


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-29.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-29.png)


[Default Cobalt Strike Certificate](https://github.com/SigmaHQ/sigma/blob/eb382c4a59b6d87e186ee269805fe2db2acf250e/rules/network/zeek/zeek_default_cobalt_strike_certificate.yml) is a rule written by [Bhabesh Raj](https://twitter.com/bh4b3sh) that uses Zeek logs to detect the default Cobalt Strike certificate.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-30.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-30.png)


[RDP over Reverse SSH Tunnel WFP](https://github.com/SigmaHQ/sigma/blob/eb382c4a59b6d87e186ee269805fe2db2acf250e/rules/windows/builtin/security/win_rdp_reverse_tunnel.yml) by [Samir Bous](blank)[seaden](blank) is a rule that can look for suspicious RDP activity using reverse tunneling.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-31.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-31.png)


[CobaltStrike Malleable Amazon Browsing Traffic Profile](https://github.com/SigmaHQ/sigma/blob/master/rules/proxy/proxy_cobalt_amazon.yml) by [Markus Neis](https://twitter.com/markus_neis) which looks at proxy logs for the Amazon Malleable profile.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-32.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-32.png)


Other malleable profile rules include [CobaltStrike Malformed UAs in Malleable Profiles](https://github.com/SigmaHQ/sigma/blob/master/rules/proxy/proxy_cobalt_malformed_uas.yml), [CobaltStrike Malleable (OCSP) Profile](https://github.com/SigmaHQ/sigma/blob/master/rules/proxy/proxy_cobalt_ocsp.yml), and [CobaltStrike Malleable OneDrive Browsing Traffic Profile](https://github.com/SigmaHQ/sigma/blob/master/rules/proxy/proxy_cobalt_onedrive.yml).


All Sigma rules here are documented towards the bottom of [Part 1](https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/).


### **Rita**


Rita stands for Real Intelligence Threat Analytics (RITA), developed by [Active Countermeasures](https://www.activecountermeasures.com/). Rita is a framework for detecting command and control communication. It takes Zeek logs data and can, in our experience, accurately detect beaconing activity. 


One of the great features of Rita is its ease of use and detailed output information in various forms, including CSV and HTML. One simply can point Rita to the Zeek logs and wait for the results. The more available data, the more precise the results will be. Zeek logs can be generated from the PCAP(s).


The screenshot samples below show the results created by Rita based on the traffic we used in the previous sections to demonstrate the jquery malleable C2 profile.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-33.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-33.png)


We left the Beacon running for an hour to simulate an actual infection while several other network-unrelated processes ran in the background. During this hour, we tasked the Beacon with carrying out several commands. Rita determined that one hour of network data was adequate for identifying the beacon link and assigning it the highest score. Although, the more data you have, the more accurate the results will be.


Below, we can see the results from one of our recent cases, [BazarLoader and the Conti Leaks](https://thedfirreport.com/2021/10/04/bazarloader-and-the-conti-leaks/). The first three IP addresses relate to the CS servers with which the Beacon communicated.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-34.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-34.png)


Rita accurately identified beaconing activity related to Cobalt Strike C2 communication. Using Rita, we can identify malicious C2 traffic based on multiple variables, including communication frequency, average bytes sent/received, number of connections etc. As a result, we can detect Cobalt Strike beaconing regardless of the malleable C2 profile utilized or any additional jitter present.


### **JA3/JA3S**


JA3 is an open-source project created by [John Althouse](https://www.linkedin.com/in/johnalthouse/), [Jeff Atkinson](https://www.linkedin.com/in/annh/) and [Josh Atkins](https://www.linkedin.com/in/joshratkins/). JA3/JA3S can create SSL fingerprints for communication between clients and servers. The unique signatures can represent several values collected from fields in the Client Hello packet:



```
- SSL Version
- Accepted Ciphers
- List of Extensions
- Elliptic Curves
- Elliptic Curve Formats
```

For more information on how JA3 works, you can visit the official GitHub repository here: <https://github.com/salesforce/ja3>.


The JA3 tool is used to generate a signature for the client-side beacon connection with the server. JA3S, on the other hand, is able to generate a server fingerprint. The combination of the two can produce the most accurate result. JA3S can capture the full cryptographic communication and combine the JA3 findings to generate the signature.


The downside of this method is that it can produce inaccurate results if the Cobalt Strike is behind redirectors.


We can find many [reports](https://thedfirreport.com/?s=72a589da586844d7f0818ce684948eea) that contain the JA3 value that corresponds to the Cobalt Strike fingerprint. When it comes to Cobalt Strike infrastructure, the known JA3 and JA3s signatures that we are looking for are:


**JA3**


* 72a589da586844d7f0818ce684948eea
* a0e9f5d64349fb13191bc781f81f42e1


**JA3s**


* b742b407517bac9536a77a7b0fee28e9


By using JA3/S signatures, we can discover various malware C2 servers and not just Cobalt Strike. Salesforce provides a thorough collection of signatures that belong to many different applications [here](https://github.com/salesforce/ja3/tree/master/lists). Some other example signatures with well known JA3 fingerprints are:


* Trickbot: 6734f37431670b3ab4292b8f60f29984
* AsyncRat: fc54e0d16d9764783542f0146a98b300
* Dridex: 51c64c77e60f3980eea90869b68c58a8
* JA3 of Python usually hosting Empire or PoshC2: db42e3017c8b6d160751ef3a04f695e7
* TOR client: e7d705a3286e19ea42f587b344ee6865


Another very good website to test the JA3 signature against a large database is [ja3er](https://ja3er.com).


### **JARM**


Similar to JA3/JA3S, JARM has the ability to fingerprint the TLS values of the remote server. It does this by interacting with the target server sending 10 TLS Client Hello packets and recording the specific attributes from the replies. It will then hash the result values and create the final JARM fingerprint.


Unlike JA3/S, JARM is an active way of fingerprinting remote server applications. [John Althouse](https://twitter.com/4a4133?lang=en) has created a [medium post](https://medium.com/@jalthouse/great-question-11aa555f6b28) that accurately conveys the differences between JA3/S and JARM:


*“JARM actively scans the server and builds a fingerprint of the server application. Whereas JA3/S is passive, just listening, not reaching out, JARM is active, actively probing the target. And is able to build a fingerprint of the server application where JA3S could not.”*


According to research and further changes on the JAVA TLS version as mentioned below, the JARM fingerprint that corresponds to a default configuration of the Cobalt Strike is:


* *07d14d16d21d21d00042d41d00041de5fb3038104f457d92ba02e9311512c2*


Cobalt Strike is dependent on Java to run both the client graphical user interface (GUI) and the team server. When we scan a Cobalt Strike server using JARM, the results we get back are dependent on the Java version that is used. According to Cobalt Strike’s [documentation](https://www.cobaltstrike.com/help-java-dependency), OpenJDK 11 is the preferred version that needs to be installed by the operators. This makes it easier to identify a potential Cobalt Strike server, however, defenders should be aware that this outcome alone is prone to false positives. This is because many other legitimate servers on the internet use this version of Java to operate their web applications.


On April 20th, 2021 Java Disabled TLS 1.0 and TLS 1.1 in favor of TLS 1.2 or above. Following this change, the JARM fingerprint for Cobalt Strike servers changed:


From: *07d14d16d21d21d07c42d41d00041d24a458a375eef0c576d23a7bab9a9fb1*


To: *07d14d16d21d21d00042d41d00041de5fb3038104f457d92ba02e9311512c2*


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-35.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-35.png)


This change was highlighted by [@bodziurity](https://twitter.com/bodziurity) and [@WLesicki](https://twitter.com/WLesicki) in a collaborative effort:


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-36.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-36.png)


Cobalt Strike has a [post](https://blog.cobaltstrike.com/2020/12/08/a-red-teamer-plays-with-jarm/) dedicated to JARM that goes into detail on how JARM works and how the specific hash value is created based on the Java version.


Looking into our reporting for this hash value will return four of our [cases](https://thedfirreport.com/?s=07d14d16d21d21d07c42d41d00041d24a458a375eef0c576d23a7bab9a9fb1). All these cases involve Cobalt Strike as the post-exploitation method.


To generate a JARM fingerprint against a server, you can run the [JARM python tool](https://github.com/salesforce/jarm):



```
python3 jarm.py [target] -p [port]
```

[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-1.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-1.png)
While JARM’s offer another tool to help reveal adversary infrastructure they are not an indicator that can be used in isolation. JARM signatures can be masked, Dagmawi Mulugeta presented at [HiTB Amsterdam in 2021](https://conference.hitb.org/hitbsecconf2021ams/materials/D2%20COMMSEC%20-%20JARM%20Randomizer%20Evading%20JARM%20Fingerprinting%20-%20Dagmawi%20Mulugeta.pdf) a tool that enables red teams or adversaries to mask the JARM signatures of their infrastructure. Called [JARM Randomizer](https://github.com/netskopeoss/jarm_randomizer) the tool can be configured as a proxy in front of the Cobalt Strike server to serve up false data to potential internet scanners.


Other JARMs can be found at: <https://github.com/cedowens/C2-JARM>.


### **Arkime (Moloch) and JA3/S**


We included [Arkime](https://arkime.com/index#home) as it integrates with JA3/JA3S and other plugins to enhance network analysis. Arkime is a tool that we use a lot to investigate network activity and gather indicators. It can index network traffic and make events easily searchable. 


Arkime is simple to set up and excellent for reviewing traffic. Arkime makes use of additional analysis tools by including them as plugins. More on this and other tools in the next report.


[![](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-2.png)](https://thedfirreport.com/wp-content/uploads/2022/01/cs2-2.png)


All for now
-----------


That wraps up Cobalt Strike, a Defender’s Guide Part 2. Would you like to see something specific in Part 3? Contact us here or on Twitter with suggestions. Thanks for reading and hope this helps!


Please see the bottom of our [first report](https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/) for more detections & rules.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Bazar]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Dridex]] [[action.malware.name=Elise]] [[action.malware.name=Empire]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=PoshC2]] [[action.malware.name=Power Loader]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Systeminfo]] [[action.malware.name=Systeminfo]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Education]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=Amsterdam]] [[victim.country.name=Netherlands]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[C2]] [[Jarm]] [[Smb]] [[Dns]] [[Ja3]] [[Cdn]] [[Screenshot]] [[Rdp]] [[Tls]] [[Ja3/s]] [[The DFIR Report]]
#### ipv4-adresses
190.114.254.116 192.198.86.130 162.244.83.216 23.19.227.147 108.62.118.247 212.114.52.180 127.0.0.1 192.168.88.179 192.168.88.2 192.168.38.102 192.168.38.104
#### urls
https://github.com/salesforce/ja3. https://github.com/cedowens/C2-JARM.
#### MD5-hash
72a589da586844d7f0818ce684948eea a0e9f5d64349fb13191bc781f81f42e1 b742b407517bac9536a77a7b0fee28e9 6734f37431670b3ab4292b8f60f29984 fc54e0d16d9764783542f0146a98b300 51c64c77e60f3980eea90869b68c58a8 db42e3017c8b6d160751ef3a04f695e7 e7d705a3286e19ea42f587b344ee6865

