# 7 million Robinhood user email addresses for sale on hacker forum
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/7-million-robinhood-user-email-addresses-for-sale-on-hacker-forum/)
+ Date: November 15, 2021
+ Author: Lawrence Abrams


## Article:
![Robinhood](https://www.bleepstatic.com/content/hl-images/2021/11/08/robinhood-header.jpg)


The data for approximately 7 million Robinhood customers stolen in a recent data breach are being sold on a popular hacking forum and marketplace.


Last week, [Robinhood disclosed a data breach](https://www.bleepingcomputer.com/news/security/robinhood-discloses-data-breach-impacting-7-million-customers/) after one of its employees was hacked, and the threat actor used their account to access the information for approximately 7 million users through customer support systems.


The data stolen during the attack includes the following personal information for Robinhood users:


* Email addresses for 5 million customers.
* Full names for 2 million other customers.
* Name, date of birth, and zip code for 300 people.
* More extensive account information for ten people.


In addition to stealing the data, Robinhood stated that the hacker attempted to extort the company to prevent the data from being released.


Stolen email addresses, especially those for financial services, are particularly popular among threat actors as they can be used in targeted phishing attacks to steal more sensitive data.


Stolen Robinhood data sold on a hacking forum
---------------------------------------------


Two days after Robinhood disclosed the attack, a threat actor named 'pompompurin' announced that they were selling the data on a hacking forum.


In a forum post, pompompurin said he was selling 7 million Robinhood customers' stolen information for at least five figures, which is $10,000 or higher.



![Threat actor selling the stolen Robinhood data](https://www.bleepstatic.com/images/news/security/d/data-breaches/r/robinhood/data-for-sale/hacker-forum-post.jpg)**Threat actor selling the stolen Robinhood data**  
*Source: BleepingComputer*
The sold data includes 5 million email addresses, and for another batch of Robinhood customers, 2 million email addresses and their full names. However, pompompurin said they were not selling the data for 310 customers who had more sensitive information stolen, including identification cards for some users.


Robinhood did not initially disclose the theft of ID cards, and the threat actor states that they downloaded them from SendSafely, a secure file transfer service used by the trading platform when performing Know Your Customer (KYC) requirements.


"As we disclosed on November 8, we experienced a data security incident and a subset of approximately 10 customers had more extensive personal information and account details revealed," Robinhood told BleepingComputer after we contacted them regarding the sale of their data.


"These more extensive account details included identification images for some of those 10 people. Like other financial services companies, we collect and retain identification images for some customers as part of our regulatory-required Know Your Customer checks."


pompompurin told BleepingComputer that he gained access to the Robinhood customer support systems after tricking a help desk employee into installing a remote access software on their computer.


Once remote access software is installed on a device, a threat actor can monitor their activities, take screenshots, and remotely access the computer. Additionally, while remotely controlling a device, the attackers can also use the employee's saved login credentials to log in to internal Robinhood systems that they had access to.


"I was able to see all account information on people. I saw a few people while the support agent did work," pompompurin told BleepingComputer.


In response to further questions regarding how the employee's device was breached, Robinhood referred us back to their original statement stating that the threat actor "socially engineered a customer support employee by phone." However, they did confirm to BleepingComputer that malware was not used in the attack


As proof that they conducted the attack, pompompurin posted screenshots seen by BleepingComputer of the attackers accessing internal Robinhood systems.


These screenshots included an internal help desk system used to lookup Robinhood member information by email address, an internal knowledge base page about a "Project Oliver Twister" initiative designed to protect high-risk customers, and an "annotations" page showing notes for a particular customer.



![Part of a screenshot showing internal member notes](https://www.bleepstatic.com/images/news/security/d/data-breaches/r/robinhood/data-for-sale/annotations.jpg)**Part of a screenshot showing internal member notes**
After learning of the data being sold, BleepingComputer contacted Robinhood and asked for confirmation as to whether these screenshots originated from their systems.


While they did not explicitly confirm the screenshots are of their systems, they asked that any screenshots be redacted of private information, indicating they were likely taken during the attack.


Same threat actor responsible for recent FBI hack
-------------------------------------------------


 This threat actor, pompompurin, was also [responsible for abusing FBI's email servers](https://www.bleepingcomputer.com/news/security/fbi-system-hacked-to-email-urgent-warning-about-fake-cyberattacks/) to send threatening emails over the weekend,


This weekend, US entities began to receive emails sent from FBI infrastructure warning recipients that their "virtualized clusters " were being targeted in a "sophisticated chain attack," as shown in the email below.



![Fake FBI warning email sent this weekend](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Fake FBI warning email sent this weekend**
To send these emails, pompompurin found a bug in the FBI Law Enforcement Enterprise Portal (LEEP) portal that the actor could exploit to send emails from IP addresses belonging to the FBI.


As the emails came from IP addresses owned by the FBI, it added legitimacy to the emails, causing the government agency to become flooded with concerned calls about the fake warnings.


After learning of the attack, the FBI took the associated server offline to resolve the issue.




#### Tags:
[[Robinhood]] [[pompompurin]] [[BleepingComputer]] [[screenshots]] [[people.]] [[emails]] [[systems.]] [[attack,]] [[Bleeping Computer]]
