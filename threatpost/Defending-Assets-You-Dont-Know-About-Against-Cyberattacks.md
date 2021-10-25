# Defending Assets You Don’t Know About Against Cyberattacks
### No security defense is perfect, and shadow IT means no company can inventory every single asset that it has. David “moose” Wolpoff, CTO at Randori, discusses strategies for core asset protection given this reality.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175730)
+ Date: October 25, 2021  5:41 pm
+ Author: David “moose” Wolpoff


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/25171347/hidden-image-e1635196458449.jpg)
Back in the 90s, we all used to build massive firewalls around our systems and spent our day-to-day resources looking for holes to patch. In theory, an impenetrable wall around everything you own is a great idea, because it protects even the things you’ve forgotten about.


However, if a wall is your only defense, it needs to be 100 percent perfect, 100 percent of the time. And if you’ve ever owned a house, you know that all walls form cracks over time. Not to mention, today’s corporate perimeter involves the cloud and mobile and remote assets too, and there could be hidden assets you’re not aware of.


Perfection must not be a prerequisite for good cybersecurity. I’d argue, you don’t need to know about everything you own to protect it. Assets can be grouped and categorized such that the security procedure accounts for perimeter and visibility weaknesses.


Think about all the ways you build security controls that affect whole groups of things:


We have all sorts of defenses that work even in the presence of unknowns or mistakes.


**Map Your Internal Paths**
---------------------------


Your system is massively complex. So if I think like an attacker, attempting to understand the entirety of an [attack surface](https://www.randori.com/solutions/asm/) is a non-starter. [I don’t need to know all your assets](https://www.randori.com/blog/using-attack-surface-management-to-impress-the-brass-upstairs/) or everything about your security strategy. I have to think in terms of what’s the most tempting target — the path to success — as an entry point to crack an attack surface.


This is how you should think about protecting your system: Find the paths that exist between your attack surface and your sensitive assets, and snuff them out. If the paths get you to a critical function, bottleneck your opponent there and bury them in fail-safes and alerts. This way, when attackers do take advantage of that path, you will know long before they are able to exfiltrate data.


There is no magical formula to categorize your assets and how you protect them. There are infinite ways you could categorize them, and the right one depends entirely on the context of your organization. At Randori, we try to train ourselves and others to group assets into functional clusters: We look at which ones represent a “path” for an attacker, and then determine how many policies we have to create around them to ensure we feel good about “coverage.”


**How Do I Categorize Assets for Cyber-Defense?**
-------------------------------------------------


One way to slice it is by categorizing assets based on what needs to talk to the internet and what doesn’t. Chances are, the vast majority of your internet-facing assets are components of software-as-a-service (SaaS) apps or appliances that you don’t use, or don’t need to use. If you have an appliance that provides file transfer and VPN and you only use the VPN, turn off the file-transfer feature.


You can shut these features down and forget about them. If an employee comes to you and says they need it to do their job, simply turn them back on (default-deny, anybody?).


Then there is the next category: Things which are visible from the outside and necessary to company operations, like your corporate website or remote-access protocol. These are no doubt some of the most prominent pathways between your attack surface and your crown jewels. They are meant to be — how else would your employees access anything? These assets must be secured with a lot of monitoring and alerting, and there should be a DMZ (demilitarized zone) around them.


**Know What Matters and Forget the Rest**
-----------------------------------------


You’ve probably already established DMZs  in your network— where you put the assets that need to be internet-accessible and closely monitored. Your corporate website lives on a server by itself totally isolated from your core business. Every time you’ve also got a [VPN or some remote-access tool](https://hexadecimoose.medium.com/why-your-vpn-is-an-attackers-next-target-6103fb1e4045?source=user_profile---------0----------------------------), it goes in your DMZ, where you’ve got heavy-handed segmentation and monitoring.


Anything in the DMZ gets intentionally implemented with least-privilege, and by being in the DMZ (or even deeper in your network), any service inherits segmentation, and some visibility or monitoring. There are some small ways in, but I stress these are small because you need to have thorough monitoring on them. Each layer deeper into your environment should inherit more defenses, and require more failures for a breach to occur.


Segmenting and hardening reduces your opponent’s options. Limiting the normal activity between assets where possible (such as between the DMZ and your core network) creates opportunities for detection.


The security team is the advisor here, and creates policies to try to inherit defenses. At Randori, when developers are experimenting with code, I want them to “code securely,” but I also want the unfinished or prototype work to inherit some defenses, even if mistakes are made. So we manage some simple additional layers: Everything gets deployed without direct internet access. Developers can do their work, but even if they accidentally disable authentication in the app they’re building, the application is still “defended” by a layer of single sign-on (SSO).


**There Will Always Be Unknowns & Assets You Can’t See**
--------------------------------------------------------


If you get a Qualys scan and it reports back 3 million vulnerabilities on your attack surface, [you can’t do much with that because you can’t ship out 3 million patches.](https://www.randori.com/blog/vulnerability-management-is-giving-you-a-vuln-overload-enter-asm/) But if you know which vulnerabilities are in segments that matter and have inherited insufficient protections, then you can prioritize which to address.


If the application server that is allowed to transit your DMZ is unpatched, you’re going to want to fix that first. Got an internal application server that’s only accessible to limited internal users? Maybe ignore that one for now. If there’s a place to panic about unknown vulnerabilities, it’s most likely the application server transiting your DMZ and not your internal one.


We all also know that shadow IT is a massive problem (something like 40 percent of IT spend), and ideally you’d use an attack-surface management platform to help you find surprises in your network. But when you’re planning your security posture, you need to assume that this shadow problem will continue to exist, and make sure that these one or two surprises don’t become an Associated Press headline.


Someone will always “plug something into the internet.” If your DMZ requires network access control (NAC), denies access to the internal network by default and generates alerts to your managed security service provider (MSSP) or IT team, then “plugging something into the internet” requires a lot more than one failure to create meaningful risk for a breach.


Bottom line: You have to design your security systems with the assumption that an attacker can break any asset and own its controls, its privileges and its functionality. You can defend an asset, even when you don’t know about it, by practicing defense-in-depth — knowing what matters, and implementing many disparate controls with no single point of failure.


***[David “moose” Wolpoff](https://threatpost.com/author/davidwolpoff/) is CTO at Randori.***


***Enjoy additional insights from Threatpost’s InfoSec Insider community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[DMZ]] [[don’t]] [[you’ve]] [[them.]] [[you’re]] [[ThreatPost]]
