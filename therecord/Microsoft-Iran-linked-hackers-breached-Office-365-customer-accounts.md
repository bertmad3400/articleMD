# Microsoft: Iran-linked hackers breached Office 365 customer accounts
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-iran-linked-hackers-breached-office-365-customer-accounts/)
+ Date: October 11, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft: Iran-linked hackers breached Office 365 customer accounts](https://therecord.media/wp-content/uploads/2021/09/hacker-attacks.png)

Microsoft said today that a new Iran-linked hacking group has targeted more than 250 Office 365 tenants and compromised accounts for less than 20.


The attacks, which the company disclosed today in a security alert, have been carried out via [password spraying](https://owasp.org/www-community/attacks/Password_Spraying_Attack), a technique where hackers try the same password over and over again—while rotating the username.


![password-spraying](https://www-therecord.recfut.com/wp-content/uploads/2021/10/password-spraying.png)Image: OWASP
The Redmond-based software company said the attacks were carried out by a new group the company is now tracking as **DEV-0343**, but which they linked to Iran because of similarities in offensive techniques, targeting, and other patterns.


Microsoft said the group’s attacks, which are still ongoing, have “a focus on US and Israeli defense technology companies, Persian Gulf ports of entry, or global maritime transportation companies with business presence in the Middle East.”



> Targeting in this DEV-0343 activity has been observed across defense companies that support United States, European Union, and Israeli government partners producing military-grade radars, drone technology, satellite systems, and emergency response communication systems. Further activity has targeted customers in geographic information systems (GIS), spatial analytics, regional ports of entry in the Persian Gulf, and several maritime and cargo transportation companies with a business focus in the Middle East.
> 
> Microsoft


Microsoft’s security teams said the password spraying attacks are usually conducted from Tor IP addresses, mimic a Firefox browser user agent, and take place during Iran’s daytime timezones — namely, between Sunday and Thursday between 7:30 AM and 8:30 PM Iran Time (04:00:00 and 17:00:00 UTC).


When attacks hit, the hackers first enumerate active employee accounts within an organization and then move to the actual password spraying routine.


To enumerate accounts, hackers abuse two Exchange email server features (Autodiscover and ActiveSync), Microsoft said.


“On average, between 150 and 1,000+ unique Tor proxy IP addresses are used in attacks against each organization,” the OS maker explained.


Microsoft has released [indicators of compromise and instructions](https://www.microsoft.com/security/blog/2021/10/11/iran-linked-dev-0343-targeting-defense-gis-and-maritime-sectors/) for Office 365 tenants on how to find past attacks in their logs and determine what accounts were compromised.


“We encourage our customers to use this information to look for similar patterns in logs and network activity to identify areas for further investigation,” the company said today.





#### Tags:
[[Microsoft]] [[The Record]]
