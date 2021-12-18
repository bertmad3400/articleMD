# Security firm Blumira discovers major new Log4j attack vector | ZDNet
### A basic Javascript WebSocket connection can trigger a local Log4j remote code attack via a drive-by compromise. Wonderful. Truly wonderful.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/security-firm-blumira-discovers-major-new-log4j-attack-vector/
+ Date: 2021-12-17 17:01:00
+ Author: Steven J. Vaughan-Nichols


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/0c84ecd68a659719b621976a0006d27d26d46eff/2021/12/14/40060811-b946-409f-9848-1f6b5af1a44b/shutterstock-1630979773.jpg?width=770&height=578&fit=crop&auto=webp)

It doesn't rain, but it pours. Previously, one assumption about the 10 out of 10 [Log4j security vulnerability](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/) was that it was limited to exposed vulnerable servers. We were wrong. The security company [Blumira](https://www.blumira.com/) claims to have found a [new, exciting Log4j attack vector](https://www.blumira.com/analysis-log4shell-local-trigger/).


You didn't really want to take this weekend off, did you? Of course not! Instead, you'll be chasing down vulnerable Log4j code ever deeper into your network. According to Blumira, this newly-discovered Javascript [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) attack vector can be exploited through the path of a listening server on their machine or local network. An attacker can simply navigate to a website and trigger the vulnerability. Adding insult to injury, WebSocket connections within the host can be difficult to gain deep visibility into. That means it's even harder to detect this vulnerability and attacks using it.

This vector significantly expands the attack surface. How much so? It can be used on services running as localhost, which are not exposed to a network. This is what we like to call a "Shoot me now" kind of problem. 

Oh, and did I mention? The client itself has no direct control over WebSocket connections. They can silently start when a webpage loads. Don't you love the word "silently" in this context? I know I do. 

WebSockets, for those of you who aren't web developers, are in almost all modern web browsers. They're commonly used for two-way communication functions such as website chat and alerts. They're great at passing timely information back to the browser and allowing the browser to quickly send data back and forth. 

However, WebSockets have their own security risks. WebSockets aren't restricted by same-origin policies like a normal cross-domain HTTP request. Instead,  they expect the webserver to validate a request's origin. In short, they don't come with much in the way of built-in security measures.

As you'd guess from this, WebSockets have been used in attacks before. [WebSockets have been used to attack cable modems](https://www.zdnet.com/article/hundreds-of-millions-of-cable-modems-are-vulnerable-to-new-cable-haunt-vulnerability/) by sending malicious requests. It's [also used by hackers for host fingerprinting and port scanning](https://datatracker.ietf.org/meeting/96/materials/slides-96-saag-1/).






In their proof-of-concept attack, Blumira found that by using one of the many [Java Naming and Directory Interface (JNDI)](https://docs.oracle.com/javase/tutorial/jndi/overview/index.html) exploits that they could trigger via a file path URL using a WebSocket connection to machines with an installed vulnerable Log4j2 library. All that was needed to trigger success was a path request that was started on the web page load. Simple, but deadly. 

Making matters worse, it doesn't need to be localhost. WebSockets allow for connections to any IP. Let me repeat, "Any IP" and that includes private IP space.

Next, as the page loads, it will initiate a local WebSocket connection, hit the vulnerable listening server, and connect out over the identified type of connection based on the JNDI connection string. The researchers saw the most success utilizing Java Remote Method Invocation (RMI). default port 1099., although we are often seeing custom ports used. Simply port scanning, a technique already in the WebSocket hacker handbook,  was the easiest path to a successful attack. Making detecting such attacks even harder, the company found "specific patterns should not be expected as it is easy to trigger traffic passively in the background."

Then, an open port to a local service or a service accessible to the host is found, it can then drop the JNDI exploit string in path or parameters. "When this happens, the vulnerable host calls out to the exploit server, loads the attacker's class, and executes it with java.exe as the parent process." Then the attacker can run whatever he wants. 

Indeed, they already are. As Anurag Gurtu, [StrikeReady](https://www.strikeready.co/)'s chief product officer, observed, "Apparently, a ransomware attack is currently exploiting the Log4Shell vulnerability. It's the [Khonsari ransomware](https://www.zdnet.com/article/khonsari-ransomware-iranian-group-nemesis-kitten-seen-exploiting-log4j/) gang that has built an attack using C# and the .NET framework. After execution, the malware enumerates all mounted drives (other than C:/) and targets user directories including Documents, Videos, Pictures, Downloads, and Desktop. An AES 128 CBC algorithm is used for encryption, and the files are saved with a .khonsari extension."

They're not the only ones. [State-sponsored hackers](https://www.zdnet.com/article/log4j-flaw-now-state-backed-hackers-are-using-bug-as-part-of-attacks-warns-microsoft/) from China, Iran, North Korea, and Turkey; [Cobalt Strike](https://www.zdnet.com/article/this-is-how-the-cobalt-strike-penetration-testing-tool-is-being-abused-by-cybercriminals/); and many others are also exploiting Log4j vulnerabilities. This latest vulnerability simply opens the doors even wider for would-be attackers. 

It will only get worst before it gets better For as [Sophos](https://www.sophos.com/) senior threat researcher Sean Gallagher recently explained to date, Log4Shell attackers have been focused on cryptomining, but this is just a "lull before the storm."

He continued, "We expect adversaries are likely grabbing as much access to whatever they can get right now... to monetize and/or capitalize on it later on. The most immediate priority for defenders is to reduce exposure by patching and mitigating all corners of their infrastructure and investigate exposed and potentially compromised systems." After all, Gallagher concluded, "This vulnerability can be everywhere."

What can you do about this? Blumira suggests the following:

Update all local development efforts, internal applications, and internet-facing environments to [Log4j 2.16](https://logging.apache.org/log4j/2.x/download.html) as soon as possible, before threat actors can weaponize this exploit further. This includes moving any custom applications in their dependency manifests to 2.16 as soon as possible to avoid incidental exploitation. 

You should also look closely at your network firewall and egress filtering. The mission here is to restrict the callback required for the actual exploit to land. Significantly limiting the egress traffic of your endpoints will reduce the risk as you patch your applications. In particular, make sure that only certain machines can send out traffic over 53, 389, 636, and 1099 ports.  All other ports should be blocked. Finally, since weaponized Log4j applications often attempt to call back home to their masters over random high ports, you should block their access to such ports. 

Good luck, get back to work hunting down Log4j libraries and calls and hope that you get as much of your infrastructure as you can batten down before the holidays. 



---

**Related stories:**

* [Log4j: Major IT vendors rush out fixes for this flaw and more ahead of Christmas](https://www.zdnet.com/article/vmware-patches-critical-non-log4j-flaw-as-ibm-cisco-release-log4j-fixes/).
* [Log4j zero-day flaw: What you need to know and how to protect yourself](https://www.zdnet.com/article/log4j-zero-day-flaw-what-you-need-to-know-and-how-to-protect-yourself/).
* [US warns Log4j flaw puts hundreds of millions of devices at risk](https://www.zdnet.com/article/log4j-flaw-puts-hundreds-of-millions-of-devices-at-risk-says-us-cybersecurity-agency/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Asia]] [[victim.country.name=Turkey]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Websocket]] [[Websockets]] [[Blumira]] [[Ip]] [[ZDNet]]
#### urls
C:/)

