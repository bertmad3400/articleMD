# Chinese APT LuminousMoth abuses Zoom brand to target gov't agencies
### Fake Zoom apps are being spread to conduct cyber surveillance.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/chinese-apt-luminousmoth-abuses-zoom-brand-to-target-govt-agencies/)
+ Date: July 16, 2021 -- 10:09 GMT (11:09 BST)
+ Author: Charlie Osborne


## Article:
Unknown

A Chinese advanced persistent threat (APT) group is spreading fake Zoom software to spy on targets in South East Asia. 


The group, dubbed [LuminousMoth by Kaspersky](https://securelist.com/apt-luminousmoth/103332/), is focused on cyberespionage and the theft of information from high-profile targets. 

Dating back to at least October 2020, roughly 100 victims have been detected in Myanmar, and close to 1,400 have been recorded in the Philippines. However, these infection rates may not tell the whole story, as the researchers believe that only a small subset of these numbers was of interest to the APT and were exploited further.  

LuminousMoth's true targets, in particular, are government agencies in both of these countries and abroad. 

According to the researchers, the preliminary rate of infection may be due to LuminousMoth's initial attack vector and spreading mechanisms, deemed "noisy" and unusual for an APT to adopt.  

The APT begins by sending spear phishing emails that contain Dropbox download links to a .RAR archive, named with political or COVID-19 themes. This file contains two malicious .DLL files which are able to then pull and deploy malicious executables on an infected system.  

Once this stage of infection has been completed, LuminousMoth will download a Cobalt Strike beacon and side-load two malicious libraries designed to establish persistence and to copy the malware onto any removable storage drives connected to a victim system. 






In cases noted by Kaspersky, the threat actors have then deployed a fake Zoom app, software that has become a lifeline -- alongside Microsoft Teams, and others -- for many businesses forced to go remote during the COVID-19 pandemic.  

The software, signed by an organization in Shanghai, is actually used to exfiltrate files of interest to LuminousMoth. Any file found with pre-defined extensions is copied and transferred to a command-and-control (C2) server.   

LuminousMoth will also look for cookies and credentials, including those used for Gmail accounts.  

"During our test, we set up a Gmail account and were able to duplicate our Gmail session by using the stolen cookies," Kaspersky says. "We can therefore conclude this post-exploitation tool is dedicated to hijacking and impersonating the Gmail sessions of the targets." 

The APT's activities also appear to overlap with [HoneyMyte](https://www.kaspersky.com/about/press-releases/2019_the-garden-of-forking-paths-sophisticated-apts-diversify-toolsets)/Mustang Panda, another Chinese-speaking group, linked to an attack against the office of Myanmar's president ([1](https://twitter.com/ESETresearch/status/1400165767488970764),[2](https://twitter.com/AvastThreatLabs/status/1404864965584977922)).  

LuminousMoth and HoneyMyte have adopted similar tactics during campaigns including C2 overlaps, .DLL side-loading, the deployment of Cobalt Strike beacons, and similar cookie-stealing functionality. 

"Both groups, whether related or not, have conducted activity of the same nature -- large-scale attacks that affect a wide perimeter of targets with the aim of hitting a few that are of interest," the researchers say.  

###  Previous and related coverage

* [Transparent Tribe APT targets government, military by infecting USB devices](https://www.zdnet.com/article/transparent-tribe-hacking-group-spreads-malware-by-infecting-usb-devices/)  

* [SideCopy cybercriminals use new custom Trojans in attacks against India's military](https://www.zdnet.com/article/sidecopy-cybercriminals-use-custom-trojans-in-india-attacks/)  

* [This new hacking group has a nasty surprise for African, Middle East diplomats](https://www.zdnet.com/article/this-new-hacking-group-has-a-nasty-surprise-for-african-middle-east-diplomats/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[LuminousMoth]] [[Gmail]] [[Kaspersky]] [[--]] [[ZDNet]]
