# Microsoft: Israeli firm used Windows zero-days to deploy spyware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-israeli-firm-used-windows-zero-days-to-deploy-spyware/)
+ Date: July 15, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft links Israeli firm to Windows spyware deployed using zero-days](https://www.bleepstatic.com/content/hl-images/2020/12/03/Stalker.jpg)


Microsoft and Citizen Lab have linked Israeli spyware company Candiru (also tracked as Sourgum) to new Windows spyware dubbed DevilsTongue deployed using now patched Windows zero-day vulnerabilities.


"Candiru is a secretive Israel-based company that sells spyware exclusively to governments," Citizen Lab explained in a report published today. "Reportedly, their spyware can infect and monitor iPhones, Androids, Macs, PCs, and cloud accounts."



"Sourgum generally sells cyberweapons that enable its customers, often government agencies around the world, to hack into their targets' computers, phones, network infrastructure and internet-connected devices," Microsoft added. "These agencies then choose who to target and run the actual operations themselves."


The investigation into Candiru's attacks started after Citizen Labs shared malware samples found on a victim's systems and led to the discovery of [CVE-2021-31979](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-31979) and [CVE-2021-33771](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-33771), two zero-day vulnerabilities fixed by Microsoft during this month's Patch Tuesday.


Microsoft researchers discovered "at least 100 victims in Palestine, Israel, Iran, Lebanon, Yemen, Spain, United Kingdom, Turkey, Armenia, and Singapore," with the victims including "politicians, human rights activists, journalists, academics, embassy workers, and political dissidents."


Citizen Lab also tied over 750 sites to Candiru's spyware infrastructure with moderate-high confidence using Internet scanning.


They also found that many of these domains were designed to mimic domains representing media companies and advocacy organizations, including Amnesty International and the Black Lives Matter movement.


Candiru's spyware
-----------------


The attackers delivered the DevilsTongue malware to victims' computers using an exploit chain that abused vulnerabilities in several popular browsers and the Windows operating system.


DevilsTongue allows its operators to collect and steal victims' files, decrypt and steal Signal messages on Windows devices, and steal cookies and saved passwords from LSASS and Chrome, Internet Explorer, Firefox, Safari, and Opera web browsers. 


It can also use cookies stored on the victim's computer for websites like Facebook, Twitter, Gmail, Yahoo, Mail.ru, Odnoklassniki, and Vkontakte to harvest sensitive information read its victims' messages, and exfiltrate photos.


DevilsTongue can also send messages as the victim on some of these websites, appearing to any recipient that the victim had sent these messages," as Microsoft researchers further found out. "The capability to send messages could be weaponized to send malicious links to more victims."


This capability could allow threat actors using Candiru's spyware to sent malicious links or messages from their victims' devices, making it almost impossible to prove who delivered the message.


"These attacks have largely targeted consumer accounts, indicating Sourgum's customers were pursuing particular individuals," Cristin Goodwin, General Manager at Microsoft's Digital Security Unit, [said](https://blogs.microsoft.com/on-the-issues/2021/07/15/cyberweapons-cybersecurity-sourgum-malware/).


"The protections we issued this week will prevent Sourgum's tools from working on computers that are already infected and prevent new infections on updated computers and those running Microsoft Defender Antivirus as well as those using Microsoft Defender for Endpoint."




#### Tags:
[[Microsoft]] [[spyware]] [[Sourgum]] [[Windows]] [[DevilsTongue]] [[Bleeping Computer]]
