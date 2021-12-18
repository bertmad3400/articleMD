# New Yanluowang Ransomware Found to be Code-Signed, Terminates Database-Related Processes
### We analyzed new samples of the Yanluowang ransomware. One interesting aspect of these samples is that the files are code-signed. They also terminate various processes which are related to database and backup management. 

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/21/l/yanluowang-ransomware-code-signed-terminates-database-processes.html
+ Date: 2021-12-10
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/yanluowang-banner.jpg)





We analyzed new samples of the Yanluowang [ransomware](https://www.trendmicro.com/vinfo/us/security/definition/ransomware), a [recently discovered](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/yanluowang-ransomware-attacks-continue) ransomware family. One interesting aspect of these samples is that the files are code-signed using a valid digital signature, which was either stolen or fraudulently signed. They also terminate various processes including Veeam and SQL, which are related to database and backup management.


After being uncovered [a few weeks ago](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/yanluowang-targeted-ransomware), the Yanluowang ransomware (named after the Chinese deity Yanluo Wang) has since been associated with campaigns, and its operators are said to launch [targeted attacks](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/yanluowang-ransomware-attacks-continue) on US corporations since at least August this year.


Yanluowang ransomware initial analysis
--------------------------------------


The Yanluowang ransomware samples we analyzed still have only a few detections as of this writing. Just looking at the files themselves shows very little about where or how they arrived at a user’s system. But since the samples require certain arguments for proper execution, it appears that the most likely scenario for their execution is through remote desktop tools.


We also believe that the files analyzed here are merely part of a toolkit used by operators once they have compromised their victims’ machines.


From our initial analysis, the ransomware checks for the following arguments that are primarily used to specify the directory where it would do its encryption:


* -h/--help
* -p/-path/--path
* -pass






![Figure 1. Checking for arguments (path)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/Fig-1-Checking-for-arguments-path.PNG)
Figure 1. Checking for arguments (path)





![Figure 2. Checking for arguments (pass)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/Fig-2-Checking-for-arguments-pass.PNG)
Figure 2. Checking for arguments (pass)




The ransomware then encrypts the files from the provided file path on the argument, appends the extension (.yanluowang), then drops the ransom note (README.txt).






![Figure 3. Yanluowang ransomware appended files](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/Fig-3-Yanluowang-ransomware-appended-files.PNG)
Figure 3. Yanluowang ransomware appended files




![Figure 4. YanLuoWang ransomnote (README.txt)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/Fig-4-YanLuoWang-ransomnote(README.txt).PNG)
Figure 4. YanLuoWang ransomnote (README.txt)




Digital signature, other features also found
--------------------------------------------


It is important to highlight that the samples obtained are code-signed with a digital signature — and a valid one on that note, during the time of the analysis. The question remains whether this signature was stolen from a company or fraudulently signed.


[Code signing](https://www.trendmicro.com/en/research/18/d/understanding-code-signing-abuse-in-malware-campaigns.html) is performed to validate the authenticity of a piece of software; thus, code-signed malware can appear legitimate and non-malicious, allowing it to bypass certain security measures. 


 






![Figure 5. Digital signature found with Yanluowang ransomware samples](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/Fig-5-Digital-signature-found-with-Yanluowang-ransomware-samples.PNG)
Figure 5. Digital signature found with Yanluowang ransomware samples




Upon execution, the ransomware also terminates the following processes, which are related to managing databases and backups, through Windows API:


* Veeam
* SQL


The termination of database-related processes could potentially lead to loss of access to backup files, which then places additional pressure on ransomware victims to pay up to retrieve their files.






![Figures 6. Terminating processes](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/Fig-6-Terminating-processes.PNG)




![Figure 7. Terminating processes](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/Fig-7-Terminating-processes.PNG)
Figures 6-7. Terminating processes




The ransomware also attempts to terminate a few more processes through the command prompt if they match the following strings:


* mysql*
* dsa*
* veeam*
* chrome*
* iexplore*
* firefox*
* outlook*
* excel*
* taskmgr*
* tasklist*
* Ntrtscan*
* ds\_monitor*
* Notifier*
* putty*
* ssh*
* TmListen*
* iVPAgent*
* CNTAoSMgr*
* IBM*
* bes10*
* black*
* robo*
* copy*
* sql
* store.exe
* sql*
* vee*
* wrsa*
* wrsa.exe
* postg*
* sage*


Aside from processes, the malware will also forcefully stop (through net stop command line) the following services:


* MSSQLServerADHelper100
* MSSQL$ISARS
* MSSQL$MSFW
* SQLAgent$ISARS
* SQLAgent$MSFW
* SQLBrowser
* ReportServer$ISARS
* SQLWriter
* WinDefend
* mr2kserv
* MSExchangeADTopology
* MSExchangeFBA
* MSExchangeIS
* MSExchangeSA
* ShadowProtectSvc
* SPAdminV4
* SPTimerV4
* SPTraceV4
* SPUserCodeV4
* SPWriterV4
* SPSearch4
* IISADMIN
* firebirdguardiandefaultinstance
* ibmiasrw
* QBCFMonitorService
* QBVSS
* QBPOSDBServiceV12
* \"IBM Domino Server (CProgramFilesIBMDominodata)\"
* \"IBM Domino Diagnostics (CProgramFilesIBMDomino)\"
* \"Simply Accounting Database Connection Manager\"
* QuickBooksDB1
* QuickBooksDB2
* QuickBooksDB3
* QuickBooksDB4
* QuickBooksDB5
* QuickBooksDB6
* QuickBooksDB7
* QuickBooksDB8
* QuickBooksDB9
* QuickBooksDB10
* QuickBooksDB11
* QuickBooksDB12
* QuickBooksDB13
* QuickBooksDB14
* QuickBooksDB15
* QuickBooksDB16
* QuickBooksDB17
* QuickBooksDB18
* QuickBooksDB19
* QuickBooksDB20
* QuickBooksDB21
* QuickBooksDB22
* QuickBooksDB23
* QuickBooksDB24
* QuickBooksDB25


Lastly, it will forcefully terminate running virtual machines (VMs) through the following command line:


* powershell -command \"Get-VM | Stop-VM -Force\"






![Figure 8. Terminating services](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/Fig-8-Terminating-services.PNG)
Figure 8. Terminating services




We will continue to monitor events related to the Yanluowang ransomware and share any updates.


Strengthening defenses against ransomware
-----------------------------------------


As new ransomware families continue to emerge, we foresee in our [2022 security predictions report](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/predictions/2022) that ransomware operators will use more modern and sophisticated methods of extortion. Moving forward, enterprises must then take extra caution in applying preventive measures.


It would also help enterprises to establish frameworks that would help them with ransomware defense. Here are some of the best practices that they can include in their frameworks:


* Audit and take inventoryof assets and data, authorized and unauthorized devices and software, and logs of events and incidents.
* Configure and monitorhardware and software configurations, and only grant admin privileges and access when absolutely necessary to an employee’s role.
* Patch and update for operating systems and applications, perform regular vulnerability assessments, and conduct patching or virtual patching for operating systems and applications.
* Protect and recover essential information and files byenforcing stringent data protection, backup, and recovery measures.
* Perform security skills assessment and training regularly and conduct red-team exercises and penetration tests.
* Secure and defend systems by employing the latest version of security solutions to all layers of the system, including email, endpoint, web, and network.


[Trend Micro Vision One™](/en_us/business/services/managed-xdr.html) offers multilayered protection and behavior detection, allowing for the detection of and blocking ransomware early on before it can do any real damage to the system. This is done by identifying questionable behavior that might otherwise seem benign when viewed from only a single layer.


[Trend Micro Cloud One™ – Workload Security](/en_us/business/campaigns/cloud-one-services.html) defends systems against both known and unknown threats that exploit vulnerabilities through techniques such as virtual patching and machine learning. It also leverages the latest in global threat intelligence to provide timely, real-time protection.


[Trend Micro™ Deep Discovery™ Email Inspector](/en_us/business/products/user-protection/sps.html) employs custom sandboxing and advanced analysis techniques to effectively block ransomware before it gets into the system, blocking phishing emails that can be used by ransomware as entry points.


[Trend Micro Apex One™](/en_us/business/technologies/control-manager.html) provides a closer inspection of endpoints through next-level automated threat detection and response against advanced concerns such as fileless threats and ransomware.


Indicators of Compromise (IoCs)
-------------------------------


View the full list of IOCs [here](/content/dam/trendmicro/global/en/research/21/l/new-yanluowang-ransomware-found-to-be-code-signed-terminates-database-related-processes/New-Yanluowang-Ransomware-Family-Found-to-be-Code-Signed-Terminates-Database-Related-Processes.txt).








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tasklist]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Yanluowang]] [[Code-signed]] [[Onetm]] [[Trend Micro]]

