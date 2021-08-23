# Windows 10 Admin Rights Gobbled by Razer Devices
### So much for Windows 10’s security: a zero-day in the device installer software grants admin rights just by plugging in a mouse or other compatible device. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168855)
+ Date: August 23, 2021  11:58 am
+ Author: Lisa Vaas


## Article:
A zero-day bug in the device installer software for Razer peripherals – be they a Razer mouse, keyboard or any device that uses the [Synapse](https://www.razer.com/synapse-3) utility – gives the plugger-inner full admin rights on Windows 10, just by inserting a compatible peripheral and downloading Synapse.


There’s apparently nothing keeping the vulnerability from allowing the same privilege escalation on Windows 11, although, if that operating system has in fact been tested, its vulnerability hasn’t yet been reported.


Razer manufactures popular, high-end hardware for gamers, including mouses, keyboards and gaming chairs. Its Razer Synapse software enables users to configure hardware devices, set up macros or map buttons.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The bug was reported by security researcher jonhat ([@j0nh4t](https://twitter.com/j0nh4t)), who [tweeted](https://twitter.com/j0nh4t/status/1429049506021138437) about it on Saturday after initially not hearing back from Razer. As of Sunday, the tweet had caught Razer’s attention, and the manufacturer told jonhat that its security team was working on getting out a fix ASAP. It also awarded jonhat a bug bounty, in spite of the fact that the bug was disclosed.



> 
> Need local admin and have physical access?  
> – Plug a Razer mouse (or the dongle)  
> – Windows Update will download and execute RazerInstaller as SYSTEM  
> – Abuse elevated Explorer to open Powershell with Shift+Right click
> 
> 
> Tried contacting [@Razer](https://twitter.com/Razer?ref_src=twsrc%5Etfw), but no answers. So here's a freebie [pic.twitter.com/xDkl87RCmz](https://t.co/xDkl87RCmz)
> 
> 
> — jonhat (@j0nh4t) [August 21, 2021](https://twitter.com/j0nh4t/status/1429049506021138437?ref_src=twsrc%5Etfw)
> 
> 



As the researcher tells it and has [BleepingComputer](https://www.bleepingcomputer.com/news/security/razer-bug-lets-you-become-a-windows-10-admin-by-plugging-in-a-mouse/) confirmed in its own tests, the problem is that when a user plugs in a Razer device (or dongle, if it’s a wireless peripheral), Windows automatically fetches an installer containing driver software and the Synapse utility. The plug-and-play Razer Synapse installation then allows users to gain SYSTEM privileges on the Windows device lickety-split, since, as part of the setup routine, it opens an Explorer window that prompts the user to specify where the driver should be installed.


SYSTEM privileges are the highest user privilege level in Windows: With a SYSTEM account, someone can get full control over the system, meaning that they can view, change or delete data; can create new accounts with full user rights; and can install whatever they want – including malware.


In other words, the setup routine for Synapse runs with the highest available privileges in Windows 10. Since the RazerInstaller.exe executable was launched via a Windows process running with SYSTEM privileges, the Razer installation program inherited those same Admin privileges. jonhat found that if a user opts to change the default location of the installation folder, it triggers a “Choose a folder” dialog. At that point, you can right-click the installation window and press the Shift key, which opens a PowerShell terminal with those same elevated privileges.


Proof-of-Concept Video
----------------------


When j0nh4t initially didn’t hear back from Razer, the researcher posted a [video](https://streamable.com/q2dsji) that shows how the bug works. Below is a version of the video that’s clearer than the one initially shared on Twitter:


BleepingComputer had a Razer mouse kicking around, so the outlet tested out the vulnerability and quickly confirmed the zero day, managing to gain SYSTEM privileges in Windows 10 within about 2 minutes of plugging it in.


Here, There & Everywhere?
-------------------------


Granted, anybody who wants to exploit this local privilege escalation (LPE) vulnerability needs two things: a Razer device and the ability to get at a targeted computer. But, as BleepingComputer pointed out, it can be as easy as spending [~$24 on a Razer mouse](https://www.amazon.com/Razer-Death-Adder-Essential-RZ01-02540100-R3U1/dp/B07F7T8J9P/ref=sr_1_3?dchild=1&keywords=razer+mouse&qid=1629732236&sr=8-3) and plugging it into Windows 10 to become an admin.


It doesn’t necessarily stop here, however.


Will Dormann ([@wdormann](https://twitter.com/wdormann)), a vulnerability analyst with the CERT Coordination Center (CERT/CC), suggested that this vulnerability could in fact be universal.



> Many vulnerabilities fall into the class of “How has nobody realized this before now?”
> 
> 
> If you combine the facts of “connecting USB automatically loads software” and “software installation happens with privileges”, I’ll wager that there are other exploitable packages out there… —Will Dormann
> 
> 


The privilege escalation might be possible in all sorts of peripherals due to the lack of safeguards in Windows that might prevent it. Threatpost has reached out to Microsoft for feedback on further safety issues that could arise when it comes to connecting a USB tat automatically triggers automatic software loading and when the installation comes with SYSTEM privileges.


The vulnerability isn’t necessarily confined to just Razer peripherals. Another commenter, @Lechatquirit, claimed that the attack also works “with any asus ROG mouse. It will prompt to install armory [sic] crate and execute it as Sys,” the user [tweeted](https://twitter.com/Lechatquirit/status/1429374730860208128) in response to jonhat. [Armoury Crate](https://www.asus.com/support/FAQ/1042459/) is a software portal that displays real-time performance and settings information for connected devices and which works with ROG, TUF Gaming and ASUS products.


Razer Calls It a ‘Very Specific’ Attack Vector
----------------------------------------------


A Razer spokesperson told Threatpost on Monday that a fix should be out soon for what it called this “very specific use case.” Here’s the full statement:



> We were made aware of a situation in which our software, in a very specific use case, provides a user with broader access to their machine during the installation process.
> 
> 
> We have investigated the issue, are currently making changes to the installation application to limit this use case, and will release an updated version shortly. The use of our software (including the installation application) does not provide unauthorized third-party access to the machine.
> 
> 
> We are committed to ensuring the digital safety and security of all our systems and services, and should you come across any potential lapses, we encourage you to report them through our bug bounty service, Inspectiv: <https://app.inspectiv.com/#/sign-up>.
> 
> 


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Windows]] [[jonhat]] [[BleepingComputer]] [[privileges.]] [[Threatpost]] [[ThreatPost]]
