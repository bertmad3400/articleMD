# OpenSea NFT platform bugs let hackers steal crypto wallets ?
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/opensea-nft-platform-bugs-let-hackers-steal-crypto-wallets-/)
+ Date: October 13, 2021
+ Author: Ionut Ilascu


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/10/13/NFT.jpg)


image credit: [Kerfin7](https://www.freepik.com/vectors/background)


Security researchers found that an attacker could leave OpenSea account owners with an empty cryptocurrency balance by luring them to click on malicious NFT art.


With a transaction volume of $3.4 billion, OpenSea is the world’s largest marketplace for buying, selling, and auctioning non-fungible tokens (NFTs) and other digital assets and collectibles.


Details emerged today about an issue on the OpenSea platform that let hackers hijack user accounts and steal the associated cryptocurrency wallets.


The attack method is as simple as creating an NFT with a malicious payload and waiting for a victim to take the bait and view it.


Multiple users reported empty cryptocurrency wallets after receiving gifts on the OpenSea marketplace, a marketing tactic known as “airdropping” and used to promote new virtual assets.


![Users reporting empty wallets after NFT airdrop](https://www.bleepstatic.com/images/news/u/1100723/2021/NFT_airdrop-hack.jpg)


Enticed by these accounts, researchers at cybersecurity company Check Point decided to take a closer look at how the platform works and check for vulnerabilities.


An OpenSea account requires a third-party cryptocurrency wallet from a list that the platform supports. One of the most popular is MetaMask, which is also what the researchers also chose.


Communication with the wallet occurs for any action in the account, including liking art in the system, which triggers a wallet sign-in request.


![Liking art on OpenSea triggers MetaMask wallet sign in](https://www.bleepstatic.com/images/news/u/1100723/2021/OpenSeaMetamaskSignIn.jpg)


The OpenSea platform lets anyone sell digital art, which can be files as large as 40MB with any of the following extensions: JPG, PNG, GIF, SVG, MP4, WEBM, MP3, WAV, OGG, GLB, GLTF.


Knowing this, Check Point uploaded to the OpenSea system an SVG image that carried malicious JavaScript code. When clicking on it to open in a new tab, they noticed that the file executed under the ‘storage.opensea.io’ subdomain.


They also added an iFrame to the SVG image to load HTML code that would inject the “window.ethereum” required to open communication with the victim’s Ethereum wallet.



“In our attack scenario, the user is asked to sign with their wallet after clicking an image received from a third party, which is unexpected behavior on OpenSea, since it does not correlate to services provided by the OpenSea platform, like buying an item, making an offer, or favoring an item” - [Check Point](https://blog.checkpoint.com/2021/10/13/check-point-software-prevents-theft-of-crypto-wallets-on-opensea-the-worlds-largest-nft-marketplace/)



Abusing the wallet functionality is done through the Ethereum RPC-API, which starts the communication with MetaMask and opens the popup for connecting to the wallet.


An attacker then needed the victim to interact with the legitimate pop-up window so they could perform actions on behalf of the victim.


The researchers note that another signature request popup was required for the hacker to get the cryptocurrency in the wallet.


This would not have been much of a problem, though, since such requests “often appear as a system notice” and users are likely to approve the transaction without reading the message.


![OpenSea NFT triggers popup to connect with MetaMask](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


With a transaction domain from the OpenSea platform and action that victims typically see with other NFT operations, it is easy to see how users could have fallen victims.


In a report today, Check Point researchers summarized the attack as follows:


* Hacker creates and gifts a malicious NFT to a target victim
* Victim views the malicious NFT, triggering a pop-up from OpenSea’s storage domain, requesting connection to the victim’s cryptocurrency wallet
* Victim clicks to connect their wallet and perform the action on the gifted NFT, thus enabling access to the victim’s wallet
* Hacker can get the money in the wallet by triggering an additional pop-up, also sent from OpenSea’s storage domain. The victim is likely to click on the pop-up without reading the note that describes the transaction


Check Point researchers informed OpenSea of their findings on September 26. The two parties collaborated to address the issue and OpenSea came up with a solution in less than an hour from the responsible disclosure.


OpenSea says that they could not identify any cases where attackers exploited this vulnerability but continue to raise awareness and educate the community on the best security practices and how to spot scams and phishing attempts.




#### Tags:
[[OpenSea]] [[NFT]] [[victim’s]] [[wallet.]] [[pop-up]] [[Bleeping Computer]]
