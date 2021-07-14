# Google: Russian SVR hackers targeted LinkedIn users with Safari zero-day
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/google-russian-svr-hackers-targeted-linkedin-users-with-safari-zero-day/)
+ Date: July 14, 2021
+ Author: Sergiu Gatlan


## Article:
![Google: Russian SVR hackers targeted LinkedIn users with Safari zero-day](https://www.bleepstatic.com/content/hl-images/2021/06/04/Google_headpic.jpg)


Google security researchers shared more information on four security vulnerabilities, also known as zero-days, unknown before they discovered them being exploited in the wild earlier this year.


The four security flaws were found by Google Threat Analysis Group (TAG) and Google Project Zero researchers after spotting exploits abusing zero-day in Google Chrome, Internet Explorer, and WebKit, the engine used by Apple's Safari web browser.



The four zero-day exploits discovered by Google researchers earlier this year while being exploited in the wild targeted:


* [CVE-2021-21166](https://www.bleepingcomputer.com/news/security/google-fixes-second-actively-exploited-chrome-zero-day-bug-this-year/) and [CVE-2021-30551](https://www.bleepingcomputer.com/news/security/google-fixes-sixth-chrome-zero-day-exploited-in-the-wild-this-year/) in Chrome,


* [CVE-2021-33742](https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2021-patch-tuesday-fixes-6-exploited-zero-days-50-flaws/) in Internet Explorer, and


* [CVE-2021-1879](https://www.bleepingcomputer.com/news/security/apple-fixes-a-ios-zero-day-vulnerability-actively-used-in-attacks/) in WebKit (Safari).




Google also published root cause analysis for all four zero-days:


* [CVE-2021-1879: Use-After-Free in QuickTimePluginReplacement](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-1879.html)
* [CVE-2021-21166: Chrome Object Lifecycle Issue in Audio](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-21166.html)
* [CVE-2021-30551: Chrome Type Confusion in V8](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-30551.html)
* [CVE-2021-33742: Internet Explorer out-of-bounds write in MSHTML](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-33742.html)


"We tie three to a commercial surveillance vendor arming govt backed attackers and one to likely Russian APT," Google Threat Analysis Group's Director Shane Huntley [said](https://twitter.com/ShaneHuntley/status/1415340345500463113).


"Halfway into 2021, there have been 33 0-day exploits used in attacks that have been publicly disclosed this year — 11 more than the total number from 2020," Google researchers [added](https://blog.google/threat-analysis-group/how-we-protect-users-0-day-attacks/).


"While there is an increase in the number of 0-day exploits being used, we believe greater detection and disclosure efforts are also contributing to the upward trend."


Zero-day exploited by Russian SVR hackers
-----------------------------------------


While the Chrome and Internet Explorer zero-day exploits were developed and sold by the same vendor to customers worldwide who wanted to boost their surveillance capabilities, they were not used in any high-profile campaigns.


This can't be said about the CVE-2021-1879 Safari flaw, which, according to Google, was used via LinkedIn Messaging "to target government officials from western European countries by sending them malicious links."


Google researchers said the attackers were part of a likely Russian government-backed actor abusing this zero-day to target iOS devices running older versions of iOS (12.4 through 13.7).


While Google didn't link the exploit to a specific threat group, Microsoft [says the culprit is Nobelium](https://www.bleepingcomputer.com/news/security/microsoft-russian-svr-hackers-target-govt-agencies-from-24-countries/), the state-sponsored hacking group behind last year's SolarWinds supply-chain attack that led to the compromise of several US federal agencies.


The United States government [formally accused the Russian Foreign Intelligence Service](https://www.bleepingcomputer.com/news/security/us-government-confirms-russian-svr-behind-the-solarwinds-hack/) (aka SVR) in April of carrying out "the broad-scope cyber espionage campaign" through its hacking division commonly known as APT29, The Dukes, or Cozy Bear.


According to Google, the end goal of the attacks was to "collect authentication cookies from several popular websites, including Google, Microsoft, LinkedIn, Facebook and Yahoo and send them via WebSocket to an attacker-controlled IP."




#### Tags:
[[Google]] [[zero-day]] [[CVE-2021-1879]] [[Bleeping Computer]]
