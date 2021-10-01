# Hackers rob thousands of Coinbase customers using MFA flaw
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/hackers-rob-thousands-of-coinbase-customers-using-mfa-flaw/)
+ Date: October 1, 2021
+ Author: Lawrence Abrams


## Article:

![Coinbase](https://www.bleepstatic.com/content/hl-images/2021/10/01/coinbase-header.jpg)*Source: Coinbase*
Crypto exchange Coinbase disclosed that a threat actor stole cryptocurrency from 6,000 customers after using a vulnerability to bypass the company's SMS multi-factor authentication security feature.


Coinbase is the world's second-largest cryptocurrency exchange, with approximately 68 million users from over 100 countries.


In a notification sent to affected customers this week, Coinbase explains that between March and May 20th, 2021, a threat actor conducted a hacking campaign to breach Coinbase customer accounts and steal cryptocurrency.


To conduct the attack, Coinbase says the attackers needed to know the customer's email address, password, and phone number associated with their Coinbase account and have access to the victim's email account.


While it is unknown how the threat actors gained access to this information, phishing campaigns targeting Coinbase customers to steal account credentials have become common. Additionally, banking trojans traditionally used to steal online bank accounts are also [known to steal Coinbase accounts](https://www.bleepingcomputer.com/news/security/banking-trojan-now-targets-coinbase-users-not-just-banking-portals/).




> 
> Fresh, less than 2 hours ago registered [@coinbase](https://twitter.com/coinbase?ref_src=twsrc%5Etfw) phishing: https://coinbase-authorise[.]com/  
> 
> Another (different than the previous) live one, [@Bank\_Security](https://twitter.com/Bank_Security?ref_src=twsrc%5Etfw)... [pic.twitter.com/ie5jzRMcj2](https://t.co/ie5jzRMcj2)
> 
> 
> — MalwareHunterTeam (@malwrhunterteam) [January 29, 2021](https://twitter.com/malwrhunterteam/status/1355231593028341761?ref_src=twsrc%5Etfw)


MFA bug allowed access to accounts
----------------------------------


Even if a hacker has access to a Coinbase customer's credentials and email account, they are normally prevented from logging into an account if a customer has multi-factor authentication enabled.


In Coinbase's [guide on securing accounts](https://help.coinbase.com/en/coinbase/privacy-and-security/data-privacy/how-can-i-make-my-account-more-secure), they recommend enabling multi-factor (MFA) authentication utilizing security keys, Time-based One Time Passwords (TOTP) with an authenticator app, or as a last resort, SMS text messages.


However, Coinbase states a vulnerability existed in their SMS account recovery process, allowing the hackers to gain the SMS two-factor authentication token needed to access a secured account.


"Even with the information described above, additional authentication is required in order to access your Coinbase account," explained a [Coinbase notification](https://s3.documentcloud.org/documents/21073975/09-24-2021-coinbase-customer-notification.pdf) to customers seen by BleepingComputer.


"However, in this incident, for customers who use SMS texts for two-factor authentication, the third party took advantage of a flaw in Coinbase’s SMS Account Recovery process in order to receive an SMS two-factor authentication token and gain access to your account."


As the threat actor also had full access to an account, customers' personal information was also exposed, including their full name, email address, home address, date of birth, IP addresses for account activity, transaction history, account holdings, and balances.


As the Coinbase bug allowed threat actors to access what were believed to be secured accounts, the exchange is depositing funds in affected accounts equal to the stolen amount.


"We will be depositing funds into your account equal to the value of the currency improperly removed from your account at the time of the incident. Some customers have already been reimbursed -- we will ensure all customers affected receive the full value of what you lost. You should see this reflected in your account no later than today," promised Coinbase.


It is not clear if Coinbase will be crediting hacked customers with the cryptocurrency that was stolen or fiat currency. If fiat currency, it could lead to a taxable event for the victims if they had an increase in profits.


What Coinbase victims should do
-------------------------------


Since the attack required the password of both a customer's Coinbase and email account, it is strongly recommended that victims change their passwords immediately.


Coinbase also recommends users switch to a more secure MFA method, such as a hardware security key or an authentication app.


Finally, victims should be on the lookout for future targeted phishing emails or SMS texts that attempt to steal credentials using information exposed in the breach.


This is not the first time a bug in Coinbase's MFA system caused issues for their customers.


In August, Coinbase accidentally [alerted 125,000 customers that their 2FA settings had been changed](https://www.bleepingcomputer.com/news/security/coinbase-seeds-panic-among-users-with-erroneous-2fa-change-alerts/), causing panic among those receiving the alert.


BleepingComputer has contacted Coinbase with further questions regarding this attack but has not heard back at this time.




#### Tags:
[[Coinbase]] [[SMS]] [[multi-factor]] [[address,]] [[MFA]] [[account,]] [[two-factor]] [[Bleeping Computer]]
