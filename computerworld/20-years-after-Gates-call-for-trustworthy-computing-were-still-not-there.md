# 20 years after Gates’ call for trustworthy computing, we’re still not there
### Then-Microsoft CEO Bill Gates spelled out what his company needed to do to build in better security two decades ago. And yet….

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3647289/20-years-after-gates-call-for-trustworthy-computing-we-re-still-not-there.html
+ Date: 2022-01-17T03:42-05:00
+ Author: Susan Bradley


## Article:
![Article Image](https://images.idgesg.net/images/idge/imported/imageapi/2022/01/11/12/internet_security_privacy-100715273-large-100916002-large.jpg?auto=webp&quality=85,70)

Do you feel more secure? Is your computing experience more trustworthy these days?

Seriously — you’re reading this article on a computer or phone, connecting to this site on an internet shared with your Grandma as well as Russian hackers, North Korean attackers, and lots of teenagers  looking at TikTok videos. It’s been 20 years since then-Microsoft CEO Bill Gates wrote his [Trustworthy Computing memo](https://www.wired.com/2002/01/bill-gates-trustworthy-computing/) where he emphasized security in the company’s products.

So are we actually more secure now?

I’m going to keep in mind the side effects from last week’s Patch Tuesday security updates and consider them in my answer. First, the good news: I don’t see major side effects occurring on PCs not connected to active directory domains (and I haven’t seen any showstoppers in testing my hardware at home). I can still print to my local HP and Brother printers. I can surf and access files. So, while I’m not ready yet to give an all-clear to install the January updates, when I do, I doubt you’ll see side effects.

But for businesses, this month’s updates deliver a confusing and murky story. Microsoft has not exactly been a good trustworthy computing partner this month. Rather taking the past two decades to develop  bullet-proof, resilient systems, we get servers going into boot loops and admins having to boot into DOS  mode and run commands to uninstall updates.

This isn’t where we were supposed to be at this point.

As Gates said 20 years ago: “Availability: Our products should always be available when our customers need them. System outages should become a thing of the past because of a software architecture that supports redundancy and automatic recovery. Self-management should allow for service resumption without user intervention in almost every case.”

And yet, I’m still delaying updates on my computer systems because the latest updates, in particular, have shown that servers may have recovery issues. Case in point: “Windows Servers domain controllers might restart unexpectedly.” That cropped up after last week’s security patches on all supported Windows server platforms. As noted in the [known-issue write-up](https://docs.microsoft.com/en-us/windows/release-health/status-windows-8.1-and-windows-server-2012-r2#2775msgdesc), this occurs after using Microsoft’s own recommended guidance for Active Directory hardening, which included using Shadow Principals in Enhanced Security Admin Environment (ESAE) or environments with Privileged Identity Management (PIM). The systems affected include Windows Server 2022 ([KB5009555](https://support.microsoft.com/en-us/topic/january-11-2022-kb5009555-os-build-20348-469-e3fb2b38-3506-4dc9-8216-5d3546a6d2a4)); Windows Server, version 20H2 ([KB5009543](https://support.microsoft.com/en-us/topic/january-11-2022-kb5009543-os-builds-19042-1466-19043-1466-and-19044-1466-b763552f-73bd-435a-b220-fc3e0bc9765b)); Windows Server 2019 ([KB5009557](https://support.microsoft.com/en-us/topic/january-11-2022-kb5009557-os-build-17763-2452-c3ee4073-1e7f-488b-86c9-d050672437ae)); Windows Server 2016 ([KB5009546](https://support.microsoft.com/en-us/topic/january-11-2022-kb5009546-os-build-14393-4886-0c2cac57-13b6-42e6-b318-41ca32428f91)); Windows Server 2012 R2 ([KB5009624](https://support.microsoft.com/en-us/topic/january-11-2022-kb5009624-monthly-rollup-23f4910b-6bdd-475c-bb4d-c0e961aff0bc)) Windows Server 2012 ([KB5009586](https://support.microsoft.com/en-us/topic/january-11-2022-kb5009586-monthly-rollup-9541f57c-89b0-48d6-ade2-31609678ce9b)).  

I’ve also seen reports that following the Active Directory security hardening guidance (created after the [November security releases](https://msrc-blog.microsoft.com/2021/12/14/ad-hardenings/)) will trigger the reboot problem if you’ve [set the PACRequestorEnforcement value to 2](https://blog.netwrix.com/2022/01/10/pacrequestorenforcement-and-kerberos-authentication/).

Even with cloud services, the issues around availability remain unsolved. For example, Microsoft 365 has a [Twitter account](https://twitter.com/MSFT365Status) whose entire focus is communicating on availability issues with the service. Rarely a week goes by that I don’t get an alert about some service issue. Cloud services are hardened, but I don’t see a lot of progress either with local servers or cloud services. Instead of planning on automatic recovery, we have to make sure we have alternative services and alternative ways to communicate should our systems be hit either by patching or by ransomware.

More from Gates: “Security: The data our software and services store on behalf of our customers should be protected from harm and used or modified only in appropriate ways. Security models should be easy for developers to understand and build into their applications.”

And yet, last week’s security releases included confusing communication regarding a potentially wormable flaw. The https bug in the form of CVE-2022-21907 is [not clear on which versions are vulnerable](https://twitter.com/wdormann/status/1480972462812770305). Clarification and analysis had to come from external sources before we could [figure out Windows 10 version 1809 and Server 2019 are not vulnerable](https://attackerkb.com/topics/xlCKfuW3a8/cve-2022-21907?referrer=profile) by default — unless the HKLM:\System\CurrentControlSet\Services\HTTP\Parameter\EnableTrailerSupport registry key is set to 1. Versions of Windows 10 after 1809 *are* vulnerable by default. I’d argue that 20 years after the release of the trustworthy computing memo, our security models — and just as importantly, our security communication — still aren’t easy to understand.

We’re also tracking [issues with HyperV servers on Server 2012R2](https://docs.microsoft.com/en-us/windows/release-health/status-windows-8.1-and-windows-server-2012-r2#2776msgdesc) (and, it appears, only that platform) where virtual machines fail to start after applying KB5009624 on devices using UEFI. If you have any virtual servers hosted on Server 2012R2, hold back on installing updates on those platforms.

And users of Windows 10 workstations that rely on Virtual Private Networks for remote access are having to uninstall the January updates due to a side effect that breaks VPN access on Windows 10 or Windows 11 systems. For those who rely on L2TP VPN or IPsec VPN, you will [fail to connect using VPN](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#2773msgdesc) after installing the updates.

Gates closed out his memo with this: “Going forward, we must develop technologies and policies that help businesses better manage ever larger networks of PCs, servers and other intelligent devices, knowing that their critical business systems are safe from harm. Systems will have to become self-managing and inherently resilient. We need to prepare now for the kind of software that will make this happen, and we must be the kind of company that people can rely on to deliver it.” 

So how did that work out? We’re in the same place we were 20 years ago; we still have to rely on ourselves to decide on the right time to install updates.

So how do you really feel about security? Join the discussion in the [AskWoody forums](https://www.askwoody.com/forums/topic/trustworthy-computing-memo-is-20-years-old/)!





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=North Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Vpn]] [[Microsoft]] [[Computerworld]]
#### CVE's
[[CVE-2022-21907]]

