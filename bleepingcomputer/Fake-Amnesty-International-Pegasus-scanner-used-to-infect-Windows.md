# Fake Amnesty International Pegasus scanner used to infect Windows
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/fake-amnesty-international-pegasus-scanner-used-to-infect-windows/)
+ Date: September 30, 2021
+ Author: Ionut Ilascu


## Article:
![Fake Amnesty International Pegasus scanner used to infect Windows](https://www.bleepstatic.com/content/hl-images/2021/09/30/Malware_code.jpg)


Threat actors are trying to capitalize on the recent revelations on Pegasus spyware from Amnesty International to drop a less-known remote access tool called Sarwent.


The malware looks and acts the part of a legitimate antivirus solution specially created to scan the system for traces of Pegasus traces and to remove them.


### Antivirus look with a RAT's bite


Sarwent-based attacks have been running since at least the beginning of the year, in January, and targeted a variety of victim profiles in several countries.


The lure used in past campaigns is not clear at the moment but researchers at Cisco Talos spotted a new attack recently where Sarwent was delivered through a fake Amnesty International website advertising Anti-Pegasus AV.


The threat actor made an effort to make the malware look like a legitimate antivirus by created an appropriate graphical user interface.


![Sarwent RAT impersonates legit antivirus software](https://www.bleepstatic.com/images/news/u/1100723/Malware/SarwentRAT_FakeAmnesty_avGUI.png)


Choosing this disguise indicates that the actor is trying to trick users concerned about Pegasus spyware infecting their devices.


It is unclear how the actor lures visitors to the fake Amnesty International website but an analysis of the domains in this campaign “shows that the initial domains are being accessed worldwide,” although there is no indication of a large-scale campaign.


“Looking at the C2 [command and control] domains' volume, we can see a much narrower distribution country wise, with an even lower volume,” the researchers note in a [report](https://blog.talosintelligence.com/2021/09/fakeantipegasusamnesty.html) Today.


Based on data from the administration panel of a Sarwent command and control (C2) server active during the investigation, the malware reached mostly users in the U.K.


![Sarwent RAT victims](https://www.bleepstatic.com/images/news/u/1100723/Malware/SarwentRAT_Vics.png)


The researchers assess with high confidence that a Russian-speaking individual is responsible for the recent Sarwent attacks. They also found a similar backend being used since 2014, suggesting either that the malware is much older than initially thought or that a different actor used it before.


Sarwent is written in Delphi and it is not a frequent encounter in the wild. It features functions typically seen in a remote access tool (RAT), giving its operator access to the infected machine.


It allows direct access to the machine by activating the remote desktop protocol (RDP) or via the Virtual Network Computing (VNC) system. However, other methods exist through its shell and PowerShell execution capabilities.


Cisco Talos researchers believe that the graphical user interface disguising Sarwent into an antivirus solution indicates that the threat actor behind it has access to the malware source code.



“This level of familiarity also supports our earlier finding that the actor had been using the Sarwent malware since as early as 2014. This access is especially interesting given that we were unable to find anyone selling access or builders for this malware” - Cisco Talos



Apart from creating fake copies for the Amnesty International website, Sarwent’s operator also registered the following domains to impersonate the organization:


* amnestyinternationalantipegasus[.]com
* amnestyvspegasus[.]com
* antipegasusamnesty[.]com


Based on the evidence gathered, the researchers are unable to categorize the Sarwent threat actor. On the surface, they appear to be someone looking for easy money


However, some of the findings seem to suggest a more advanced adversary that does not have a financial motivation. Among the clues supporting this theory are the low number of victims and the customization level in the campaign.


Another hint refers to domain registration details (name, email addresses, postal addresses) that appear to point to the operator of the malware. Making this information available may be intentional, in an attempt to confuse investigators.




#### Tags:
[[Sarwent]] [[malware]] [[Talos]] [[Bleeping Computer]]
