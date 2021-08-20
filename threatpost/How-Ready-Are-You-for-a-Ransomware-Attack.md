# How Ready Are You for a Ransomware Attack?
### Oliver Tavakoli, CTO at Vectra, lays out the different layers of ransomware defense all companies should implement.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168837)
+ Date: August 19, 2021  5:13 pm
+ Author: Oliver Tavakoli


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/19171000/ransomware-6-e1629407417209.jpg)
Determining how hard a target you present for the current wave of human-driven ransomware involves multiple considerations. There are four steps to analyzing how prepared you are for a ransomware attack.


Such analysis roughly breaks down as follows: (1) How easy it is to break into your environment in the first place; (2) given an initial toe-hold, how difficult is it for an attacker to escalate privilege, move laterally and get access to data and systems critical to your business; (3) do you have a handle on data which would warrant a substantial ransom to prevent public disclosure and how easy would it be to exfiltrate large amounts of data from your environment without detection; and (4) how confident are you of your ability to quickly restore your environment from backups?


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


It’s important to note that while you may end up on their list of targets, they will walk away if your environment ends up posing too big a challenge – after all, they only care about the money and if there is an easier target they could be attacking instead, they are apt to move on. So, this is not like a targeted attack being carried out by a nation-state where there is great motivation on the part of the attacker to specifically attack you. In the context of human-operated ransomware, putting up enough of a fight can prove effective in actually thwarting the attack.


Breaking In
-----------


Note that the various groups carrying out ransomware attacks have different skills and utilize different tools, but they all employ some combination of automated and manual techniques.


There are two main ways in which attackers gain initial access to your environment: By leveraging human beings, and by attacking internet-accessible services.


By far the most common way of targeting human beings is via phishing emails, though there are also variants such as watering-hole attacks (e.g. hacking the website of a local food delivery service which your organization frequents), which can be effective. You will never achieve perfect security, but the goal here should be to have credible controls, less gullible employees, good email security, good web security gateways and patched end user systems (especially web browsers).


Protecting yourself from attacks on your internet-accessible services is a bit more complicated. It’s easy to assume that you have an accurate inventory of all your internet-accessible services – until a developer stands up a test system under an AWS account that you’re not even aware of. Time spent on understanding what part of your environment is internet-accessible (i.e., your organization’s “digital footprint”) is important cyber-hygiene.


For every service which is internet-accessible, your patching and authentication strategies need to be top-notch, as it is relatively easy for hackers to reuse publicly available exploits and attempt brute-force authentication attacks, which are normal everyday occurrences for such services.


Escalating Privilege and Moving Laterally
-----------------------------------------


Setting the bar high enough to protect against initial entry is a laudable goal, but also adheres to the law of diminishing returns. This means the focus must shift towards improving how difficult it is for an attacker to move around your environment once they have gotten inside.


This phase of the attack often requires some manual control, so identifying and disrupting command and control (C2) channels can pay significant dividends – but realize that only the least sophisticated attacker will reuse the same domains and IPs of a previous attack. So rather than looking for C2 communications via threat intel feeds, your approach needs to be to look for patterns of behavior which look like remote-access trojans (RATs) or hidden tunnels (suspicious forms of beaconing).


Barriers to privilege escalation and lateral movement come down to cyber-hygiene related to patching (are there easily accessible exploits for local privilege escalation?), rights management (are accounts granted overly generous privileges?) and network segmentation (is it easy to traverse the network?).


Most of the current raft of ransomware attacks have utilized the serial compromise of credentials to move from the initial point-of-entry to more useful parts of the network. Particularly valuable targets for these attacks are Microsoft servers which have rights to Group Policy Object (GPO) and Active Directory Domain Controllers.


One of the means of determining how easy this form of lateral movement is in your environment is to run a [tool like BloodHound](https://github.com/BloodHoundAD/BloodHound) to visualize the possible attack paths leading to these targets.


Exfiltration and Public Disclosure
----------------------------------


Most modern ransomware attacks try to maximize the likelihood of ransoms being paid by exfiltrating data as well as encrypting it – thus being able to threaten public disclosure of data (which may result in fines or embarrassment).


Whether you’re likely to pay a substantial ransom to prevent public disclosure of data depends entirely on the type of business you run and the data you retain. Think about the data you would least like to see leaked (the standard [80/20 rule](https://en.wikipedia.org/wiki/Pareto_principle) probably applies) and place additional controls over access to it – this will generally buy you more time to detect and evict attackers before they get to this data.


Also consider whether an exfiltration of several gigabytes of data (this is the scale that’s generally involved in ransomware attacks) would likely raise an alarm from one of your existing security controls, and question how quickly you would notice and stop such a transfer.


Encryption and Ability to Restore Operations
--------------------------------------------


At this point in the campaign, the attackers have entered your environment, spread laterally and exfiltrated data they believe to be valuable and have started encrypted that data. Assuming you stopped things now, how difficult would it be to restore operations?


Attackers will try to go after your backups to further skew this calculus in their favor, so ensure that the backups are not accessible with your existing credentials or that you employ immutable backup solutions. It will also be important to understand how quickly you can restore from backups – after all, if you can restore 10 gigabytes an hour (which sounds great) but you have 100 terabytes of data to restore, it will take you more than 400 days to restore your data.


Some Final Points
-----------------


Your obvious goal in dealing with ransomware attacks is to catch them (and eject the attacker) before exfiltration begins. But even before exfiltration starts, the attacker may well have gotten access to GPO and pushed malware to all domain-joined systems – so you really want to catch the attack before that happens, as remediation after this point is bound to be expensive and very time-consuming.


The further left you move in the timeline of the attack, the more you will have to rely on aggregating several weaker signals into one stronger one to identify a possible ransomware attack. The more hurdles you throw in the path of the attacker – in terms of cyber-hygiene, and detection and response capabilities – the more likely it is that the attacker will give up or that you will buy yourself enough time in this race against the clock to successfully evict them from your network.


***Oliver Tavakoli is CTO at Vectra.***


***Enjoy additional insights from Threatpost’s InfoSec Insider community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***


 




#### Tags:
[[ransomware]] [[attack.]] [[internet-accessible]] [[data.]] [[ThreatPost]]
