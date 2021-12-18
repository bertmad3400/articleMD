# After a rocky year for patching, a look ahead to ‘22
### If 2021 was all about ongoing patch issues with Windows 10 — and the arrival of Windows 11 — 2022 might be the year those issues become at least manageable.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3644275/after-a-rocky-year-for-patching-a-look-ahead-to-22.html
+ Date: 2021-12-13T11:38-05:00
+ Author: Susan Bradley


## Article:
![Article Image](https://images.idgesg.net/images/article/2021/07/dreamstime_l_97816995-100896931-large.jpg?auto=webp&quality=85,70)

For Windows users, it’s been a [rough year for security vulnerabilities and patches](https://www.computerworld.com/article/3643411/a-look-at-microsofts-patches-and-fixes-in-2021-the-year-of-change.html). Now, my view about these kinds of problems is always a bit jaded. I pay attention to what people post about on the [Askwoody forums](https://www.askwoody.com/forums/forum/askwoody-support/), and they typically don’t say much if they have no problems. All I see are people with issues, not those with systems that install patches and reboot just fine.

That said, Windows servicing still genuinely concerns me at times. Before I look ahead to 2022, I want to dwell a bit on where we are now.

When Windows 10 misbehaves and balks at installing updates, the solution isn’t always easy. Case in point: [having to use the DISM technique](https://www.computerworld.com/article/3643309/using-dism-to-install-windows-updates.html) to get a misbehaving Windows system back on track. I’ve seen Microsoft support engineers use this to get Windows servers into patchable condition when there’s no easy way to reinstall the OS or do an [in-place repair over the top](https://www.computerworld.com/article/3262979/how-to-fix-windows-10-with-an-in-place-upgrade-install.html). But no one should have to rely on near-critical surgery techniques to get updates installed. Windows users should be able to use a sfc/scannow or plain DISM commands to repair their OS.

What’s behind these update issues? In my experience, the failure often involves registry cleaners or third-party programs that damage the installer software. That shouldn’t happen, and yet it does. Annoyingly so.

Faced with this kind of problem, server administrators often must choose whether to “spin up” a new operating system — and move the roles or duties to another server — or turn to DISM commands. My recommendation to admins? Set up your deployment so you don’t cringe when thinking of rebuilding any particular server. Build in resilience so you can quickly move files and roles between servers if a platform runs into update troubles. And limit your use of third-party tools.

In short: Try to keep hardware deployed in a way that mirrors what Microsoft is expecting. Don’t reuse hardening techniques that you would have done on Server 2003 or Server 2008. Evaluate your deployments and try to stick with [security baselines](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-configuration-framework/windows-security-baselines) — not inherited security deployment settings.

In the last several years, we’ve mainly tracked issues and side effects involving Windows 10. (While Windows 8.1 and Windows 7 are still in use, their numbers are dwindling.) As 2021 fades out, Windows 11 is gaining market share and will continue to do so in 2022. Given its steep hardware requirements, many of us won’t see Windows 11 until we purchase new computers; you can, of course, [bypass the hardware mandates](https://support.microsoft.com/en-us/windows/ways-to-install-windows-11-e0edbbfb-cfc5-4011-868b-2ce77ac7c70e?ranMID=24542), but I don’t recommend doing so. It’s better to run Windows 10 for several more years on existing hardware and move to Windows 11 when you upgrade your PC.

One of the major advantages coming with Windows 11 is the size of updates. Microsoft patching can sometimes require grabbing 1GB or more of updates every month — not ideal for anyone without a Fiber connection and lots of bandwidth. In Windows 11,  Microsoft has [drastically reduced the size of the patching](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/how-microsoft-reduced-windows-11-update-size-by-40/ba-p/2839794): updates are 40% smaller. That will be a boon for those who don’t have the connectivity (or time) to download large files.

And now, for some 2022 predictions…

* Windows 10 will turn into a boring and predictable operating system. Because Microsoft will be focusing all its energy and effort on Windows 11, Windows 10 will get security releases and bug fixes, but few major changes. The annual feature release cadence will make it a stable platform for both home and business users. Meanwhile, more changes will be coming to Windows 11. Already Microsoft is bringing things like a new Notepad and tweaking [Android applications on Windows 11](https://blogs.windows.com/windows-insider/2021/10/20/introducing-android-apps-on-windows-11-to-windows-insiders/). Given the negative feedback from users, I predict (and hope) that Microsoft will continue to work on the menu system.
* Microsoft will make more changes to Windows 11 once enterprises start providing more feedback. It gets a lot of feedback in its insider program — case in point, [more than 25,000 upvotes](https://aka.ms/AAd2ifw) for bringing back the ability to move the taskbar to the top and sides of Windows 11 —but often we see more changes occur when businesses start deploying the operating system.
* The desktop operating system will be less important. For many years, certain key line-of-business apps were best on a desktop. But the tide is turning more towards online applications. Mind you, I don’t think consumers and small to mid-sized businesses (SMBs) will be moving to [Windows 365](https://www.microsoft.com/en-us/windows-365?ef_id=abb0b063887a1161272dd1d5dacb362d:G:s&OCID=AID2200899_SEM_abb0b063887a1161272dd1d5dacb362d:G:s&msclkid=abb0b063887a1161272dd1d5dacb362d&rtc=1), Microsoft’s hosted operating system. Instead, I believe we’ll be moving to platforms that can be accessed from a variety of devices ranging from tablets, iPads, and phones. Using a full-blown desktop and keyboard is still the most effective and efficient way to work on a project, but these days we’re not always near a desk and a desktop. We’ve learned to be more flexible as our work needs change, and that trend will continue.
* Expect more changes as Microsoft responds to feedback and as users make changes in how we work with technology. Ultimately, any software company has to figure out how we’re going to use technology in the future. The last few years have been disruptive, and 2022 will be no different. Buckle your seatbelt, more changes are coming.





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Dism]] [[Computerworld]]

