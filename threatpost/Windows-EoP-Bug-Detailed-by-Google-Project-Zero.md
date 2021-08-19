# Windows EoP Bug Detailed by Google Project Zero
### Microsoft first dismissed the elevation of privilege flaw but decided yesterday that attackers injecting malicious code is worthy of attention.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168823)
+ Date: August 19, 2021  12:58 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/19124155/window-e1629391328534.jpeg)
Google Project Zero has apparently blown its own 90-day disclosure window. On Wednesday, it disclosed details about an elevation of privilege (EoP) flaw in Windows that it reported to Microsoft on July 8.


Granted, Microsoft initially said that it wasn’t going to bother: On July 18, it told Project Zero that exploitation requires compromising an [AppContainer](https://docs.microsoft.com/en-us/windows/win32/secauthz/appcontainer-for-legacy-applications-) – I.e., a sandbox used to test Windows app security before letting the apps run free – that’s presumably already accessing the internet.


Given that, Microsoft said that “it’s a non-issue and they will not fix it,” according to Project Zero security researcher James Forshaw. Then, after further analysis, Microsoft spun on its heel. Yesterday, on Wednesday, the company said that yes, it would be tackling the beast.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


As Forshaw recounted in a technical [report](https://bugs.chromium.org/p/project-zero/issues/detail?id=2207&can=2&q=&colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary&cells=ids) about the flaw, the researcher basically shrugged at the “can’t be bothered” response from Redmond. It’s still an issue, Forshaw said at the time, given that attackers could still exploit the flaw to sneak in via intranet locations that, otherwise, they wouldn’t typically be able to get at. Nonetheless, a day after Microsoft’s “Won’tFix” response on July 18, Forshaw accepted the company’s choice to ignore the vulnerability.


Bullies in the Sandbox
----------------------


The gist of the matter is that the default rules of the Windows Filtering Platform (WFP) – a set of API and system services that provide a platform for creating network filtering apps – permit executable files to connect to TCP sockets in AppContainers, which can enable malicious actors to pull off EoP.


Essentially, some rules defined in WFP can be matched by a malicious actor to connect to an AppContainer and inject malicious code.


As Forshaw explained in his report, connecting to an external network resource from an AppContainer is enforced through default rules in the WFP: “For example, connecting to the internet via IPv4 will process rules in the FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V4 layer,” he wrote.


That layer can contain rules such as “InternetClient Default Rule” that will match if the caller is in an AppContainer (AC) that’s internet-connected. “If a match is made then the connection is allowed,” Forshaw continued. “Eventually an AC process will match the ‘Block Outbound Default Rule’ rule if nothing else has, which will block any connection attempt.”


He gave this example of one such rule, found in both IPv4 and IPv6 connect layers and illustrated below:



> Name : Allow outbound TCP traffic from dmcertinst.exe  
> 
> Action Type: Permit  
> 
> Key : e83eb750-283b-43e6-b8b5-2ec0df33a2f0  
> 
> Id : 70341  
> 
> Description:  
> 
> Layer : FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_V4  
> 
> Sub Layer : {b3cdd441-af90-41ba-a745-7c6008ff2300}  
> 
> Flags : Indexed  
> 
> Weight : 422487342972928  
> 
> Conditions :  
> 
> FieldKeyName MatchType Value
> 
> 
> ———— ——— —–
> 
> 
> FWPM\_CONDITION\_ALE\_APP\_ID Equal \device\harddiskvolume3\windows\system32\dmcertinst.exe
> 
> 
> FWPM\_CONDITION\_IP\_PROTOCOL Equal Tcp
> 
> 


“This will permit TCP traffic to any host and port as long as the process executable is dmcertinst.exe,” Forshaw noted. “There’s similar rules for omadmclient.exe and deviceenroller.exe. As there’s no restrictions other than the process executable an AC just has to inject code into an instance of one of those processes and it can connect to arbitrary TCP hosts.”


It’s a ‘General Problem’
------------------------


Forshaw noted that this is, of course, “a general problem” for any application that’s added permit rules that can be reached by an AC, given that the rules could be matched ahead of the blocking rule. Although the flaw affects any system with these default rules, he specifically mentioned testing on Windows 10 version 2004 in his report.


“Of course this is no doubt by design, but the problem here is these rules are there by default on all systems I’ve tested,” he elaborated. “Therefore any system would be vulnerable. Note this doesn’t grant access to localhost, as that fails in the ACCEPT/RECV layer which blocks AppContainer localhost connections early.”


As far as a fix goes, Forshaw suggested that perhaps default rules “shouldn’t match AC processes (so add a check for FWPM\_CONDITION\_ALE\_PACKAGE\_ID) or they should be ordered after the AC block rule.”


Then again, maybe the rules are “too flexible,” he hypothesized, and provide too broad an attack surface. “Even limiting to a specific port might at least reduce the attack surface,” he said. “I’m not sure if there’s a general way of fixing the issue, but as an AC process can’t enumerate the current rules (AFAIK) then an AC process would never know if non-default rules have been added that they could abuse.”


Microsoft Changes Its Mind
--------------------------


As of Wednesday, Microsoft had decided to take this EoP problem seriously, reaching out to Project Zero to let Forshaw know that it had decided to work on the issue in spite of its initial feedback being that it was “out of scope.” At this point, a fix is in progress, Forshaw said.


Threatpost has reached out to Forshaw for a clarification of Project Zero’s 90-day disclosure policy, which, in this case, appears to have shrunk. The disclosure policy, as Forshaw posted in his report, states the following:



> This bug is subject to a 90-day disclosure deadline. If a fix for this issue is made available to users before the end of the 90-day deadline, this bug report will become public 30 days after the fix was made available. Otherwise, this bug report will become public at the deadline. The scheduled deadline is 2021-10-06. —Project Zero, Issue 2207
> 
> 


Microsoft fixed a similar [EoP flaw](https://threatpost.com/win-10-serioussam/168034/) in Windows 10 last month. The bug would have opened all systems to attackers to access data and create new accounts on systems. Microsoft issued a workaround to prevent such exploitation.


Threatpost reached out to Microsoft for some insight into what made the company change its mind about fixing this flaw.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Forshaw]] [[Microsoft]] [[Windows]] [[AppContainer]] [[90-day]] [[TCP]] [[Wednesday,]] [[that’s]] [[Threatpost]] [[ThreatPost]]
