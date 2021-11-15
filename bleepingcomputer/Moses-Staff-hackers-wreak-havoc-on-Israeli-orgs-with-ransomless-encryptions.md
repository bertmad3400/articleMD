# Moses Staff hackers wreak havoc on Israeli orgs with ransomless encryptions
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/moses-staff-hackers-wreak-havoc-on-israeli-orgs-with-ransomless-encryptions/)
+ Date: November 15, 2021
+ Author: Bill Toulas


## Article:
![moses](https://www.bleepstatic.com/content/hl-images/2021/11/15/moses_staff.jpg?rand=1275656711)


A new hacker group named Moses Staff has recently claimed responsibility for numerous attacks against Israeli entities, which appear politically motivated as they do not make any ransom payment demands.


The threat actors have repeatedly caused damage to Israeli systems in the past couple of months, infiltrating networks and encrypting files, and then leaking the stolen copies to the public.


As such, the group's apparent motive is to cause maximum operational disruption and damage to its targets by exposing corporate secrets and other sensitive information via dedicated data leaks sites, Twitter accounts, and Telegram channels.


Publicly available info
-----------------------


Researchers at Check Point have published a detailed report today on Moses Staff, looking into the techniques, infection chain, and the toolset used by the actor.


Moses Staff appears to be using publicly available exploits for known vulnerabilities that remain unpatched on public-facing infrastructure.


For example, the hacking group has been targeting vulnerable Microsoft Exchange servers that have been under exploitation [for months now](https://www.bleepingcomputer.com/news/security/microsoft-exchange-servers-being-hacked-by-new-lockfile-ransomware/), yet many deployments [remain unpatched](https://www.bleepingcomputer.com/news/microsoft/microsoft-urges-exchange-admins-to-patch-bug-exploited-in-the-wild/).


After successfully breaching a system, the threat actors will laterally move through the network with the help of PsExec, WMIC, and Powershell, so no custom backdoors are used.


The actors eventually use a custom **PyDCrypt** malware that utilizes the DiskCryptor, an open-source disk encryption tool [available on GitHub](https://github.com/DavidXanatos/DiskCryptor), to encrypt devices.



![Moses Staff Infection chain](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/infection_chain.jpg)**MosesStaff Infection chain**  
*Source: CheckPoint*
Weak encryption scheme
----------------------


CheckPoint explains that the encrypted files can be restored under certain circumstances, as the encryption scheme uses symmetric key generation when encrypting devices.


PyDCrypt generates unique keys for every hostname based on MD5 hash and crafted salt. If the PyDCrypt copy used in the attack is retrieved and reversed, the hashing function can be derived.



![Replicating the attack parameters for decryption](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/finding_info.jpg)**Replicating the attack parameters for decryption**  
*Source: CheckPoint*
This is possible in many cases where the self-deletion of the ransomware hasn't worked or was disabled in the configuration.


In general, Moses Staff isn’t putting much effort into this aspect of their operation, as the main thing they aim for is to cause chaos in the targeted Israeli operation and not to ensure that the encrypted drives are irrecoverable.


Political motivation
--------------------


Although the actor is new by name, it may have links to '[Pay2Key](https://www.bleepingcomputer.com/news/security/iranian-nation-state-hackers-linked-to-pay2key-ransomware/)' or '[BlackShadow](https://www.bleepingcomputer.com/news/security/blackshadow-hackers-breach-israeli-hosting-firm-and-extort-customers/),' who have the same political motivation and [targeting scope](https://www.jpost.com/israel-news/moses-staff-hackers-strike-again-attack-israeli-engineering-companies-683855).


"In September 2021, the hacker group Moses Staff began targeting Israeli organizations, joining a wave of attacks which was started about a year ago by the Pay2Key and BlackShadow attack groups," the researchers explain in [their report](http://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/).


"Those actors operated mainly for political reasons in attempt to create noise in the media and damage the country's image, demanding money and conducting lengthy and public negotiations with the victims."


The group has a vocal presence on social media, a Tor data leak site, and a Telegram channel, all used to publish stolen data in as many channels as possible to maximize damage.



![MosesStaff boasting on Twitter](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Moses Staff boasting on Twitter**
So far, analysts haven't been able to attribute Moses Staff to any particular geographic location or whether they are a state-sponsored group. 


However, one of the malware samples used in Moses Staff attacks was [uploaded to VirusTotal](https://www.virustotal.com/gui/file/2aae636691b7d258528d19411d111bc48f36616438e8a8d0b223ecc8b33dd3db/detection) from Palestine a few months before the attacks began.


"Although this is not a strong indication, it might betray the attackers' origins; sometimes they test the tools in public services like VT to make sure they are stealthy enough," explains Check Point.


As Moses Staff attacks use old vulnerabilities that have available patches, Check Point advises all Israeli entities to patch their software to help prevent attacks.




#### Tags:
[[PyDCrypt]] [[Bleeping Computer]]
