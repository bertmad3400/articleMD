# Cyberattackers are now quietly selling off their victim's internet bandwidth
### Proxyware is yet another way for criminals to generate revenue from their victims.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/cyberattackers-are-now-quietly-selling-off-their-victims-internet-bandwidth/)
+ Date: August 31, 2021 -- 12:00 GMT (13:00 BST)
+ Author: Charlie Osborne


## Article:
Unknown

Cyberattackers are now targeting their victim's internet connection to quietly generate illicit revenue following a malware infection. 


On Tuesday, researchers from [Cisco Talos](https://blog.talosintelligence.com/2021/08/proxyware-abuse.html) said "proxyware" is becoming noticed in the cybercrime ecosystem and, as a result, is being twisted for illegal purposes.  

Proxyware, also known as internet-sharing applications, are legitimate services that allow users to portion out part of their internet connection for other devices, and may also include firewalls and [antivirus programs](https://www.zdnet.com/article/antivirus-software-explained/).  

Other apps will allow users to 'host' a hotspot internet connection, providing them with cash every time a user connects to it.  

It is this format, provided by legitimate services including Honeygain, PacketStream, and Nanowire, which is being used to generate passive income on behalf of cyberattackers and malware developers.  

According to the researchers, proxyware is being abused in the same way as legitimate [cryptocurrency mining](https://www.zdnet.com/article/170-android-cryptocurrency-mining-scam-apps-have-stolen-350000-from-users/) software: quietly installed -- either as a side component or as a main payload -- and with efforts taken to try and stop a victim from noticing its presence, such as through resource use control and obfuscation.  

In cases documented by Cisco Talos, proxyware is included in multi-stage attacks. An attack chain begins with a legitimate software program bundled together with a Trojanized installer containing malicious code. 






When the software is installed, the malware is also executed. One campaign has utilized a legitimate, signed Honeygain package which was patched to also drop separate, malicious files containing an XMRig cryptocurrency miner and to redirect the victim to a landing page connected to Honeygain referral codes.  

Once the victim signs up for an account, this referral earns revenue for an attacker -- all the while a cryptocurrency miner is also stealing computer resources.  

However, this isn't the only method used to generate cash. In a separate campaign, a malware family was identified that tries to install Honeygain on a victim's PC and registers the software under an attacker's account, and so any earnings are sent to the fraudster.  

"While Honeygain limits the number of devices operating under a single account, there is nothing to stop an attacker from registering multiple Honeygain accounts to scale their operation based on the number of infected systems under their control," the researchers say.  

Another variant exploited multiple avenues, bundling not only proxyware software, but also a cryptocurrency miner and information stealer for the theft of credentials and other valuable data.  

"This is a recent trend, but the potential to grow is enormous," Cisco Talos says. "We are already seeing serious abuse by threat actors that stand to make a significant amount of money off these attacks. These platforms also pose new challenges for researchers, since there is no way to identify a connection through these kinds of networks -- the origin IP becomes even less meaningful in an investigation." 

###  Previous and related coverage

* [Fujitsu says stolen data being sold on dark web 'related to customers'](https://www.zdnet.com/article/fujitsu-says-stolen-data-being-sold-on-dark-web-related-to-customers/)  

* [Parents of teens who stole $1 million in Bitcoin sued by alleged victim](https://www.zdnet.com/article/parents-of-teens-who-stole-1-million-in-bitcoin-sued-by-alleged-victim/)  

* [Google: Here's how our $10bn investment will boost US cybersecurity](https://www.zdnet.com/article/software-supply-chain-security-google-touts-its-10bn-investment-and-zero-trust-work/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Honeygain]] [[malware]] [[proxyware]] [[account,]] [[ZDNet]]
