# Attackers don’t bother brute-forcing long passwords, Microsoft engineer says
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/attackers-dont-bother-brute-forcing-long-passwords-microsoft-engineer-says/)
+ Date: November 22, 2021
+ Author: Catalin Cimpanu


## Article:
![Attackers don’t bother brute-forcing long passwords, Microsoft engineer says](https://therecord.media/wp-content/uploads/2021/11/password-decryption-key.jpg)

According to data collected by Microsoft’s network of honeypot servers, most brute-force attackers primarily attempt to guess short passwords, with very few attacks targeting credentials that are either long or contain complex characters.


“I analysed the credentials entered from over >25 million brute force attacks against SSH. This is around 30 days of data in Microsoft’s sensor network,” said [Ross Bevington](https://www.linkedin.com/in/ross-bevington-854440152/), a security researcher at Microsoft.


“77% of attempts used a password between 1 and 7 characters. A password over 10 characters was only seen in 6% of cases,” said Bevington, who works as Head of Deception at Microsoft, a position in which he’s tasked with creating legitimate-looking honeypot systems in order to study attacker trends.


![0-Bevington-image](https://www-therecord.recfut.com/wp-content/uploads/2021/11/0-Bevington-image.jpg)Image: Ross Bevington
Bevington says that only 7% of the brute-force attempts he analyzed in the sample data included a special character. In addition, 39% actually had at least one number, and none of the brute-force attempts used passwords that included white space.


The researcher’s findings suggest that longer passwords that include special characters are most likely safe from the vast majority of brute-force attacks, as long as they haven’t been leaked online and are part of attackers’ brute-forcing dictionaries.


### RDP brute-force attacks tripled this year


In addition, Bevington said that based on data from more than 14 billion brute-force attacks attempted against Microsoft’s network of honeypot servers —also known as a **sensor network**— until September this year, attacks on Remote Desktop Protocol (RDP) servers have tripled compared to 2020, seeing a rise of 325%.


Network printing services also saw an increase of 178%, as well as Docker and Kubernetes systems, which saw an increase of 110%.


“Stats on SSH & VNC are just as bad – they just hasn’t changed that much since last year,” Bevington said.


“By default solutions like RDP are turned off but if you decide to turn them on, don’t put stuff straight on the Internet. Remember that attackers will go after any brute forcible remote admin protocol. If you must have yours accessible on the Internet use strong passwords, managed identity, MFA,” the Microsoft manager said.





#### Tags:
[[brute-force]] [[Bevington]] [[Microsoft’s]] [[The Record]]
