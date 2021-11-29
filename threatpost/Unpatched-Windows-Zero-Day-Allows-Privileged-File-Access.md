# Unpatched Windows Zero-Day Allows Privileged File Access
### A temporary fix has been issued for CVE-2021-24084, which can be exploited using the LPE exploitation approach for the HiveNightmare/SeriousSAM bug.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176609)
+ Date: November 29, 2021  12:47 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26141726/Windows-Abstract.jpg)
An unpatched Windows security vulnerability could allow information disclosure and local privilege escalation (LPE), researchers have warned. The issue (CVE-2021-24084) has yet to get an official fix, making it a zero-day bug – but a micropatch has been rolled out as a stop-gap measure.


Security researcher Abdelhamid Naceri [originally reported](https://halove23.blogspot.com/2021/06/CVE-2021-24084-Unpatched-ID.html) the vulnerability as an information-disclosure issue in October 2020, via Trend Micro’s Zero-Day Initiative (ZDI). Though Microsoft had told him it was planning a fix for last April, the patch has not yet been forthcoming.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Then, this month, Naceri discovered that CVE-2021-24084 could also be exploited for LPE, so that non-admin Windows users can read arbitrary files even if they do not have permissions to do so. In a proof-of-concept exploit, he demonstrated that it’s possible to copy files from a chosen location into a Cabinet (.CAB) archive that the user can then open and read.



> 
> I mean this is still unpatched and allow LPE if shadow volume copies are enabled;   
> But I noticed that it doesn't work on windows 11 <https://t.co/HJcZ6ew8PO>
> 
> 
> — Abdelhamid Naceri (@KLINIX5) [November 15, 2021](https://twitter.com/KLINIX5/status/1460338968780804098?ref_src=twsrc%5Etfw)
> 
> 



The process for doing so is very similar to the [LPE exploitation approach](https://www.hackingarticles.in/windows-privilege-escalation-hivenightmare/) for the HiveNightmare bug, [CVE-2021-36934](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36934)**,** which affects the Security Accounts Manager (SAM) database in all versions of Windows 10. The SAM component in Windows houses user account credentials and network domain information – a juicy target for attackers.


“As [HiveNightmare/SeriousSAM](https://threatpost.com/win-10-serioussam/168034/) has taught us, an arbitrary file disclosure can be upgraded to local privilege escalation if you know which files to take and what to do with them,” Mitja Kolsek, head of the 0patch team, noted in a [recent posting](https://blog.0patch.com/2021/11/micropatching-unpatched-local-privilege.html). “We confirmed this [for the zero-day and were] able to run code as local administrator.”



> 
> It's still hilarious that this bug is still unpatched and fully functional on a windows 10 21H1 with october patch. <https://t.co/HO4Kwbql9z>
> 
> 
> — Abdelhamid Naceri (@KLINIX5) [November 2, 2021](https://twitter.com/KLINIX5/status/1455500874596356098?ref_src=twsrc%5Etfw)
> 
> 



**Windows 10 Bug Exploitation Details**
---------------------------------------


Specifically, the vulnerable functionality exists under the “access work or school” settings, according to the opatch writeup. A normal user can make use of the “export your management log files” function, which triggers the Device Management Enrollment Service.


“This service first copies some log files to the C:\ProgramData\Microsoft\MDMDiagnostics folder, and then packages them into a .CAB file whereby they’re temporarily copied to C:\Windows\Temp folder,” explained Kolsek. “The resulting .CAB file is then stored in the C:\Users\Public\Public Documents\MDMDiagnostics folder, where the user can freely access it.”


However, when the .CAB file is copied into the Windows Temp folder, a local attacker can pounce. The adversary would simply create a file shortcut link with a predictable file name that would normally be used in the normal export process, pointing to a target folder or file that the attacker would like to access.


“Since the Device Management Enrollment Service runs as Local System, it can read any system file that the attacker can’t,” Kolsek said.


There are two pre-requisites for achieving LPE, Kolsek noted.


“System protection must be enabled on drive C, and at least one restore point created. Whether system protection is enabled or disabled by default depends on various parameters,” he said. And, “at least one local administrator account must be enabled on the computer, or at least one ‘administrators’ group member’s credentials cached.”


To address the issue, the free micropatch simply checks for the presence of short-cut links during the .CAB file creation.


“The function we patched is CollectFileEntry inside mdmdiagnostics.dll. This is the function that copies files from C:\Windows\Temp folder into the .CAB file, and can be tricked into reading some other files instead,” Kolsek explained. “Our patch is placed immediately before the call to CopyFileW that opens the source file for copying, and uses the GetFinalPathNameByHandleW function to determine whether any junctions or other types of links are used in the path. If they are, our patch makes it look as it the CopyFileW call has failed, thereby silently bypassing the copying of any file that doesn’t actually reside in C:\Windows\Temp.”


Vulnerable versions of Windows include:


Windows Servers are not affected, and neither are Windows 11, Windows 10 v1803 and older Windows 10 versions.


Microsoft did not immediately return a request for comment on the timeline for an official patch.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***




#### Tags:
[[Windows]] [[.CAB]] [[Naceri]] [[Abdelhamid]] [[folder,]] [[Kolsek]] [[ThreatPost]]
