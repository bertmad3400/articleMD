# Exchange Servers Under Active Attack via ProxyShell Bugs
### There’s an entirely new attack surface in Exchange, a researcher revealed at Black Hat, and threat actors are now exploiting servers vulnerable to the RCE bugs. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168661)
+ Date: August 13, 2021  2:56 pm
+ Author: Lisa Vaas


## Article:
Researchers’ Microsoft Exchange server honeypots are being actively exploited via ProxyShell: The name of an attack disclosed at Black Hat last week that chains three vulnerabilities to enable unauthenticated attackers to perform remote code execution (RCE) and snag plaintext passwords.


In his Black Hat [presentation](https://www.blackhat.com/us-21/briefings/schedule/#proxylogon-is-just-the-tip-of-the-iceberg-a-new-attack-surface-on-m) last week, Devcore principal security researcher [Orange Tsai](https://twitter.com/orange_8361) said that a survey shows more than 400,000 Exchange servers on the internet that are exposed to the attack via port 443. On Monday, the SANS Internet Storm Center’s Jan Kopriva [reported](https://isc.sans.edu/forums/diary/ProxyShell+how+many+Exchange+servers+are+affected+and+where+are+they/27732/) that he found more than 30,000 vulnerable Exchange servers via a Shodan scan and that any threat actor worthy of that title would find it a snap to pull off, given how much information is available.


Going by calculations tweeted by security researcher Kevin Beaumont, this means that, between ProxyLogon and ProxyShell, “just under 50 percent of internet-facing Exchange servers” are currently vulnerable to exploitation, according to a Shodan search.



> 
> Breakdown of Exchange servers on Shodan vulnerable to ProxyShell or ProxyLogon, it's just under 50% of internet facing Exchange servers. [pic.twitter.com/3samyNHBpB](https://t.co/3samyNHBpB)
> 
> 
> — Kevin Beaumont (@GossiTheDog) [August 13, 2021](https://twitter.com/GossiTheDog/status/1426207905779527682?ref_src=twsrc%5Etfw)
> 
> 



On the plus side, Microsoft has already released patches for all of the vulnerabilities in question, and, cross your fingers, “chances are that most organizations that take security at least somewhat seriously have already applied the patches,” Kopriva wrote.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The vulnerabilities affect Exchange Server 2013, 2016 and 2019.


On Thursday, Beaumont and NCC Group’s vulnerability researcher Rich Warren disclosed that threat actors have exploited their Microsoft Exchange honeypots using the ProxyShell vulnerability.


“Started to see in the wild exploit attempts against our honeypot infrastructure for the Exchange ProxyShell vulnerabilities,” Warren tweeted, along with a screen capture of the code for a c# aspx webshell dropped in the /aspnet\_client/ directory.



> 
> Started to see in the wild exploit attempts against our honeypot infrastructure for the Exchange ProxyShell vulnerabilities. This one dropped a c# aspx webshell in the /aspnet\_client/ directory: [pic.twitter.com/XbZfmQQNhY](https://t.co/XbZfmQQNhY)
> 
> 
> — Rich Warren (@buffaloverflow) [August 12, 2021](https://twitter.com/buffaloverflow/status/1425831100157349890?ref_src=twsrc%5Etfw)
> 
> 



Beaumont [tweeted](https://twitter.com/GossiTheDog/status/1425844380376735746) that he was seeing the same and connected it to Tsai’s talk: “Exchange ProxyShell exploitation wave has started, looks like some degree of spraying. Random shell names for access later. Uses foo name from @orange\_8361’s initial talk.”



> 
> Exchange ProxyShell exploitation wave has started, looks like some degree of spraying. Random shell names for access later. Uses foo name from [@orange\_8361](https://twitter.com/orange_8361?ref_src=twsrc%5Etfw)'s initial talk.
> 
> 
> — Kevin Beaumont (@GossiTheDog) [August 12, 2021](https://twitter.com/GossiTheDog/status/1425844380376735746?ref_src=twsrc%5Etfw)
> 
> 



Dangerous Skating on the New Attack Surface
-------------------------------------------


In [a post](https://devco.re/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-1-ProxyLogon/) on Sunday, Tsai recounted the in-the-wild ProxyLogon proof of concept that Devco reported to MSRC in late February, explaining that it made the researchers “as curious as everyone after eliminating the possibility of leakage from our side through a thorough investigation.


“With a clearer timeline appearing and more discussion occurring, it seems like this is not the first time that something like this happened to Microsoft,” he continued. Mail server is both a highly valuable asset and a seemingly irresistible target for attackers, given that it holds businesses’ confidential secrets and corporate data.


“In other words, controlling a mail server means controlling the lifeline of a company,” Tsai explained. “As the most common-use email solution, Exchange Server has been the top target for hackers for a long time. Based on our research, there are more than four hundred thousands Exchange Servers exposed on the Internet. Each server represents a company, and you can imagine how horrible it is while a severe vulnerability appeared in Exchange Server.”


During his Black Hat presentation, Tsai explained that the new attack surface his team discovered is based on “a significant change in Exchange Server 2013, where the fundamental protocol handler, Client Access Service (CAS), splits into frontend and backend” – a change that incurred “quite an amount of design” and yielded eight vulnerabilities, consisting of server-side bugs, client-side bugs and crypto bugs.


He chained the bugs into three attack vectors: The now-infamous [ProxyLogon](https://threatpost.com/microsoft-exchange-exploits-ransomware/164719/) that induced [patching frenzy](https://threatpost.com/microsoft-exchange-servers-proxylogon-patching/165001/) a few months back, the ProxyShell vector that’s now under active attack, and another vector called ProxyOracle.


“These attack vectors enable any unauthenticated attacker to uncover plaintext passwords and even execute arbitrary code on Microsoft Exchange Servers through port 443, which is exposed to the Internet by about 400,000 Exchange Servers,” according to the presentation’s introduction.


The three Exchange vulnerabilities, all of which are [patched](https://threatpost.com/microsoft-crushes-116-bugs/167764/), that Tsai chained for the ProxyShell attack:


ProxyShell earned the Devcore team a $200,000 bounty after they used the bugs to take over an Exchange server at the [Pwn2Own 2021](https://twitter.com/thezdi/status/1379467992862449664) contest in April.


During his Black Hat talk, Tsai said that he discovered the Exchange vulnerabilities when targeting the Microsoft Exchange CAS attack surface. As Tsai explained, CAS is “a fundamental component” of Exchange.


He referred to [Microsoft’s documentation](https://docs.microsoft.com/en-us/exchange/architecture/architecture?view=exchserver-2019), which states:


“Mailbox servers contain the Client Access services that accept client connections for all protocols. These frontend services are responsible for routing or proxying connections to the corresponding backend services on a Mailbox server.”


“From the narrative you could realize the importance of CAS, and you could imagine how critical it is when bugs are found in such infrastructure. CAS was where we focused on, and where the attack surface appeared,” Tsai wrote. “CAS is the fundamental component in charge of accepting all the connections from the client side, no matter if it’s HTTP, POP3, IMAP or SMTP, and proxies the connections to the corresponding backend service.”


ProxyShell Just the ‘Tip of the Iceberg’
----------------------------------------


Out of all the bugs he found in the new attack surface, Tsai dubbed [CVE-2020-0688](https://www.zerodayinitiative.com/blog/2020/2/24/cve-2020-0688-remote-code-execution-on-microsoft-exchange-server-through-fixed-cryptographic-keys) (an RCE vulnerability that involved a hard-coded cryptographic key in Exchange) the “most surprising.”


“With this hard-coded key, an attacker with low privilege can take over the whole Exchange Server,” he wrote. “And as you can see, even in 2020, a silly, hard-coded cryptographic key could still be found in an essential software like Exchange. This indicated that Exchange is lacking security reviews, which also inspired me to dig more into the Exchange security.”


But the “most interesting” flaw is [CVE-2018-8581](https://www.zerodayinitiative.com/blog/2018/12/19/an-insincere-form-of-flattery-impersonating-users-on-microsoft-exchange), he said, which was disclosed by someone who cooperated with ZDI. Though it’s a “simple” server-side request forgery (SSRF), it could be combined with NTLM Relay, enabling the attacker to “turn a boring SSRF into [something really fancy,” Tsai said.](https://dirkjanm.io/abusing-exchange-one-api-call-away-from-domain-admin/)


For example, it could “directly control the whole Domain Controller through a low-privilege account,” Tsai said.


Autodiscover Figures into ProxyShell
------------------------------------


As [BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-servers-are-getting-hacked-via-proxyshell-exploits/) reported, during his presentation, Tsai explained that one of the components of the ProxyShell attack chain targets the Microsoft Exchange [Autodiscover](https://docs.microsoft.com/en-us/exchange/architecture/client-access/autodiscover?view=exchserver-2019) service: a service that eases configuration and deployment by providing clients access to Exchange features with minimal user input.


Tsai’s talk evidently triggered a wave of scanning for the vulnerabilities by attackers.


After watching the presentation, other security researchers replicated the ProxyShell exploit. The day after Tsai’s presentation, last Friday, PeterJson and Nguyen Jang [published](https://peterjson.medium.com/reproducing-the-proxyshell-pwn2own-exploit-49743a4ea9a1) more detailed technical information about their successful reproduction of the exploit.


Soon after, Beaumont [tweeted](https://twitter.com/GossiTheDog/status/1422178411385065476?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1422178411385065476%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.bleepingcomputer.com%2Fnews%2Fmicrosoft%2Fmicrosoft-exchange-servers-scanned-for-proxyshell-vulnerability-patch-now%2F) about a threat actor who was probing his Exchange honeypot using the [Autodiscover service](https://docs.microsoft.com/en-us/exchange/architecture/client-access/autodiscover?view=exchserver-2019). As of yesterday, Aug. 12, those servers were being targeted using autodiscover.json, he tweeted.



> 
> Exchange ProxyShell exploitation wave has started, looks like some degree of spraying. Random shell names for access later. Uses foo name from [@orange\_8361](https://twitter.com/orange_8361?ref_src=twsrc%5Etfw)'s initial talk.
> 
> 
> — Kevin Beaumont (@GossiTheDog) [August 12, 2021](https://twitter.com/GossiTheDog/status/1425844380376735746?ref_src=twsrc%5Etfw)
> 
> 



As of Thursday, ProxyShell was dropping a 265K webshell – the minimum file size that can be created via ProxyShell due to its use of the Mailbox Export function of Exchange Powershell to create PST files – to the ‘c:\inetpub\wwwroot\aspnet\_client\’ folder. Warren shared a sample with BleepingComputer that showed that the webshells consist of “a simple authentication-protected script that the threat actors can use to upload files to the compromised Microsoft Exchange server.”


Bad Packets told the outlet that as of Thursday, was seeing threat actors scanning for vulnerable ProxyShell devices from IP addresses in the U.S., Iran and the Netherlands, using the domains @abc.com and @1337.com, from the known addresses 3.15.221.32 and 194.147.142.0/24.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[ProxyShell]] [[Tsai]] [[Microsoft]] [[presentation,]] [[Shodan]] [[ProxyLogon]] [[(@GossiTheDog)]] [[wrote.]] [[Thursday,]] [[webshell]] [[ThreatPost]]
