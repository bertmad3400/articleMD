# Windows security in ’22 — you need more than just antivirus software
### Antivirus software is useful, but sometimes can cause more trouble than it's worth. To be really secure, Windows users have to do more.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3646552/windows-security-in-22-you-need-more-than-just-antivirus-software.html
+ Date: 2022-01-10T06:10-05:00
+ Author: Susan Bradley


## Article:
![Article Image](https://images.idgesg.net/images/article/2021/03/maze-1-100880563-large.jpg?auto=webp&quality=85,70)

Do you need antivirus in 2022 — especially when some options now come with a cryptominer built in?

Several antivirus vendors — some options free, others, paid — have begun bundling their antivirus products with software that generates virtual currency. Of all of the requirements for antivirus, using excess cycles on your computer to generate crypto-coins is not on my list of must-haves.

Recently, [Krebs on Security](https://krebsonsecurity.com/2022/01/500m-avira-antivirus-users-introduced-to-cryptomining/) noted that both Norton Antivirus and Avira have told users that versions of their respective software now include a cryptominer. While it’s not enabled by default, it still gives me pause; antivirus is supposed to protect us from such potentially unwanted software, and these two vendors are now including it in their wares.

I have often thought that *no* antivirus software is better than the various options available. I’ve tracked patch installations on Windows platforms for years and have often seen bad interactions between antivirus software and Windows updates. Early in the Windows 7 release cycle, I regularly advised users to uninstall antivirus software before applying security updates or service packs to avoid problems. Some users also saw side effects with browsers and had to uninstall or reinstall their antivirus software to get their browser working properly. (Even with Windows 10, it’s important to ensure users are running a supported version of antivirus.)

Just think of the number of times historically that Microsoft has used [installation blocks](https://support.microsoft.com/en-us/topic/important-windows-security-updates-and-antivirus-software-4fbe7b34-b27d-f2c4-ee90-492ef383fb9c) due to interaction with antivirus products.

As Microsoft explained one case in 2018: “The compatibility issue arises when antivirus applications make unsupported calls into Windows kernel memory. These calls may cause stop errors (also known as blue screen errors) that make the device unable to boot. To help prevent these stop errors, Microsoft is currently only offering the January and February 2018 Windows security updates to devices that are running antivirus software that is from antivirus software vendors who have confirmed that their antivirus software is compatible by setting a required registry key.”

The issue then was that some antivirus vendors used undocumented code hooks — rather than hooking into the Windows firewall — to perform antivirus scans. During the installation of a service pack, these hooks into the Windows kernel would conflict with the new code and trigger blue screens or at a minimum trigger the rollback of the service pack install.

For smaller businesses with 300 users or less, Microsoft is in the process of testing Microsoft Defender for Business, a [security suite](https://techcommunity.microsoft.com/t5/small-and-medium-business-blog/introducing-microsoft-defender-for-business/ba-p/2898701) that adds the ability to manage, track, and protect against threats in a network. In addition to scanning for, and alerting about, issues, it also provides actionable security tips unique to each platform. It will often recommend Attack Surface Reduction rules that can help make your network more secure. If you’re an SMB, I recommend that you check out the preview to see if your network would benefit from the additional guidance.

For home users, I remain a fan of Microsoft Defender, which is built into both Windows 10 and 11. Though some would rather have a third-party vendor be on the lookout for security issues — they argue that relying on Defender is like letting the fox guard the hen house — my philosophy is that any form of antivirus is reactionary, not proactive. Antivirus is not the best tool to filter email for phishing attacks, nor is it the best tool to check where you browse online. You need security services in front of your computer, not just something that checks the software on your computer.

These days, security is about more than antivirus. Start with the basics, such as your email provider, and review your options. If you are still using the same ISP-based email from 20 years ago, it’s time to investigate other email services that might scan and review or attacks better. And your options extend beyond just Gmail and Outlook; look to services such as [ProtonMail](https://protonmail.com/) for secure and encrypted email.

Next, use a password manager to keep track of passwords or even (gasp!) write your passwords down in a small notepad. Writing down passwords isn’t the main problem these days; it’s the fact that many users regularly reuse the *same* passwords over and over on various websites. Thus, if one site is breached, attackers can try those stolen passwords elsewhere and often get in.

The next key security move is to back up everything. And then back it up again — preferably using offline backup media. That way, should ransomware hit your computer, attackers won’t be able to encrypt your backups, too. Don’t make one backup, make several.

Be sure to secure your home network by ensuring your router has the latest firmware and the password for it is secured. Security blogger Corey Parker has some [great suggestions on reviewing the DHCP listing](https://firewallsdontstopdragons.com/new-years-resolutions-2021/) to see who’s been logging into your home network. If you don’t recognize a device listed there, disable it. If you accidentally turn off a streaming device you use every day, you can reenable it. This time, however, document what each device is so you know exactly what is connecting to your network.

Do update everything in a timely manner, but don’t rush. We follow this rule on the Askwoody.com site all the time; I always recommend holding back a bit before updating. It’s a matter of timing. You want to install security updates, just not necessarily on the first day they’re out.

Finally, always be on the lookout for two-factor authentication, especially for key sensitive sites. Don’t just rely on a password for access, ensure that you add a text message sent to your phone as the bare minimum to protect your accounts.

The bottom line these days is that security goes beyond just antivirus on your computer. That said, it’s important to choose antivirus software [supported by the vendor](https://support.microsoft.com/en-US/windows-antivirus-software-providers#avtabs=win7) and approved for your platform. And find one that keeps you safe from cryptominers you don’t want on your system. Bundling in a cryptominer with the very software you purchased to keep you safe isn’t the way forward.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Proton]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Cryptominer]] [[Computerworld]]

