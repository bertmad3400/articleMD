# Turla APT Plants Novel Backdoor In Wake of Afghan Unrest
### “TinyTurla,” simply coded malware that hides away as a legitimate Windows service, has flown under the radar for two years. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=174858)
+ Date: September 21, 2021  12:02 pm
+ Author: Lisa Vaas


## Article:
The Turla advanced persistent threat (APT) group is back with a new backdoor used to infect systems in Afghanistan, Germany and the U.S., researchers have reported.


On Tuesday, [Cisco Talos researchers said](https://blog.talosintelligence.com/2021/09/tinyturla.html) that they’ve spotted infections they attributed to the Turla group (aka Snake, Venomous Bear, Uroburos and WhiteBear) – a Russian-speaking APT. Those attacks are “likely” using a stealthy, “second-chance” backdoor to maintain access to infected devices, they noted.


“Second-chance,” as in, it’s sticky: Even if an infected machine supposedly gets wiped clean of the primary malware, the attackers can maintain access to the system.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The novel backdoor, dubbed TinyTurla, can be used to drop payloads and to upload and/or execute files, according to the writeup. It could also be used as a second-stage dropper to infect the system with additional malware.


“The backdoor code is quite simple but is efficient enough that it will usually fly under the radar,” according to the report.


How TinyTurla Tiptoes
---------------------


Cisco Talos said that the attackers have installed TinyTurla as a service disguised as “Windows Time Service,” mimicking the legitimate [Windows service](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-top) that’s used to synchronize the date and time for systems running in Active Directory Domain Services (AD DS).


TinyTurla also mimics the legitimate Windows Time service in its ability to upload, execute or exfiltrate files. The backdoor contacts a command-and-control (C2) server via an HTTPS encrypted channel every five seconds to check for new commands, the researchers explained.


Due to TinyTurla’s limited functionality and its simple coding, anti-malware tools have a tough time detecting that it’s malware, the researchers said. That helps to explain why it hasn’t been identified yet, even though adversaries have deployed it since “at least 2020.”


“Turla is well-known and closely monitored by the security industry. Nevertheless, they managed to use this backdoor for almost two years,” Cisco Talos stressed. “This clearly shows that there is room for improvement on the defensive side.”


However, that five-second anomalous blip in network traffic can be sniffed out by some defense systems, they noted, showing “a great example of how important it is to incorporate network behavior-based detection into your security approach.”


How TinyTurla Twirls
--------------------


The attackers used a .BAT file that installs TinyTurla as an innocent-looking, fake Microsoft Windows Time service and which also sets the configuration parameters in the registry used by the backdoor. Below is a screenshot shared by Cisco Talos, redacted to remove the original C2 IP addresses “due to ongoing investigations.”


Cisco Talos researchers said that the malware’s DLL ServiceMain startup function doesn’t do much beyond executing a function they called “main\_malware” that includes the backdoor code. They called the dynamic link library (DLL) “pretty simple”: It consists of just a few functions and two “while” loops, including “the whole malware logic.”


The researchers noted that while Turla often uses sophisticated malware, the group also uses “good enough” malware like this to fly under the radar.


The APT actor isn’t perfect, though, and has make mistakes on the detection front: “Talos has monitored many noisy Turla operations, for example,” the report continued. “During their campaigns, they are often using and re-using compromised servers for their operations, which they access via SSH, often protected by Tor. One public reason why we attributed this backdoor to Turla is the fact that they used the same infrastructure as they used for other attacks that have been clearly attributed to their Penguin Turla infrastructure.”


That infrastructure is old: In the [Penguin Turla attacks](https://threatpost.com/linux-modules-connected-to-turla-apt-discovered/109765/) of 2011, disclosed by Kaspersky Lab in 2014, Linux machines were targeted with [a backdoor](https://threatpost.com/russian-speaking-turla-joins-apt-elite/124695/) based on the open-source LOKI2 backdoor that was released in [Phrack magazine](http://phrack.org/issues/51/6.html) in September 1997.)


Who Is Turla?
-------------


The Turla APT has roots that go back to 2004 and earlier, according to research from Kaspersky. In January, the firm suggested that Turla malware [may have been used](https://threatpost.com/solarwinds-hack-linked-turla-apt/162918/) in the SolarWinds blitzkrieg, given that Kaspersky researchers found code similarities between the Sunburst backdoor used in that sprawling series of [supply-chain attacks](https://threatpost.com/solarwinds-chris-krebs-alex-stamos-hack/162889/) and the Kazuar backdoor attributed to Turla.


At the time, Kaspersky described Turla as “a complex cyberattack platform focused predominantly on diplomatic and government-related targets, particularly in the Middle East, Central and Far East Asia, Europe, North and South America, and former Soviet-bloc nations.”


The APT has developed a huge arsenal of tools to do so. Besides being potentially tied to the Sunburst backdoor used in SolarWinds, Turla has also been linked to well-known malware like [Crutch](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/) – which leveraged Dropbox in [espionage attacks](https://threatpost.com/turla-backdoor-dropbox-espionage-attacks/161777/) against European Union countries last December – and, again, with the [Kazuar](https://threatpost.com/russian-espionage-custom-malware/160673/) backdoor, described in 2017 by [Palo Alto Networks](https://unit42.paloaltonetworks.com/unit42-kazuar-multiplatform-espionage-backdoor-api-access/) as a multiplatform espionage backdoor [with API access](https://threatpost.com/payment-api-exposes-payment-data/174825/).


Cisco Talos noted that monitoring of Russian-speaking actors; technical evidence; and tactics, techniques and procedures (TTPs) all help to trace things back to Turla in this latest case.


“By tracking these plus political interests, it’s often possible to attribute certain campaigns and toolsets to this actor,” the researchers wrote.


Used to Target Afghan Government
--------------------------------


Cisco Talos first unearthed the TinyTurla backdoor when it was used to target Afghanistan in the leadup to the [Taliban’s coup](https://www.wsj.com/articles/who-are-the-taliban-11628629642) and the pullout of Western military might. It assesses with “moderate confidence” that the malware was used to target the former Afghan government.


It’s a case study in how malicious services can slip by unnoticed in the crowd of legitimate services constantly running in the background, according to the writeup.


“It’s often difficult for an administrator to verify that all running services are legitimate,” the report explained, reiterating the need for network monitoring that can alert security teams to these infections. “It is important to have software and/or automated systems detecting unknown running services and a team of skilled professionals who can perform a proper forensic analysis on potentially infected systems,” researchers said.


Cisco Talos concluded by urging adoption of a multi-layered security architecture to detect these kinds of attacks. “It isn’t unlikely that the adversaries will manage to bypass one or the other security measures, but it is much harder for them to bypass all of them,” researchers forecasted.


They said they expect Turla campaigns – along with further refinement of the TTPs being used – as likely to continue “for the foreseeable future.”


***Rule #1 of Linux Security:** No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[Turla]] [[Talos]] [[TinyTurla]] [[Linux]] [[malware]] [[it’s]] [[malware,]] [[Windows]] [[Kaspersky]] [[ThreatPost]]
