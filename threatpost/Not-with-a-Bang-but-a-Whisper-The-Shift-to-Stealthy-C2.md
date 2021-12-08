# Not with a Bang but a Whisper: The Shift to Stealthy C2
### DoH! Nate Warfield, CTO of Prevailion, discusses new stealth tactics threat actors are using for C2, including Malleable C2 from Cobalt Strike's arsenal.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176853
+ Date: 2021-12-08T19:28:35+00:00
+ Author: Nate Warfield


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2019/01/23110846/Hacker-e1638987782327.jpg)

As defensive tools have evolved to detect more and more traditional attack techniques, it should come as no surprise that attackers have shifted tactics. 


This ever-evolving arms race between offensive security toolsets, bespoke advanced persistent threat (APT) malware and the billion-dollar infosec industry is hard to keep up with, so today we’re going to take a closer look at the new tactics threat actors are using for command-and-control (C2) obfuscation. 


**DNS over HTTPS**
------------------


The goal of DNS over HTTPS (DoH) is to increase user privacy and prevent DNS traffic from being eavesdropped on or manipulated by man-in-the-middle (MITM) attacks. The problem with this is, many security controls need the ability to monitor DNS traffic to detect attempts to contact malicious infrastructure. Web browsers started adding support in 2018, and both macOS and Windows now come with built-in support for it.


![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)


By hiding DNS requests inside DoH, attackers can both prevent the interception and blocking of DNS lookups to their infrastructure, but also bury C2 traffic inside encryption which looks exactly like normal encrypted web traffic. It is extremely hard to detect and block this traffic, because security devices frequently look for “uncommon traffic” (TOR, Internet Relay Chat (IRC), etc.) but HTTPS is the standard for nearly all web traffic today. 


**TOR**
-------


The Onion Router (TOR), also called the dark web, was, like DoH, initially designed as a privacy shield. It works by routing traffic through layers of relay nodes  – hence the onion part of its name – which conceal the original IP address of the connecting client. While most of the publicity TOR gets is around darknet marketplaces for drugs, weapons or hacking tools, it’s also been used for C2. 


TOR-based C2 is easier to detect and block than DoH, since many organizations will block the ports it uses (9001, 9030) and security devices can flag it as “uncommon.” However, with the huge numbers of remote working during COVID-19, it’s impossible to deploy these same security controls to remote workers’ home networks.


It’s more complex for attackers to use TOR, as there is no built-in support for it on any operating system, so malware needs to either come packaged with a TOR client or immediately download it as a secondary payload. Complexity, however, is rarely a deterrent to a persistent attacker, so administrators should ensure their endpoint software, firewalls or network policies are blocking the ports that TOR uses, alerting for sudden creation of connections to the TOR network and even educate their users on how to use the firewall features of their home networking equipment to block the ports if they aren’t actively using TOR.


 


**WebSockets**
--------------


WebSockets are a technology – generally in the form of an API – which allow software on a client system to use the web browser to interact with a remote server. By leveraging the existing web browser on a victim system, it removes the need for malware to establish a C2 connection directly. This is powerful, because many endpoint detection and response (EDR) solutions look for activity like an executable being started and then talking outbound to the internet, or for “unlikely behavior” such as an office document downloading from the internet, a .PDF creating a network connection or an executed file suddenly spawning additional processes. 


Detecting C2 over WebSockets is in the same problem space as DoH: There are many perfectly legitimate reasons software will use it – if there weren’t, API support wouldn’t exist. And because the traffic looks identical to normal web traffic – and is most likely encrypted with TLS – there’s no easy way to differentiate safe traffic versus malicious traffic. Upstream proxy servers may be able to look for anomalies like connections to never-before-seen servers, but this is error-prone and easily bypassed by attackers hosting infrastructure on public clouds.


**Malleable C2**
----------------


One of the most powerful and undetectable C2 methods today are Malleable C2 profiles from the Cobalt Strike commercial toolset. Malleable C2 is such a complex topic that an entire article devoted to it would only scratch the surface, but at the most abstract level it operates by supplying the malware payload and C2 server with a special command structure dictating how the malware will communicate. 


All the communication is done via what appear to be normal, perfectly legitimate HTTP headers, so even if the connection isn’t TLS-encrypted, security devices or software can’t tell if the connection is malicious. And, because this configuration can be modified at any time, in any way the attacker chooses, even if a connection can be fingerprinted, the resulting heuristic is easily bypassed.


This also allows attackers to impersonate legitimate websites, because the C2 server is custom configured to interpret headers in ways outside the HTTP specification, what may appear as a normal “Host: www.microsoft.com” host header – evading detection by security controls – is in fact some part of the C2 connection. 


**Telegram**
------------


An [emerging method](https://threatpost.com/magecart-credit-card-skimmer-telegram-c2-channel/158851/) for C2 is the extremely popular chat program Telegram. With more than 500 million monthly users, its popularity and proliferation mean its traffic has become commonplace and no longer “unique” – making it harder to differentiate legitimate from malicious intent. Telegram supports bots, which can be developed to perform any actions the attacker chooses and then packaged into malicious attachments or malware. Another common attack vector is to send a Telegram user a link which when clicked, triggers the malware. 


Telegram C2 is difficult to detect because once again, it runs across standard web ports (443, 80) and encrypts its connections by default. It also has clients for Mac, Windows, iPhone and Android, so it’s an appealing C2 method for cross-platform attacks.


**Adjusting Your Defensive Strategy**
-------------------------------------


There is no silver bullet to detecting these emerging trends in adversarial tactics, and we can expect future techniques will be just as stealthy. 


As new internet tools and applications gain popularity, attackers will attempt to abuse them for their purposes. Detection technologies like antivirus, the “detection and response” tools like EDR/NDR/MDR/XDR, proxy devices and network monitoring systems will always lag behind as they’re predicated on known attack signatures. 


To defend against these tactics, defenders must adopt multi-layered security controls and frequently test these controls. Security validation is an emerging tactic, where real-world attacker techniques are run in a controlled fashion to determine whether the existing controls are effective. And lastly, the first line of defense for any organization is their users; therefore, continued training, education and making security information readily available is imperative to preventing a breach or detecting it early if and when it occurs. 


***Nate Warfield is CTO at [Prevailion](https://www.prevailion.com/).***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[C2]] [[Malware]] [[Dns]] [[Https]] [[Websockets]] [[ThreatPost]]
#### urls
www.microsoft.com”

