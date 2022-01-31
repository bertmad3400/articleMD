# 277,000 routers exposed to Eternal Silence attacks via UPnP
### A malicious campaign known as 'Eternal Silence' is abusing Universal Plug and Play (UPnP) turns your router into a proxy server used to launch malicious attacks while hiding the location of the threat actors.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/277-000-routers-exposed-to-eternal-silence-attacks-via-upnp/
+ Date: 2022-01-31T10:40:46-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/08/06/Router.jpg)

![router](https://www.bleepstatic.com/content/hl-images/2021/08/06/Router.jpg?rand=2058127415)


A malicious campaign known as 'Eternal Silence' is abusing Universal Plug and Play (UPnP) turns your router into a proxy server used to launch malicious attacks while hiding the location of the threat actors.


UPnP is a connectivity protocol optionally available in most modern routers that allows other devices on a network to create port forwarding rules on a router automatically. This allows remote devices to access a particular software feature or device as necessary, with little configuration required by a user.


However, it is yet another technology that [trades convenience for security](https://www.bleepingcomputer.com/news/security/unpatched-upnp-enabled-devices-left-exposed-to-attacks/), especially when the UPnP implementation is [potentially vulnerable](https://www.bleepingcomputer.com/news/security/callstranger-upnp-bug-allows-data-theft-ddos-attacks-lan-scans/) to attacks allowing remote actors to add UPnP port-forwarding entries via a device's exposed WAN connection.


Researchers from Akamai have spotted actors abusing this vulnerability to create proxies that hide their malicious operations, calling the attack [UPnProxy](https://www.akamai.com/content/dam/site/en/documents/research-paper/upnproxy-blackhat-proxies-via-nat-injections-white-paper.pdf).


Out of 3,500,000 UPnP routers found online, 277,000 are vulnerable to UPnProxy, and 45,113 of them have already been infected by hackers.


A new family of injections
--------------------------


Akamai's analysts speculate that the actors attempt to exploit EternalBlue (CVE-2017-0144) and EternalRed (CVE-2017-7494) on unpatched Windows and Linux systems, respectively.


Leveraging these flaws can lead to an array of potential problems, including resource-consuming cryptominer infections, devastating worm-like attacks that quickly spread to entire corporate networks, or initial access to corporate networks.


The new rulesets defined by the hackers contain the phrase 'galleta silenciosa', which is Spanish for 'silent cookie'.



```
{"NewProtocol": "TCP", "NewInternalPort": "445", "NewInternalClient": "192.168.10.212",

"NewPortMappingDescription": "galleta silenciosa", "NewExternalPort": "47669"}
```

The injections attempt to expose TCP ports 139 and 445 on devices connected to the targeted router, roughly 1,700,000 machines running SMB services.


Akamai is unsure about the success rate of this campaign, but observed a systematic approach to the scans, targeting devices that utilize static ports and paths for their UPnP daemons to inject port forwards.


Eternal exploits
----------------


Akamai's analysts speculate that the actors attempt to exploit EternalBlue (CVE-2017-0144) and EternalRed (CVE-2017-7494) on unpatched Windows and Linux systems respectively.


Leveraging these flaws can lead to an array of potential problems, including resource-consuming cryptominer infections, devastating worm-like attacks that quickly spread to entire corporate networks, or initial access to corporate networks.


"Because there is a decent possibility that (vulnerable) machines unaffected by the first round of EternalBlue and EternalRed attacks were safe only because they weren't exposed directly to the internet. They were in a relatively safe harbor living behind the NAT," explains [Akamai's report](https://www.akamai.com/blog/security/upnproxy-eternal-silence)


"The EternalSilence attacks remove this implied protection granted by the NAT from the equation entirely, possibly exposing a whole new set of victims to the same old exploits."


Defending against Eternal Silence
---------------------------------


'Eternal Silence' is a very cunning attack because it renders the practice of network segmentation ineffective and doesn't give any indication of what is happening to the victim.


The best way to determine if your devices have been captured is by scanning all endpoints and auditing the NAT table entries.


There are many ways to do this, but Akamai has conveniently provided this [bash script](https://www.akamai.com/blog/security/upnproxy-eternal-silence#:~:text=Below%20is%20a%20simple%20bash%20script%20used%20during%20this%20research) (screenshot below), which can be run against a potentially vulnerable URL.


![](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/bash.jpg)


If you've located a device compromised with Eternal Silence, disabling UPnP won't clear the existing NAT injections. Instead, users will need to reset or flash the device. 


Also, applying the latest firmware update should be a priority as the device vendor may have addressed any UPnP implementation flaws via a security update.





## Tags:

#### Threatactor:
[[threatactor.name=Equation]] [[threatactor.name=RTM]] [[threatactor.name=Silence]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=route]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Upnp]] [[Eternalblue]] [[Eternalred]] [[Bleeping Computer]]
#### ipv4-adresses
192.168.10.212
#### CVE's
[[CVE-2017-0144]] [[CVE-2017-7494]]

