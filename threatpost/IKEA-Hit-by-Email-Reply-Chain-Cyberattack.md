# IKEA Hit by Email Reply-Chain Cyberattack
### IKEA, king of furniture-in-a-flat-box, warned employees on Friday that an ongoing cyberattack was using internal emails to malspam malicious links in active email threads. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176625)
+ Date: November 29, 2021  4:22 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/29155618/ikea-scaled-e1638219440979.jpeg)
As of Friday – as in, shopping-on-steroids Black Friday – retail titan IKEA was wrestling with a then-ongoing reply-chain email phishing attack in which attackers were malspamming replies to stolen email threads.


[BleepingComputer](https://www.bleepingcomputer.com/news/security/ikea-email-systems-hit-by-ongoing-cyberattack/) got a look at internal emails – one of which is replicated below – that warned employees of the attack, which was targeting the company’s internal email inboxes. The phishing emails were coming from internal IKEA email addresses, as well as from the systems compromised at the company’s suppliers and partners.



> “There is an ongoing cyberattack that is targeting Inter IKEA mailboxes. Other IKEA organisations, suppliers, and business partners are compromised by the same attack and are further spreading malicious emails to persons in Inter IKEA.
> 
> 
> “This means that the attack can come via email from someone that you work with, from any external organisation, and as reply to an already ongoing conversation. It is therefore difficult to detect, for which we ask you to be extra cautious.” –IKEA internal email to employees.
> 
> 


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

IKEA didn’t immediately respond to Threatpost’s request for comment. Hence, it’s unclear if the attack carried through the weekend and into Monday.


IKEA sent its employees an example phishing email, shown below, that was received in Microsoft Outlook. The company’s IT teams reportedly pointed out that the reply-chain emails contain links ending with seven digits. Employees were warned against opening the emails, regardless of who sent them, and were asked to immediately report the phishing emails to the IT department if they receive them.


Exchange Server Attacks Déjà Vu?
--------------------------------


The attack sounds familiar: Earlier this month, Trend Micro published a [report](https://www.trendmicro.com/en_us/research/21/k/Squirrelwaffle-Exploits-ProxyShell-and-ProxyLogon-to-Hijack-Email-Chains.html) about attackers who were doing the same thing with replies to hijacked email threads. The attackers were gnawing on the ProxyLogon and ProxyShell vulnerabilities in Microsoft Exchange Server to hijack email chains, by malspamming replies to ongoing email threads and hence boosting the chance that their targets would click on malicious links that lead to malware infection.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


As security experts have noted, hijacking email replies for malspam campaigns is a good way to slip past people’s spam suspicions and to avoid getting flagged or quarantined by email gateways.


What was still under discussion at the time of the Trend Micro report: Whether the offensive was delivering SquirrelWaffle, the new email loader that [showed up](https://threatpost.com/squirrelwaffle-loader-malspams-packing-qakbot-cobalt-strike/175775/) in September, or whether SquirrelWaffle was just one piece of malware among several that the campaigns were dropping.


Cisco Talos researchers first [got wind](https://blog.talosintelligence.com/2021/10/squirrelwaffle-emerges.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+feedburner%2FTalos+%28Talos%E2%84%A2+Blog%29) of the SquirrelWaffle malspam campaigns beginning in mid-September, when they saw boobytrapped Microsoft Office documents delivering [Qakbot malware](https://threatpost.com/prolock-ransomware-qakbot-trojan/155828/) and the penetration-testing tool [Cobalt Strike](https://threatpost.com/cobalt-strike-cybercrooks/167368/) – two of the most common threats regularly observed targeting organizations around the world. The Office documents infected systems with SquirrelWaffle in the initial stage of the infection chain.


SquirrelWaffle campaigns are known for using stolen email threads to increase the chances that a victim will click on malicious links. Those rigged links are tucked into an email reply, similar to how the virulent [Emotet](https://threatpost.com/emotet-takedown-infrastructure-netwalker-offline/163389/) malware – typically spread via malicious emails or text messages – has been known to work.


Trend Micro’s incident-response team had decided to look into what its researchers believed were SquirrelWaffle-related intrusions in the Middle East, to figure out whether the attacks involved the notorious, [oft-picked-apart](https://threatpost.com/microsoft-exchange-servers-proxylogon-patching/165001/) [ProxyLogon](https://threatpost.com/deadringer-targeted-exchange-servers-before-discovery/168300/) and [ProxyShell](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) Exchange server vulnerabilities.


Their conclusion: Yes, the intrusions were linked to ProxyLogon and ProxyShell attacks on unpatched Exchange servers, as evidenced by the IIS logs of three compromised servers, each compromised in a separate intrusion, all having been exploited via the ProxyShell and ProxyLogon vulnerabilities [CVE-2021-26855](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26855), [CVE-2021-34473](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473) and [CVE-2021-34523](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523).


In the Middle East campaign that Trend Micro analyzed, the phishing emails contained a malicious Microsoft Excel doc that did [what malicious Excel documents do](https://threatpost.com/hackers-update-age-old-excel-4-0-macro-attack/154898/): It prompted targets to choose “Enable Content” to view a protected file, thus launching the infection chain.


Since IKEA hasn’t responded to media inquiries, it’s impossible to say for sure whether or not it has suffered a similar attack. However, there are yet more similarities between the IKEA attack and the Middle East attack analyzed by Trend Micro earlier this month. Specifically, as BleepingComputer reported, the IKEA reply-email attack is likewise deploying a malicious Excel document that similarly instructs recipients to “Enable Content” or “Enable Editing” to view it.


Trend Micro shared a screen capture, shown below, of how the malicious Excel document looked in the Middle East campaign:


You Can’t Trust Email from ‘Someone You Know’
---------------------------------------------


It’s easy to mistake the malicious replies as coming from legitimate senders, given that they pop up in ongoing email threads. Saryu Nayyar, CEO of Gurucul, noted that IKEA employees are learning the hard way that replies in threads aren’t necessarily legitimate and can be downright malicious.


“If you get an email from someone you know, or that seems to continue an ongoing conversation, you are probably inclined to treat it as legitimate,” she told Threatpost via email on Monday. “However, IKEA employees are finding out otherwise. They are being attacked by phishing emails that are often purportedly from known sources, and may be carrying the Emotet or Qbot trojans to further infect the system and network.”


This attack is “particularly insidious,” she commented, in that it “seemingly continues a pattern of normal use.”


No More Ignoring Quarantine
---------------------------


With such “normal use” patterns lulling would-be victims into letting down their guards, it raises the possibility that employees might assume that email filters were mistaken if they quarantined the messages.


Thus, IKEA’s internal email advised employees that its IT department was disabling the ability to release emails from quarantine. As it is, its email filters were identifying at least some of the malicious emails:



> “Our email filters can identify some of the malicious emails and quarantine them. Due to that the email could be a reply to an ongoing conversation, it’s easy to think that the email filter made a mistake and release the email from quarantine. We are therefore until further notice disabling the possibility for everyone to release emails from quarantine.” –IKEA internal email to employees.
> 
> 


Is Training a Waste of Time?
----------------------------


With such sneaky attacks as these, is training pointless? Some say yes, some say no.


Erich Kron, security awareness advocate at [KnowBe4](https://u7061146.ct.sendgrid.net/ls/click?upn=4tNED-2FM8iDZJQyQ53jATUavSzE-2FiwjSkZ-2BMZMLjTD68bBzltWsjOj4iPYBhQEjDkwmuP_q07lK5GAAVvAnbc-2Fr-2FBDhAPhoMvwzp-2Bdh4wgfTcF0AUhu01ZMXdKNJrsN0iCyDU7ehW0N22Ype9yCK1TM6XYzZcULka2hXrkxot-2FYcsNMOW-2Fi7ZSbc4BW4Y4w5w74JadqFiCZdgYU0Y0aYb-2FD61SsSN5WSYToKPBxI2VArzhMwftrf78GbiRjwM9LzhmNBFfpMuXBsqYiKB-2B-2F-2BBM3106r2sgW-2Be451MnVYlMzEVQ43u-2Fx2JCoSpeITOcIPo6Gi3VBNSVcUaapZzArkSDh5SZ2Cih-2F-2FVdRBgHXCsqyWXs7po0-2FS83TsiYRB3U8HOgtt0HT6BGdSMjxi-2FVc6P1ZgVny6ZGKAKxbHvydLCfU5zrtFQ-3D), is pro-training, particularly given how damaging these attacks can be.


“Compromised email accounts, especially those from internal email systems with access to an organization’s contact lists, can be very damaging, as internal emails are considered trusted and lack the obvious signs of phishing that we are used to looking for,” he told Threatpost via email on Monday. “Because it is from a legitimate account, and because cybercriminals often inject themselves into previous legitimate conversations, these can be very difficult to spot, making them very effective.


“These sorts of attacks, especially if the attackers can gain access to an executive’s email account, can be used to spread ransomware and other malware or to request wire transfers to cybercriminal-owned bank accounts, among other things,” Kron said.


He suggested training employees not to blindly trust emails from an internal source, but to hover over links and to consider the context of the message. “If it does not make sense or seems unusual at all, it is much better to pick up the phone and quickly confirm the message with the sender, rather than to risk a malware infection or falling victim to a scam,” he said.”


In contrast, Christian Espinosa, managing director of [Cerberus Sentinel](https://u7061146.ct.sendgrid.net/ls/click?upn=4tNED-2FM8iDZJQyQ53jATUc1h7F6EeKyqQHDAzxY6FeBG4AZ1lNaZ-2Fme9HKLAKT7PeL3x_q07lK5GAAVvAnbc-2Fr-2FBDhAPhoMvwzp-2Bdh4wgfTcF0AUhu01ZMXdKNJrsN0iCyDU7ehW0N22Ype9yCK1TM6XYzZcULka2hXrkxot-2FYcsNMOW-2Fi7ZSbc4BW4Y4w5w74JadqFiCZdgYU0Y0aYb-2FD61SsSN5WSYToKPBxI2VArzhMwftrf78GbiRjwM9LzhmNBFfpMuXBsqYiKB-2B-2F-2BBM3106r8Wex0T7OFTT8vFIbMA9T-2BlDgGhDFXEelC-2FWPjZXKe9NWtbBbYafHTvkVre5k1vKi3GgofOJKSR-2F2xlpyW7kQklpPEA59unEm4rAKnCodaK-2FrXGwLA5yk9gY1MBMzuyaJeG4mVY1yL-2F3YI1d-2BMmcWiY-3D), is a firm vote for the “training is pointless” approach.


“It should be evident by now that awareness and phishing training is ineffective,” he told Threatpost via email on Monday. “It’s time we accept ‘users’ will continuously fall for phishing scams, despite how much ‘awareness training’ we put them through.”


But what options do we have? Espinosa suggested that cybersecurity defense playbooks “should focus on items that reduce risk, such as application whitelisting, which would have stopped this attack, as the ‘malware’ would not be whitelisted.”


He pointed to other industries that have compensated for human factors, such as transportation. “Despite awareness campaigns, the transportation industry realized that many people did not ‘look’ before turning across traffic at a green light,” Espinosa said. “Instead of blaming the drivers, the industry changed the traffic lights. The newer lights prevent drivers from turning across traffic unless there is a green arrow.”


This change saved thousands of lives, he said, and it’s high time that the cybersecurity industry similarly “takes ownership.”


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** [***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This*** [***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***for the LIVE event!***




#### Tags:
[[emails]] [[IKEA]] [[phishing]] [[malware]] [[Threatpost]] [[it’s]] [[Monday.]] [[Microsoft]] [[ProxyLogon]] [[ProxyShell]] [[ThreatPost]]
