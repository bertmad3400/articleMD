# Google Emergency Update Fixes Two Chrome Zero Days
### This is the second pair of zero days that Google’s fixed this month, all four of which have been actively exploited in the wild. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175266)
+ Date: September 30, 2021  6:38 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/02/25133033/Chrome_Web_Browser_Google.jpg)
Google has pushed out an emergency Chrome update to fix yet another pair of zero days – the second pair this month – that are being exploited in the wild.


This hoists this year’s total number of zero days found in the browser up to a dozen.


On Thursday evening, the web Goliath released the [Chrome 94.0.4606.71](https://chromereleases.googleblog.com/2021/09/stable-channel-update-for-desktop_30.html) stable channel release for Windows, Mac and Linux to fix the two zero-days, which were included in an update with a total of four security fixes.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“Google is aware the exploits for CVE-2021-37975 and CVE-2021-37976 exist in the wild,” Google disclosed with the release of the browser fixes.


No Details for the Zero Days
----------------------------


Just as it did with the pair of zero days that were being exploited in the wild [earlier this month](https://threatpost.com/google-chrome-zero-day-exploited/169442/), Google is keeping technical details close to the vest, at least until most users have had a chance to plug in the update. The company started pushing out Chrome 94.0.4606.71 to users worldwide in the Stable Desktop channel, and it should be available to all users within coming days.


“Access to bug details and links may be kept restricted until a majority of users are updated with a fix,” the company said in Thursday’s security update. “We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed.”


Here are details on the two zero-days:


The second high-severity bug Google addressed on Thursday, **CVE-2021-37974**, is another use-after-free vulnerability: this time, in safe browsing.


The earlier pair of zero days Google addressed this month in a Sept. 13 update, CVE-2021-30632 and CVE-2021-30633, were likewise being actively exploited in the wild. The first was an out-of-bounds write in V8 JavaScript Engine, and the second was a use-after-free vulnerability in the IndexedDB API.


Use After Free
--------------


Use-after-free issues [can result in](https://cwe.mitre.org/data/definitions/416.html) any number of attack types, ranging from the corruption of valid data to the execution of arbitrary code. Writing for Threatpost’s [InfoSec Insider](https://threatpost.com/microsite/infosec-insiders-community/) series, Gurucul CEO Saryu Nayyar has described these flaws as among the year’s [most dangerous software weaknesses](https://threatpost.com/2021-angerous-software-weaknesses/169458/).


As Nayyar tells it, use-after-free vulnerabilities entail memory manipulation: “When an application needs memory for a variable, it either programmatically allocates that memory, or the underlying platform (JVM or .NET Runtime),” she wrote earlier this month. “When the application is done with that memory, either it or the platform returns it to the free memory list.”


But if an attacker has managed to get the memory address, the actor “can gain access to the free memory list, and insert malicious software into free memory,” Nayyar continued. “The next time that memory is allocated, it is allocated with a payload that can cause harm. Further, the memory isn’t wiped clean when it is returned to the free memory list, enabling attackers to read the contents of that memory.”


She noted that some commercial debuggers can look into a running process and let programmers – or attackers – obtain information using memory locations. “While these types of debuggers are needed, any tool that lets attackers look into specific memory addresses to determine their contents has the potential to be used as a hacking tool,” Nayyar advised.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Google]] [[Nayyar]] [[use-after-free]] [[ThreatPost]]
