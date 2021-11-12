# Mac Zero Day Targets Apple Devices in Hong Kong
### Google researchers have detailed a widespread watering-hole attack that installed a backdoor on Apple devices that visited Hong Kong-based media and pro-democracy sites. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176300)
+ Date: November 12, 2021  1:05 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/06/30130453/watering-hole2.jpg)
Since at least late August, attackers have been using flaws in macOS and iOS – including in-the-wild use of what was then a zero-day flaw – to install a backdoor on the Apple devices of users who visited Hong Kong-based media and pro-democracy sites.


This isn’t a finely targeted campaign, but it’s a sophisticated one. The [watering-hole attack](https://threatpost.com/watering-hole-attack-claims-us-department-of-labor-website/100081/) indiscriminately slipped malware onto any iOS or macOS device unfortunate enough to have stumbled across the infected sites, according to a [report](https://blog.google/threat-analysis-group/analyzing-watering-hole-campaign-using-macos-exploits) published on Thursday by Google’s Threat Analysis Group (TAG).


In other words, the threat actors threaded malware into the legitimate websites of “a media outlet and a prominent pro-democracy labor and political group” in Hong Kong, according to TAG.


The victims’ devices were inflicted with what was then a zero day, plus another exploit that used a previously patched vulnerability for macOS that was used to install a backdoor on their computers, according to TAG’s report.


Likely the Work of State-Backed Attackers
-----------------------------------------


TAG doesn’t usually speculate about attribution, and at any rate, it said it lacked sufficient evidence in this case to definitively pin down the threat actor.


But from what the team could see, they believe the attackers are probably state-backed.


“Based on our findings, we believe this threat actor to be a well-resourced group, likely state backed, with access to their own software engineering team based on the quality of the payload code,” wrote Erye Hernandez, the Google researcher who discovered the campaign. “The payload seems to be a product of extensive software engineering.”


Hernandez was also one of the TAG researchers credited with originally finding the zero day that was used: [CVE-2021-30869](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30869), a type-confusion issue that Apple [patched in September](https://threatpost.com/apple-patches-zero-days-attack/174988/) with “improved state handling,” according to [its advisory](https://support.apple.com/en-us/HT212825) at the time. The September advisory also noted that Apple was aware of exploits in the wild.


The vulnerability was a bad one: It allows a malicious app to execute arbitrary code with kernel privileges in macOS Catalina. The payload was apparently set up to attack macOS Mojave (10.14) as well, first running a check to see which OS version was in use before springing the exploits. However, TAG said that when they visited a rigged site using Mojave, they only saw remnants of an exploit. They got the full Monty – the entire non-encrypted exploit chain – when browsing the site with Catalina.


In the case of the Hong Kong-focused campaign, exploit led to the installation of a backdoor that has an eye-watering list of surveillance capabilities, including capturing the fingerprints of victims’ devices, screen captures, file download/upload, executing terminal commands, audio recording and keylogging.


Links to China
--------------


Chinese-backed threat actors have been known to use zero days to construct elaborate, sprawling, untargeted watering-hole attacks to go after broad populations, including campaigns to target the country’s minority Muslim population of Uyghurs in Xinjiang.


Google’s Project Zero brought to light [one such campaign](https://googleprojectzero.blogspot.com/2019/08/a-very-deep-dive-into-ios-exploit.html) in 2019 after having discovered a small collection of compromised websites. The campaign, which had gone on for more than two years, similarly used vulnerabilities – two of them being zero days, including an iPhone zero day, in an attack chain that relied on a total of 14 flaws – in indiscriminate watering-hole attacks on site visitors.


As well, [MIT Technology Review reported](https://www.technologyreview.com/2021/05/06/1024621/china-apple-spy-uyghur-hacker-tianfu/) in May that actors working for Chinese intelligence used an exploit presented in 2017 at the Tianfu Cup hacking competition to target Uyghurs.


Another link to China comes from the code, which contains strings written in Chinese, according to what Apple product researcher Patrick Wardle told [Motherboard](https://www.vice.com/en/article/93bw8y/google-caught-hackers-using-a-mac-zero-day-against-hong-kong-users) after inspecting the exploit code. Also, the command and control server that it connected to was located in Hong Kong.


macOS Exploit Payload
---------------------


However the websites were compromised, they wound up serving up two iframes, for both iOS and macOS exploit chains, that served exploits from a server controlled by the attacker. TAG researchers were only able to retrieve the macOS one.


The exploit chain for macOS combined a remote-code execution (RCE) weakness in WebKit and the zero day, CVE-2021-30869.


Hernandez explained that the exploit was reminiscent of another in-the-wild vulnerability previously [analyzed](https://bugs.chromium.org/p/project-zero/issues/detail?id=2107&q=MACH_SEND_SYNC_OVERRIDE&can=1) by Project Zero’s Ian Beer. And, it turned out that the exact same exploit was [presented](https://github.com/wangtielei/Slides/blob/main/zer0con21.pdf) by cybersecurity research group Pangu Lab in a public talk at the zer0con21 conference in China in April, TAG head Shane Huntley told [Motherboard.](https://www.vice.com/en/article/93bw8y/google-caught-hackers-using-a-mac-zero-day-against-hong-kong-users) It was also presented at the Mobile Security Conference (MOSEC) in July, Hernandez wrote – in other words, just a few months before it was used against Hong Kong residents.


The macOS payload had several components that were apparently configured as modules, Hernandez explained, including a kernel module for capturing keystrokes, as well as other functions that the binaries didn’t directly access but which may have been downloaded onto victims’ machines at later stages of the attack chain.


Pegasus-Like Use of Zero Days for Surveillance
----------------------------------------------


TAG’s suggestion that this campaign looks to be coming from a state-backed attacker has historical precedence, given its sophisticated use of zero days. Campaigns using NSO Group’s military-grade surveillance tool – Pegasus – come to mind. Both the Hong Kong watering-hole attacks and NSO Group tools rely on use of zero days before vendors or the public know anything about them.


For example, in August, cybersecurity watchdog Citizen Lab saw the new zero-day FORCEDENTRY exploit successfully deployed against the [iPhones of Bahraini activists](https://threatpost.com/pegasus-spyware-uses-iphone-zero-click-imessage-zero-day/168899/) – including one living in London at the time.


***Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** [***“Password Reset: Claiming Control of Credentials to Stop Attacks,”***](https://bit.ly/3bBMX30) ***on Wed., Nov. 17 at 2 p.m. ET. Sponsored by Specops.***


[***Register NOW***](https://bit.ly/3bBMX30)***for the LIVE event!***




#### Tags:
[[macOS]] [[watering-hole]] [[Hernandez]] [[campaign,]] [[victims’]] [[day,]] [[ThreatPost]]
