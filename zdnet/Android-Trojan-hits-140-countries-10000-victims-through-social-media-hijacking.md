# Android Trojan hits 140 countries, 10,000 victims through social media hijacking
### Security company Zimperium uncovered a new malware campaign spread through social media hijacking, third-party app stores, and sideloaded applications.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/android-trojan-hits-140-countries-10000-victims-through-social-media-hijacking/)
+ Date: August 9, 2021 -- 23:12 GMT (00:12 BST)
+ Author: Jonathan Greig


## Article:
Unknown

A new Android Trojan has been identified by cybersecurity firm Zimperium, which [released a report](https://blog.zimperium.com/flytrap-android-malware-compromises-thousands-of-facebook-accounts/) on Monday explaining how the malware has been able to hit more than 10,000 victims in 144 countries. 

The trojan -- named FlyTrap by Zimperium researchers -- has been able to spread through "social media hijacking, third-party app stores, and sideloaded applications" since March. 

Zimperium's zLabs mobile threat research teams first identified the malware and figured out that it uses social engineering tricks to compromise Facebook accounts. The malware hijacks social media accounts by infecting Android devices, allowing attackers to collect information from victims like Facebook ID, location, email address and IP address as well as cookies and tokens tied to your Facebook account.

"These hijacked Facebook sessions can be used to spread the malware by abusing the victim's social credibility through personal messaging with links to the Trojan, as well as propagating propaganda or disinformation campaigns using the victim's geolocation details," the Zimperium researchers wrote. 

"These social engineering techniques are highly effective in the digitally connected world and are used often by cybercriminals to spread malware from one victim to another. The threat actors made use of several themes that users would find appealing such as free Netflix coupon codes, Google AdWords coupon codes, and voting for the best football (soccer) team or player."

The researchers attributed the malware to groups based in Vietnam and said they are able to distribute it using Google Play and other app stores. Google was sent a report about the malware, verified it and removed all of the applications from the store. 

But the report notes that three of the applications are still available on "third-party, unsecured app repositories."






Once victims are convinced to download the app through deceptive designs, the app urges users to engage and eventually asks for people to enter their Facebook account information in order to vote on something or collect coupon codes. Once everything is entered, the app takes victims to a screen that says the coupon has already expired. 

The researchers explained that the malware uses a technique called "JavaScript injection" which allows the app to open legitimate URLs inside a "WebView configured with the ability to inject JavaScript code." The app then extracts information like cookies, user account details, location, and IP address by injecting malicious JS code.

Zimperium suggests Android users find ways to check if any applications on their device have FlyTrap and noted that these breached accounts could be used as a botnet for other purposes like boosting the popularity of certain pages or sites. 

"FlyTrap is just one example of the ongoing, active threats against mobile devices aimed at stealing credentials. Mobile endpoints are often treasure troves of unprotected login information to social media accounts, banking applications, enterprise tools, and more," Zimperium researchers said. 

"The tools and techniques used by FlyTrap are not novel but are effective due to the lack of advanced mobile endpoint security on these devices. It would not take much for a malicious party to take FlyTrap or any other Trojan and modify it to target even more critical information."

Setu Kulkarni, vice president at NTT Application Security, said FlyTrap was a "nifty combination" of a handful of vulnerabilities and took advantage of the abundance of meta-data open to access, like location, as well as the implicit trust that can be gained by clever yet dubious associations with companies like Google, Netflix and others. 

"This is not even the most concerning bit -- the concerning bit is the network effect this type of trojan can generate by spreading from one user to many. Moreover, as the summary of Zimperium's findings state -- this trojan could be evolved to exfiltrate significantly more critical information like banking credentials," Kulkarni said. 

"The what-if scenarios don't end there unfortunately. What-if this type of trojan is now offered as-a-service or what-if this transforms quickly into ransomware targeting 100s of thousands of users. The bottom line does not change. It all begins with a user who is enticed to click a link. This begs the question – shouldn't Google and Apple be doing more to address this for their entire customer base?"





#### Tags:
[[malware]] [[Zimperium]] [[Facebook]] [[Google]] [[Android]] [[location,]] [[ZDNet]]
