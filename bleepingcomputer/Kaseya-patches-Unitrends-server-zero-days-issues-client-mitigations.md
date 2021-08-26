# Kaseya patches Unitrends server zero-days, issues client mitigations
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/kaseya-patches-unitrends-server-zero-days-issues-client-mitigations/)
+ Date: August 26, 2021
+ Author: Sergiu Gatlan


## Article:
![Kaseya patches Unitrends server zero-days, issues client mitigations](https://www.bleepstatic.com/content/hl-images/2021/07/05/Kaseya.jpg)


American software company Kaseya has issued a security update to patch server-side Kaseya Unitrends zero-day vulnerabilities found by security researchers at the Dutch Institute for Vulnerability Disclosure (DIVD).


[Kaseya Unitrends](https://www.unitrends.com/) is a cloud-based enterprise backup and recovery solution provided as a stand-alone solution or an add-on for Kaseya's VSA remote management platform.


The vulnerabilities (an authenticated remote code execution bug and a privilege escalation from read-only user to admin) were discovered on July 2 and privately disclosed to Kaseya the next day.


Roughly two weeks later, on July 14, DIVD began scanning the Internet for exposed Kaseya Unitrends instances to inform owners to get vulnerable servers offline until a patch was released.


[DIVD publicly disclosed the vulnerabilities via a TLP:AMBER advisory](https://www.bleepingcomputer.com/news/security/researchers-warn-of-unpatched-kaseya-unitrends-backup-vulnerabilities/) on July 26 after it got leaked online following a coordinated disclosure involving 68 government CERTs.


Client unauth RCE still waiting for a patch
-------------------------------------------


Kaseya released Unitrends version 10.5.5-2 on August 12 to patch the two server vulnerabilities, but it's still working on a fix for a third unauthenticated remote code execution flaw impacting the client.


"The client side vulnerability is current unpatched, but Kaseya urges users to mitigate these vulnerabilities via firewall rules as per their [best prectices and firewall requirements](https://support.unitrends.com/hc/en-us/articles/360013264518)," DIVD said in an [advisory published today](https://csirt.divd.nl/2021/08/26/Kaseya-Unitrends-update/).


"In addition to that they have released a [knowledge base article](https://support.unitrends.com/hc/en-us/articles/4404684084369-RCE-KB) with steps to mitigate the vulnerability."


After releasing the patched Unitrends version, Kaseya reached out to customers advising them to patch vulnerable servers and apply client mitigations.


Luckily, unlike the [Kaseya VSA zero-days](https://www.bleepingcomputer.com/news/security/kaseya-was-fixing-zero-day-just-as-revil-ransomware-sprung-their-attack/) REvil used in the [early July ransomware attack](https://www.bleepingcomputer.com/news/security/revil-ransomware-hits-1-000-plus-companies-in-msp-supply-chain-attack/) that hit hundreds of Kaseya customers, these three vulnerabilities are more difficult to exploit.


This is because attackers would need valid credentials to launch a remote code execution attack or escalate privileges on Internet-exposed and vulnerable Unitrends servers.


Furthermore, the threat actors are also required to have already breached their targets' networks to exploit the unauthenticated client RCE flaw successfully.


Additionally, DIVD Chairman [Victor Gevers](https://twitter.com/0xDUDE) told BleepingComputer that, despite being found on the networks of organizations from sensitive industries, the amount of vulnerable Unitrends instances is low.




#### Tags:
[[Kaseya]] [[Unitrends]] [[DIVD]] [[Bleeping Computer]]
