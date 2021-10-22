# FIN7 Lures Unwitting Security Pros to Carry Out Ransomware Attacks
### The infamous Carbanak operator is moving is looking to juice its ransomware game by recruiting IT staff to its fake Bastion Secure ‘pen-testing’ company. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175681)
+ Date: October 22, 2021  3:59 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/22155602/help-wanted-sign-on-store-window-vf-e1634932579106.png)
The financially motivated cybercrime gang behind the Carbanak backdoor malware, FIN7, has hit upon a genius idea for maximizing profit from ransomware: Hire real pen-testers to do some of their dirty work instead of striking partnerships with other criminals.


According to a report from Gemini Advisory, the group has set up a fake security company (called “Bastion Secure”) and is looking to hire security pros under the guise of needing red-teaming expertise for its clients. In reality, the duped “employees” are carrying out malicious activity, unbeknownst to them.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


It’s not the first time FIN7 has masqueraded as a legitimate security firm, but this latest gambit showcases its continued expansion into the ransomware area, researchers noted.


**FIN7’s Expansion into Ransomware**
------------------------------------


FIN7 (aka Carbanak Gang or Navigator Group) has been in operation since at least 2015, and is well-known for both maintaining persistent access at target companies with its custom backdoor malware, and for targeting point-of-sale (PoS) systems with skimmer software. The group often targets [casual-dining restaurants](https://threatpost.com/chilis-doesnt-leave-data-breach-on-the-back-burner/131955/), casinos and hotels, and it’s been wildly successful at it, too: In the U.S. alone, FIN7 has stolen more than 20 million customer card records from more than 6,500 individual PoS terminals at more than 3,600 separate business locations, in all 50 states, [according to the Department of Justice](https://threatpost.com/fin7-pen-tester-jail/167293/). The total haul in terms of victim losses has exceeded $1 billion.


Since 2020 though, FIN7 [has gotten into](https://threatpost.com/fin7s-liquor-lure-law-firm-backdoor/168086/) the ransomware/data exfiltration game, with its activities involving [REvil](https://threatpost.com/revil-servers-offline-governments/175675/) or [Ryuk](https://threatpost.com/ryuk-ransomware-worming-self-propagation/164412/) as the payload, Gemini researchers added. The attacks have included the careful selection of targets according to revenue using the ZoomInfo service, performing recon, establishing initial access and carrying out all of the advanced activities these types of hits require – however, FIN7’s exact involvement in the process is unknown.


“Whether they sold the access to ransomware groups or have formed a partnership with these groups remains unclear,” according to the report, [issued Thursday](https://geminiadvisory.io/fin7-ransomware-bastion-secure/) – which was based on information from a source who was almost duped into becoming one of FIN7’s recruits. “However, the tasks that were assigned to the Gemini source by FIN7 (operating under the guise of Bastion Secure) matched the steps taken to prepare a ransomware attack.”


Typically, the ransomware economy is a [complex tangle of relationships](https://threatpost.com/inside-ransomware-economy/166471/), with ransomware-as-a-service (RaaS) gangs offering their malware for rent to affiliates, who perform the actual cyberattack in exchange for a portion of the ransom. These affiliates may in turn partner with other cybercriminals who offer services like initial access via persistent backdoors, rental of various tools, and post-attack activities like money laundering. The total cost of an attack can be an expensive endeavor, which a millions-dollar ransom of course makes worthwhile.


Gemini researchers theorized that Bastion Secure is an idea for retaining a maximum amount of profit from this new arm of FIN7 operations, by operating outside of this paradigm. Simply put, paying “legit” salaries is cheaper than what services go for on the cyber-underground.


“Bastion Secure’s job offers for IT specialist positions ranged between $800 and $1,200 USD a month, which is a viable starting salary for this type of position in post-Soviet states,” according to Gemini. It added that with willing accomplices, FIN7 would be forced to share a percentage of ransom payments – but “FIN7’s fake company scheme enables the operators of FIN7 to obtain the talent that the group needs to carry out its criminal activities, while simultaneously retaining a larger share of the profits.”


Given FIN7’s increased interest in ransomware, Bastion Secure is likely specifically looking for system administrators, Gemini speculated. Those skills would include the ability to map compromised companies’ systems; identify users and devices within the systems; and locate backup servers and files.


“FIN7 operators could obtain the initial access through their well-documented phishing and social-engineering methods, or by purchasing access on Dark Web forums from a large pool of vendors,” according to Gemini. “Once the system administrator mapped out the system and identified backups, FIN7 could then escalate to the next step in the malware and ransomware infection process.”


**Bastion Secure: Your New, Legit-Looking Employment Home**
-----------------------------------------------------------


FIN7 has gone to great lengths for verisimilitude for its fake company, starting with the name, Bastion Secure, which Gemini pointed out is remarkably close to the name of a real company specializing in physical security called Bastion Security.


The company’s office addresses meanwhile are lifted from a real but now-closed office for the legitimate Bastion Security, and three real office buildings that contain multiple businesses, in Hong Kong, Moscow and Tel Aviv.


Then, there’s the website. Gemini found that the malicious company’s web presence is just a copy of Convergent Network Solutions’ site (though it’s hosted on a Russian domain registrar favored by cybercriminals called Beget – a potential red flag).


In short, a quick Google search may be enough to convince someone the faux Bastion Secure was a legit deal.


“The criminal group leveraged true, publicly available information from various legitimate cybersecurity companies to create a thin veil of legitimacy around Bastion Secure,” according to the report. “In effect, FIN7 is adopting disinformation tactics so that if a potential hire or interested party were to fact-check Bastion Secure, then a cursory search on Google would return ‘true’ information for companies with a similar name or industry to FIN7’s Bastion Secure.”


Bastion Secure also posts legitimate-appearing job offers on both its own website and prominent job-search sites in post-Soviet states, according to the report. It’s also happy to provide reputable-seeming references for additional credibility.


“In the past several months, Bastion Secure has posted job offerings for system administrators on job search sites and added new vacancies for PHP, Python, and C++ programmers and reverse engineers on their website,” according to Gemini researchers. “On these job sites, Bastion Secure provides sufficiently professional information to appear legitimate and includes purported office information and a phone number.”


**Bastion Secure’s Steps to Recruitment**
-----------------------------------------


The report detailed FIN7’s careful recruitment and grooming of security pros, based on the source who went through the process. The effort involves three stages.


Based on the experience of Gemini’s source, the first stage of the hiring process offers zippo indication that something is amiss, researchers said.


First, an “HR representative” tells the target that he or she has reviewed the source’s resume and is interested in hiring them as an IT specialist. After that, the rep sets up a normal-seeming first-stage interview – albeit via messages on Telegram (potentially a red flag).


After completing the interviews, the source is told what to expect for next steps:


The second stage of the hiring process didn’t really flag Bastion Secure as a cybercriminal operation either, according to the source: The target is simply instructed to install certain platforms and conduct a series of practice assignments that Gemini noted would be typical for the position.


The software was purportedly licensed to “Checkpoint Software,” which of course attempts to coopt the name of legitimate company Check Point. However, the firm’s analysis uncovered that the tools provided are actually components of the infamous remote-access trojan (RAT) Carbanak, and a recently developed RAT called Lizar/Tirion.


There were a few “things that make you go hmmm” moments: For one, the company warned of big fines fine if the source installed antivirus software on the virtual machine; and two, the source was told that employees are required to use specific tools to avoid detection.


In the third stage, Bastion Secure offers the mark a “real” assignment with a “client company” to work on. This is where the façade fell apart for the source, according to Gemini.


“It became immediately clear that the company was involved in criminal activity,” researchers said. “The task would have been to use a script to collect information on domain administrators, domain trust relationships, file shares, backups and hypervisors….Bastion Secure provided access to the company’s network without any legal documentation or explanation.”


Gemini’s source noted that this, combined with the red flags from earlier in the hiring process, indicated that something shady was going on.


**Masquerading as Legitimate**
------------------------------


It’s unclear how successful Bastion Secure has been so far, but it’s continuing its endeavors – its website and job listings are still up and running, according to Gemini.


Masquerading as being involved in legitimate security activities is a bit of a tried-and-true (and staggeringly ironic) tactic for FIN7. In May for instance the Lizar RAT was [discovered spreading](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/) under the guise of being a Windows pen-testing tool for ethical hackers. In that case, FIN7 was pretending to be a legitimate organization that hawks a security-analysis tool.


Before that, security company BI.ZONE observed it pushing Carbanak under the guise of the package being a tool from cybersecurity stalwarts Check Point or Forcepoint, just as Bastion Secure does.


And as far back as 2018, the U.S. Department of Justice found FIN7 [posing as “Combi Security,”](https://www.justice.gov/opa/pr/three-members-notorious-international-cybercrime-group-fin7-custody-role-attacking-over-100) another fake cybersecurity company, to involve unaware IT specialists in its carding campaigns.


The tactic also isn’t specific to FIN7, though it’s been used to achieve different outcomes. Earlier this year, a North Korean advanced persistent threat group (APT) called Zinc, which has links to the more notorious APT Lazarus, mounted two separate attacks looking to infect security researchers with malware.


In January, the group [used elaborate social-engineering efforts](https://threatpost.com/north-korea-security-researchers-0-day/163333/) through Twitter and LinkedIn, as well as other media platforms like Discord and Telegram, to set up trusted relationships with researchers by appearing to themselves be legitimate researchers interested in offensive security.


Specifically, attackers initiated contact by asking researchers if they wanted to collaborate on vulnerability research together. They demonstrated their own credibility by posting videos of exploits they’ve worked on, including faking the success of a working exploit for an existing, patched Windows Defender vulnerability that had been exploited as part of the massive SolarWinds attack.


Eventually, after much correspondence, attackers provided the targeted researchers with a Visual Studio Project infected with malicious code that could install a backdoor onto their system. Victims also could be infected by following a malicious Twitter link.


Zinc [was back at it in April](https://threatpost.com/north-korean-apt-security-researchers/165155/), using some of the same social-media tactics but adding Twitter and LinkedIn profiles for a fake company called “SecuriElite,” which purported to be an offensive security firm located in Turkey. The company claimed to offer pen tests, software-security assessments and exploits, and purported to actively recruit cybersecurity personnel via LinkedIn.


While it’s not a new tactic, this latest case pushes the envelope on truthiness, Gemini noted. “Not only is FIN7 looking for unwitting victims on legitimate job sites, but also attempting to obfuscate its true identity as a prolific cybercriminal and ransomware group by creating a fabricated web presence through a largely legitimate-appearing website, professional job postings, and company info pages on Russian-language business development sites,” the report recapped.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[FIN7]] [[ransomware]] [[FIN7’s]] [[it’s]] [[cybersecurity]] [[Gemini.]] [[Carbanak]] [[It’s]] [[company’s]] [[ThreatPost]]
