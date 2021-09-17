# Cyberattacks against the aviation industry linked to Nigerian threat actor
### The investigation began after a Microsoft tweet concerning AsyncRAT.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cyberattacks-against-the-aviation-industry-that-flew-under-the-radar-linked-to-nigerian-threat-actor/)
+ Date: September 17, 2021 -- 09:06 GMT (10:06 BST)
+ Author: Charlie Osborne


## Article:
Unknown

Researchers have unmasked a lengthy campaign against the aviation sector, beginning with the analysis of a Trojan by Microsoft. 


On May 11, Microsoft Security Intelligence published a [Twitter thread](https://twitter.com/MsftSecIntel/status/1392219314535559169) outlining a campaign targeting the "aerospace and travel sectors with spear-phishing emails that distribute an actively developed loader, which then delivers RevengeRAT or AsyncRAT." 

The operator of this campaign used email spoofing to pretend to be legitimate organizations in these industries, and an attached .PDF file included an embedded link, containing a malicious VBScript which would then drop Trojan payloads on a target machine.  

According to Microsoft, the malware was used to spy on victims as well as to exfiltrate data including credentials, screenshots, clipboard, and webcam data.  

Microsoft's security team has been [monitoring the campaign](https://www.zdnet.com/article/microsoft-warns-watch-out-for-this-new-malware-that-steals-passwords-webcam-and-browser-data/), and now, Cisco Talos has also contributed its findings on the operation.  

Cisco Talos researchers Tiago Pereira and Vitor Ventura published [a blog post](https://blog.talosintelligence.com/2021/09/operation-layover-how-we-tracked-attack.html) on Thursday documenting the scheme, dubbed "Operation Layover," which has now been linked to an actor that has been active since at least 2013 -- and has been targeting aviation for at least two years.  

In addition to Microsoft's investigation, the cybersecurity company has established connections between this threat actor to campaigns against other sectors, spanning over the past five years. 






When it comes to aviation targets, sample emails containing malicious .PDFs were very similar to those obtained by Microsoft. The emails and .PDF attachments are aviation-themed, with mentions of trip itineraries, flight routing, private jets, quotes, charter requests, cargo details, and more.

Based on passive DNS telemetry, the team believes the threat actor is located in Nigeria, due to 73% of IPs connected to hosts, domains, and the attacks at large originate from this country. Pseudonyms appear to include the handle "Nassief2018" on hacking forums, as well as the monikers "bodmas" and "kimjoy." 

The cybercriminal started by using the off-the-shelf CyberGate malware and does not appear to have gone beyond commercially available code since. The threat actor has [also been linked](https://mobile.twitter.com/sS55752750/status/1393283668962119685) to [crypter](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader) purchases from online forums, email addresses, and phone numbers, although these findings have not been verified.  

CyberGate has since been replaced with AsyncRAT in recent campaigns, with over 50 samples detected that are communicating with a command-and-control (C2) server used by the threat actor. As of now, eight more domains linked to AsyncRAT deployment have been detected, the majority of which were registered over 2021. 

RevengeRAT and AsyncRAT, however, are not the only brands of malware in use. One domain spotted by the team also indicates that the operator is using a variant of njRAT in cyberattacks.   

"Actors that perform smaller attacks can keep doing them for a long period of time under the radar," Cisco Talos says. "However, their activities can lead to major incidents at large organizations. These are the actors that feed the underground market of credentials and cookies, which can then be used by larger groups on activities like big game hunting." 

###  Previous and related coverage

* [First gate-to-gate autonomous airplane flight](https://www.zdnet.com/article/first-gate-to-gate-autonomous-airplane-flight/)  

* [Airlines warn passengers of data breach after aviation tech supplier is hit by cyberattack](https://www.zdnet.com/article/airlines-warn-passengers-of-data-breach-after-aviation-tech-supplier-is-hit-by-cyberattack/)  

* [Sabre Systems IT outage cripples airline operations globally](https://www.zdnet.com/article/sabre-systems-it-outage-cripples-airline-operations-globally/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Microsoft]] [[emails]] [[malware]] [[Talos]] [[ZDNet]]
