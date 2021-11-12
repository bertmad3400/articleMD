# Google warns of hackers using macOS zero-day flaw to capture keystrokes, screengrabs
### Likely state-sponsored engineers create a Mac hack that was used for at least the past three months.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/google-warns-of-hackers-using-macos-zero-day-flaw-to-capture-keystrokes-screengrabs/)
+ Date: November 12, 2021
+ Author: Liam Tung


## Article:
Unknown

Google's Threat Analysis Group (TAG) has revealed that hackers targeting visitors to websites in Hong Kong were using a previously undisclosed, or zero-day, flaw in macOS to spy on people. 

Apple patched the bug, tracked as CVE-2021-30869, in a [macOS Catalina update in September](https://support.apple.com/en-us/HT212825), about a month after Google TAG researchers found it being used. 


"A malicious application may be able to execute arbitrary code with kernel privileges. Apple is aware of reports that an exploit for this issue exists in the wild," Apple said, crediting Google TAG researchers with reporting the flaw. 

**SEE:** [**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/#link=%7B%22role%22:%22standard%22,%22href%22:%22http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EA%20winning%20strategy%20for%20cybersecurity%3C/strong%3E%22%7D) **(ZDNet special report)**

Now Google has provided more information, noting that this was a so-called "watering hole" attack, where attackers select websites to compromise because of the profile of typical visitors. The attacks targeted Mac and iPhone users. 

"The websites leveraged for the attacks contained two iframes which served exploits from an attacker-controlled server—one for iOS and the other for macOS," [said Erye Hernandez of Google TAG](https://blog.google/threat-analysis-group/analyzing-watering-hole-campaign-using-macos-exploits/). 

The watering hole served an XNU privilege escalation vulnerability at that point unpatched in macOS Catalina, which led to the installation of a backdoor.






"We believe this threat actor to be a well-resourced group, likely state-backed, with access to their own software engineering team based on the quality of the payload code," he added. 

The attackers were using the previously disclosed flaw in XNU, tracked as CVE-2020-27932, and a related exploit to create an elevation of privilege bug that gave them root access on a targeted Mac. 

Once root access was gained, the attackers downloaded a payload that ran silently in the background on infected Macs. The design of the malware suggests a well-resourced attacker, according to Google TAG. 

"The payload seems to be a product of extensive software engineering. It uses a publish-subscribe model via a [Data Distribution Service (DDS)](https://en.wikipedia.org/wiki/Data_Distribution_Service) framework for communicating with the C2. It also has several components, some of which appear to be configured as modules," notes Hernandez. 

**SEE:** [**Cloud security in 2021: A business guide to essential tools and best practices**](https://www.zdnet.com/article/cloud-security-in-2021-a-business-guide-to-essential-tools-and-best-practices/)

The backdoor included the usual-suspect traits of malware built for spying on a target, including device fingerprint, screen captures, the ability to upload and download files, as well as execute terminal commands. The malware could also record audio and log keystrokes. 

Google didn't disclose the websites targeted but noted that they included a "media outlet and a prominent pro-democracy labor and political group" related to Hong Kong news.





#### Tags:
[[Google]] [[websites]] [[macOS]] [[malware]] [[ZDNet]]
