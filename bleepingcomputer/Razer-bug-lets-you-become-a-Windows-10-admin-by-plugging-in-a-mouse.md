# Razer bug lets you become a Windows 10 admin by plugging in a mouse
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/razer-bug-lets-you-become-a-windows-10-admin-by-plugging-in-a-mouse/)
+ Date: August 22, 2021
+ Author: Lawrence Abrams


## Article:
![Razer](https://www.bleepstatic.com/content/hl-images/2020/09/11/razer.jpg)


A Razer Synapse zero-day vulnerability has been disclosed on Twitter, allowing you to gain Windows admin privileges simply by plugging in a Razer mouse or keyboard.


Razer is a very popular computer peripherals manufacturer known for its gaming mouses and keyboards.


When plugging in a Razer device into Windows 10 or Windows 11, the operating system will automatically download and begin installing the [Razer Synapse software](https://www.razer.com/synapse-3) on the computer. Razer Synapse is software that allows users to configure their hardware devices, set up macros, or map buttons.


Razer claims that that their Razer Synapse software is used by over 100 million users worldwide.


Security researcher [jonhat](https://twitter.com/j0nh4t) discovered a zero-day vulnerability in the plug-and-play Razer Synapse installation that allows users to gain SYSTEM privileges on a Windows device quickly.


SYSTEM privileges are the highest user rights available in Windows and allow someone to perform any command on the operating system. Essentially, if a user gains SYSTEM privileges in Windows, they attain complete control over the system.


After not receiving a response from Razer, jonhat disclosed the zero-day vulnerability on Twitter yesterday and explained how the bug works with a short video.




> 
> Need local admin and have physical access?  
> 
> - Plug a Razer mouse (or the dongle)  
> 
> - Windows Update will download and execute RazerInstaller as SYSTEM  
> 
> - Abuse elevated Explorer to open Powershell with Shift+Right click  
>   
> 
> Tried contacting [@Razer](https://twitter.com/Razer?ref_src=twsrc%5Etfw), but no answers. So here's a freebie [pic.twitter.com/xDkl87RCmz](https://t.co/xDkl87RCmz)
> 
> 
> — jonhat (@j0nh4t) [August 21, 2021](https://twitter.com/j0nh4t/status/1429049506021138437?ref_src=twsrc%5Etfw)


Getting SYSTEM privileges by plugging in a mouse
------------------------------------------------


As BleepingComputer has a Razer mouse available, we decided to test out the vulnerability and have confirmed that it took us about two minutes to gain SYSTEM privileges in Windows 10 after plugging in our mouse.


It should be noted that this is a local privilege escalation (LPE) vulnerability, which means that you need to have a Razer devices and physical access to a computer. With that said, the bug is so easy to exploit as you just need to spend $20 on Amazon for Razer mouse and plug it into Windows 10 to become an admin.


To test this bug, we created a temporary 'Test' user on one of our Windows 10 computers with standard, non-administrator privileges, as shown below.



![Test user with no administrative rights in Windows 10](https://www.bleepstatic.com/images/news/security/vulnerabilities/r/razer/razer-lpe-driver/whoami-standard.jpg)**Test user with no administrative rights in Windows 10**
When we plugged the Razer device into Windows 10, the operating system automatically downloaded and installed the driver and the Razer Synapse software.


Since the RazerInstaller.exe executable was launched via a Windows process running with SYSTEM privileges, the Razer installation program also gained SYSTEM privileges, as shown below.



![RazerInstaller.exe running with SYSTEM privileges](https://www.bleepstatic.com/images/news/security/vulnerabilities/r/razer/razer-lpe-driver/razer-process-properties.jpg)**RazerInstaller.exe running with SYSTEM privileges**
When the Razer Synapse software is installed, the setup wizard allows you to specify the folder where you wish to install it. The ability to select your installation folder is where everything goes wrong.


When you change the location of your folder, a 'Choose a Folder' dialog will appear. If you press Shift and right-click on the dialog, you will be prompted to open 'Open PowerShell window here,' which will open a PowerShell prompt in the folder shown in the dialog.



![Razer Synapse installation prompt](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Razer Synapse installation prompt**
As this PowerShell prompt is being launched by a process with SYSTEM privileges, the PowerShell prompt will also inherit those same privileges.


As you can see below, once we opened the PowerShell prompt and typed the 'whoami' command, it showed that the console has SYSTEM privileges allowing us to issue any command we want.



![PowerShell prompt with SYSTEM privileges](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**PowerShell prompt with SYSTEM privileges**
As explained by [Will Dormann](https://twitter.com/wdormann), a Vulnerability Analyst at the CERT/CC, similar bugs are likely to be found in other software installed by the Windows plug-and-play process.




> 
> Many vulnerabilities fall into the class of "How has nobody realized this before now?"  
>   
> 
> If you combine the facts of "connecting USB automatically loads software" and "software installation happens with privileges", I'll wager that there are other exploitable packages out there...
> 
> 
> — Will Dormann (@wdormann) [August 22, 2021](https://twitter.com/wdormann/status/1429433081728053248?ref_src=twsrc%5Etfw)


Razer to fix the vulnerability
------------------------------


After this zero-day vulnerability gained wide attention on Twitter, Razer has contacted the security researcher to let them know that they will be issuing a fix.




> 
> I would like to update that I have been reached out by [@Razer](https://twitter.com/Razer?ref_src=twsrc%5Etfw) and ensured that their security team is working on a fix ASAP.  
>   
> 
> Their manner of communication has been professional and I have even been offered a bounty even though publicly disclosing this issue.
> 
> 
> — jonhat (@j0nh4t) [August 22, 2021](https://twitter.com/j0nh4t/status/1429462941070409728?ref_src=twsrc%5Etfw)


Razer also told the researcher that he would be receiving a bug bounty reward even though the vulnerability was publicly disclosed.




#### Tags:
[[Windows]] [[PowerShell]] [[zero-day]] [[jonhat]] [[privileges,]] [[Bleeping Computer]]
