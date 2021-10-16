# TrickBot Gang Enters Cybercrime Elite with Fresh Affiliates
### The group – which also created BazarLoader and the Conti ransomware – has juiced its distribution tactics to threaten enterprises more than ever. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175510)
+ Date: October 15, 2021  2:05 pm
+ Author: Tara Seals


## Article:
The cybercriminals behind the infamous TrickBot trojan have signed two additional distribution affiliates, dubbed Hive0106 (aka TA551) and Hive0107 by IBM X-Force. The result? Escalating ransomware hits on corporations, especially using the Conti ransomware.


The development also speaks to the TrickBot gang’s increasing sophistication and standing in the cybercrime underground, IBM researchers said: “This latest development demonstrates the strength of its connections within the cybercriminal ecosystem and its ability to leverage these relationships to expand the number of organizations infected with its malware.”


The TrickBot malware started life as a banking trojan back in 2016, but it quickly evolved to become a modular, full-service threat. It’s capable of a range of backdoor and data-theft functions, can deliver additional payloads, and has the ability to quickly [move laterally](https://threatpost.com/trickbot-port-scanning-module/163615/) throughout an enterprise.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


According to IBM, the TrickBot gang (aka ITG23 or Wizard Spider) has now added powerful additional distribution tactics to its bag of tricks, thanks to the two new affiliates.


“Earlier this year, [the TrickBot gang] primarily relied on email campaigns delivering Excel documents and a call-center ruse known as BazarCall to deliver its payloads to corporate users,” IBM researchers said in a [Wednesday analysis](https://securityintelligence.com/posts/trickbot-gang-doubles-down-enterprise-infection/). “However…the new affiliates have added the use of hijacked email threads and fraudulent website customer-inquiry forms. This move not only increased the volume of its delivery attempts but also diversified delivery methods with the goal of infecting more potential victims than ever.”


BazarCall is a [distribution tactic](https://unit42.paloaltonetworks.com/bazarloader-malware/) that starts with emails offering “trial subscriptions” to various services – with a phone number listed to call customer service to avoid being charged money. If someone calls, a call-center operator answers and directs victims to a website to purportedly unsubscribe from the service:  a process the “agent” walks the caller through. In the end, vulnerable computers become infected with malware – usually the [BazarLoader implant](https://threatpost.com/bazarloader-malware-slack-basecamp/165455/), which is another malware in the TrickBot gang’s arsenal, and sometimes TrickBot itself. These types of attacks have continued into the autumn, enhanced by the fresh distribution approaches, according to IBM.


Meanwhile, since 2020, the TrickBot gang has been heavily involved in the ransomware economy, with the TrickBot malware acting as an initial access point in campaigns. Users infected with the trojan will see their device become part of a botnet that attackers typically use to load the second-stage ransomware variant. The operators have developed their own ransomware as well, according to IBM: the Conti code, which is notorious for hitting hospitals, [destroying backup files](https://threatpost.com/conti-ransomware-backups/175114/) and pursuing [double-extortion tactics](https://threatpost.com/double-extortion-ransomware-attacks-spike/154818/).


IBM noted that since the two affiliates came on board in June, there’s been a corresponding increase in Conti ransomware attacks – not likely a coincidence.


“Ransomware and extortion go hand in hand nowadays,” according to the firm’s analysis. “[The TrickBot gang] has also adapted to the ransomware economy through the creation of the Conti ransomware-as-a-service (RaaS) and the use of its BazarLoader and Trickbot payloads to gain a foothold for ransomware attacks.”


**Affiliate Hive0106: Spam Powerhouse**
---------------------------------------


IBM X-Force researchers noted that the most important development since June for the distribution of the TrickBot gang’s various kinds of malware is the newly minted partnership with Hive0106 (aka TA551, Shathak and UNC2420).


Hive0106 specializes in massive volumes of spamming and is a financially motivated threat group that’s lately been looking to partner with elite cybercrime gangs, the firm said.


Hive0106 campaigns begin with hijacking email threads: a tactic pioneered by its frenemy [Emotet](https://threatpost.com/emotet-takedown-infrastructure-netwalker-offline/163389/). The tactic involves [jumping into ongoing correspondence](https://unit42.paloaltonetworks.com/emotet-thread-hijacking/) to respond to an incoming message under the guise of being the rightful account holder. These existing email threads are stolen from email clients during prior infections. Hive0106 is able to mount these campaigns at scale, researchers said, using newly created malicious domains to host malware payloads.


“The emails include the email thread subject line but not the entire thread,” according to IBM X-Force’s writeup. “Within the email is an archive file containing a malicious attachment and password.”


In the new campaigns, that malicious document drops an HTML application (HTA) file when macros are enabled.


“HTA files contain hypertext code and may also contain VBScript or JScript scripts, both of which are often used in boobytrapped macros,” according to the analysis. “The HTA file then downloads Trickbot or BazarLoader, which has subsequently been observed downloading Cobalt Strike.”


Cobalt Strike is the legitimate pen-testing tool that’s [often abused by cybercriminals](https://threatpost.com/cobalt-strike-cybercrooks/167368/) to help with lateral movement. It’s often a precursor to a ransomware infection.


**Hive0107 Comes on Board**
---------------------------


Another prominent affiliate that hooked its wagon up to the TrickBot gang this summer is Hive0107, which spent the first half of the year distributing the IcedID trojan (a [TrickBot rival](https://threatpost.com/icedid-banking-trojan-surges-emotet/165314/)). It switched horses to TrickBot in May, using its patented contact form distribution method.


Analysts “observed Hive0107 with occasional distribution campaigns of the Trickbot malware detected mid-May through mid-July 2021…after that period, Hive0107 switched entirely to delivering BazarLoader,” according to the researchers, who added that most of the campaigns target organizations in the U.S. and, to a lesser extent, Canada and Europe.


Hive0107 is well-known for using customer contact forms on company websites to send malicious links to unwitting employees. Usually, the messages it sends threaten legal action, according to the analysis.


Previously, the cybercriminals used copyright infringement as a ruse: “The group typically enters information into these contact forms — probably using automated methods — informing the targeted organization that it has illegally used copyrighted images and includes a link to their evidence,” IBM X-Force researchers explained.


In the new campaigns, Hive0107 is using a different lure, the researchers said, claiming that the targeted company has been performing distributed denial-of-service (DDoS) attacks on its servers. Then, the messages provide a (malicious) link to purported evidence and how to remedy the situation.


The group also sends the same content via email to organization staff – an additional switch-up in tactics.


In any event, the links are hosted on legitimate cloud storage services where the payload lives, according to the analysis.


“Clicking on the link downloads a .ZIP archive containing a malicious JScript (JS) downloader titled ‘Stolen Images Evidence.js’ or ‘DDoS attack proof and instructions on how to fix it.js,'” researchers explained. “The JS file contacts a URL on newly created domains to download BazarLoader.”


BazarLoader then goes on to download Cobalt Strike and a PowerShell script to exploit the [PrintNightmare vulnerability](https://threatpost.com/microsoft-unpatched-printnightmare-zero-day/168613/) (CVE-2021-34527), they added – and sometimes TrickBot.


“IBM suspects that access achieved through these Hive0107 campaigns is ultimately used to initiate a ransomware attack,” the researchers noted.


The new affiliate campaigns are evidence of the TrickBot gang’s continuing success breaking into the circle of the cybercriminal elite, the firm concluded – a trend IBM X-Force expects to continue into next year.


“[The gang] started out aggressively back in 2016 and has become a cybercrime staple in the Eastern European threat-actor arena,” researchers said. “In 2021, the group has repositioned itself among the top of the cybercriminal industry.”


They added, “The group already has demonstrated its ability to maintain and update its malware and infrastructure, despite the efforts of law enforcement and industry groups [to take it down](https://threatpost.com/authorities-arrest-trickbot-member/169236/).”


**How to Protect Companies When TrickBot Hits**
-----------------------------------------------


To reduce the chances of suffering catastrophic damage from an infection (or a follow-on ransomware attack), IBM recommends taking the following steps:


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[TrickBot]] [[ransomware]] [[malware]] [[Hive0107]] [[Hive0106]] [[analysis.]] [[“The]] [[Conti]] [[gang’s]] [[cybercriminals]] [[ThreatPost]]
