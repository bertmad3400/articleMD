# These ransomware criminals lost millions of dollars in payments when researchers secretly found mistakes in their code
### BlackMatter ransomware had a bug that allowed cybersecurity researchers at Emsisoft to hand out decryption keys to victims -- removing the need to pay ransoms.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cybersecurity-researchers-secretly-cost-ransomware-criminals-millions-of-dollars-after-finding-mistakes-in-their-code/)
+ Date: October 26, 2021
+ Author: Danny Palmer


## Article:
Unknown

A major [ransomware](https://www.zdnet.com/article/ransomware-an-executive-guide-to-one-of-the-biggest-menaces-on-the-web/) operation was prevented from making millions of dollars after cybersecurity researchers discovered a flaw in the ransomware that enabled encrypted files to be recovered without paying a ransom to cyber criminals.


Cybersecurity researchers at Emsisoft have detailed how they were secretly able to foil the cyber criminals behind [BlackMatter ransomware](https://www.zdnet.com/article/this-is-the-perfect-ransomware-victim-according-to-cybercriminals/), saving several victims from having to pay the ransom.

After keeping what they were doing under wraps to avoid the cyber criminals finding out, [researchers have now disclosed](https://blog.emsisoft.com/en/39181/on-the-matter-of-blackmatter/) how they were undermining BlackMatter by providing decryption keys to victims of their attacks.

BlackMatter has been active in its current incarnation since July this year, but has actually been around for a lot longer than that because the consensus among information security analysts is that BlackMatter is a rebranded version of [DarkSide ransomware](https://www.zdnet.com/article/iowa-farm-services-provider-hit-with-blackmatter-ransomware-and-5-9-million-ransom/). 

[DarkSide](https://www.zdnet.com/article/darkside-the-ransomware-group-responsible-for-colonial-pipeline-cyberattack-explained/) became notorious earlier this year as the culprits behind the [Colonial Pipeline ransomware attack](https://www.zdnet.com/article/colonial-pipeline-ransomware-attack-everything-you-need-to-know/). The incident led to shortages of gas and fuel across the US North Eastern seaboard while the criminals [walked away with millions of dollars](https://www.zdnet.com/article/colonial-pipeline-paid-close-to-5-million-in-ransomware-blackmail-payment/) when Colonial paid the ransom.

But the impact of the attack didn't go unnoticed and shortly after [the White House vowed action](https://www.zdnet.com/article/have-we-reached-peak-ransomware-how-the-internets-biggest-security-problem-has-grown-and-what-happens-next/) against those responsible, DarkSide lost control of part of their critical infrastructure and [some of their Bitcoin wallets were seized](https://www.zdnet.com/article/majority-of-ransom-paid-by-colonial-pipeline-seized-and-returned-by-doj/). The group seemed to go dark after that. 

However, DarkSide soon re-emerged as BlackMatter and the cyber criminals behind it don't appear to have been put off by finding themselves in the sights of the US government. They have gone onto [launch a string of ransomware attacks against companies in North America](https://www.zdnet.com/article/cisa-says-blackmatter-ransomware-group-behind-recent-attacks-on-agriculture-companies/). 






Posts by BlackMatter on underground forums offering to buy access to compromised networks in the USA, Canada, the UK, and Australia claimed that BlackMatter wouldn't go after hospitals or state institutions. But this was untrue, and in addition to critical infrastructure in the form of [several agricultural companies](https://www.zdnet.com/article/iowa-farm-services-provider-hit-with-blackmatter-ransomware-and-5-9-million-ransom/), the group has also struck blood testing facilities.

**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)**

"The gang's claim that attacks on the critical infrastructure and certain other sectors was empty: it attacked the very organisations it said it would not," Brett Callow, threat analyst at Emsisoft told ZDNet.  

"So why did they make the claim in the first place? It may have been an attempt to avoid attracting immediate attention from law enforcement agencies in the aftermath of the Colonial Pipeline incident or, perhaps, they believed that companies would be more inclined to negotiate if they didn't appear to be thugs who attacked hospitals".

In December last year, Emsisoft researchers noticed a mistake made by the DarkSide operators that allowed the decryption of data encrypted by the Windows version of the ransomware without the need for a ransom to be paid -- although the criminals fixed it in January.  

However, it turns out that the ransomware group made a similar mistake once again when they rebranded, and researchers uncovered a flaw in the BlackMatter ransomware payload which allowed victims to recover files without paying the ransom.

After uncovering the second vulnerability, Emsisoft worked with others to provide as many BlackMatter victims as possible with the decryption key before they paid the ransom, a move that has prevented cyber criminals from pocketing tens of millions of dollars. 

Unfortunately, BlackMatter eventually figured out that something was wrong and closed the loophole. 

"BlackMatter will likely have suspected something was amiss when their revenue started to dip, and will have become more suspicious the longer it went on. Unfortunately, it's inevitable that gangs will realise they have a problem in these situations. All we can do is work quickly and quietly to help as many victims as we possibly can while the windows of opportunity exist," said Callow. 

"This effort shows the importance of public-private sector collaboration. Working together, we can put a big dent in the profitability of cybercrime, and that's a key element in combatting the ransomware problem," he added.

Ransomware remains a major information security issue and the best way to avoid having to react to attack is to not become a victim in the first place. Cybersecurity strategies like [applying security patches in a timely manner](https://www.zdnet.com/article/this-one-change-could-protect-your-systems-from-attack-so-why-dont-more-companies-do-it/), ensuring [multi-factor authentication is applied across the network](https://www.zdnet.com/article/multi-factor-authentication-use-it-for-all-the-people-that-access-your-network-all-the-time/), and only providing users with the access they need -- for example, by not giving admin privileges to people who don't need them -- can all help prevent ransomware attacks. 

As for BlackMatter, it's likely they'll carry on -- but their mistakes may have damaged their reputation in cyber criminal circles. 

"I wouldn't be at all surprised if the operators were to abandon the BlackMatter name and rebrand. Their reputation will be in the  toilet. Their repeated mistakes have cost affiliates money. Lots of money," said Callow.

**MORE ON CYBERSECURITY**

* **[**Ransomware: A company paid millions to get their data back, but forgot to do one thing. So the hackers came back again**](https://www.zdnet.com/article/ransomware-this-is-the-first-thing-you-should-think-about-if-you-fall-victim-to-an-attack/)**
* **[**Ransomware: Looking for weaknesses in your own network is key to stopping attacks**](https://www.zdnet.com/article/ransomware-looking-for-weaknesses-in-your-own-network-is-key-to-stopping-attacks/)**
* [**Have we reached peak ransomware? How the internet's biggest security problem has grown and what happens next**](https://www.zdnet.com/article/have-we-reached-peak-ransomware-how-the-internets-biggest-security-problem-has-grown-and-what-happens-next/)
* **[**Ransomware: Even when the hackers are in your network, it might not be too late**](https://www.zdnet.com/article/ransomware-even-when-the-attackers-are-in-your-network-its-not-too-late-to-fight-back/)**
* [**Ransomware gangs are complaining that other crooks are stealing their ransoms**](https://www.zdnet.com/article/these-ransomware-crooks-are-complaining-they-are-getting-ripped-off-by-other-ransomware-crooks/)





#### Tags:
[[BlackMatter]] [[ransomware]] [[DarkSide]] [[Emsisoft]] [[ZDNet]]
