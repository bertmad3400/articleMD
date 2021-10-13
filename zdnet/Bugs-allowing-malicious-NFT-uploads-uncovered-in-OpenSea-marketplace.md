# Bugs allowing malicious NFT uploads uncovered in OpenSea marketplace
### Malicious NFTs could have become an attack vector for hackers trying to steal digital wallet funds.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/bugs-allowing-malicious-nft-uploads-uncovered-in-opensea-marketplace/)
+ Date: October 13, 2021
+ Author: Charlie Osborne


## Article:
Unknown

Critical security issues in the OpenSea NFT marketplace that allowed attackers to steal cryptocurrency wallet funds have been patched. 


[NFT](https://www.zdnet.com/article/are-nft-collectibles-the-new-trading-cards-or-a-hype-bubble-soon-to-burst/)s, also known as non-fungible tokens, are digital assets that can be sold and traded on the blockchain. While some NFTs -- from a pixel cartoon to a popular meme -- can reach a sale price of [millions of dollars](https://www.bbc.co.uk/news/technology-56371912), the popularity of this phenomenon has also created a new attack vector for exploitation.  

On Wednesday, the Check Point Research (CPR) [team said](https://blog.checkpoint.com/) that flaws in the OpenSea NFT marketplace could have allowed "hackers to hijack user accounts and steal entire crypto wallets of users, by sending malicious NFTs." 

An investigation was launched after [reports surfaced](https://www.bleepingcomputer.com/news/security/fake-opensea-support-staff-are-stealing-cryptowallets-and-nfts/) of malicious NFTs, airdropped for free, being used as conduits for cryptocurrency theft and account hijacking.  

The NFT itself, and the airdrop, was not the source of the issue. Instead, once an NFT had been gifted to a potential victim, they would view it -- and then a pop-up would trigger, requesting a signature to connect to a wallet. A secondary signature request prompt would then appear, and if accepted, could grant attackers access to an unwitting user's wallet, funds, and more.  

In OpenSea's case, the security flaw allowed the team to upload an .SVG file containing a malicious payload, which would execute under the OpenSea storage subdomain. 

"In our attack scenario, the user is asked to sign with their wallet after clicking an image received from a third party, which is unexpected behavior on OpenSea, since it does not correlate to services provided by the OpenSea platform, like buying an item, making an offer, or favoring an item," CPR says. "However, since the transaction operation domain is from OpenSea itself, and since this is an action the victim usually gets in other NFT operations, it may lead them to approve the connection."






The researchers disclosed their findings to OpenSea on September 26. Within less than an hour, the marketplace had triaged and verified the security issues and deployed a fix.  

In a statement, OpenSea said: 


> "Security is fundamental to OpenSea. We appreciate the CPR team bringing this vulnerability to our attention and collaborating with us as we investigated the matter and implemented a fix within an hour of it being brought to our attention.  
> 
> These attacks would have relied on users approving malicious activity through a third-party wallet provider by connecting their wallet and providing a signature for the malicious transaction." 
> 
> 

OpenSea added that the organization has not found any evidence of exploitation in the wild. 

###  Previous and related coverage

* [Learn all about crypto trading and NFTs in 11 hours of self-paced training for just $30](https://www.zdnet.com/article/learn-all-about-crypto-trading-and-nfts-in-11-hours-of-self-paced-training-for-just-30/)  

* [New platform uses NFTs as a gateway for digital rights management](https://www.zdnet.com/article/new-platform-uses-nfts-as-a-gateway-for-digital-rights-management/)  

* [Kusama introduces 'art legos': Complex programmable NFTs](https://www.zdnet.com/article/kusama-introduces-art-legos-complex-programmable-nfts/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[OpenSea]] [[NFT]] [[NFTs]] [[ZDNet]]
