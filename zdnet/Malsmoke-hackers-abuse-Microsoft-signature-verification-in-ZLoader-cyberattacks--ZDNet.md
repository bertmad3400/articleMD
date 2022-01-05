# Malsmoke hackers abuse Microsoft signature verification in ZLoader cyberattacks | ZDNet
### Malware exploits the system to steal credentials and other data.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/malsmoke-hackers-now-abuse-microsoft-e-signature-verification-tool-in-cyberattacks/
+ Date: 2022-01-05 11:03:43
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/0a23fd3fd1977148ea7e0c43698e65290bb65d8b/2021/11/02/0c449f08-f978-48e5-b0c2-6d0f588ad91e/sale-305237-article-image.jpg?width=770&height=578&fit=crop&auto=webp)

The Malsmoke hacking group is now abusing a vulnerability in Microsoft's e-signature verification tool to deploy malware and steal user data.


On Wednesday, Check Point Research (CPR) said that as of now, over [2,100 victims](https://research.checkpoint.com/2022/can-you-trust-a-files-digital-signature-new-zloader-campaign-exploits-microsofts-signature-verification-putting-users-at-risk/) have been detected worldwide in a new campaign, with the majority resident in the United States, Canada, and India – although evidence of the malware has been found in 111 countries.  

Dubbed ZLoader, the malicious code has been used in the past to deliver banking Trojans and has been closely connected to multiple [ransomware strains](https://www.cisa.gov/uscert/ncas/alerts/aa21-265a).  

The new campaign is thought to have started in November 2021. During its initial attack stages, the malware's operators have decided to use Atera, legitimate remote management software, as the springboard to infect a system. 

While it is not known how the malicious package containing Atera is currently being distributed, upon installation, Atera will also show a fake Java installer. This file, however, is busy installing an agent that connects the endpoint PC to an attacker's account, allowing them to remotely deploy malicious payloads.  

Two .bat files are then uploaded to the victim's machine: the first is responsible for tampering with Windows Defender, and the second is used to load ZLoader. During this stage, Windows Defender exclusions are added to stop the cybersecurity tool from launching alerts, existing software that may detect the manipulation of the task manager and cmd.exe is disabled, and further scripts used to disable "Admin Approval Mode" are executed.  

In addition, a script is added to the startup folder for persistence and a PC reboot is forced to apply the system changes.  






Of note is a signed, malicious .DLL file used to infect a machine with ZLoader, according [to the team](https://twitter.com/_CPResearch_/status/1463104303770578944). CPR said the file was modified and additional code was included by utilizing a known issue in the signature validation of crafted PE files, mentioned in [CVE-2020-1599](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-1599), [CVE-2013-3900](https://nvd.nist.gov/vuln/detail/CVE-2013-3900), and [CVE-2012-0151](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0151).  

![screenshot-2022-01-04-at-11-36-36.png]()![screenshot-2022-01-04-at-11-36-36.png](https://www.zdnet.com/a/img/resize/6ea21a05b8ed2aef5d06ca164523b02d94d62cbc/2022/01/04/20a27dd6-7beb-4041-bcdf-a13d126abcbf/screenshot-2022-01-04-at-11-36-36.png?width=370&fit=bounds&auto=webp)While a fix [was issued](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2013/ms13-098) years ago, false positives against legitimate installers resulted in the patch being [made opt-in](https://docs.microsoft.com/en-us/security-updates/securityadvisories/2014/2915720).

"Microsoft addressed the issue in 2013 with a Security Bulletin and pushed a fix," the researchers say. "However, they stated after implementing it that they "determined that impact to existing software could be high." Therefore, in July 2014, they pulled the stricter file verification and changed it to an opt-in update. In other words, this fix is disabled by default, which is what enables the malware author to modify the signed file."

The final ZLoader payload is then deployed. This malware, a [banking Trojan in its own right](https://www.zdnet.com/article/this-ransomware-dropping-malware-has-swapped-phishing-for-a-sneaky-new-attack-route/), is able to steal user credentials, cookies, and sensitive information – including financial account login data – as well as act as a backdoor and loader for other malicious code.  

In September, Microsoft warned that ZLoader is being spread through Google keyword advertisements to infect vulnerable PCs with Conti ransomware.  

CPR believes that [MalSmoke](https://blog.malwarebytes.com/threat-analysis/2020/11/malsmoke-operators-abandon-exploit-kits-in-favor-of-social-engineering-scheme/) is behind the latest campaign due to coding similarities, the use of Java plugins as fake installers, and due to connections between registrar records for domains previously used by the group to spread [Raccoon Stealer](https://www.zdnet.com/article/raccoon-stealer-as-a-service-will-now-try-to-steal-your-cryptocurrency/) malware. 

According to the researchers, the authentication gap being exploited is a problematic area as Microsoft's stricter signature options are not enabled by default – and while the cybersecurity firm recommends that users apply Microsoft's update for Authenticode verification, this may also occasionally flag up legitimate installers as having an invalid signature.  

"All in all, it seems like the ZLoader campaign authors put great effort into defense evasion and are still updating their methods on a weekly basis," commented Kobi Eisenkraft, Malware Researcher at Check Point. "I strongly urge users to apply Microsoft's update for strict Authenticode verification. It is not applied by default." 

Microsoft and Atera have been made aware of the researchers' findings. 

"We released a security update (CVE-2013-3900) in 2013 to help keep customers protected from exploitation of this vulnerability," a Microsoft spokesperson told ZDNet. "Customers who apply the update and enable the configuration indicated in the security advisory will be protected. Exploitation of this vulnerability requires the compromise of a user's machine or convincing a victim to run a specially crafted, signed PE file."

###  Previous and related coverage

* [MosesStaff attacks organizations with encryption malware: No payment demand made](https://www.zdnet.com/article/mosesstaff-attackers-deploy-ransomware-on-your-systems-no-payment-no-decryption-possible/)
* [Variant of Phorpiex botnet used for cryptocurrency attacks in Ethiopia, Nigeria, India and more](https://www.zdnet.com/article/variant-of-phorpiex-botnet-used-for-cryptocurrency-attacks-in-ethopia-nigeria-and-india/)
* [Hackers pretending to be Iranian govt steal credit card infomation and create botnet](https://www.zdnet.com/article/hackers-pretending-to-be-iranian-govt-use-sms-messages-to-steal-credit-card-info-create-botnet/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=cmd]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Ethiopia]] [[victim.continent.name=Africa]] [[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Niger]] [[victim.continent.name=Africa]] [[victim.country.name=Nigeria]] [[victim.continent.name=Africa]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.country.name=Canada]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Malware]] [[Zloader]] [[Atera]] [[ZDNet]]
#### CVE's
[[CVE-2020-1599]] [[CVE-2013-3900]] [[CVE-2012-0151]]

