# Amazon and Google patch major bug in their DNS-as-a-Service platforms
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/amazon-and-google-patch-major-bug-in-their-dns-as-a-service-platforms/)
+ Date: August 4, 2021
+ Author: Catalin Cimpanu


## Article:
![Amazon and Google patch major bug in their DNS-as-a-Service platforms](https://therecord.media/wp-content/uploads/2021/08/world-map-cyber.jpg)

At the Black Hat security conference today, two security researchers have [disclosed](https://www.blackhat.com/us-21/briefings/schedule/#a-new-class-of-dns-vulnerabilities-affecting-many-dns-as-service-platforms-23563) a security issue impacting hosted DNS service providers that can be abused to hijack the platform’s nodes, intercept some of the incoming DNS traffic, and then map customers’ internal networks.


Discovered by Shir Tamari and Ami Luttwak from cloud security company [Wiz](https://www.wiz.io), the vulnerability highlights the amount of sensitive information collected by managed DNS platforms and their attractiveness from a cyber-espionage and intelligence data collection standpoint.


### How the vulnerability occurs


Also known as DNS-as-a-Service providers, these companies effectively rent DNS servers to corporate entities. While it’s not hard to run your own DNS name server, the benefit of using a service like AWS Route53 or the Google Cloud Platform is that companies can offload managing DNS server infrastructure to a third-party and take advantage of better uptime and top-notch security.


Companies that sign up for a managed DNS provider typically have to onboard their internal domain names with the service provider. This typically means companies have to go to a backend portal and add their *company.com* and other domains to one of the provider’s name servers (i.e., *ns-1611.awsdns-09.co.uk*).


Once this is done, when a company employee wants to connect to an intranet app or an internet website, their computer will query the third-party DNS server for the IP address it needs to connect.


What the Wiz team discovered was that several managed DNS providers did not blacklist their own DNS servers inside their backends.


In an interview last week, Wiz researchers told *The Record* they were able to add the managed DNS provider’s name server itself (i.e., *ns-1611.awsdns-09.co.uk*) inside the backend and point it to their internal network.


This effectively allowed the Wiz team to hijack DNS traffic hitting the hijacked managed DNS provider’s server. However, the Wiz team said they didn’t receive all the DNS traffic going through that server, but only dynamic DNS updates.


These are special DNS messages that workstations send to DNS servers when their IP address inside the internal network, or other details, have changed.


![DDNS-updates](https://www-therecord.recfut.com/wp-content/uploads/2021/08/DDNS-updates-1024x524.png)Image: Wiz
However, the Wiz team said that while they weren’t able to sniff on a company’s real-time DNS traffic, the dynamic DNS updates allowed them to create maps of companies who were using the same managed DNS server and maps of those companies’ internal networks.


#### An intelligence gold mine


While this data looked innocuous, it was not.


Tamari and Luttwak said that in the 14 hours their tests took place, they were able to collect dynamic DNS updates from more than 15,000 organizations, including more than 130 government agencies and many Fortune 500 companies.


The data included internal and external IP addresses for each system, computer names, and in some cases, even employee names.


The two described the collected data as an intelligence gold mine.


The two researchers told *The Record* the data could be used in a wide variety of ways. It could be used to determine the internal structure of high-value companies, identify domain controllers, and then launch cyber-attackers with higher precision than regular spam-and-pray approaches.


For example, the research team was able to identify which company systems were running NAT-protected IPv4 addresses and which were running IPv6 addresses—systems that, by the nature of IPv6, are connected online at all times and exposed to non-stop, direct attacks.


Furthermore, the data could also be used for purposes outside cybersecurity. An intelligence agency could use this data to cross-correlate connections between companies and government agencies and identify government contractors.


In addition, the Wiz team said that after plotting the collected data on a map, they were also able to identify companies that broke OFAC regulations and were doing business in sanctioned countries, such as Iran and the Ivory Coast.


![DNS-endpoint-maps](https://www-therecord.recfut.com/wp-content/uploads/2021/08/DNS-endpoint-maps.jpg)Image: Wiz
#### Amazon and Google roll out updates


The Wiz team said they found three DNS-as-a-Service providers vulnerable to this issue. Two of them, Amazon and Google, have rolled out updates, while a third is in the process of patching it.


In emails this week, both Amazon and Google spokespersons told*The Record* they have fixed the attack vector discovered by Wiz and are now blocking the registration of their own domains names inside their backends.


*The Record* also asked the two companies if they have investigated past incidents where a customer might have abused this bug to collect data on its customers. While an Amazon spokesperson did not respond to this particular inquiry, Google said it has not seen “any evidence of malicious abuse on [their] platform.”


In addition, the Wiz team said they suspect that around a dozen more DNS-as-a-Service providers are most likely vulnerable to similar attacks.


However, the Wiz team said the issue here runs deeper than just providers forgetting to blacklist the registration of their own DNS servers inside their own backends.


The issue here is why dynamic DNS updates are reaching the internet in the first place and why these updates aren’t limited to local networks only.


Here, researchers blamed a default option in Microsoft Windows servers that allows this type of DNS traffic to pass the local network and reach the internet.


Reached out for comment, a Microsoft spokesperson recommended that companies follow the below guides in order to prevent dynamic DNS updates from reaching the internet:


* [Guidance related to enabling secure Windows Server DNS updates](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/configure-dns-dynamic-updates-windows-server-2003)
* [Additional information related to best practices on network security](https://social.technet.microsoft.com/wiki/contents/articles/34981.active-directory-best-practices-for-internal-domain-and-network-names.aspx#Using_a_single_namespace_for_internal_an)





#### Tags:
[[DNS]] [[Google]] [[DNS-as-a-Service]] [[provider’s]] [[IP]] [[backends.]] [[However,]] [[The Record]]
