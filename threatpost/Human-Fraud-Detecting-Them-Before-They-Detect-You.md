# Human Fraud: Detecting Them Before They Detect You
### Tony Lauro, director of security technology and strategy at Akamai, discusses how to disrupt account takeovers in the exploitation phase of an attack.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169230)
+ Date: September 6, 2021  11:29 am
+ Author: Tony Lauro


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/06111636/Mule-e1630941412596.jpg)
**This is Part II of a two-part blog series taking readers inside the criminal enterprise that is account-takeover fraud. For part I, please [click here](https://threatpost.com/underground-economy-account-takeovers/169032/).**


In my last blog, we focused on the initial phases of the account-takeover (ATO) kill chain – recon, weaponization and delivery – and how attackers leverage various tools and techniques to obfuscate bot activity as they acquire and test credentials via automation. After weaponization, threat actors will either decide to sell validated combo-lists for another criminal gang to leverage, or they will continue down the [ATO kill chain](https://www.akamai.com/content/dam/site/en/documents/infographic/account-takeover-kill-chain.pdf), moving into the exploitation and action phases.


In these last two stages, attackers put the bots aside, roll up their sleeves and take a manual (human) approach to try and compromise individual accounts. The purpose? Well, that depends on what type of account they have compromised. For accounts that have digital wallets, they will be performing the process of money-muling, which involves extracting that money from the digital account and transferring it to themselves in some untraceable way.


For accounts that have loyalty points or digital assets of some kind, the process is similar: get the value from the account you’ve taken over and monetize it for yourself. Europol [reports](https://www.europol.europa.eu/crime-areas-and-trends/crime-areas/forgery-of-money-and-means-of-payment/money-muling) [that 90 percent](https://www.europol.europa.eu/crime-areas-and-trends/crime-areas/forgery-of-money-and-means-of-payment/money-muling) of the money-muling they see is attributed to cybercrime.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


So what typically happens next, before the money-muling begins? Criminals take the validated combo-lists and start logging in to the targeted accounts. In some cases, they’ll get access to the account because, after all, the credential-stuffing effort already demonstrated that the credentials were valid. However, traditional indicators of compromise (IOCs) might trigger the manual fraud alarm bells, like recent changes to shipping and/or email addresses.


Or, perhaps the fraud team notices that multiple accounts across the targeted organization suddenly all have the same shipping address. In these cases, bad actors get challenged with secondary/step-up authentication requests from the website. It could be a security question, a code sent to the mobile phone listed in the account profile, or other challenge.


PayPal: An Example of the Exploitation and Action Phase
-------------------------------------------------------


Let’s imagine that the attacker tries to access a PayPal account with the legitimate owner’s username and password. But because something about the login is different, PayPal decides to direct the attacker to a screen requesting a one-time password validation. These challenges may be enough to ward off many account-takeover attempts. However, if the target account is high profile or lucrative enough, the attacker may go the extra mile to circumvent the organization’s fraud controls and challenges.


And while the attacker didn’t necessarily gain access to the account this time, knowing which authentication controls that an organization has in place is invaluable information to the criminal who can now adjust tactics and techniques.


Continuing with the PayPal example, let’s say PayPal sends a response that a one-time password will be texted to the account owner’s phone number on record, with the screen displaying the last four digits of that number. By way of a quick Google search, the attacker can now easily uncover the full phone number of the individual and determine the associated cell phone carrier.


Now, with various legitimate pieces of personal information on the potential victim on hand, the criminal could attempt to social-engineer the carrier’s customer service agent to conduct [a SIM swap](https://threatpost.com/mobile-customer-service-sim-swap-fraud/151993/) and have another cell phone activated with the number tied to the targeted individual’s PayPal account. Motivated by large upsides, attackers will put skin in the [money-muling](https://www.fbi.gov/scams-and-safety/common-scams-and-crimes/money-mules#:~:text=A%20money%20mule%20is%20someone,on%20behalf%20of%20someone%20else.&text=Money%20mules%20can%20move%20funds,cards%2C%20or%20money%20service%20businesses.) game to maximize their chances of handsome ATO payouts.


**Issues with Asymmetric Detection**
------------------------------------


To increase the fidelity of stopping manual fraudsters, we are seeing some security technologies deploy asymmetric detection capabilities to stop would-be ATO attackers at the moment of login. While the threat actor may still be using accurate usernames and passwords, account protection technology looks for particular signals and assesses associated risk profiles in real time to determine whether to authenticate the user – all without alerting the attacker they have triggered this score and represent an anomaly.


This account-protection technology builds a dynamic profile of the valid user based on characteristics that can’t easily be guessed or mimicked by the attacker. For example, user and population profiling captures various information about the device that can be compared to a database of valid fingerprints. If the attacker claims to be coming from an iOS device with software version 14.2 but sends headers of an older web browser, this could be a trigger to suspect something is wrong.


But — attackers have been getting better at emulating these devices without error so we need to be looking at something the attackers can not easily emulate.


**Monitoring for Real Human Behavior**
--------------------------------------


One idea is to create a database of what “real users” or more importantly “valid account owners” look like when they connect. For instance, what device they last came from when they successfully logged in, or what ISP they’re using when they commonly connect from home. These kinds of signals are more specific to the actual account owners that would be much more difficult for the attacker to try and emulate on their own.


As an example, if the legitimate account owner logged in from a Texas IP address 15 minutes ago, it would be improbable that the same legitimate user logged in an hour later from a residential IP block in Maine. (This might trigger the “improbable travel” risk score.) The conflicting physical IP addresses associated with the login attempt would trigger an appropriate response based on a real-time risk score.


Of course, they could also be employing a VPN so many different signals like this need to be evaluated at the time of login.


Even so, by creating a risk-based view of how similar the current login request looks to what the known good user looked like the last few times they’ve logged in provides additional insights into the questions “Is this really Tony Lauro logging in, or someone else using his credentials?”


By evaluating these known traits sampled from the real Tony Lauro, it allows more accurate options available if a fraudster is detected such as step-up authentication, one-time password (OTP) challenges, blocking or simply tag the request with its associated risk score to be passed onto the companies fraud team where they can have further fidelity into what their tools are doing to detect imposters and stop them before they take over customer accounts.


And that’s the good news in the fight against ATO risks. We don’t have to accept that direct fraud will happen. Taking steps to stop the ATO attacks earlier in the kill chain can help both clients and consumers interact more safely online.


**This is Part II of a two-part blog series taking readers inside the criminal enterprise that is account-takeover fraud. For part I, please [click here](https://threatpost.com/underground-economy-account-takeovers/169032/).**


***Tony Lauro is director of security technology and strategy at Akamai.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[ATO]] [[PayPal]] [[account-takeover]] [[accounts.]] [[money-muling]] [[one-time]] [[example,]] [[IP]] [[ThreatPost]]
