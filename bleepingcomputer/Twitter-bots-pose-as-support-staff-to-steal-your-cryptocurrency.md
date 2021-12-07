# Twitter bots pose as support staff to steal your cryptocurrency
### Scammers monitor every tweet containing requests for support on MetaMask, TrustWallet, and other popular crypto wallets, and respond to them with scam links in just seconds.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/twitter-bots-pose-as-support-staff-to-steal-your-cryptocurrency/
+ Date: 2021-12-07T04:04:02-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/09/05/Twitter--header.jpg)

![Twitter](https://www.bleepstatic.com/content/hl-images/2021/09/05/Twitter--header.jpg)


Scammers monitor every tweet containing requests for support on MetaMask, TrustWallet, and other popular crypto wallets, and respond to them with scam links in just seconds.


To conduct these targeted phishing attacks, scammers abuse Twitter APIs that allow them to [monitor all public tweets](https://developer.twitter.com/en/docs/tutorials/stream-tweets-in-real-time) for specific keywords or phrases.


If those phrases are present, these same programs will direct Twitter bots under the scammer's control to automatically reply to the tweets as fake support agents with links to scams that steal cryptocurrency wallets.


These attacks are nothing new, and [we reported on them in May](https://www.bleepingcomputer.com/news/security/trust-wallet-metamask-crypto-wallets-targeted-by-new-support-scam/). However, these attacks have expanded to other cryptocurrencies, and the scams continue to run rampant.


Therefore, we felt it was vital for our readers to revisit this attack and illustrate how it works, so you do not accidentally become a victim.


The anatomy of the Twitter crypto scam
--------------------------------------


In tests conducted by BleepingComputer, tweets containing the words 'support,' 'help,' or 'assistance' along with the keywords like 'MetaMask,' 'Phantom,' 'Yoroi,' and 'Trust Wallet' will result in almost instantaneous replies from Twitter bots with fake support forms or accounts.


Other keywords have mixed results, such as wallets' names and the word 'stolen.'


Our first test of these cryptocurrency scam bots was to pack a tweet with numerous keywords and see what would happen.



> 
> I need trust wallet metamask phantom yoroi support! I lost all my crypto and password recovery phrase.  
>   
> 
> Come on all you bots!
> 
> 
> — Lawrence Abrams (@LawrenceAbrams) [December 6, 2021](https://twitter.com/LawrenceAbrams/status/1467915157150085127?ref_src=twsrc%5Etfw)


We then [conducted further tests](https://twitter.com/BeepinComputer) to try and narrow down what keywords would trigger the bot's replies.


Within seconds of posting our tests, we received replies from numerous scam accounts pretending to be MetaMask and TrustWallet support accounts, "previous victims," or helpful users.




| Fake MetaMask support account | Fake Phantom support account |
| Trustwallet scammer | Yoroi scammer |

All of the scammer's replies share a common purpose - to steal the recovery phrases for a victim's wallet, which the attackers can then use to import the wallet onto their own devices.


To steal the recovery phrases (aka seed phrases), the threat actors set up support forms on Google Docs and other cloud platforms.


These forms impersonate a basic support form, asking the user for their email address, the problem they are having, and their wallet's recovery phrase, as shown by the fake MetaMask support form below.



![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Fake MetaMask support form**  
*Source: BleepingComputer*
When prompting for the recovery phrase, they include silly language about it being processed by their "encrypted cloud bot," likely to try and convince the user to post the sensitive information.



![Prompting the victim to enter their recovery phrase](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Prompting the victim to enter their recovery phrase**
Once the recovery phrase is sent to the attackers, it's game over and they now have full access to the cryptocurrency within your wallet and can transfer it to other wallets under their control.


Before you say that no one falls for these scams, sadly, that is untrue, and Twitter users have had their wallets, cryptocurrency, and NFTs, stolen.



> 
> [@merchant\_token](https://twitter.com/merchant_token?ref_src=twsrc%5Etfw) I wasn't able to change my withdrawal address from Binance to metamask, so I contacted and have been fooled by a fake metamask support [@MetaMasko](https://twitter.com/MetaMasko?ref_src=twsrc%5Etfw) who stole my tokens from my Metamask Wallet.
> 
> 
> — Sébastien FC (@fc\_sebastien) [July 9, 2021](https://twitter.com/fc_sebastien/status/1413531075142377475?ref_src=twsrc%5Etfw)



> 
> Thank you Kenzie. I was getting what I thought was customer support for funds that were missing since last week. The fake customer support shared a link , and through that they extracted my Metamask. I've been all day trying to at least recover art that wasn't sold.
> 
> 
> — Nightversion (@NightversionHQ) [November 24, 2021](https://twitter.com/NightversionHQ/status/1463416080303591424?ref_src=twsrc%5Etfw)


Never share recovery phrases!
-----------------------------


As a general rule, you should **never share your wallet's recovery phrase** with anyone. The recovery phrase is only for you, and no legitimate support person from MetaMask, TrustWallet, or elsewhere will ever ask for it.


It is also important to remember not to share your screen with an untrusted user who then requests that you display your recovery phrase. At that point, they can simply take a screenshot and write it down manually.


Ultimately, these attacks will continue unless Twitter figures out a way to prevent these bots from running rampant, restrict the use of specific keywords, or put more stringent controls on who can join their developer platform.


BleepingComputer has reached out to Twitter with questions regardings these attacks and the API abuse but has not received a reply.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Metamask]] [[Trustwallet]] [[Bleepingcomputer]] [[Metamask]] [[Bleeping Computer]]

