# A look at Microsoft's patches and fixes in 2021 — the year of change
### This year saw the (planned) end of Windows 10, the birth of Windows 11, a new version of Edge, a plethora of patches —  and not a few spillover effects from them. It wasn't your typical year for Microsoft.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3643411/a-look-at-microsofts-patches-and-fixes-in-2021-the-year-of-change.html
+ Date: 2021-12-07
+ Author: Susan Bradley


## Article:
![Article Image](https://images.idgesg.net/images/article/2020/07/software_update_by_gocmen_gettyimages-1146311500_2400x1600-100852481-large.jpg?auto=webp&quality=85,70)

As we near the end of another year, I like to look back at the past 12 months in patching from MIcrosoft. What changed (a lot), what didn’t (patch-related problems). We began 2021 thinking Windows 10 would continue to be serviced and updated as usual, for instance. We end the year knowing different. (I’ll have some predictions for 2022 next week.)

We now know that Windows 10 will not receive updates indefinitely. Earlier this year, Microsoft unveiled Windows 11 and announced it would need certain hardware and Trusted Platform Module installed before machines would receive new OS. Given that most users only have hardware that will support Windows 10, many will be running the older OS until 2025. Microsoft already [announced it will be providing security updates for Windows 10 until then](https://blogs.windows.com/windowsexperience/2021/11/16/how-to-get-the-windows-10-november-2021-update/) and will move to an annual feature release model — matching the cadence for Windows 11. (My prediction for 2025: Microsoft will offer extended security patches for even consumer versions of Windows 10 because so many of us will have still usable machines unable to update to Windows 11. Come back in 2025 and we’ll see if I’m right.)

We started 2021 worrying about whether major companies were getting attacked with a back door vulnerability that entered systems [through monitoring software called Solarwinds Orion](https://www.computerworld.com/article/3602549/solarwinds-solorigate-and-what-it-means-for-windows-updates.html). A security company called FireEye found unusual behavior in their systems and traced it back to third-party monitoring software it implanted in its updating software. This vulnerability was an eye-opener for businesses that rely on the security of our vendors.

January also saw Microsoft [moving to disable Adobe Flash in Windows](https://www.computerworld.com/article/3602450/microsoft-takes-steps-to-scrub-flash-from-windows.html). I always felt that embedding flash into the operating system was a bad decision. Adobe Flash had a bad security rep and embedding it meant mandatory Flash patching for Windows systems. A month later, in February, Microsoft announced it would [phase out the old Edge browser in favor of the new Chromium-based version](https://www.computerworld.com/article/3606788/microsoft-to-replace-legacy-edge-in-april-with-chromium-based-version.html) as of April 2021.

In March, Microsoft released an [out-of-band update for Exchange email servers](https://www.computerworld.com/article/3610703/pause-patch-tuesday-updates-watch-out-for-exchange-server-attacks.html). Initially it said the attacks were specifically targeted against certain businesses. But a few days later, it was clear that even small businesses were hit by attackers using the vulnerability. Microsoft customers stressed that servicing Exchange email was difficult for several reasons. First, taking a mail server offline for maintenance has to be planned. Second, ensuring that mail flow is not affected means many mail admins were woefully behind on patching. Microsoft had to release patches for versions that were long out of support just to ensure that firms were protected. Even the [Federal Bureau of Investigation](https://www.csoonline.com/article/3615691/fbi-cleans-web-shells-from-hacked-exchange-servers-in-rare-active-defense-move.html) got into the act and proactively patched the web shells of affected servers to ensure all customers were protected. This unusual act set a precedent we’ve yet to see repeated.

In April, as promised, Microsoft released the Chromium-based Edge on Windows 10. The company also changed 20H1 and 20H2 to integrate Service Stack updates (SSUs) in the Cumulative update releases. Microsoft did so to make it easier for IT admins to always have the latest servicing stack update installed.

May turned out to be a big month, with the end of support for Windows 10, version 1803 (Enterprise, Education, IoT Enterprise); Windows 10, version 1809 (Enterprise, Education, IoT Enterprise); Windows 10, version 1909 (Home, Pro, Pro Education, Pro for Workstations); and Windows Server, version 1909 (Datacenter, Standard).

That same month, Microsoft dropped SHA-1 support from its download site, which meant that many older Windows tools suddenly no longer worked. It took several months to get [WUShowhide tool](https://www.askwoody.com/2021/wushowhide-is-back/) re-signed with SHA2. And finally, on May 18 [official release of Windows 10 21H1](https://www.computerworld.com/article/3619490/microsoft-releases-windows-10-21h1-as-another-minor-os-refresh.html) arrived. A minor, quick update, 21H1 brought a few features for Windows 10 and was relatively painless to deploy.

In July, users saw the [first of many print spooler patches](https://www.computerworld.com/article/3624584/to-patch-or-not-to-patch-that-is-the-question.html) that led to side effects for the rest of 2021. The “Print Nightmare” caused [printing nightmares for many IT admins](https://www.computerworld.com/article/3625472/a-big-july-patch-tuesday-and-the-ongoing-print-nightmare.html). While less disruptive to consumers, it showed that print spooler code has long allowed attackers to enter computer systems. Also arriving that month, a fix to remove Adobe flash completely from Windows systems and the inclusion of “News and Interests” in a cumulative update rather than having to wait for a feature release to be deployed.

August saw yet another print spooler vulnerability patched — and the [first of many fixes for the printing issues](https://www.computerworld.com/article/3630629/windows-print-nightmare-continues-enterprise.html) introduced in July. In October, we got the first patches for the just-released Windows 11, including a remote code execution fix. And in November, Microsoft pushed out updates that also introduced unwanted side effects with single-sign-on and certain Kerberos deployments.

Oh, and we can’t forget [Windows 10 21H2](https://docs.microsoft.com/en-us/windows/whats-new/whats-new-windows-10-version-21h1), a minor released that did not add many new features. What it *did* bring was a major change to the Windows 10 feature release cadence. Microsoft announced that it would no longer be supporting a twice-yearly release schedule, [opting instead to match Windows 11’s once-a-year schedule](https://www.computerworld.com/article/3640973/microsoft-releases-its-windows-10-november-2021-update.html). (This had long been a request from both users and IT administrators.

As I look back now, I realize how many changes we’ve had to deal with in 2021. Too often, Windows users complain that security updates cause disruptions because they make changes to the operating system. Yet, many of these changes are actually introduced in the feature release process. With Microsoft finally moving to a once-a-year model, these disruptions will hopefully be minimized.

As we near the last major Patch Tuesday update for 2021 — next Tuesday, Dec. 14 — now’s a good time to review the health of your system. Is there enough space available on your C drive? If you’re using a desktop computer, can it handle more RAM? Should you at least take a can of compressed air and blow out the dust bunnies? (Yes.) As you reflect on any patching issues you faced this year, feel free to send any lingering questions to Askwoody.com. We love to help.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Admins]] [[Computerworld]]

