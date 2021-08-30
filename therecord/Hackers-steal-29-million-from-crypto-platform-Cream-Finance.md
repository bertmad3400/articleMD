# Hackers steal $29 million from crypto-platform Cream Finance
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/hackers-steal-29-million-from-crypto-platform-cream-finance/)
+ Date: August 30, 2021
+ Author: Catalin Cimpanu


## Article:
![Hackers steal $29 million from crypto-platform Cream Finance](https://therecord.media/wp-content/uploads/2021/08/cryptocurrency-bitcoin-ethereum.png)

Hackers are estimated to have stolen more than $29 million in cryptocurrency assets from Cream Finance, a decentralized finance (DeFi) platform that allows users to loan and speculate on cryptocurrency price variations.


The company confirmed the hack earlier today, half an hour after blockchain security firm PeckShield [noticed](https://twitter.com/peckshield/status/1432250879407792130) signs of an ongoing attack.





Cream Finance said the hacker used a “reentrancy attack” in its “flash loan” feature to steal 418,311,571 in AMP tokens (estimated at around $25.1 million at the time of the hack) and 1,308.09 in ETH coins (estimated at around $4.15 million).


The term “flash loan” refers to a contract (script) that runs on the Etherium blockchain that allows Cream Finance users to take quick loans from the company’s funds and then return them at a later date.


Reentrancy attacks take place when a bug in these contracts allows an attacker to withdraw funds repeatedly, in a loop, before the original transaction is approved or declined or the funds need to be returned.


[PeckShield](https://twitter.com/CreamdotFinance/status/1432249773575208964) and [Tal Be’ery](https://twitter.com/TalBeerySec/status/1432356294640422917), the founder of cryptocurrency wallet app ZenGo, confirmed that the Cream Finance hacker exploited a bug in the [ERC777 token contract](https://eips.ethereum.org/EIPS/eip-777#erc777token-token-contract) interface that’s used by Cream Finance to interact with the underlying Etherium blockchain.


Be’ery told *The Record* today that ERC777 has [enabled several reentrancy attacks on DeFi online services](https://www.zengo.com/imbtc-defi-hack-explained/), which keep relying on the feature despite its history of bad implementations, bugs, and hacks.


The ZenGo founder also told *The Record* that DeFi services need to develop or implement a firewall-like system for their platforms in order to filter malicious requests to their underlying contracts, which are the backbone of their services and the targets of most of these hacks.





DeFi related hacks have accounted for 76% of all major hacks in 2021, and users have lost more than $474 million to attacks on DeFi platforms this year, according to CipherTrace. Most of the attacks on DeFi protocols employed flash loans, [the company said](https://ciphertrace.com/cryptocurrency-crime-and-anti-money-laundering-report-august-2021/) in a report released earlier this month.


Similarly, DeFi hacks also made up 21% of all the 2020 cryptocurrency hacks and stolen funds after being almost inexistent a year before, in 2019, the company said in a [report last year](https://ciphertrace.com/half-of-2020-crypto-hacks-are-from-defi-protocols-and-exchanges/).


This trend of hackers targeting DeFi platforms can be explained by the fact that the cryptocurrency ecosystem is highly unregulated, security is almost an afterthought, and many platforms fail at implementing their underlying technical base, many running buggy contracts (scripts) that can be easily abused by anyone with knowledge of cryptography and C and C++ coding.





#### Tags:
[[]] [[The Record]]
