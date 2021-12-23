# What’s all the fuss with Log4j2?
### As companies scramble to determine whether they're vulnerable to the Log4j2 flaw, SMBs may not have the resources to do so themselves. Here's what you can do.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3645430/whats-all-the-fuss-with-log4j2.html
+ Date: 2021-12-20T10:16-05:00
+ Author: Susan Bradley


## Article:
![Article Image](https://images.idgesg.net/images/article/2019/11/microsoft_windows_security_binary_lock_by_gerd_altmann_cc0_via_pixabay_1800x1200-100817345-large.jpg?auto=webp&quality=85,70)

If you’re a Windows user tracking various tech and security websites, you’ve probably read about [the Log4j2 vulnerability](https://www.csoonline.com/article/3645132/second-log4j-vulnerability-carries-denial-of-service-threat-new-patch-available.html) that’s taken the internet by storm, literally and figuratively. While large firms have application developers that know what code they’ve used — and thus authoritatively know where their firm may be vulnerable — what if you are a smaller company without such resources? (Or what if you’re a home user wondering whether you need to be concerned?)

First, let’s explain what Log4j is: a logging framework that developers who code use to build what they need in their software. It was written in [Java](https://www.tutorialspoint.com/log4j/log4j_overview.htm#:~:text=History%20of%20log4j%201%20Started%20in%20early%201996,by%20the%20open%20source%20initiative.%20More%20items...%20), licensed for anyone to use, and is typically used in open-source software. The vulnerability was first reported by the Alibaba Cloud Security Team and a fix was in the works when Minecraft gamers [found that certain code strings entered into a chat box](https://twitter.com/MalwareTechBlog/status/1469290238702874625?s=20) could trigger a remote code execution. While Microsoft [fixed Minecraft game servers](https://minecraftonline.com/wiki/Log4Shell), it was soon clear that the issue went beyond cloud servers. It could affect business applications, too. While there are a variety of [government resources available for larger firms](https://www.ncsc.gov.uk/blog-post/log4j-vulnerability-what-should-boards-be-asking), I’ve yet to see good advice for small businesses and individual users.

Here’s my advice for those wondering how they might be affected.

Most importantly, if you run Windows and use basic Microsoft Office software, you should be ok. Basic Microsoft products are not vulnerable. This is Apache-based software that isn’t natively installed on Windows — especially for home users. (And if you use any cloud-based apps that rely on Log4j2, vendors will be the ones updating and patching their offerings.)

The vulnerability could be lurking in many kinds of devices, including routers, firewalls, printers, or other Internet of Things hardware that’s *not* Windows based. It will be for you to determine whether you are vulnerable. You’ll need to think of how these devices connect to your internal network and whether they are exposed externally.

Many people don’t realize that such devices are exposed online until something bad happens. Printers, for example, are often set up to have internet-based printing enabled. While being able to e-print to any device from anywhere sounds wonderful, it also exposes such devices to manipulation. (If port 9100 is open to the Internet, attackers can print things to your printers.) So remember: anytime you have a  device that wants access “from anywhere,” stop and think about what that access might bring to your platform. If you use these features, ensure that you set up appropriate restrictions when choosing authentication or adding two-factor authentication.

For small businesses, the chance that you have vulnerable software inside your Windows network rises a bit if you have SQL server installed. If you or your vendors have installed a Java-based logging module, it could include the vulnerability. Your best bet here is to see whether you have a SQL instance installed on your servers and reach out to your vendors for guidance. If a consultant helps with your network, ask them for guidance. And if you are a consultant, reach out to colleagues and your management tool vendors to identify any software that needs to be patched.

For small firms with users under 300, one way to monitor and review whether you are at risk is to sign up for a preview of [Microsoft Defender for Business](https://techcommunity.microsoft.com/t5/small-and-medium-business-blog/introducing-microsoft-defender-for-business/ba-p/2898701). With this cloud-based console, you can review and monitor workstations that might be vulnerable. If you use something else to monitor and scan for viruses, reach out to the vendor to see if they are proactively searching for the flaw.

You’ll want to review the [listing of software](https://github.com/cisagov/log4j-affected-db) on the CISA site and see whether you have any of the software listed. In addition, an excellent recap of links to track down affected software is [available online](https://www.techsolvency.com/story-so-far/cve-2021-44228-log4j-log4shell/). (I was able to track down and confirm that my [Ricoh printers](https://www.ricoh.com/info/2021/1215_1/) were not vulnerable.)

Next, look at other devices that share the same internet connection as your network. If you’re unsure of their security, and they don’t need to share the same network as your business devices, set up a separate network for them. Make sure they are not on the same IP range as your business assets. Any IoT devices should be on their own network.

I do recommend you use [the focus on the Log4j2 security vulnerability](https://www.csoonline.com/article/3645348/how-to-properly-mitigate-the-log4j-vulnerabilities.html) to identify your own security information and resources for your devices. And know where to go for more information. One of the hardest things about this issue is finding the security bulletins released for each platform. Use this process to determine how to track down the resources you need to know what is and is not vulnerable, not only for Log4j2, but for future security issues. We may see more of these types of issues in the future. Be prepared for it.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=route]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Log4j2]] [[Microsoft]] [[Computerworld]]

