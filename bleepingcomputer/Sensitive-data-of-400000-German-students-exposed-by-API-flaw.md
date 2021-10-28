# Sensitive data of 400,000 German students exposed by API flaw
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/sensitive-data-of-400-000-german-students-exposed-by-api-flaw/)
+ Date: October 28, 2021
+ Author: Bill Toulas


## Article:
![school board](https://www.bleepstatic.com/content/hl-images/2020/12/01/sad-class.jpg?rand=879425660)


Approximately 400,000 users of Scoolio, a student community app widely used in Germany, had sensitive information exposed due to an API flaw in the platform.


[Lilith Wittmann](https://twitter.com/LilithWittmann), a security researcher from the IT security collective “Zerforchung” discovered the bug and immediately disclosed their findings to the Scoolio team.


A “student” business
--------------------


Scoolio is a German student community app that aims to build better time management skills, tutoring, homework planning, and group chats to network with peers. The app also allows companies to network with students to share job openings or internship opportunities.


Scoolio makes money by collecting data generated through these tools and features and then monetizing it with targeted advertising. However, Scoolio states that they do not collect or share any information from students without their consent.


To build student membership, Scoolio has partnered with schools around Germany to use their platform as a remote teaching assistance tool for file exchanges or remote digital homework collection.


It's very development was financially backed by three state-owned investment groups, namely SIB Innovations - und Beteiligungsgesellschaft mbH, Technologiegründerfonds Sachsen, and Kreissparkasse Bautzen. 


Due to the partnerships and government backings, many students use the app as a standard tool in their classes.


Data exposed by leaky API
-------------------------


In Zerforchung's report, Wittmann explains how she exploited Scoolio API flaws to retrieve extremely sensitive data for any user ID used on the app.


The exposed personal data includes:


* User nickname
* User and parent email addresses
* GPS location at which the app was last opened
* Name of school and class
* Interests
* UUID details
* Personality traits (origin, religion, sexuality)


Wittman shared a fictitious sample of the types of data exposed by the flaw below.



![Sample profile details](https://www.bleepstatic.com/images/news/security/scoolio-data.jpg)**Fictitious sample of types of exposed data**  
*Source: Zerforschung*
While Scoolio states that 1.8 million people use their app, the researcher believes that the actual number is closer to 400,000 based on how user ids are created.


"We cannot say exactly how many students are affected. Because scoolio artificially inflates its user numbers by creating accounts without asking: As soon as you download the app and open it once, an empty profile with a UUID is generated - regardless of whether you actually want to create a user account," explains the [Zerforchung report](https://zerforschung.org/posts/scoolio/).


Fix released after thirty days
------------------------------


Zerforchung states that they disclosed the flaw to Scoolio on September 21, 2021, but it took the software developer until October 25, 2021 to deploy a patch.


However, due to the simplicity of the fix and the sensitive nature of the exposed data, Wittmann believes the fix should have been released more quickly.


"I would like to thank Ms. Wittmann for the information and the SDS for the exchange and thank you for your feedback on our security measures," Danny Roller, CEO andFounder of the Scoolio app, shared in a statement.


"Fortunately, after extensive testing, we can confirm that No user data was intercepted by third parties prior to the investigation by Ms. Wittmann and we have successfully closed the gaps found."




#### Tags:
[[Scoolio]] [[Wittmann]] [[API]] [[Zerforchung]] [[Bleeping Computer]]
