# Meris botnet assaults KrebsOnSecurity
### The botnet appears to be made up of compromised routers.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/meris-botnet-assaults-krebsonsecurity/)
+ Date: September 15, 2021 -- 09:27 GMT (10:27 BST)
+ Author: Charlie Osborne


## Article:
Unknown

KrebsOnSecurity is often the target of disgruntled cybercriminals and has now been targeted by a large and powerful botnet. 


The website, operated by security expert Brian Krebs, was [subject to an assault](https://krebsonsecurity.com/2021/09/krebsonsecurity-hit-by-huge-new-iot-botnet-meris/) by the "Meris" botnet on Thursday evening.  

Meris is a new botnet on the scene which is powered by Internet of Things (IoT) devices. IoT products, PCs, home gadgets -- including cameras, VCRs, TVs, and routers -- that are hijacked become slave nodes in a botnet's network and are then can be used to conduct distributed denial-of-service (DDoS) attacks, among other functions.  

In this case, Meris is composed of a huge number of MikroTik routers. According to [Qrator Labs and Yandex](https://blog.qrator.net/en/meris-botnet-climbing-to-the-record_142/), Meris first appeared in late June and is still growing.  

Meris may bring Mirai to mind, a botnet famous for taking down large swathes of the internet in 2016, but the team says this may not be the right comparison to make at this time. 

"Some people and organizations already called the botnet "a return of Mirai," which we do not think to be accurate," Qrator Labs says. "Mirai possessed a higher number of compromised devices united under C2C, and it attacked mainly with volumetric traffic." 

Mirai's source code was later leaked, [causing many variants](https://www.zdnet.com/article/this-new-variant-of-mirai-botnet-malware-is-targeting-network-attached-storage-devices/) to appear that are still in operation.






Krebs says that the DDoS attack, albeit "mercifully brief," was larger than the one launched against [KrebsOnSecurity in 2016](https://krebsonsecurity.com/2016/09/the-democratization-of-censorship/) by a Mirai operator. The attack was large enough that Akamai, which had fended off past attacks against Krebs pro-bono, had to unmoor the domain in light of the potential ramifications for other clients.  

The security expert says the volume of junk traffic launched by the botnet was more "than four times" that of Mirai, reaching over two million requests-per-second.  

The domain is now protected under Google's [Project Shield](https://projectshield.withgoogle.com/).  

It is also suspected that Meris is behind two other major attacks this year, that of search engine Yandex last week, and a substantial attack against [Cloudflare in July](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/), clocking in at 17.2 million request-per-second. 

MikroTik has [issued a statement](https://forum.mikrotik.com/viewtopic.php?f=21&t=178417) on the botnet, noting that the compromise of its devices appears to stem from a vulnerability patched in RouterOS in 2018, rather than a zero-day or new vulnerability.  

"Unfortunately, closing the vulnerability does not immediately protect these routers," the company said. "If somebody got your password in 2018, just an upgrade will not help. You must also change [your] password, re-check your firewall [so] it does not allow remote access to unknown parties, and look for scripts that you did not create. We have tried to reach all users of RouterOS about this, but many of them have never been in contact with MikroTik and are not actively monitoring their devices. We are working on other solutions too." 

###  Previous and related coverage

* [This ransomware-spreading malware botnet just won't go away](https://www.zdnet.com/article/this-ransomware-spreading-malware-botnet-just-wont-go-away/)  

* [This is why the Mozi botnet will linger on](https://www.zdnet.com/article/this-is-why-the-mozi-botnet-will-linger-on/)  

* [Now this botnet is hunting for unpatched Microsoft Exchange servers](https://www.zdnet.com/article/now-this-botnet-is-hunting-for-unpatched-microsoft-exchange-servers/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[botnet]] [[Meris]] [[MikroTik]] [[Mirai]] [[ZDNet]]
