# Top 10 Cybersecurity Best Practices to Combat Ransomware
### Immutable storage and more: Sonya Duffin, data protection expert at Veritas Technologies, offers the Top 10 steps for building a multi-layer resilience profile.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176316)
+ Date: November 12, 2021  3:24 pm
+ Author: Sonya Duffin


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/19100940/checklist2-e1634652595388.jpg)
If you’re like most IT professionals, the threat of a ransomware attack might keep you up at night. And you have a valid reason to worry — ransomware doesn’t discriminate. Organizations across every industry, public or private, are potential victims, if they haven’t been victims already.


In fact, recent Veritas Technologies [research](https://www.veritas.com/form/whitepaper/vulnerability-lag) suggests that the average organization has had 2.57 ransomware attacks that led to significant downtime in the past 12 months, with 10 percent experiencing downtime that impacted business more than five times.


Although ransomware can cause serious damage to your business and reputation, it’s not invincible. In fact, it’s only as strong as your organization’s weakest link. The good news is that there are clear steps your organization can take to prevent being a cybercrime target and diminish the likelihood that an attack could take down your business.


Let’s look at the 10 most impactful best practices you can implement today to protect your data and ensure business resilience.


**1. Prompt Systems Upgrades and Software Updates**
---------------------------------------------------


Using out-of-date software can allow attackers to exploit unmitigated security vulnerabilities. To reduce your attack surface, ensure you patch and upgrade all infrastructure, operating systems and software applications frequently. It’s also important to update your backup application. Don’t fight today’s ransomware with yesterday’s technology.


**2. Implement the 3-2-1-1 Backup Rule**
----------------------------------------


If you back up your data, system images and configurations frequently, you’ll always have an up-to-date place to resume operations if ransomware does strike. Better yet, go one step further and avoid a single point of failure, by dispersing your data using the 3-2-1 backup rule.


This means keeping *three* or more copies in different locations, using *two* distinct storage mediums and storing *one* copy off-site. This will reduce the chances of an attacker gaining access to everything. This 3-2-1 approach also ensures that a vulnerability in one of those doesn’t compromise all your copies, and it provides options if an attack takes out an entire data center.


Many organizations are also now going one more step to 3-2-1-1, by keeping at least one copy on immutable (can’t be changed) and indelible (can’t be deleted) storage.


**3. Implement the Zero-Trust Model**
-------------------------------------


The zero-trust model [is a mindset](https://threatpost.com/key-questions-zero-trust-success/175392/) that focuses on not trusting any devices — or users — even if they’re inside the corporate network, by default.


Instead of just requiring a password (yes, even if it’s long and complicated), also require multi-factor authentication (MFA) and role-based access control (RBAC), monitor for and mitigate malicious activity, and encrypt data both in-flight and at-rest, which renders exfiltrated data unusable.


It warrants sharing loudly and openly that you should never use factory passwords anywhere.


Also, if you limit access to backups, you’ll shut down the most common entry method for ransomware. Many organizations are moving towards a just-in-time (JIT) security practice where access is granted on an as-needed basis or for a predetermined period of time, which is something to consider for crucial and business critical data.


**4. Network Segmentation**
---------------------------


Attackers love a single continuous, flat network. That means that they can spread throughout your entire infrastructure with ease.


An effective way to stop attackers and significantly reduce their attack surface is with network segmentation and micro-segmentation. With this model, networks are divided into multiple zones of smaller networks and access is managed and limited, especially to your most crucial data.


It’s also a common best practice to keep the most vital infrastructure functions off the web. Additionally, as part of your company’s zero-trust model, consider segmenting third-party vendors, as there have been many notable attacks to supply chains resulting from vendor mismanagement. The [Sunburst hack](https://threatpost.com/solarwinds-default-password-access-sales/162327/) and [Colonial Pipeline attack](https://threatpost.com/colonial-pays-5m/166147/) are two great examples.


**5. Endpoint Visibility**
--------------------------


Most organizations have a severe lack of visibility into remote endpoints. It has now become a common practice for bad actors to get past front-line security and hang out — staying dormant long enough to locate weaknesses and find the opportune time to attack. It is vital that you implement tools that provide complete visibility across your entire environment, detect anomalies, and hunt for and alert you to malicious activity on your network, giving ransomware no place to hide. This will help you to mitigate both threats and vulnerabilities before the bad actors have the opportunity to take action.


**6. Immutable and Indelible Storage**
--------------------------------------


As mentioned earlier, one of the best ways to safeguard your data against ransomware is to implement immutable and indelible storage, which ensures that data cannot be changed, encrypted or deleted for a determined length of time. However, the term “immutable storage” has become somewhat of a buzzword across backup vendors these days. Look for immutability that is not just logical but also includes physical immutability, and it’s important to include built-in security layers.


The industry is moving towards two types of immutability. At Veritas, we call them Enterprise Mode and Compliance Mode. Enterprise Mode is known as a “four eyes” approach—meaning you need two sets of eyes to validate any change. For example, the first pair of eyes is the backup admin’s and the second pair of eyes is the security admin’s. Without both providing approval, no alteration is possible. Compliance Mode refers to un-alterable immutability, which is data that is not changeable under any circumstances. Both modes include a Compliance Clock that is completely independent from the OS, so that if the OS clock is spoofed, it does not affect the release of the data.


**7. Rapid Recovery**
---------------------


Most ransomware attackers hope for two things: Time for the attack to spread; and money (from you) to make it stop. Historically, recovery could take weeks or even months when it was an extremely manual and labor-intensive process that extended across multiple stakeholders within an organization. Now, recovery can be orchestrated and automated with flexible and alternative options — such as rapidly standing up a data center on a public cloud provider — that can shorten downtime and provide alternatives to paying a ransom. With the right systems in place, recovery times can be reduced to seconds if necessary.


**8. Regular Testing and Validation**
-------------------------------------


Creating a comprehensive data-protection plan doesn’t mean your job is finished. Testing ensures your plan will work when you need it. And although initial testing can confirm all aspects of the plan actually work, it’s critical to test regularly, because IT environments are constantly in flux.


Importantly, any plan is only as good as the last time it was tested, and if you don’t test, then there is no guarantee that you can recover quickly! It’s also vital to implement solutions that test to a non-disruptive, isolated recovery or sandbox environment.


**9. Educated Employees**
-------------------------


It’s common knowledge that employees are often the gateway for an attack. Don’t blame your employees—mistakes happen. Modern phishing attacks and social engineering are now so advanced that they often fool security professionals.


Instead, focus on training employees to identify phishing and social engineering tactics; build strong passwords; browse safely; utilize MFA; and always use secure VPNs, never public Wi-Fi. Also ensure that employees know what to do and who to alert if they fall victim.


**10. Cyberattack Playbooks**
-----------------------------


Imagine if everyone in your organization knew exactly what to do and when, in the face of a ransomware attack. That’s not impossible if you create a standard [cyberattack playbook](https://threatpost.com/proactive-ransomware-playbook-threat-landscape/176224/) that clarifies roles, and aligns and empowers cross-functional teams with clear communication paths and response protocols in the event of emergencies.


A great piece of advice is to set up an emergency communication channel on a secure texting app for senior leadership of your organization to communicate in the event of a cyberattack, as company email or chat systems may also be down as a result of the attack. It is also a great idea to hire a third-party agency to audit your team’s strategy and check your work.


You have the power to take important steps to combat ransomware and flip the tables on cybercriminals. By putting together a multi-layered ransomware resiliency strategy that includes the best practices above and impeccable cybersecurity hygiene, you can stop attackers before they gain a foothold.


***Sonya Duffin is a ransomware and data protection expert at [Veritas Technologies](https://www.veritas.com).***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[ransomware]] [[it’s]] [[It’s]] [[attack.]] [[doesn’t]] [[data.]] [[ThreatPost]]
