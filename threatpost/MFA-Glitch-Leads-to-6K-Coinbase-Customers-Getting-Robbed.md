# MFA Glitch Leads to 6K+ Coinbase Customers Getting Robbed
### Coinbase suspects phishing led to attackers getting personal details needed to access wallets but also blamed a flaw in its SMS-based 2FA. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175290)
+ Date: October 1, 2021  4:08 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/12/21111956/Digital-Wallet.jpg)
The accounts of at least 6,000 Coinbase customers were robbed of funds after attackers bypassed the cryptocurrency exchange’s multi-factor authentication (MFA).


According to a notification letter ([PDF](https://s3.documentcloud.org/documents/21073975/09-24-2021-coinbase-customer-notification.pdf)) Coinbase sent to affected customers and filed with the California state Attorney General’s office, the theft happened between March and May 20, 2021.


The attacker(s) used a flaw in Coinbase’s account recovery process to seize the SMS two-factor authentication tokens needed to break into customers’ accounts and transfer funds to crypto wallets unassociated with Coinbase.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In order to pull it off, the culprits first needed access to victims’ email addresses, passwords, phone numbers and personal email inboxes. Coinbase doesn’t know exactly how the third parties gained access to all that, but the exchange doesn’t think it’s to blame: “We have not found any evidence that these third parties obtained this information from Coinbase itself,” according to the exchange’s breach notification.


Coinbase noted that such information is often gleaned through phishing attacks or other social engineering techniques that trick victims into disclosing their login credentials.


Coinbase Phishing Attacks Are Rising
------------------------------------


In fact, earlier this week, on Monday, Coinbase warned that [phishing attacks are on the rise](https://blog.coinbase.com/phishing-attacks-are-on-the-rise-here-are-some-steps-you-can-take-to-protect-yourself-872833c7671b), both in terms of volume and success rates. Between April and early May 2021, its security team saw a “significant uptick” in Coinbase-branded phishing messages that targeted users of a range of commonly used email service providers: attacks that “demonstrated a higher degree of success” at bypassing spam filters of certain older email services.


Coinbase provided samples of the phishing attacks its team has seen, including the ones shown below:


Clearly, cryptocurrency thieves are nothing if not creative, and understandably so: They’re going after a lucrative, juicy target. While they’re considered a secure place for users to store their cryptocurrency assets, [researchers in 2018 proved](https://threatpost.com/cryptocurrency-wallet-hacks-spark-dustup/140445/) that wallets such as Ledger and Trezor are vulnerable to a number of cyber attacks.


Subsequent events proved their point: In July 2020, an unauthorized third party [accessed Ledger’s](https://www.ledger.com/addressing-the-july-2020-e-commerce-and-marketing-data-breach) e-commerce and marketing database, which held email addresses as well as contact and order details including first and last name, postal address, email address, and phone number.


Following the July attack, researchers discovered [widespread campaigns](https://threatpost.com/malicious-google-web-extensions-cryptowallet/154832/) spreading malicious browser extensions that were abusing Google Ads and well-known cryptocurrency brands including Ledger to lure victims and eventually steal their cryptocurrency wallet credentials. Other wallets targeted in the campaign included Electrum, Exodus, Jaxx, KeepKey, MetaMask, MyEtherWallet and Trezor.


As well, the rise of cryptocurrency has made compromised crypto accounts hugely valuable in Dark Web marketplaces, according to the [2021 Dark Web price index](https://threatpost.com/dark-web-markets-stolen-data/164626/) from Privacy Affairs.


“Due to the skyrocketing prices of Bitcoin and other cryptocurrencies, hacked accounts may hold large sums of coin-based currency and cash, protected by relaxed security measures after the initial verification process,” according to the report, which listed the average price for a hacked Coinbase-verified account to be $610.


SMS 2FA Authentication Flaw
---------------------------


TL;DR: There are a lot of ways that the attackers could have gotten Coinbase users’ personal details.


But beyond the personal information they needed to crack victims’ accounts, the thieves needed more. For customers who use SMS texts for two-factor authentication (2FA), the unauthorized third parties had to leverage what Coinbase called a flaw in its SMS account recovery process, in order to receive an SMS 2FA token so as to gain access to accounts.


Coinbase didn’t go into detail about the flaw: It only said that as soon as it learned about the issue, it “updated our SMS Account Recovery protocols to prevent any further bypassing of that authentication process.”


In a [guide on securing accounts](https://help.coinbase.com/en/coinbase/privacy-and-security/data-privacy/how-can-i-make-my-account-more-secure), Coinbase recommends enabling MFA authentication using security keys or Time-based One Time Passwords (TOTP) with an authenticator app. Verification via SMS text messages is listed as an option, but with caveats: This verification is, after all, subject to [SIM-swap](https://threatpost.com/mobile-customer-service-sim-swap-fraud/151993/) or phone-port attack.


SIM swapping​​ is a form of fraud that allows crooks to bypass SMS-based 2FA and crack online banking or other high-value accounts such as cryptocurrency wallets. In a typical scenario, an attacker would start by phishing personal and banking information – often via SMS phishing, which has the added benefit of confirming that a victim’s cell phone number is an active line. Next, an attacker calls the victim’s mobile carrier – easily discovered with an online search – and convinces a service rep to port the line to a different SIM card/device.


Can We Please Just Ditch SMS-Based 2FA?
---------------------------------------


Experts agree that we should stick a fork in SMS-based 2FA: It’s clearly toast.


Roger Grimes, author of “Hacking Multifactor Authentication” and data-driven defense evangelist, for [KnowBe4,](https://u7061146.ct.sendgrid.net/ls/click?upn=4tNED-2FM8iDZJQyQ53jATUavSzE-2FiwjSkZ-2BMZMLjTD68bBzltWsjOj4iPYBhQEjDkyRzZ_q07lK5GAAVvAnbc-2Fr-2FBDhAPhoMvwzp-2Bdh4wgfTcF0AUhu01ZMXdKNJrsN0iCyDU7ehW0N22Ype9yCK1TM6XYzZcULka2hXrkxot-2FYcsNMOW-2Fi7ZSbc4BW4Y4w5w74Jad0kl33W4of4UEvii1-2FaSF1UuT-2BEz-2F3w-2Fa4quMRgT-2BQRwS2UzU-2B80mrmRcZ7BOu57U-2BlcUbUsgPP5Wrdcp27qpLYZxzLJ8Qwfb3N2eINqk-2B5ALA-2BX5H1WrmgjAUxrSn8W0e1Z6v5ZnIV13lpn-2B50Ro1gC3Tlq6dmLQeuWBPT6iCljuZaA0Ro4dPQB024lIgxWmvsVLHVUCHy-2BYHA-2BMTirRBLwlLSZQSccA4CzRdeZ-2Fb9M-3D)  said that this has got to be at least the third or fourth time that Coinbase customers have been compromised. While all MFA solutions can be hacked multiple ways, SMS-based MFA are “among the most hackable MFA solutions,” he said.


It isn’t exactly breaking news. In 2017, the [NIST Digital Identity Guidelines](https://www.nist.gov/itl/applied-cybersecurity/tig/projects/special-publication-800-63) said that SMS-based MFA was very weak and shouldn’t be used to protect valuable data and content, going so far as to reserve the right  to remove it as an allowed MFA solution completely in the future.


In spite of that, “SMS-based MFA is probably the most used MFA solution on the internet today,” Grimes said. He blames vendors who force users to rely on SMS-based MFA because that’s what the vendor uses.


“Almost all the users that do use SMS-based MFA do not know how easily it is hacked,” Grimes contended, which is an issue with all MFA solutions. “Users are not told how each type can be still be hacked, abused and bypassed, sometimes easily so, and this leads to most users thinking they are being super secure because they are using MFA and far less hackable, when that is absolutely not the case.”


Grimes thinks that the MFA solution lies in making sure “that  all stakeholders (e.g., management, buyers, implementers, sysadmins, users, etc.) understand what the potential weaknesses are for their particular type of MFA, and everyone is educated about possible attacks and how to avoid them.”


Chris Clements, vice president of solutions architecture for Cerberus Sentinel, added that it’s incumbent on cryptocurrency users  to understand that they’re constantly being targeted by cybercriminals attempting to rob them.


And once those funds are gone, they’re gone for good, Clements said. “The decentralized nature of most coins means that if criminals are successful in stealing them, there’s very little chance you will be able to recover your losses,” he said.  “As such, it’s important that users of cryptocurrency study up and implement appropriate opsec to protect themselves from the inevitable attacks, including ensuring that any computing devices or smartphones are hardened and up to date with the latest security patches and implementing strong unique passwords as well as multi-factor authentication controls such as TOTP or hardware security keys like FIDO.  Finally, cold wallets kept completely offline are useful for limiting much easier online attack vectors.”


Coinbase Makes Good on the Money
--------------------------------


Coinbase said that it will deposit funds back into victims’ accounts, “equal to the value of the currency improperly removed from your account at the time of the incident.” Some customers have already been reimbursed, the exchange said, promising that customers will receive “the full value of what you lost.”


The exchange is also providing free credit monitoring to affected customers.


Coinbase encouraged users of SMS-based authentication to drop it and to instead use stronger MFA, including TOTP or a hardware security key. It also strongly encouraged victims to change their Coinbase account password to a new, strong and unique password: one that’s not used on any other site.


The same goes for email accounts: “Because the third parties needed access to your personal email account as part of this incident, we strongly encourage you to change your password in the same way for your email account and for any other online accounts where you use a similar password,” the exchange advised.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Coinbase]] [[MFA]] [[SMS]] [[SMS-based]] [[phishing]] [[said.]] [[victims’]] [[it’s]] [[they’re]] [[2FA]] [[ThreatPost]]
