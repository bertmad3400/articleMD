# Fake Zoom App Dropped by New APT ‘LuminousMoth’
### First comes spear-phishing, next download of malicious DLLs that spread to removable USBs, dropping  Cobalt Strike Beacon, and then, sometimes, a fake Zoom app. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167822)
+ Date: July 15, 2021  11:49 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/15113710/moths-to-a-lightbulb-scaled-e1626363452342.jpeg)
Researchers have spotted a weird one: A newly identified threat actor linked to China that’s first mass-attacking, but then cherry-picking, just a few targets to hit with malware and data exfiltration.


Kaspersky researchers said in a Wednesday [writeup](https://securelist.com/apt-luminousmoth/103332/) that they’ve named the advanced threat actor (APT) LuminousMoth.


The campaign, going back to at least last October and targeting first Myanmar and now mostly the Philippines, is both large-scale and highly active.



That’s not uncommon. What is atypical about the LuminousMoth campaign is that it’s not only showy, it’s also targeted with “almost surgical precision,” they said.



> “It’s not often we observe a large-scale attack conducted by actors fitting this profile, usually due to such attacks being noisy, and thus putting the underlying operation at risk of being compromised by security products or researchers.” —Kaspersky researchers
> 
> 


The noise of a high-volume attack is a red flag for researchers. Of course, that’s a downside for hackers, given that it blows their cover. The analysts suggested one possible rationale for the splashiness: It could have to do with how LuminousMoth spreads. Namely, it copies itself to removable USB drives.


“It is likely that the high rate of infections is due to the nature of the LuminousMoth attack and its spreading mechanism, as the malware propagates by copying itself to removable drives connected to the system,” according to the writeup. Then again, the higher hit rate in the Philippines could boil down to another, undetected infection vector being used solely in the Philippines, or it could simply be that the attackers are more keenly interested in going after targets there.


Mustang Panda Rides Again
-------------------------


The LuminousMoth actors are using a unique set of tools and malware propagation methods, but their network infrastructure shares parts with another notorious Chinese hacking group named [Mustang Panda](https://threatpost.com/ta416-apt-plugx-malware-variant/161505/), a.k.a. HoneyMyte, TA416 or RedDelta.


There are also similarities in the tactics, techniques and procedures (TTPs) used by the two APTs: Namely, the deployment of the [Cobalt Strike beacon as a payload](https://threatpost.com/cobalt-strike-cybercrooks/167368/), as was also noted [by ESET](https://twitter.com/ESETresearch/status/1400165767488970764) last month. For its part, [Avast](https://twitter.com/AvastThreatLabs/status/1404864965584977922) last month attributed a supply-chain attack against the Myanmar president’s office website to Mustang Panda, showing that Mustang Panda was focusing on the same region as LuminousMoth.


“The proximity in time and common occurrence in Myanmar of both campaigns could suggest that various TTPs of HoneyMyte may have been borrowed for the activity of LuminousMoth,” Kaspersky analysts surmised.


They noted that the two APTs also share the TTPs of using DLL side-loading, as well as both using forms of stealers going after Chrome user-authentication cookies.


Targeted Regions
----------------


Luminous Moth was first going after important organizations in Myanmar, where researchers came across about 100 victims. The campaign ramped up in the Philippines, where they found nearly 1,400 targeted victims.


The true targets were only a subset of that. They represented a selection of high-profile government entities within the two targeted countries and abroad: Two such were Myanmar’s Ministry of Transport and Communications and the country’s Development Assistance Coordination Unit of the Foreign Economic Relations Department. Those were two of the names researchers found on archives inside two malicious DLL libraries.


Boobytrapped USBs Spread Fake Zoom
----------------------------------


LuminousMoth has a few ways to break in.


First, the campaign sends a spear-phishing email to the victim. The email contains a Dropbox download link that fetches a RAR archive. That’s where a pair of malicious DLLs can be found, masquerading as a .DOCX file. After that initial infection, the second vector kicks in, with the DLLs being sideloaded by two executables to spread to removable devices and also download a copy of Cobalt Strike.


In some cases in the Myanmar attacks, the initial infection was followed by deployment of a signed, fake version of the popular Zoom app. That fake Zoom app was actually malware that enabled the attackers to exfiltrate files from compromised systems. The valid certificate is owned by Founder Technology, a subsidiary of Peking University’s Founder Group, located in Shanghai.


It’s unclear whether the “sheer volume” of the attacks is due to the malware replicating through removable devices or whether it’s caused by something else, such as being spread on [watering-hole websites](https://threatpost.com/watering-holes-asian-ethnic-flash-update-decoy/154323/) or via a [supply-chain attack](https://threatpost.com/kaseya-patches-zero-days-revil-attacks/167670/), the researchers said.


What is clear: LuminousMoth is a new campaign coming from a Chinese-speaking actor that echoes Mustang Panda/HoneyMyte in that it spreads in large-scale attacks, but in actuality only targets a few of them. The newcomer bears monitoring, analysts said, given that it could just be Mustang Panda trying on new clothes, trying to rub out its tracks by re-tooling and coming up with new, unknown malware implants.


“This allows them to obscure any ties to their former activities and blur their attribution to known groups,” Kaspersky researchers concluded.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[LuminousMoth]] [[malware]] [[Myanmar]] [[Kaspersky]] [[large-scale]] [[HoneyMyte]] [[TTPs]] [[ThreatPost]]
