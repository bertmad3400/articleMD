# OpenSea ‘Free Gift’ NFTs Drain Cryptowallet Balances
### Cybercriminals exploited bugs in the world’s largest digital-goods marketplace to create malicious artwork offered as a perk to unsuspecting users.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175453)
+ Date: October 13, 2021  9:04 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/13090321/nft-e1634130217291.png)
Users of OpenSea, the world’s largest digital-collectible marketplace, have found their cryptocurrency wallets ripped off thanks to cyberattackers weaponizing security bugs that allowed them to highjack user accounts. The attacks revolved around boobytrapped art files, which circulated in the form of “free gifts.”


That’s according to Check Point Research, whose researchers looked into a series of claims that cryptocurrency balances were going *poof* for both market shoppers and merchants.


OpenSea is a peer-to-peer marketplace for virtual goods – a bit like the Etsy of non-fungible tokens (NFTs) and crypto collectibles. NFTs are a way to take reproduceable digital items such as photos, videos, audio and art files, and turn them into unique items; marketplaces use blockchain technology to establish a verified and public proof of ownership for such items. OpenSea has benefitted from the [NFT boom](https://www.rfi.fr/en/culture/20210312-digital-nft-artwork-sold-for-record-69-3-million-rocks-the-art-world-united-states-beeple-non-fungible-token), racking up $3.4 billion in transaction volume [just in August](https://www.yahoo.com/now/opensea-trading-volume-breaches-3bn-133114338.html).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Cybercriminals are of course drawn to such money hubs [like moths to a flame](https://threatpost.com/nft-collector-tricked-into-buying-fake-banksy/169179/) – and they have been true to form with OpenSea, according to Check Point.


To uncover how the wallet-draining attacks were carried out, researchers focused on reports that they began with a target being offered a free NFT gift or a link to OpenSea Art. For instance, one victim confirmed to CPR that he interacted with an airdropped NFT object prior to the wallet theft.


“So, we decided to check what will happened if we would create malicious art that contains code in it, for example an .SVG image. We created a simple .SVG file and uploaded it with a simple payload,” researchers explained in a [Wednesday analysis](https://research.checkpoint.com/2021/check-point-research-prevents-theft-of-crypto-wallets-on-opensea-the-worlds-largest-nft-marketplace/). “By clicking on the art and opening it in anther tab or clicking on the links on the page, our SVG will be executed under https://storage.opensea.io subdomain; at this point, we have a SVG file with JavaScript capabilities.”


In order to have the “artwork” steal cryptocurrency however, Check Point’s proof of concept needed a few more bells and whistles.


**Delivering Weaponized NFT Art**
---------------------------------


Diving deeper, the researchers found that a user is required to connect a third-party crypto wallet to an account at OpenSea, to pay for collectibles and receive payment for any offerings one puts up for sale. The way the platform works is by communicating with the wallet for almost every account action, such as uploading art. In turn, the wallet is communicating with its back-end cryptocurrency network. In Check Point’s research, the analysts used the MetaMask wallet, which communicates to the Ethereum network by using the JSON-RPC API.


To exploit this setup, the researchers added an iframe to the .SVG file, which inserted an Ethereum object onto the page where the malicious .SVG was on offer.


“This way we can get the window.ethereum injected, which will allow us to communicate with the Ethereum JSON-RPC API,” according to the analysis. “In order to hijack the currencies, first the attacker needs to open a communication with the wallet via a rpc-api action that will start the communication with MetaMask.”


When a target is offered the “free gift” – i.e., the malicious NFT – a pop-up window appears to the target asking for confirmation for the transaction. Once the victim clicks on the popup to sign the transaction, he or she can interact with the file. In the background, the payload executes and an attacker would be able to see any wallet activity and be able to perform actions on the victim’s behalf.


“The transfer will happen seamlessly, and the victim will get the art to his collection without any action needed from his side,” Check Point researchers explained. “Then if the victim will open the new art and press the image or links, connect his wallet and sign the transaction in the popup, he will lose all his balance.”


**How to Protect Against NFT-Related Cyberattacks**
---------------------------------------------------


Check Point researchers disclosed the vulnerabilities to OpenSea, who has implemented fixes – but they warned that attacks like this will not likely be uncommon. A main key to protecting oneself, they said, is to pay close attention to any wallet messages and popups.


“It should be noted that wallet signature popups often appear as a system notice, and are a standard platform process to create several activities,” researchers noted – these popups usually appear when users are buying an item or making an offer, for example. However, they pointed out that being asked to sign with the wallet after clicking an image received from a third party is not usual.


“Users should note that OpenSea does not request wallet approval for viewing or clicking third-party links,” according to Check Point. “Such activity is highly suspicious and users should not interact with wallet approvals that are unrelated to OpenSea specific actions such as buying, making an offer, liking an image.”


Thus, before approving a request, users should carefully review what’s being requested and consider whether the request is abnormal or suspicious.


“In this instance, the user could have unknowingly enabled access to their account (and the money in it) based on the same known process if they do not carefully read the popup,” researchers said. “Users should be hyper-aware of what they sign on OpenSea, as well as other NFT platforms, and whether it correlates with expected actions.”


***Check out our free***[***upcoming live and on-demand online***](https://threatpost.com/category/webinars/) ***town halls*** ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[NFT]] [[OpenSea,]] [[OpenSea]] [[.SVG]] [[Ethereum]] [[ThreatPost]]
