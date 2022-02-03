# Wormhole Crypto Platform: 'Funds Are Safe' After $314M Heist
### The popular bridge, which connects Ethereum, Solana blockchain & more, was shelled out by it's-not-saying. Wormhole is trying to negotiate  with the attacker.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178189
+ Date: 2022-02-03T18:28:14+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/26171204/cryptocurrency_fail-405x270-1.jpeg)

Wormhole – a web-based blockchain “bridge” that enables users to convert cryptocurrencies – said on Thursday that “all funds are safe” after attackers abused a vulnerability to shake it down for 120,000 Ethereum (approximately $314 million).


The popular bridge, which connects Ethereum (ETH), the Solana blockchain (SOL) and more, has reportedly been trying to negotiate on-chain with the attacker since Wednesday’s attack. The exploit was [reportedly](https://www.reuters.com/technology/crypto-network-wormhole-hit-with-possible-320-mln-hack-2022-02-03/) the fourth-largest [crypto-heist](https://cointelegraph.com/explained/the-biggest-crypto-heists-of-all-time) ever, the biggest of 2022 so far, and the biggest one that Solana has faced yet.[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In a postmortem shared with Threatpost on Thursday, blockchain security and smart-auditing company CertiK said that its preliminary analysis indicates that “the attacker exploited a mint function on the Solana side of the Wormhole bridge to create 120,000 wETH [wrapped Ethereum] for themselves, then used these minted tokens to claim ETH that was held on the Ethereum side of the bridge.”


As far as negotiation attempts go, CertiK said that the Wormhole team left a message to the attacker stating, “We noticed you were able to exploit the Solana VAA verification and mint tokens. We’d like to offer you a white-hat agreement, and present you a bug bounty of $10 million for exploit details, and return the wETH you’ve minted. You can reach out to us at [contact@certus.one](https://t.nylas.com/t1/222/6go6zh11n354zj4gtfyydtk2j/0/7e3f0565dba6ac71abf6ccdb740c5697cd8db828b0852af88c0c054ee28bb3c2).”


Its total on the heist differs a bit from that of Wormhole: CertiK’s analysis showed that the attacker got away with 93,750 ETH ($251 million), 432,662 SOL ($46.6 million) and 4.14 million in USD Coin (USDC) ($4.14 million), for a total of $302,495,717.


This is the [second-largest hack](https://defiyield.app/rekt-database) of a decentralized finance (DeFi) platform, second only to the Poly Network (ETH) exploit, in which an attacker ripped off about $602 million. That attacker reportedly went on to [pay it back](https://threatpost.com/poly-network-recoups-610m-stolen-from-defi-platform/168906/), however, after accepting a gig as chief security advisor with Poly Network.


In an early-morning [tweet](https://twitter.com/wormholecrypto/status/1489233259808571401) on Thursday, the official Wormhole Twitter account confirmed that it had been raided for 120,000 ETH, but that the vulnerability is now patched.



> 
> 1/2
> 
> 
> All funds have been restored and Wormhole is back up.
> 
> 
> We're deeply grateful for your support and thank you for your patience.
> 
> 
> — Wormhole🌪 (@wormholecrypto) [February 3, 2022](https://twitter.com/wormholecrypto/status/1489232008521859079?ref_src=twsrc%5Etfw)
> 
> 



Wormhole’s Portal – its token bridge – was back up as of 13:29 UTC, the team said.


A ‘Rather Common’ Programming Error
-----------------------------------


Roger Grimes, data driven defense evangelist for KnowBe4, told Threatpost on Thursday that the attack was successful because of what he called a “rather common” programming error.


“The function inside of the multiple nested smart contracts which was supposed to verify the signature was not coded to ensure the integrity check actually happened,” he exlained via email. “So there was no integrity guaranteed in the integrity check. Yeah, that is a problem.”


Why So Popular?
---------------


CertiK said that the bridge’s popularity meant that it had become the dominant bridge between Solana and Ethereum, “and as such was responsible for a large proportion of all wrapped Ethereum on the Solana blockchain.”


Investors’ gonads have shrunk in response to the massive heist: The price of Solana, which outpaced both Bitcoin and Ethereum last year, was in [freefall](https://www.forbes.com/sites/billybambrough/2022/02/03/crypto-price-alert-ethereum-rival-solana-suddenly-in-free-fall-after-huge-325-million-hack/?sh=442f39b04bb5) Thursday morning. It was selling at $97.69 as of 12:50 ET, down 10 percent since the details of the theft were revealed. Solana had hit a high of $260 in November 2021. Ethereum is also giving investors the hives, having dropped about 5 percent as of the same time on Thursday.


At this point, the full extent of this attack “still remains to be seen,” CertiK said. It could turn out to be a precursor to other attacks, the firm suggested, if, for example, Wormhole’s bridge to a different cryptocurrency – the Terra blockchain – shares the same vulnerability as its Solana bridge.


Who Bailed Out Wormhole?
------------------------


The Wormhole team didn’t specify who dug into what must be some seriously deep pockets to back-fill all that money. The Twitterverse, of course, had hypotheses, including that perhaps it was Alameda Research: a cryptocurrency quantitative trading firm and liquidity provider that claims to “manage over $70 million in digital assets and trade around $1 billion per day across thousands of products: all major coins and altcoins, and their derivatives.”


“It was either dilute their equity to infinity with $300 million bail out or watch all of Solana ecosystem crash and burn (which would have costed Alameda more than $300 million on their books),” suggested one Twitter user.



> 
> Alameda probably bailed them out, it was either dilute their equity to infinity with $300 million bail out or watch all of Solana ecosystem crash and burn (which would have costed Alameda more than $300 million on their books)
> 
> 
> — ichioku (@1chioku) [February 3, 2022](https://twitter.com/1chioku/status/1489240858017021956?ref_src=twsrc%5Etfw)
> 
> 



Alameda hasn’t made a public statement on the matter. Wormhole has promised a detailed incident report as soon as possible.


Crypto’s Cutting Edge Gets a Nasty Cut
--------------------------------------


Ronghui Gu, co-founder and professor of CertiK, told Threatpost on Thursday that clearly this Wormhole exploit isn’t the first of its kind, and obviously, it won’t be the last.


“We saw another cross-chain bridge exploited less than a week ago, when Qubit Finance lost $80 million,” Gu pointed out, referring to an attack [confirmed](https://blockworks.co/defi-protocol-qubit-finance-loses-80m-in-hack/#:~:text=Hackers%20have%20stolen%20%2480%20million,ever%2C%20DeFiYield%20Rekt%20data%20shows.) by the DeFi protocol Qubit Finance on Friday.


The attackers reportedly made off with 206,809 Binance coins through Qubit’s QBridge deposit function, making it the seventh-largest DeFi hack ever.


Expect more of the same when it comes to bridge exploits, Gu said, given insatiable demand for these technologies. “We seem to be at an awkward point where the demand for cross-chain infrastructure is far outpacing the industry’s ability to build services securely,” he told Threatpost via email.


Of course, there’s always the “because that’s where the money is” rationale, Gu noted: “Bridges are an attractive target for hackers: they hold millions of dollars of tokens in what is essentially an escrow contract, and by operating across multiple chains they multiply their potential points of failure.”


Threat actors follow the money, he said, and those on the cutting edge of cryptocurrency technology can get bumped off as a result: “A lot of money goes to the newest, most exciting ecosystems. The price that the most adventurous DeFi explorers pay is a heightened risk of falling victim to these exploits of innovative but ultimately insecure platforms.”


A Need for Secure Development Lifecycle
---------------------------------------


Where there is software, there are bugs. Grimes pointed to the attack as being a case in point about the need for training in secure development lifecycle (SDL) coding. “SDL teaches developers about common exploitable bugs and how to avoid putting it into their own code,” he explained. “It teaches about using bug checking tools, using coding tools that automatically rule out as many security bugs as they can, and in general, puts security into the whole lifecycle of developing something, be it a traditional program, smart phone app or smart contract.”


But there’s a  bigger underlying problem, he noted: Namely, most developers and smart contract creators, aren’t trained in SDL and “get little to no training in secure development. So, these sorts of bugs are going to creep in and bad actors are going to take advantage of them.”


One thing to note is that the cryptocurrency world is full of trillions of dollars, but it’s still at the toddler stage. “It is an immature industry using immature code, and like all new industries, it is moving ahead at warp speed, good security be damned,” Grimes said.


Whereas it’s getting harder for bad actors and bug hunters to find really good exploits in Microsoft Windows, Macs, Linux and Google ChromeOS, these platforms are maturing, making it tougher to pull them apart, he said. That includes the experienced coders, tools and the protective mechanisms of the operating systems themselves.


Not so with the  cryptocurrency world, Grimes said, which is the mirror opposite.


“It is built on very secure protocols and algorithms, but then a lot of very immature and buggy applications are built on top of it,” he observed.


He compared it to putting your door key in your potted plant in front of the door: “Sometimes all a thief has to do is look. And that is what hackers exploiting cryptocurrency are doing. They are taking their traditional methods for hunting bugs and using them against immature cryptocurrency applications. And viola, they are finding lots of exploitable bugs.”


And once the money’s gone bye-bye, it’s tough to claw it back. “The exploits always result in stolen money, which are hard to track to and [identify], and almost always impossible to reverse, even if you are watching it in real time,” Grimes said.


He predicted that after suffering billions of dollars in pain, the cryptocurrency world “will mature and it will become harder for hackers to find the easy pickings.”


Too bad the lessons are so painful, Grimes said: “You always hope that when the next cool digital thing happens that we will better apply the security lessons learned from the previous platforms. But we always seem to want there to be more digital blood on the ground than there needs to be. We always, over and over, want to learn the hard way. Each new computing platform is like we have learned nothing at all.”


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=Arp]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Solana]] [[Ethereum]] [[Certik]] [[Threatpost]] [[Blockchain]] [[Million)]] [[“it]] [[“we]] [[Qubit]] [[ThreatPost]]
#### email-adresses
contact@certus.one

