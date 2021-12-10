# Log4j zero-day gets security fix just as scans for vulnerable systems ramp up
### The Apache Software Foundation has released an emergency security update today to patch a zero-day vulnerability in Log4j, a Java library that provides logging capabilities.

## Information:
+ Source: The Record
+ Link: https://therecord.media/log4j-zero-day-gets-security-fix-just-as-scans-for-vulnerable-systems-ramp-up/
+ Date: 2021-12-10T11:58:42+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2021/12/Apache-Log4J.jpg)

The Apache Software Foundation has released an emergency security update today to patch a zero-day vulnerability in Log4j, a Java library that provides logging capabilities.


The patch—part of the [2.15.0 release](https://logging.apache.org/log4j/2.x/security.html)—fixes a remote code execution vulnerability (**CVE-2021-44228**) disclosed yesterday on Twitter, complete with [proof-of-concept code](https://github.com/tangxiaofeng7/apache-log4j-poc).




> Apache Log4j2 jndi RCE[#apache](https://twitter.com/hashtag/apache?src=hash&ref_src=twsrc%5Etfw) [#rce](https://twitter.com/hashtag/rce?src=hash&ref_src=twsrc%5Etfw)<https://t.co/ZDmc7S9WW7> [pic.twitter.com/CdSlSCytaD](https://t.co/CdSlSCytaD)
> 
> — p0rz9 (@P0rZ9) [December 9, 2021](https://twitter.com/P0rZ9/status/1468949890571337731?ref_src=twsrc%5Etfw)



The vulnerability, also nicknamed **Log4Shell**, can be exploited by forcing Java-based apps and servers, where the Log4j library was used, to log a specific string into their internal systems.


When the app or server processes the logs, this string can force the vulnerable system to download and run a malicious script from an attacker-controlled domain, effectively taking over the vulnerable application/server, according to a [technical breakdown](https://www.lunasec.io/docs/blog/log4j-zero-day/) published yesterday by security firm LunaSec.


With a score of 10/10 on the CVSSv3 severity scale, Log4Shell is as bad as it gets in terms of security flaws, being both remotely exploitable and requiring little technical skill to execute.


### Enormous impact


Discovered during a bug bounty engagement against Minecraft servers, the vulnerability is far more impactful than some might expect, primarily because of Log4j’s near-ubiquitous presence in almost all major Java-based enterprise apps and servers.


For example, Log4j is included with almost all the enterprise products released by the Apache Software Foundation, such as Apache Struts, Apache Flink, Apache Druid, Apache Flume, Apache Solr, Apache Flink, Apache Kafka, Apache Dubbo, and possibly many more.


In addition, other open-source projects like Redis, ElasticSearch, Elastic Logstash, the NSA’s Ghidra, and others also use it in some capacity or other.


Naturally, all the companies that use any of these products are also indirectly vulnerable to the Log4Shell exploit, even if some of them may be aware of it or not.


[According to some research](https://github.com/YfryTchsGD/Log4jAttackSurface) published yesterday, companies with servers confirmed to be vulnerable to Log4Shell attacks include the likes of Apple, Amazon, Twitter, Cloudflare, Steam, Tencent, Baidu, DIDI, JD, NetEase, and possibly thousands more.


### Attacks can be blocked with a config change


According to p0rz9, the Chinese security researcher who first posted the exploit code online, CVE-2021-44228 can only be abused if the **log4j2.formatMsgNoLookups** option in the library’s configuration is set to **false**.


In a conversation today, Heige, the founder and CEO of Chinese security firm KnownSec 404 Team and one of the first researchers to understand the vulnerability’s impact, told *The Record*that today’s Log4j 2.15.0 release basically sets this option to **true** in order to block attacks.


Log4j users who update to the 2.15.0 version but then set this flag back to false will remain vulnerable to attacks. Similarly, Log4j users who can’t update but set the flag to true can block attacks even on older versions.


Unfortunately, this option is set to false by default in old releases, meaning that all past Log4j releases since 2.10.0, when this option was added, are vulnerable by default.




> It’s hard to imagine that Twitter is still so peaceful! The vulnerability of Log4j has a huge impact! ! !
> 
> — heige (@80vul) [December 9, 2021](https://twitter.com/80vul/status/1468988170021011459?ref_src=twsrc%5Etfw)



According to reports from security firms [Bad Packets](https://twitter.com/bad_packets/status/1469225135504650240) and [Greynoise](https://twitter.com/_mattata/status/1469144854672379905), multiple threat actors are already scanning for apps that may be vulnerable to the Log4Shell attack, meaning that server owners will most likely have a very small patch window at their disposal before servers start getting backdoored if they haven’t been already.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Log4j]] [[Log4shell]] [[Apps]] [[The Record]]
#### urls
rcehttps://t.co/ZDmc7S9WW7
#### CVE's
[[CVE-2021-44228]]

