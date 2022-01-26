# Linux Bug in All Major Distros: ‘An Attacker’s Dream Come True’
### Every major Linux distribution has an easily exploited memory-corruption bug that’s been lurking for 12 years – a stunning revelation that’s likely to be followed soon by in-the-wild exploits.  Found in polkit’s pkexec – a tool for controlling system-wide privileges in Unix-like operating systems that allows a user to execute commands as another user, serving

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177996
+ Date: 2022-01-26T17:52:49+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/26113325/DreamDoorClouds-scaled-e1643214849877.jpg)

Every major Linux distribution has an easily exploited memory-corruption bug that’s been lurking for 12 years – a stunning revelation that’s likely to be followed soon by in-the-wild exploits.


Found in [polkit’s pkexec](https://access.redhat.com/security/vulnerabilities/RHSB-2022-001#:~:text=Pkexec%2C%20part%20of%20polkit%2C%20is,definitions%20using%20the%20setuid%20feature.) – a tool for controlling system-wide privileges in Unix-like operating systems that allows a user to execute commands as another user, serving as an alternative to [sudo](https://en.wikipedia.org/wiki/Sudo) – successful exploitation gives full root access to any unprivileged user.


Qualys researchers, who discovered the long-dormant powderkeg and named it PwnKit, said in a Tuesday [report](https://blog.qualys.com/vulnerabilities-threat-research/2022/01/25/pwnkit-local-privilege-escalation-vulnerability-discovered-in-polkits-pkexec-cve-2021-4034) that they developed an exploit and obtained full root privileges on default installations of Ubuntu, Debian, Fedora and CentOS, while they believe that other Linux distributions are “likely vulnerable and probably exploitable.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“This vulnerability is an attacker’s dream come true,” Qualys researchers [said](https://www.openwall.com/lists/oss-security/2022/01/25/11).


They offered these other reasons why attackers are probably misty-eyed right now:


* pkexec has been vulnerable since its creation, in May 2009;
* any unprivileged local user can exploit this vulnerability to obtain full root privileges;
* although this vulnerability is technically a memory corruption, it is exploitable instantly, reliably, in an architecture-independent way; and
* it is exploitable even if the polkit daemon itself is not running.


“This vulnerability allows any unprivileged user to gain full root privileges on a vulnerable host by exploiting this vulnerability in its default configuration,” Bharat Jogi, director of vulnerability and threat research at Qualys, [said](https://blog.qualys.com/vulnerabilities-threat-research/2022/01/25/pwnkit-local-privilege-escalation-vulnerability-discovered-in-polkits-pkexec-cve-2021-4034) in a Wednesday post, adding that the flaw “has been hiding in plain sight for 12+ years and affects all versions of pkexec since its first version in May 2009.”


Polkit also supports non-Linux operating systems such as Solaris and *BSD, but Qualys hasn’t yet investigated their exploitability. Researchers said that OpenBSD is not exploitable, “because its kernel refuses to execve() a program if argc is 0.”


Polkit (formerly PolicyKit) provides an organized way for non-privileged processes to communicate with privileged processes, Qualys explained, and can be used to execute commands with elevated privileges using the command pkexec followed by the command intended to be executed (with root permission).


If there’s one saving grace in this [Log4j](https://threatpost.com/microsoft-rampant-log4j-exploits-testing/177358/)-esque, déjà vu situation, it’s that PwnKit is a local privilege escalation vulnerability. “Any vulnerability that gives root access on a Linux system is bad. Fortunately, this vulnerability is a Local exploit, which mitigates some risk,” Yaniv Bar-Dayan, CEO and co-founder at Vulcan Cyber, told Threatpost on Wednesday.


Technical Details
-----------------


Qualys has provided some technical details, though it’s abstained from sharing its proof-of-concept (PoC) before patches are widely available. In a nutshell, an out-of-bounds write vulnerability allows for re-introduction of an “unsecure” environment variable (for example, LD\_PRELOAD) into pkexec’s environment, the researchers explained.


“These ‘unsecure’ variables are normally removed (by ld.so) from the environment of SUID programs before the main() function is called,” they said.


Qualys shared the following video, which demonstrates a potential exploit path.



Patch or Mitigate ASAP
----------------------


Qualys said that it expects vendors to release patches sooner rather than later, and it’s recommending that users make haste in patching when those patches are available. “Given the breadth of the attack surface for this vulnerability across both Linux and non-Linux OS, Qualys recommends that users apply patches for this vulnerability immediately,” its researchers advised.


Given the ease of exploit, Qualys also expects public exploits to become available quick-time:


“We anticipate public exploits to become available within a few days of this blog’s post date,” researchers said on Tuesday.


If there aren’t patches already available for a given operating system, there’s a mitigation: “Remove the SUID-bit from pkexec as a temporary mitigation,” Qualys suggested, giving this example:


# chmod 0755 /usr/bin/pkexec


Latest Example of the Need for SBOMs
------------------------------------


Greg Fitzgerald, co-founder, Sevco Security, noted to Threatpost that these types of bugs – ones that have been lurking in networks for more than a decade – can create serious problems for security teams, who often don’t even know where to find all the instances of a newly problematic piece of their infrastructure.


Stop us if you’ve heard this one before, but Pkexec – just like the similarly open-source Apache Log4j logging library that’s still rocking the internet – is ubiquitous across many enterprises.


Fitzgerald said that the priority for organizations right now “has to be patching Linux machines across the enterprise.”


That is, the priority is to patch all machines that IT and security teams know about, he pointed out. Unfortunately, and this gets back to the screaming need for [software bills of material](https://threatpost.com/2022-software-bill-of-materials/177736/) (SBOMs), “there are not many companies with an accurate IT asset inventory that dates back more than a decade,” Fitzgerald understated.


Thus, even if an organization patches all of the machines they’re aware of, they could still be susceptible to the PwnKit vulnerability because they lack an accurate inventory of their IT assets, Fitzgerald said: “You can’t apply a patch to an asset you don’t know is on your network. Abandoned and unknown IT assets are often the path of least resistance for malicious actors trying to access your network or data.”


Open-Source Bugs: Good, Bad & Badder
------------------------------------


Vulcan Cyber’s Bar-Dayan called the open-source software model a two-edged blade: “On one side, everyone can look at the code and audit it to identify and patch vulnerabilities. On the other side, threat actors can look at the code and find subtle issues that everyone else has missed,” he explained. “The advantages of this model have historically outweighed the disadvantages, with many eyes on the code and patches frequently appearing very rapidly after a vulnerability comes to light.”


He sees a future where auditing will help to catch and correct vulnerabilities before they’re used in the wild – a future that also entails improved integration with vulnerability and patch management tools that will make open-source-software-based systems even more secure and easy to maintain.


On the blade’s flip side of open-source is that there’s no one vendor holding the bag. Bud Broomhead, CEO at Viakoo, provider of automated IoT cyber hygiene, told Threatpost that the fact that pkexec is an open-source component makes this bug “a big deal.”


After all, there’s no one vendor to blame, and no one vendor to turn to for a fix: “Unlike fully proprietary systems where a single manufacturer can issue a single patch to address a vulnerability, a single open-source vulnerability can be present in multiple systems (including proprietary ones) which then requires multiple manufacturers to separately develop, test, and distribute a patch,” Broomhead said.


That adds “enormous time and complexity” for both the manufacturer and end user when it comes to implementing a security fix for a known vulnerability, he added.


This tangled net makes open-source systems extremely attractive to threat actors. “Vulnerabilities that exploit open-source systems (like the recent Log4j vulnerability) require patches and updates to be developed by multiple device or system manufacturers, and threat actors are betting on some manufacturers being slow in releasing fixes and some end users being slow in updating their devices,” Broomhead noted.


Besides mandatory SBOMs, Broomhead said that the future has got to entail automated deployment of security fixes and extending [Zero Trust](https://threatpost.com/zero-trust-future-security-risks/177502/) to IoT/OT systems.


He ticked off the improvements that those three things would usher in: “Having clarity over what is in a software distribution via an SBOM makes finding vulnerable systems easier,” he enumerated. “Automated implementation of security fixes is needed to address the scale issue, both number and geography, especially with IoT systems. And extending Zero Trust to IoT/OT devices can add additional security to prevent vulnerabilities from being exploited.”


This Won’t Be the Last Horror Show
----------------------------------


As with proprietary, so it goes with open-source: The parade of new technologies never stops. That parade ushers in new vulnerabilities and problems, as noted by John Bambenek, principal threat hunter at Netenrich.


“Compromised infrastructure is particularly useful to attackers who wish to use someone else’s resources to launch their attacks or otherwise obfuscate their identities,” Bambenek told Threatpost. “We will keep adopting new technologies in the Linux world that will introduce new vulnerabilities and problems for organizations. We are only just now getting our hands around cloud asset management, and asset management is essentially the first step of any security program.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Bread]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.city.name=Quito]] [[victim.country.name=Ecuador]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Qualys]] [[Open-source]] [[Pkexec]] [[Linux]] [[Threatpost]] [[Fitzgerald]] [[Broomhead]] [[Pwnkit]] [[ThreatPost]]

