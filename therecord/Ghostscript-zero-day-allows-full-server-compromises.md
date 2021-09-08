# Ghostscript zero-day allows full server compromises
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/ghostscript-zero-day-allows-full-server-compromises/)
+ Date: September 7, 2021
+ Author: Catalin Cimpanu


## Article:
![Ghostscript zero-day allows full server compromises](https://therecord.media/wp-content/uploads/2021/09/GhostScript.png)

Proof-of-concept exploit code was published online over the weekend for an unpatched Ghostscript vulnerability that puts all servers that rely on the component at risk of attacks.


Published by Vietnamese security researcher [Nguyen The Duc](https://twitter.com/ducnt_/status/1434534373416574983), the proof-of-concept code is available [on GitHub](https://github.com/duc-nt/RCE-0-day-for-GhostScript-9.50) and was confirmed to work by several of today’s leading security researchers.





Released back in 1988, [Ghostscript](https://www.ghostscript.com) is a small library that allows applications to process PDF documents and PostScript-based files.


While its primary use is for desktop software, Ghostscript is also used server-side, where it is typically included with image conversion and file upload processing toolkits, such as the popular ImageMagick.


The proof-of-concept code released by Nguyen on Sunday exploits this latter scenario, allowing an attacker to upload a malformed SVG file that escapes the image processing pipeline and runs malicious code on the underlying operating system.


While Nguyen released the public exploit for this bug, he is not the one who discovered the vulnerability.


The person who did is Wunderfund CTO and founder [Emil Lerner](https://twitter.com/emil_lerner), who found the bug last year and used it to obtain bug bounties from companies like Airbnb, Dropbox, and Yandex.


Details about the vulnerability leaked into the public domain last month after Lerner held a talk at the [ZeroNight X security conference](https://zeronights.ru/en/reports-en/hotpics-2021/) about the current attack vector posed by server-side image conversion tools and used the Ghostscript zero-day as an example.





“Exploit seems to be correct,” Lerner told *The Record* yesterday in a private conversation when asked about Nguyen’s proof-of-concept.


The researcher told *The Record* that he was not aware of any patch for the Ghostscript vulnerability prior to Nguyen’s release of the public exploit.


Artifex, the company behind the Ghostscript project, did not return a request for comment sent on Monday via their website.


This is the second time the Ghostscript project is in the news because of security issues. [In August 2018](https://bugs.chromium.org/p/project-zero/issues/detail?id=1640), a Google security researcher discovered multiple critical vulnerabilities in the Ghostscript library that Artifex failed to patch in time. The company did, however, release fixes two days later after the Ghostscript security issues were broadly exposed.





#### Tags:
[[Ghostscript]] [[The Record]]
