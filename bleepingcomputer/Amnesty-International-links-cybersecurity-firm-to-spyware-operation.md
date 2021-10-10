# Amnesty International links cybersecurity firm to spyware operation
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/amnesty-international-links-cybersecurity-firm-to-spyware-operation/)
+ Date: October 10, 2021
+ Author: Bill Toulas


## Article:
![Hacker](https://www.bleepstatic.com/content/hl-images/2020/07/09/Stalkerware_spyware_surveillance.jpg?rand=627524029)


A report by Amnesty International links an Indian cybersecurity company to an Android spyware program used to target prominent activists. 


The investigation comes from Amnesty International's team, who confirmed a case of espionage against a Togolese activist and also observed signs of spyware deployment across several key Asian regions. 


A link to an Indian cybersecurity firm
--------------------------------------


According to [Amnesty International](http://www.amnesty.org/en/latest/news/2021/10/togo-activist-targeted-with-spyware-by-notorious-hacker-group/), the Android spyware has been linked to Indian cybersecurity company Innefu Labs after an IP address belonging to the company was repeatedly used for the distribution of the spyware payload. 


However, the actual deployment could be the work of the 'Donot Team' (APT-C-35), a collective of Indian hackers who have been targeting governments in Southeast Asia since at least 2018. 


Amnesty notes that it's possible Innefu is not aware of how its customers or other third parties are using its tools. However, an external audit could reveal everything now that full technical details have come to light. 


In a written letter to Amnesty International, Innefu Labs denies any involvement with the Donot Team and the targeting of activists.



> 
> "At the outset we firmly deny the existence of any link whatsoever between Innefu Labs and the spyware tools associated with the ‘Donot Team’ group and the attacks against a Human Rights Defender in Togo. As has already been stated by us in our previous letter, we are not aware of any ‘Donot Team’ or have any relationship with them.
> 
> 
> In your letter dated 20.09.2021, references have been made to a Xiaomi Redmi 5A phone, which has allegedly accessed the IP address of Innefu Labs, and also of some other private VPN server to access the Ukrainian hosting company called Deltahost. We believe this phone does not belong to any person associated with Innefu Labs. Merely because our IP address has been accessed using this phone does not ipso facto conclude Innefu Labs’ involvement in any of the alleged activities" - Innefu Labs.
> 
> 
> 


BleepingComputer has contacted Innefu Labs multiple times since yesterday morning but did not receive a response.


Targeting Togo activists
------------------------


The attack on the activists began with an unsolicited message on WhatsApp, suggesting the installation of a supposedly secure chat app called ‘ChatLite.’


Having failed there, the attackers sent an email from a Gmail account, carrying a laced MS Word file that exploits an old vulnerability to drop the spyware. 



![Actors sending unsolicited messages to the target.](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/chat.jpg)**Actors sending unsolicited messages to the target**  

Source: Amnesty International
In the ChatLite case, the spyware was a custom-developed Android app that allowed the attacker to collect sensitive data from the device and fetch additional malware tools.



![The ChatLite app icon.](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/chat%20lite.jpg)**The ChatLite app icon**  

Source: Amnesty International
For the spyware distributed via malicious Word document, it had the following capabilities: 


* Record keystrokes
* Take screenshots regularly
* Steal files from local and removable storage
* Download additional spyware modules


By analyzing the Android spyware sample, Amnesty's investigators found several similarities to "Kashmir\_Voice\_v4.8.apk" and "SafeShareV67.apk", two malware tools linked to past Donot Team operations.


The threat actor's opsec mistake allowed the investigators to discover a  "testing" server in the USA where the threat actors were storing screenshots and keylogging data from compromised Android phones.



![Files of screen captures from compromised devices](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Files of screen captures from compromised devices**  

Source: Amnesty International
This is where Amnesty first saw the Innefu Labs IP address, as otherwise, the real source was hiding behind a VPN.


Togo hiring foreign hackers?
----------------------------


This is the first time that the Donot Team was spotted targeting entities in African countries, and it could be a clue that the group is offering 'hacker for hire' services to governments. 


Freedom House gives Togo a [‘Partly Free’ rating](https://freedomhouse.org/country/togo/freedom-world/2021), with the ruling of the country being in the hands of the Gnassingbé family since 1963. The main opposition candidate, Agbéyomé Kodjo, was arrested in April 2020. 


Unfortunately, human rights violations, targeting activists and civil liberties advocates, and crippling political pluralism are common in Togo, and according to Amnesty’s report, things are only getting worse in the African country.




#### Tags:
[[Innefu]] [[spyware]] [[Android]] [[IP]] [[cybersecurity]] [[Donot]] [[Source:]] [[Bleeping Computer]]
