# Wormhole restores stolen $326 million after major crypto bailout
### Cryptocurrency platform Wormhole has recovered upwards of $326 million stolen in this week's crypto hack, thanks to a major bailout.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/wormhole-restores-stolen-326-million-after-major-crypto-bailout/
+ Date: 2022-02-04T05:09:21-05:00
+ Author: Ax Sharma


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/06/02/ethereum-header.jpg)

![ethereum](https://www.bleepstatic.com/content/hl-images/2021/06/02/ethereum-header.jpg)


Cryptocurrency platform Wormhole has recovered upwards of $326 million stolen in this week's crypto hack, thanks to a major bailout.


Being a cross-chain crypto platform, Wormhole allows users to transfer cryptocurrency across different blockchains, such as Ethereum, Solana, and Binance Smart Chain, among others.


It does this by locking the original token in a smart contract and then minting a "wrapped" version of the stored token that can be transferred to another blockchain.


Wormhole rescued by VC firm in $326 million hack
------------------------------------------------


Wormhole has announced a successful recovery of all funds stolen in [this week's $326 million hack](https://www.bleepingcomputer.com/news/cryptocurrency/wormhole-cryptocurrency-platform-hacked-to-steal-326-million/), and the crypto platform is back up.


Sharing a timeline of the incident, the company states a detailed incident report will follow:



> 
> The team is working on a detailed incident report and will share it asap  
>   
> 
> 18:26 UTC - contract was exploited for 120k ETH  
>   
> 
> 00:33 UTC - vulnerability was patched  
>   
> 
> 13:08 UTC - ETH contract has been filled and all wETH are backed 1:1  
>   
> 
> 13:29 UTC - the Portal (token bridge) is back up
> 
> 
> — Wormhole (@wormholecrypto) [February 3, 2022](https://twitter.com/wormholecrypto/status/1489233259808571401?ref_src=twsrc%5Etfw)


On February 2nd, Wormhole had announced a temporary shut down of its crypto platform as it investigated an exploit on their network.


The same day, the company [confirmed](https://twitter.com/wormholecrypto/status/1489001949881978883) that Wormhole's network had indeed been exploited for 120,000 wrapped Ethereums (wETH) and they were working on restoring the lost funds.


Blockchain analytics company, Elliptic [had previously revealed](https://www.elliptic.co/blog/325-million-stolen-from-wormhole-defi-service) that Wormhole attempted to offer the attacker a $10 million bug bounty—should the latter agree to return the stolen funds. But, the effort failed to reach fruition, with over $265 million worth of ETH still remaining in the [attacker's wallet](https://etherscan.io/address/0x629e7da20197a5429d30da36e77d06cdf796b71a), as seen by BleepingComputer today.


Granted, the company has now restored the lost Ethereum, the funds didn't appear out of thin air.


Wormhole's bailout from this loss was made possible by industry partner, [Jump Crypto](https://jumpcrypto.com/introducing-jump-crypto/), part of the [Jump Trading Group](https://en.wikipedia.org/wiki/Jump_Trading) that also owns the venture capital (VC) firm, Jump Capital.


"[Jump Crypto] believes in a multichain future and that [Wormhole] is essential infrastructure," [says](https://twitter.com/JumpCryptoHQ/status/1489301013408497666) the company. "That's why we replaced 120k ETH to make community members whole and support Wormhole now as it continues to develop."


Vulnerability hiding in plain sight?
------------------------------------


Not much info has been given out by Wormhole just yet as to how attackers managed to steal the funds, or the nature of the vulnerability exploit.


Analysis of illicit transactions by renowned cryptocurrency security researcher *[Samczsun](https://cointelegraph.com/top-people-in-crypto-and-blockchain-2021/samczsun)* revealed that Wormhole wasn't properly validating all input accounts on its platform.


This enabled attackers to spoof "guardian" signatures and mint 120,000 ETH on the Solana blockchain out of thin air. Out of these funds, attackers were able to bridge 93,750 back to Ethereum, [according to](https://twitter.com/samczsun/status/1489044999211823107) the researcher.


*Samczsun* specifically pointed out the flaw existed in the 'verify\_signatures' function which is designed to "take a set of signatures provided by the guardians and pack it into a `SignatureSet`." But, the researcher [explains](https://twitter.com/samczsun/status/1489044979087515654), the function failed to conduct any of the verification checks.


Another researcher *[smartcontracts](https://twitter.com/kelvinfichter/status/1489050921938132996)*analyzed the GitHub commit history for the Wormhole open source project and revealedthat the code changes supposedly fixing the bug were pushed to the repository about **nine hours before** the hack took place:



![Changes made to verify_signatures functiona](https://www.bleepstatic.com/images/news/u/1164866/2022/Feb-2022/wormhole-recovers-funds/verify-signature-function.jpeg)**Changes made to 'verify\_signatures' function in Solana bridge just hours before the Wormhole hack**(GitHub)
"Possible that an attacker was keeping an eye on the repository and looking out for suspicious commits," says the researcher.


Interestingly, *smartcontracts* also [concludes](https://twitter.com/kelvinfichter/status/1489089952164069376) that the code change wasn't a deliberate bug patch—it was likely rolled out inadvertently by Wormhole developers looking to simply [bump up their Solana dependency version](https://github.com/certusone/wormhole/pull/751).


Public knowledge of pending security updates or outdated dependencies that are yet to be replaced (e.g. through a GitHub pull request) can give sharp-eyed adversaries a heads up, leading to exploitation of these flaws before they are patched.


In Wormhole's case, the pull request to update the platform's Solana version had been open since January 13th, as seen by BleepingComputer. But, the actual source code changes in GitHub took place on February 1st—hours before the attack on production systems.


In recent times, cryptocurrency exchanges and DeFi protocols have become popular targets of threat actors.


Last month, cryptocurrency exchange Crypto.com suffered a [$34 million hack](https://www.bleepingcomputer.com/news/security/483-cryptocom-accounts-compromised-in-34-million-hack/) in which 483 of its customer accounts were affected. The same month DeFi platform Qubit Finance also faced an [$80 million loss](https://cointelegraph.com/news/qubit-finance-suffers-80-million-loss-following-hack) from a cyber attack.





## Tags:

#### Action:
[[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Solana]] [[Utc]] [[Ethereum]] [[Github]] [[Bleeping Computer]]

