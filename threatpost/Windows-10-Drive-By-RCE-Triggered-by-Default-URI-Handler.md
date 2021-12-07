# Windows 10 Drive-By RCE Triggered by Default URI Handler
### There's an argument injection weakness in the Windows 10/11 default handler, researchers said: an issue that Microsoft has only partially fixed.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176830
+ Date: 2021-12-07T20:24:02+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/26141726/Windows-Abstract.jpg)

Researchers have discovered a drive-by remote code-execution (RCE) bug in Windows 10 via Internet Explorer 11/[Edge Legacy](https://support.microsoft.com/en-us/microsoft-edge/what-is-microsoft-edge-legacy-3e779e55-4c55-08e6-ecc8-2333768c0fb0) – the EdgeHTML-based browser that’s currently the default browser on Windows 10 PCs – and [Microsoft Teams](https://threatpost.com/microsoft-teams-tabs-bec/166909/).


According to a [report](https://positive.security/blog/ms-officecmd-rce) posted Tuesday by Positive Security, the vulnerability is triggered by an argument injection, which is a type of attack that involves tampering with a page’s input parameters. It can enable attackers to see or to modify data via the user interface that they normally can’t get at.


In this case, the issue lies in the Windows 10/11 default Uniform Resource Identifier (URIs) handler for ms-officecmd: URIs are used by the Microsoft Office [Universal Windows Platform](https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide) (UWP) app to launch other Office desktop applications.


Some of the noteworthy, not-great things that threat actors can do with the vulnerability include crafting highly believable phishing attacks in which webpages can hide their origin or the fact that their content is coming from an external page; issues with code execution in Outlook; [command-line switches for Microsoft Office products](https://support.microsoft.com/en-us/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6) that allow for loading of add-ins on startup, including allowing for loading of malicious Word/Excel add-ins.


**Likely Unpatched?**
---------------------


The researchers have been going back and forth with Microsoft about this for months, having initially disclosed the weakness to Microsoft in March. Microsoft closed Positive Security’s initial report the very next day, based on what Positive Security called Microsoft’s “erroneous” belief that the exploit relies on social engineering:



> […] Unfortunately your report appears to rely on social engineering to accomplish, which would not meet the definition of a security vulnerability. […] —Microsoft’s initial rejection comment, per Positive Security
> 
> 


“Only after our appeal was the issue reopened and classified as ‘critical, RCE,'” according to the security firm’s writeup.



> **We want to know what your biggest cloud security concerns and challenges are, and how your company is dealing with them. Weigh in with our exclusive, anonymous [Threatpost Poll](https://threatpost.com/cloud-security-challenges-poll/176702/)!**
> 
> 


You can see where Microsoft got the idea that the exploit would require social engineering: In other browsers, an exploit requires a victim to accept “an inconspicuous confirmation dialog,” the researchers explained. Another option for attackers would be to deliver a malicious URL via a desktop application performing [unsafe URL handling](https://positive.security/blog/url-open-rce), they added.


After five months, Microsoft patched the flaw, but the patch failed to address the underlying argument injection, Positive Security asserted. In fact, researchers wrote that it’s “currently also still present on Windows 11.”


A spokesperson told Threatpost that, unfortunately, “we don’t know if/when Microsoft released any changes for Internet Explorer,” referring to a comment from Microsoft about the fix not having gone out through Windows Update.


In other words, don’t bother to hunt for a CVE or a related patch. This is how Microsoft explained it, as Positive Security recounted:



> Unfortunately in this case there was no CVE or advisory tied to the report. Most of our CVEs are created to explain to users why certain patches are sent through Windows Update and why they should be installed. Changes to websites, downloads through Defender, or through the Store normally do not get a CVE attached in the same way. In this case the fix did not go out through Windows Update. —Microsoft, per Positive Security
> 
> 


Microsoft didn’t immediately respond to Threatpost’s request for comment on when a fix might be coming, though it said back in September that the fix would be released “within a few days.”


Windows 10 URI Handler Coughed up a Bug Lickety-Split
-----------------------------------------------------


Positive Security had set its cap on digging up a code-execution vulnerability in a default Windows 10 URI handler. It only took two weeks, researchers said, and they suspect that it’s “very likely” that other custom Windows URI handlers are vulnerable too.


The original motivation: To improve the malicious URI attack scenario. In January, researchers had analyzed how popular desktop applications [handle user-supplied URIs](https://positive.security/blog/url-open-rce). Not well, they concluded, after having come across code-execution vulnerabilities “in most of them.”


The Windows 10 drive-by RCE isn’t the first time that vulnerabilities have cropped up in third-party URI handlers, the researchers said, pointing to these prior instances:


* **2012:** A code-execution flaw ([PDF](http://revuln.com/files/ReVuln_Steam_Browser_Protocol_Insecurity.pdf)) in the Steam URL protocol was found that [could have been abused](https://threatpost.com/steam-gaming-platform-vulnerable-remote-exploits-50-million-risk-101912/77134/) to exploit vulnerabilities in games. It put more than 50 million users of the Steam gaming and media distribution platform at risk of remote compromise.
* **2018:** A [code-execution flaw](https://www.electronjs.org/blog/protocol-handler-fix) affecting Electron apps that register custom protocols was discovered.
* **2018:** A high-severity vulnerability ([PDF](https://sequretek.com/wp-content/uploads/2018/10/Sequretek-Advisory-CVE-2020-13699_.pdf)) in TeamViewer could have allowed for offline password cracking when visiting malicious sites (CVE 2020-13699).


“Windows 10 comes with an abundance of custom URI handlers relating to different OS features or other Microsoft software,” Positive Security said. Researchers found ms-officecmd particularly interesting “due to its apparent complexity,” they said:



> The ms-officecmd: scheme immediately grabbed our attention due to its promising name: MS Office is a very complex suite of applications with many legacy features and a long history of exploitability. On top of that, the scheme ends in the abbreviation for ‘command’, which suggests even more complexity and potential for injection. —Positive Security
> 
> 


While inspecting the handler, researchers noticed an executable called LocalBridge.exe that would briefly run … but apparently do nothing. But upon checking the Windows Event Log, they discovered that a .NET JsonReaderException was triggered by opening the URI “ms-officecmd:invalid.” Observing the way that the URI handler parsed JSON confirmed that “URIs have potential to do very complex things,” the researchers explained. “We were determined to find out exactly what they can do.”


Exploit
-------


The flaw is triggered by a malicious website that “performs a Javascript redirect to a crafted ms-officecmd: URI” scheme, the researchers explained.


The researchers exploited the URI handler’s argument injection flaw to bypass a security measure in [Electron](https://en.wikipedia.org/wiki/Electron_(software_framework)) – an open-source software framework for developing desktop GUI apps using web technologies. They injected an arbitrary OS command via the –gpu-launcher parameter of the Microsoft Teams Electron app.


They demonstrated the drive-by RCE on Windows 10 via MS Edge in the proof of concept (PoC) video below.



Video Player<https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/07131741/drive-by-RCE.mp4>00:0000:0000:21[Use Up/Down Arrow keys to increase or decrease volume.](javascript:void(0);)
The crafted ms-officecmd: URI shown in their PoC video reads like so:


ms-officecmd:{


“LocalProviders.LaunchOfficeAppForResult”: {


“details”: {


“appId”: 5,


“name”: “irrelevant”,


“discovered”: {


“command”: “irrelevant”


}


},


“filename”: “a:/b/ –disable-gpu-sandbox –gpu-launcher=\”C:\\Windows\\System32\\cmd /c ping 2016843009 && \””


}


}


Below is the “rather inconspicuous confirmation dialog” shown in browsers other than IE and Microsoft Edge Legacy before opening the malicious URI.


“With the extracted JSON payload we were finally able to open Office desktop applications via ms-officecmd: URIs,” the researchers said.” Specifically, the payload extracted from the Office UWP app could be used to open Outlook.”


Microsoft Teams Required
------------------------


Positive Security said that for the exploit to work, Microsoft Teams has to be installed but not running. Researchers also shared details on how the scheme and argument injection could be abused in other ways, “with and without the help of MS Teams.”


Those who want to dive right into the gory technical details can check out the [vulnerability report](https://positive.security/blog/ms-officecmd-rce#original-msrc-report) that Positive Security submitted to the Microsoft Security Response Center.


Positive Security told Threatpost that the immediate risk of the Teams-based RCE exploit was mitigated via a patch to Microsoft Teams, “so people don’t need to worry too much.” But the remaining argument injection and other issues, including the Outlook issues, “should be easy to replicate with our provided PoC links,” the firm said.


On Tuesday, after its report was published, Positive Security told Threatpost that the team has once again recently tested a JavaScript-forward payload in Internet Explorer 11, and “it seems to now crash the browser.”


Mitigations
-----------


With regards to how to protect systems while waiting for a patch, Positive Security advised against using Internet Explorer 11/Edge Legacy. That’s not a very big ask, given that the browser is [no longer supported by Microsoft](https://docs.microsoft.com/en-us/deployedge/edge-learnmore-neededge), is [no longer secure](https://threatpost.com/ie-browser-death-march/160571/), and, as of May 2020, had a measly [1.87 percent](https://gs.statcounter.com/browser-market-share#monthly-201905-202005-bar) share of the browser market.


As far as other browsers and applications go, Positive Security recommended not clicking on ‘ms-officecmd:’-links. Also, refrain from confirm dialogs that ask to open the LocalBridge executable.


The company offered a number of additional mitigations in its writeup, including, is possible, removal of the URI handler and a migration to the application-specific URI handlers (e.g. “teams:” and “ms-word:”) to open the applications.


“Making the URI handler only available to the Office PWA app would also greatly reduce the risk, if somehow possible,” the researchers recommended.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** [***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This*** [***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***  

[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***for the LIVE event!***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[Threatpost]] [[Ms-officecmd]] [[Code-execution]] [[Teams]] [[Rce]] [[Drive-by]] [[Url]] [[Cve]] [[ThreatPost]]
#### urls
Playerhttps://media.threatpost.com/wp-content/uploads/sites/103/2021/12/07131741/drive-by-RCE.mp400:0000:0000:21Use a:/b/

