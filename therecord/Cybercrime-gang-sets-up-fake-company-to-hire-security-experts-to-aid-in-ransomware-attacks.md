# Cybercrime gang sets up fake company to hire security experts to aid in ransomware attacks
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/cybercrime-gang-sets-up-fake-company-to-hire-security-experts-to-aid-in-ransomware-attacks/)
+ Date: October 21, 2021
+ Author: Catalin Cimpanu


## Article:
![Cybercrime gang sets up fake company to hire security experts to aid in ransomware attacks](https://therecord.media/wp-content/uploads/2021/05/hacker-keyboard.jpg)

* FIN7 hacking group created and operated a fake security company called Bastion Secure.
* The group used the company to recruit and trick security researchers into executing ransomware attacks.
* Bastion Secure recruited solely via Russian job portals.


**A cybercrime group known as FIN7 has created a fake security firm earlier this year, used it to hire security researchers, and then trick them into participating in ransomware attacks.**


Named **Bastion Secure**, the company claims to provide penetration testing services for private companies and public sector organizations across the world.


![Bastion Secure](https://www-therecord.recfut.com/wp-content/uploads/2021/10/BastionSecure-1024x680.png)
But according to an [investigation](https://geminiadvisory.io/fin7-ransomware-bastion-secure/) by Gemini Advisory, a division of Recorded Future, the company is a front for the [FIN7](https://malpedia.caad.fkie.fraunhofer.de/actor/fin7) group, which used the Bastion Secure website as a front to post ads on Russian job portals seeking to hire cybersecurity experts for various positions [[1](https://www.superjob.ru/vakansii/administrator-windows-setej-36641469.html), [2](https://ua.joblum.com/company/bastion-secure-ltd), [3](https://ua.jubee.org/ru/company/bastion-secure-ltd), [4](https://rabota.ua/company10418701), [5](https://jobs.ua/company-bastion-secure-ltd-1603731), [6](https://moscow.cataloxy.ru/firms/bastionsecure.com.htm – 74996423420), [7](https://remoteworkukraine.com/ua/company/ua-bastion-secure/)].


Ads on its website [[archived](https://web.archive.org/web/20211008191816/https://www.bastionsecure.com/vacancies.html)] show that FIN7 recruited reverse engineers, system administrators, C++, Python, and PHP programmers.


Those who applied went through a three-phase interviewing process; the Gemini Advisory team said today after one of its partners went through the process in order to study the shady company.


**Phase 1**  
The first phase included a basic interview process with an HR representative, typically carried out via Telegram. After a successful interview, the job applicants were told to sign a contract with a non-disclosure agreement and configure their computer by installing several virtual machines and opening certain ports.


**Phase 2**  
Applicants received legitimate penetration testing security tools from the company to conduct a series of test assignments.


**Phase 3**  
Applicants were brought in to participate in a “real” assignment where they were told to conduct a penetration test against one of Bastion Secure’s customers.


Gemini Advisory said that this last step in the interviewing process did not include any form of legal documents authorizing the penetration tests, as it’s customary in such cases, or explanation to participants.


Furthermore, Bastion Secure representatives also told applicants to use only specific tools that would not be detected by security software and to specifically look for backups and file storage systems once inside a company’s network.


### FIN7 group identified as operators of the Darkside RaaS


Tools shared by Bastion Secure with the Gemini partner who participated in the interviewing process were linked to malware strains like Carbanak and Lizar/Tirion, tools that have been historically part of FIN7’s arsenal.


In addition, Gemini Advisory said that tasks and operations assigned to applicants “matched the steps taken to prepare a ransomware attack.”


The attacks installed ransomware such as Ryuk or REvil, two ransomware strains that have been tied in recent years to FIN7 attacks, according to Gemini Advisory.


Newer attacks would have deployed the DarkSide and BlackMatter ransomware, according to security researchers from Microsoft, who have also been tracking the fake FIN7 security company.


In a talk at the Mandiant Cyber Defense Summit, Microsoft’s Nick Carr and Christopher Glyer said that FIN7 didn’t just deploy the Darkside ransomware (and its later [BlackMatter rebrand](https://therecord.media/blackmatter-ransomware-targets-companies-with-revenues-of-100-million-and-more/)) in attacks, but that FIN7 also managed the Darkside RaaS (Ransomware-as-a-Service) itself.





### FIN7 previously operated Combi Secure


But the tactic of operating a fake security firm isn’t particularly new for the FIN7 group, which also did the same thing back in the mid-2010s when they operated another fake security firm called Combi Security.


![Combi Security](https://www-therecord.recfut.com/wp-content/uploads/2021/10/CombiSecure-1024x507.png)
At the time, FIN7 was primarily engaged in deploying Point-of-Sale malware, and they used Combi Security to recruit penetration testers to breach retail company networks and then deploy said-PoS malware to collect payment card details from the hacked networks, according to an [indictment](https://www.justice.gov/opa/pr/three-members-notorious-international-cybercrime-group-fin7-custody-role-attacking-over-100) by the US Department of Justice.


### Hiring pen-testers is cheaper


As for the reasons why a criminal group like FIN7 would go to such great lengths to operate a fake security company not only once but twice, the answer is simple and has to do with operational costs and money, according to Gemini Advisory.


The reality is that it is cheaper to hire a security researcher than for FIN7 to work with other hacking groups or hackers recruited via underground forums.


A security researcher in Russia typically makes between $800 and $1,200 a month, according to Gemini Advisory, while criminal hackers would most likely want a percentage cut of the ransomware payment, which in some cases can easily reach millions of US dollars, Gemini Advisory said today.





#### Tags:
[[FIN7]] [[ransomware]] [[Darkside]] [[Combi]] [[The Record]]
