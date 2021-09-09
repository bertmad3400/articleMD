# Financial Cybercrime: Why Cryptocurrency is the Perfect ‘Getaway Car’
### John Hammond, security researcher with Huntress, discusses how financially motivated cybercrooks use and abuse cryptocurrency.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169327)
+ Date: September 9, 2021  1:51 pm
+ Author: John Hammond


## Article:
*This is part one of a two-part series on how hackers stole $2 million in cryptocurrency. Part 2 will be posted nest week!*


It’s no secret: Hackers are out to make money. Over the summer, it seemed there was practically a new ransomware attack every day of the week. Whether it be Colonial Pipeline, JBS, the Massachusetts Steamship, Fujifilms or any other organization in the headlines, cybercrime is in the spotlight more than ever before — and with good reason: cybercrime is a lucrative gig.


We tend to poke fun at the historic television game show *Who Wants To Be A Millionaire?* Certainly, just about everyone in the world wants to be a millionaire, and threat actors are no exception. In recent reports, cybercrime cost the world [over $1 trillion](https://www.mcafee.com/enterprise/en-us/about/newsroom/press-releases/press-release.html?news_id=6859bd8c-9304-4147-bdab-32b35457e629), and it’s predicted to cost the global economy [$10.5 trillion by 2025](https://cybersecurityventures.com/cybercrime-damage-costs-10-trillion-by-2025/).


Headlines and breaking news reports make this abundantly clear—after seeing Colonial Pipeline pay $4.4 million to ransomware hackers, other cybercrime gangs selling data on the Dark Web, or compromising servers and online websites to add to a botnet.


There is one strong commonality with all these incidents and attacks: The hackers want the funds in cryptocurrency.


**How Hackers Make Money**
--------------------------


There are dozens of ways that threat actors profit off of their victims. There are a few methods that stand out:


Encrypting a target’s computer systems, including their personal data and documents and holding an entire network for ransom, creates urgency and chaos for the victim. Hackers extort the target, demand payment within a short timeline and threaten to publicize the data. All of these tactics induce panic for the victim.


Ransomware is fast and lucrative, with potential payouts ranging from thousands of dollars to millions as we’ve seen. But ransomware is loud and overt. If a victim is hit with ransomware, it’s clearly evident on their computer screen, and they know they’ve been compromised. This takes away an element of stealth from the hackers.


If a hacker has initial access and can listen in on network communications or uncover sensitive information, they could put this to use. They might sell the access to other hackers on the Dark Web, or use found banking information or credentials to send money, or gain access to credit-card data. They can do a lot of damage.


While this method is stealthier than ransomware, there is still a risk of getting caught. Also, the potential payout depends on the amount of money the victim has to begin with. If they were selling this information, there is still the chance they may not get a buyer. Ultimately, this method has too many variable results, and hackers might opt for a different tactic.


After a threat actor has compromised a machine, they can do anything they want. Oftentimes, hackers will install a backdoor, or ensure they have persistent access and can maintain control of the machine over long periods of time. Typically, this persistence takes the form of a small, inconspicuous “stub” that might hide amongst autoruns or other segments of code that will run automatically.


Persistence on its own doesn’t make money, though. Installing a small routine to mine cryptocurrency with the target’s resources however, does.


This option enslaves the victim machine to compute hashes and solve mathematical problems in order to mine Bitcoin, Ethereum, Monero or any other cryptocurrency they like. Hackers take advantage of the target computer’s CPU, RAM and other resources and run up the victim’s electricity bill rather than their own. This works in a similar way as persistence, as this should remain hidden but actively run every time the device is turned on.


From these options, slowly mining cryptocurrency would make the least amount of money in the short term. But if this attack goes unnoticed, it could make a hefty payout in the long term, especially if it is a widespread attack across multiple victims. This tactic is the most stealthy, and can be carried out in a slow, noninvasive way. Unlike ransomware, where the victim knows they are compromised—if a cryptocoin miner is running, the target may be completely oblivious.


**Why Cryptocurrency?**
-----------------------


Cryptocurrency is the perfect getaway car for hackers. It offers autonomy, anonymity and permanence in their transactions. With cryptocoins, there is no oversight — there aren’t any intermediary authorities like banks or governments, no banking fees, account maintenance, minimum balances or overdraft charges — you can truly do what you want with your money.


By accepting payment solely in cryptocoins, bad guys can remain practically anonymous. Transactions do not carry your identity, or things like email addresses, names or any details. Ultimately, cryptocurrencies are just digital data. A “wallet address” is just nonsense letters and numbers that might look like gibberish: “bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh,” for example.


The most attractive feature of cryptocurrency for hackers is likely the permanence: when money is sent, you cannot get it back. Much like with cash — unless the recipient gives that money back to you — it’s now out of your control. This means for attacks like ransomware, hackers can literally take the money and run.


One important note for cryptocurrencies is that **transactions are kept and displayed on a public ledger.** Anyone could look up where money was sent to and from on the blockchain, simply checking online explorers.


You might be scratching your head and wondering then, “If the transactions are public, how can they bad guys remain anonymous?”


Keep in mind that the wallet addresses and transfers themselves carry no personally identifiable information. On top of that, hackers might often send the funds through “a mixer” or “wash” the cryptocurrency by transferring it through numerous wallets. It is truly money laundering brought into the digital age.


In fact, there are automated services that will do this for you—tornado.cash being a fine example for “washing” Ethereum. By sending money through multiple wallets, there are fewer ties to the original actor, and they increase their degree of privacy.


With all that in mind, cryptocoins like Bitcoin and others remain “a hacker’s currency.” They still offer real-world value, as they equate to a legitimate financial dollar amount. Without an overseeing authority and with removed governance, markets can run unregulated without prying eyes. Ultimately, without any ties to the bad actors themselves, this allows for covert and under-the-table business deals. No other technology makes for the perfect crime.


**How Prolific Is Cryptocurrency?**
-----------------------------------


With a quick jaunt through the Dark Web, you can find numerous threat actors buying and selling malware or hacking services with solely cryptocurrency.


In most cases, a QR code is displayed to easily make a purchase. If for whatever reason a buyer cannot scan the QR code, the lengthy wallet address that can be copied and pasted into their purchasing application is displayed.


This is prevalent all throughout malware marketplaces and hacking forums. While there are tools and frameworks for sale (often scams on their own), some peculiar utilities capitalize on the very nature of buying and selling with cryptocurrencies.


The simple act of copying and pasting a wallet address is one tiny attack vector that hackers can abuse. Because a wallet address follows a standard pattern and structure (specific amount of characters, using letters and numbers, etc.), threat actors could latch onto the computer clipboard and monitor for the presence of a wallet address as the victim is about to send money to purchase something.


Malware can perform a simple switcheroo and just swap out the *intended* recipient’s wallet address with *its own malicious* wallet address — sending the money to the bad guys and leaving the victim without any means of ever getting it back.


In our next article, we’ll explore this tactic firsthand as we uncover how hackers stole more than $2 million in cryptocurrency with this “clipboard hijacker” technique.


*This is part one of a two-part series on how hackers stole $2 million in cryptocurrency. Part 2 will be posted nest week!*


***John Hammond is a security researcher with Huntress.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[cryptocurrency.]] [[cybercrime]] [[ransomware,]] [[ransomware]] [[it’s]] [[Web,]] [[data.]] [[Ultimately,]] [[ThreatPost]]
