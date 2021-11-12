# Windows 10 Privilege-Escalation Zero-Day Gets an Unofficial Fix
### Researchers warn that CVE-2021-34484 can be exploited with a patch bypass for a bug originally addressed in August by Microsoft.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176313)
+ Date: November 12, 2021  2:49 pm
+ Author: Tara Seals


## Article:
![microsoft patch tuesday](https://media.threatpost.com/wp-content/uploads/sites/103/2019/06/11161849/microsoft_patch.png)
A partially unpatched security bug in Windows that could allow local privilege escalation from a regular user to System remains unaddressed fully by Microsoft – but an unofficial micropatch from oPatch has hit the scene.


The bug ([CVE-2021-34484](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34484)) was originally disclosed and patched as part of Microsoft’s [August Patch Tuesday updates](https://threatpost.com/exploited-windows-zero-day-patch/168539/). At the time, it was categorized as an arbitrary directory-deletion issue that was considered low-priority because an attacker would need to locally log into the targeted computer to exploit it, which, in theory, would allow the adversary to delete file folders anyway.


However, the security researcher who discovered it, Abdelhamid Naceri, [soon uncovered](https://halove23.blogspot.com/2021/10/windows-user-profile-service-0day.html) that it could also be used for privilege escalation, which is a whole other ball of wax. System-level users have access to resources, databases and servers on other parts of the network.


Abdelhamid also took a look at Microsoft’s original patch, subsequently finding a bypass for it via a simple tweak to the exploit code he had developed, essentially reverting it to zero-day status.



“The vulnerability lies in the User Profile Service, specifically in the code responsible for creating a temporary user profile folder in case the user’s original profile folder is damaged or locked for some reason,” explained 0Patch’s Mitja Kolsek in a [Thursday writeup](https://blog.0patch.com/2021/11/micropatching-incompletely-patched.html) . “Abdelhamid found that the process (executed as Local System) of copying folders and files from user’s original profile folder to the temporary one can be attacked with symbolic links to create attacker-writable folders in a system location from which a subsequently launched system process would load and execute attacker’s DLL.”


The exploit is straightforward: An attacker would create a specially crafted symbolic link (essentially, a shortcut link that points to a specific file or folder), then would need to save it in the temporary user profile folder (C:\Users\TEMP).


Then, when the User Profile Service copies a folder from user’s original profile folder as described by Kolsek, the symbolic link will force it to create a folder containing a malicious library (DLL) payload somewhere else where the attacker would normally not have permissions to create one.


“Microsoft, even though believing the vulnerability only allowed for deletion of an arbitrarily ‘symlinked’ folder, made a conceptually correct fix: it checked whether the destination folder under C:\Users\TEMP was a symbolic link, and aborted the operation if so,” explained Kolsek. “The incompleteness of this fix, as noticed by Abdelhamid, was in the fact that the symbolic link need not be in the upper-most folder (which Microsoft’s fix checked), but in any folder along the destination path.”


The micropatch fixes this by extending the security check for symbolic links to the entire destination path by calling the “GetFinalPathNameByHandle” function.


It should be noted that a workable exploit also requires attackers to be able to win a race condition (with unlimited attempts) since the system will be attempting to perform two operations (one malicious, one legitimate) at the same time. Also, even though Abdelhamid said that “it might be possible to [exploit] without knowing someone [else’s] password,” so far, having user credentials for the targeted computer remains an obstacle, Kolsek noted.


The bug affects Windows 10 (both 32 and 64 bit), versions v21H1, v20H2, v2004 and v1909; and Windows Server 2019 64 bit.


Microsoft hasn’t released a timeline for updating its official patch and didn’t immediately respond to a request for comment.


***Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** [***“Password Reset: Claiming Control of Credentials to Stop Attacks,”***](https://bit.ly/3bBMX30) ***on Wed., Nov. 17 at 2 p.m. ET. Sponsored by Specops.***


[***Register NOW***](https://bit.ly/3bBMX30)***for the LIVE event!***




#### Tags:
[[Windows]] [[Microsoft’s]] [[Abdelhamid]] [[user’s]] [[ThreatPost]]
