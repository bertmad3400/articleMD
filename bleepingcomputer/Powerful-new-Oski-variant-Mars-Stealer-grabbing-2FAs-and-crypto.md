# Powerful new Oski variant ‘Mars Stealer’ grabbing 2FAs and crypto
### A new and powerful malware named 'Mars Stealer' has appeared in the wild, and appears to be a redesign of the Oski malware that shut down development abruptly in the summer of 2020.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/powerful-new-oski-variant-mars-stealer-grabbing-2fas-and-crypto/
+ Date: 2022-02-01T13:41:04-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/02/01/mars.jpg)

![](https://www.bleepstatic.com/content/hl-images/2022/02/01/mars.jpg?rand=1366538389)


A new and powerful malware named ‘Mars Stealer’ has appeared in the wild, and appears to be a redesign of the [Oski](https://www.bleepingcomputer.com/news/security/hackers-hijack-routers-dns-to-spread-malicious-covid-19-apps/) malware that shut down development abruptly in the summer of 2020.


Mars Stealer is an information-stealing malware that steals data from all popular web browsers, two-factor authentication plugins, and multiple cryptocurrency extensions and wallets.


Additionally, the malware can exfiltrate files from the infected system and relies on its own loader and wiper, which minimizes the infection footprint.


From Oski to Mars Stealer
-------------------------


In July 2020, the developers behind the Oski information-stealing trojan suddenly shut down their operation after no longer responding to buyers and the closing of their Telegram channel.


Fast forward almost a year later, and a new information-stealing malware called 'Mars Stealer' began to be promoted on Russian-speaking hacking forums.



![Mars Stealer promoted on a hacking forum](https://www.bleepstatic.com/images/news/malware/m/mars-stealer/mars-stealer.jpg)**Mars Stealer promoted on a hacking forum**  
*Source: 3xp0rt*
After security researcher [@3xp0rt](https://twitter.com/3xp0rtblog) obtained a sample, the [researcher discovered](http://3xp0rt.com/posts/mars-stealer) that the Mars Stealer is a redesigned version of Oski malware with enhanced functionality.


Stealing everything
-------------------


Mars Stealer uses a custom grabber that retrieves its configuration from the C2 and then proceeds to target the following applications:


**Internet apps:** Google Chrome, Internet Explorer, Microsoft Edge (Chromium Version), Kometa, Amigo, Torch, Orbitium, Comodo Dragon, Nichrome, Maxxthon5, Maxxthon6, Sputnik Browser, Epic Privacy Browser, Vivaldi, CocCoc, Uran Browser, QIP Surf, Cent Browser, Elements Browser, TorBro Browser, CryptoTab Browser, Brave, Opera Stable, Opera GX, Opera Neon, Firefox, SlimBrowser, PaleMoon, Waterfox, CyberFox, BlackHawk, IceCat, K-Meleon, Thunderbird.


**2FA apps:** Authenticator, Authy, EOS Authenticator, GAuth Authenticator, Trezor Password Manager.


**Crypto extensions:** TronLink, MetaMask, Binance Chain Wallet, Yoroi, Nifty Wallet, Math Wallet, Coinbase Wallet, Guarda, EQUAL Wallet, Jaox Liberty, BitAppWllet, iWallet, Wombat, MEW CX, Guild Wallet, Saturn Wallet, Ronin Wallet, Neoline, Clover Wallet, Liquality Wallet, Terra Station, Keplr, Sollet, Auro Wallet, Polymesh Wallet, ICONex, Nabox Wallet, KHC, Temple, TezBox Cyano Wallet, Byone, OneKey, Leaf Wallet, DAppPlay, BitClip, Steem Keychain, Nash Extension, Hycon Lite Client, ZilPay, Coin98 Wallet.


**Crypto wallets:** Bitcoin Core and all derivatives (Dogecoin, Zcash, DashCore, LiteCoin, etc), Ethereum, Electrum, Electrum LTC, Exodus, Electron Cash, MultiDoge, JAXX, Atomic, Binance, Coinomi.



![Wallets targeted by Mars Stealer](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/wallets.png)**Wallets targeted by Mars Stealer**  
*Source: 3xp0rt.com*
Moreover, Mars Stealer will capture and send the following basic information to the C2:


* IP and country
* Working path to EXE file
* Local time and time zone
* Language system
* Language keyboard layout
* Notebook or desktop
* Processor model
* Computer name
* User name
* Domain computer name
* Machine ID
* GUID
* Installed software and their versions

The only notable omission from the targeted application list is Outlook, which the malware authors will likely add in future releases.



![Custom Mars Stealer grabber](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Custom Mars Stealer grabber**  
*Source: 3xp0rt.com*
Evading detection
-----------------


Mars Stealer is a lean malware of just 95 KB in size, which attempts to evade security by using routines that hide API calls and string-encryption techniques using a combination of RC4 and Base64.


The information it collects is wrapped in memory, while all connections with the C2 are done with the SSL (Secure Sockets Layer) protocol, so they’re encrypted.


Moreover, the Mars Stealer code contains Sleep function intervals to perform timing checks that would result in a mismatch if a debugger is used.



![Anti-debugging sleep function](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Anti-debugging sleep function**  
*Source: 3xp0rt.com*
Finally, the malware can remove itself after the user data has been exfiltrated or when the operator decides to wipe it.


Functional checks
-----------------


Mars Stealer also checks if a user is based in countries historically part of the [Commonwealth of Independent States](https://www.nti.org/education-center/treaties-and-regimes/commonwealth-independent-states-cis/), which is common for many Russian-based malware.


If the device's language ID matches Russia, Belarus, Kazakhstan, Azerbaijan, Uzbekistan, and Kazakhstan, the program will exit without performing any malicious behavior.



![Language checks for target exclusion](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Language checks for target exclusion**  
*Source: 3xp0rt.com*
Moreover, the malware has to have a compilation date no older than a month than the system time; otherwise, it exits the execution process.


Currently, Mars Stealer is sold for $140 to $160 (extended version) on hacking forums, so it will likely get in the hands of numerous threat actors and be used in attacks in the future.





## Tags:

#### Threatactor:
[[threatactor.name=Sandworm Team]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Epic]] [[action.malware.name=Exodus]] [[action.malware.name=Net]] [[action.malware.name=Tor]] [[action.malware.name=Wiper]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Azerbaijan]] [[victim.continent.name=Asia]] [[victim.country.name=Kazakhstan]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Uzbekistan]] [[victim.continent.name=Asia]] [[victim.country.name=Belarus]] [[victim.continent.name=Europe]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[Oski]] [[3xp0rt.com]] [[Information-stealing]] [[C2]] [[Bleeping Computer]]

