# Ransomware attackers targeted this company. Then defenders discovered something curious
### Cybersecurity researchers detail a mysterious attack that uses sophisticated techniques to deliver a relatively unsophisticated ransomware. The question is, why?

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/ransomware-attackers-targeted-this-company-then-defenders-discovered-something-curious/)
+ Date: September 23, 2021
+ Author: Danny Palmer


## Article:
Unknown

Cybersecurity researchers have detailed a ransomware campaign that clearly borrows attack techniques used by nation-state-backed hacking and cyber-espionage operations. 

The campaign came to light when cyber criminals attempted to launch a ransomware attack against an unspecified product safety testing organisation. The attack was detected and stopped before it was successful, but [provided cybersecurity researchers at eSentire](https://www.esentire.com/security-advisories/ransomware-hackers-attack-a-top-safety-testing-org-using-tactics-and-techniques-borrowed-from-chinese-espionage-groups) with enough information to analyse the tactics, techniques and procedures being used.


As eSentire's security research team began to investigate the incident, they said they "discovered some very curious findings, relating to both the threat group behind the attack, as well as the tools and techniques used in the attack". 

**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)**

The attack methods used in attempted ransomware campaign resembled techniques previously attributed to state-backed Chinese hacking operations including [APT27 – also known as Emissary Panda](https://www.zdnet.com/article/deadringer-chinese-apts-strike-major-telecommunications-companies/). 

eSentire said the low quality of the ransomware and the lack of any known ransomware breaches by this 'Hello Ransomware', along with the attackers' use of intrusion and reconnaissance methods that are typically associated with sophisticated groups, raises the question of whether the ransomware is the primary goal of the operators. 

"Or are the cyber criminals dropping ransomware into their target victims' IT environment to simply distract from their real motive – cyber espionage?" eSentire said.






While all of this doesn't necessarily mean that those behind the ransomware are working out of or on behalf of China, it demonstrates how cyber criminals can mimic the tactics used by advanced government-backed hacking groups in an effort to deliver [malware](https://www.zdnet.com/article/what-is-malware-everything-you-need-to-know-about-viruses-trojans-and-malicious-software/). 

Techniques deployed in the attempted attack in July include the use of SharePoint exploits and [China Chopper](https://www.zdnet.com/article/hafniums-china-chopper-a-slick-and-tiny-web-shell-for-creating-server-backdoors/), a stealthy remote access tool that provides a backdoor onto compromised systems, often distributed onto web servers. [While commonly used by Chinese APT groups](https://www.zdnet.com/article/deadringer-chinese-apts-strike-major-telecommunications-companies/), China Chopper web shell is widely available and is popular with a variety of attackers, both state-backed and cyber criminal. 

But the use of these exploits and China Chopper aren't the only techniques the attackers behind ransomware use alongside APT groups, such as using Mimikatz for password scraping and privilege escalation, attempts to disable security monitoring, as well as dropping PowerShell command executions via masquerading as a legitimate anti-virus provider – in this case, mimicking Kaspersky.  

There are also time delays between different steps of the attack in an effort to avoid detection. These time delays also [suggest a hands-on human touch](https://www.zdnet.com/article/hackers-are-getting-more-hands-on-with-their-attacks-thats-not-a-good-sign/) when carrying out the attacks, something that's common with APT groups. 

While the methodology is the same as that used by nation-state hacking groups, it would be unusual for a state-sponsored group to directly engage in ransomware attacks. [Wannacry ransomware](https://www.zdnet.com/article/ransomware-how-the-nhs-learned-the-lessons-of-wannacry-to-protect-hospitals-from-attack/), deployed by North Korea, is an infamous example of an attempted ransomware attack by a state, but on the whole, ransomware is the domain of cyber criminals. 

There's the possibility that those behind ransomware are performing a false flag operation, deploying tactics known to be used by a particular operation because it leads any investigation away from them. It's also well-known that the tactics are an effective means of compromising networks – meaning they're perfect for ransomware attacks. 

Like other forms of ransomware, Hello encrypts files – in this case with a .hello extension – and demands a ransom from victims in exchange for the decryption key. The ransom note is fairly basic, using Notepad to present a ransom note telling the victim to email the attackers to negotiate a deal.  

Hello ransomware is also quite basic by the standards of top ransomware in 2021 because [there's no threat to leak stolen data](https://www.zdnet.com/article/ransomware-theres-been-a-big-rise-in-double-extortion-attacks-as-gangs-try-out-new-tricks/) and no leak site for publishing stolen data on. It also isn't run on a ransomware-as-a-service model, like many of the most prolific ransomware variants today, meaning that it stands out. 

Despite all this, the hands-on nature of attacks indicates that whoever is behind Hello ransomware knows what they're doing. 

"Hello ransomware is an exception of ransomware evolution. There's nothing particularly sophisticated about the ransomware itself, or even the initial access vector, a two-year-old SharePoint vulnerability," Keegan Keplinger, research and reporting lead at eSentire, told ZDNet. 

"It is the post-compromise actions which can really be considered sophisticated," he added. 


Researchers even suggest the possibility that the ransomware could be laid down as a distraction while laying the foundations for something else.  

**SEE:** [**Four months on from a sophisticated cyberattack, Alaska's health department is still recovering**](https://www.zdnet.com/article/four-months-on-from-sophisticated-cyber-attack-alaskas-health-services-is-still-recovering/)

"There is a stark difference between the sophisticated intrusion capabilities, used in conjunction with the seemingly simplistic Hello Ransomware. This, in addition to the little-publicised success of the Hello ransomware campaigns, also bring the actors' motivations into question," said Keplinger. 

The campaign remains mysterious, but while the attack targeting the safety testing organisation was stopped before it was able to encrypt the network, others might not be so lucky. 

Steps that businesses can take to help avoid falling victim to ransomware – and many other forms of cyberattacks – include [applying security patches for known vulnerabilities](https://www.zdnet.com/article/this-one-change-could-protect-your-systems-from-attack-so-why-dont-more-companies-do-it/) in a timely manner and using [multi-factor authentication across the network](https://www.zdnet.com/article/multi-factor-authentication-use-it-for-all-the-people-that-access-your-network-all-the-time/) to make it more difficult for intruders to move around networks. 





#### Tags:
[[ransomware]] [[eSentire]] [[groups,]] [[ZDNet]]
