# Microsoft Exchange servers hacked in internal reply-chain attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-exchange-servers-hacked-in-internal-reply-chain-attacks/)
+ Date: November 20, 2021
+ Author: Bill Toulas


## Article:
![Mirosoft Exchange](https://www.bleepstatic.com/content/hl-images/2021/03/10/Exchange1.jpg)


Threat actors are hacking Microsoft Exchange servers using ProxyShell and ProxyLogon exploits to distribute malware and bypass detection using stolen internal reply-chain emails.


When threat actors conduct malicious email campaigns, the hardest part is to trick users into trusting the sender enough so that they open up linked to or included malware-distributing attachments.


TrendMicro researchers have discovered an interesting tactic used of distributing malicious email to a company's internal users using the victim's compromised Microsoft exchange servers.


The actors behind this attack are believed to be 'TR', a known threat actor who distributes emails with malicious attachments that drop malware, including Qbot, IcedID, Cobalt Strike, and SquirrelWaffle payloads.


As a way to trick corporate targets into opening malicious attachments, the threat actor exploits Microsoft Exchange servers using the [ProxyShell](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-servers-are-getting-hacked-via-proxyshell-exploits/) and [ProxyLogon](https://www.bleepingcomputer.com/news/security/the-microsoft-exchange-hacks-how-they-started-and-where-we-are/) vulnerabilities.


The threat actors then uses these compromised Exchange servers to reply to the company's internal emails in reply-chain attacks containing links to malicious documents that install various malware.


"In the same intrusion, we analyzed the email headers for the received malicious emails, the mail path was internal (between the three internal exchange servers’ mailboxes), indicating that the emails did not originate from an external sender, open mail relay, or any message transfer agent (MTA)," explains Trend Micro's [report](https://www.trendmicro.com/en_us/research/21/k/Squirrelwaffle-Exploits-ProxyShell-and-ProxyLogon-to-Hijack-Email-Chains.html).



![One of Squirrelwaffle's emails to a target](https://www.bleepstatic.com/images/news/u/1220909/Phishing/email_chain.jpg)**One of Squirrelwaffle's emails to a target**  
*Source: TrendMicro*
As these emails originate from the same internal network and appear to be a continuation of a previous discussion between two employees, it leads to a greater degree of trust that the email is legitimate and safe.


Not only is this effective against the human recipients, but it’s also excellent for not raising any alarms on the email protection systems used in the target firm.


The attachments that come or are linked to by these emails are your standard malicious Microsoft Excel templates that tell recipients to 'Enable Content' to view a protected file.



![Malicious Microsoft Excel document used by SquirrelWaffle](https://www.bleepstatic.com/images/news/security/squirrelwaffle-template.jpg)**Malicious Microsoft Excel document used by SquirrelWaffle**
However, once the user enables content, malicious macros are executed to download and install the malware distributed by the attachment, whether that be Qbot, Cobalt Strike, SquirrelWaffle, or another malware.


According to Trend Micro's report, the researchers said that they have seen these attacks distribute the SquirrelWaffle loader, which then installs Qbot.


However, Cryptolaemus researcher '[TheAnalyst](https://twitter.com/ffforward)' says that the malicious document used by this threat actor [drop both malware as discrete payloads](https://twitter.com/ffforward/status/1461810464460054538), rather than SquirrelWaffle distributing Qbot.




> 
> Some of this name confusing might come from initial phrases like "SquirrelWaffle drops QakBot", however as far as I know this has never happened. The maldoc has dropped both DLLs, but the timing is att the qbot traffic starts later than SqWa, so just looks that way in pcaps. 
> 
> 
> — TheAnalyst (@ffforward) [November 19, 2021](https://twitter.com/ffforward/status/1461810485872021505?ref_src=twsrc%5Etfw)


Keep your Exchange servers updated
----------------------------------


Microsoft has patched the ProxyLogon vulnerabilities in [March](https://www.bleepingcomputer.com/news/security/microsoft-fixes-actively-exploited-exchange-zero-day-bugs-patch-now/) and the ProxyShell vulnerability in [April and May](https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-urgently-patch-exchange-proxyshell-bugs/), addressing them as zero-days at the time.


Threat actors have abused both vulnerabilities to [deploy ransomware](https://www.bleepingcomputer.com/news/security/conti-ransomware-now-hacking-exchange-servers-with-proxyshell-exploits/) or [install webshells](https://www.bleepingcomputer.com/news/security/more-hacking-groups-join-microsoft-exchange-attack-frenzy/) for later backdoor access. The ProxyLogon attacks got so bad that the [FBI removed web shells](http://remove%20web%20shells%20from%20compromised%20US-based%20Microsoft%20Exchange%20servers%20without%20first%20notifying%20the%20servers'%20owners.) from compromised US-based Microsoft Exchange servers without first notifying the servers' owners.


After all this time and the wide media these vulnerabilities have received, not patching Exchange Servers is just an open invitation to hackers.




#### Tags:
[[Microsoft]] [[emails]] [[ProxyLogon]] [[SquirrelWaffle]] [[ProxyShell]] [[malware]] [[Bleeping Computer]]
