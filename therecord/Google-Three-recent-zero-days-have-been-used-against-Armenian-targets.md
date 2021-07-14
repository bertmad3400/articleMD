# Google: Three recent zero-days have been used against Armenian targets
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/google-three-recent-zero-days-have-been-used-against-armenian-targets/)
+ Date: July 14, 2021
+ Author: Catalin Cimpanu


## Article:
![Google: Three recent zero-days have been used against Armenian targets](https://therecord.media/wp-content/uploads/2021/07/Yerevan-Armenia.jpg)

* New Google report reveals hacking campaigns involving three zero-days targeting Armenian users.
* All three zero-days appear to have been developed by the same exploit broker, Google said.
* A fourth zero-day was also used by Russian cyberspies to go after western European government officials.


One of Google’s security teams has published today technical details about four zero-day vulnerabilities that have been abused in attacks this year to compromise users as part of highly targeted hacking campaigns.


The zero-days—listed below—were used to attack users of Chrome, Internet Explorer, and the Safari for iOS browsers, Google said in a [technical report](https://blog.google/threat-analysis-group/how-we-protect-users-0-day-attacks/) published earlier today:


* [CVE-2021-21166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21166) and [CVE-2021-30551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30551) in Chrome,
* [CVE-2021-33742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33742) in Internet Explorer, and
* [CVE-2021-1879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-1879) in WebKit (Safari).


### Three zero-days developed by the same exploit broker


According to Google, the three Chrome and IE zero-days were “developed by the same commercial surveillance company that sold these capabilities to two different government-backed actors.”


Google did not name the exploit broker nor the two threat actors who used the vulnerabilities as part of their attacks.


Google said that all three zero-days were used in attacks targeted at Armenians.


For example, Google said that the Chrome zero-day exploits CVE-2021-21166 and ​​CVE-2021-30551 were used in a campaign that sent one-time links by email to targeted individuals, links that mimicked legitimate websites.


When a target clicked the link, they were redirected to a webpage that would fingerprint their device, collect system information about the client and generate ECDH keys to encrypt the exploits, and then send this data back to the exploit server. The information collected from the fingerprinting phase included screen resolution, timezone, languages, browser plugins, and available MIME types. This information was collected by the attackers to decide whether or not an exploit should be delivered to the target.


Google said its researchers discovered the two zero-days after figuring out two correct configurations needed to deliver a working exploit.


After the renderer is compromised [by the zero-day exploit], an intermediary stage is executed to gather more information about the infected device including OS build version, CPU, firmware and BIOS information. This is likely collected in an attempt to detect virtual machines and deliver a tailored sandbox escape to the target. In our environment, we did not receive any payloads past this stage.


The Google TAG team also said that the CVE-2021-21166 also impacted Safari’s WebKit browser engine due to some shared codebase, and they reported the issue to Apple, which promptly fixed it in its products as CVE-2021-1844.


“We do not have any evidence that this vulnerability was used to target Safari users,” the Google TAG team said today.


As for the IE zero-day tracked as CVE-2021-33742, which Microsoft patched in June, Google said this was also used against Armenian targets.


This time around, the delivery method was via emails that carried malicious Office documents that loaded web content inside Office via an embeddable component of Internet Explorer.


Just like the two Chrome zero-days, the attack involved a fingerprinting stage before the attackers would deploy a second-stage payload.


The similarities between the two different campaigns, carried out by separate threat actors, led the TAG team to conclude that the zero-day exploits were most likely created by the same exploit broker.


### Safari for iOS zero-day abused via LinkedIn


In addition, Google said that it also detected attacks that leveraged CVE-2021-1879, a security flaw in WebKit for iOS.


These attacks, which Google attributed to a “likely Russian government-backed actor,” were executed via LinkedIn Messenger, a LinkedIn feature that lets users exchange messages on the platform.


Google said that the Russian threat actor used LinkedIn to send messages with malicious links to government officials from western European countries.


If the targets opened the link via Safari/WebKit browser on an iOS device, the zero-day exploit would disable [Same-Origin-Policy](https://en.wikipedia.org/wiki/Same-origin_policy) protections in order to “collect authentication cookies from several popular websites, including Google, Microsoft, LinkedIn, Facebook and Yahoo and send them via WebSocket to an attacker-controlled IP.”


The exploit worked on users running iOS versions 12.4 through 13.7, and Google said the same CVE-2021-1879 zero-day was also spotted in other campaigns documented by [Microsoft](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/) and [Volexity](https://www.volexity.com/blog/2021/05/27/suspected-apt29-operation-launches-election-fraud-themed-phishing-campaigns/) in the spring. Those attacks were attributed to a threat actor known as [Nobelium and APT29](https://therecord.media/svr-cyberspies-used-ios-zero-day-in-recent-phishing-campaign/), a threat actor [linked by White House officials to the SVR](https://therecord.media/white-house-formally-blames-russian-intelligence-service-svr-for-solarwinds-hack/), the Russian Foreign Intelligence Service.





#### Tags:
[[Google]] [[zero-day]] [[zero-days]] [[LinkedIn]] [[WebKit]] [[CVE-2021-21166]] [[Microsoft]] [[The Record]]
