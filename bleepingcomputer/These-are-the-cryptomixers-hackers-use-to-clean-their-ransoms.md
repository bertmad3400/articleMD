# These are the cryptomixers hackers use to clean their ransoms
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/these-are-the-cryptomixers-hackers-use-to-clean-their-ransoms/)
+ Date: November 16, 2021
+ Author: Bill Toulas


## Article:
![washing_machine](https://www.bleepstatic.com/content/hl-images/2021/11/16/washing_machine.jpg?rand=126836188)


Cryptomixers have always been at the epicenter of cybercrime activity, allowing hackers to "clean" cryptocurrency stolen from victims and making it hard for law enforcement to track them.


When threat actors steal cryptocurrency or receive it as a ransom payment, law enforcement or researchers can see what cryptocurrency wallet the funds were sent to.


Mixers allow threat actors to deposit illicitly obtained cryptocurrency and then mix it in a large pool of "random" transactions.


This way, the original crypto gets muddled in a large collection of sums from many different and unknown sources.


When done, the "cleaned" crypto is sent to a different address owned by the threat actors that have not been used before and is unknown to law enforcement. For the use of this service, the cryptomixers take a commission (usually 1-3%) from the mixed cryptocurrency.



![The bitcoin mixing process](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/mixing_process.jpg)**The bitcoin mixing process**  
*Source: Intel471*
There's a dedicated area of research around the tracing of illicit cryptocurrency transactions, so mixing services need to use secret and robust mixing algorithms, or law enforcement could trace the funds.


Also, these services have to avoid keeping any logs or any piece of information that could help identify users and link them to their assets.


Researchers at Intel471 have explored the cybercrime underground to find which platforms are thought to be the most reliable in eradicating the transactions' trace, and they found four notable examples.


Today’s mixing scene
--------------------


Today, hackers use four popular cryptomixing services, namely Absolutio, AudiA6, Blender, and Mix-btc.


Except for Mix-btc, all platforms operate on the Tor network to ensure the anonymity and privacy of their users.


They support Bitcoin, Bitcoin Cash, Dash, Ethereum, Ethereum Classic, Litecoin, Monero, and Tether.


Mixers charge either a flat fee or a dynamic fee for using their services. Intel471 explains that "dynamic fee."


"Some services allow users to choose a “dynamic” service fee, which is most likely done to complicate investigations into illicit cryptocurrency funds by altering the amount being laundered at different stages of the process, making it more difficult to tie the funds to a specific crime or individual," explains [the report](http://intel471.com/blog/cryptomixers-ransomware) by Intel471.


The different fees offered by each of the four mixers are below:


* Absolutio: 1% to 30% (dynamic)
* AudiA6: 3% to 5.5% (flat)
* Blender: 0.6% to 2.5% (dynamic)
* Mix-btc: 3% to 5.5% (flat)


Below you can see the various configurations options threat actors can use on the Absolutio mixing platform.



![The Absolutio mixing platform](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/absolutio.jpg)**The Absolutio mixing platform**
Absolutio also offers time-delay options to help introduce variations that will help strengthen the anonymization. Also, it promises to wipe all request data after two days.


The service claims that all the coins come from allowed addresses and reputable exchanges and that users won't get crypto from "shady" sources.


A gray area
-----------


Analysts at Intel471 were able to find a wallet that belongs to Blender and report that between June 2020 and July 2020, it handled cryptocurrency transactions worth $3,400,000.


This indicates the business size of these platforms, which operate in [a gray legal area](https://www.bleepingcomputer.com/news/security/us-treasury-hits-bitcoin-mixer-with-60-million-penalty/), making tens of thousands of dollars per month, mostly coming from cybercrime activities.


Cryptocurrency mixing isn't intrinsically illegal and is commonly promoted as a privacy-boosting method.


However, if a mixer is knowingly assisting illegal operations in laundering their illicit proceeds, law enforcement will target them and shut down their operations.


In the past, law enforcement operations [shut down the Helix bitcoin mixer](https://www.bleepingcomputer.com/news/security/helix-bitcoin-mixer-owner-charged-for-laundering-over-310-million/) for laundering hundreds of millions of dollars of illicit narcotics proceeds. Similarly, the [Dutch police seized the BestMixer.io domain](https://www.bleepingcomputer.com/news/security/bestmixerio-service-shut-down-for-laundering-200-million-/) after building a case that threat actors used the mixer to launder at least $200 million bitcoin for cybercriminals.


Intel471 also says that some ransomware groups integrated cryptocurrency mixing services directly in their administrative panels.


"The developers behind Avaddon, DarkSide 2.0 (also known as BlackMatter) and REvil likely integrated the BitMix cryptocurrency mixer to facilitate the laundering of ransom payments for program affiliates," reads the report by Intel471.


As mixers are known to be used by illegal operations, they will continue to be targeted by law enforcement and possibly US sanctions, as we saw with the [Chatex](https://www.bleepingcomputer.com/news/security/us-sanctions-chatex-cryptoexchange-used-by-ransomware-gangs/) and [Suex](https://www.bleepingcomputer.com/news/security/us-sanctions-cryptocurrency-exchange-used-by-ransomware-gangs/) exchanges.




#### Tags:
[[Intel471]] [[cybercrime]] [[bitcoin]] [[Absolutio]] [[Bleeping Computer]]
