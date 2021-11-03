# Mekotio Banking Trojan Resurges with Tweaked Code, Stealthy Campaign
### The banker, aka Metamorfo, is roaring back after Spanish police arrested more than a dozen gang members.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175981)
+ Date: November 3, 2021  3:47 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/03152802/Latin-America.jpg)
The Mekotio Latin American banking trojan is bouncing back after several of the gang that operates it were arrested in Spain. More than 100 attacks in recent weeks have featured a new infection routine, indicating that the group continues to actively retool.


“The new campaign started right after the Spanish Civil Guard [announced the arrest](https://therecord.media/spain-arrests-16-for-distributing-the-mekotio-and-grandoreiro-banking-trojans/) of 16 people involved with Mekotio [aka Metamorfo] distribution in July,” according to Check Point Research (CPR). “It appears that the gang behind the malware were able to narrow the gap quickly and change tactics to avoid detection.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Mekotio, like [other Latin American banking trojans](https://threatpost.com/brazils-banking-trojans-global/157452/), steals online banking logins and other financial credentials from unsuspecting victims. But they’re constantly evolving to avoid detection. In this case, the freshened-up Mekotio infection vector contains “unprecedented elements” to keep detection rates low, according to the firm’s analysis, [issued Wednesday](https://research.checkpoint.com/2021/mekotio-banker-returns-with-improved-stealth-and-ancient-encryption/). These are:


“In the last three months, we saw approximately 100 attacks use new, simple obfuscation techniques, with the help of a substitution cipher, to hide the first module of the attack,” according to CPR. “This simple obfuscation technique allows it to go undetected by most of the antivirus products.”


**Layers and Layers in the Malware Deployment**
-----------------------------------------------


The attacks are multistage in all phases, and they begin with Spanish-language phishing emails containing a .ZIP archive link or .ZIP file attachment. The lure is a claim that the email contains a digital tax receipt pending submission.


If a user is duped into clicking on either form of .ZIP file, the aforementioned stealthy batch file executes. In turn, it issues a PowerShell command to download and run a PowerShell script in memory.


The batch file has two layers of obfuscation and often contains a file name that starts with “Contacto,” according to CPR.


“The first layer of the obfuscation is a simple substitution cipher,” researchers explained. “Substitution ciphers encrypt plaintext by replacing each symbol in the plaintext with the corresponding symbol from the lookup table.”


The second layer of obfuscation is a technique that takes slices of the command code and saves them in different environment variables. When these are concatenated, the PowerShell command emerges that downloads the PowerShell script.


The PowerShell script is responsible for conducting pre-infection checks, i.e., determining if the target is located in a desired geography within Latin America (Brazil, Chile, Mexico, Spain or Peru), and verifying that it’s not running in a virtual machine/sandbox environment.


“The next thing the script does is to create an empty file, used as a footprint, whose name is the current date,” according to the firm. “This lets it know if it already ran in the system. If the file already exists, the script stops the execution.”


After that, it establishes persistence (by adding a new value to the following registry key: “HKCU\Software\Microsoft\Windows\CurrentVersion\Run”); and then it downloads a secondary .ZIP archive to the ProgramData Directory.


That secondary .ZIP archive contains three files, which are extracted, renamed and saved in a new directory on the infected system. The PowerShell script checks the size of the extracted files to distinguish between the type and the purpose of the files.


The first file is an interpreter for AutoHotkey (AHK), which is an open-source scripting language for Windows that lets users create shortcuts to files. The malware [added its use of AHK](https://threatpost.com/metamorfo-banking-trojan-autohotkey/164735/) to the mix last March as yet another evasion tactic.


The PowerShell script uses the interpreter to run a second file, which is an AHK script; and the AHK script then runs the third file, which is the Mekotio payload (in the form of a DLL packed with Themida v3).


[Themida](https://www.oreans.com/Themida.php) is a legitimate software protector/encryptor that was originally created to keep a cyberattacker from directly inspecting or modifying the code of a compiled application.


Once unpacked, “the DLL contains the main Mekotio banker functionality for actions such as stealing access credentials for electronic banking portals and a password stealer,” according to CPR analysis. “The stolen data is sent to the command-and-control server.”


While banking trojans targeting Latin America are common, they’re interesting to analyze because they tend to be modular, meaning that attackers can make small tweaks in order to stay off the detection radar, researchers noted.


“CPR sees a lot of old malicious code used for a long time, and yet the attacks manage to stay under the radar of antivirus and endpoint detection and response (EDR) solutions by changing packers or obfuscation techniques such as a substitution cipher,” they said. “Our analysis of this campaign highlights the efforts that attackers make to conceal their malicious intentions, bypass security filtering and trick users.”


**How to Protect Against Banking Trojans**
------------------------------------------


To protect against this type of attack, CPR offered the following basic anti-social-engineering tips:


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[PowerShell]] [[Mekotio]] [[.ZIP]] [[“The]] [[file,]] [[AHK]] [[ThreatPost]]
