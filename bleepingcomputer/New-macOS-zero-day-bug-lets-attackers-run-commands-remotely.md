# New macOS zero-day bug lets attackers run commands remotely
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/apple/new-macos-zero-day-bug-lets-attackers-run-commands-remotely/)
+ Date: September 21, 2021
+ Author: Sergiu Gatlan


## Article:
![New zero-day lets attackers run arbitrary commands on Macs](https://www.bleepstatic.com/content/hl-images/2021/09/21/MacBook.jpg)


Security researchers disclosed today a new vulnerability in Apple's macOS Finder, which makes it possible for attackers to run arbitrary commands on Macs running any macOS version up to the latest release, Big Sur.


Zero-days are publicly disclosed flaws that haven't been patched by the vendor which, in some cases, are also actively exploited by attackers or have publicly available proof-of-concept exploits.


The bug, found by independent security researcher Park Minchan, is due to the way macOS processes inetloc files which inadvertently causes it to run any commands embedded by an attacker inside without any warnings or prompts.


On macOS, [Internet location files](https://www.oreilly.com/library/view/mac-os-x/9781449314828/ch18s10.html) with .inetloc extensions are system-wide bookmarks that can be used to open online resources (news://, ftp://, afp://) or local files (file://).


"A vulnerability in macOS Finder allows files whose extension is inetloc to execute arbitrary commands,"  [SSD Secure Disclosure advisory](https://ssd-disclosure.com/ssd-advisory-macos-finder-rce/) published today revealed.


"These files can be embedded inside emails which if the user clicks on them will execute the commands embedded inside them without providing a prompt or warning to the user."



![macOS zero-day demo](https://www.bleepstatic.com/images/news/u/1109292/2021/macos%20rce.gif)*Image: SSD Secure Disclosure*
Apple botches patch, doesn't assign a CVE ID
--------------------------------------------


While Apple silently fixed the issue without assigning a CVE identification number, as Minchan later discovered, Apple's patch only partially addressed the flaw as it can still be exploited by changing the protocol used to execute the embedded commands from file:// to FiLe://.


"Newer versions of macOS (from Big Sur) have blocked the file:// prefix (in the com.apple.generic-internet-location) however they did a case matching causing File:// or fIle:// to bypass the check," the advisory adds.


"We have notified Apple that `FiLe://` (just mangling the value) doesn’t appear to be blocked, but have not received any response from them since the report has been made. As far as we know, at the moment, the vulnerability has not been patched."


Although the researcher did not provide any info on how this bug might be abused by attackers, it could potentially be used by threat actors to create malicious email attachments that, when opened by the target, would be able to launch a bundled or remote payload.


BleepingComputer also tested the proof-of-concept exploit shared by the researcher and was able to confirm that the vulnerability can be used to run arbitrary commands on macOS Big Sur using specially crafted files downloaded from the Internet without any prompts or warnings.


An .inetloc file with the PoC code [was not detected by any of the antimalware engines on VirusTotal](https://www.virustotal.com/gui/file/9bb6ce7cb19b779bc53b8d14ff95da0ddc37be1f383ff47d9186a3b7c1660844) which means that macOS users potentially targeted by threat actors using this attack method won't be protected by security software.


An Apple spokesperson was not available for comment when contacted by BleepingComputer earlier today.




#### Tags:
[[macOS]] [[Bleeping Computer]]
