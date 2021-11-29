# ScarCruft APT Mounts Desktop/Mobile Double-Pronged Spy Attacks
### The North Korea-linked group is deploying the Chinotto spyware backdoor against dissidents, journalists and other politically relevant individuals in South Korea.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176620)
+ Date: November 29, 2021  2:08 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/26152055/north-korea-flag-e1635276069649.jpeg)
The North Korea-linked ScarCruft advanced persistent threat (APT) group has developed a fresh, multiplatform malware family for attacking North Korean defectors, journalists and government organizations involved in Korean Peninsula affairs.


Since 2019, ScarCruft (aka APT37 or Temp.Reaper) has been using spyware dubbed Chinotto to target victims for espionage purposes, according to an analysis from Kaspersky, although the code only recently came to the attention of researchers.


![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)


Chinotto is triple-pronged, with the ultimate double-pronged goal of surveilling victims across mobile and desktop.


“The actor utilized three types of malware with similar functionalities: Versions implemented in PowerShell, Windows executables and Android applications,” researchers noted in a [Monday blog posting](https://securelist.com/scarcruft-surveilling-north-korean-defectors-and-human-rights-activists/105074/). “Although intended for different platforms, they share a similar command-and-control scheme based on HTTP communication. Therefore, the malware operators can control the whole malware family through one set of command-and-control scripts.”


ScarCruft specifically controls the malware using a PHP script on a compromised web server, directing the binaries based on HTTP parameters.


**Inside the Chinotto Backdoor**
--------------------------------


Chinotto has various tricks up its sleeve, researchers said, including detection evasion (i.e., employing garbage code to impede analysis) and establishing persistence via the registry key. And as far as the actual spyware functionality goes, it “shows fully fledged capabilities to control and exfiltrate sensitive information from the victims,” according to Kaspersky, across three types of variants: a Windows executable, a PowerShell version and an Android application.


“The actor targeted victims with a probable spear-phishing attack for Windows systems and smishing for Android systems,” according to Kaspersky. “The actor leverages Windows executable versions and PowerShell versions to control Windows systems. We may presume that if a victim’s host and mobile are infected at the same time, the malware operator is able to overcome two-factor authentication by stealing SMS messages from the mobile phone.”


When it comes to the Windows executable, the backdoor continuously queries its command-and-control (C2) server, awaiting commands from the malware operator. The commands include beaconing, executing Windows commands, downloading and uploading specific files, uploading log files, archiving and uploading whole directories, collecting and uploading all files with specific extensions, taking screenshots, and updating the malware.


Meanwhile, a different Chinotto variant contains an embedded PowerShell script, according to the analysis.


“It contains additional backdoor commands, such as uploading and downloading capabilities,” researchers explained. “Based on the build timestamp of the malware, we assess that the malware author used the PowerShell embedded version from mid-2019 to mid-2020 and started to use the malicious, PowerShell-less Windows executable from the end of 2020 onward.”


And finally, there’s also an Android application version of Chinotto, Kaspersky found. It comes in the form of a malicious APK that requests excessive permissions, which allows the app to collect sensitive information. This includes SMS messages, messaging app messages, contact lists, stored account information, call logs, device information and audio recordings of phone calls.


“Each sample has a different package name, with the analyzed sample bearing ‘com.secure.protect’ as a package name,” researchers explained.


Chinotto enables the operator to steal any information across desktop and mobile, which can then be used in follow-on attacks, researchers noted: “For example, the group attempts to infect additional valuable hosts and contact potential victims using stolen social-media accounts or email accounts.”


**Spear-Phishing Spycraft**
---------------------------


Kaspersky discovered the malware while conducting a forensic investigation on one victim that runs a business related to North Korea. The attack had started on social media when a ScarCruft representative contacted an acquaintance of the victim using the victim’s stolen Facebook account.


“After a conversation on social media, the actor sent a spear-phishing email to the potential victim using a stolen email account,” researchers said. “The actor leveraged their attacks using stolen login credentials, such as Facebook and personal email accounts, and thereby showed a high level of sophistication.”


The spear-phishing email contained a password-protected .RAR archive with the password shown in the email body; the RAR file in turn contained a malicious Word document entitled, “North Korea’s latest situation and our national security.”


This document contained a malicious macro that kicked off a multi-stage infection process.


“We suspect this host was compromised on March 22,” researchers said. “After the initial infection, the actor attempted to implant additional malware, but an error occurred that led to the crash of the malware. The malware operator later delivered the Chinotto malware in August 2021 and probably started to exfiltrate sensitive data from the victim.”


As for attribution, Kaspersky researchers discovered several code overlaps with an [older known ScarCruft malware](https://threatpost.com/scarcruft-apt-bluetooth-harvester/144643/) named POORWEB as well as a document-stealer malware the APT is known to use. This, combined with the victimology (South Korean journalists, diplomats and government employees), pointed to ScarCruft, according to the analysis.


“Many journalists, defectors and human rights activists are targets of sophisticated cyberattacks,” the firm concluded. “While hunting for related activity, we uncovered an older set of activity dating back to mid-2020, possibly indicating that ScarCruft operations against this set of individuals have been operating for a longer period of time.”


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***




#### Tags:
[[malware]] [[Windows]] [[ScarCruft]] [[“The]] [[Android]] [[PowerShell]] [[command-and-control]] [[spear-phishing]] [[Kaspersky]] [[ThreatPost]]
