# Fears surrounding Pegasus spyware prompt new Trojan campaign
### Criminals hope that the lure of a promise to protect you from spyware will make you click that link.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/fears-surrounding-pegasus-spyware-prompt-new-trojan-campaign/)
+ Date: September 30, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A recent investigation into how Pegasus spyware is being used to monitor civil rights agencies, journalists, and government figures worldwide is being abused in a new wave of cyberattacks. 


Pegasus is a surveillance system offered by the NSO Group. While advertised as software for fighting crime and terrorism, a [probe into the spyware](https://www.zdnet.com/article/nso-groups-pegasus-spyware-used-against-journalists-political-activists-worldwide-report/) led to allegations that it is [being used against](https://www.zdnet.com/article/whatsapp-chief-says-government-officials-us-allies-targeted-by-nso-groups-pegasus-spyware/) innocents, including human rights activists, political activists, lawyers, journalists, and politicians worldwide.  

Israel-based NSO Group denied the findings of the investigation, conducted by Amnesty International, Forbidden Stories, and numerous media outlets.  

Apple has since patched a [zero-day vulnerability](https://www.zdnet.com/article/apple-releases-update-fixing-nso-spyware-vulnerability-affecting-macs-iphones-ipads-and-watches/) utilized by Pegasus, a discovery made together with Citizen Lab.  

Now, cybercriminals unconnected to Pegasus are attempting to capitalize on the damning report by promising individuals a way to 'protect' themselves against such surveillance -- but are secretly deploying their own brands of malware, instead.   

On Thursday, researchers from [Cisco Talos said](https://blog.talosintelligence.com/) that threat actors are masquerading as Amnesty International and have set up a fake domain designed to impersonate the organization's legitimate website. 

This points to an 'antivirus' tool, "AVPegasus," that promises to protect PCs from the spyware.  

![screenshot-2021-09-30-at-10-30-47.png]()![screenshot-2021-09-30-at-10-30-47.png](https://www.zdnet.com/a/img/resize/e553ef6d9aa51f720474d788897ac9c948137699/2021/09/30/c3451f70-e4b2-4cb0-a702-8e251d549166/screenshot-2021-09-30-at-10-30-47.png?width=1200&fit=bounds&auto=webp)
 Cisco Talos
 




However, according to Talos researchers Vitor Ventura and Arnaud Zobec, the software contains the Sarwent Remote Access Trojan (RAT).

The domains associated with the campaign are amnestyinternationalantipegasus[.]com, amnestyvspegasus[.]com, and antipegasusamnesty[.]com. 

Written in Delphi, Sarwent installs a backdoor onto machines when executed and is also able to leverage a remote desktop protocol (RDP) to connect to an attacker-controlled command-and-control (C2) server.  

The malware will attempt to exfiltrate credentials and is also able to download and execute further malicious payloads.  

The UK, US, Russia, India, Ukraine, the Czech Republic, Romania, and Colombia are the most targeted countries to date. Talos believes the cyberattacker behind this campaign is a Russian speaker who has operated other Sarwent-based attacks over 2021.  

"The campaign targets people who might be concerned that they are targeted by the Pegasus spyware," Talos says. "This targeting raises issues of possible state involvement, but there is insufficient information available to Talos to make any determination there. It is possible that this is simply a financially motivated actor looking to leverage headlines to gain new access." 

###  Previous and related coverage

* [NSO Group's Pegasus spyware used against journalists, political activists worldwide](https://www.zdnet.com/article/nso-groups-pegasus-spyware-used-against-journalists-political-activists-worldwide-report/)  

* [WhatsApp chief says government officials, US allies targeted by Pegasus spyware](https://www.zdnet.com/article/whatsapp-chief-says-government-officials-us-allies-targeted-by-nso-groups-pegasus-spyware/)  

* [FBI launches investigation into Pegasus spyware vendor over US citizen hacks](https://www.zdnet.com/article/fbi-launches-investigation-into-pegasus-spyware-vendor-over-us-intelligence-gathering-hacks/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Talos]] [[spyware]] [[journalists,]] [[NSO]] [[ZDNet]]
