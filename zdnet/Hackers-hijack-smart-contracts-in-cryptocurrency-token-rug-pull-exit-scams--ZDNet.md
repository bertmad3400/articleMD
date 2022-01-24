# Hackers hijack smart contracts in cryptocurrency token 'rug pull' exit scams | ZDNet
### Misconfiguration provides the perfect opportunity for token-based theft.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/hackers-hijack-smart-contracts-in-new-cryptocurrency-token-rug-pull-scams/
+ Date: 2022-01-24 09:06:37
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/2271ef902266baeee69e832e2e10f13be07ab0bb/2019/01/23/ea1e5dd9-47ff-4ef1-bdc1-4cc05b9b1126/istock-cryptocurrency-coins.jpg?width=770&height=578&fit=crop&auto=webp)

Hackers are abusing misconfigurations in smart contracts to launch token rug pulls, researchers say. 


Despite the current volatility in the cryptocurrency market, with prices for many popular coins including Bitcoin (BTC) plunging, interest in the crypto, token, and NFT spaces remains stable. 

2021 was a record-breaking year for cryptocurrency-related theft and fraud. Cybercriminals netted an estimated $14 billion in cryptocurrency and fraudulent schemes involving digital assets continue to evolve. 

On Monday, Check Point Research (CPR) said that scammers are now turning their attention [to smart contracts](https://research.checkpoint.com/2022/scammers-are-creating-new-fraudulent-crypto-tokens-and-misconfiguring-smart-contracts-to-steal-funds/), with misconfigurations utilized to launch new crypto tokens -- before an inevitable "rug pull" takes place.  

Rug pulls occur when developers of a crypto or virtual asset project manipulate a token's perceived worth and then abandon the project – taking investor funds with them. 

A recent example is the [SQUID token](https://www.zdnet.com/article/squid-game-cryptocurrency-creators-pull-the-rug-from-under-investors-steal-millions/) which, at its peak, saw the token reach $2,850 in value. Once the developers rug pulled and prevented traders from selling, the coin crashed by over 99.99%, rendering it basically worthless while netting the developers millions of dollars.  

There are some indicators of a potential token scam, including 99% buy fees and mechanisms that prevent investors from reselling. According to the researchers, flaws in smart contract code and vulnerabilities can also be harnessed by external attackers to increase the risk of a project losing investor money.






Fraudsters employ a range of tactics to conduct a rug pull including the use of scam services to create smart contracts which are then issued a new token name and symbol before becoming public. The manipulation of functions to create hidden triggers to launch a rug pull may also be included. 

Social media networks are then used to hype up a token -- and its perceived value -- before an exit scam occurs. In addition, timelocks are not usually imposed.  

"Timelocks are mostly used to delay administrative actions and are generally considered a strong indicator that a project is legitimate," the researchers noted.  

Buy and sell fees are a common technique for rug pulls. In a smart contract examined by CPR, the firm discovered both "approve" and "aprove" functions. The former was a legitimate, standard function for contract transactions, whereas "aprove" was hidden and designed to allow the developers to impose 99% fees after a project took off.  

"A legitimate token will not charge fees or will charge hardcoded values that can't be adjusted by the developer," CPR says.  

Another example of potential scam mechanisms is a hidden function that allows developers to create more coins or control who can sell tokens. In the source code of a basketball-themed smart contract, the team found a transfer function that prevented reselling by average traders -- a similar element used by SQUID.  

A function found in a separate contract that allowed coin minting was exploited by an attacker after the contract's private key was accidentally leaked online. A threat actor was able to use the key to fraudulently mint millions of virtual coins before withdrawing them. In the same contract, an error in emergency withdrawal functions was also exploited. 

Attackers may also burn tokens to ramp up the price of existing pools. A failure to limit external burns in the [Zenon Network](https://halborn.com/explained-the-zenon-network-hack-november-2021/) was exploited in 2021, leading to a pool drain and the theft of over $814,000 from the project.  

"It's hard to ignore the appeal of crypto," CPR says. "It's a shiny new thing that promises to change the world, and if prices continue on their upward trajectory, people have an opportunity to win a significant amount of money. However, cryptocurrency is a volatile market. Scammers will always find new ways to steal your money using cryptocurrency." 

###  Previous and related coverage

* [Amazon fake crypto token investment scam steals Bitcoin from victims](https://www.zdnet.com/article/amazon-fake-crypto-token-investment-scam-steals-bitcoin-from-victims/)
* [Cryptocurrency scams pose largest threat to investors](https://www.zdnet.com/article/cryptocurrency-scams-pose-largest-threat-to-investors/)
* [2020's worst cryptocurrency breaches, thefts, and exit scams](https://www.zdnet.com/article/2020s-worst-cryptocurrency-breaches-thefts-and-exit-scams/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=HTTPBrowser]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cpr]] [[ZDNet]]

