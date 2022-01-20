# Cybersecurity for Industrial Control Systems: Part 2
### Part 2 of this cybersecurity for industrial control systems series discusses malware detection and distribution to help strengthen ICS cybersecurity.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/22/a/cybersecurity-for-industrial-control-systems-part-2.html
+ Date: 2022-01-20
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/cybersecurity-for-industrial-control-systems-part-1/Threats-Affecting-ICS-Endpoints.jpg)





In part two of the series, we discussed that ransomware, legacy malware, coinminer, and Conficker continue to pose a great risk to industrial control systems. To cap off the series, let’s talk about detection in top ten countries. We’ll also share some helpful insights and tips in making your ICS cybersecurity framework stronger.


Top 10 counties and detections






![top-10-countries-and-detections](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/threats-affecting-ics-endpoints-part-2-country-detection-and-insights/top-10-countries-and-detections.png)
Figure 8. Top 10 countries’ percentage of industrial control systems with malware and grayware detections





Malware and grayware threats were also discovered during our research. We found that China had the most grayware and malware detections in the top 10 countries, while Japan had the least. From a geographical point of view, we can see that some threat types affected certain countries more than others.






![top-10-countries-and-detections2](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/threats-affecting-ics-endpoints-part-2-country-detection-and-insights/top-10-countries-and-detections2.png)
Figure 9. Top 10 countries breakdown of detections according to type




Legacy malware had the most detections in India, China, the US, and Taiwan. For coinminer, Equated malware, and WannaCry, India had the most detections. On the other hand, Japan had the most Emotet infections, while ICSs in Germany had the most adware incidents.


Through this extensive research, we found that there were several malware threats that pose a great risk on ICSs. By identifying these threats, we can now determine various steps that your enterprise can take to better secure your industrial control systems.


But what does this information mean? This tells us several things:


* Ransomware continues to be a major concern and continues to be a rapidly evolving threat to ICSs across the globe;
* Coinminers affect ICSs mostly through unpatched operating systems;
* Conficker continues to propagate on ICS endpoints running newer OS;
* Legacy malware still affects IT/OT networks; and
* Malware detected on ICS endpoints varies between countries.


Based on the detection data, we can conclude that modern malware such as the threats we discussed affect ICSs. It means both modern techniques like fileless malware and hacking tools and age-old methods like removable drive autorun can successfully infect ICS endpoints.


The stakes are also higher for some attacks. [As illustrated by the Colonial Pipeline incident](/en_us/research/21/e/what-we-know-about-darkside-ransomware-and-the-us-pipeline-attac.html), ransomware attackers are into big-game hunting. They identify whom they were able to compromise and then determine key systems in the network that can cause the most disruption. After this, they coerce the victim into paying.


The presence of ransomware in ICSs in several attacks may indicate that attackers are now recognizing these systems and actively targeting them.


Security is paramount for ICSs


These findings mean security must be a major consideration when interconnecting the IT network with the OT network. Enterprises should address security issues brought about by both legacy malware and the latest attack trends.


Using malware detections as one of the criteria of IT/OT networks’ cybersecurity readiness can help enhance their security posture and better protect ICSs endpoints This also helps prevent unintended downtown and the loss of view and control.


Moreover, IT security staff should work with OT engineers to properly account for key systems as well as identify various dependencies like OS compatibility and up-time requirements. They should also learn the process and operational practices and plan a suitable cybersecurity strategy for the protection of these important systems.


Other tips to secure your ICS endpoints


* Patch systems with security updates to avoid compromises. EnternalBlue was exploited initially by zero-day malware and then by commoditized Equation group tools installing coinminers. Once an exploit is out, it gets assimilated into the attacker’s playbooks, so patching is vital.
* Use micro-segmentation in the network or virtual technologies. If patching is not an option, this can enhance security by restricting network access and communications to only necessary devices.
* Restrict network shares and implement strong username and password combinations. This method can help prevent unauthorized access through credential brute force.
* Use Intrusion Detection System (IDS) and Intrusion Prevention System (IPS). These can flag possible network anomalies as well as identify malicious traffic. These help with device visibility as well.
* Install antimalware solutions. These solutions can address legacy worms and viruses that can stay dormant in removable drives and air-gapped systems.
* Set up USB scanning kiosks. These stations can scan for malware from removable drives used to transfer data in between air-gapped endpoints.
* Apply the least privilege principle. Applying this strategy means an operator is allowed to use the ICS but only an administrator can install software or make system changes on the endpoint.
* Use a safelist. This may be appropriate for certain ICSs of specific functions.
* Conduct incident responsive and network sweeping for compromise (IoCs). By doing this, you can determine the extent of intrusion and security weaknesses that were abused by attackers. These steps can also help in creating a security strategy based on the incident.


Apart from these recommendations, a robust cybersecurity solution can help future-proof an enterprise's ICS and its endpoints. As a leader in cybersecurity solutions, Trend Micro offers forward-looking products that address various needs, including ICS security. [Check out our product page to learn more about our offerings](/en_us/business/products.html).








## Tags:

#### Threatactor:
[[threatactor.name=Equation]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conficker]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Emotet]] [[action.malware.name=Miner-C]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=WannaCry]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[Icss]] [[Ics]] [[Cybersecurity]] [[Ransomware]] [[Trend Micro]]

