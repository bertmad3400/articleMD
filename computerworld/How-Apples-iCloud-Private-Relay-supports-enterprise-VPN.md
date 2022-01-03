# How Apple's iCloud Private Relay supports enterprise VPN
### Apple's iCloud Private Relay is compatible with enterprise security policies, including VPN and proxy server prohibition.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3645848/how-apples-icloud-private-relay-supports-enterprise-vpn.html
+ Date: 2021-12-23T05:22-05:00
+ Author: Jonny Evans


## Article:
![Article Image](https://images.idgesg.net/images/article/2017/08/10_encrypt-for-security-100732873-large.jpg?auto=webp&quality=85,70)

Apple’s [iCloud Private Relay](https://apple.sjv.io/c/321564/435031/7613?subid1=US-011-3645848-000-000000-web&u=https://www.apple.com/privacy/docs/iCloud_Private_Relay_Overview_Dec2021.PDF) service gives users privacy, security, and convenience. It is best seen as a limited form of virtual private network (VPN) that protects a user’s [Safari browsing activity from prying eyes](https://www.applemust.com/apple-cloudflare-solve-huge-web-security-flaw/). But, is it compatible with your [enterprise’s existing VPN systems](https://www.computerworld.com/article/3621731/wwdc-why-icloud-will-help-secure-the-enterprise.html)?

*(TL;DR: Yes)*.

**iCloud Private Relay and enterprise VPN**
-------------------------------------------

Solid VPN usage statistics are relatively hard to find. [Security.org](https://www.security.org/resources/vpn-consumer-report-annual/) clams that two-thirds of Americans have used a VPN with around 38 million people making regular use of these tools. The move to working from home during the pandemic may have sparked an increase in such use, with [68% of companies](https://openvpn.net/covid-19-fast-tracks-virtualization-openvpn-study-reveals-remote-work-is-the-future/) beginning to or increasing their use of such services.

The inference is that more businesses than ever before now make use of VPN services, and they will need to know whether these are compatible with iCloud Private Relay.

The short answer is yes, they are compatible. Apple designed it this way.

“Private Relay is designed to provide clear status information and control to the user, and provide appropriate controls to enterprises and network operators that might require the ability to audit all traffic on their network,” the company explains in its [recently-published guide to the service](https://apple.sjv.io/c/321564/435031/7613?subid1=US-011-3645848-000-000000-web&u=https://www.apple.com/privacy/docs/iCloud_Private_Relay_Overview_Dec2021.PDF).

**How iCloud Private Relay works**
----------------------------------

At its simplest, iCloud Private Relay works by separating a user’s identity from the nature of their Safari web browsing session.

When they make a request to visit a site, the request is sent through two separate internet relays operated by two different entities.

* One (the ‘ingress proxy’) will handle the user’s original IP address but does not know the website name they are requesting.
* The other ‘egress proxy’ uses an assigned IP address that does not relate to the user to summon the site.
* The idea is that people cannot be directly connected to the sites they visit and that no one in the chain has access to that information.

The system is sufficient to support location-personalized web experiences but does not undermine regional content restrictions. So, if you want to watch U.S. Netflix from your luxury pad in Lisbon, Portugal, you’ll need to use a VPN. You should also take care to [scrutinize which VPN service you select](https://www.computerworld.com/article/3430899/many-vpn-apps-on-apple-s-app-store-can-t-be-trusted-researcher-warns.html).

The system has solid [TLS 1.3 security](https://www.cloudflare.com/en-gb/learning-resources/tls-1-3/) to encrypt what happens between the user’s device and the ingress and egress proxies. You can explore Apple’s online dedicated [Private Relay pages](https://support.apple.com/en-gb/HT212614) and its [recent document](https://apple.sjv.io/c/321564/435031/7613?subid1=US-011-3645848-000-000000-web&u=https://www.apple.com/privacy/docs/iCloud_Private_Relay_Overview_Dec2021.PDF) to gain more in-depth insight into the system. This [WWDC developer presentation](https://developer.apple.com/videos/play/wwdc2021/10096/) may also be of interest.

**How iCloud Private Relay supports existing enterprise VPNs**
--------------------------------------------------------------

It supports existing enterprise security systems (including VPNs) in the following ways:

* Private Relay only protects connections made using public internet servers.
* Private Relay allows users to access local or private servers (such as your company server) directly.
* If it detects that the server being used is not a public internet name, it will instruct the device to access the server directly over the local network.
* In a protection against spoofing attempts in which an attacker may choose to pose as a local network server to access data, the device never allows direct connections to names held on DuckDuckGo’s known tracker list.
* Private Relay will not try to proxy traffic that it recognizes as specific to the local network.
* Most managed networking settings as used by enterprises take precedence over Private Relay
* If a device has a VPN installed, traffic that goes through that VPN will not use Private Relay.
* Similarly, a proxy configuration, such as a Global Proxy, will be used instead of Private Relay.
* If your network forbids use of proxy servers, then iCloud Private Relay will not function.

What this all means is that if you are using a corporate VPN, iCloud Private Relay will ignore the internet transaction. And if you make use of a local network or global proxy server, or forbid use of proxy servers on your network, no protection will be put in place.

Another exception relates to those who use custom-encrypted DNS settings, as the specified DNS server will be used instead of Private Relay.

**What about MDM systems?**
---------------------------

If your business manages a fleet of devices, Apple has made it possible to enable or disable iCloud Private Relay using your MDM tools. It does this by allowing these systems to install and use management profiles on devices to disable use of iCloud Private Relay on them.

**What about network audits?**
------------------------------

Some industries require businesses to log network traffic, particularly in highly sensitive or heavily regulated sectors. If your business needs to audit network traffic, then it is possible to block access to Private Relay.

In the event use of the service is blocked on your network, a user will receive an error message to let them know they must disable Private Relay for that network or use another network.

Convincing your employees to use your network rather than another may be the biggest security challenge you find in consequence.

**What else should you know?**
------------------------------

With so many employees working remotely, it’s important to understand what iCloud Private Relay does not protect. While it will do a great job of securing a remote user’s browsing traffic when transacted on a public server using Wi-Fi or a wired internet connection, it does not protect traffic sent across cellular networks.

It is also important to note that only Safari sessions are protected. Traffic from apps, emails, or browsers is not. If you and/or your business needs to protect all your online traffic — apps, services, emails and so on — you’ll still need to use a VPN.

The service is pretty relevant. “As a result of its growth in the enterprise, Apple devices are now a bigger security threat target,” [Jamf Senior Manager Garrett Denney writes](https://www.jamf.com/blog/apples-wwdc-2021-day-one-recap/).

**How to enable and disable Private Relay**
-------------------------------------------

Private Relay is available to [iCloud+ subscribers](https://www.computerworld.com/article/3634029/what-is-icloud-and-why-should-you-use-it.html) running iOS 15, iPad OS 15 or macOS Monterey or later.

To enable it, open *Settings* (*System Preference*s on Mac), then open your *Apple ID>iCloud* section and toggle Private Relay to On. Or toggle it to off to disable the service.

*Please follow me on [Twitter](https://twitter.com/jonnyevans_cw), or join me in the [AppleHolic’s bar & grill](https://mewe.com/join/appleholics_bar_and_grill) and [Apple Discussions](https://mewe.com/join/apple_discussions) groups on MeWe.*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Spark]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Portugal]] [[victim.continent.name=Europe]] [[victim.city.name=Lisbon]] [[victim.country.name=Portugal]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Icloud]] [[Vpn]] [[Computerworld]]

