# Microsoft to disable Excel 4.0 macros, one of the most abused Office features
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-to-disable-excel-4-0-macros-one-of-the-most-abused-office-features/)
+ Date: October 7, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft to disable Excel 4.0 macros, one of the most abused Office features](https://therecord.media/wp-content/uploads/2021/10/Excel.png)

Microsoft plans to disable a legacy feature known as Excel 4.0 macros, also XLM macros, for all Microsoft 365 users by the end of the year, according to an email the company has sent customers this week, also seen by *The Record*.


Introduced in 1992 with the release of the Excel 4.0 software — from where the feature also gets its name — XLM macros allow users to enter complex formulas inside Excel cells that can execute commands, either inside Excel or the local filesystem.


While XLM macros were replaced with the release of Excel 5.0, which introduced VBA-based macros, support for this feature has remained inside the Office Excel software to this day.


#### Excel 4.0 macros have been widely abused over the past two years


As with most Office tools that allow basic scripting-like actions, the feature has been abused over the course of the past decades by both financially motivated groups and state-sponsored threat actors alike.


But the abuse has never been as rampant as it has been since early 2020 when several security researchers noted the sudden and unexplainable increased attention XLM macros had been getting from numerous top-tier threat actors.


Reports from [VMWare](https://blogs.vmware.com/networkvirtualization/2020/10/evolution-of-excel-4-0-macro-weaponization-continued.html/), [ReversingLabs](https://blog.reversinglabs.com/blog/excel-4.0-macros), [Lastline](https://www.lastline.com/labsblog/evolution-of-excel-4-0-macro-weaponization/), [MadLabs](https://madlabs.dsu.edu/madrid/blog/2021/05/17/analyzing-document-with-malicious-excel-4-0-macros/), [Expel](https://twitter.com/jhencinski/status/1415682299992100864), [DeepInstinct](https://www.deepinstinct.com/2021/08/12/black-hat-2021-def-con-29-new-research-on-excel-4-0-macros/), and many [others](https://www.sneakymonkey.net/2020/06/22/excel-4-0-macros-so-hot-right-now/) referenced a spike in malware strains and threat actors abusing XLM macros, used in anything from cyber-espionage to banking trojans, and from ransomware to cryptocurrency theft.


![XLM-lastline](https://www-therecord.recfut.com/wp-content/uploads/2021/10/XLM-lastline-1024x198.png)Image: Lastline
Microsoft, too, has been aware of this issue, and added XLM macro support to the Antimalware Scan Interface (AMSI) for Office 365 [in March 2021](https://www.microsoft.com/security/blog/2021/03/03/xlm-amsi-new-runtime-defense-against-excel-4-0-macro-malware/) as a way to “to help antivirus solutions tackle the increase in attacks that use malicious XLM macros.”


However, over the summer months, several security researchers have publicly criticized Microsoft for leaving users exposed to attacks and asked more from the OS maker, namely, to disable the feature by default inside Office applications.


This way, they argued that the companies which rely on it could re-enable it for their employees while everyone else remained protected, in case they received an Excel file boobytrapped with a malicious XLM macro.


But while Microsoft is not disabling the feature for all users, it is taking steps to disable it, by default, for its paying customers, part of the Microsoft 365 service.


In an email sent to Microsoft 365 customers, Microsoft has laid out its plan to disable the feature across three stages:


* **Insiders-Slow:** will rollout in late October and be complete in early November.
* **Current Channel:** will rollout in early November and be complete in mid-November.
* **Monthly Enterprise Channel (MEC):** will begin and complete rollout in mid-December.





Customers who’d like to disable XLM (Excel 4.0) macros right now can follow the following [steps](https://techcommunity.microsoft.com/t5/excel-blog/restrict-usage-of-excel-4-0-xlm-macros-with-new-macro-settings/ba-p/2528450).


With XLM macros disabled, researchers are now asking Microsoft to do the same for VBA macros as well.10All suggestions





#### Tags:
[[XLM]] [[Microsoft]] [[macros,]] [[The Record]]
