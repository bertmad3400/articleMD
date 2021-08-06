# Golang Cryptomining Worm Offers 15% Speed Boost
### The latest variants of the Monero-mining malware exploit known web server bugs and add efficiency to the mining process.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168456)
+ Date: August 6, 2021  4:41 pm
+ Author: Tara Seals


## Article:
A freshly discovered variant of the Golang crypto-worm was recently spotted dropping Monero-mining malware on victim machines; in a switch-up of tactics, the payload binaries are capable of speeding up the mining process by 15 percent, researchers said.


According to research from Uptycs, the worm scans for and exploits various known vulnerabilities in popular Unix and Linux-based web servers, including [CVE-2020-14882](https://nvd.nist.gov/vuln/detail/CVE-2020-14882) in the Oracle WebLogic Server, and [CVE-2017-11610](https://nvd.nist.gov/vuln/detail/CVE-2017-11610), a remote code-execution (RCE) bug which affects XML-RPC servers. XML-RPC is an interface provided by WordPress.


“CVE-2020-14882 [is a] classic path-traversal vulnerability used for exploiting vulnerable web logic servers,” according to Uptycs. “It seemed like the attacker tried to bypass the authorization mechanism by changing the URL and performing a path traversal using double encoding on /console/images.”



The exploit for CVE-2017-11610 meanwhile contains an encoded payload in one of the parameters, researchers added.


**Golang Cryptomining Attack Kill Chain**
-----------------------------------------


After initial exploitation, the attack begins with a shell script which downloads the worm using the curl utility, researchers noted, adding that the script uses several defense-evasion techniques like firewall altering and disabling monitoring agents.


That initial script then downloads the first-stage worm sample, which was compiled in Golang (hence its name) and UPX-packed, the report noted. The worm uses the go-bindata package to embed off-the-shelf XMRig cryptominer inside itself.


Once installed, the worm downloads another shell script which downloads a copy of the same Golang worm. It goes on to write multiple copies of itself to various sensitive directories like /boot,/efi,/grub.


After that, it ultimately installs the XMRig into a /tmp location, and uses a base64 encoded command that downloads the shell script on any other remote vulnerable servers from the C2.


**Monero-Mining with an Efficiency Boost**
------------------------------------------


XMRig is a well-known [cryptominer](https://threatpost.com/cloud-cryptomining-swindle-google-play/167581/) for the Monero cryptocurrency, which has been [used as a payload](https://threatpost.com/worm-golang-malware-windows-payloads/156924/) by the worm for some time. In this latest campaign however, the binaries have been modified to improve efficiency, according to the [Uptycs report](https://www.uptycs.com/blog/cryptominer-elfs-using-msr-to-boost-mining-process), issued Thursday.


Specifically, the various malware variants use the Model Specific Register (MSR) driver to disable hardware prefetchers. MSRs in Unix and Linux  servers are used for debugging, logging and so on.


“Hardware prefetcher is a technique in which the processors prefetch data based on the past access behavior by the core,” Uptycs researchers explained. “The processor (or the CPU), by using hardware prefetcher, stores instructions from the main memory into the L2 cache. However, on multicore processors, the use of aggressive hardware prefetching causes hampering and results in overall degradation of system performance.”


That degradation of performance is a problem for XMRig, which harnesses a machine’s processing horsepower to perform the complex calculations at scale required to earn Monero coins.


To prevent this, the cryptomining binaries spotted by Uptycs use MSR registers to toggle certain CPU features and computer performance monitoring. By manipulating the MSR registers, hardware prefetchers can be disabled, researchers explained.


“According to the documentation of XMRig, disabling the hardware prefetcher increases the speed up to 15 percent,” researchers said.


However, this function presents an enhanced risk to businesses, researchers warned: “Alongside the mining process, modification of the MSR registers can lead to fatal performance issues of the corporate resources,” according to the analysis.


In all, the Uptycs team identified seven similar samples of the Golang wormed cryptominer, starting in June.


“With the rise and sky-high valuation of Bitcoin and several other cryptocurrencies, cryptomining-based attacks [have continued to dominate](https://threatpost.com/ddos-attacks-q4-cryptomining-resurgence/163998/) the threat landscape,” researchers concluded. “Wormed cryptominer attacks have a greater threshold as they write multiple copies and also spread across endpoints in a corporate network.”


To avoid becoming a victim, keeping systems up-to-date and patched would thwart this particular attack, since it starts with bug exploitations.


**Worried about where the next attack is coming from? We’ve got your back.****[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****for our upcoming live webinar,****[How to Think Like a Threat Actor](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****, in partnership with Uptycs. Find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on Aug. 17 at 11AM EST for this****[LIVE](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****discussion.**




#### Tags:
[[Golang]] [[Uptycs]] [[XMRig]] [[cryptominer]] [[MSR]] [[ThreatPost]]
