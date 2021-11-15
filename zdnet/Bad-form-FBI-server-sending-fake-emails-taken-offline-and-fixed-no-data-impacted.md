# Bad form: FBI server sending fake emails taken offline and fixed, no data impacted
### Far from complex, the sender manipulated a POST request to send an email from FB infrastructure, and automated it.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/bad-form-fbi-server-sending-fake-emails-taken-offline-and-fixed-no-data-impacted/)
+ Date: November 15, 2021
+ Author: Chris Duckett


## Article:
Unknown

![fbi-decision-to-withhold-kaseya-ransomware.jpg](https://www.zdnet.com/a/img/resize/84e9bbb7032d59612f7e0471df4c273e6349f02b/2021/09/27/11cf4ae8-38a8-4caa-8a94-b2652ec8bc61/fbi-decision-to-withhold-kaseya-ransomware.jpg?width=1200&fit=bounds&auto=webp)
 Image: Dzelat/Shutterstock
 The FBI has [placed the blame](https://www.fbi.gov/news/pressrel/press-releases/fbi-statement-on-incident-involving-fake-emails) for a weekend fake email incident on a misconfiguration in its Law Enforcement Enterprise Portal (LEEP) that allowed emails to be sent from the ic.fbi.gov domain.

"LEEP is FBI IT infrastructure used to communicate with our state and local law enforcement partners," it said. 

"While the illegitimate email originated from an FBI operated server, that server was dedicated to pushing notifications for LEEP and was not part of the FBI's corporate email service. No actor was able to access or compromise any data or PII on the FBI's network."

The FBI said it initially took the "impacted hardware" quickly offline, and later said it quickly remediated the "software vulnerability" as well as confirmed its network integrity.

Spamhaus [said](https://twitter.com/spamhaus/status/1459459116435480577) it saw two waves of email being sent.

Brain Krebs [reported](https://krebsonsecurity.com/2021/11/hoax-email-blast-abused-poor-coding-in-fbi-website/) the sender of the emails found they were able to send emails because the FBI was generating a client-side  one-time code to sign up to a new account on LEEP, and it was sent along with an email subject and body as a POST request to the FBI's servers. Manipulating the request parameters enabled the emails to be sent, and a script was used to automate the sending process.

It would seem all the so-called misconfigurations and software vulnerabilities were in the way the FBI had its portal built, with the cherry on top being how it exposed and piped user input to a mail server. Pretty embarrassing and worthy of a dozen facepalms, at least.





#### Tags:
[[emails]] [[ZDNet]]
