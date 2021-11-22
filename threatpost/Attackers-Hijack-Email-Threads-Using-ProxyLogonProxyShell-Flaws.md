# Attackers Hijack Email Threads Using ProxyLogon/ProxyShell Flaws
### Exploiting Microsoft Exchange ProxyLogon & ProxyShell vulnerabilities, attackers are malspamming replies in existing threads and slipping past malicious-email filters. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176496)
+ Date: November 22, 2021  2:26 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/22134744/ProxyLogon_logo_-_Black-e1637606992968.png)
Attackers are gnawing on the ProxyLogon and ProxyShell vulnerabilities in Microsoft Exchange Server to hijack email chains, by malspamming replies to ongoing email threads, researchers say.


What’s still under discussion: Whether the offensive is delivering SquirrelWaffle, the new email loader that [showed up](https://threatpost.com/squirrelwaffle-loader-malspams-packing-qakbot-cobalt-strike/175775/) in September, or whether SquirrelWaffle is just one piece of malware among several that the campaigns are dropping.


Cisco Talos researchers first [got wind](https://blog.talosintelligence.com/2021/10/squirrelwaffle-emerges.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+feedburner%2FTalos+%28Talos%E2%84%A2+Blog%29) of the SquirrelWaffle malspam campaigns beginning in mid-September, when they saw boobytrapped Microsoft Office documents delivering [Qakbot malware](https://threatpost.com/prolock-ransomware-qakbot-trojan/155828/) and the penetration-testing tool [Cobalt Strike](https://threatpost.com/cobalt-strike-cybercrooks/167368/) – two of the most common threats regularly observed targeting organizations around the world. The Office documents infected systems with SquirrelWaffle in the initial stage of the infection chain.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


SquirrelWaffle campaigns are known for using stolen email threads to increase the chances that a victim will click on malicious links. Those rigged links are tucked into an email reply, similar to how the virulent [Emotet](https://threatpost.com/emotet-takedown-infrastructure-netwalker-offline/163389/) malware – typically spread via malicious emails or text messages – has been known to work.


Slipping Under People’s Noses
-----------------------------


In a [report](https://www.trendmicro.com/en_us/research/21/k/Squirrelwaffle-Exploits-ProxyShell-and-ProxyLogon-to-Hijack-Email-Chains.html) posted on Friday, Trend Micro researchers ​​Mohamed Fahmy, Sherif Magdy and Abdelrhman Sharshar said that hijacking email replies for malspam is a good way to slip past both people’s spam suspicions and to avoid getting flagged or quarantined by email gateways.


“Delivering the malicious spam using this technique to reach all the internal domain users will decrease the possibility of detecting or stopping the attack, as the mail [gateways] will not be able to filter or quarantine any of these internal emails,” they wrote.


The attacker also didn’t drop, or use, tools for lateral movement after gaining access to the vulnerable Exchange servers, Trend Micro said. Thus, they left no tracks, as “no suspicious network activities will be detected. Additionally, no malware was executed on the Exchange servers that will trigger any alerts before the malicious email is spread across the environment.”


Middle East Campaign
--------------------


Trend Micro’s Incident Response team had decided to look into what researchers believe are SquirrelWaffle-related intrusions in the Middle East, to figure out whether the attacks involved the notorious Exchange server vulnerabilities.


They shared a screen capture, shown below, that’s representative of the malicious email replies that showed up in all of the user inboxes of one affected network, all sent as legitimate replies to existing threads, all written in English.


They found that other languages were used in different regions outside of the Middle East attack they examined. Still, in the intrusions they analyzed that were outside of the Middle East, most of the malicious emails were written in English, according to the report.


“With this, the attackers would be able to hijack legitimate email chains and send their malicious spam as replies to the said chains,” the researchers wrote.


Who’s Behind This?
------------------


[Cryptolaemus](https://www.zdnet.com/article/meet-the-white-hat-group-fighting-emotet-the-worlds-most-dangerous-malware/) researcher [TheAnalyst](https://twitter.com/ffforward) disagreed with Trend Micro on its premise that SquirrelWaffle is actually acting as a malware dropper for Qbot or other malwares. Rather, TheAnalyst asserted on Friday that the threat actor is dropping both SquirrelWaffle and Qbot as [discrete payloads](https://twitter.com/ffforward/status/1461810466720825352), and the most recent [confirmed SquirrelWaffle drop](https://twitter.com/ffforward/status/1461810488870944768) it has seen was actually on Oct. 26.



With regards to who’s behind the activity, TheAnalyst said that the actor/activity is tracked as tr01/TR (its QakBot affiliate ID) [TA577](https://twitter.com/hashtag/TA577?src=hashtag_click) by Proofpoint and as ChaserLdr by [Cryptolaemus](https://twitter.com/Cryptolaemus1) and that the activity goes back to at least 2020. The actors are easy to track, TheAnalyst said, given small tweaks to their tactics, techniques and procedures (TTPs).


One such TTP that tr01 favors is adding links to malicious documents included in stolen reply chains, TheAnalyst noted. The threat actor is known to deliver “a multitude of malware,” they said, such as [QakBot](https://threatpost.com/prolock-ransomware-qakbot-trojan/155828/), [Gozi](https://threatpost.com/banking-trojans-nymaim-gozi-merge-to-steal-4m/117412/), [IcedID](https://threatpost.com/icedid-banking-trojan-surges-emotet/165314/), Cobalt Strike and potentially more.


The Old ‘Open Me’ Excel Attachment Trick
----------------------------------------


The malicious emails carried links (aayomsolutions[.]co[.]in/etiste/quasnam[]-4966787 and aparnashealthfoundation[.]aayom.com/quasisuscipit/totamet[-]4966787) that dropped a .ZIP file containing a malicious Microsoft Excel sheet that downloads and executes a malicious DLL related to the [Qbot](https://threatpost.com/ta551-tactics-sliver-red-teaming/175651/) banking trojan.


What’s particularly notable, Trend Micro said, is that real account names from the victim’s domain were used as sender and recipient, “which raises the chance that a recipient will click the link and open the malicious Microsoft Excel spreadsheets,” according to the report.


As shown below, the Excel attachment does [what malicious Excel documents do](https://threatpost.com/hackers-update-age-old-excel-4-0-macro-attack/154898/): It prompts targets to choose “Enable Content” to view a protected file.


Trend Micro offered the chart below, which shows the Excel file infection chain.


The Exchange Tell-Tales
-----------------------


The researchers believe that the actors are pulling it off by targeting users who are relying on Microsoft Exchange servers that haven’t yet been patched for the notorious, [oft-picked-apart](https://threatpost.com/microsoft-exchange-servers-proxylogon-patching/165001/) [ProxyLogon](https://threatpost.com/deadringer-targeted-exchange-servers-before-discovery/168300/) and [ProxyShell](https://threatpost.com/exchange-servers-attack-proxyshell/168661/) vulnerabilities.


Trend Micro found evidence in the IIS logs of three compromised Exchange servers, each compromised in a separate intrusion, all having been exploited via the vulnerabilities [CVE-2021-26855](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26855), [CVE-2021-34473](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473) and [CVE-2021-34523](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34523) – the same CVEs used in ProxyLogon (CVE-2021-26855) and ProxyShell (CVE-2021-34473 and CVE-2021-34523) intrusions, according to Trend Micro.


The IIS log also showed that the threat actor is using a [publicly available](https://github.com/Jumbo-WJB/Exchange_SSRF) exploit in its attack. “This exploit gives a threat actor the ability to get users SID and emails” the researchers explained. “They can even search for and download a target’s emails.”


The researchers shared evidence from the IIS logs, replicated below, that depicts the exploit code.


Microsoft fixed the ProxyLogon vulnerabilities in [March](https://threatpost.com/microsoft-exchange-servers-proxylogon-patching/165001/) and the ProxyShell vulnerabilities in [May](https://threatpost.com/wormable-windows-bug-dos-rce/166057/). Those who’ve applied the [May or July](https://techcommunity.microsoft.com/t5/exchange-team-blog/proxyshell-vulnerabilities-and-your-exchange-server/ba-p/2684705) updates are protected from all of these. Microsoft has [reiterated](https://techcommunity.microsoft.com/t5/exchange-team-blog/proxyshell-vulnerabilities-and-your-exchange-server/ba-p/2684705) that those who’ve applied the ProxyLogon patch released in [March](https://msrc-blog.microsoft.com/2021/03/05/microsoft-exchange-server-vulnerabilities-mitigations-march-2021/) aren’t protected from ProxyShell vulnerabilities and should install the more recent security updates.


How to Fend Off ProxyLogon/ProxyShell Attacks
---------------------------------------------


Exploiting ProxyLogon and ProxyShell enabled the attackers to slip past checks for malicious email, which “highlights how users [play] an important part in the success or failure of an attack,” Trend Micro observed. These campaigns “should make users wary of the different tactics used to mask malicious emails and files,” the researchers wrote.


In other words, just because email comes from a trusted contact is no guarantee that any attachment or link it contains can be trusted, they said.


Of course, patching is the number one way to stay safe, but Trend Micro gave these additional tips if that’s not possible:


***There’s a sea of unstructured data on the internet relating to the latest security threats. REGISTER TODAY to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.*** 




#### Tags:
[[Microsoft]] [[SquirrelWaffle]] [[ProxyLogon]] [[ProxyShell]] [[malware]] [[TheAnalyst]] [[emails]] [[below,]] [[wrote.]] [[Qbot]] [[ThreatPost]]
