# macOS zero-day deployed via Hong Kong pro-democracy news sites
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/macos-zero-day-deployed-via-hong-kong-pro-democracy-news-sites/)
+ Date: November 11, 2021
+ Author: Catalin Cimpanu


## Article:
![macOS zero-day deployed via Hong Kong pro-democracy news sites](https://therecord.media/wp-content/uploads/2021/11/hong-kong.jpg)

A suspected state-sponsored threat actor has used Hong Kong pro-democracy news sites to deploy a macOS zero-day exploit chain that installed a backdoor on visitors’ computers.


* The attacks have been taking place since at least August 2021.
* The exploit chain combined a remote code execution bug in WebKit (CVE-2021-1789, [patched](https://support.apple.com/en-us/HT212152) on Jan 5, 2021) with a local privilege escalation in the XNU kernel component (CVE-2021-30869, later [patched](https://support.apple.com/en-us/HT212825) on Sept 23, 2021).
* The attackers used the exploit chain to gain root access to the macOS operating system and download and install a malware strain named **MACMA** or **OSX.CDDS**.


This never-before-seen malware contained features specific to both backdoor and spyware strains and gave attackers the ability to:


* Fingerprint devices for later identification
* Take screenshots of the screen
* Log keystrokes
* Record local audio
* Download or upload files
* Execute terminal commands.


The attacks using this macOS zero-day were first detected by the Google Threat Analysis Group, which reported the zero-day vulnerability to Apple to have it patched.


The Google team has released a [report](https://blog.google/threat-analysis-group/analyzing-watering-hole-campaign-using-macos-exploits/) today detailing what they saw in the attacks. Additional details from this report also include:


* iOS users were also targeted, but using a different exploit chain which Google TAG wasn’t able to recover in full.
* The zero-day exploit was actually public, having been [presented](https://github.com/wangtielei/Slides/blob/main/zer0con21.pdf) by the Pangu Lab research team in a talk at zer0con21 in April 2021 and Mobile Security Conference (MOSEC) in July 2021, before being used in attacks in August.
* It’s unclear if Pangu Lab reported the vulnerability to Apple or if Apple was tardy in patching the bug, as usual, allowing the threat actors to mount their attacks based on the public information.
* Google TAG described the threat actor behind the attacks as a “*well-resourced group, likely state backed, with access to their own software engineering team based on the quality of the payload code.*“
* Google did not attribute the attacks to any country nor any threat actor they saw in previous operations.


Besides Google’s report, macOS security researcher Patrick Wardle has also published an [independent analysis of the MACMA (OSX.CDDS) malware](https://objective-see.com/blog/blog_0x69.html) on his blog, going into details beyond Google’s short analysis.





#### Tags:
[[macOS]] [[zero-day]] [[malware]] [[Google]] [[The Record]]
