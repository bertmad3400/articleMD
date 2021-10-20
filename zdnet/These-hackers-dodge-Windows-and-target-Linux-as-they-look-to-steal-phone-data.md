# These hackers dodge Windows and target Linux as they look to steal phone data
### Dubbed LightBasin, the stealthy attack group appears to be an intelligence gathering operation, warn researchers.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/these-hackers-dodge-windows-and-target-linux-as-they-look-to-steal-phone-data/)
+ Date: October 20, 2021
+ Author: Danny Palmer


## Article:
Unknown

A stealthy hacking group is infiltrating telecommunications companies around the world in a campaign which researchers have linked to intelligence gathering and cyber espionage. 

The campaign, which has been active since at least 2016, has been [detailed by cybersecurity researchers at CrowdStrike](https://www.crowdstrike.com/blog/an-analysis-of-lightbasin-telecommunications-attacks/), who've attributed the activity to a group they call LightBasin - also known as UNC1945.  

It's believed that since 2019, the offensive hacking group has compromised at least 13 telecommunication companies with the aim of stealing specific information about mobile communications infrastructure, including subscriber information and call metadata – and in some cases, direct information about what data smartphone users are sending and receiving via their device. 

"The nature of the data targeted by the LightBasin aligns with information likely to be of significant interest to signals intelligence organisations. Their key motives are likely a combination of surveillance, intelligence, and counterintelligence collection," Adam Meyers, SVP of Intelligence at CrowdStrike told ZDNet. 

"There is significant intelligence value to any state-sponsored adversary that's likely contained within telecommunications companies," he added. 

The exact origins of LightBasin aren't disclosed, but researchers suggest that the author of tools used in attacks has knowledge of the Chinese language – although they don't go as far to suggest a direct link with China or any other Chinese-speaking countries. 

The attackers employ extensive operational security measures in an effort to avoid detection and will only compromise Windows systems on target networks if absolutely necessary. LightBasin's primary focus is on Linux and Solaris servers which are critical for running telecommunications infrastructure – and are likely to have less security measures in place than Windows systems. 






**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)**

Initial access to networks is gained via external DNS (eDNS) servers, which are part of the General Packet Radio Service (GPRS) network which connects different phone operators. Researchers discovered that LightBasin accessed one victim from a previously compromised victim. It's likely that initial access to original victims is gained by exploiting weak passwords via the use of [brute force attacks](https://www.zdnet.com/article/these-systems-are-facing-billions-of-attacks-every-month-as-hackers-try-to-guess-passwords/). 

Once inside the network and calling back to a command and control server run by the attackers, LightBasin is able drop TinyShell, an open-source Unix backdoor [used by many cyber criminal groups](https://www.zdnet.com/article/hacker-group-uses-solaris-zero-day-to-breach-corporate-networks/). By combining this with emulation software, the attacker is able to tunnel traffic from the telecommunications network. 

Other tools deployed in campaigns include CordScan, a network scanner which enables the retrieval of data when dealing with communications protocols.  

LightBasin has the ability to do this with many different telecommunications architectures, indicating what researchers describe as "robust research and development capabilities to target vendor-specific infrastructure commonly seen in telecommunications environments" and something "consistent with a signals intelligence organization" - or in other words, an espionage campaign. 

However, despite their best efforts to remain hidden, there are some elements of the campaigns which means they can be discovered and identified, such as not encrypting binaries while using SteelCorgi, a known ATP espionage tool.  There's also evidence of the same tools and techniques being used in the networks of compromised telecommunications providers, pointing towards a singular entity behind the whole campaign. 

It's believed that LightBasin is still actively targeting telecommunications providers around the world. 

"Given LightBasin's usage of bespoke tools and in-depth knowledge of telecommunications network architectures, we've seen enough to realize the threat LightBasin poses is not localized and could affect organizations outside of the ones we work with," said Meyers. 

"The potential payoff to these threat actors in terms of intelligence gathering and surveillance is just too big for them to walk away from," he added. 

To protect networks from this and other cyber attacks, it's recommended that telecommunications companies ensure that the firewalls responsible for GPRS network to have rules applied which mean networks can only be accessed via expected protocols.  

"Securing a telecommunications organization is by no means a simple task, especially with the partner-heavy nature of such networks and the focus on high-availability systems; however, with the clear evidence of a highly sophisticated adversary abusing these systems and the trust between different organizations, focusing on improving the security of these networks is of the utmost importance," the [CrowdStrike blog post](https://www.crowdstrike.com/blog/an-analysis-of-lightbasin-telecommunications-attacks/) said. 

**MORE ON CYBERSECURITY**

* [**Ransomware attackers targeted this company. Then defenders discovered something curious**](https://www.zdnet.com/article/ransomware-attackers-targeted-this-company-then-defenders-discovered-something-curious/)
* [**Hackers are targeting telecom companies to steal 5G secrets**](https://www.zdnet.com/article/hackers-are-targeting-telecoms-companies-to-steal-5g-secrets/)
* [**Learn cybersecurity skills with these 5 online courses**](https://www.cnet.com/tech/services-and-software/best-online-cybersecurity-courses/)
* [**Hackers are getting more hands-on with their attacks. That's not a good sign**](https://www.zdnet.com/article/hackers-are-getting-more-hands-on-with-their-attacks-thats-not-a-good-sign/)
* [**Nation-state cyberattacks targeting businesses are on the rise**](https://www.zdnet.com/article/nation-state-cyber-attacks-targeting-businesses-are-on-the-rise/)





#### Tags:
[[LightBasin]] [[cybersecurity]] [[ZDNet]]
