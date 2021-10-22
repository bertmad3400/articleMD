# Hackers somehow got their rootkit a Microsoft-issued digital signature
### FiveSys rootkit somehow used a valid digital signature to help bypass cybersecurity measures in order to steal usernames and passwords from victims.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/hackers-somehow-got-their-rootkit-a-microsoft-issued-digital-signature/)
+ Date: October 22, 2021
+ Author: Danny Palmer


## Article:
Unknown

Cybersecurity researchers [at Bitdefender](https://www.bitdefender.com/blog/labs/digitally-signed-rootkitsare-back-a-look-atfivesys-and-companions/) have detailed how cyber criminals have been using FiveSys, a rootkit that somehow made its way through the driver certification process to be digitally signed by Microsoft.  

The valid signature enables the rootkit – [malicious software](https://www.zdnet.com/article/what-is-malware-everything-you-need-to-know-about-viruses-trojans-and-malicious-software/) that allows cyber criminals to access and control infected computers – to appear valid and bypass operating systems restrictions and gain what researchers describe as "virtually unlimited privileges". 

It's known for cyber criminals to use stolen digital certificates, but in this case, they've managed to acquire a valid one. It's a still a mystery how cyber criminals were able to get hold of a valid certificate. 

"Chances is that it was submitted for validation and somehow it got through the checks. While the digital signing requirements detect and stop most of the rootkits, they are not foolproof," Bogdan Botezatu, director of threat research and reporting at Bitdefender told ZDNet. 

It's uncertain how FiveSys is actually distributed, but researchers believe that it's bundled with [cracked software downloads](https://www.zdnet.com/article/this-password-stealing-windows-malware-is-distributed-via-ads-in-search-results/). 

**SEE:**[**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/)**(ZDNet special report)**

Once installed, FiveSys rootkit redirects internet traffic to a proxy server, which it does by installing a custom root certificate so that the browser won't warn about the unknown identity of the proxy. This also blocks other malware from writing on the drivers, in what's likely an attempt to stop other cyber criminals from taking advantage of the compromised system. 






Analysis of attacks shows that FiveSys rootkit is being used in cyber attacks targeting online gamers, with the aim of stealing login credentials and the ability to hijack in-game purchases. 

[The popularity of online games](https://www.zdnet.com/article/security-blocking-the-path-that-leads-from-gaming-cheats-to-malware/) means that a lot of money can be involved - not only because banking details are connected to accounts, but also because prestigious virtual items can fetch large sums of money when sold, meaning attackers could exploit access to steal and sell these items. 

Currently, the attacks are targeting gamers in China – which is where researchers also believe that the attackers are operating from.  

The campaign started slowly in late 2020, but massively expanded during the course of summer 2021. The campaign is now blocked after researchers at Bitdefender flagged the abuse of digital trust to Microsoft, which revoked the signature. ZDNet contacted Microsoft but hadn't received a response at the time of publication. 

While the rootkit is currently being used to steal login credentials from gaming accounts, it's possible that it could be directed at other targets in future. But by taking some relatively simple cybersecurity precautions, it's possible to avoid falling victim to this or similar attacks. 

"In order to stay safe, we recommend that users only download software from the vendor's website or from trusted resources. Additionally, modern security solutions can help detect malware - including rootkits – and block their execution before they are able to start," said Botezatu. 

**MORE ON CYBERSECURITY**

* [**This password-stealing Windows malware is distributed via ads in search results**](https://www.zdnet.com/article/this-password-stealing-windows-malware-is-distributed-via-ads-in-search-results/)
* [**Gaming mods, cheat engines are spreading Trojan malware and planting backdoors**](https://www.zdnet.com/article/gaming-tools-backdoored-cheat-engines-are-now-new-weapons-in-cyberattacks/)
* [**Best antivirus software for 2021**](https://www.cnet.com/tech/services-and-software/best-antivirus/)
* [**A company spotted a security breach. Then investigators found this new mysterious malware**](https://www.zdnet.com/article/a-company-spotted-a-security-breach-then-investigators-found-this-new-mysterious-malware/)
* [**Digital transformation is creating new security risks, and businesses can't keep up**](https://www.zdnet.com/article/digital-transformation-is-creating-new-security-risks-and-businesses-cant-keep-up/)





#### Tags:
[[rootkit]] [[malware]] [[Bitdefender]] [[FiveSys]] [[ZDNet]]
