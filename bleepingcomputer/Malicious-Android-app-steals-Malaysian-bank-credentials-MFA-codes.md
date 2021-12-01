# Malicious Android app steals Malaysian bank credentials, MFA codes
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/malicious-android-app-steals-malaysian-bank-credentials-mfa-codes/)
+ Date: December 1, 2021
+ Author: Bill Toulas


## Article:
![cleaner](https://www.bleepstatic.com/content/hl-images/2021/12/01/cleaning.jpg?rand=1498601066)


A fake Android app is masquerading as a housekeeping service to steal online banking credentials from the customers of eight Malaysian banks.


The app is promoted through multiple fake or cloned websites and social media accounts to promote the malicious APK, 'Cleaning Service Malaysia.'


This app was first spotted by MalwareHunterTeam last week and was subsequently analyzed by researchers at [Cyble](https://blog.cyble.com/2021/12/01/banking-trojan-targets-banking-users-in-malaysia/), who provide detailed information on the app's malicious behavior.




> 
> "cleaningservicemalaysia.apk": 7845bb247dbfad94018047afbb2f5e1d9e54752b620d995033c695d9a2d104a0 [pic.twitter.com/wx6nM2GFdX](https://t.co/wx6nM2GFdX)
> 
> 
> — MalwareHunterTeam (@malwrhunterteam) [November 25, 2021](https://twitter.com/malwrhunterteam/status/1463960912180744195?ref_src=twsrc%5Etfw)


Phishing process
----------------


Upon installing the app, users are requested to approve no less than 24 permissions, including the risky 'RECEIVE\_SMS,' which allows the app to monitor and read all SMS texts received on the phone.


This permission is abused for monitoring SMS texts to steal one-time passwords and MFA codes used in e-banking services, which are then sent to the attacker's server.



![Exfiltrating SMS content from the victim's device](https://www.bleepstatic.com/images/news/u/1220909/Security/SMS_exfiltration.png)**Exfiltrating SMS content from the victim's device.**  
*Source: Cyble*
Once launched, the malicious app will display a form asking the user to reserve a house cleaning appointment.



![Fake house cleaning reservation](https://www.bleepstatic.com/images/news/security/cleaning-service-malaysia.png)**Fake house cleaning reservation**  
*Source: Cyble*
Once the user enters their cleaning service details (name, address, phone number) on the fake app, they are prompted to select a payment method.



![Selecting the e-banking services on the app](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Selecting the payment method in the app**  
*Source: Cyble*
This step offers a selection of Malaysian banks and internet banking options, and if the victim clicks on one, they are taken to a fake login page created to mimic the appearance of the real one.


This login page is hosted on the actor’s infrastructure, but of course, the victim has no way to realize that from inside the app's interface.



![Phishing layout mimicking the real login page.](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Phishing layout mimicking the real login page.**  
*Source: Cyble*
Any banking credentials entered in this step are sent directly to the actors, who can use them along with an intercepted SMS code to access the victim’s e-banking account.


Signs of fraud
--------------


Some clear signs of fraud in the social media accounts that promote these APKs are their low follower count and the fact that they were created very recently.


Another issue is a mismatch in the provided contact details. Because most of the decoy sites picked real cleaning services to mimic, telephone numbers or email differences are a big red flag.



![Fake housekeeping site created by threat actors](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Fake housekeeping site created by threat actors**  
*Source: Cyble*
The requested permissions also indicate something is not right, as a cleaning service app does not have a legitimate reason to request access to a device's texts.


To minimize the chances of falling victim to phishing attacks of this kind, only download Android apps from the official Google Play Store.


Furthermore, always review the requested permissions carefully and do not install an app that is asking for greater privileges than it should require for its functionality.


Finally, keep your device up to date by applying the latest available security updates and using a mobile security solution from a reputable vendor.




#### Tags:
[[Cyble]] [[SMS]] [[Bleeping Computer]]
