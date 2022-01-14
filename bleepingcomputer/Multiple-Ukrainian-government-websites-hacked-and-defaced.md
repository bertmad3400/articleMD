# Multiple Ukrainian government websites hacked and defaced
### At least 15 websites belonging to various Ukrainian public institutions were compromised, defaced, and subsequently taken offline.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/multiple-ukrainian-government-websites-hacked-and-defaced/
+ Date: 2022-01-14T11:11:14-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/14/hacker-hacking.jpg)

![Hacker hacking](https://www.bleepstatic.com/content/hl-images/2022/01/14/hacker-hacking.jpg)


At least 15 websites belonging to various Ukrainian public institutions were compromised, defaced, and subsequently taken offline.


This includes the websites of the ministry of foreign affairs, agriculture, education and science, security and defense, and the online portal for the cabinet of ministers.


The defacement messages were posted in Ukrainian, Russian, and Polish, warning the sites' visitors that all citizen data uploaded to the public network had been compromised.



![Messages posted on defaced pages](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/FJDIGd5X0AISrJN.jpg)**Messages posted on defaced pages**  
*Twitter | [Maryna Fedorenko](https://twitter.com/MarynaFedorenko/status/1481904293376626690)*
At the time of writing this, some of the websites remain inaccessible as the country's IT specialists are still in the process of restoring them.



> 
> As a result of a massive cyber attack, the websites of the Ministry of Foreign Affairs and a number of other government agencies are temporarily down. Our specialists have already started restoring the work of IT systems, and the cyberpolice has opened an investigation.
> 
> 
> — Oleg Nikolenko (@OlegNikolenko\_) [January 14, 2022](https://twitter.com/OlegNikolenko_/status/1481880668195983362?ref_src=twsrc%5Etfw)


The Ukrainian cyber-police has also posted an announcement where they underline that no personal data was compromised due to these attacks and that the warning messages to visitors were false and only meant to scare citizens.


"In order to prevent the spread of the attack on other resources and localization of the technical problem, the work of other government sites was temporarily suspended," explains the [police announcement](https://cyberpolice.gov.ua/news/kiberpolicziya-sbu-ta-derzhspeczzvyazku-vstanovlyuyut-prychetnyx-do-kiberatak-na-sajty-derzhavnyx-struktur-1630/) (translated).


"Currently, the Cyberpolice Department together with the State Special Communications Service and the Security Service of Ukraine are collecting digital evidence and identifying those involved in the cyber attacks."


Sources have told journalist [Kim Zetter](https://twitter.com/KimZetter/status/1481890639029551106) that all 15 compromised Ukrainian sites were using an outdated version of the October CMS, vulnerable to [CVE-2021-32648](https://nvd.nist.gov/vuln/detail/CVE-2021-32648).


This is a critical (CVSS: 9.1) authentication flaw allowing an attacker to send a specially crafted request to perform a password reset on the platform, thus taking over admin accounts.


This vulnerability was fixed with [build 472 version 1.1.5](https://github.com/octobercms/october/security/advisories/GHSA-mxr5-mc97-63rc), released in August 2021, but it appears that several Ukrainian government websites hadn't applied the security updates.


A [later advisory](https://cert.gov.ua/article/17899) from the Ukraine cyber-police confirmed Zetter's reporting of the October CMS vulnerability as the intrusion vector.


Poland impacted too?
--------------------


Today, after Ukraine had acknowledged their attacks, the Polish Ministry of National Defense also announced that some of their databases containing sensitive military information were compromised.


The Ministry underlines that it's not sure whether the accessed database contained test files or actual data, and investigations are still ongoing.


However, members of the local press speak with certainty about the validity of the leaked files and the link to the Ukrainian cybersecurity incident.



> 
> Not just Ukrainian servers got hacked. In [#Poland](https://twitter.com/hashtag/Poland?src=hash&ref_src=twsrc%5Etfw) 1,8 million data points of military equipment, units were put online. That is the state of Polish F-16s or the location of single soldiers. Reported by [@OnetWiadomosci](https://twitter.com/OnetWiadomosci?ref_src=twsrc%5Etfw). This is big. Demands now that defense minister shall resign.
> 
> 
> — Philipp Fritz (@phil\_ipp\_fritz) [January 14, 2022](https://twitter.com/phil_ipp_fritz/status/1481955606818926595?ref_src=twsrc%5Etfw)


Actors unknown
--------------


The cyber-police has opened criminal proceedings under Article 361 (unauthorized interference with computers and computer networks), but the actors remain unknown.


Polish people noticed obvious grammatical errors in the messages posted on the defaced pages and claimed this was the product of Yandex translation. As such, the actor could be Russian.


Even though Ukraine is going through [extreme tensions](https://www.reuters.com/world/europe/russia-says-us-nato-talks-so-far-unsuccessful-2022-01-13/) with Russia, website defacement acts aren't the typical attack method of [a Russian state-sponsored hacking group like GRU](https://www.bleepingcomputer.com/news/security/us-indicts-russian-gru-sandworm-hackers-for-notpetya-worldwide-attacks/).


However, [researchers theorize](https://twitter.com/vxunderground/status/1481943972046123008) that the attacks could have been conducted by the GhostWriter APT hacking group, which has a history of targeting government entities in Poland and Ukraine.


In November, Mandiant released a report linking the Ghostwriter group to the Belarusian government.


"UNC1151 has targeted a wide variety of governmental and private sector entities, with a focus in Ukraine, Lithuania, Latvia, Poland, and Germany," explains a [report by Mandiant](https://www.mandiant.com/resources/unc1151-linked-to-belarus-government).


The targeting also includes Belarusian dissidents, media entities, and journalists. While there are multiple intelligence services that are interested in these countries, the specific targeting scope is most consistent with Belarusian interests."


Also, yesterday, the Ukrainian cyberpolice announced the [arrest of five ransomware affiliates](https://www.bleepingcomputer.com/news/security/ukranian-police-arrests-ransomware-gang-that-hit-over-50-firms/) responsible for over 50 attacks against companies worldwide.


The chances of this wave of defacements being a retaliative act are slim, as the messages don't mention anything relevant.





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=RTM]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Agriculture]] [[victim.industry.name=Education]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Belarus]] [[victim.continent.name=Europe]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.country.name=Latvia]] [[victim.continent.name=Europe]] [[victim.country.name=Lithuania]] [[victim.continent.name=Europe]] [[victim.country.name=Poland]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Websites]] [[Cyber-police]] [[Belarusian]] [[Bleeping Computer]]
#### CVE's
[[CVE-2021-32648]]

