# Volatile and Adaptable: Tracking the Movements of Modern Ransomware
### Trend Micro's tracking of  modern ransomware, as well as of older families, shows which attacks are gaining momentum and which families are particularly dangerous for enterprises and private users.  

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware.html
+ Date: 2021-12-15
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware/banner%20volatile%20ransomware.jpg)





In the first half of 2021, we saw that [modern ransomware threats](https://www.trendmicro.com/vinfo/us/security/research-and-analysis/threat-reports/roundup/attacks-from-all-angles-2021-midyear-security-roundup) were still active and evolving, using double extortion techniques to victimize targets. Unlike traditional ransomware tactics, current adversaries use private data stolen from victims’ machines to add pressure and threaten to release valuable information onto public leak sites if the ransom remains unpaid. Further into the year, our tracking of these threats, as well as of older ransomware families, shows which attacks are gaining momentum and which families are particularly dangerous for enterprises and private users.  


A deeper look into 2021’s modern ransomware


The total number of Trend Micro detections of ransomware threats, which covers all types of ransomware, lessened in June and July but started picking up again in August. Upon looking at the targets of these ransomware threats, we found that enterprises were the most targeted, while consumers were next in line. 






![Figure 1. Ransomware detections by layer (email, file, and URL) from January to September 2021 ](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware/Volatile%20Ransomware-1-01.jpg)
Figure 1. Ransomware detections by layer (email, file, and URL) from January to September 2021 





![Figure 2. Ransomware file detections by business segment from January to September 2021 ](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware/Volatile%20Ransomware-2-01.jpg)
Figure 2. Ransomware file detections by business segment from January to September 2021




Although threat actors are still utilizing various tactics to abuse users’ systems, we have been tracking older ransomware families as well as modern ransomware and observed some differences. 


WannaCry (aka WCry), an older and more traditionally operated thread, has been dominant among the total ransomware threats since 2007. To understand trends of the modern ransomware families, we therefore need to check the data without WCry, as well as look at the movement of WCry alone. As the following chart shows, by excluding WCry, we can see the increase in the other ransomware families. On the other hand, we can see that the legacy WCry family is on the decline. Older families like Locky can also be considered legacy ransomware and so might be in the same situation in the future.   




Modern or post-intrusion ransomware is typically loaded after another malware gains access to a victim’s device. The latest rankings indicate the volatility of these modern high-profile ransomware families. For example, Sodinokibi (aka REvil) shows irregular behavior. Due to the "targeted" nature of these families, the detection counts spike depending on whether or not specific attacks occur. With traditional ransomware, the campaigns are released without a specific target, like a net that catches whatever it can.    








![Figure 3. Top 10 ransomware families detected from January to September 2021; highlighted sections show the decline of WannaCry and the volatility of the REvil modern ransomware.](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware/Volatile%20Ransomware-3-01.jpg)
Figure 3. Top 10 ransomware families detected from January to September 2021; highlighted sections show the decline of WannaCry and the volatility of the REvil modern ransomware.




![Figure 4. Monthly ransomware file detections with and without WCry](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware/Volatile%20Ransomware-4-01.jpg)
Figure 4. Monthly ransomware file detections with and without WCry




Ransomware campaign trends  




Emotet, Ryuk, and Trickbot are the three malware families with the most active campaigns this far into 2021. In January 2021, law enforcement agencies from eight countries coordinated with one another to disrupt the Emotet botnet, causing the steep decline from January and February as seen in Figure 5. Unfortunately, even after this disruption, the remaining Emotet operators continued with their campaigns. [Emotet is largely known as an example of malware as a service](https://www.trendmicro.com/en_ph/research/21/c/emotet-one-month-after-the-takedown.html), which provides other groups with access to compromised computers. Trickbot has also been [used to move laterally across a network and propagate](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/examining-ryuk-ransomware-through-the-lens-of-managed-detection-and-response). Many ransomware operators, like those distributing Ryuk, have used these tools and services to conduct campaigns.    




Among these families, Emotet has the highest detection rate (we detect both the primary payload along with its ransom notes). Ryuk has steadily been increasing over the course of the year and showed a significant surge in August. Notably, the 734.1% increase was possibly caused by some specific, large-scale attacks. Our data shows that the considerable surge occurred only in the enterprise and small-to-medium business (SMB) categories, showing that it could be part of particular attacks launched on corporate sectors. By September, the surge had died down considerably.  








![Notes: Ryuk and Emotet detections include ransom notes Figure 5. Top three malware families with the most active campaigns](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware/Volatile%20Ransomware-5-01.jpg)
Figure 5. Top three malware families with the most active campaigns (Notes: Ryuk and Emotet detections include ransom notes)




The global threat of post-intrusion ransomware


Post-intrusion ransomware groups use various tools and compromised accounts for access and lateral movement — and these families are generally more sophisticated than traditional ransomware. We saw that the detections for post-intrusion ransomware were consistent from 2019 up until the third quarter of 2020. However, in the fourth quarter of 2020, we saw a dramatic increase. While post-intrusion ransomware in 2021 decreased compared to the fourth quarter of 2020, it is still significantly higher when compared to detections from the first to the third quarter of 2020.  








![Figure 6. Rates of post-intrusion ransomware from January 2020 to September 2021](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware/Volatile%20Ransomware-6-02.jpg)
Figure 6. Rates of post-intrusion ransomware from January 2020 to September 2021




Countries like US, India, Japan, Germany, and others were consistently affected by post-intrusion ransomware from 2019 until the first half of 2021. However, the United Kingdom, Singapore, Hong Kong, and Netherlands saw the rate of their ransomware incidents increase, and these countries rose in the ranking of top countries with ransomware detections from 2019 to the first half of 2021.  








![Figure 7. Global ranking of the four countries with regard to overall (email, URL and file) ransomware detections from Trend Micro data](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/volatile-and-adaptable-tracking-the-movements-of-modern-ransomware/Volatile%20Ransomware-7-01.jpg)
Figure 7. Global ranking of the four countries with regard to overall (email, URL and file) ransomware detections from Trend Micro data




Based on the data in the preceding chart, ransomware actors seem to be following a trend where they either continue targeting countries where they previously experienced success or increase their efforts there. We see this especially in the UK and the Netherlands. These two trends might also indicate that ransomware actors are slowly moving away from countries where they don’t have as much success. 


Solutions and Security Recommendations 


Ransomware groups are a persistent threat, and they continue to evolve their business strategy as well as the tools and techniques they use to target enterprises. Organizations can mitigate the risks of ransomware with these best practices:  




* Deploy cross-layered detection and response solutions. Find solutions that can anticipate and respond to ransomware activities, techniques, and movements before the threat culminates. [Trend Micro Vision One™️ with Managed XDR](https://www.trendmicro.com/en_us/business/products/detection-response.html) helps detect and block ransomware components to stop attacks before they can affect an enterprise.
* Make a playbook for prevention and recovery. Invest in incident response or [IR teams](https://www.trendmicro.com/vinfo/us/security/news/managed-detection-and-response/cyberattacks-from-the-frontlines-incident-response-playbook-for-beginners), as well as a dedicated and specific playbook applicable to the company. IR [playbook](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) [frameworks](https://www.cynet.com/incident-response/incident-response-sans-the-6-steps-in-depth/) allow an organization to plan and prepare for attacks such as ransomware and breaches. Maintain these guides with proper procedures that everyone can follow when the need arises.
* Conduct attack simulations. Expose employees to a [realistic cyberattack simulation](https://www.nytimes.com/2021/06/03/us/politics/ransomware-cybersecurity-infrastructure.html). This can help decision-makers, security personnel, and IR teams identify and prepare for potential security gaps as well as pressure points in systems and people.








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Emotet]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=REvil]] [[action.malware.name=REvil]] [[action.malware.name=REvil]] [[action.malware.name=Ryuk]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]] [[action.malware.name=WannaCry]] [[action.malware.name=WannaCry]]

#### Location:
[[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.city.name=Singapore]] [[victim.country.name=Singapore]] [[victim.continent.name=Asia]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.country.name=Netherlands]] [[victim.continent.name=Europe]] [[victim.country.name=United Kingdom]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Post-intrusion]] [[Emotet]] [[Wcry]] [[Ransomware]] [[Malware]] [[Ryuk]] [[Trend Micro]]

