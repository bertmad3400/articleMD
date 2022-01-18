# Beijing 2022 Winter Olympics app bursting with privacy risks
### The official app for Beijing 2022 Winter Olympics, 'My 2022,' was found to be insecure when it comes to protecting the sensitive data of its users.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/beijing-2022-winter-olympics-app-bursting-with-privacy-risks/
+ Date: 2022-01-18T09:50:46-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/18/winter-olympics.jpg)

![winter-olympics](https://www.bleepstatic.com/content/hl-images/2022/01/18/winter-olympics.jpg?rand=410169842)


The official app for Beijing 2022 Winter Olympics, 'My 2022,' was found to be insecure when it comes to protecting the sensitive data of its users.


Most importantly, the app's encryption system carries a significant flaw that enables middle-men to access documents, audio, and files in cleartext form.


'My 2022' is also subject to censorship based on a list of keywords and has an unclear privacy policy that doesn't determine who exactly receives and processes all the sensitive data users have to upload to it.


As such, it is violating Google's software policy and Apple's App Store guidelines, yet it is available in both stores. Finally, the app violates China's own laws regarding privacy protection.



![The My 2022 app that all attendees are required to install and use](https://www.bleepstatic.com/images/news/u/1220909/Android%20malware/my2022.png)**The My 2022 app that all attendees are required to install and use**  
*Source: Citizen Lab*
Requesting everything
---------------------


In a detailed report by [Citizen Lab](https://citizenlab.ca/2022/01/cross-country-exposure-analysis-my2022-olympics-app/), researchers analyzed the 'My 2022' app for potential privacy and security issues and found that the app collects the following sensitive information:


* Device identifiers and model
* Cellular service provider information
* Installed apps on the device
* WLAN status
* Real-time location
* Audio information
* Device storage access
* Location access

This data collection is disclosed in the privacy policy and is required for COVID-19 protection controls, translation services, Weibo integration, and tourism recommendations and navigation.


However, using 'My 2022' isn’t optional. All athletes, members of the press, and the audience have to install the app and add their personal information to it.


For domestic users, 'My 2022' collects names, national identification numbers, phone numbers, email addresses, profile pictures, and employment information and shares it with the Beijing Organizing Committee for the 2022 Olympics.


For foreigners, 'My 2022' collects complete passport information, daily health status, COVID-19 vaccination status, demographic data, and which organization they work for.


Insecure communications
-----------------------


Even more concerning are flaws in the app's SSL-based encryption that allows rogue connections due to certification validation issues.


According to the findings of Citizen Lab, an attacker may spoof at least five servers and intercept data sent from the app, tricking it into seeing a malicious host as trusted.


As such, all of the sensitive data described in the previous section can be collected by third parties that are out of the Chinese government's control.


In addition to the server spoofing problem, the analysts found transmitted data is not always encrypted, so some transmissions containing sensitive metadata could be intercepted and read in plaintext form via simple network packet eavesdropping.


Disclosure and response
-----------------------


The severe privacy and security risks discovered by Citizen Labs were reported to the Beijing Organizing Committee for the 2022 Olympic and Paralympic Winter Games on December 3, 2021.


As of today (January 18, 2022), nobody has responded, so the researchers publicly disclosed the flaws.


Yesterday, the app developers released the 'My 2022' version 2.0.5, and upon a new round of analysis, it was determined that the reported issues still remain unresolved.


On the question of whether China placed the flaws in the app intentionally, Citizen Labs finds that highly unlikely, considering that the recipient of the data is the Chinese state, and there's no incentive to create additional backdoors for anyone else.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=Beijing]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Beijing]] [[Bleeping Computer]]

