# Spyware features found in Chinese state benefits app
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/spyware-features-found-in-chinese-state-benefits-app/)
+ Date: July 29, 2021
+ Author: Catalin Cimpanu


## Article:
![Spyware features found in Chinese state benefits app](https://therecord.media/wp-content/uploads/2021/07/Beijing-China.png)

Spyware-like features have been discovered inside an app named “Beijing One Pass” that foreign companies operating in China are forced to install on their systems in order to access a digital platform to manage employee state benefits.


The spyware behavior was discovered last month by Insikt Group, the threat research division of Recorded Future, which analyzed a copy received from a customer who was forced to install the suspicious on its systems.


According to the [team’s analysis](https://www.recordedfuture.com/beijing-one-pass-benefits-software-spyware?__hstc=156209188.ab5a6c06abbde6989d75a44e2f4ed75c.1627606833094.1627606833094.1627606833094.1&__hssc=156209188.1.1627606833095&__hsfp=3914057893), the app contained features that could be considered “suspicious for a benefits software application” and which are ordinarily found in malware strains. This included features such as:


* Disabling of security and backup services on the host device
* Reading data from the clipboard
* Recording screenshots
* Capturing and retrieving keystrokes
* Attempt to read, create, or modify system registry ROOT certificates
* Check periodically for human interaction with the operating system as the file is run
* Allow-listing domains for ActiveX use, which would allow it to connect to external internet resources
* The ability to autorun at Windows startup to ensure persistence


![Beijing-One-Pass](https://www-therecord.recfut.com/wp-content/uploads/2021/07/Beijing-One-Pass.png)
The suspicious app, shown in the image above, was developed by the Beijing Certificate Authority ([BJCA](https://www.bjca.cn/)), a Chinese state-owned company primarily known for its certificate authority (CA) business.


At the time of writing, it is unclear if the spyware features were added inside the Beijing One Pass software on purpose or if they were inserted after a compromise of the company’s software development pipeline.


Contacted by phone, a BJCA spokesperson did not want to comment.


While information about how the spyware functionality made it inside the app is still shrouded in mystery, their presence is undeniable. Furthermore, companies doing business in China may not have an option and may be forced to install the software.


For this reason, Insikt Group analysts recommend that companies run the app only on systems that do not store sensitive corporate information.


The Insikt Group’s discovery is also reminiscent of the findings of Trustwave Labs, which found in June 2020 that a Chinese bank was forcing foreign companies operating in China to install [a backdoored app](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/) in order to file taxes with local governments.





#### Tags:
[[spyware]] [[Insikt]] [[The Record]]
