# Hackers take over diplomat's email, target Russian deputy minister
### Hackers believed to work for the North Korean government have compromised the email account of a staff member of Russia's Ministry of Foreign Affairs (MID) and deployed spear-phishing attacks against the country's diplomats in other regions.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/hackers-take-over-diplomats-email-target-russian-deputy-minister/
+ Date: 2022-01-12T03:35:06-05:00
+ Author: Ionut Ilascu


## Article:
![Article Image](https://www.bleepstatic.com/content/posts/2022/01/11/Figure7_HNYScreenSaver.jpg)

![Konni hackers compromise Russian Ministry of Foreign Affairs email account](https://www.bleepstatic.com/content/posts/2022/01/11/Figure7_HNYScreenSaver.jpg)


Hackers believed to work for the North Korean government have compromised the email account of a staff member of Russia’s Ministry of Foreign Affairs (MID) and deployed spear-phishing attacks against the country’s diplomats in other regions.


One of the targets was Sergey Alexeyevich Ryabko, the deputy foreign minister for the Russian Federation, among other things responsible for bilateral relations with North and South America.


The phishing campaign started since at least October 19, 2021, deploying Konni malware, a remote administration tool (RAT) associated with the cyber activity from North Korean hackers known as APT37 (or StarCruft, Group123, Operation Erebus, and Operation Daybreak).


### Russian diplomatic targets


Cybersecurity firm Cluster25 last week [published research](https://cluster25.io/2022/01/03/konni-targets-the-russian-diplomatic-sector/) about a phishing campaign towards the end of December 2021 that delivered Konni RAT to individuals in the Russian diplomatic apparatus.


The researchers found that the hackers used the New Year theme as a decoy in emails to staff at the Russian embassy in Indonesia.



![Konni phishing email](https://www.bleepstatic.com/images/news/u/1100723/2022/APT%20Groups/Konni/KonniPhish_Emails-Cluster25.jpg)source: Cluster25
It was a congratulatory message that appeared to be from fellow diplomats at the Russian embassy in Serbia sending a ZIP archive with a holiday screensaver.


When extracted, the file was an executable that ultimately delivered the Konni RAT disguised as Windows service “scrnsvc.dll.”



![Konni infection chain](https://www.bleepstatic.com/images/news/u/1100723/2022/APT%20Groups/Konni/KonniRussiaPhish.jpg)source: Cluster25
Researchers at Lumen’s Black Lotus Labs were also tracking these spear-phishing campaigns that had started at least two months earlier, the likely goal being to harvest credentials of an active MID account.


To achieve their objective, the attackers relied on spoofed hostnames for email services common in Russia, Mail.ru and Yandex.


Another campaign started around November 7, delivering URLs for downloading an archive with documents asking for information on the vaccination status.


The archive also included an executable posing as legitimate software used for checking the Covid-19 vaccination status, which executed a malware loader that infected the system with Konni.


According to Black Lotus Labs researchers, the campaign in December also spotted by Cluster25 was the third one from the same threat actor and used the compromised MID account “mskhlystova@mid[.]ru” to send out malicious emails.


The recipients of the malicious messages were the Russian embassy in Indonesia and Russian politician Sergey Alexeyevich Ryabkov, currently serving as Deputy Foreign Minister.



![Konni spear-phishing targeting Russian diplomats](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)source: Lumen's Black Lotus Labs
Looking at the email headers revealed that the source of the messages was the same IP address, 152.89.247[.]26, used for the phishing campaign in October, [Black Lotus Labs found](https://blog.lumen.com/new-konni-campaign-targeting-russian-ministry-of-foreign-affairs/).


Technical analysis of the infection chain from Lumen’s researchers confirmed Cluster25’s findings, including the evasion technique of hiding a payload in a “401 unauthorized” server error response.



![Konni campaign - hiding payload in 401 server response](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)source: Cluster25
Black Lotus Labs researchers say that this was a highly targeted campaign that “downloaded a first-stage agent which is nearly identical to the agent” [discovered by Malwarebytes](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/) in a Konni attack against Russian targets.


Both cybersecurity outfits are confident in attributing the spear-phishing campaigns against the Russian diplomatic entities to the Konni advanced persistent threat.





## Tags:

#### Threatactor:
[[threatactor.name=APT3]] [[threatactor.name=APT37]] [[threatactor.name=APT37]]

#### Action:
[[action.malware.name=ABK]] [[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=KONNI]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Indonesia]] [[victim.continent.name=Asia]] [[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.country.name=Serbia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Konni]] [[Cluster25]] [[Spear-phishing]] [[Phishing]] [[Bleeping Computer]]

