# Why is Cybersecurity Failing Against Ransomware?
### Hardly a week goes by without another major company falling victim to a ransomware attack. Nate Warfield, CTO at Prevailion, discusses the immense challenges in changing that status quo.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175637)
+ Date: October 21, 2021  9:16 am
+ Author: Nate Warfield


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/21084125/strategy.jpg)
Yes, security is hard – no one is ever 100 percent safe from the threats lurking out there. But how is it that time and time again, companies – big companies – are [continuing to fall for](https://threatpost.com/ransomware-candy-corn-halloween/175630/) ransomware attacks? Why aren’t we getting any better at preventing them?


Let’s explore the main reasons why, starting with some basics before getting more in-depth:


2FA Not Implemented Universally
-------------------------------


Two-factor authentication (2FA) is probably the easiest security improvement an organization can implement, and it’s one of the most advocated-for solutions by infosec professionals. Despite this, we continue to see breaches like [Colonial Pipeline](https://threatpost.com/takeaways-colonial-pipeline-ransomware/166980/) occur because organizations have either failed to implement 2FA or have failed to *fully* implement it.


Anything that requires a username and password to access should have 2FA enabled. That means email, business applications, cloud deployments, VPNs – anything with logon credentials.


User Errors Will Never Stop – Why Pretend Otherwise?
----------------------------------------------------


Modern phishing techniques are so advanced that even infosec practitioners fall prey to them, so how can the average user be expected to perform any better?


Attackers perform recon against their targets and tune their techniques for success. And many employees’ workflows are literally a case study in what phishing attacks target. After all, how can Pat in accounting – whose job it is to open PDFs and process purchase orders – be expected to know on-sight which PDF is safe and which could contain malware?


We place unrealistic expectations on users, then act surprised and blame them when they make the same mistake many infosec pros have made themselves. Dave Aitel hit the [nail on the head](https://www.csoonline.com/article/2131941/why-you-shouldn-t-train-employees-for-security-awareness.html) years ago when he argued that employees can’t be expected to not screw up. Employees are always going to make mistakes, so why do we pretend that will change?


Antivirus Solutions Rely on Easily Bypassed Detection Logic
-----------------------------------------------------------


Antivirus, the oldest security software in existence, has come a long way in the last 20 years. However, many AV solutions still rely on antiquated signature-based systems to detect malicious software.


Detecting malicious code with AV is predicated on having a binary signature of the code, or a file hash, and this only works if the code doesn’t change. Renaming functions inside the code prior to compiling it or moving code blocks around inside the code can render a previously viable detection useless.


Traditional AV does not “detonate” malware – that is, run the code in a protected sandbox – so even though the behavior of the malware will be identical regardless of its signature, this is extremely difficult to detect.


This problem is so systemic that frameworks like [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) exist to help red teams – and subsequently malicious actors – bypass antivirus solutions.


EDR/XDR/MDR Solutions Are Prone to Delays
-----------------------------------------


The myriad of “DR” (detection and response) endpoint solutions are significantly more robust than antivirus, but they too have their limits.


Since the logic to process endpoint events lives in the cloud, it means there can be a delay of several seconds to several minutes between an event occurring and its arrival in the administrator’s console. This makes them prone to missing ransomware execution.


When a ransomware payload is activated, the entire network can be shut down within a matter of seconds, maybe minutes. Ransomware operators will frequently stage the actual ransomware payload across all systems in the network ahead of time, so that the payload is executed nearly simultaneously across all systems in the organization, and far faster than a DR solution will be able to detect.


It’s worth pointing out that DR+AV solutions from the same vendor frequently come with a ‘block’ option which may allow the administrator to isolate/quarantine a machine if a malicious payload or sequence of actions is detected. However, in practice this option is generally disabled by default and – due to concerns of impacting user productivity due to false positives – it’s frequently left disabled.


LOLBin Techniques Are Harder to Detect
--------------------------------------


Another common reason why ransomware succeeds is that the operators have learned to use a technique called “living off the land binaries” (LOLBins).


These are normal administrative tools, generally in Microsoft Windows, but all modern operating systems have some. These tools have valid, legitimate purposes and are used every day by administrators, which makes the detection of *malicious* use of these tools exceedingly difficult. For example, the recent leak of the [Conti group’s playbook](https://threatpost.com/affiliate-leaks-conti-ransomware-playbook/168442/) shows a heavy reliance on standard Windows administrative tooling.


It’s trivial for antivirus and DR solutions to catch bespoke, actor-developed tools, but nearly impossible to determine if commands to look up the local Domain Controllers and who the Domain Administrators are were done as part of troubleshooting network connectivity or a precursor to lateral movement. For this reason, most DR vendors either don’t alert on use of these LOLBins, or alert with low severity as these commands have a very high false-positive rate when used to detect malicious activity.


In some cases, the LOLBin tools can be leveraged for additional functionality which was added to the code because a developer or customer at one point wanted their administrative tools to have the ability to download arbitrary files from the internet, or the tools themselves can start secondary applications.


This is done to bypass a security control called Application Allow-Listing. Allow-listing tells the operating system not to run any software unless it has been digitally signed by a trusted vendor (Apple, Google, Microsoft, etc.). However, by tricking a valid, signed application into opening an untrusted, unsigned application, the attackers can bypass this security control with nothing more than default applications which are part of the operating system.


Freely Available Attack Toolsets Have Lowered the Bar for Ransomware Groups
---------------------------------------------------------------------------


Attackers have never had it better in terms of [freely available tooling](https://threatpost.com/apt-harvester-telco-government-data/175585/), such as Metasploit and Mimikatz, or pirated copies of Cobalt Strike.


Whether they need phishing toolsets, obfuscation frameworks, initial access tools, command-and-control (C2) infrastructure, credential-abuse tools or even open-source ransomware payloads, nearly all of this can be found for free on GitHub. Most people assume malicious actors are hiding on the Dark Web, selling tools for Bitcoin to only the shadiest of black hats, but this simply isn’t true.


The industry has given offensive security professionals its blessing to develop and release attack frameworks under the rationale that “defenders need to understand these tactics.” But this glosses over the fact that attack frameworks also help the attackers and make it harder for defenders to keep up.


While it’s true that defenders do need to understand offensive tactics, in reality, most defenders are too swamped in day-to-day work to have the time to test every offensive framework and then develop defensive guidance.


Most of these attack tools are well documented in their use, but not their detection. And while the barrier for entry of an attacker has dropped to “can you use Google, GitHub and have basic computer skills,” defenders are left paying huge sums of money for complex tooling and appliances which may only perform well in a controlled test scenario.


Ransomware Groups Collaborate Better than the InfoSec Industry
--------------------------------------------------------------


Ransomware cartels exist because they collaborate. In fact, most in the security industry agree that bad actors actually collaborate *better* than the teams and organizations trying to stop them.


By spreading the work across multiple criminal groups, it makes the tactics, techniques and procedures (TTPs) harder to attribute to any single actor, it can obfuscate the intentions of the malicious actor and it allows ransomware-as-a-service (RaaS) cartels to prioritize high-value targets.


The [profit-sharing model](https://threatpost.com/inside-ransomware-economy/166471/) of RaaS works well to motivate these actors to constantly find new targets, while shifting the heavy lifting to more sophisticated professionals. This method of collaboration leads to a highly effective division of labor, with criminal groups farming out initial access, and requiring their affiliates to select high-value, high-net-worth organizations that are more likely to pay the ransom than a small family-owned business (although the latter clearly isn’t immune).


Once the attacker determines the business they’ve impacted and the value of the company, they’ll set the ransom to something the victim can afford. An attack which costs one company $10,000 might cost another company $10 million, and it’ll use the exact same tooling, attack flow, access broker and ransomware payload.


Lack of Coordinated Response & Strategy in Both Private & Public Sectors
------------------------------------------------------------------------


Ransomware isn’t a new threat, but it’s become increasingly easier to accomplish, get paid and get away with. A big part of the problem is at the public-sector level – for years, there has been no clear policy, direction or strategic planning for how the federal government should address these attacks. We are struggling to develop a consistent policy for deterrence, as well as for response.


So, many businesses that are hit are left with no recourse except to pay the ransom.


The U.S. government’s targeted prosecutions of individuals has had [little if any impact](https://threatpost.com/trickbot-malware-virtual-desktop-espionage/167789/) on criminal or nation-state activity. And public/private sector coordination has been sorely lacking; it has only recently become a greater priority.


The above-mentioned public-policy problems are exacerbated by that fact that ransomware gangs frequently operate in countries outside of U.S. jurisdiction and without U.S. extradition agreements.


Countries like Russia have made it clear they will not extradite bad actors from their country, unless it’s part of a much larger deal with the U.S. (and geopolitical strategy), nor will they take any domestic law-enforcement action unless these actors attack Russian businesses. This means criminals are essentially free to operate – unhindered and with impunity.


This is why most ransomware payloads check for Russian and bordering country languages in-use by the operating system and immediately, harmlessly, self-destruct if they detect themselves running on a system in a country where an attack could draw the ire of the Russian government.


The geopolitical aspects of this problem are non-trivial, [if they can even be addressed](https://www.nytimes.com/2021/10/14/us/politics/global-ransomware-meeting.html). The internet has no borders, and while an attacker may decide to obfuscate their location and mimic a Russian-based attacker, there is no way to determine with absolute certainty that the attack originated from within Russian borders. This makes traditional government methods of bending a country to their will – like sanctions, embargoes, import tax increases, etc. – an infeasible way of inflicting consequences.


Cryptocurrency Fuels the Entire Industry
----------------------------------------


Cryptocurrency will be remembered for two things: Facilitating ransomware and exponentially increasing CO2 output. In all seriousness, without a robust cryptocurrency ecosystem, ransomware gangs would be starved out of existence.


Cryptocurrency fuels the entire criminal industry, as it provides a financial framework that bypasses the U.S.-controlled global financial system, is often difficult to trace (even though ransom payments are often demanded in Bitcoin, they are then transferred into a different, untraceable cryptocurrency before withdrawing the funds) and easily crosses international boundaries.


Although the U.S. Treasury Department recently sanctioned the [cryptocurrency exchange SUEX](https://threatpost.com/feds-sanctions-suex-cryptocurrency-ransomware/174895/) for its alleged involvement in ransomware crime, this action is just a drop in the ocean. These groups can also shift to different exchanges, require direct transactions from victims or switch to harder to trace cryptocurrency like Monero.


If the U.S. government wants to get serious about crippling the criminal cryptocurrency industry, it should target the untraceable coins themselves – by sanctioning any business (crypto or otherwise) that allows these transactions and conversions.


**What to Do About the Ransomware Scourge**
-------------------------------------------


Unfortunately, there is no silver bullet to stop the existential threat ransomware poses to computing, critical infrastructure and the increasingly interconnected world we live in.


Users and organizations need to be ever vigilant, adopt multi-layered security approaches [*some ideas for strategizing [can be found here](https://threatpost.com/cybersecurity-strategy-ransomware/169397/) — Ed.*], and understand that early detection and prompt remediation of any breach – no matter how small – is a far more economical approach than the alternative.


***[Nate Warfield](https://threatpost.com/author/natewarfield/) is CTO at Prevailion and a former Microsoft researcher.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[ransomware]] [[Ransomware]] [[U.S.]] [[it’s]] [[2FA]] [[infosec]] [[phishing]] [[However,]] [[tools,]] [[isn’t]] [[ThreatPost]]
