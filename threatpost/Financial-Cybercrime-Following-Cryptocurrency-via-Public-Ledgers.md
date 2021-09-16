# Financial Cybercrime: Following Cryptocurrency via Public Ledgers
### John Hammond, security researcher with Huntress, discusses a wallet-hijacking RAT, and how law enforcement recovered millions in Bitcoin after the Colonial Pipeline attack.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169987)
+ Date: September 16, 2021  9:08 am
+ Author: John Hammond


## Article:
*This is Part II of a two-part series on how cybercrooks embrace and use cryptocurrency. To read Part I, please [click here](https://threatpost.com/financial-cybercrime-cryptocurrency/169327/).*


While Bitcoin transactions are anonymous, it’s possible to follow the money through public ledgers to see what those transactions actually are and how they flow. This allows us to glean more about the Colonial Pipeline attack that [occurred this summer](https://threatpost.com/takeaways-colonial-pipeline-ransomware/166980/), and the process also led us to uncover a wallet-hijacking malware that was making the rounds earlier this year.


**A Look at Crypto’s Role in the Colonial Pipeline Attack**
-----------------------------------------------------------


Famously, Colonial Pipeline was compromised with a ransomware attack earlier this year. And ultimately, it paid $4.4 million in Bitcoin to recover their systems and data. As this was a very large-scale attack, the federal government stepped in.


And in early June, millions of dollars that were paid to the hackers were recovered and returned to Colonial Pipeline. On its own, this is a massive achievement and a great stride in our fight for cybersecurity — but it offers an interesting story to walk through the to-and-from process of cryptocurrency transactions.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The FBI released a public but [redacted affidavit](https://storage.courtlistener.com/recap/gov.uscourts.cand.379840/gov.uscourts.cand.379840.1.0.pdf) surrounding the incident:


As you can see, the cryptocurrency wallets in question were partially redacted — but as we know, these follow a recognizable pattern and can be uncovered in the public ledger. Security researchers were able to uncover the full wallet address and follow the breadcrumbs to see where the money went — and how.


Thus began a short journey on the public blockchain ledger, that we can join in on the ride just as well.


After determining the full wallet address, we can find this wallet on the blockchain and see what was transferred and when. Paralleling this with the affidavit, we can follow the whole chain of transactions.


Note that the number of Bitcoins received, as well as the latter half of the wallet address, align with what is stated in the affidavit.


Please bear in mind that the U.S. dollar value of Bitcoin fluctuates, and the value presented in these screenshots will differ from what the currency conversion is today.


Examining steps 28-33 outlined in the affidavit, we can follow through approximately five different wallet addresses to track where the original money had gone.


With just five “hops” from the original wallet address, it appears as if these threat actors had not used a mixer. They simply… moved the money around?


The final resulting transaction sends 63 Bitcoin to the FBI seizure wallet address. However, 63 BTC does not align with the original payment of 75 Bitcoin, and that leaves us with some lingering questions.


It should be noted that 63 BTC does not equate to 75 BTC, regardless of the current conversion rate to USD. We can only speculate that perhaps some of the original pool of money was given to affiliates or partners, as it is well known that DarkSide (the ransomware gang behind the Colonial Pipeline attack) does work with others. Perhaps the wallet address that those funds were sent to was not one that the FBI was able to control and could not recover. Without other information, we cannot be sure.


We can, however, be thankful that out of the original $4.4 million that was paid to the hackers, $2.3 million was able to be recovered, considering the fluctuating value of Bitcoin and the funds available in the seized wallets.


Unfortunately, we are again left to wonder about this in speculation. It’s fair to consider the FBI had uncovered the private key for the wallet, but the underlying question of how has not been publicly disclosed. Certainly there could have been some OpSec mistakes on the part of the hackers, or other leaks, or even some active intrusion performed by the FBI… but it remains a mystery.


**A Bitcoin Stealer**
---------------------


Now, let’s turn to a peculiar example of a clipboard hijacking malware sample. We recently uncovered a persistent foothold hiding amongst common autoruns, with the file contents like so:


Needless to say, this is practically unintelligible. We could determine that this was a JScript file, or the Microsoft Windows dialect of ECMAScript/JavaScript that will execute natively on a modern Windows computer.


However, this file was dubiously named “AdobeColorCR\_ExtraSettings\_1\_0-mul.zip”. Upon our own inspection, it was clear that this was *not* a ZIP file.


This code was kickstarted with the following payload:


![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/16083827/Payload.png)


The wscript.exe native binary would execute this file, parsed as JScript, with a supplied “key.” Our task was to determine what this JScript code really did with this “key,” so we dove into the code and began to deobfuscate that large, unintelligible garbage above.


Thankfully, the large chunk was simply a glorified “eval” statement, which would evaluate data passed in and execute another layer of code. We refer to these as “stages” of the payload, like peeling off layers of an onion, or taking off one larger Matryoshka doll to find the next smaller doll.


After *five* stages of deobfuscation efforts (typically decrypting AES-encrypted data with that given key), we finally uncover the core functionality of this malware sample, which is at least sensible code that a human analyst can make sense of:


![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/16083959/Code.png)


Examining this malware, we found clear remote access-trojan (RAT) functionality—the capability to send and receive data and execute commands just as a traditional RAT would. The malware would check for installed antivirus products and work to run undetected.


The most interesting aspect of this malware soon came to light, as we uncovered peculiar functions named `funcCret` and `sendClib`. The former function included bare cryptocurrency wallet addresses, and would examine the victim computer’s clipboard data to check for the presence of any *other* wallet address. If any wallet address were found in the clipboard (as if the user had “copied” an address to purchase an item), the `sendClib` function would execute and *replace* the clipboard contents with its own rogue wallet address:


![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/16084244/Code2.png)


This is the smoking gun that proves the simple swapping of wallet addresses. If the user intended to send money to one original recipient, attempting to paste the original address would result in the *hacker’s address* being pasted. The money would then get sent to the bad guys, and ultimately, the threat actors would have stolen the funds, leaving the victim with no means of ever recovering it.


Given these wallet addresses stored in different variables, we can assume that “bch” in the code above refers to Bitcoin Cash and “etho” refers to Ethereum, but the “Mizu” address isn’t as clear. Anyone can simply lookup the transactions and value stored in the Ethereum and Bitcoin Cash wallets on the public blockchain just as we have, but the more interesting story comes from the Mizu address: “1NSrjTotDiuK7S1xMm9yuppq4dr4Uf9saM.”


As it turns out, the Mizu address refers to pure Bitcoin (BTC). [Examining the wallet on the public blockchain](https://www.blockchain.com/btc/address/1NSrjTotDiuK7S1xMm9yuppq4dr4Uf9saM), we can see that there have been relatively recent transactions, and it has transacted over a hundred times.


When we had first discovered this, the value of Bitcoin was equated to so much USD that the wallet address has received more than $2 million. Using internet-archive websites like “The Way-Back Machine,” anyone can now “go back in time” and see the blockchain page as it was then:


While this is alarming on its own, we wanted to dig a bit deeper. We were curious, ***what did the hackers do with the money?*** Did they cash out?


There are “crypto-exchanges” that convert one form of cryptocurrency to another, or even to fiat currency like real dollar bills you can hold in your hand. [Binance](http://binance.com) is one fine example of this, and there are a number of other services that let you use crypto for legitimate payments, like [CoinPayments](https://coinpayments.net), [CryptoPay](https://cryptopay.me), or even for trading on sites like [Bittrex](https://bittrex.com).


Thanks to the public blockchain ledger, we can again walk through different transactions and put the puzzle pieces together to tell the greater story here.


The crypto-exchange Binance has previously [shared its own public wallet address](https://twitter.com/binance/status/961666467325358081?lang=en). Examining the [wallet on the blockchain](https://www.blockchain.com/btc/address/1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s), the cumulative value of transactions taken place with the service is absolutely mind-blowing.


Interestingly enough, the hacker wallet we have been tracking had one peculiar transaction in March 2021. Following just one other hop, we find that a portion of the money is in fact sent to Binance shortly after.


Granted, we can see the amount of Bitcoin sent is a very small amount, but this could very well be just one breadcrumb, amongst a sea of other wallet addresses and transactions (if they did in fact use a mixer in some cases), that points to the threat actors really making use of this money.


On [other blockchain explorers](https://www.walletexplorer.com/info), those that have the functionality to merge addresses together if funds are “co-spent” in one transaction, [we can again see the nefarious wallet send or receive funds](https://www.walletexplorer.com/wallet/0123a03a34c51754) to exchange, trading or payment websites.


Truthfully, walking through each of these transfers of funds and understanding the implications becomes a bit murky due to the significant amount of transactions. At its core, malware has still stolen over millions of dollars in cryptocurrency — and using this “clipboard hijacking” technique is one novel option amongst the others that hackers use to make money.


Considering this malicious activity, we have ensured that these wallet addresses have been reported. Websites like [bitcoinabuse.com](https://www.bitcoinabuse.com/) keep a record of known malicious Bitcoin addresses used by ransomware, blackmailers, fraudsters and other bad actors.


The malicious wallet address used in this malware and attack [have been reported](https://www.bitcoinabuse.com/reports/1NSrjTotDiuK7S1xMm9yuppq4dr4Uf9saM) to this Bitcoin Abuse Database.


Those with a technical eye may have noticed the strange verss string in the final stage of this malware sample, “backendSoft\_1.0.1.9”. As part of the investigative process we look for breadcrumbs that might help identify this malware sample. Doing some simple research on this, we discovered there has been [recent](https://www.reddit.com/r/Bitcoin/comments/mlm58c/rat_remote_access_trojan_that_is_deeply/) [chatter](https://twitter.com/search?q=%23ViperSoftX&lang=en) regarding this malware, apparently originally known as “ViperSoftX.”


Other researchers have analyzed the original “ViperSoftX” sample in 2020, and all of the technical tradecraft remains the same between “ViperSoft” and “BackendSoft.”


The hardcoded version string, the command-and-control servers and the crypto-coin addresses are different — but the attack technique remains the same.


**Lessons Learned: Bitcoin and the Cyber-Underground**
------------------------------------------------------


After all is said, we come away with some lessons learned.


This clipboard-hijacking RAT and malware strain “backendSoft” is a re-run of “ViperSoft” RAT, which the industry previously uncovered the 2020 rendition.


This malware strain would not have been found without looking in the corners and crevices of the Windows filesystem, examining autoruns and hunting for persistent footholds. Persistence proves time and time again to be the smoking gun at the crime scene.


With or without following the trail of money through the public blockchain, the fact remains that a hacker’s cryptocurrency was found present in malware that led to stealing millions of dollars with legitimate real-world value.


While we have seen ransomware run rampant, information and data up for auction on the Dark Web, and cryptocurrency miners pinning down system resources, this clipboard hijacking technique is a worthy story to be told.


*This is Part II of a two-part series on how cybercrooks stole $2 million in Bitcoin, and how they use cryptocurrency in the underground economy. To read Part I, please [click here](https://threatpost.com/financial-cybercrime-cryptocurrency/169327/).*


***John Hammond is a security researcher with Huntress.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[Bitcoin]] [[malware]] [[blockchain]] [[here.]] [[ransomware]] [[transactions.]] [[address,]] [[address.]] [[Windows]] [[blockchain,]] [[ThreatPost]]
