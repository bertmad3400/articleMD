# Researchers Caught Multiple Backdoors In Auerswald VoIP Phone System
### Auerswald addressed the backdoors issue with the latest firmware release for its VoIP phone systems, alongside patching other bugs.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2021/12/30/researchers-caught-multiple-backdoors-in-auerswald-voip-phone-system/
+ Date: 2021-12-30
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2021/12/pbx.jpg)
 Security researchers found numerous backdoors in Auerswald VoIP appliances risking users’ security. The vendors patched the flaw with the latest firmware releases. Thus, all users should ensure receiving the updates alongside implementing mitigation strategies to secure their devices.

 Auerswald VoIP Phone System Backdoors
-------------------------------------

 According to a [report](https://blog.redteam-pentesting.de/2021/inside-a-pbx/), researchers from the German cybersecurity firm RedTeam Pentesting GmbH discovered numerous backdoors in Auerswald VoIP appliances. Exploiting these could allow an adversary to gain administrative access to the device’s web-based management application.

 As elaborated in a [separate advisory](https://www.redteam-pentesting.de/en/advisories/rt-sa-2021-007/-auerswald-compact-multiple-backdoors), they found the backdoors while analyzing Auerswald COMpact 5500R PBX. Nonetheless, they confirmed that the same vulnerabilities also affect other appliances too.

 Regarding their backdoors, the advisory reads,

 
> Two backdoor passwords were found in the firmware of the COMpact 5500R PBX. One backdoor password is for the secret user “Schandelah”, the other can be used for the highest-privileged user “Admin”. No way was discovered to disable these backdoors.
> 
> 

 The researchers found the backdoors while assessing the firmware with [Ghidra](https://latesthackingnews.com/2019/03/10/ghidra-nsas-reverse-engineering-tool-now-available-for-free/) – NSA’s opensource tool reverse-engineering tool. They used the password reset functionality to dig deeper and found hard-coded credentials of a secretive admin account “Schandelah”.

 
> Analysis revealed that the corresponding password for this username is derived by concatenating the PBX’s serial number, the string “r2d2” and the current date, hashing it with the MD5 hash algorithm and taking the first seven lower-case hex chars of the result.
> 
> 

 Despite hashing, an adversary can easily decipher the password “by requesting the path “/about\_state”.

 Besides this, the researchers also found another backdoor account with the username “Admin” and an easy-to-derive password. The researchers have shared the method to figure out this password in their advisory.

 Mitigations and Patches
-----------------------

 After finding these backdoor accounts, an adversary can easily take over the target PBX device.

 Unfortunately, disabling these accounts isn’t possible. Nonetheless, the researchers recommend restricting or disabling the web-based management interface as a workaround.

 Thankfully, the vendors have addressed this issue with the latest [firmware release 8.2B](https://www.auerswald.de/en/start/news/article/new-firmware-update-82b). Hence, users must ensure updating their devices with this release to get the patches and avoid potential risks.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Backdoors]] [[Auerswald]] [[Voip]] [[Latest Hacking News]]

