# More than 1,200 phishing toolkits capable of intercepting 2FA detected in the wild
### A team of academics said it found more than 1,200 phishing toolkits deployed in the wild that are capable of intercepting and allowing cybercriminals to bypass two-factor authentication (2FA) security codes.

## Information:
+ Source: The Record
+ Link: https://therecord.media/more-than-1200-phishing-toolkits-capable-of-intercepting-2fa-detected-in-the-wild/
+ Date: 2021-12-27T15:29:00+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2021/12/2FA.png)

A team of academics said it found more than 1,200 phishing toolkits deployed in the wild that are capable of intercepting and allowing cybercriminals to bypass two-factor authentication (2FA) security codes.


Also known as **MitM (Man-in-the-Middle) phishing toolkits**, these tools have become extremely popular in the cybercrime underworld in recent years after major tech companies started making 2FA a default security feature for their users.


The direct result was that threat actors who managed to trick a user into entering credentials on a phishing site found that the stolen credentials became useless since they couldn’t bypass the 2FA procedure.


To counter this new trend in account security protections, since at least 2017, threat actors started adopting new tools that would allow them to bypass 2FA by stealing a user’s authentication cookies, which are files created inside a web browser once the user has logged into an account after the 2FA process was completed.


In most instances, cybercrime groups have relied on a malware category known as an “infostealer” to steal these authentication cookie files from computers they managed to infect.


However, there is another way to steal these files that does not rely on infecting a computer with malware—namely, by stealing the authentication cookies while they transit the internet from the service provider to a user’s computer.


#### Explained: Real-time phishing -vs- MitM phishing


For the past few years, cybercriminals have been slowly adapting their old phishing toolkits to go around 2FA procedures, primarily by using two techniques.


The first one is known as “**real-time phishing**“[[1](https://www.mandiant.com/resources/reelphish-real-time-two-factor-phishing-tool), [2](https://www.cyjax.com/2020/07/14/two-factor-fail-analysis-of-a-modern-phishing-kit/)] and relies on an operator sitting in front of a web panel while a user is navigating and interacting with a phishing site.


The idea is that once a user enters their credentials on the phishing site, the operator uses these credentials to authenticate themselves on the real site.


When the attacker is presented with a 2FA challenge, the threat actor simply pushes a button that prompts the user for the actual 2FA code (received via email, SMS, or authenticator app) and then collects and enters the 2FA token on the real site, creating a legitimate connection between their (attacker) system and the victim’s account.


![Real-Time-Phishing](https://therecord.media/wp-content/uploads/2021/12/Real-Time-Phishing.png)Image: Cyjax
Typically, real-time phishing tools are used for breaking into web banking portals, where user login sessions don’t stay active longer than a few minutes, and every re-authentication request needs another 2FA code.


Attackers that use real-time phishing don’t bother collecting authentication cookies—since these have a short life—and typically steal user funds from an account right away, burning their access.


However, mundane services like email providers, social media accounts, gaming services, and others have more relaxed rules around user login sessions, and they create authentication cookies that sometimes are valid for years.


Once obtained, these files can grant the attackers a more stable and undetectable way of accessing an account, even without the owner’s knowledge.


This is where MitM phishing toolkits have proven to be useful for some threat actors who don’t want to dabble with distributing infostealer malware.


Instead, they use phishing kits adapted to work as [reverse proxies](https://en.wikipedia.org/wiki/Reverse_proxy), which relay traffic between the victim (1), the phishing site (2), and the legitimate service (3).


Users who authenticate on a MitM phishing site are actually logged into a legitimate site, but since all the traffic goes through the reverse proxy system, the attacker also has a copy of the authentication cookie, which he can then abuse or resell on underground markets dedicated to the trade of authentication cookies [[1](https://www.kaspersky.com/about/press-releases/2019_meet-genesis-the-underground-e-shop-with-tens-of-thousands-of-digital-doppelgangers), [2](https://ke-la.com/exploring-the-genesis-supply-chain-for-fun-and-profit/)].


![mitmToolkitOverview](https://therecord.media/wp-content/uploads/2021/12/mitmToolkitOverview-1024x519.png)Image: Kondracki et al
In a way, MitM phishing toolkits are real-time phishing toolkits but without the need of a human operator since everything is automated through the reverse proxy.


Ironically, today, many of these MitM phishing toolkits are based on tools developed by security researchers, such as [Evilginx](https://github.com/kgretzky/evilginx2), [Muraena](https://github.com/muraenateam/muraena), and [Modlishka](https://github.com/drk1wi/Modlishka).


#### MitM phishing toolkits are gaining in popularity


In a study published last month, academics from Stony Brook University and security firm Palo Alto Networks said they analyzed 13 versions of these three MitM phishing toolkits and created fingerprints for the web traffic that goes through one of these tools.


They used their findings to develop a tool called [PHOCA](https://github.com/catching-transparent-phish/phoca) that could detect if a phishing site was using a reverse proxy—a clear sign that the attacker was trying to bypass 2FA and collect authentication cookies rather than credentials alone.


The researchers said they fed PHOCA with URLs reported by the cybersecurity community as phishing sites between March 2020 and March 2021 and found that 1,220 of these sites were using MitM phishing toolkits.


The number is a significant jump from the roughly 200 phishing sites running reverse proxies that were active in late 2018 and early 2019, according to stats provided at the time to this reporter by late RiskIQ researcher [Yonathan Klijnsma](https://twitter.com/ydklijnsma).


This rise shows that these tools, and MitM phishing kits in general, have slowly gained in popularity among the cybercrime ecosystem.


A reason why they did can also be linked to the fact that most are free to download, easy to run, and there are plenty of tutorials and collaboration requests on hacking forums that have helped threat actors get acquainted with this new technology.


![XSS-ad-1](https://therecord.media/wp-content/uploads/2021/12/XSS-ad-1.png)Image: The Record
![XSS-ad-2](https://therecord.media/wp-content/uploads/2021/12/XSS-ad-2.png)Image: The Record
With 2FA seeing a broader adoption among online services, currently, all signs point to the fact that most phishing operations will eventually evolve to include MitM capabilities into their standard features sometime in the near future. They have no reason not to, and this is why this research was carried out in the first place.


For more information on this study, the researchers presented their findings last month at the ACM CCS 2021 security conference.


The video of their presentation is below and a copy of their report, titled “**Catching Transparent Phish: Analyzing and Detecting MITM Phishing Toolkits**,” is also available for download as a [PDF](https://catching-transparent-phish.github.io/catching_transparent_phish.pdf).








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]] [[action.malware.name=UPPERCUT]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Phishing]] [[Mitm]] [[2fa]] [[Toolkits]] [[Cybercrime]] [[Real-time]] [[The Record]]

