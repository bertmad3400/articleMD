# The Underground Economy: Recon, Weaponization & Delivery for Account Takeovers
### In part one of a two-part series, Akamai’s director of security technology and strategy, Tony Lauro, lays out what orgs need to know to defend against account takeover attacks.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169032)
+ Date: August 30, 2021  3:44 pm
+ Author: Tony Lauro


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/21130321/chrome-password-stealer.jpeg)
With account takeover (ATO) attacks on the rise, stopping threat actors in the [early phases of the](https://www.akamai.com/us/en/multimedia/documents/infographic/account-takeover-kill-chain-infographic.pdf) [kill chain](https://www.akamai.com/us/en/multimedia/documents/infographic/account-takeover-kill-chain-infographic.pdf) will help today’s defenders gain an upper hand against direct fraud campaigns.


Understanding how and where these attacks are carried out and the underlying support structure enabling ATO are key to informing what types of defenses should be deployed to help reduce an organization’s risk – and associated pain – for customer account compromise. Let’s take a closer look at early stages of the kill chain – reconnaissance, weaponization and delivery – to examine how criminals gather leaked credentials, then validate this data to ultimately extract value from accounts they’ve gained access to for monetization.


As is the case with many types of cyberattacks, initial planning – or recon – for ATO starts in what is considered the internet’s underground economy, where threat actors communicate, coordinate and plan their criminal endeavors. It’s important to understand what type of activity and processes take place here to give more context for criminal motivations and help explain why ATO attacks are becoming commonplace.


As a quick refresher, many may not know that the Surface Web, what we consider the public internet (indexed by search engines), only makes up about 4 percent of the total volume of the internet. What is commonly called the Dark Web makes up roughly 6 percent of the internet. So what about the remaining unaccounted for 90 percent? The vast majority of the total internet consists of the Deep Web and is not indexed, as the data sits behind a protected database or service that requires a user login to access information. Credential gathering, data sharing and recon – the beginning of the ATO kill chain – starts here.


**Credential gathering is the first phase.** Attackers breach or skim sites, phish website users or purchase combo-lists of stolen credentials on the Dark Web. Oftentimes these lists of usernames and passwords have been exposed during a data breach. [Pastebin](https://pastebin.com/), [ControlC](https://controlc.com/), [Combo-lists.com](https://combo-list.com/) and [ZeroBin.net](https://zerobin.net/) are examples of underground economy sites for attackers to find combo-lists.


Also, tools have actually been written to help facilitate the process for criminals. One such tool, D3vSpider, was written so that attackers can more easily search Pastebin to look for a username/password combinations; email/password combinations or proxy lists; or email addresses and URLs that might be interesting to target.


If the acquired combo-lists have recently been publicly leaked to sites, it’s important for attackers to quickly validate those credentials before knowledge of a public security breach puts password reset and other post-compromise security mechanisms into action. If a data breach has occurred, but is not yet made public, attackers can buy a list of credentials that have already been validated. And because the breach is still not yet publicly known, it’s less likely that the targeted company has taken any post-breach actions, nor have consumers been alerted to reset their passwords.


Once criminal actors have combo-lists in hand, they will then move into the second stage of the ATO kill chain.


**The second stage is weaponization.** During this phase and the next (delivery), attackers rely heavily on automation by building or renting botnets to scale credential-stuffing attacks against the target’s website to validate which credentials work. However, attackers can’t just directly launch into delivery.


First, they load the acquired combo-list into the botnet. Then, to increase their chances of a successful attack, they need to implement some botnet obfuscation techniques by either using proxy networks or bot nodes to make sure their activity is not easily identified. When an attacker is using common botnet attack tools like [Snipr](https://blogs.akamai.com/2018/03/what-you-need-to-know-snipr-credential-stuffing-tool.html) or [Sentry MBA](https://blogs.akamai.com/2020/06/mitigating-credential-stuffing-attacks-in-the-financial-sector.html), they need to look like they are real users to evade detection.


As an example, attackers who are targeting U.S.-based companies no longer launch attacks from out-of-country IP addresses, because that would be too obvious and easily flagged as suspicious account activity.


Instead, they attempt to look like they’re coming from in-country cloud providers and data center IP addresses. But enterprise defenders realized that “actual” users don’t typically access sites from data center IP addresses; instead, legitimate users are more likely to come from ISP-based IP addresses (think residential). Attackers saw that they were getting detected and have pivoted to using proxy services or bot nodes that are proxied through compromised IoT devices located on home networks. Many nefarious proxy services are even advertised on Twitter, noting that they specialize in allowing access through proxies with residential IP addresses.


**Next, it’s time for  the delivery phase of the kill chain.** With obfuscation techniques in place and combo-lists locked and loaded into botnet tools, attackers are ready to launch a credential-stuffing attack.


Here’s an overview of how that attack might play out.


The credential-stuffing attack can be volumetric, trying to log in from a few devices and testing thousands of credentials per second. Or the attack can be “low and slow,” using more devices and fewer requests per second in hopes of avoiding detection. But each attempted login by the botnet works the same way to try and validate the account.


The botnet uses the usernames and passwords to see if the site lets the attacker in, thinking it’s the account owner. Maybe the login attempt fails, as many attempts will. For example, perhaps the legitimate owner of the credentials doesn’t have a PayPal account. Maybe they changed their password recently. Or likely the site is protected with some kind of challenge action or step-up authentication via email or text to prove the account owner’s identity.


But some stolen credentials will work, and the attackers only need a small percentage of their list to be validated for the attack to be financially successful. The process continues until the attacker has tested all the credentials in the combo-list. Keep in mind that attackers might execute the account-takeover attack themselves, but it’s also very common for criminals to sell validated credentials to another criminal group operating within the internet’s underground economy.


Now with valid credentials, the attacker will be ready to move onto the next phases of the ATO kill chain – where human driven intervention completes the final stages of a direct fraud campaign. In part II of this blog series, we’ll examine the tactics and techniques of human fraudsters performing targeted attacks against individual user accounts and how organizations can be better prepared to fight back.


Stay tuned for Part II, next week!


***Tony Lauro is director of security technology and strategy at Akamai.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[ATO]] [[it’s]] [[botnet]] [[IP]] [[combo-lists]] [[credential-stuffing]] [[ThreatPost]]
