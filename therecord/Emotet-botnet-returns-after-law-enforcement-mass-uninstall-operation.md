# Emotet botnet returns after law enforcement mass-uninstall operation
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/emotet-botnet-returns-after-law-enforcement-mass-uninstall-operation/)
+ Date: November 15, 2021
+ Author: Catalin Cimpanu


## Article:
![Emotet botnet returns after law enforcement mass-uninstall operation](https://therecord.media/wp-content/uploads/2021/11/Emotet.png)

**The Emotet malware botnet is back up and running once again almost ten months after an international law enforcement operation [took down its command and control servers](https://www.europol.europa.eu/newsroom/news/world%E2%80%99s-most-dangerous-malware-emotet-disrupted-through-global-action) earlier this year in January.**


The comeback is surprising because after taking over Emotet’s server infrastructure, law enforcement officials also [orchestrated a mass-uninstall](https://www.zdnet.com/article/authorities-plan-to-mass-uninstall-emotet-from-infected-hosts-on-april-25-2021/) of the malware from all infected computers on April 25, effectively wiping out the entire botnet across the internet.


Once described as the “**world’s most dangerous malware**,” Emotet worked by sending massive waves of email spam to users all over the world in order to infect them with its malware strain.


Once infected, these systems would allow the Emotet gang to download and install additional payloads. Over the past three to four years, Emotet has served as a Malware-as-a-Service infrastructure for various cybercrime groups, such as ransomware gangs and Point-of-Sale malware operators.


All of this stopped in January when the Emotet gang lost access to the servers controlling its vast network of infected devices.


### Ten months later, Emotet returns


But over the weekend, security researcher [Luca Ebach](https://cyber.wtf/2021/11/15/guess-whos-back/) said he spotted that another malware botnet named TrickBot was helping the Emotet gang get back on its feet by installing the Emotet malware on systems that had been previously infected with TrickBot.


“We used to call this **Operation ReachAround** back when Emotet was dropped by Trickbot in the past,” a spokesperson for Cryptolaemus, [a group of security researchers who tracked Emotet in the past](https://www.zdnet.com/article/meet-the-white-hat-group-fighting-emotet-the-worlds-most-dangerous-malware/), told *The Record* today.


“This is something they have done before and we knew it could be a way to come back,” Cryptolaemus told us, confirming Ebach’s findings.


The new Emotet malware versions were also spotted on the third-year anniversary of the Cryptolaemus Twitter account, but it’s unclear if the Emotet administrators have intentionally planned for this to happen. The Cryptolaemus group played a crucial role in tracking, mapping, and then helping law enforcement take down Emotet earlier this year.





A screenshot shared with *The Record* by Abuse.ch, a member of the Cryptolaemus group, shows the gap in Emotet’s dormant period between January and November 2021, while the group rolled out new command and control servers.


![Feodo-Tracker Emotet](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Feodo-Tracker-1024x552.jpg)Image: Absue.ch (provided)
Cryptolaemus said that right now, the Emotet gang is not sending out any new email spam but relying on the TrickBot gang to help them create an initial footprint of their new botnet incarnation before ramping up spam operations again.


“It doesn’t seem too large at this time, and we are not seeing active distribution yet,” the white-hat research group said.


But if Emotet’s comeback will succeed remains to be seen. It would be very hard for Emotet to reach its previous size any time in the coming months; however, the malware strain itself remains a very sophisticated and capable threat that shouldn’t be ignored.


“We urge you to *BLOCK* [these command and control servers](https://feodotracker.abuse.ch/browse/emotet/) and regularly update your block list to receive the maximum protection,” Abuse.ch [wrote on Twitter](https://twitter.com/abuse_ch/status/1460308766767915013) earlier today.





#### Tags:
[[Emotet]] [[malware]] [[Cryptolaemus]] [[botnet]] [[Emotet’s]] [[The Record]]
