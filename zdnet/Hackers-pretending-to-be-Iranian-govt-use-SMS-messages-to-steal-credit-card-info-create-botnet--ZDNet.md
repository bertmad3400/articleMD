# Hackers pretending to be Iranian govt use SMS messages to steal credit card info, create botnet | ZDNet
### Hackers in Iran have been able to convince citizens to download malicious applications by claiming judicial complaints have been filed against them.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/hackers-pretending-to-be-iranian-govt-use-sms-messages-to-steal-credit-card-info-create-botnet/
+ Date: 2021-12-07 00:38:54
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/c2ac2f2f9fbed08c3621002581e084c96e95e152/2018/05/09/9824ea10-5e49-4e4e-9202-a97915bb5fa4/iran-thumb.jpg?width=770&height=578&fit=crop&auto=webp)

Security company Check Point Research has [uncovered](https://research.checkpoint.com/2021/smishing-botnets-going-viral-in-iran/) a hacking campaign that involves cyberattackers impersonating Iranian government bodies to infect the mobile devices of Iranian citizens through SMS messages. 

The SMS messages urge victims to download Android applications related to official Iranian services, such as the Iranian Electronic Judicial Services. The first messages typically claim that a complaint has been filed against the victim and that an application needs to be downloaded in order to respond. 

Once downloaded, the applications allow hackers to access the victim's personal messages. Victims are asked to enter credit card information in order to cover a service fee, giving attackers access to card information that can now be used. With access to a victim's personal messages, the attackers can also get past two-factor authentication. 

Check Point Research said the campaign is ongoing and is being used to infect tens of thousands of devices. In addition to the Check Point report, Iranian citizens [have taken to social media](https://twitter.com/mohebatre/status/1440401410017742851) to complain about the scams. Some Iranian news outlets [are also covering the issue](https://www.iribnews.ir/fa/news/3181066/%DA%A9%D9%84%D8%A7%D9%87%D8%A8%D8%B1%D8%AF%D8%A7%D8%B1%DB%8C-%D8%A7%D8%B2-%D8%B7%D8%B1%DB%8C%D9%82-%D8%A7%D8%B1%D8%B3%D8%A7%D9%84-%D9%BE%DB%8C%D8%A7%D9%85%DA%A9-%D8%AC%D8%B9%D9%84%DB%8C-%D8%A8%D8%A7-%D9%86%D8%A7%D9%85-%D8%B3%D8%A7%D9%85%D8%A7%D9%86%D9%87-%D8%AB%D9%86%D8%A7). 

"The threat actors then proceed to make unauthorized money withdrawals and turn each infected device into a bot, spreading the malware to others. CPR attributes attacks to threat actors, likely in Iran, who are financially motivated," the cybersecurity company explained. 

"CPR estimates tens of thousands of Android devices have fallen victim, leading to theft of billions of Iranian Rial. Threat actors are using Telegram channels to transact malicious tools involved for as low as $50. CPR's investigation reveals that data stolen from victims' devices has not been protected, making it freely accessible to third parties online."

Check Point's Shmuel Cohen said in one campaign, more than 1,000 people downloaded the malicious application in less than 10 days. Even if they did not enter credit card information, their device became part of the botnet. 

![s3.jpg]()![s3.jpg](https://www.zdnet.com/a/img/resize/08db882bae156bfc447d1a6d5959d0107ed2dc43/2021/12/07/3a287185-c2a9-4734-aaa5-7e9003bb0770/s3.jpg?width=470&fit=bounds&auto=webp)
 Check Point Research
 




Alexandra Gofman, threat intelligence team leader at Check Point, told ZDNet that the attacks appear to be a form of cybercrime and not attributed to any state-backed actors.

The velocity and spread of these cyberattacks are unprecedented, Gofman said, adding that it is an example of a monetarily-successful campaign aimed at the general public. 

"The campaign exploits social engineering and causes major financial loss to its victims, despite the low quality and technical simplicity of its tools. There are a few reasons for its success. First, when official-looking government messages are involved, everyday citizens are inclined to investigate further, clicking the provided link," Gofman said. 

"Second, due to the botnet nature of these attacks, where each infected device gets the command to distribute additional phishing SMS messages, these campaigns spread quickly to a large number of potential victims. Although these specific campaigns are widespread in Iran, they can take place in any other part of the world. I think it's important to raise awareness of social engineering schemes that are employed by malicious actors."

Check Point explained that the cybercriminals behind the attack are using a technique known as "smishing botnets." Devices that have already been compromised are used to send SMS messages to other devices. 

The people behind the technique now offer it to others on Telegram for up to $150, providing anyone with the infrastructure to launch similar attacks easily. Even though Iranian police [were able to arrest](https://www.mehrnews.com/news/5311178/%D9%86%D9%88%D8%AC%D9%88%D8%A7%D9%86-%DB%B1%DB%B7-%D8%B3%D8%A7%D9%84%D9%87-%DA%AF%D8%B1%DA%AF%D8%A7%D9%86%DB%8C-%D8%A8%D8%A7-%D9%BE%DB%8C%D8%A7%D9%85%DA%A9-%D8%AB%D9%86%D8%A7-%DB%B8%DB%B0%DB%B0-%D9%85%DB%8C%D9%84%DB%8C%D9%88%D9%86-%DA%A9%D9%84%D8%A7%D9%87%D8%A8%D8%B1%D8%AF%D8%A7%D8%B1%DB%8C-%DA%A9%D8%B1%D8%AF) one of the culprits, there are dozens of different cybercriminals in Iran using the tool now. 

The company estimates that about $1,000 to $2,000 has been stolen from most victims. The attackers are also offering the personal information that was stolen to others online. 

Gofman added that the general population of Iran is now in a situation where cyberattacks significantly impact day-to-day lives. 

These attacks [began with railways](https://www.zdnet.com/article/cybercriminals-troll-irans-leader-cause-railway-network-chaos/), Gofman said, noting that the company traced that attack to a group called Indra. 

"The attacks continued [with gas stations](https://www.npr.org/2021/10/27/1049566231/irans-president-says-cyberattack-was-meant-to-create-disorder-at-gas-pumps), and then the [national aviation company](https://www.reuters.com/business/aerospace-defense/irans-mahan-air-says-its-has-foiled-cyber-attack-tv-2021-11-21/). Now, we're seeing yet another cyberattack that shows how even pure cybercrime can make headlines and chaos, hurting many in Iran," Gofman said. 

"Although we do not see a direct connection between these latest cyberattacks and the major aforementioned attacks, our latest insights show how even unsophisticated cyber attacks create significant damage on Iran's general population."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Chaos]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Iran]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Gofman]] [[Sms]] [["the]] [[Cyberattacks]] [[ZDNet]]

