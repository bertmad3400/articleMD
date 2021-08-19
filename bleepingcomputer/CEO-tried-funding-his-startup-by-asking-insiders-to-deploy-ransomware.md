# CEO tried funding his startup by asking insiders to deploy ransomware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/ceo-tried-funding-his-startup-by-asking-insiders-to-deploy-ransomware/)
+ Date: August 19, 2021
+ Author: Ionut Ilascu


## Article:
![CEO tried funding his startup by asking insiders to deploy ransomware](https://www.bleepstatic.com/content/posts/2021/08/19/slip-up_banana.jpg)


Likely inspired by the LockBit ransomware gang, a Nigerian threat actor tried their luck with a $1 million payment lure to recruit an insider to detonate a ransomware payload on the company servers.


The plan backfired when the scammer picked the wrong target, revealing their technique along with their lack of experience and reconnaissance skills.


### A one million dollar offer


Multiple messages sent to inboxes protected by cloud email security platform Abnormal Security caught the researchers’ attention due to the sender’s offer for the recipient: a $1 million payout for deploying ransomware on the network.


![Nigerian scammer tries to deploy open-source ransomware via company insider](https://www.bleepstatic.com/images/news/u/1100723/2021/MadalinDemonware.png)


Demonware (also known as Black Kingdom) is an open-source ransomware project available on GitHub and typically deployed by individuals less technical individuals. However, the actor claimed it was their Python-coded project.


The researchers responded to the threat actor’s invitation to chat by posing as an employee that wanted to make some easy money, Crane Hassold, director of threat intelligence at Abnormal Security writes in a [blog post](https://abnormalsecurity.com/blog/nigerian-ransomware-soliciting-employees-demonware/) today.


With introductions no longer needed, the threat actor delivered the ransomware payload and the conversation kept flowing over Telegram, providing insight into the motivation and technical abilities of the scammer.


As the chat continued, the actor kept lowering the payout, first to $250,000 and then to $120,000, a clear sign that they were not familiar with how the ransomware game is played.


What drove the threat actor into trying their luck with ransomware was the desire to fund their business, a social network startup called Sociogram where he acted as CEO. They disclosed more personal details by saying they owned the startup and that they were located in Nigeria and even shared their LinkedIn profile


![Wannabe Nigerian ransomware actor shares motivation](https://www.bleepstatic.com/images/news/u/1100723/2021/MadalinMotiv.png)


This information fits the details the researchers found before starting talking with the actor by looking for data online associated with the email address in the initial message.


However, more important for the researchers was the method used to collect the target email addresses. This was nothing complicated: parsing LinkedIn accounts for corporate emails belonging to executive-level employees.


![Wannabe Nigerian ransomware actor shares method](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


As per the threat actor, they resorted to ransomware after trying without success to compromise the email accounts through phishing.


Nigeria is best known in the infosec industry as the cradle of business email compromise (BEC) scammers, so social engineering is a common tactic among the country’s cybercriminals.


It appears that the Nigerian actor could not come up with an original lure and took a page from LockBit’s book when trying to enlist an insider for the job.


At the beginning of the month, [BleepingComputer reported](https://www.bleepingcomputer.com/news/security/lockbit-ransomware-recruiting-insiders-to-breach-corporate-networks/) that the LockBit ransomware gang announced that they were looking for corporate insiders to help with breaching and encrypting networks.


The group promised millions of U.S. dollars to employees that switched to their side and provided RDP, VPN, or corporate email credentials that permitted access to the network.




#### Tags:
[[ransomware]] [[Bleeping Computer]]
