# Windows 0-Days Used Against Dissidents in Israeli Broker’s Spyware
### Candiru, aka Sourgum, allegedly sells the DevilsTongue surveillance malware to governments around the world. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167865)
+ Date: July 16, 2021  11:55 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2015/02/07005538/i-spy--e1626449373529.jpg)
A set of unique spyware strains created by an Israeli firm and allegedly used by governments around the world to surveil dissidents has been defanged by Microsoft, the software giant said.


The private company, called variously Candiru, Grindavik, Saito Tech and Taveta (and dubbed “Sourgum” by Microsoft), [reportedly](https://www.forbes.com/sites/thomasbrewster/2019/10/03/meet-candiru-the-super-stealth-cyber-mercenaries-hacking-apple-and-microsoft-pcs-for-profit/?sh=4f4be6805a39) sells its wares exclusively to governments, according to Citizen Lab, which first analyzed the malware and flagged it for Microsoft. The code, collectively known as “DevilsTongue,” has been used in highly targeted cyberattacks against civil society, according to [an advisory](https://citizenlab.ca/2021/07/hooking-candiru-another-mercenary-spyware-vendor-comes-into-focus/) issued Thursday – making use of a pair of zero-day vulnerabilities in Windows (now patched).


The victims number more than 100, and include politicians, human-rights activists, journalists, academics, embassy workers and political dissidents, Citizen Lab and Microsoft said. The targets have been global, located in Armenia, Iran, Israel, Lebanon, Palestine, Singapore, Spain, Turkey, United Kingdom and Yemen.



“Sourgum generally sells cyberweapons that enable its customers, often government agencies around the world, to hack into their targets’ computers, phones, network infrastructure and internet-connected devices,” according to Microsoft’s [tandem advisory](https://blogs.microsoft.com/on-the-issues/2021/07/15/cyberweapons-cybersecurity-sourgum-malware/?fbclid=IwAR3eN3x9ZzDt10dZh0aP5tEZ0AIvmu_dzah4F85dEYRlLliUhT3-gUET5Hc). “These agencies then choose who to target and run the actual operations themselves.”


Citizen Lab researchers said that DevilsTongue can exfiltrate data and messages from various accounts, including Facebook, Gmail, Skype and Telegram. The spyware can also capture browsing history, cookies and passwords, turn on the target’s webcam and microphone, and take pictures of the screen.


“Capturing data from additional apps, such as Signal Private Messenger, is sold as an add-on,” according to the firm.


Microsoft noted that the stolen cookies can later be used by the attacker to sign in as the victim to websites to enable further information gathering.


The code can infect and monitor Android phones, cloud accounts, iPhones, Macs and PCs, Citizen Lab researchers said, noting that DevilsTongue’s command-and-control (C2) infrastructure involves more than 750 websites, including “domains masquerading as advocacy organizations such as Amnesty International, the Black Lives Matter movement as well as media companies.”


**Millions of Euros**
---------------------


DevilsTongue as a kit goes for millions of Euros, according to a leaked proposal [[PDF](https://www.themarker.com/embeds/pdf_upload/2020/20200902-161742.pdf)] obtained by Citizen Lab. It can be deployed in a number of attack vectors, including via malicious links,  attached files in emails and man-in-the-middle attacks. The cost depends on the number of concurrent infections a user would like to maintain.


“The €16 million project proposal allows for an unlimited number of spyware infection attempts, but the monitoring of only 10 devices simultaneously,” according to Citizen Lab. “For an additional €1.5M, the customer can purchase the ability to monitor 15 additional devices simultaneously, and to infect devices in a single additional country. For an additional €5.5M, the customer can monitor 25 additional devices simultaneously, and conduct espionage in five more countries.”


It added, “For a further additional €1.5M fee, customers can purchase a remote-shell capability, which allows them full access to run any command or program on the target’s computer. This kind of capability is especially concerning, given that it could also be used to download files, such as planting incriminating materials, onto an infected device.”


Use of DevilsTongue is restricted in a handful of countries, including China, Iran, Israel, Russia and the U.S. However, there are, apparently, loopholes.


“Microsoft observed Candiru victims in Iran, suggesting that in some situations, products from Candiru do operate in restricted territories,” Citizen Lab researchers said. “In addition, targeting infrastructure disclosed in this report includes domains masquerading as the Russian postal service.”


**Zero-Day Exploits**
---------------------


The spyware exploits two elevation-of-privilege security vulnerabilities in Windows, CVE-2021-31979 and CVE-2021-33771, both of which [were addressed](https://threatpost.com/microsoft-crushes-116-bugs/167764/) in Microsoft’s July Patch Tuesday update this week. The attacks are carried out via “a chain of exploits that impacted popular browsers and our Windows operating system,” Microsoft noted.


Both bugs give an attacker the ability to escape browser sandboxes and gain kernel code execution, Microsoft said:


To mitigate the attacks, Microsoft said that it “built protections into our products against the unique malware Sourgum created,” in addition to the patching.


“These attacks have largely targeted consumer accounts, indicating Sourgum’s customers were pursuing particular individuals,” according to Microsoft. “The protections we issued this week will prevent Sourgum’s tools from working on computers that are already infected and prevent new infections on updated computers and those running Microsoft Defender Antivirus as well as those using Microsoft Defender for Endpoint.”


Private brokers of cyberattack kits for government surveillance have been publicized mainly thanks to another Israeli firm, NSO Group, which created the Pegasus spyware that enables customers to remotely exploit and monitor mobile devices. NSO Group has [long maintained](https://threatpost.com/nso-group-president-defends-controversial-tactics/150694/) that its kit is meant to be a tool for governments to use in fighting crime and terror, and that it’s not complicit in any government’s misuse of it. However, critics say that repressive governments use it for [more nefarious purposes](https://threatpost.com/nso-group-impersonates-facebook-security/156021/) to track dissidents, journalists and other members of civil society — and that NSO Group assists them. In December, Pegasus [added](https://threatpost.com/zero-click-apple-zero-day-pegasus-spy-attack/162515/) an exploit for a zero-day in Apple’s iMessage feature for iPhone.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Microsoft]] [[spyware]] [[Sourgum]] [[DevilsTongue]] [[Windows]] [[5M]] [[NSO]] [[ThreatPost]]
