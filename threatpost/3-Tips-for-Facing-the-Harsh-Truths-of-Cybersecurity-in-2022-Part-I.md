# 3 Tips for Facing the Harsh Truths of Cybersecurity in 2022, Part I
### Sonya Duffin, ransomware and data-protection expert at Veritas Technologies, shares three steps organizations can take today to reduce cyberattack fallout.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178311
+ Date: 2022-02-09 21:06:38+00:00
+ Author: Sonya Duffin


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/29112739/nuclear-bomb-explosion-1478796377Hhl.jpeg)

Be forewarned—I’m about to lay down some harsh truths here.


First, ransomware is prevalent, and there is no way to completely eliminate the threat.


Second, at this point, you should operate under the assumption that hackers are already in your systems or could easily access them at any moment. It should come as no surprise when I tell you that the sophisticated cybercriminals behind today’s ransomware threats have been consistently getting past even the best frontline security — and for a while now.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Third, cybercriminals may know your systems and infrastructure better than you do. Once in, their strategy is to lay low and remain hidden while they learn as much as they can. Then they strike at the optimal time to inflict as much damage as possible to ensure a hefty payday.


So now what?


The good news is that there are practices and technologies that can help you detect threats before the bad actors can take action. There are also strategies that you can use to reduce your attack surface while preventing large-scale disruption and disablement once they are inside your environment.


With that in mind, this two-part series will outline the top six steps you should take right away to ensure resiliency in the face of this ever-present threat. Let’s begin with the first three.


**Get Full Infrastructure Awareness**
-------------------------------------


Attackers are looking for your weakest links, and the dark corners where there may be limited security and oversight in your environment. So, it’s vital to implement tools that provide full infrastructure awareness by shining a light on all the dark data in your environment. According to the recently published Veritas Vulnerability Lag research ([PDF here](https://www.veritas.com/content/dam/Veritas/docs/reports/GA_ENT_AR_Veritas-Vulnerability-Gap-Report-Global_V1414.pdf)), 35 percent of data is still dark. That is alarmingly high. Get to work on knowing what data you have and where it is ASAP.


***Important reminder:*** In addition to full visibility of everything in your environment, it is also vital to have clear hard-copy documentation on the details of your environment, like procedures and configurations—including IP addresses, passwords etc.—to help aid with recovery. Missing these details can keep you and your team from being able to quickly recover in the chaos of an attack. Store these in a safe that is checked and updated regularly.


**Automate Alerts for Anomalous Behavior**
------------------------------------------


Implement tools that can provide you with detection of anomalous behaviors or activities associated with both data and user activity across your entire environment. It’s important that the detection capabilities can run autonomously, without the need for manual steps.


Alerting your teams to anything anomalous or out of the ordinary will provide you with the upper hand, and a chance to act before the cybercriminals or a malicious code attack. This could be things like unusual file-write activity that could indicate an infiltration, but it could also be detecting known ransomware file extensions, file access patterns, traffic patterns, code downloads, access requests, storage capacity surges, external traffic paths or even an unusual jump in activity compared to individuals’ typical patterns.


For example, in the infamous [SolarWinds hack](https://threatpost.com/solarwinds-default-password-access-sales/162327/), hackers used a regular software update to slip some elegant and innovative malicious code into a multitude of companies’ networks, using the SolarWinds software.


For more than nine months they roamed around high-profile and sensitive companies, hiding in plain sight while learning their systems and gathering intelligence. Their mistake came when they started roaming around the cybersecurity company FireEye.


The security team at FireEye noticed suspicious activity — someone trying to register a second phone onto the company network. Finding it odd that an employee would have two phones, they jumped into action and called the user. Surprise! That user did not register that phone and had no idea who did. Thanks to the vigilance of FireEye, which investigated out-of-the-ordinary activity, the broader intrusions came to light.


***Important reminder:*** Conduct cyber-threat hunts regularly. Take it seriously and implement protocols for investigating anomalous behaviors. Hire a third-party agency to audit your strategy, check your work and find vulnerabilities.


**Limit Access & Reduce Your Attack Surface**
---------------------------------------------


After sneaking into your environment, cybercriminals often search for confidential information or login credentials that will allow them to move laterally across your environment. This means that they can also gain access to your backup systems and will attempt to eliminate recovery options.


There are a few things that you can do to help mitigate this practice:


1. For starters, limit what and where each set of credentials can operate, and have different passwords for every domain.
2. Make sure that there is not one god-admin that can do everything.
3. It is also important to lock down or limit executives’ access, as they are often easy targets.
4. Just as important, limit admin access and privileges, especially to backups.
5. Another common practice is to implement zero-trust approaches with multifactor authentication (MFA) and role-based access controls.
6. Also vital is to segment or microsegment your network into multiple zones of smaller networks and ensure access is managed and limited, especially to your most crucial data.
7. Many organizations are also moving towards a just-in-time security practice where access is granted on an as-needed basis or for a predetermined period of time, which is something to consider for crucial and business-critical data.


By building a variety of barriers, bad actors will be contained and prevented from moving around your environments. They are essentially stopped in their tracks. So, get creative—meaning, set up a system unique to your needs and security requirements.


When the Metropolitan Transportation Authority of New York was hacked last April, attackers did not gain any access to systems that control train cars nor was any customer information compromised. Why? Because they have a multilayered, segmented network of more than 18 different systems, only three of which were compromised. Thanks to this great system, the threat actors were prevented from moving throughout the system, the event was isolated and systems were restored quickly.


***Important reminder:*** Create a walled-off network that looks exactly like your production network, but with different management credentials. Share nothing with your production networks except access to immutable storage. You can use this space to recover your data and services and scrub your data of malware. It is also a great place to test recovery.


Stay tuned for part two in this series, where I’ll cover the remaining three of the top six steps you should take today to ensure ransomware resiliency in today’s rapidly evolving cybersecurity landscape.


***Sonya Duffin is a ransomware and data protection expert at [Veritas Technologies](https://www.veritas.com/).***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by visiting our [microsite](https://threatpost.com/microsite/infosec-insiders-community/).***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Chaos]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Cybercriminals]] [[Fireeye]] [[ThreatPost]]

