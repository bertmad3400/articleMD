# MyKings botnet still active and making massive amounts of money
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/mykings-botnet-still-active-and-making-massive-amounts-of-money/)
+ Date: October 13, 2021
+ Author: Bill Toulas


## Article:
![king](https://www.bleepstatic.com/content/hl-images/2021/10/13/king.jpg?rand=940724531)


The MyKings botnet (aka Smominru or DarkCloud) is still actively spreading, making massive amounts of money in crypto, five years after it first appeared in the wild.


Being one of the most analyzed botnets in recent history, MyKings is particularly interesting to researchers thanks to its vast infrastructure and versatile features, including bootkits, miners, droppers, clipboard stealers, and more.


The latest team of researchers to look into MyKings is Avast Threat Labs, which gathered 6,700 unique samples to analyze since the beginning of 2020.


During the same period, Avast actively prevented over 144,000 attacks MyKings against its clients, most of them based in Russia, India, and Pakistan.



![Victims heat map](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/map.png)**Victims heat map**  

Source: Avast
The botnet uses many cryptocurrency wallet addresses, with the balances in some of them being quite high. Avast believes that these wallets' cryptocurrency was amassed by the clipboard stealer and the crypto mining components.


The earnings reflected in the wallet addresses linked to MyKings are approximately $24.7 million. However, since the botnet uses more than 20 cryptocurrencies in total, this amount is only a part of its total financial gains.



![Earnings concerning three cryptocurrencies](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/earnings.jpg)**Earnings concerning three cryptocurrencies**  

Source: Avast
To protect the hardcoded wallet address value from extraction and analysis, the malware encrypts it with a simple ROT cipher. In general, though, no notable upgrades have been spotted on that front in the recent samples.


New URL substitution tricks
---------------------------


Apart from the wallet address substitution that diverts transactions, Avast has also [spotted a new monetization technique](http://decoded.avast.io/janrubin/the-king-is-dead-long-live-mykings/) used by MyKings operators involving the Steam gaming platform.



![Victimized Steam users complaining about the trade link changes](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Victimized Steam users complaining about the trade link changes**  

Source: Avast
The latest versions of the malware also feature a new URL manipulation system in the clipboard stealer module, which the attackers created to hijack Steam item trade transactions. The module changes the trade offer URL, so the actor is placed at the receiving end, stealing valuable in-game items, etc.


Similar functionality was added for the Yandex disk storage cloud service, with MyKing manipulating the URLs sent by users to their acquaintances.


The modified links point to Yandex storage addresses containing RAR or ZIP archives named "photos," which deliver a copy of the MyKings malware to these machines.



![Fake 'photos' archive delivering malware](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Fake 'photos' archive delivering malware**  

Source: Avast
In 2018, MyKings was growing steadily, with the malware [reaching 520,000 infections](https://www.bleepingcomputer.com/news/security/smominru-botnet-infected-over-500-000-windows-machines/) and making millions of dollars for its operators. 


Today, it appears that the botnet has grown to new proportions while still managing to remain hidden and free from law enforcement crackdowns.




#### Tags:
[[MyKings]] [[malware]] [[botnet]] [[Source:]] [[Bleeping Computer]]
