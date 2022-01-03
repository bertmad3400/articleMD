# Apple iOS vulnerable to HomeKit 'doorLock' denial of service bug
### A novel persistent denial of service vulnerability named 'doorLock' was discovered in Apple HomeKit, affecting iOS 14.7 through 15.2.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/apple-ios-vulnerable-to-homekit-doorlock-denial-of-service-bug/
+ Date: 2022-01-03T10:39:58-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/02/10/Apple_red.jpg)

![Apple logo in red background](https://www.bleepstatic.com/content/hl-images/2021/02/10/Apple_red.jpg)


A novel persistent denial of service vulnerability named 'doorLock' was discovered in Apple HomeKit, affecting iOS 14.7 through 15.2.


Apple HomeKit is a software framework that lets iPhone and iPad users control smart home appliances from their devices.


According to Trevor Spinolas, the security researcher who publicly disclosed the details, Apple has known about the flaw since August 10, 2021. Yet, despite the repeated promises to fix it, the researcher says Apple has continually pushed the security update further, and it remains unresolved.



> 
> I believe this bug is being handled inappropriately as it poses a serious risk to users and many months have passed without a comprehensive fix. The public should be aware of this vulnerability and how to prevent it from being exploited, rather than being kept in the dark. - Spinolas.
> 
> 
> 


Forcing a reset
---------------


To trigger 'doorLock,' an attacker would change the name of a HomeKit device to a string larger than 500,000 characters.


To demonstate the doorLock bug, Spinolas has released a proof-of-concept exploit in the form of an iOS app that has access to Home data and can change HomeKit device names.


Even if the target user doesn’t have any Home devices added on HomeKit, there’s still an attack pathway by forging and accepting an invitation to add one.



Upon attempting to load the large string, a device running a vulnerable iOS version will be thrown into a denial of service (DoS) state, with a forced reset being the only way out of it. However, resetting the device will cause all stored data to be removed and only recoverable if you have a backup.


To make matters worse, once the device reboots and the user signs back into the iCloud account linked to the HomeKit device, the bug will be re-triggered.



"In iOS 15.1 (or possibly 15.0), a limit on the length of the name an app or the user can set was introduced," explains Spinolas in his [blog post](https://trevorspiniolas.com/doorlock/doorlock.html).


"The introduction of a local size limit on the renaming of HomeKit devices was a minor mitigation that ultimately fails to solve the core issue, which is the way that iOS handles the names of HomeKit devices."


"If an attacker were to exploit this vulnerability, they would be much more likely to use Home invitations rather than an application anyways, since invitations would not require the user to actually own a HomeKit device."


The impact of this attack ranges from having an unusable device that reboots indefinitely to not being able to take a backup of your data from iCloud as signing back to the online backup services re-triggers the flaw.


As the researcher explains, this attack could be used as a ransomware vector, locking iOS devices into an unusable state and demanding a ransom payment to set the HomeKit device back to a safe string length.


How to protect yourself
-----------------------


It is essential to underline that the bug can only be exploited by someone with access to your 'Home' or via manually accepting an invitation to one.


With that said, there’s no reliable method of regaining access to local data after 'doorLock' has been triggered, so users should focus all efforts on prevention.


For this, beware of suspicious invitation messages from email addresses that resemble Apple services or HomeKit products.


If the damage has already been done, follow these three steps to restore your data from the iCloud:


1. Restore the affected device from Recovery or DFU Mode
2. Set up the device as usual, but do NOT sign back into the iCloud account
3. After setup is finished, sign in to iCloud from settings. Immediately after doing so, disable the switch labeled “Home.” The device and iCloud should now function again without access to Home data.

According to the researcher, Apple’s latest estimate for fixing the bug is for "early 2022," which will be done through an upcoming security update.


We have reached out to Apple to request a comment on the above, and we will update this story as soon as we hear back from them.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Homekit]] [[Icloud]] [[Spinolas]] [[Bleeping Computer]]

