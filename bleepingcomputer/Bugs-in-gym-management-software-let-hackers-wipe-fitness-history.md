# Bugs in gym management software let hackers wipe fitness history
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/bugs-in-gym-management-software-let-hackers-wipe-fitness-history/)
+ Date: August 13, 2021
+ Author: Ionut Ilascu


## Article:
![Multiple vulnerabilities in Wodify fitness management platform](https://www.bleepstatic.com/content/hl-images/2021/08/13/Wodify.jpg)


Security researchers found vulnerabilities in the Wodify fitness platform that allows an attacker to view and modify user workouts from any of the more than 5,000 gyms that use the solution worldwide.


User data (e.g. personal, workout, payments) may currently be at risk since Wodify has yet to confirm the roll out of a patch, despite being given ample time to address the security issues.



[Wodify](https://www.wodify.com/) is an all-in-one platform used by more than 5,000 gyms worldwide. Apart from offering membership management options, it can also help clients achieve their goals and better track their performance.


The platform addresses both coaches and athletes and features an automated billing system, class scheduling, allows creating custom workouts, and tracking fitness data (e.g. heart rate) in real-time.


### Changing user workout data


In a report published today, researchers at cybersecurity company Bishop Fox disclosed a set of vulnerabilities in the Wodify platform that could affect not only users’ workouts and personal information but also the financials of a gym.


Exploiting the flaws allows enumerating and modifying entries in the Wodify platform from all the gyms that use it, says Dardan Prebreza, Senior Security Consultant at Bishop Fox. Despite the need to authenticate, the issues have serious implications.



“While modifying the data, an attacker could insert malicious stored JavaScript payloads, leading to XSS. This could be leveraged to hijack a user’s session, steal a hashed password, or the user’s JWT through the Sensitive Information Disclosure vulnerability” - [Dardan Prebreza](https://labs.bishopfox.com/advisories/wodify)



By compromising administrative gym accounts, the researcher says, a financially motivated attacker could edit payment settings to steal the money from gym members.


One of the vulnerabilities refers to insufficient authorization controls, which could serve to enumerate users and change their data in the Wodify platform.


Leveraging the bug requires authentication. The researcher tested this bug successfully after getting consent from a Wodify customer to use their account.


![Enumerating user IDs in Wodify fitness management app](https://www.bleepstatic.com/images/news/u/1100723/2021/WodifyInsufCtrl_BishoFox.png)


This kind of access allowed inserting malicious code that would impact other users on the platform, “including instance or gym administrators,” via cross-site scripting (XSS) attacks.


By adding a malicious JavaScript payload in the target user’s workout comment, the researcher triggered the XSS vulnerability that could allow an attacker to change all Wodify users’ workout data, results included.


![XSS triggered in Wodify fitness management app](https://www.bleepstatic.com/images/news/u/1100723/2021/WodifyXSS_BishoFox.png)


With this kind of access, Prebreza told BleepingComputer, hackers could also wipe a user's entire workout history, something that would have a serious negative impact on an athlete's training.


Further investigation revealed four stored XSS vulnerabilities in the Wodify application. Privileges of a regular user are sufficient to plant malicious JavaScript in a workout result that would trigger an XSS bug.


A user loading that page would trigger caused the attacker’s code to run, potentially giving them administrative access to the target gym’s application.


“If an attacker gained administrative access over a specific gym in this manner, they would be able to make changes to payment settings, as well as access and update other users’ personal information” - Dardan Prebreza


Another vulnerability in the Wodify application exposes sensitive user information and allows hijacking sessions with the help of an XSS flaw.


### A patch is not confirmed


Prebreza first notified Wodify of his findings more than half a year ago and was told in April that the bugs would be fixed within 90 days.


The researcher told BleepingComputer that communication with Wodify has been very difficult and it took the company a long time to acknowledge the vulnerabilities.



“It took almost two months until they acknowledged the vulnerabilities and only by directly reaching out to their CEO via email, which then put me in touch with their new head of technology back in April."



“They were supposed to release the new/patched version in May, which then got pushed back several times. Last time they replied to us, they mentioned August 5th as the final release date,” the researcher said.


According to the disclosure timeline from Bishop Fox, Wodify was supposed to release a new version of the app on June 11 but delayed the update for August 5.


However, Bishop Fox says they have not heard from the vendor since July 13 and are unaware if a patch has been released to customers.


BleepingComputer has reached out to Wodify but has not heard back by publishing time.




#### Tags:
[[Wodify]] [[Prebreza]] [[XSS]] [[users’]] [[JavaScript]] [[user’s]] [[Bleeping Computer]]
