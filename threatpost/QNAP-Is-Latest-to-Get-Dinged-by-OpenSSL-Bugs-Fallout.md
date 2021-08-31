# QNAP Is Latest to Get Dinged by OpenSSL Bugs Fallout
### The NAS maker issued two security advisories about the RCE and DoS flaws, adding to a flurry of advisories from the vast array of companies whose products use OpenSSL. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169054)
+ Date: August 31, 2021  11:08 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/31105632/qnap-devices-scaled-e1630421811772.jpeg)
On Monday, QNAP put out two security advisories about OpenSSL remote-code execution and denial-of-service (DoS) bugs, fixed last week, that affect its network-attached storage (NAS) devices.


The vulnerabilities are tracked as [CVE-2021-3711](https://www.qnap.com/en-us/security-advisory/QSA-21-39) – a high-severity buffer overflow related to SM2 decryption– and [CVE-2021-3712](https://www.qnap.com/en-us/security-advisory/QSA-21-40), a medium-severity flaw that can be exploited for DoS attacks and possibly for the disclosure of private memory contents.


These OpenSSL flaws are spreading ripples far and wide.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


That’s because [OpenSSL](https://en.wikipedia.org/wiki/OpenSSL) is mostly used by network software – including being widely used by Internet servers and the majority of HTTPS websites – that use the TLS protocol (transport layer security), formerly known as SSL (secure sockets layer), to protect data in transit.


TLS has replaced SSL, which contained what Sophos’s Paul Ducklin called a “huge” number of cryptographic flaws. But many popular open-source programming libraries that support it – including OpenSSL, LibreSSL and BoringSSL, “have kept old-school product names for the sake of familiarity,” Ducklin commented in a recent [drilldown](https://nakedsecurity.sophos.com/2021/08/27/big-bad-decryption-bug-in-openssl-but-no-cause-for-alarm/) into the OpenSSL bugs.


QNAP on Monday joined a parade of organizations whose products rely on OpenSSL and which are either investigating the flaws (in QNAP’s case) or have already released security advisories, including Linux distributions such as [Red Hat](https://access.redhat.com/security/cve/cve-2021-3711) (not affected), [Ubuntu](https://ubuntu.com/security/CVE-2021-3711), [SUSE](https://www.suse.com/security/cve/CVE-2021-3711.html), [Debian](https://security-tracker.debian.org/tracker/CVE-2021-3711) and [Alpine Linux](https://www.alpinelinux.org/posts/Alpine-3.14.2-released.html).


QNAP Hammers Out Fixes
----------------------


QNAP said that it’s “thoroughly investigating the case” and that it plans to release security updates and more information ASAP.


Same goes for NAS appliance maker [Synology](https://www.synology.com/en-global/security/advisory/Synology_SA_21_24), which told its customers that the OpenSSL vulnerabilities affect its Synology DiskStation Manager (DSM), Synology Router Manager (SRM), VPN Plus Server and VPN Server products. On Thursday, Synology assigned “important” and “moderate” severity ratings to the vulnerabilities and said that it’s working on patches.


Yet another storage solutions provider, [NetApp](https://security.netapp.com/advisory/ntap-20210827-0010/), is now trying to figure out which of its products may be affected. So far, it’s confirmed that Clustered Data ONTAP, E-Series SANtricity OS controller software, the NetApp Manageability SDK, NetApp SANtricity SMI-S Provider, and NetApp Storage Encryption are affected, and it’s investigating dozens more of its products.


[Cisco](https://tools.cisco.com/security/center/publicationListing.x) and [Broadcom](https://support.broadcom.com/security-advisory/security-advisories-list.html?segment=SE) are also expected to release advisories describing how the latest OpenSSL vulnerabilities will affect their products.


QNAP’s Advisories
-----------------


It turns out that the OpenSSL vulnerabilities affect QNAP NAS devices running the [HBS 3 Hybrid Backup Sync](https://www.qnap.com/en/how-to/tutorial/article/hybrid-backup-sync) data backup and disaster recovery tool, the [QTS](https://www.qnap.com/en-us/qts4/con_show.php?op=showone&cid=1) GUI, the [QuTS hero](https://www.qnap.com/quts-hero/en-us/) operating system, and [QuTScloud](https://www.qnap.com/solution/qutscloud-overview/en-us/#:~:text=QuTScloud%20is%20the%20operating%20system,at%20a%20predictable%20monthly%20cost.), which is an operating system for QNAP Cloud NAS virtual appliances.


According to Sophos’s Ducklin, the flaws could allow an attacker to trick an application “into thinking that something succeeded (or failed) when it didn’t, or even to take over the flow of program execution entirely.


If successfully exploited, the flaws could allow remote attackers to execute arbitrary code with the permissions of the user running the application, QNAP said, which gives CVE-2021-3711 a high severity rating. CVE-2021-3712 allows remote attackers to disclose memory data or execute a DoS attack, making it a medium-security flaw.


MITRE has the technical details here for [CVE-2021-3712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712) and [CVE-2021-3711](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3711).


CVE-2021-3711 is a [heap-based buffer overflow](https://cwe.mitre.org/data/definitions/122.html#:~:text=Description,routine%20such%20as%20malloc().). These bugs generally lead to crashes but can also translate into lack of availability, including putting the program into an infinite loop. Such vulnerabilities can also allow attackers to carry out RCE, bypass protection, or to modify memory.


According to MITRE, the CVE-2021-3711 bug in OpenSSL allows an attacker who can present SM2 content – SM2 being a public key cryptographic algorithm based on elliptic curves that’s used to generate and verify digital signatures for decryption – to send data that overflows the buffer by up to a maximum of 62 bytes, “altering the contents of other data held after the buffer, possibly changing application behaviour or causing the application to crash.”


As Sophos’s Ducklin explained when writing about this decryption bug, OpenSSL includes implementations of the SM algorithms: It uses SM2 for key agreement and digital signatures, SM3 for hashing, and SM4 for block encryption. On the plus side, Sophos researchers don’t think that crooks are going to be able to exploit this bug, given that “official TLS support for ShangMi was only introduced in [RFC 8998](https://datatracker.ietf.org/doc/html/rfc8998), dated March 2021, so it’s a newcomer to the world’s cryptographic stable.”


As Ducklin wrote, OpenSSL does include implementations of SM2, SM3 and SM4, “it doesn’t yet include the code needed to allow you to choose these algorithms as a ciphersuite for use in TLS connections.”



> “You can’t ask your TLS client code to request a ShangMi connection to someone else’s server, as far as we can see; and you can’t get your TLS server code to accept a ShangMi connection from someone else’s client.
> 
> 
> “So the bug is in there, down in the low-level OpenSSL libcrypto code, but if you use OpenSSL at the TLS level to make or accept secure connections, we don’t think you can open up a session in which the buggy code could be triggered.
> 
> 
> “In our opinion, that greatly reduces the likelihood of criminals abusing this flaw to implant malware on your laptop, for example by luring you to a booby-trapped website and presenting you with a rogue certificate during connection setup.” —Sophos’s Paul Ducklin
> 
> 


Technical Details
-----------------


The CVE-2021-3712 flaw is caused by a [read buffer overrun](https://cwe.mitre.org/data/definitions/119.html) weakness while processing ASN.1 strings. [MITRE explains](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3712) that [ASN.1](https://www.ncbi.nlm.nih.gov/Structure/asn1.html#:~:text=1%20file%20format-,ASN.,to%20achieve%20interoperability%20between%20platforms.&text=It%20permits%20computers%20and%20software,the%20data%20structure%20and%20content.) strings are represented internally within OpenSSL as an ASN1\_STRING structure that contains a buffer holding the string data and a field holding the buffer length, as opposed to normal C strings that are represented as a buffer for the string data, which is terminated with a NUL (0) byte. “If a malicious actor can cause an application to directly construct an ASN1\_STRING and then process it through one of the affected OpenSSL functions then this issue could be hit,” according to MITRE. That could lead to a crash, causing DoS or could also lead to disclosure of private memory contents, such as private keys or even sensitive content in plaintext.


Both of the OpenSSL bugs were [fixed](https://www.openssl.org/news/vulnerabilities.html) in OpenSSL 1.1.1l on Tuesday of last week.


Fix Them If You Can
-------------------


Sophos’s Ducklin recommended upgrading to OpenSSL 1.1.1l if possible. “Although most software on Windows, Mac, iOS and Android will not be using OpenSSL, because those platforms have their own alternative TLS implementations, some software may include an OpenSSL build of its own and will need updating independently,” he noted. “If in doubt, consult your vendor. Most Linux distros will have a system-wide version of OpenSSL, so check with your distro for an update. (Note: Firefox doesn’t use OpenSSL on any platforms.)”


There’s no shortage of reasons to heed his advice, given that criminal gangs already have NAS devices in their crosshairs. In a [report](https://unit42.paloaltonetworks.com/ech0raix-ransomware-soho/) published a few weeks ago, Palo Alto Network Unit 42 researchers said that they’d discovered a new variant of the eCh0raix ransomware string that exploited a critical bug, [CVE-2021-28799](https://nvd.nist.gov/vuln/detail/CVE-2021-28799) – an improper authorization vulnerability that gives attackers access to hard-coded credentials so as to plant a backdoor account – in the Hybrid Backup Sync (HBS 3) software on QNAP’s NAS devices.


The nearly year-old eCh0raix ransomware strain has been used to target both QNAP and Synology network-attached storage (NAS) devices in past, separate campaigns, but the new variant is more efficient: It can target either vendors’ devices [in a single campaign](https://threatpost.com/ech0raix-ransomware-variant-qnap-synology-nas-devices/168516/).




#### Tags:
[[OpenSSL]] [[QNAP]] [[TLS]] [[Ducklin]] [[it’s]] [[NAS]] [[CVE-2021-3711]] [[SM2]] [[Sophos’s]] [[Synology]] [[ThreatPost]]
