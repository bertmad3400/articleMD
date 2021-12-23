# Phishing campaign targets CoinSpot cryptoexchange 2FA codes
### A new phishing campaign that targets users of the CoinSpot cryptocurrency exchange employs a new theme that revolves around withdrawal confirmations.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/phishing-campaign-targets-coinspot-cryptoexchange-2fa-codes/
+ Date: 2021-12-23T13:31:49-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/03/05/cryptocurrency-assorted.jpg)

![cryptocoins](https://www.bleepstatic.com/content/hl-images/2021/03/05/cryptocurrency-assorted.jpg?rand=520395637)


A new phishing campaign that targets CoinSpot cryptocurrency exchange users employs a new theme revolving around withdrawal confirmations with the end goal of stealing two-factor authentication (2FA) codes.


More specifically, the threat actors send emails from a Yahoo address, replicating real emails from CoinSpot that ask the recipients to confirm or cancel a withdrawal transaction.


These phishing messages also include details such as the transaction amount and a Bitcoin wallet address to add legitimacy to the attack.


Clicking on either of the embedded buttons on the email takes the victim to a phishing landing page that clones the CoinSpot login page and uses a domain name sufficiently close to the spoofed one not to attract the target's attention.



![The email that reaches CoinSpot users](https://www.bleepstatic.com/images/news/u/1220909/Phishing/email(5).png)*Phishing email sent to CoinSpot users (Cofense)*
"The style appears authentic, and there is even a Bitcoin address included to add to legitimacy. The user is prompted to either confirm or cancel the withdrawal, but both links have the same SendGrid hyperlink," explains the [Cofense report](https://cofense.com/blog/cryptocurrency-and-exchange-phish-used-to-steal-user-information/).


To further increase the "authentic" look of the phishing page, the threat actors also use a digital certificate that adds a lock symbol to the URL address bar to trick the visitor into thinking they've reached CoinSpot's legitimate and secure login form.



![Login page on the spoofed CoinSpot site](https://www.bleepstatic.com/images/news/u/1220909/Phishing/login.png)*CoinSpot login form cloned page used for phishing credentials (Cofense)*
On the landing page, the victims are prompted to enter their account credentials on the phishing site, allegedly to verify or reject the transaction.


If they do that, they are served with a two-factor authentication page, which is the last protection measure against account takeover attempts.



![Stealing 2FA codes through a legitimate-looking page](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Stealing 2FA codes through a legitimate-looking page**  
*Source: Cofense*
After entering their 2FA code, the victims are redirected to the official CoinSpot website in a final attempt to reduce the chances of raising suspicion.


The attackers can then use the account credentials and the stolen 2FA codes to take over the victim's account. This is a time-sensitive act, indicating the scammers' active involvement throughout the process.


Keep your crypto-investments secure
-----------------------------------


The hype around cryptocurrency investing creates a constant influx of inexperienced and potentially gullible users, which compels an ever-increasing number of threat actors to target the particular field.


This year, we have seen many different methods and tricks employed by phishing actors and scammers, from [smishing](https://www.bleepingcomputer.com/news/security/celsius-email-system-breach-leads-to-phishing-attack-on-customers/) and [support scams](https://www.bleepingcomputer.com/news/security/trust-wallet-metamask-crypto-wallets-targeted-by-new-support-scam/) to [fake giveaways](https://www.bleepingcomputer.com/news/security/new-elon-musk-club-crypto-giveaway-scam-promoted-via-email/) and [malicious Google Ads](https://www.bleepingcomputer.com/news/security/crypto-investors-lose-500-000-to-google-ads-pushing-fake-wallets/).


In this case, even though the phishing email appears legitimate, the fact that it comes from a Yahoo email address is a clear sign of fraud.


Whenever you receive emails that ask you to take action, review basic elements such as the sender’s address calmly, and look for anything out of place.


Even if everything looks authentic, do not click on embedded email buttons. Instead, open a new tab on your browser, visit the official website manually, log in to your account, and check for any alerts or messages that require your attention.


For a complete list of security recommendations from CoinSpot on how to secure your devices and protect yourself from scammers, [check out this support page](https://coinspot.zendesk.com/hc/en-us/articles/333757066344).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Phishing]] [[Coinspot]] [[Emails]] [[2fa]] [[Scammers]] [[Bleeping Computer]]

