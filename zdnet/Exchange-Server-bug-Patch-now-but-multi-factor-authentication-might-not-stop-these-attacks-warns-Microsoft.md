# Exchange Server bug: Patch now, but multi-factor authentication might not stop these attacks, warns Microsoft
### Even if an Exchange account has multi-factor authentication enabled, an attacker could use this vulnerability to compromise email accounts.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/exchange-server-bug-patch-now-but-mfa-might-not-stop-these-attacks-warns-microsoft/)
+ Date: November 10, 2021
+ Author: Liam Tung


## Article:
Unknown

Microsoft has released security updates for its Exchange on-premises email server software that businesses should take on board. 

The security updates are for flaws in Exchange Server 2013, 2016, and 2019 -- the on-premises versions of Exchange that were compromised earlier this year by [the Beijing-backed hacking group that Microsoft calls Hafnium](https://www.zdnet.com/article/everything-you-need-to-know-about-microsoft-exchange-server-hack/). Four vulnerabilities in on-premises Exchange server software were exploited, and now Microsoft has warned that one newly-patched flaw -- tracked as CVE-2021-42321 -- is also under attack. 

The Exchange security updates were released as part of [Microsoft's November 2021 Patch Tuesday](https://www.zdnet.com/article/microsoft-november-2021-patch-tuesday-55-bugs-patched-two-under-active-exploit/) updates for Windows, the Edge browser, the Office suite, and other software products. 

"The Exchange bug CVE-2021-42321 is a "*post-authentication* vulnerability in Exchange 2016 and 2019. Our recommendation is to install these updates *immediately* to protect your environment," [Microsoft said in a blog post](https://techcommunity.microsoft.com/t5/exchange-team-blog/released-november-2021-exchange-server-security-updates/ba-p/2933169) about the new Exchange bugs. 

"These vulnerabilities affect on-premises Microsoft Exchange Server, including servers used by customers in Exchange Hybrid mode. Exchange Online customers are already protected and do not need to take any action," Microsoft notes.  

Attacks that affect users after authentication are risky because they affect users who have authenticated with legitimate but stolen credentials. Some post-authentication attacks can render two-factor authentication useless [since the malware does its trick after a person has authenticated](https://www.zdnet.com/article/google-disrupts-massive-phishing-and-malware-campaign/) with a second factor. 

The China-based attackers accessed Exchange Servers through the four bugs or stolen credentials, allowing them to create web shells -- a command-line interface -- to remotely communicate with an infected computer. Web shells are handy for attackers because [they can survive on a system after a patch](https://www.zdnet.com/article/fbi-blasts-away-web-shells-on-us-servers-in-wake-of-exchange-vulnerabilities/) and need to be manually removed. 






Attackers generally go after admin credentials to run malware, but they also use connections that aren't protected by a VPN. Alternatively, [they attack VPNs](https://www.zdnet.com/article/ransomware-crooks-are-targeting-vulnerable-vpn-devices-in-their-attacks/) themselves. 

Microsoft provides detailed update instructions that Exchange admins should follow, including updating the relevant cumulative updates (CU) for Exchange Server 2013, 2016, and 2019. 

The company cautions that admins should update to one of the supported CUs: it won't be providing updates to unsupported CUs, which won't be able to install the November security updates.  

Microsoft confirmed that two-factor authentication (2fa) won't necessarily protect against attackers exploiting the new Exchange flaws, particularly if an account has already been compromised. 

"If auth is successful (2FA or not) then CVE-2021-42321 could be exploitable," says Microsoft program manager Nino Bilic.  

"But indeed, 2FA can make authentication be harder to go through so in that respect, it can 'help'. But let's say if there is an account with 2FA that has been compromised -- well, in that case it would make no difference," Bilic adds. 

To detect compromises, Microsoft recommends running the PowerShell query on your Exchange server to check for specific events in the Event Log: 

*Get-EventLog -LogName Application -Source "MSExchange Common" -EntryType Error | Where-Object { $\_.Message -like "*BinaryFormatter.Deserialize*" }* 




 





#### Tags:
[[Microsoft]] [[on-premises]] [[CVE-2021-42321]] [[ZDNet]]
