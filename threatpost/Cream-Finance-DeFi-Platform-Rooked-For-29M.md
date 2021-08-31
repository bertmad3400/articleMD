# Cream Finance DeFi Platform Rooked For $29M
### Cream is latest DeFi platform to get fleeced in rash of attacks.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169077)
+ Date: August 31, 2021  4:33 pm
+ Author: Becky Bracken


## Article:
Cream Finance is the latest decentralized finance (DeFi) platform for cryptocurrency trading to take a major financial hit at the hands of hackers, losing nearly $19 million in an attack this week on its “flash loan” feature.


The attacker was able to steal nearly $29 million before being discovered, 418,311,571 in Amp Coin and 1,308.09 in Ethereum cryptocurrency, Cream Finance confirmed.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“We have stopped the exploit by pausing supply and borrow on AMP,” the company statement said. “No other markets were affected.”



DeFi platforms connect various cryptocurrency blockchains to create a decentralized infrastructure for borrowing, trading and other transactions.


**Cream Finance Hit With Reentry Attack**
-----------------------------------------


According to researchers at PeckShield, a bug in the feature allowed the threat actors to pull off a “reentry attack,” which allows funds to be borrowed on a loop, repeatedly, while the previous transaction is being processed.


“The hack is made possible due to a reentrancy bug introduced by $AMP, which is an ERC777-like token and exploited to re-borrow assets during its transfer, before updating its first borrow,” PeckShield explained.



The attack on Cream Finance comes just days after [Poly Networks suffered a $610 million theft](https://threatpost.com/crypto-hack-600-million/168554/), the largest DeFi breach in history, before the [money was returned by the attacker](https://threatpost.com/poly-network-recoups-610m-stolen-from-defi-platform/168906/) in a weird twist, likely after the criminal figured out that stealing the crypto is easier than making a withdrawal.


**Solidity Leaves Plenty of Room for Error**
--------------------------------------------


The complexity of implementing Solidity coding language used to create DeFi “smart contracts” on a variety of blockchain platforms leaves plenty of room of coding errors, and opportunity for attackers, Joe Stewart with PhishLabs told Threatpost. An error in smart-contract coding is what enabled the Cream Finance reentry attack, Stewart said.


“The recent security breach of the Cream Finance platform was facilitated by the latest in a long chain of smart contract vulnerabilities introduced by human error (or possibly insider attacks),” Stewart said. “Because Solidity is an evolving language, it is very easy to shoot yourself in the foot by something as simple as failing to include the correct function modifier in your code – exactly what happened to the author of the Cream Finance smart contract.”


The layers of complexity are made even more tricky once those DeFi smart contracts start interacting with others,” Stewart added.


“The increasing complexity of DeFi contracts that interact with one another (possibly even across different blockchains) make it difficult to predict all possible code paths that could lead to privilege escalation and loss of funds locked in the contract,” Stewart added. “This is what happened in the recent PolyNetwork hack resulting in $610M being stolen (although subsequently returned by the hacker).”


Tal Be’ery, co-founder of ZenGo, pointed out via tweet that in both the attacks on both Cream and Poly Networks, the threat actors wouldn’t have been able to test their various exploits in a lab environment, they were likely poking around for some time in the systems looking for a hole.


**Attackers Sharpening Tools, Attacks**
---------------------------------------


“The attackers had to develop and test their exploits against a real chain, because it’s too complex to set up in a lab,” Be’ery explained. “A good monitoring (and) alert solution might have given enough time to fix.”



As DeFi platforms figure out how to shore up security, Karl Steinkamp with Coalfire warned that threat actors, motivated by volatile crypto-bubbles, are working overtime to refine attacks.


“Given the generally appreciating value of crypto-assets, bad actors will likely continue to use them for many more years into the future,” Steinkamp told Threatpost. “While it has been seen currently to a limited extent over the last 10 years, bad cybercriminals will need to get smarter in using blockchains and crypto if they are going to be successful, which will likely include mixing tools and more off-chain and/or hardware addressed wallets.”


And the most recent data shows [DeFi platforms](https://atlasvpn.com/blog/defi-related-hacks-account-for-76-of-all-major-hacks-in-2021) were on the receiving end of 76 percent of all major hacks in 2021 and even before the Poly Networks hack, losses for 2021 had already exploded by 180 percent over last year, according to Atlas VPN.


With rising risk of theft, its going to be up to the DeFi platforms themselves and larger cryptocurrency community to offer some reassurance it’s safe.


“The crypto-industry has generated a lot of excitement; however, many newcomers are unaware of the risks,” Atlas VPN’s researchers said. “Lack of regulation in the crypto-industry allows cybercriminals to thrive either by hacking less secured DeFi projects or by carrying out rug pull scams. For DeFi to become more legitimate, it is essential to establish security and business regulations.”


In the meantime, KnowBe4’s James McQuiggan suggested that users concerned about security should keep their cryptocurrency stored offline.


“Whether reverse-engineering the cryptography or attacking the source, cybercriminals continue to find ways to circumvent controls to steal money for their financial gain and ruin the customers’ portfolios,” McQuiggan said. “It demonstrates that users should maintain offline wallets to protect a large portion of their investments versus having them all in one location and risk losing their entire investment through a data breach or attack.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[said.]] [[“The]] [[cybercriminals]] [[ThreatPost]]
