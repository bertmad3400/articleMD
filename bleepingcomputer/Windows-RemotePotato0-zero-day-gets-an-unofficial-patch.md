# Windows 'RemotePotato0' zero-day gets an unofficial patch
### A privilege escalation vulnerability impacting all Windows versions that can let threat actors gain domain admin privileges through an NTLM relay attack has received unofficial patches after Microsoft tagged it as won't fix.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/windows-remotepotato0-zero-day-gets-an-unofficial-patch/
+ Date: 2022-01-13T12:31:13-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/07/23/Windows-attack.jpg)

![Windows RemotePotato0 zero-day](https://www.bleepstatic.com/content/hl-images/2021/07/23/Windows-attack.jpg)


A privilege escalation vulnerability impacting all Windows versions that can let threat actors gain domain admin privileges through an NTLM relay attack has received unofficial patches after Microsoft tagged it as "won't fix."


The vulnerability, [dubbed RemotePotato0 SentinelOne researchers](https://www.sentinelone.com/labs/relaying-potatoes-another-unexpected-privilege-escalation-vulnerability-in-windows-rpc-protocol/) Antonio Cocomazzi and Andrea Pierini, who found it and disclosed it in April 2021, is a zero-day flaw (according to [Microsoft's own definition](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/tvm-zero-day-vulnerabilities)) that is yet to receive a CVE ID after Redmond refused to issue a fix.


It makes it possible for attackers to trigger authenticated RPC/DCOM calls and relay the NTLM authentication to other protocols, which allows them to elevate privileges to domain administrator, likely allowing full domain compromise.


"It allows a logged-in low-privileged attacker to launch one of several special-purpose applications in the session of any other user who is also currently logged in to the same computer, and make that application send said user's NTLM hash to an IP address chosen by the attacker," 0patch co-founder [Mitja Kolsek explained](https://blog.0patch.com/2022/01/free-micropatches-for-remotepotato0.html) in a blog post sharing info on free micropatches released to block RemotePotato0 exploitation on impacted servers.


"Intercepting an NTLM hash from a domain administrator, the attacker can craft their own request for the domain controller pretending to be that administrator and perform some administrative action such as adding themselves to the Domain Administrators group."


While the attackers would have to trick home users with admin privileges into logging in at the time of the attack for successful exploitation.


However, as Kolsek said, this is a lot easier on Windows Server systems since multiple users are logged simultaneously, including administrators, thus eliminating the social engineering requirement.


A video demo of the RemotePotato0 micropatch in action is embedded below.



Admins told to disable NTLM or correctly configure servers
----------------------------------------------------------


The Windows NT (New Technology) LAN Manager (NTLM) authentication protocol is used to authenticate remote users and to provide session security when requested by app protocols.


Kerberos has superseded NTLM, the current default auth protocol for domain-connected devices for all Windows 2000 and later.


Despite this, NTLM is still in use on Windows servers, allowing attackers to exploit vulnerabilities like RemotePotato0 designed to bypass NTLM relay attack mitigations.


[Microsoft told the researchers](https://www.sentinelone.com/labs/relaying-potatoes-another-unexpected-privilege-escalation-vulnerability-in-windows-rpc-protocol/) that Windows admins should either disable NTLM or [configure their servers to block NTLM relay attacks](http://Active%20Directory%20Certificate%20Services%20(AD%20CS)) using Active Directory Certificate Services (AD CS).


The researchers "hope that MS reconsider their decision not to fix this serious vulnerability" since RemotePotato0 can be exploited without requiring the target's interaction by relaying authentication to other protocols, unlike similar NTLM relay attack techniques using bugs like [CVE-2020-1113](https://blog.compass-security.com/2020/05/relaying-ntlm-authentication-over-rpc/) and [CVE-2021-1678](https://www.crowdstrike.com/blog/cve-2021-1678-printer-spooler-relay-security-advisory/).


Free patch available until Microsoft provides one
-------------------------------------------------


Until Microsoft decides to issue security updates for this vulnerability, the [0patch micropatching service](https://0patch.com/) has [released free unofficial patches](https://twitter.com/0patch/status/1458545386243727361) (known as micropatches).


0patch has developed the micropatches using information shared by Cocomazzi and Pierini in their April 2021 report.


The unofficial patches for RemotePotato0 are available for all Windows versions from Windows 7 to the latest Windows 10 version and from Windows Server 2008 to Windows Server 2019.


To install the micropatch on your system, you will first have to [create a 0patch account](https://central.0patch.com/) and then install the [0patch agent](https://0patch.com/).


After launching the agent, the micropatch will be applied automatically without a restart if you haven't enabled any custom patching enterprise policy to block it.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Ntlm]] [[Remotepotato0]] [[Microsoft]] [[0patch]] [[Micropatch]] [[Bleeping Computer]]
#### CVE's
[[CVE-2020-1113]] [[CVE-2021-1678]]

