# Atom Silo ransomware operators target vulnerable Confluence servers
### A weaponized exploit used by the cybercriminals was only disclosed in August.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/atom-silo-ransomware-operators-target-vulnerable-confluence-servers/)
+ Date: October 5, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A new ransomware operator is targeting Confluence servers by using a recently-disclosed vulnerability to obtain initial access to vulnerable systems. 


According to [Sophos cybersecurity](https://news.sophos.com/en-us/2021/10/04/atom-silo-ransomware-actors-use-confluence-exploit-dll-side-load-for-stealthy-attack/) researchers Sean Gallagher and Vikas Singh, the new threat actors, dubbed Atom Silo, are taking advantage of the flaw in the hopes that Confluence server owners are yet to apply the required security updates to resolve the bug.  

Atlassian Confluence is a web-based virtual workplace for the enterprise, allowing teams to communicate and collaborate on projects.  

Sophos described a recent attack conducted by Atom Silo over a period of two days. The vulnerability used in the attack, tracked as CVE-2021-08-25, allowed the cybercriminals to obtain initial access to the victim's corporate environment.   

The Confluence vulnerability is being actively exploited in the wild. While fixed in August, [the vendor warned](https://confluence.atlassian.com/doc/confluence-security-advisory-2021-08-25-1077906215.html) that Confluence Server and Confluence Data Center are at risk and should be patched immediately.  

If exploited, unauthenticated threat actors are able to perform an OGNL injection attack and execute arbitrary code. 

CVE-2021-08-25 was used to compromise the [Jenkins project](https://www.zdnet.com/article/jenkins-project-attacked-through-atlassian-confluence-vulnerability/) in September. [US Cybercom said](https://www.zdnet.com/article/us-cybercom-says-mass-exploitation-of-atlassian-confluence-vulnerability-ongoing-and-expected-to-accelerate/) in the same month that attacks were "ongoing and expected to accelerate." 






In the case examined by Sophos, Atom Silo utilized the vulnerability on September 13 and was able to use the code injection bug to create a backdoor, leading to the download and execution of a second, stealthy backdoor.  

To stay under the radar, this payload dropped a legitimate and signed piece of software vulnerable to an unsigned DLL sideload attack. A malicious .DLL was then used to decrypt and load the backdoor from a separate file containing code similar to a Cobalt Strike beacon, creating a tunnel for remotely executing Windows Shell commands through WMI.  

"The intrusion that made the ransomware attack possible made use of several novel techniques that made it extremely difficult to investigate, including the side-loading of malicious dynamic-link libraries tailored to disrupt endpoint protection software," the researchers say. 

Within a matter of hours, Atom Silo began moving laterally across its victims' network, compromising multiple servers in the process and executing the same backdoor binaries on each while also conducting additional reconnaissance.  

11 days after its initial intrusion, ransomware and a malicious Kernel Driver utility payload, designed to disrupt endpoint protection, were then deployed. Separately, another threat actor noticed the same system was vulnerable to CVE-2021-08-25 and quietly implanted cryptocurrency mining software.  

The ransomware is "virtually identical" to LockFile. Files were encrypted using the .ATOMSILO extension and a ransomware note demanding $200,000 was then dropped on the victim's system. 

"Ransomware operators and other malware developers are becoming very adept at taking advantage of these gaps, jumping on published proof of concept exploits for newly-revealed vulnerabilities and weaponizing them rapidly to profit off them," Sophos says. "To reduce the threat, organizations need to both ensure that they have robust ransomware and malware protection in place, and are vigilant about emerging vulnerabilities on Internet-facing software products they operate on their networks." 

###  Previous and related coverage

* [Atlassian CISO defends company's Confluence vulnerability response, urges patching](https://www.zdnet.com/article/atlassian-ciso-there-will-always-be-some-number-of-instances-of-software-on-the-internet-thats-out-of-date-and-being-exploited/)  

* [US Cybercom says mass exploitation of Atlassian Confluence vulnerability 'ongoing and expected to accelerate'](https://www.zdnet.com/article/us-cybercom-says-mass-exploitation-of-atlassian-confluence-vulnerability-ongoing-and-expected-to-accelerate/)  

* [Jenkins project attacked through Atlassian Confluence vulnerability](https://www.zdnet.com/article/jenkins-project-attacked-through-atlassian-confluence-vulnerability/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[ransomware]] [[Atlassian]] [[Sophos]] [[ZDNet]]
