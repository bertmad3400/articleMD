# Ransomware decryptor roundup: BlackByte, Atom Silo, LockFile, Babuk decryptors released
### This follows the release of multiple decryptors over the past few months, including REvil/Sodinokibi.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/ransomware-decryptor-roundup-blackbyte-atom-silo-lockfile-babuk-decryptors-released/)
+ Date: November 1, 2021
+ Author: Jonathan Greig


## Article:
Unknown


Ransomware decryptors for the BlackByte, Atom Silo, LockFile and Babuk strains were released over the last two weeks, highlighting some amount of progress in the fight against a few of the smaller ransomware gangs.

Last week, security company Avast released three decryptors, including ones for those affected by the [AtomSilo, LockFile](https://www.bleepingcomputer.com/news/security/free-decryptor-released-for-atom-silo-and-lockfile-ransomware/) and [Babuk](https://www.avast.com/ransomware-decryption-tools#babuk) ransomware. Cybersecurity firm Trustwave released a decryptor for the [BlackByte ransomware](https://www.zdnet.com/article/blackbyte-ransomware-decryptor-released/) two weeks ago.  

Allan Liska, a ransomware expert with the Recorded Future security company, told *ZDNet* that while it often feels as though security teams are losing the fight against ransomware, there is progress being seen. 

"Since August, by my count, we have seen decryptors for BlackMatter, REvil, AtomSilo, Babuk, LockFile, BlackByte, Prometheus and Ragnarok (I'm probably missing some others)," Liska said.

When asked why there was a recent wave of decryptors being released, Liska attributed it to a number of factors.

"Security researchers at companies like Emsisoft are getting better at finding flaws in ransomware and writing decryptors. And, communication between security companies on ransomware is increasing, so we are sharing information privately that helps victims," Liska said.

"We can't discount the impact that 10 law enforcement actions against ransomware groups is also having. These actions, [like the ones recently](https://www.zdnet.com/article/ransomware-police-sting-targets-suspects-behind-1800-attacks-that-wreaked-havoc-across-the-world/), raise the cost of ransomware operations, and many third and fourth-tier ransomware groups are deciding it is no longer worth the risk. So, they 'retire' and release their keys, making it easier to create decryptors."






BreachQuest CTO Jake Williams noted that each of the most recent ransomware decryptors released was enabled by operational security or programming mistakes made by the threat actors. 

Security teams, he added, had little to do with this recent wave of decryptors other than the possibility that they were getting better at operationalizing available data.

"The LockFile/AtomSilo decryptor targets weaknesses in the implementation of the cryptographic algorithm used to encrypt the files. The same is true for BlackByte. In the case of Babuk, the decryptor was enabled by a source code dump in September. It's worth noting that any encryptions performed by Babuk after the source code dump probably can't be decrypted by the tool. This is because the master key has been changed after leaking in the dump," Williams explained.

When asked which recent decryptor would be the most consequential, Williams said that without a doubt, it would be Babuk. 

"This wasn't enabled by any cryptographic weaknesses and instead required a leak. The fact that the ransomware source code leaked at all is likely driving anxiety in the ransomware operator community, which in recent months has also seen the leak of the Conti ransomware affiliate handbook and successful law enforcement action against REvil," Williams told *ZDNet*. 

Like Digital Shadows' Ivan Righi, other experts said malware analysts are improving and capitalizing on mistakes or weaknesses in threat actors' encryption processes. 

Ransomware has been a big focus for many security teams in 2020 and 2021, and the more resources that are invested into fighting against ransomware, the smaller the room for mistakes is from a cybercriminal's perspective, Righi said. 

Over the last few years, the wealth brought in by certain ransomware gangs has attracted multiple threat actors, some of whom are not as sophisticated as others.

"As the number of ransomware variants continues to pile up, it is no surprise that we will begin to find weaknesses in some of these ransomware variants, which may allow for decryption keys to be extracted," Righi said. 

Of all the decryptors released over the past few months, the universal decryptor for victims of the Kaseya VSA supply-chain attack stood out most to Righi.

[Released in September by Bitdefender](https://www.zdnet.com/article/bitdefender-releases-universal-decryptor-for-revilsodinokibi-victims-hit-before-july-13/), the universal decryptor only works for REvil/Sodinokibi victims infected before July 13, 2021. Hundreds of victims were helped with the decryptor after the group [went dark yet again last month](https://www.zdnet.com/article/revil-ransomware-operators-claim-group-is-ending-activity-again-happy-blog-now-offline/). It was later revealed that law enforcement officials from multiple countries [were involved in disrupting the REvil ransomware gang](https://www.zdnet.com/article/multiple-governments-involved-in-coordinated-takedown-of-revil-ransomware-group-reuters/).

But Righi noted that just because a decryptor is released, that doesn't mean a ransomware gang is necessarily finished. 

"The release of a decryptor for a ransomware variant does not mean the end of that ransomware group. DarkSide had a decryptor released in January 2021, but the group simply improved its tools and continued attacks until May 2021, when the Colonial Pipeline attack occurred," Righi said. "However, the release of decryptors may damage a group's reputation and ability to attract new affiliates."





#### Tags:
[[ransomware]] [[decryptor]] [[decryptors]] [[Righi]] [[Babuk]] [[Liska]] [[said.]] [[ZDNet]]
