# This 'particularly dangerous' phishing attack features a weaponized Excel file
### Security researchers warn about a sneaky phishing campaign from one of the most creative cybercrime groups on the internet.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-particularly-dangerous-phishing-attack-features-a-weaponized-excel-file/)
+ Date: October 18, 2021
+ Author: Liam Tung


## Article:
Unknown

A new phishing campaign is targeting employees in financial services using links that download what is described as a 'weaponized' Excel document. 

The phishing campaign, dubbed MirrorBlast, was detected by security firm ET Labs in early September. Fellow security firm Morphisec has now analyzed the malware and notes the malicious Excel files could bypass malware-detection systems because it contains "extremely lightweight" embedded macros, making it "particularly dangerous" for organizations that depend on detection-based security and sandboxing. 


Macros, scripts for automating tasks, have become a popular tool for cyberattackers. While macros are disabled in Excel by default, attackers use social engineering to trick potential victims into enabling macros. 

**SEE:** [**This new ransomware encrypts your data and makes some nasty threats, too**](https://www.zdnet.com/article/this-new-ransomware-encrypts-your-data-and-makes-some-nasty-threats-too/)

Though seemingly a basic technique, macros have been used by state-sponsored hackers because they often work. Microsoft earlier this year [expanded its Antimalware Scan Interface (AMSI) for antivirus to address the surge in macro malware](https://www.zdnet.com/article/microsoft-were-cracking-down-on-malware-that-uses-excel-macros/) and a new trend by attackers to use legacy Excel 4.0 XLM macros (instead of newer VBA macros) to bypass anti-malware systems.    

According to Morphisec, the attack chain in MirrorBlast resembles techniques used by a well-established, financially motivated Russia-based cybercriminal [group that's tracked by researchers as TA505](https://www.zdnet.com/article/this-hacking-gang-just-switched-its-malware-attacks-to-a-new-target/). The group has been active since at least 2014 and is known for the wide variety of tools they use. 

"TA505 is most known for frequently changing the malware they use as well as driving global trends in malware distribution," [Morphisec researcher Arnold Osipov notes in a blogpost](https://blog.morphisec.com/explosive-new-mirrorblast-campaign-targets-financial-companies). 






While the MirrorBlast attack starts with a document attached to an email, it later uses a Google feedproxy URL with a SharePoint and OneDrive lure that poses as a file share request. Clicking the URL leads to a compromise SharePoint site or fake OneDrive site. Both versions lead to the weaponized Excel document.  

The sample MirrorBlast email shows the attackers are exploiting the theme of company-issued information about COVID-related changes to working arrangements. 


Morphisec notes that the macro code can be executed only on a 32-bit version of Office due to compatibility reasons with ActiveX objects. The macro itself executes JavaScript script designed to bypass sandboxing by checking if the computer is run in administrator mode. It then launches the the msiexec.exe process, which downloads and installs an MSI package. 

**SEE:** [**This new ransomware encrypts your data and makes some nasty threats, too**](https://www.zdnet.com/article/this-new-ransomware-encrypts-your-data-and-makes-some-nasty-threats-too/)

Morphisec found two variants of the MIS installer that used legitimate scripting tools called KiXtart and REBOL. 

The KiXtart script sends the victim's machine information, such as the domain, computer name, user name, and process list, to the attacker's command and control server. It then responds with a number instructing whether to proceed with the Rebol variant. 

According to Morphisec, the Rebol script leads to a remote access tool called FlawedGrace, which [has been used by the group in the past](https://www.zdnet.com/article/this-trojan-attack-adds-a-backdoor-to-your-windows-pc-to-steal-data/).

"TA505 is one of many financially motivated threat groups currently active in the marketplace. They are also one of the most creative, as they have a tendency to constantly shift the attacks they leverage to achieve their goals," Osipov notes.  





#### Tags:
[[malware]] [[Morphisec]] [[MirrorBlast]] [[ZDNet]]
