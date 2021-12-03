# Store your corporate card on an iPhone? Uh-oh
### Apple, Google, and especially Visa this month have given us yet another example of how security and convenience are at odds in the mobile world. Convenience seems to have won out.


## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3640715/store-your-corporate-card-on-an-iphone-uh-oh.html
+ Date: 2021-11-15
+ Author: Evan Schuman


## Article:
![Article Image](https://images.techhive.com/images/article/2015/09/thinkstockphotos-484198990-100611992-large.jpg?auto=webp&quality=85,70)

Apple and Google (and especially Visa) last week gave us yet another example of how security and convenience are often at odds with each other. And it looks like they opted for convenience.

The latest issue speaks to only a subset of iPhone and Android users — specifically, those who use their phones for mass transit payments. If you think of how subways work in a major city (I’ll use New York City as an example), they require extreme speed. Using facial recognition or entering a PIN right before paying to get on the subway would dramatically slow down the line. 

Instead of allowing authentication to happen earlier — say, perhaps within five minutes of a transaction — or by accelerating the process to a split second, Apple, Google, and Visa apparently chose to forego any meaningful authentication. (Note: I am focusing on Visa because the hole still exists for it. MasterCard and others have already patched the flaw.)

Security researchers at [Positive Technologies](https://www.ptsecurity.com/ww-en/) tested the phones and found the problem. 

“The flaws allow attackers to make unlimited purchases using stolen smartphones with enabled express transport schemes that do not require unlocking the device to make a payment,” [Positive said in a statement](https://www.ptsecurity.com/ww-en/about/news/positive-technologies-vulnerabilities-in-apple-pay-samsung-pay-and-google-pay-allow-attackers-to-make-unauthorized-purchases/). “Until June 2021, рurchases could be made at any PoS terminals, not only in public transport. On iPhones, payments could be made even if the phone's battery is emptied. Prior to 2019, Apple Pay and Samsung Pay did not allow payments unless the phone was unlocked with a fingerprint, facial ID, or PIN code. But today, it has become possible by using public transport schemes or Apple's Express Transit mode.”

Timur Yunosov, a Positive researcher, said in an interview that the risk still exists, but varies based on the combination of payment card brand (Visa, MasterCard, American Express, etc.) and device type.

“If you use a Visa card on Apple Pay, anyone could take your phone — even uncharged — go to a luxury shop and buy something with your phone. Before June 2021, the same could have happened with the Samsung Pay/MasterCard pair,” said Yunosov, who spoke last week at [Black Hat Europe](https://www.blackhat.com/eu-21/briefings/schedule/#hand-in-your-pocket-without-you-noticing-current-state-of-mobile-wallet-security-24739). “But at some point, they silently fixed the issue. Google Pay is most at risk. If the NFC is enabled, someone could even clone your MasterCard card within a short period of time and use it later to buy goods. Even after all the changes that MasterCard made, it’s still a possibility for fraud against lost mobile wallets (Apple, Samsung, Visa, MasterCard, AMEX), although it requires special equipment, such as a modified POS or direct access to the transaction stream."

Given that this involves stolen devices, this raises a difficult IT question. For many enterprises, standard IT protocol when a device is labeled “likely stolen” is to remote wipe it, theoretically removing any further risk. But that may not work if the phone is not connected to the internet, is shut down or has a dead battery. 

“If the phone is uncharged, it's still possible to use it for identification. So information would not be wiped from the device. It also depends if the wiping mechanisms include deleting records from the security systems (e.g., a database of devices that belong to employees), it would be secure,” Yunosov said. “Otherwise, it might put the whole system at risk. Until we see these systems being implemented in big companies, this is all just speculation.”

There is some good news — albeit temporarily, in theory. Other sensitive data on the phone should not be at risk. And if it is, a remote wipe *should* resolve issue, assuming that a proper remote wipe connection can be made.

But, as Yunosov pointed out, this flaw may get a lot worse. Apple is preparing a series of new “value additional services,” such as ways to access secure buildings. For speed and convenience, it might also use the same process in place for transit payments. That increases the universe of potential victims.

Another key issue: What happens if a thief does indeed make fraudulent purchases using the phone? Proving that the charges are fraudulent might be tricky. “It would be extremely hard to prove to your issuing bank that you didn't pay for these things and that the phone was not unlocked with your fingerprint or PIN,” Yunosov said. 

Some victims might get lucky if there is a security camera filming the person making the purchase or if the victim can prove that they were somewhere else at the time of the theft. 

It seems as if Apple could leverage the Apple Watch here. What if your Apple Watch constantly notes how far it is from the iPhone? And what if, at a predetermined distance, the watch allowed the user to disable the phone, either temporarily or permanently? It’s important to give a user the option to temporarily disable; that’s where the difference between a lost phone and a stolen phone kicks in. 

The Watch could also tell the user exactly where the phone appears to be — or at least where it was when last detected. That information would help the user determine whether the phone is simply misplaced or has likely been stolen.

At the very least Apple, Google, and financial institutions need to remember that convenience shouldn't come at the cost of security. Because slowing down the subway line might be inconvenient, but dealing with fraud and theft is worse.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]]

#### Industry:
[[victim.industry.name=Finance]]

#### Location:
[[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Mastercard]] [[Yunosov]] [[Google]] [[Samsung]] [[Computerworld]]

