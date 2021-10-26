# SquirrelWaffle Loader Malspams, Packing Qakbot, Cobalt Strike
### Say hello to what could be the next big spam player: SquirrelWaffle, which is spreading with increasing frequency via spam campaigns and infecting systems with a new malware loader. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175775)
+ Date: October 26, 2021  6:25 pm
+ Author: Lisa Vaas


## Article:
SquirrelWaffle, a new malware loader, is mal-spamming malicious Microsoft Office documents to deliver [Qakbot malware](https://threatpost.com/prolock-ransomware-qakbot-trojan/155828/) and the penetration-testing tool [Cobalt Strike](https://threatpost.com/cobalt-strike-cybercrooks/167368/) – two of the most common threats regularly observed targeting organizations around the world.


Cisco Talos researchers [said](https://blog.talosintelligence.com/2021/10/squirrelwaffle-emerges.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+feedburner%2FTalos+%28Talos%E2%84%A2+Blog%29) on Tuesday that they got wind of the malspam campaigns beginning in mid-September, when they saw the boobytrapped Office documents working to infect systems with SquirrelWaffle in the initial stage of the infection chain.


The campaigns are using stolen email threads to come off as replies in those threads, similar to how the virulent [Emotet](https://threatpost.com/emotet-takedown-infrastructure-netwalker-offline/163389/) malware – typically spread via malicious emails or text messages – works. “The campaigns themselves feature several similar characteristics to the campaigns previously seen associated with established threats like Emotet,” Cisco Talos researchers explained.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Due to the prevalence of these campaigns, organizations should be aware of SQUIRRELWAFFLE and the way it could be used by attackers to further compromise corporate networks,” they advised.


The SquirrelWaffle emails typically contain hyperlinks to malicious ZIP archives being hosted on attacker-controlled web servers, researchers said. An example of one of the malspam emails is shown below.


Most of the messages – 76 percent – are written in English. But the language used in the reply message shifts to match what was used in the original email thread, “demonstrating that there is some localization taking place dynamically,” Cisco Talos said. Besides English, the top five languages being used also include French, German, Dutch and Polish.


Not Always the Ripest Nut in the Nest
-------------------------------------


These squirrels aren’t always picking up acorns that are fated to grow into majestic, money-making oaks. Researchers said that, “consistent with other threats also leveraging stolen email threads,” SquirrelWaffle took a few potshots in choosing which email chains to hijack.


They provided the following example, in which the attacker replied to an extortion email message – a choice that’s likely “ineffective in convincing the recipient to access the content in the body of the email,” researchers understated.


SquirrelWaffle Not Scampering as Furiously as Emotet – Yet
----------------------------------------------------------


SquirrelWaffle isn’t as prolific as Emotet – at least, not yet, though it’s growing steadily. Cisco Talos shared a graph, shown below, illustrating the volume of the campaigns between Sept. 1 and Oct. 15.


“While the volume associated with these campaigns is not yet reaching the same level seen previously with threats like Emotet, it appears to be fairly consistent and may increase over time as the adversaries infect more users and increase the size of their botnet,” Cisco Talos predicted.


Malspam O-Matic
---------------


In analyzing the campaign, researchers found multiple characteristics that pointed to the malicious Office documents as likely having been crafted using an automated builder. For example, in the recent campaigns, “the Microsoft Excel spreadsheets were crafted to make static analysis with tools like XLMDeobfuscator less effective,” they said.


The earliest files were submitted to public malware repositories on Sept. 10. Three days later, the campaign volume began to ramp up and “has been characterized by daily spam runs observed since then,” according to the writeup.


More signs that it’s getting cranked out with an automated builder: “The URL structure of the SQUIRRELWAFFLE distribution servers appears somewhat tied to the daily campaigns, and rotates every few days,” according to the analysis. Cisco Talos gave the example of the table, shown below, which depicts variance in the URL landing pages seen over a period of several days.


“This rotation is also reflected in the maldoc macros themselves, with the macro function names and hashes rotating at the same time,” the researchers added.


How the Squirrel Twitches
-------------------------


Victims who fall for the emails and click on their links wind up downloading a malicious ZIP archive that contains tainted Microsoft Office files, which have been evenly split between Word documents and Excel spreadsheets. The caveat: This is an actively evolving threat, and researchers have seen the threat actor shift from an initial reliance on using Word documents to an almost exclusive use of Excel spreadsheets.


In the earlier email campaigns using malicious Word documents, researchers saw the threat actor gussy up the document so it looked like it was associated with the DocuSign document-sharing and signing platform: a popular choice for dealing with official transactions.


At any rate, the Office files, be they .DOC or .XLS, spring the next-stage component, which is the SquirrelWaffle payload.


In all of the SquirrelWaffle campaigns seen so far, the rigged links used to host the ZIP archives contain Latin words and follow a URL structure similar to this one:



> abogados-en-medellin[.]com/odit-error/assumenda[.]zip
> 
> 


But in many cases, the campaign includes separate ZIP archives being hosted in different directories on the same domain. Inside of the ZIP archives, the malicious Office files often follow a naming convention similar to these examples:


They’re Kicking Servers When They’re Already Down
-------------------------------------------------


The malware distribution campaigns are apparently jumping on previously compromised web servers: primarily those running versions of WordPress, with the most prevalent compromised version being WordPress 5.8.1.


Researchers also identified one case of “a SQL dump related to an AZORult panel present on the same host being used as a C2 server by SQUIRRELWAFFLE,” they said.


They couldn’t figure out if the responsible actor was the same threat or whether the server had been gang-attacked by multiple actors: “As is often the case with vulnerable servers exposed to the internet, it is unclear whether this panel was being administered by the same threat actor or if the server had simply been compromised by multiple unrelated entities,” Cisco Talos said.


The More Malware Changes…
-------------------------


Cisco Talos said that while the SquirrelWaffle threat is relatively new, the workings – including the distribution campaigns, infrastructure and command-and-control (C2) implementations – have a lot in common with those seen from other, more established threat actors.


“Organizations should continue to employ comprehensive defense-in-depth security controls to ensure that they can prevent, detect, or respond to SQUIRRELWAFFLE campaigns that may be encountered in their environments,” they recommended.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Talos]] [[SquirrelWaffle]] [[malware]] [[said.]] [[emails]] [[campaigns,]] [[Microsoft]] [[Emotet]] [[SQUIRRELWAFFLE]] [[URL]] [[ThreatPost]]
