# Microsoft beefs up Edge's security against zero-day attacks
### In the latest beta release of its Edge browser, Microsoft introduced a new feature for IT admins to better secure the Chromium-based app against web-based attacks on desktop systems.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3648068/microsoft-beefs-up-edges-security-against-zero-day-attacks.html
+ Date: 2022-01-20T13:16-05:00
+ Author: Lucas Mearian


## Article:
![Article Image](https://images.idgesg.net/images/idge/imported/imageapi/2021/11/26/20/keyboard_laptop_microsoft-edge-logo_web-browser_by-urupong-getty-images-1200x800-100816809-large-100912436-large.jpg?auto=webp&quality=85,70)

In the latest release of its Edge beta, Microsoft introduced a new way for IT admins to better secure the Chromium-based browser against web-based attacks.

The [release notes for Microsoft Edge Beta Channel](https://docs.microsoft.com/en-us/deployedge/microsoft-edge-relnote-beta-channel#version-980110823-january-14) describe the new security features as employing several techniques to guard against so-called zero-day exploits; Zero-day exploits are software or network vulnerabilities developers are unaware of, and so they’ve not been patched.

ADVERTISEMENTImagine if the keylock mechanism on your home’s backdoor was faulty and jiggling the doorknob released the latch. Burglars could walk door to door looking for that particular vulnerability and jiggle doorknobs until one opened. Zero days are the same concept, but in cyberspace.

IT systems are increasingly coming under assault by new viruses, cyberwarfare, and brute-force attacks. One of the easier avenues into an organization’s systems is through an unknown, and unpatched, vulnerability — especially one outside an organization’s firewalls (i.e., an end-user’s device). The obvious problem with zero-day exploits is they're hard to catch when developers and security admins don't know what to look for, according to Jack Gold, principal analyst at J. Gold Associates.

Hackers — both good and bad actors — sell zero-day exploits they discover. The good guys sell them to corporations to bolster their security; the bad guys sell them to other bad actors. For example, at the beginning of the pandemic, [hackers sold software vulnerabilities discovered in the video conferencing app Zoom](https://www.tripwire.com/state-of-security/featured/zoom-zero-day-exploit-sale-500000/); one exploit was for Windows PCs, the other, for macOS systems. The hackers allegedly saw a half million-dollar payday.

Microsoft’s new Edge feature enables admins to configure certain Group Policies for end-user desktops (Windows, macOS, and Linux) to help protect against zero-day vulnerabilities. When turned on, the feature adds Hardware-enforced [Stack Protection](https://techcommunity.microsoft.com/t5/windows-kernel-internals-blog/understanding-hardware-enforced-stack-protection/ba-p/1247815), [Arbitrary Code Guard](https://blogs.windows.com/msedgedev/2017/02/23/mitigating-arbitrary-native-code-execution/) (ACG), and [Content Flow Guard](https://docs.microsoft.com/en-us/windows/win32/secbp/control-flow-guard) (CFG) as supporting security mitigations to better protect users online. The group policies include: EnhanceSecurityMode; EnhanceSecurityModeBypassListDomains; and EnhanceSecurityModeEnforceListDomains.

"So the safest way to protect browsing is to prevent the browser from interacting with any other parts of the machine," Gold said. "Basically, the safest way to do this is to put the browser in a 'vault' where all the browser code remains locked into a virtual section of the machine and can’t go anywhere else. It’s basically a containment policy. What Microsoft is trying to do with the new Edge features is to make sure that anything in the browser can’t interact with over apps and/or modify the OS."

Stack protection and arbitrary code guard, Gold explained, prevent any zero-day exploits that would have a way to exit from the browser into the machine. Content follow is similar in that it prevents interacting with and taking over apps (e..g, opening an infected doc in Word).

"So, it is this a big deal," Gold said. "There are many examples of machines being infected with malware from browsing the wrong site. Anything that can prevent this from happening is good."

Conversely, setting policies also means that some sites that legitimately need to access other apps on an end-user's device, and/or access parts of the OS, will not be able to, Gold said. While that may be fine for casual internet browsing, the biggest challenge is that, if set this way, some internal browser-based apps may not run (e.g., pop up screens to fill in info or get a status).

ADVERTISEMENT"So, as with any security technology, there are pros and cons to shutting down specific features. But the potential damage of a zero-day getting into my machine, and then into the networks is a good reason to cause a bit of inconvenience," Gold said.

There are already other third-party browser implementations that have done a similar “run in isolation” feature for a while now; Edge is now catching up, Gold said.

The update to the Edge beta also introduces a custom primary password feature. While the browser already allows  users to add an authentication step before saved passwords are auto-filled in web forms (in other words, two-factor authentication), being able to create a custom password adds yet another layer of privacy and helps prevent unauthorized users from using saved passwords to logon to websites.

Custom primary password is an evolution of that same feature, where users can now use a custom string of their choice as their primary password. After it's enabled, users will enter this password to authenticate themselves and have their saved passwords auto-filled into web forms.

ADVERTISEMENTAlong with the new security features, [other improvements](https://techcommunity.microsoft.com/t5/discussions/dev-channel-update-to-99-0-1135-5-is-live/m-p/3066199) include a fix for an issue where default search providers can't be removed, a small tweak to show search suggestions immediately when you click on the address bar, and the addition of Web Capture when viewing PDFs in Microsoft Edge.

Finally, Microsoft has updated its scrollbars with an overlay-based design in Edge. Users can turn this feature on in edge://flags.

Enabling this feature hides the toolbar, and prevents your scrollbar from appearing, requiring a user to hover the mouse over the edge of your window to trigger the scrollbar to appear.

Disabling it will make the toolbar automatically appear.

ADVERTISEMENT



## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Zero-day]] [[Microsoft]] [[Apps]] [[Admins]] [[End-user]] [[Computerworld]]
#### urls
edge://flags.Enabling

