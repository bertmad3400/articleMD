# Security researchers find another UEFI bootkit used for cyber-espionage
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/security-researchers-find-another-uefi-bootkit-used-for-cyber-espionage/)
+ Date: October 5, 2021
+ Author: Catalin Cimpanu


## Article:
![Security researchers find another UEFI bootkit used for cyber-espionage](https://therecord.media/wp-content/uploads/2021/10/chip-rootkit-bootkit.png)

The number of UEFI bootkits used in targeted attacks has been slowly growing in recent years, highlighting that threat actors have found reliable and stealthy methods to abuse the UEFI component to deploy highly persistent malware on targeted systems using a mechanism thought to be more secure than the older BIOS technology.


Past examples of UEFI bootkits include:


* [**FinSpy**](https://securelist.com/finspy-unseen-findings/104322/)– a UEFI bootkit component used with the government-grade FinFisher spyware, discovered last week by security firm Kaspersky.
* [**Demodex**](https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/) – a UEFI bootkit used by a Chinese cyber-espionage group since July 2020, also disclosed last week by security firm Kaspersky.
* [**LoJax**](https://www.welivesecurity.com/2018/09/27/lojax-first-uefi-rootkit-found-wild-courtesy-sednit-group/) – a UEFI bootkit used by Russian state hackers since 2018 in attacks across Europe.
* [**Hacking Team Vector EDK**](https://github.com/hackedteam/vector-edk) – a UEFI bootkit part of the now-defunct HackingTeam’s malware arsenal.
* [**DerStarke**](https://wikileaks.org/ciav7p1/cms/page_26968082.html) and [**QuarkMatter**](https://wikileaks.org/ciav7p1/cms/page_26968082.html) – UEFI rootkits part of the CIA’s hacking tools leaked in 2016 part of the Vault7 trove.


The latest addition to this list is **ESPecter**, a UEFI bootkit that was detailed for the first time in a [report](https://www.welivesecurity.com/2021/10/05/uefi-threats-moving-esp-introducing-especter-bootkit/) published today by Slovak security firm ESET.


Attacks using this new malware were spotted as far back as 2012. However, ESET researchers said that ESPecter didn’t start out as a UEFI bootkit from the get-go, with initial versions being configured to attack systems using legacy BIOS components.


But ESET said that in 2020, the attackers upgraded the ESPecter code to attack modern UEFI systems.


“What is interesting is that the malware’s components have barely changed over all these years and the differences between 2012 and 2020 versions are not as significant as one would expect,” ESET researchers Anton Cherepanov and Martin Smolár explained today.


ESET researchers said they still don’t know how attackers are carrying out the attacks in the first stages. It’s unclear if they are gaining physical access to hacked systems or are using classic phishing and boobytrapped Office documents to deploy ESPecter on a target’s network.


However, once the installation process begins, the initial ESPecter components modify the Windows Boot Manager component and bypass the Windows Driver Signature Enforcement (DSE) to load and run an unsigned malicious driver — the actual ESPecter bootkit payload.


![ESPecter-scheme](https://www-therecord.recfut.com/wp-content/uploads/2021/10/ESPecter-scheme.png)Image: ESET
After installing this latter component, ESET said that attackers usually use ESPecter to deploy other malware and survive OS reinstalls. Malware spotted in past attacks includes a backdoor trojan that attackers used to search for sensitive files on the local system, take periodic screenshots of the victim’s screen, and run a keylogger to monitor key presses.


While ESET didn’t connect or attribute ESPecter with any known major threat actor, the advance and complex nature of the code, along with its silent use for target monitoring, led researchers to believe they were looking at a state-sponsored cyber-espionage tool.


In addition, the ESET team also pointed out that ESPecter is also the second known UEFI bootkit that (ab)uses the EFI System Partition (ESP) as its entry point, after the recently discovered FinSpy, which is different from other past UEFI bootkits, most of which use the UEFI SPI Flash memory.





#### Tags:
[[UEFI]] [[bootkit]] [[ESET]] [[ESPecter]] [[malware]] [[The Record]]
