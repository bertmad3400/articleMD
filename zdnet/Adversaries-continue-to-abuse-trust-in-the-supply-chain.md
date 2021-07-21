# Adversaries continue to abuse trust in the supply chain
### A recent ransomware attack used one system to successfully target thousands of victim companies.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/adversaries-continue-to-abuse-trust-in-the-supply-chain/)
+ Date: July 20, 2021 -- 20:32 GMT (21:32 BST)
+ Author: Forrester Research


## Article:
Unknown

We trust so much in our organizations — systems, partners, and vendors — for deploying software, monitoring [network performance](https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack), [patching](https://www.wsj.com/articles/one-year-after-notpetya-companies-still-wrestle-with-financial-impacts-1530095906) (both systems and software), procuring software/hardware, and performing so many other tasks. A recent ransomware attack used one such system to successfully target thousands of victim companies.  


In this most recent example, attackers targeted Kaseya VSA IT Management Software, which was designed to allow IT admins to monitor systems, automate mundane tasks, deploy software, and patch systems. Attackers were able to [exploit a zero day](https://helpdesk.kaseya.com/hc/en-gb/articles/4403584098961) to access customer instances of the product and use its native functionality to deploy ransomware to those customers endpoints.

Further compounding the problem, managed service providers (MSPs) use Kaseya software to manage their customer environments. When the attackers compromised Kaseya, the MSPs inadvertently and unknowingly spread the ransomware to their customers.  

This is only one example of how attackers continue to abuse trust in unique ways that leaves many security and IT practitioners to wonder, "Why didn't something like this happen sooner?" 

### **Attackers Are Getting Bolder**

Ransomware group REvil continues to get even bolder. Make no mistake, an attack like we saw against Kaseya was prescriptive and purposeful to inflict the maximum amount of damage to the most amount of targets. Immediately after the attack, they bragged about infecting more than [a million devices and set a ransom demand of $70 million](https://www.theverge.com/2021/7/5/22564054/ransomware-revil-kaseya-coop). If one organization paid, they promised that the decryptor would work across all organizations that were affected.  

This shines a light on a troubling trend we're seeing, where attack targets are shifting from individual organizations to exploiting platforms, like Kaseya or SolarWinds, that allow for multiple organizations to be affected. Attackers continue to research the tools we all rely on to find ways to abuse the native functionality to effectively execute an attack. This latest attack abused an old copy of Microsoft Defender that allowed sideloading of other files.  

### **Software Is Vulnerable All The Way Down The Chain**

All the tools that organizations rely on -- such as tax software, oil pipeline sensors, collaboration platforms, and even security agents -- are built on top of the same vulnerable code, platforms, and software libraries that your vulnerability management team is screaming from the hills to patch or update immediately.  






Organizations need to both hold their supply chain partners, vendors, and others accountable for addressing the vulnerabilities in the software that they've built on top of this house of cards as well as understand the exposure they have by deploying said software within their environments. 

### **Run Faster Than The Next Guy; Take Defensive Steps Now**

Forrester blog, [Ransomware: Survive By Outrunning The Guy Next To You](https://go.forrester.com/blogs/ransomware-survive-by-outrunning-the-guy-next-to-you/?utm_source=zdnet&utm_medium=pr&utm_campaign=sr), discusses protecting against ransomware by hardening systems to make your organization a hard target. Supply chain attacks bypass defenses by exploiting your trust in systems. To protect against them, you have to scrutinize the inherent trust you've placed on your supply chain.  

To start, organizations should take an inventory of the critical partners that have a large foothold within their environment, such as the vendors used for collaboration/email, MSPs that manage and monitor infrastructure, or security providers that may have an agent deployed to every system. After compiling your list, you should:  

* Ask those partners what they're doing to prevent you from being the next victim of a destructive attack. Ask about the gating process for pushing updates to your environment. How do they QA updates before they're pushed? Ask solution providers how they secure their code and assess that code for vulnerabilities.
* Find out if they have the appropriate processes and architecture in place to prevent the type of lateral movement we saw with the latest attack. Ask how they secure their own environments, especially their update servers. Ask to see audit or assessment results from third-party assessors.    

* [Review your service agreements](https://news.bloomberglaw.com/tech-and-telecom-law/supply-chain-hit-spurs-companies-to-rethink-vendor-relationships) to find out what contractual responsibility those partners have to keep you safe from ransomware and malware. Understand what rights you have to demand compensation, if you are the victim of an attack due to a service provider's systems being used as a delivery vehicle.    


Organizations should take aggressive steps to implement prescriptive [ransomware advice](https://go.forrester.com/blogs/ransomware-survive-by-outrunning-the-guy-next-to-you/?utm_source=zdnet&utm_medium=pr&utm_campaign=sr) as well as take a look at additional [ransomware resources](https://go.forrester.com/blogs/forresters-list-of-ransomware-resources/?utm_source=zdnet&utm_medium=pr&utm_campaign=sr) to limit the blast radius of an attack.  

*This post was written by Analyst Steve Turner, and it originally appeared*[*here*](https://go.forrester.com/blogs/using-our-tools-against-us-adversaries-continue-to-abuse-trust-in-the-supply-chain/?utm_source=zdnet&utm_medium=pr&utm_campaign=sr)*.*






#### Tags:
[[ransomware]] [[Kaseya]] [[MSPs]] [[ZDNet]]
