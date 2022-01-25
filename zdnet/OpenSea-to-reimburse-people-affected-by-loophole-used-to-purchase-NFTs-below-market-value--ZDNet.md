# OpenSea to reimburse people affected by loophole used to purchase NFTs below market value | ZDNet
### Elliptic said it has identified at least three people making more than $1 million off of NFTs being sold for a fraction of what they're worth.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/opensea-reimbursing-people-affected-by-bug-used-to-purchase-nfts-below-market-value/
+ Date: 2022-01-25 01:41:11
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/01c58e0ad04e30160eeb407218f71408632ef5fe/2022/01/21/968b39f9-3c62-49f2-b739-ff3567d9c131/nft-1.jpg?width=770&height=578&fit=crop&auto=webp)

OpenSea is contacting and reimbursing users affected by a loophole that allows people to buy NFTs for a fraction of their true cost and resell it for thousands.

On Monday, blockchain security company [Elliptic](https://www.elliptic.co/blog/bug-allows-nfts-worth-over-1-million-to-be-stolen) and [multiple Twitter users](https://twitter.com/yakirrotem/status/1485559864948629512) spoke out about the bug. [Motherboard](https://www.vice.com/en/article/y3vnzw/scammers-exploit-opensea-flaw-to-buy-nfts-at-rock-bottom-prices) was the first to report on the incident. 

Elliptic said it "identified at least three attackers who have purchased at least eight NFTs for much less than their market value within the past 12 hours." The issue affects Bored Ape Yacht Club, Mutant Ape Yacht Club, Cool Cats and Cyberkongz NFTs.

One user wrote on Twitter that [his NFT](https://opensea.io/assets/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/9991) was bought for about $1,800 worth of the Ethereum cryptocurrency before it was resold for $196,000.




> Yooo guys! Idk what just happened by why did my ape just sell for .77?????
> 
> — TBALLER.eth (@T\_BALLER6) [January 24, 2022](https://twitter.com/T_BALLER6/status/1485523314621632514?ref_src=twsrc%5Etfw)




 window.ZdnetFunctions.logWithLabel('%c One Trust ', "Service loaded: script\_twitterwidgets with class optanon-category-5");
 
"One attacker, going by the pseudonym 'jpegdegenlove' today paid a total of $133,000 for seven NFTs -- before quickly selling them on for $934,000 in ether. Five hours later this ether was sent through Tornado Cash, a 'mixing' service that is used to prevent blockchain tracing of funds. Jpegdegenlove also seems to have partially compensated two of their victims -- sending 20 ETH ($45,000) to TBALLER and 13 ETH ($30,000) to Vault327. Another attacker purchased a single Mutant Ape Yacht Club NFT for $10,600, before selling it on five hours later for $34,800," Elliptic explained.

"The [exploit](https://twitter.com/yakirrotem/status/1485559864948629512) appears to originate from the ability to re-list an NFT at a new price, without cancelling the previous listing. Those previous listings are now being used to purchase NFTs at prices specified at some point in the past -- which is often well below current market prices."

DeFi developer Rotem Yakir [released](https://twitter.com/yakirrotem/status/1485559864948629512) a detailed thread on Twitter explaining the OpenSea bug, writing that it "stems from the fact that previously you could re-list an NFT without canceling it (which you can't now) and all the previous listing are not canceled on-chain."






"Previously, you could have re-list an NFT without canceling the previous list. Sometimes but not always, If you cancel your new listing, the old one will not appear on the UI but is still valid," Yakir said. 

"Using services like [https://orders.rarible.com](https://t.co/vY98JCm6sj) or even OS API someone can obtain the old listing and still use it. To make sure you are safe, you can check on [https://orders.rarible.com](https://t.co/vY98JCm6sj) and see if your previous listing is still there. However, if you want to be 100% safe then just transfer your NFT to a different wallet."

An OpenSea spokesperson told *ZDNet* that it has been trying to create solutions for the problem since it was identified. They also denied that it was a bug or vulnerability.

"Since this issue was identified, we've taken it incredibly seriously and worked to ship product solutions for the community. This is not an exploit or a bug -- it's an issue that arises because of the nature of the blockchain. OpenSea cannot cancel listings on behalf of users. Instead, users must cancel their own listings," the spokesperson said. 

"It's OpenSea's priority to make users aware of all their listings, and we're working on a number of product improvements to address this, including a dashboard where they can easily see and cancel listings. In addition, we have been actively reaching out to and reimbursing affected users. We have not communicated broadly about this issue because we did not want to risk bringing it to the attention of bad actors who could abuse it at scale before we had mitigations in place." 

*ZDNet* could not confirm whether users have been reimbursed. The OpenSea spokesperson said that it's an issue of "confusing UI" that arises when users create listings and then transfer the listed NFT to a different wallet. 

When a user transfers items out of their third-party wallet, the listing they created for the item does not automatically cancel and cannot be canceled by OpenSea directly because it requires the user to sign for the cancellation in their wallet, the spokesperson explained. OpenSea is not the only platform affected by the issue, the NFT platform explained. 

According to OpenSea, the issue can arise any time a user moves an NFT to a different wallet without canceling active listings because the transaction is posted to the blockchain.

The company added that it is in the process of changing its default listing duration from 6 months to 1 month so that if an NFT is transferred back into a wallet after 1 month, the listing will have expired.

They also plan to notify users that they have a higher-priced listing still active when they lower the price for the same item. OpenSea said it is adding a dashboard to user profiles that shows all inactive listings and gives users an opportunity to cancel each listing with a single click.

In the next two days, the company plans to integrate another feature that will surface in-product notifications about active listings and ask if users want to cancel it when they transfer an NFT that has an active listing associated with it out of their wallet. Users will also get an email from OpenSea when they transfer an NFT into a wallet with an active listing for that NFT.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Nft]] [[Opensea]] [[Nfts]] [[Blockchain]] [[Re-list]] [[ZDNet]]
#### urls
https://orders.rarible.com

