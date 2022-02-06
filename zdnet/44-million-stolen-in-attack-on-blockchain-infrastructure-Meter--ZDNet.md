# $4.4 million stolen in attack on blockchain infrastructure Meter | ZDNet
### The Meter and Moonriver networks were affected by the cyberattack.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/4-4-million-stolen-in-attack-on-blockchain-infrastructure-meter/
+ Date: 2022-02-06 11:00:01
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/699a6b2877a9dd94b2ee7a1223ddffef0f94078c/2019/07/15/bc57c400-ec17-4fcf-968f-17314e68a653/blockchain-566x372.jpg?width=770&height=578&fit=crop&auto=webp)

Blockchain infrastructure company Meter said $4.4 million was stolen during a cyberattack on the platform that started at around 9 am ET on Saturday morning.

The company said it manages an infrastructure that allows smart contracts to scale and travel through heterogeneous blockchain networks. The Meter network as well as the Moonriver network were affected by the hack. 

Blockchain research company PeckShield [confirmed](https://twitter.com/peckshield/status/1490121762847092736) that [1391 ETH and 2.74 BTC](https://moonriver.moonscan.io/tx/0x5a87c24d0665c8f67958099d1ad22e39a03aa08d47d00b7276b8d42294ee0591) were stolen during the incident. 




> The [@Meter\_IO](https://twitter.com/Meter_IO?ref_src=twsrc%5Etfw) is hacked with the loss of $~4.3M (including 1391.24945169 ETH + 2.74068396 BTC). The extension over the original (unaffected) ChainBridge introduces a false deposit issue !!! <https://t.co/YShfXnEZzD> [pic.twitter.com/oY6bpau8DA](https://t.co/oY6bpau8DA)
> 
> — PeckShield Inc. (@peckshield) [February 6, 2022](https://twitter.com/peckshield/status/1490121762847092736?ref_src=twsrc%5Etfw)




Around 2 pm ET on Saturday, the company [said](https://twitter.com/Meter_IO/status/1490045486606139392) it was hacked and urged users not to trade unbacked meterBNB circulating on Moonriver. 

"We have identified the issue: Passport has a feature to automatically wrap and unwrap gas tokens like ETH and BNB for user convenience. However the contract did not block direct interaction of the wrapped ERC20 tokens for the native gas token and did not properly transfer and verify the correct number of WETH transferred from the callers' address. We are working on compensating funds to all affected users," the company explained. 

By 6 pm, Meter [wrote](https://twitter.com/Meter_IO/status/1490103308421255168) that it stopped all bridge transactions and discovered that the issue related to a bug "introduced in the automatic wrap and wrap of native tokens like BNB and ETH extended by the Meter team."

According to Meter, its extended code "had a wrong trust assumption" that let the hacker fake BNB and ETH transfers by "calling the underlying ERC20 deposit function." 






They are working with authorities and said they found "some early traces of the hacker," urging the culprit to return the stolen money. 

Compensation plans are allegedly being created for the users who held WETH and BNB as well as the "liquidity providers." 

"We urge all the liquidity providers that provide liquidity involving WETH and BNB to remove liquidity from the pool and wait for an additional announcement from the Meter team. Please try avoid trading in these pairs as well," the company explained. 




> We are working on taking a snapshot from before the attack & will convert the original BNB & WETH to 1:1 their values in MTRG, the rest inflated BNB & WETH will be converted based on the hacker stolen value from the LP pools.  
>   
> We've set aside $4.4M of MTRG based on today's price.
> 
> — ⚡️Meter.io⚡️ (@Meter\_IO) [February 5, 2022](https://twitter.com/Meter_IO/status/1490110423667929092?ref_src=twsrc%5Etfw)




On Wednesday, [$324 million was stolen](https://www.zdnet.com/article/324-million-in-ether-stolen-from-blockchain-platform-wormhole/) through popular decentralized cross-chain message passing protocol Wormhole. Researchers found evidence of an [80,000 ETH transfer](https://etherscan.io/tx/0xacd309b02e4b533484d148de9ab0adf367ed4e70ed751d1ff036152dc3bc0479) from Wormhole as well as another [40,000 of ETH](https://twitter.com/0xB07DAD/status/1488982652174540802) being sold by the hacker on Solana. 

They have [offered](https://wormholecrypto.medium.com/wormhole-incident-report-02-02-22-ad9b8f21eec6) $10 million to the hacker for the return of the funds and offered the same amount to anyone who can provide information "leading to the arrest and conviction of those responsible for the hack."

Just five days before the Wormhole incident, DeFi protocol Qubit Finance took to Twitter to beg hackers to return [more than $80 million](https://www.zdnet.com/article/qubit-finance-crypto-platform-begs-hacker-to-return-80-million-in-stolen-funds/) that was stolen from them. 

The recent hacks continue a run of attacks on DeFi and blockchain platforms that have occurred over the last year. Chainalysis said at least [$2.2 billion was outright stolen](https://www.zdnet.com/article/22-billion-in-cryptocurrency-stolen-from-defi-platforms-in-2021-report/) from DeFi protocols in 2021. Poly Network saw [$611 million](https://www.zdnet.com/article/poly-network-hackers-potentially-stole-610-million-is-bitcoin-still-safe/) stolen from their platform in August while [Bitmart lost $196 million](https://www.zdnet.com/article/bitmart-breach-losses-reach-200-million/) in early December.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Bnb]] [[Weth]] [[ZDNet]]
#### urls
https://t.co/YShfXnEZzD

