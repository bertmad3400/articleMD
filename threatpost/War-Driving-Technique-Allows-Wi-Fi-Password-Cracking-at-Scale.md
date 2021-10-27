# War-Driving Technique Allows Wi-Fi Password-Cracking at Scale
### A researcher was able to crack 70 percent of the gathered hashes in an experiment in a residential neighborhood.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175817)
+ Date: October 27, 2021  1:00 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/27125920/wardriving-e1635353977846.jpg)
War-driving – the process of driving around mapping residential Wi-Fi networks in hopes of finding a vulnerability to exploit – can still pay off for attackers, apparently: A CyberArk researcher recently found he could easily slice open about 70 percent of Wi-Fi network passwords in one Tel Aviv community — all at once.


CyberArk’s Ido Hoorvitch ran the experiment after observing that across multiple apartment moves, his neighbors’ mobile numbers turned out to also be their Wi-Fi passwords. He knew this because he asked to piggyback on the neighbors’ Wi-Fi while waiting for cable to be installed.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


From there, “I hypothesized that most people living in Israel (and globally) have unsafe Wi-Fi passwords that can be easily cracked or even guessed by curious neighbors or malicious actors,” he noted, in a [Tuesday blog](https://www.cyberark.com/resources/threat-research-blog/cracking-wifi-at-scale-with-one-simple-trick). Well, it turns out he was right.


**Walking, Sniffing & Cracking in Tel Aviv**
--------------------------------------------


To carry out the experiment, Hoorvitch gathered 5,000 Wi-Fi network hashes by strolling the streets in Tel Aviv with readily available, commercial Wi-Fi sniffing equipment.


His hash-sniffing rig consisted of a $50 AWUS036ACH ALFA wireless network interface card (NIC) installed in a cheap Ubuntu machine, and the Hcxdumptool utility from ZerBea. Hcxdumptool is used to capture packets from WLAN devices, available on GitHub. The NIC has monitor-mode capabilities, which allows packet capturing without having to associate with an access point, the researcher explained.


After gathering what he felt was a decent sample size of 5,000 SSIDs and password hashes, it was then time to get crackin’ – literally.


“Our first step in the cracking procedure is to install Hashcat, the world’s fastest and most advanced password-recovery tool,” he said, which includes several password-cracking methods like mask and dictionary attacks.


After he converted the sniffing results into a hashfile format compatible with Hashcat, he ran them through a mask attack first, which is a process of trying all possible combinations from a set of characters. Mask attacks are more specific than, say, brute-force attacks, because the list of characters in the set is reduced based on information an attacker knows.


In this case, the Hashcat command tried all of the possible cellphone number combinations in Israel against each hash.


“We chose to start with what’s called a mask attack, due to the terrible habit many people living in Israel have of using their cellphone numbers as Wi-Fi passwords,” he said, adding that this approach becomes easier because the Israeli cellphone prefix is always the same: 05.


“[Numbers] are 10 digits long and it starts with 05,” Hoorvitch explained. “Therefore, we need to guess the remaining eight digits. Each digit has 10 options (0-9), hence 10**8 possible combinations.”


That translates into millions of combinations, but his laptop was able to cycle through 194,000 hashes per second. Upon the first run of the mask, he was able to crack 2,200 passwords.


The next step was mounting a standard dictionary attack, in which a set of common passwords is tried against a given account.


“With the most common dictionary, Rockyou.txt, [we] cracked more than 900 hashes,” said Hoorvitch, bringing the total to around 3,500 cracked passwords, or 70 percent of the hashes he had gathered.


**Roaming Insecurity**
----------------------


While the obvious moral of the story is that most people use dumb passwords, the other part of the narrative is the fact that Hoorvitch used a [relatively new sniffing technique](https://hashcat.net/forum/thread-7717.html) that only works with routers that support roaming features (which he details in his post).


Roaming routers are usually deployed in city- or campus-mesh type situations where Wi-Fi is deployed as a blanket of internet access using multiple access points (APs). They use something called PMKID keys, which are unique key identifiers used to keep track of the password hash being used for the client as a person moves from router to router, to ensure continuous connectivity.


Many routers have dual-purpose capabilities so that roaming options often show up in APs in residential settings even though their owners don’t need the functionality.


“Not all routers support roaming features and are, therefore, not vulnerable to the PMKID attack,” Hoorvitch said. “However, our research found that routers manufactured by many of the world’s largest vendors are vulnerable.”


Thus, turning off roaming (if possible) is a good mitigation to war-driving. Otherwise, previous sniffing techniques required an attacker to be able to intercept the four-way handshake that happens when someone connects an AP – which prevents any cracking at scale.


“As I estimated beforehand, the process of sniffing Wi-Fis and the subsequent cracking procedures was a very accessible undertaking in terms of equipment, costs and execution,” the researcher noted. “The bottom line is that in a couple of hours and with approximately $50, your neighbor or a malicious actor can compromise your privacy and much more if you don’t have a strong password.”


**How to Protect Against Wi-Fi Cyberattacks**
---------------------------------------------


Exploitation stakes can be high when it comes to routers: Hoorvitch pointed out that breaking into a residential network allows attackers to pivot to any of the devices connected to it to steal information or drop malware; and with people working from home since the pandemic, this could also have big consequences for business data protection.


“For the small business, the risk lies in an attacker infiltrating a network and then moving laterally to high-value applications or data, such as a billing system or cashier,” according to the analysis. “Concerning the enterprise, it’s possible for an attacker to gain initial access to a remote user’s Wi-Fi and then hop to the user’s computer and wait for a VPN connection or for the user to go to the office and move laterally from there.”


To protect themselves, users should of course replace any default usernames and passwords, and choose complex passwords. They should also disable weak encryption protocols (as WAP or WAP1) and disable WPS, the researcher advised.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Wi-Fi]] [[Hoorvitch]] [[Aviv]] [[passwords.]] [[cellphone]] [[passwords,]] [[ThreatPost]]
