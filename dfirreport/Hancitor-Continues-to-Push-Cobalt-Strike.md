# Hancitor Continues to Push Cobalt Strike
### 

## Information:
+ Source: The DFIR Report
+ Link: [article](https://thedfirreport.com/2021/06/28/hancitor-continues-to-push-cobalt-strike/)
+ Date: June 28, 2021
+ Author: Unknown


## Article:


> 
> First observed in 2014, Hancitor (also known as Chanitor and Tordal) is a downloader trojan that has been used to deliver multiple different malware such as Pony, Vawtrak, and DELoader. [[1]](https://digital.nhs.uk/cyber-alerts/2016/cc-678)
> 
> 
> 


Here’s some great write ups on Hancitor:


Binary Defense – [Analysis of Hancitor – When Boring Begets Beacon – Binary Defense](https://www.binarydefense.com/analysis-of-hancitor-when-boring-begets-beacon)


Group IB – [Connecting the Bots: Hancitor fuels Cuba Ransomware Operations (group-ib.com)](https://blog.group-ib.com/hancitor-cuba-ransomware)


Unit 42 – [Recent Hancitor Infections Use Cobalt Strike and a Network Ping Tool (paloaltonetworks.com)](https://unit42.paloaltonetworks.com/hancitor-infections-cobalt-strike/)


### Case Summary


In this short intrusion, the threat actor gained initial access on a system through a maldoc campaign which made use of the Hancitor downloader. The first-stage DLL, which was dropped by a malicious Word document, attempted to download multiple malware payloads on the beachhead system, including Ficker Stealer. In addition, a Cobalt Strike beacon payload was downloaded, and deployed to perform post-exploitation activities. Once inside the target environment, port scans and a large amount of ICMP traffic was observed–to identify additional active systems. After about 20 minutes, the threat actor copied a batch script file and DLL file to another system using the SMB protocol. A remote service was installed to start the batch file, which executed the Cobalt Strike shellcode-embedded DLL. On the second compromised system, various discovery-related commands were executed before going silent. The threat actors were evicted before completing their mission.


### Services


We offer multiple services including a Threat Feed service which tracks Command and Control frameworks such as Cobalt Strike, Metasploit, Empire, PoshC2, etc. More information on this service and others can be found [here](https://thedfirreport.com/services/). One of the Cobalt Strike servers used in this intrusion was known about as far back as February and the other 2 were added to our Threat Feed on 5/20/21.


We also have artifacts available from this case such as pcaps, memory captures, files, Kape packages, and more, under our [Security Researcher and Organization](https://www.patreon.com/thedfirreport) services.


###  **Timeline**


[![](https://thedfirreport.com/wp-content/uploads/2021/06/Hancitor-Continues-to-Push-Cobalt-Strike.png)](https://thedfirreport.com/wp-content/uploads/2021/06/Hancitor-Continues-to-Push-Cobalt-Strike.png)


Analysis and reporting completed by **[@pigerlin](https://twitter.com/pigerlin)** and **[@v3t0\_](https://twitter.com/v3t0_)**


Reviewed by **[@\_pete\_0](https://twitter.com/_pete_0)**


### MITRE ATT&CK v9


### Initial Access


The Hancitor malware was embedded in a macro-based Word document. This single-paged document contained a picture with instructions, attempting to lure the victim into enabling macros.  


[![](https://thedfirreport.com/wp-content/uploads/2021/06/image-21.png)](https://thedfirreport.com/wp-content/uploads/2021/06/image-21.png)
   
When the macro was enabled, the infection chain started, and the first-stage Hancitor DLL was dropped to disk. 


Reviewing the macro we can see that in sub yyy (towards the bottom) content within the document is being copied and used to create a file object by sub xxx which then is executed by the shell call to rundll32.


[![](https://thedfirreport.com/wp-content/uploads/2021/06/55-2.png)](https://thedfirreport.com/wp-content/uploads/2021/06/55-2.png)


Looking at the strings of the word document, we can see that there’s an embedded OLE object, which appears to be a PE file.


[![](https://thedfirreport.com/wp-content/uploads/2021/06/4301-1.png)](https://thedfirreport.com/wp-content/uploads/2021/06/4301-1.png)


### Execution


The malicious Hancitor DLL in the OLE object, named “rem.r”, was executed via rundll32.exe by passing the entry point “ESLMJYVFM”. 


[![](https://thedfirreport.com/wp-content/uploads/2021/06/001_execution-2.png)](https://thedfirreport.com/wp-content/uploads/2021/06/001_execution-2.png)



[![](https://thedfirreport.com/wp-content/uploads/2021/06/3-1.png)](https://thedfirreport.com/wp-content/uploads/2021/06/3-1.png)


The botnet ID and C2 were extracted using [Hatching Triage](https://tria.ge):


[![](https://thedfirreport.com/wp-content/uploads/2021/06/33.png)](https://thedfirreport.com/wp-content/uploads/2021/06/33.png)


Later on in the intrusion, the threat actor used the following command to execute a Cobalt Strike Beacon on another machine:



```
rundll32.exe c:\programdata\95.dll,TstSec 11985756 
```


### Defense Evasion






On the beachhead system, the malicious Hancitor DLL injected into the svchost.exe process. The code was injected into multiple instances of svchost.exe.






[![](https://thedfirreport.com/wp-content/uploads/2021/06/006_defense-evasion.png)](https://thedfirreport.com/wp-content/uploads/2021/06/006_defense-evasion.png)  
Memory analysis also shows suspicious memory protections (page\_execute\_readwrite) and regions of the particular process. 






[![](https://thedfirreport.com/wp-content/uploads/2021/06/007_defense-evasion.png)](https://thedfirreport.com/wp-content/uploads/2021/06/007_defense-evasion.png)  
   
Finally, when looking at the process tree, we can identify the unusual parent-child process relationship of rundll32.exe starting svchost.exe.   






[![](https://thedfirreport.com/wp-content/uploads/2021/06/image-25.png)](https://thedfirreport.com/wp-content/uploads/2021/06/image-25.png)




The svchost.exe process, in turn, injected a Cobalt Strike beacon into multiple rundll32.exe instances. One of the injected rundll32.exe instance was also observed connecting to the Cobalt Strike C2 server. 






[![](https://thedfirreport.com/wp-content/uploads/2021/06/44.png)](https://thedfirreport.com/wp-content/uploads/2021/06/44.png)




In addition, the malicious 95.dll, which was observed during the lateral movement phase, is also designed to evade automated sandbox analysis. This DLL is crafted in such a way that it wouldn’t show malicious behavior if an exported function is not called by passing a specific parameter. The DLL contains the Cobalt Strike shellcode and will only execute if the “*11985756”* parameter is passed to the TstSec function. 






[![](https://thedfirreport.com/wp-content/uploads/2021/06/image-26.png)](https://thedfirreport.com/wp-content/uploads/2021/06/image-26.png)




   
After extracting the Cobalt Strike shellcode from 95.dll and emulating it via [scdbg](http://sandsprite.com/blogs/index.php?uid=7&pid=152), we found that it’s connecting to 162.244.83[.]95 over port 8080.






[![](https://thedfirreport.com/wp-content/uploads/2021/06/image-27.png)](https://thedfirreport.com/wp-content/uploads/2021/06/image-27.png)




Since 95.dll was executed by rundll32.exe, and from the host logs, it is evident  that rundll32.exe connected to 162.244.83[.]95 over port 8080. 


[![](https://thedfirreport.com/wp-content/uploads/2021/06/012_defense-evasion-2.png)](https://thedfirreport.com/wp-content/uploads/2021/06/012_defense-evasion-2.png)











Packet analysis to the IP address mentioned above, shows that it’s downloading the Cobalt Strike beacon by initiating a HTTP GET request to /hVVH URI. 











![](https://thedfirreport.com/wp-content/uploads/2021/06/1-1.png)


Once downloaded, the stager allocates a new memory region inside the current rundll32.exe process and loads it into the memory and starts the C2 activity. 






### Discovery






On the beachhead system, the threat actor started exploring their options to move laterally within the target network. The logged-on user account was utilized to interact with IPC$ shares.


[![](https://thedfirreport.com/wp-content/uploads/2021/06/023_discovery.png)](https://thedfirreport.com/wp-content/uploads/2021/06/023_discovery.png)


For one specific system, for which the threat actor showed interest, the contents of the C$ share was listed–we assess, to verify if the account had access permissions to the share before copying the malware to it: 






[![](https://thedfirreport.com/wp-content/uploads/2021/06/image-30-1024x65.png)](https://thedfirreport.com/wp-content/uploads/2021/06/image-30.png)




The threat actor also pinged one of the Active Directory domain controllers from the beachhead machine. 






[![](https://thedfirreport.com/wp-content/uploads/2021/06/image-29-1024x78.png)](https://thedfirreport.com/wp-content/uploads/2021/06/image-29.png)




A high amount of ICMP traffic, targeting various Class-A subnets ranges, was observed and used to identify other active systems within the environment.   
[![](https://thedfirreport.com/wp-content/uploads/2021/06/016_discovery.png)](https://thedfirreport.com/wp-content/uploads/2021/06/016_discovery.png)










On the second system, to which the adversary laterally moved (see section below), the following discovery commands were executed: 


[![](https://thedfirreport.com/wp-content/uploads/2021/06/2.png)](https://thedfirreport.com/wp-content/uploads/2021/06/2.png)












```
nltest /domain\_trusts  
net view /domain  
net time
```

### Lateral Movement






The injected svchost process dropped two files: a batch-file named: “95.bat” and a DLL-file named: “95.dll”. Both files were copied to the ProgramData folder of another system within the environment. 






[![](https://thedfirreport.com/wp-content/uploads/2021/06/3.png)](https://thedfirreport.com/wp-content/uploads/2021/06/3.png)




The content of the batch file can be seen below–it executes the transferred DLL and then deletes itself:   
   
[![](https://thedfirreport.com/wp-content/uploads/2021/06/020_lateralmovement.png)](https://thedfirreport.com/wp-content/uploads/2021/06/020_lateralmovement.png)  
 


To execute the batch file, the threat actor installed, and started, a remote service on the other system. 


[![](https://thedfirreport.com/wp-content/uploads/2021/06/002_execution-2.png)](https://thedfirreport.com/wp-content/uploads/2021/06/002_execution-2.png)


[![](https://thedfirreport.com/wp-content/uploads/2021/06/021_persistence-2.png)](https://thedfirreport.com/wp-content/uploads/2021/06/021_persistence-2.png)
















[![](https://thedfirreport.com/wp-content/uploads/2021/06/022_persistence-2.png)](https://thedfirreport.com/wp-content/uploads/2021/06/022_persistence-2.png)






### Credential Access






An attempt to open lsass.exe process was observed on the system where lateral movement occurred but there were no signs of successful read attempts.


[![](https://thedfirreport.com/wp-content/uploads/2021/06/55.png)](https://thedfirreport.com/wp-content/uploads/2021/06/55.png)


### Command and Control


In the network traffic, we can identify a data stream pattern that is distinctive to Hancitor malware. 


[![](https://thedfirreport.com/wp-content/uploads/2021/06/003_cnc-1.png)](https://thedfirreport.com/wp-content/uploads/2021/06/003_cnc-1.png)


First, the malware performed a lookup of the external IP-address of the infected system (1). This was followed by Hancitor C2 traffic, sent via HTTP POST requests, which included unique attributes of the infected system, such as hostname and username information (2). 


Hancitor then attempted to download additional malware. This included the info-stealer known as “Ficker Stealer” (4), for which the DNS traffic corresponds to a recent article posted by [Brad](https://unit42.paloaltonetworks.com/hancitor-infections-cobalt-strike/). However, in our case, the post infection HTTP traffic of Ficker Stealer was not observed. 


[![](https://thedfirreport.com/wp-content/uploads/2021/06/004_cnc.png)](https://thedfirreport.com/wp-content/uploads/2021/06/004_cnc.png)



Hancitor also attempted to download Cobalt Strike stagers (.bin files) (3), and Cobalt Strike traffic was sent both encrypted and unencrypted (5).


**Hancitor**   
  
vaethemanic[.]com/8/forum.php   
tembovewinated[.]ru/8/forum.php   
prournauseent[.]ru/8/forum.php   
   
**Cobalt Strike**   
   
216.250.248[.]88   
Config:



```
"x64":    
"config":    
"Jitter": 0,   
"Method 2": "POST",   
"Beacon Type": "0 (HTTP)",   
"Watermark": 0,   
"Method 1": "GET",   
"Polling": 60000,   
"C2 Server": "216.250.248.88,/ga.js",   
"Port": 80,   
"Spawn To x64": "%windir%\\sysnative\\rundll32.exe",   
"Spawn To x86": "%windir%\\syswow64\\rundll32.exe",   
"C2 Host Header": "",   
"HTTP Method Path 2": "/submit.php"   
  
"x86":    
"config":    
"Jitter": 0,   
"Method 2": "POST",   
"Beacon Type": "0 (HTTP)",   
"Watermark": 0,   
"Method 1": "GET",   
"Polling": 60000,   
"C2 Server": "216.250.248.88,/ptj",   
"Port": 80,   
"Spawn To x64": "%windir%\\sysnative\\rundll32.exe",   
"Spawn To x86": "%windir%\\syswow64\\rundll32.exe",   
"C2 Host Header": "",   
"HTTP Method Path 2": "/submit.php" 
```

162.244.83[.]95   
Config:



```
"x64":    
"sha1": "93d1f927eae5d7cee5a36c4b5570fedd1e04f362",   
"uri\_queried": "/WZSY",   
"sha256": "0e5f353721f618b1d1ec89570443a4a42ae5e41d466f9a022ace75bf74ff9dcd",   
"config":    
"HTTP Method Path 2": "/submit.php",   
"C2 Host Header": "",   
"Watermark": 0,   
"Spawn To x86": "%windir%\\syswow64\\rundll32.exe",   
"Method 1": "GET",   
"Spawn To x64": "%windir%\\sysnative\\rundll32.exe",   
"Polling": 60000,   
"C2 Server": "162.244.83.95,/fwlink",   
"Port": 8080,   
"Method 2": "POST",   
"Jitter": 0,   
"Beacon Type": "0 (HTTP)"   
  
"x86":    
"sha1": "d8f0bda5ee2416d7059b9ff58aa6c7f5357d3a6d",   
"uri\_queried": "/Vdn4",   
"sha256": "c0ef889bda5881d8c5441ba7bed8655851d9f734d1ede2bb934f2c5060b65e61",   
"config":   
"HTTP Method Path 2": "/submit.php",   
"C2 Host Header": "",   
"Watermark": 0,   
"Spawn To x86": "%windir%\\syswow64\\rundll32.exe",   
"Method 1": "GET",   
"Spawn To x64": "%windir%\\sysnative\\rundll32.exe",   
"Polling": 60000,   
"C2 Server": "162.244.83.95,/match",   
"Port": 8080,   
"Method 2": "POST",   
"Jitter": 0,   
"Beacon Type": "0 (HTTP)" 
```

80.209.242[.]9



```
**ja3:** 72a589da586844d7f0818ce684948eea   
**ja3s:** ae4edc6faf64d08308082ad26be60767   
**Certificate**:[6e:ce:5e:ce:41:92:68:3d:2d:84:e2:5b:0b:a7:e0:4f:9c:b7:eb:7c ]  
**Not Before:** 2015/05/20 14:26:24  
**Not After:** 2025/05/17 14:26:24   
**Issuer Org**  
**Subject Common**  
**Subject Org**  
**Public Algorithm:**rsaEncryption
```

Config:



```
  
"x86":   
"sha256": "57d4976c4daee794299e5e7c6374db3494e9a1df1f967aa9010624099ed6da16",  
"time": 1621526952543.7,  
"sha1": "0aea959b387c58f1ac47fb6946d1330cab301c2e",  
"md5": "494db8c61916acc6ae99b868d4869089",  
"config":   
"Port": 80,  
"Spawn To x64": "%windir%\\sysnative\\rundll32.exe",  
"Spawn To x86": "%windir%\\syswow64\\rundll32.exe",  
"Beacon Type": "0 (HTTP)",  
"C2 Server": "80.209.242.9,/match",  
"HTTP Method Path 2": "/submit.php",  
"Method 2": "POST",  
"Method 1": "GET",  
"Polling": 60000,  
"Jitter": 0  
  
  
"x64":   
"sha256": "e468e4c9226f47815dee0bfd35a2b065e7375a7be228845e35607ea00c87b6ac",  
"time": 1621526967489.4,  
"sha1": "db3a7c60fc281a200a3cf1554bae5f99491fa744",  
"md5": "b4589d6f80fa1131e8ab7504793f878b",  
"config":   
"Port": 80,  
"Spawn To x64": "%windir%\\sysnative\\rundll32.exe",  
"Spawn To x86": "%windir%\\syswow64\\rundll32.exe",  
"Beacon Type": "0 (HTTP)",  
"C2 Server": "80.209.242.9,/updates.rss",  
"HTTP Method Path 2": "/submit.php",  
"Method 2": "POST",  
"Method 1": "GET",  
"Polling": 60000,  
"Jitter": 0  
  
"x86":   
"sha256": "e9a95e09e762020f23d238b364be8b5b61c6662099f5bdf4ac5a102bd31fec98",  
"time": 1621526949089.5,  
"sha1": "45d1f56ccbe33d0f8c727ef2c740fdd1b3eee01b",  
"md5": "d1f6ba82ba87e4a957e73160773e782a",  
"config":   
"Port": 443,  
"Spawn To x64": "%windir%\\sysnative\\rundll32.exe",  
"Spawn To x86": "%windir%\\syswow64\\rundll32.exe",  
"Beacon Type": "8 (HTTPS)",  
"C2 Server": "80.209.242.9,/ca",  
"HTTP Method Path 2": "/submit.php",  
"Method 2": "POST",  
"Method 1": "GET",  
"Polling": 60000,  
"Jitter": 0  
  
"x64":   
"sha256": "0fdf544145bd491fa7a19b24875f0231f414fbde07e50e1af219d063c08989f9",  
"time": 1621526962664.6,  
"sha1": "67213613a61c9552955e068ad417e48b7bad8fa6",  
"md5": "a4e1f497c424a259d2b52d6414a6365f",  
"config":   
"Port": 443,  
"Spawn To x64": "%windir%\\sysnative\\rundll32.exe",  
"Spawn To x86": "%windir%\\syswow64\\rundll32.exe",  
"Beacon Type": "8 (HTTPS)",  
"C2 Server": "80.209.242.9,/ca",  
"HTTP Method Path 2": "/submit.php",  
"Method 2": "POST",  
"Method 1": "GET",  
"Polling": 60000,  
"Jitter": 0
```

### Impact


In this intrusion we did not see a final action on objectives.


### IOC’s


**Files**



```
95.dll
98b2fff45a9474d61c1bd71b7a60712b
3b0ec4b6ad3cf558cac6b2c6e7d8024c438cfbc5
7b2144f2b5d722a1a8a0c47a43ecaf029b434bfb34a5cffe651fda2adf401131
  
95.bat
5b3c525c2883ba588d0cfe848c0151b3
012c934a2e4536398ac2c3a1614a3927709e7d61
28b3b7d1421b39ad747d3ddfe2322bfe505a00f43d0adab80671e9c442f1472e  
  
rem.r  
f7b1fc5b175b40bcddf6170ed265b442  
f67c640d6b00c7bcd0d498c8de1b6eee6868d41f50b63958880b915219d5364d08593dce44effd49a0f25f7b0609cab8f1e0ec5d  
  
0520\_656407893761.doc632c214b5a3f8bdfa91197e121f41db19744884a328416906de484acbe1200a83cb7b5fad43ec0226fd6af4d0848cd1fa2329b93fb73341814dd8536c53b6da0e31b3844
```

   
**Network** 



```
tembovewinated[.]ru   
prournauseent[.]ru   
sweyblidian[.]com   
vaethemanic[.]com   
q09pi7[.]ru   
   
216.250.248[.]88   
162.244.83[.]95   
80.209.242[.]9 
```

### Detections


**Suricata**   
ET POLICY External IP Lookup (ipfy.org)   
ET INFO Suspicious Empty SSL Certificate – Observed in Cobalt Strike   
ET INFO GENERIC SUSPICIOUS POST to Dotted Quad with Fake Browser 1   
ET NETBIOS DCERPC SVCCTL – Remote Service Control Manager Access   
ET TROJAN Observed Cobalt Strike User-Agent  
ETPRO TROJAN Tordal/Hancitor/Chanitor Checkin  
ETPRO TROJAN Cobalt Strike Beacon Observed


**Snort**



```
[Binary Defense Created](https://www.binarydefense.com/analysis-of-hancitor-when-boring-begets-beacon) - alert tcp any any -> any $HTTP\_PORTS (msg:"Possible Hancitor Checkin"; flow:established,to\_server; content:"POST"; http\_method;content:"GUID="; http\_client\_body; content:"&BUILD="; http\_client\_body; content:"&INFO="; http\_client\_body; content:"&EXT="; http\_client\_body; content:"&IP="; http\_client\_body; content:"&WIN="; http\_client\_body; reference:md5, 3c3a9a00b60c85c507ece4b4025d0f72; classtype:trojan-activity; sid:210611; rev:1;)
```

**Sigma**   
<https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/win_susp_svchost.yml>     
<https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/sysmon_rundll32_net_connections.yml>    
<https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/win_trust_discovery.yml>  


**YARA**



```
/*  
YARA Rule Set  
Author: The DFIR Report  
Date: 2021-06-27  
Identifier: 4301 Hancitor  
Reference: https://thedfirreport.com  
*/  
  
/* Rule Set ----------------------------------------------------------------- */  
  
import "pe"  
  
rule sig\_95\_dll\_cobalt\_strike {  
meta:  
description = "file 95.dll"  
author = "The DFIR Report"  
reference = "https://thedfirreport.com"  
date = "2021-06-24"  
hash1 = "7b2144f2b5d722a1a8a0c47a43ecaf029b434bfb34a5cffe651fda2adf401131"  
strings:  
$s1 = "TstDll.dll" fullword ascii  
$s2 = "!This is a Windows NT windowed dynamic link library" fullword ascii  
$s3 = "AserSec" fullword ascii  
$s4 = "`.idata" fullword ascii /* Goodware String - occured 1 times */  
$s5 = "vEYd!W" fullword ascii  
$s6 = "[KpjrRdX&b" fullword ascii  
$s7 = "XXXXXXHHHHHHHHHHHHHHHHHHHH" fullword ascii /* Goodware String - occured 2 times */  
$s8 = "%$N8 2" fullword ascii  
$s9 = "%{~=vP" fullword ascii  
$s10 = "it~?KVT" fullword ascii  
$s11 = "UwaG+A" fullword ascii  
$s12 = "mj\_.%/2" fullword ascii  
$s13 = "BnP#lyp" fullword ascii  
$s14 = "(N\"-%IB" fullword ascii  
$s15 = "KkL{xK" fullword ascii  
$s16 = ")[IyU," fullword ascii  
$s17 = "|+uo6\\" fullword ascii  
$s18 = "@s?.N^" fullword ascii  
$s19 = "R%jdzV" fullword ascii  
$s20 = "R!-q$Fl" fullword ascii   
condition:   
uint16(0) == 0x5a4d and filesize < 100KB and   
( pe.imphash() == "67fdc237b514ec9fab9c4500917eb60f" and ( pe.exports("AserSec") and pe.exports("TstSec") ) or all of them )   
}   
  
rule cobalt\_strike\_shellcode\_95\_dll {   
  
meta:   
description = "Cobalt Strike Shellcode"   
author = "The DFIR Report"   
reference = "https://thedfirreport.com"   
date = "2021-06-23"   
hash = "7b2144f2b5d722a1a8a0c47a43ecaf029b434bfb34a5cffe651fda2adf401131"   
  
strings:   
  
$str\_1 = { E8 89 00 00 00 60 89 E5 31 D2 64 8B 52 30 8B 52 }   
$str\_2 = "/hVVH"   
$str\_3 = "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; BOIE9;ENGB)"   
  
condition:   
3 of them  
  
}
```

**MITRE** 


User Execution – T1204  
Web Protocols – T1071.001  
Dynamic-link Library Injection – T1055.001  
Remote System Discovery – T1018  
Network Service Scanning – T1046  
Windows Service – T1543.003  
Domain Trust Discovery – T1482  
System Time Discovery – T1124  
Network Share Discovery – T1135  
File Deletion – T1070.004


Internal case 4301





#### Tags:
[[exe]] [[rundll32]] [[Hancitor]] [[HTTP]] [[C2]] [[windir]] [[x64]] [[x86]] [[php]] [[DLL]] [[The DFIR Report]]
