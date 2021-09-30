# Keep Attackers Out of VPNs: Feds Offer Guidance
### The NSA and CISA issued guidance on choosing and hardening VPNs to prevent nation-state APTs from weaponizing flaws & CVEs to break into protected networks.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175150)
+ Date: September 29, 2021  7:10 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/29190943/no-trespassing-sign-department-of-national-defence-department-e1632956995628.jpeg)
Unsecured VPNs can be a hot mess: Just ask Colonial Pipeline (which [got pwned](https://threatpost.com/darkside-pwned-colonial-with-old-vpn-password/166743/) by the REvil ransomware crooks with an old VPN password) or the 87,000 ([at least](https://www.bleepingcomputer.com/news/security/hackers-leak-passwords-for-500-000-fortinet-vpn-accounts/)) Fortinet customers whose credentials for unpatched SSL-VPNs were [posted online](https://threatpost.com/thousands-of-fortinet-vpn-account-credentials-leaked/169348/) earlier this month.


Vulnerabilities in VPN servers are like welcome mats to nation-state advanced persistent threat (APT) actors who’ve weaponized VPN CVEs and vulnerabilities to break into protected networks.


But as of Tuesday, as they have [repeatedly](https://threatpost.com/apt-groups-exploiting-flaws-in-unpatched-vpns-officials-warn/148956/) [attempted](https://threatpost.com/nsa-security-bugs-active-nation-state-cyberattack/165446/) in the past, the Feds moved to whisk away that mat.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


On Tuesday, the National Security Agency (NSA) and the Cybersecurity and Infrastructure Security Agency (CISA) issued [guidance](https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/2791320/nsa-cisa-release-guidance-on-selecting-and-hardening-remote-access-vpns/) on selecting and hardening remote virtual access networks (VPNs): guidance that will hopefully help U.S. military leaders to better understand what risks are associated with these devices.


What’s at Stake
---------------


As the advisory from the NSA and CISA explained, exploiting CVEs associated with VPNs can enable a malicious actor “to steal credentials, remotely execute code, weaken encrypted traffic’s cryptography, hijack encrypted traffic sessions, and read sensitive data from the device.”


The guidance continued: “If successful, these effects usually lead to further malicious access and could result in a large-scale compromise to the corporate network.”


A recent example of nation-state actors preying on vulnerable VPNs came in May, when Pulse Secure rushed a fix for a critical zero-day security vulnerability in its Connect Secure VPN devices. The zero day was exploited by two [APTs, likely linked to China](https://threatpost.com/pulse-secure-vpns-fix-critical-zero-day-bugs/165850/), who used it to launch cyberattacks against U.S. defense, finance and government targets, as well as victims in Europe.


This Is So Old School
---------------------


Archie Agarwal, founder and CEO of automated threat modeling provider ThreatModeler, pointed out that a quick search with Shodan – the search engine of Internet-connected devices – uncovers more than a million VPNs on the internet in the U.S. alone. “These are the doorways to private sensitive internal networks and are sitting there exposed to the world for any miscreant to try to break through,” he told Threatpost via email on Wednesday.


All of those sitting VPN ducks represent “the old perimeter security paradigm,” Agarwal said, and they’ve “failed to protect the inner castle over and again.” If credentials are leaked or stolen, or new vulnerabilities are (inevitably) discovered, “the game is lost and the castle falls,” he commented.


Better for organizations to use the [Zero Trust](https://threatpost.com/practical-guide-zero-trust-security/151912/) approach being advocated by the U.S. government and NIST, Agarwal suggested. Zero Trust, an approach that pivots from a “trust but verify” to a “never trust/always verify” approach, slams shut those public doorways into the network and “throws an invisible cloak over the entire network,” he said.


In May, the White House issued an [executive order](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) mandating that the federal government move toward a Zero Trust architecture: a mandate that’s [trickier to implement](https://threatpost.com/practical-guide-zero-trust-security/151912/) than may first appear. Earlier this month, the Biden administration also [offered guidance](https://www.nextgov.com/cybersecurity/2021/09/biden-administration-releases-draft-zero-trust-guidance/185166/) on how to implement it.


VPNs: Here to Stay or Headed to the Dust Bin?
---------------------------------------------


Will the push to Zero Trust spell doomsday for VPNs? Agarwal thinks so: He pointed to startups that are pioneering Zero Trust and predicted that “the days of VPNs on the Internet are thankfully numbered.”


But there are those who would beg to differ.


Heather Paunet, senior vice president at SMB network security provider Untangle, noted that while the concept of Zero Trust is clear, the term has been interpreted differently “by both those trying to implement it and vendors moving fast to be able to state that they provide it.”


She told Threatpost via email on Wednesday that Zero Trust “can incorporate VPN technologies,” and that the NSA’s guidelines on selecting and hardening VPN standards “clearly show that it’s important to look carefully at selecting which VPN technology to use. Vendors that don’t fully research VPN technologies can end up with a solution that is less likely to stand up to an attack.”


Paunet painted a pro-VPN future: “While there has been a rise in vulnerabilities of VPNs due to more VPN usage over the last year and a half, newer VPN technologies with newer types of cryptography are evolving to ensure the protection of information transmitted across the internet. WireGuard VPN, for example, uses state-of-the-art cryptography and is becoming more popular.”


How to Choose and Harden a VPN
------------------------------


For now, the future of VPNs is moot: VPNs haven’t disappeared yet, so for now, there’s clearly still work to be done to harden their defenses.


To that end, the federal agencies released an information sheet ([PDF](https://media.defense.gov/2021/Sep/28/2002863184/-1/-1/0/CSI_SELECTING-HARDENING-REMOTE-ACCESS-VPNS-20210928.PDF)) that details what to take into account when selecting a remote access VPN, as well as how to harden these devices from compromise.


One of the recommendations: use tested and validated VPN products listed on the [National Information Assurance Partnership (NIAP) Product Compliant List](https://www.niap-ccevs.org/Product/PCL.cfm) that employ strong authentication methods like multi-factor authentication (MFA).


Other tips:


Don’t Forget the Human Element
------------------------------


Untangle’s Paunet sees a missing piece of the guidance: namely, humans. Besides following strict guidelines, IT professionals are also challenged with getting employees to effectively use the technology, she noted, and “if the VPN is too difficult to use, or slows down systems, the employee is likely to turn it off.”


Paunet noted that VPN technologies “have come a long way over the last two to three years, with newer technologies … providing fast connections that are easy to set up by administrators and simple to use by employees. The challenge for IT professionals is to find a VPN solution that fits the guidelines, but is also fast and reliable so that employees turn it on once and forget about it.”


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[VPN]] [[VPNs]] [[U.S.]] [[Threatpost]] [[“the]] [[Paunet]] [[ThreatPost]]
