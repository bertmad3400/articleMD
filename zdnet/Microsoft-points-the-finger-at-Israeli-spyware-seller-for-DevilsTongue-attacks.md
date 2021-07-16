# Microsoft points the finger at Israeli spyware seller for DevilsTongue attacks
### Updates released this week protect against two key zero-day vulnerabilities weaponized by customers.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-points-the-finger-at-israeli-private-exploit-seller-for-devilstongue-malware-attacks/)
+ Date: July 16, 2021 -- 08:28 GMT (09:28 BST)
+ Author: Charlie Osborne


## Article:
Unknown

[Microsoft](https://www.zdnet.com/topic/microsoft/)'s war against private exploit and offensive security sellers continues with a strike against Sourgum. 


On July 15, the Microsoft Threat Intelligence Center (MSTIC) said that the Redmond giant has been quietly tackling the threat posed to Windows operating systems by the organization, dubbed a "private-sector offensive actor" (PSOA).  

A tip provided by human rights outfit Citizen Lab [led Microsoft to the PSOA](https://blogs.microsoft.com/on-the-issues/2021/07/15/cyberweapons-cybersecurity-sourgum-malware/), dubbed Sourgum, a company said to sell cyberweapons including the DevilsTongue malware. 

"The weapons disabled were being used in precision attacks targeting more than 100 victims around the world including politicians, human rights activists, journalists, academics, embassy workers, and political dissidents," Microsoft says.  

Approximately half of DevilsTongue victims are located in Palestine, but a handful has also been traced back to countries including Israel, Iran, Spain/Catalonia, and the United Kingdom. 

According to the Citizen Lab, Sourgum [is based in Israel](https://citizenlab.ca/2021/07/hooking-candiru-another-mercenary-spyware-vendor-comes-into-focus/) and counts government agencies across the globe among its customers.  

With the assistance of Citizen Lab, Microsoft has examined the unique malware family developed by Sourgum and has now pushed protections against it in Windows security products. This includes patching previously unknown vulnerabilities, [CVE-2021-31979](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31979) and [CVE-2021-33771](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33771).  






These two vulnerabilities were listed as actively exploited in Microsoft's latest security update, known as [Patch Tuesday](https://www.zdnet.com/article/microsoft-july-2021-patch-tuesday-117-vulnerabilities-pwn2own-exchange-server-bug-fixed/), which is issued on a monthly basis. They are both described as Windows Kernel privilege escalation security flaws.  

Microsoft says that the exploits are "key" elements of wider attack chains used by Sourgum to target Windows PCs and browsers in order to deliver DevilsTongue. Browser exploits appear to be used in one of the initial attack stages, where they are served through malicious URLs and sent via messaging services including WhatsApp.  

The modular malware is described as "complex" with "novel capabilities." While analysis is ongoing, Microsoft says that DevilsTongue's main functionality is stored in encrypted .DLL files, only decrypted when loaded into memory, and both configuration and tasking data are separate from the main payload.  

DevilsTongue can be used in both user and kernel modes and is capable of .DLL hijacking, COM hijacking, shellcode deployment, file collection, registry tampering, cookie theft, and the extraction of credentials from browsers. A feature of note is a module dedicated to decrypting and extracting conversations taking place over Signal. 

The malicious code also contains sophisticated obfuscation and persistence mechanisms.  

"With these hacking packages, usually the government agencies choose the targets and run the actual operations themselves," Microsoft says. "The tools, tactics, and procedures used by these companies only add to the complexity, scale, and sophistication of attacks. We take these threats seriously and have moved swiftly alongside our partners to build in the latest protections for our customers." 

Detection data has also been shared with the [wider security community](https://www.microsoft.com/security/blog/2021/07/15/protecting-customers-from-a-private-sector-offensive-actor-using-0-day-exploits-and-devilstongue-malware/).  

"We're providing this guidance with the expectation that Sourgum will likely change the characteristics we identify for detection in their next iteration of the malware," the company added. "Given the actor's level of sophistication, however, we believe that outcome would likely occur irrespective of our public guidance." 

In [related news this week](https://www.zdnet.com/article/windows-print-spooler-hit-with-local-privilege-escalation-vulnerability/), Microsoft disclosed a third vulnerability impacting the Windows Print Spooler service, joining the duo of security flaws known as PrintNightmare. Tracked as CVE-2021-34481, the bug can be exploited to obtain system-level privileges locally. 

###  Previous and related coverage

* [Windows Print Spooler hit with local privilege escalation vulnerability](https://www.zdnet.com/article/windows-print-spooler-hit-with-local-privilege-escalation-vulnerability/)  

* [Microsoft rolls out first Windows 10 21H2 test build](https://www.zdnet.com/article/microsoft-rolls-out-first-windows-10-21h2-test-build/)  

* [Windows 11 has advanced hardware security. Here's how to get it in Windows 10 today](https://www.zdnet.com/article/windows-11-has-advanced-hardware-security-heres-how-to-get-it-in-windows-10-today/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Microsoft]] [[Windows]] [[Sourgum]] [[DevilsTongue]] [[malware]] [[ZDNet]]
