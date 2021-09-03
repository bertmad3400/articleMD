# FIN7 Capitalizes on Windows 11 Release in Latest Gambit
### The financially motivated group looked to steal payment-card data from a California-based point-of-sale service provider.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169206)
+ Date: September 3, 2021  12:07 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/03115152/windows-11-e1630684336344.png)
The FIN7 financial cybercrime gang is back, delivering JavaScript backdoors using Word documents themed around the next version of Windows.


That’s according to researchers at Anomali, who observed a recent campaign from the group that leveraged six different docs, all referencing “Windows 11 Alpha” – the [“Insider Preview” version](https://blogs.windows.com/windows-insider/2021/06/28/announcing-the-first-insider-preview-for-windows-11/) of the upcoming Windows 11 operating system from Microsoft.


Windows 11 Alpha was released to the computing giant’s developer channels in late June, and it generated buzz among the technorati for offering a glimpse of the planned upgrades that Windows users can look forward to when Windows 11 rolls out this fall.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The FIN7 crooks looked to capitalize on this, delivering the themed docs to targets at a California-based point-of-sale provider called Clearmind (likely via email), among others – all boobytrapped with malicious Visual Basic (VBA) macros.


**FIN7’s Latest Attack Layout**
-------------------------------


The infection chain begins with a Microsoft Word document featuring a decoy image, telling readers that it was made with Windows 11 Alpha. The image asks the user to “Enable Editing and Enable Content” to see more.


Once the content/editing has been enabled, a VBA macro executes that takes encoded values from a hidden table inside the .doc file and deciphers them with an XOR key. This creates a script that carries out various checks on the target.


It first checks for the target system’s language. If Russian, Ukrainian or any number of other Eastern European languages are found to be the default, the script will terminate. Anomali researchers said that while it’s “accepted as an almost unofficial policy that cybercriminals based in the Commonwealth of Independent States (CIS) are generally left alone,” this particular check goes beyond those borders to include Sorbian, a minority German Slavic language; plus Estonian, Slovak and Slovenian. Those are also additions used by the [REvil ransomware gang](https://threatpost.com/kaseya-universal-decryptor-revil-ransomware/168070/), which has been known to work with FIN7 in the past, researchers noted.


The script also checks for virtual machines, to make sure it’s not being analyzed in a sandbox environment, and will terminate if one is found. Then, interestingly, it looks to see if the target is on the domain clearmind.com – the domain of the point-of-sale (PoS) service provider. If it is, it serves as a “proceed” check.


“The specified targeting of the Clearmind domain fits well with FIN7’s preferred modus operandi,” according to Anomali’s [Thursday writeup](https://www.anomali.com/blog/cybercrime-group-fin7-using-windows-11-alpha-themed-docs-to-drop-javascript-backdoor) on the campaign. “As a California-based provider of PoS technology for the retail and hospitality sector, a successful infection would allow the group to obtain payment-card data and later sell the information on online marketplaces.”


If the checks are satisfactory, the script drops a JavaScript file called “word\_data.js” into the TEMP folder which, once deobfuscated, turns out to be a JavaScript backdoor that FIN7 has been employing since 2018, researchers noted. From there, FIN7 can further penetrate a victim’s machine to steal data and perform recon for lateral movement.


**FIN7: No Signs of Slowing Down**
----------------------------------


FIN7 (aka Carbanak Group or Navigator Group) is a well-known threat actor that’s been circulating since at least 2015. The group [typically uses](https://threatpost.com/fin7-hitting-restaurants-with-fileless-malware/126213/) malware-laced phishing attacks against victims in hopes of infiltrating systems to steal bank-card data and sell it. The gang [consistently retools](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/) its malware arsenal. It has also become well-known for targeting PoS systems at casual-dining restaurants, casinos and hotels. Since 2020, it has also added ransomware/data exfiltration attacks to the mix, carefully selecting targets according to revenue using the ZoomInfo service.


The group has caught the eye of the U.S. Justice Department, which credits FIN7 with the theft of more than 15 million payment-card records and $1 billion in global losses. In the U.S. alone, the group has compromised the networks of organizations in 47 states and the District of Columbia, according to the DoJ, which in June [sentenced](https://threatpost.com/fin7-pen-tester-jail/167293/) a so-called “pen-tester” to seven years in prison and a $2.5 million fine after being convicted for payment-card theft. Other arrests and convictions have also plagued the group.


However, the legal action has done nothing to slow the group down – one month later it was back, [successfully compromising](https://threatpost.com/fin7s-liquor-lure-law-firm-backdoor/168086/) at least one law firm, using as a lure a legal complaint involving the liquor company that owns Jack Daniels whiskey.


“FIN7 is one of the most notorious financially motivated groups due to the large amounts of sensitive data they have stolen through numerous techniques and attack surfaces,” according to Anomali. “Despite high-profile arrests and sentencing, including alleged higher-ranking members, the group continues to be as active as ever. U.S. prosecutors believe the group numbers around 70 individuals, meaning the group can likely accommodate these losses as other individuals will step in.”


 




#### Tags:
[[FIN7]] [[Windows]] [[JavaScript]] [[payment-card]] [[U.S.]] [[ThreatPost]]
