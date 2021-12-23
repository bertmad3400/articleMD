# Telegram Abused to Steal Crypto-Wallet Credentials
### Attackers use the Telegram handle “Smokes Night” to spread the malicious Echelon infostealer, which steals credentials for cryptocurrency and other user accounts, researchers said.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177266
+ Date: 2021-12-23T16:00:22+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2018/03/20144222/Telegram_Messagees.jpg)

Attackers are targeting crypto-wallets of Telegram users with the Echelon infostealer, in an effort aimed at defrauding new or unsuspecting users of a [cryptocurrency](https://threatpost.com/financial-cybercrime-cryptocurrency-public-ledgers/169987/) discussion channel on the messaging platform, researchers have found.


Researchers at the SafeGuard Cyber’s Division Seven threat analysis unit detected a sample of Echelon posted to a Telegram channel focused on cryptocurrency in October, they said in [an analysis](https://www.safeguardcyber.com/blog/echelon-malware-crypto-wallet-stealer-malware) on Thursday.


The malware used in the campaign aims to steal credentials from multiple messaging and file-sharing platforms, including Discord, Edge, FileZilla, OpenVPN, Outlook and even Telegram itself, as well as from a number of cryptocurrency wallets, including AtomicWallet, BitcoinCore, ByteCoin, Exodus, Jaxx and Monero.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The campaign was a “spray and pray” effort: “Based on the malware and the manner in which it was posted, SafeGuard Cyber believes that it was not part of a coordinated campaign, and was simply targeting new or naïve users of the channel,” according to the report.


 


Attackers used the handle “Smokes Night” to distribute Echelon on the channel, but it’s unclear how successful it was, researchers found. “The post did not appear to be a response to any of the surrounding messages in the channel,” they wrote.


Other users on the channel did not appear to notice anything suspicious or engage with the message, they said. However, this doesn’t mean that the malware didn’t reach users’ devices, researchers wrote.


“We did not see anyone respond to ‘Smokes Night’ or complain about the file, though this does not prove that users of the channel did not get infected,” they wrote.


The Telegram messaging app indeed has become a hotbed of activity for cybercriminals, who have capitalized on its popularity and broad attack surface by [using bots](https://threatpost.com/telegram-bots-classiscam-scam/163061/), [malicious accounts](https://threatpost.com/telegram-toxiceye-malware/165543/) and other means to distribute malware on the platform.


**Malware Analysis**
--------------------


Attackers delivered Echelon to the cryptocurrency channel in an .RAR file titled “present).rar” that included three files: “pass – 123.txt,” a benign text document containing a password; “DotNetZip.dll,” a non-malicious class library and toolset for manipulating .ZIP files; and “Present.exe,” the malicious executable for the Echelon credential stealer.


The payload, written in .NET, also included several features that made it difficult to detect or analyze, including two anti-debugging functions that immediately terminate the process if a debugger or other malware analysis tools are detected, and obfuscation using the open-source [ConfuserEx tool](https://ethicalhackingguru.com/how-to-use-confuser-ex-to-bypass-antivirus/).


Researchers eventually managed to de-obfuscate the code and peer under the hood of the Echelon sample delivered to users of the Telegram channel. They found that it contains domain detection, which means the sample also will attempt to steal data regarding any domain that the victim has visited, researchers wrote. A full list of platforms the Echelon sample attempted to target are included in the report.


Other features of the malware include computer fingerprinting, as well the ability to take a screenshot of the victim’s machine, researchers wrote. The Echelon sample lifted from the campaign sends credentials and other stolen data and screenshots back to a command-and-control server using a compressed .ZIP file, they said.


Fortunately, Windows Defender detects and deletes the Present.exe malicious executable sample and alerts it as ‘#LowFI:HookwowLow, mitigating any potential damage from Echelon for users with the antivirus software installed, researchers noted.


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Exodus]] [[action.malware.name=Exodus]] [[action.malware.name=Net]] [[action.malware.name=Reg]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Malware]] [[ThreatPost]]

