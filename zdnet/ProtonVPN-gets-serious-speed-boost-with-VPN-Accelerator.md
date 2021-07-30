# ProtonVPN gets serious speed boost with VPN Accelerator
### When push comes to shove, what you really want from a Virtual Private Network, such as ProtonVPN, is 1) privacy and 2) speed. The new ProtonVPN delivers on both.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/protonvpn-gets-serious-speed-boost-with-vpn-accelerator/)
+ Date: July 30, 2021 -- 13:14 GMT (14:14 BST)
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

[ProtonVPN](http://cnetpartner.go2cloud.org/aff_c?aff_id=1&offer_id=5&aff_sub=%5Bsubid_value%5D&url=https%3A%2F%2Fprotonvpn.com%2F) has long been a good [Virtual Private Network (VPN)](https://www.zdnet.com/article/how-to-use-a-vpn-to-protect-your-internet-privacy/) system. But, now that it's sped up its connection by up to 400%, it demands your attention.


This new speed boost "VPN Accelerator," is enabled by default on all ProtonVPN paid accounts and with all the ProtonVPN apps. It also works with all of ProtonVPN and is available for all users. VPN Accelerator will give you its speed boost no matter which VPN protocol you use:  [OpenVPN TCP](https://openvpn.net/faq/why-does-openvpn-use-udp-and-tcp/), OpenVPN UDP, Wireguard, or IKEv2 VPN protocols.

How? By making a variety of improvements. For example, to give the popular [OpenVPN](https://openvpn.net/) and other single-threaded protocols a kick in the pants, ProtonVPN has re-written OpenVPN so that multiple OpenVPN processes per server now run to take advantage of multi-core processors. That's a good start, but to further improve it, since by itself this doesn't properly load-balance OpenVPN processes, other code changes make sure the OpenVPN load is properly distributed between the multiple processes. Similar techniques were applied by other VPN protocols.

TCP, the internet's fundamental network protocol, overall throughput is inversely proportional to latency and packet loss. In English, the more slowdowns and data loss there is in a connection, the slower the connection will go. In practical terms, the farther away a server is from you, the more likely it is you'll have poor latency and lose data packets. The result is lower network speeds. This isn't a VPN problem, it's just the nature of the internet. But, VPNs tend to amplify this program by increasing the distance of the end-to-end path from your device to the final server. 

As Andy Yen, ProtonVPN's co-founder explained, "To give an extreme example, if you were in Switzerland, connected to a server in New Zealand, and visited a website in the US, [your traffic would travel most of the way around the world](https://protonvpn.com/blog/vpn-accelerator/), resulting in approximately 600 ms of [round trip delay (RTD)](https://www.da-rz.de/en/glossary/round-trip-delay-rtd-latency/) latency."

To address this issue, ProtonVPN breaks up the 600 ms path into shorter paths. This gives you much faster throughput along each of the shorter paths. The net result is better-combined performance over the entire connection. 

To squeeze even more speed from the connection, VPN Accelerator also uses the TCP delay-controlled flow control algorithm [BBR](https://datatracker.ietf.org/doc/html/draft-cardwell-iccrg-bbr-congestion-control-00) on longer paths or congested networks, which suffer from packet loss. BBR recovers faster and ramps up quicker once a data transfer starts. 






How important is this? According to Yen, "For high latency servers, or when there is packet loss, the performance increase can be game-changing. … Even with just 1.5% packet loss, [BBR provides a 100x performance improvement](https://atoonk.medium.com/tcp-bbr-exploring-tcp-congestion-control-84c9c11dc3a9) compared to other congestion control algorithms." That's impressive.

ProtonVPN also did some tuning on Linux's TCP congestion algorithms and protocol-specific issues that can lead to networking socket stalls. The program also now circumvents the normal packet processing path for "known traffic." This significantly increases speed while decreasing latency. 

Finally, as before, ProtonVPN doesn't use virtual machines (VM)s or containers. Instead, its entire infrastructure runs on bare-metal servers. This eliminates forwarding encrypted packets between VMs or containers and their host machines. This also reduces latency and boosts speed.

When you put it all together, as a user you'll see the greatest gains when you access a site located far away from you. When you connect to a server that's close by, you may not see significant speed improvements. But, you don't have to worry about that. ProtonVPN does all this invisibly and automatically. 

In practice, I found ProtonVPN delivered the speed goods when I used it from my home office in Asheville, NC to connect with sites in the Netherlands, the United Kingdom, Japan, and New Zealand. The speed increase wasn't as noticeable, however, when I used it to connect with sites in the States. 

If this sounds like ProtonVPN's developers really know their networking stuff it's because they do. The company was founded by [CERN (European Center for Nuclear Research)](https://home.cern/) engineers and scientists who wanted to protect activists and journalists with the best possible technical protection. Besides technology, ProtonVPN is based in Switzerland with its very strong privacy laws.

ProtonVPN will run on pretty much any platform you want to use it on. It comes with a [variety of service levels and prices](https://protonvpn.com/pricing). It also has a free tier.


I usually recommend avoiding free VPN services, but I'll make an exception for ProtonVPN. While this service only offers 23 servers in 3 countries with a single speed-limited VPN connection, it doesn't throttle your traffic. You can use it for free all year round. 

Next up is [ProtonVPN Basic](http://cnetpartner.go2cloud.org/aff_c?aff_id=1&offer_id=5&aff_sub=%5Bsubid_value%5D&url=https%3A%2F%2Fprotonvpn.com%2Fpricing). This costs $5 per month or $4 a month on the $48 annual plan. With this tier, you can use 350+ servers in 40+ countries. P2P and BitTorrent file sharing are also allowed at this tier and you get access to the NetShield adblocker.

At the top, you'll find the [ProtonVPN Plus](http://cnetpartner.go2cloud.org/aff_c?aff_id=1&offer_id=5&aff_sub=%5Bsubid_value%5D&url=https%3A%2F%2Fprotonvpn.com%2Fpricing) plan. For this level of network protection, you'll pay $10 a month or $8 a month with a yearly $96 plan. With this plan, you can use 1200+ servers in 55 countries with over 10 simultaneous VPN connections. It also supports internet speeds of up to 10 Gbps. I wish I could get speeds like that! This level also supports streaming services. Finally, it also includes Secure Core VPN, which bounces your traffic across ProtonVPN servers to make it even harder to track, and [TOR over VPN](https://protonvpn.com/blog/tor-vpn/), which uses the [TOR](https://www.torproject.org/) network to further hide your online tracks. 

In addition, for $288 a year, the Visionary plan gives you everything you get with Plus and a [ProtonMail Visionary email](https://protonmail.com/support/knowledge-base/paid-plans/) account. This is a high-security email plan. It provides you with end-to-end encryption and zero-access encrypted email. Only you and the people you send messages to can read your mail. No one else can, including Proton.  

So, if you're really serious about security and you want good VPN performance as well I recommend you give ProtonVPN a try. They're, in a word, impressive. 

**Related Stories:**

* [Apple has a problem with ProtonVPN wanting to challenge governments](https://www.zdnet.com/article/apple-has-a-problem-with-protonvpn-wanting-to-challenge-governments/)
* [ProtonVPN apps handed to open source community in transparency push](https://www.zdnet.com/article/protonvpn-apps-handed-to-open-source-community-in-transparency-security-push/)
* [Best VPN 2021: Top VPN services reviewed](https://www.zdnet.com/article/best-vpn/)





#### Tags:
[[ProtonVPN]] [[VPN]] [[OpenVPN]] [[plan.]] [[But,]] [[connection,]] [[BBR]] [[ZDNet]]
