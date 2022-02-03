# UEFI firmware vulnerabilities affecting Fujitsu, Intel and more discovered | ZDNet
### 23 high-impact vulnerabilities were discovered by security company Binarly.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/firmware-vulnerabilities-affecting-fujitsu-intel-and-more-discovered/
+ Date: 2022-02-03 02:31:00
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/29de1f4fbcdedea2133bc822d503e01216b8db8a/2020/05/13/5d58fd08-54ac-461b-a79f-a5904a0b672b/vulnerability-code-binary.png?width=770&height=578&fit=crop&auto=webp)

Researchers have [discovered](https://www.binarly.io/posts/An_In_Depth_Look_at_the_23_High_Impact_Vulnerabilities/index.html) 23 "high-impact vulnerabilities" affecting any vendors that adopted Independent BIOS Developers (IBV) code into their Unified Extensible Firmware Interface (UEFI) firmware.

Binarly explained the vulnerabilities in a blog post this week, confirming that "all these vulnerabilities are found in several of the major enterprise vendor ecosystems" including Fujitsu, Siemens, Dell, HP, HPE, Lenovo, Microsoft, Intel and Bull Atos. CERT/CC [confirmed](https://kb.cert.org/vuls/id/796611) that Fujitsu, Insyde and Intel were affected but left the others tagged as "unknown," urging anyone affected to update to the latest stable version of firmware.

According to the blog, the majority of the vulnerabilities disclosed lead to code execution with SMM privileges and had severity ratings of between 7.5 - 8.2. 

"The root cause of the problem was found in the reference code associated with InsydeH2O firmware framework code. All of the aforementioned vendors were using Insyde-based firmware SDK to develop their pieces of firmware," Binarly wrote. 

"We had a short discussion with Fujitsu PSIRT and came to the conclusion that we should report all those issues to [CERT/CC](https://www.kb.cert.org/) to lead an industry-wide disclosure. This is how the VU#796611 was created and how Binarly collaboration with CERT/CC began in September 2021."

They commended Fujitsu, Intel and others for responding quickly and solving the vulnerabilities. UEFI provider Insyde Software [said](https://www.insyde.com/press_news/press-releases/insyde%C2%AE-software-credits-binarly%E2%80%99s-ai-powered-firmware-threat-detection) it worked with Binarly to resolve the vulnerabilities and has [released firmware updates](https://www.insyde.com/security-pledge) for all the issues listed. 

"We are extremely thankful for Binarly's work in discovering the items outlined in today's published security disclosures," said Tim Lewis, CTO at Insyde Software on Tuesday.






"We appreciated Insyde Software's prompt and professional response to the results of our analysis on their firmware," said Alex Matrosov, Founder and CEO of Binarly. 

The vulnerabilities are tracked as CVE-2020-27339, CVE-2020-5953, CVE-2021-33625, CVE-2021-33626, CVE-2021-33627, CVE-2021-41837, CVE-2021-41838, CVE-2021-41839, CVE-2021-41840, CVE-2021-41841, CVE-2021-42059, CVE-2021-42060, CVE-2021-42113, CVE-2021-42554, CVE-2021-43323, CVE-2021-43522, CVE-2021-43615, CVE-2021-45969, CVE-2021-45970, CVE-2021-45971, CVE-2022-24030, CVE-2022-24031, CVE-2022-24069.

"A local attacker with administrative privileges (in some cases a remote attacker with administrative privileges) can use malicious software to perform any of the following: Invalidate many hardware security features (SecureBoot, Intel BootGuard), Iinstall persistent software that cannot be easily erased and create backdoors and back communications channels to exfiltrate sensitive data," CERT/CC explained. 

Mike Parkin, engineer at Vulcan Cyber, said any vulnerabilities that let an attacker manipulate or alter a system's BIOS can have potentially devastating consequences. 

"Fortunately, the attack described here requires privileged access to execute. This isn't uncommon with BIOS attacks in that they require some level of privilege or physical access to implement. But that doesn't mean we can ignore them. For a threat actor, the value of embedding malicious code in the BIOS makes the effort worthwhile," Parkin said. 

"The issue will be identifying all the systems that are affected by these vulnerabilities and rolling out the updates once they are available from the vendor. System BIOS updates are often more involved and time consuming than a simple system patch, which makes finding and fixing them all somewhat challenging."

Viakoo CEO Bud Broomhead noted that the issue was similar to recent open source vulnerabilities like Log4j, PwnKit and others because vulnerabilities that exist within the UEFI layer from Insyde are difficult to quickly patch at scale due to the multitude of manufacturers that will each need to produce and distribute a patch to the end user. 

It's then up to the end user how quickly the patch is installed, Broomhead said. Unless patched, these vulnerabilities provide a direct path for threat actors to deploy malware within the OS layer, or even brick the devices, he added. 

"This disclosure reinforces the need to ensure that all assets can be quickly located through an automated discovery and threat assessment solution, followed by an automated method to patch or upgrade the system firmware. The need to quickly patch multiple forms of devices (IT, IoT, OT, ICS, etc) is now way beyond any organization's ability to manually implement security fixes," Broomhead said. 

"Organizations will be dealing with this for a while; because multiple system manufacturers using Insyde UEFI are impacted by this there are likely many devices in the supply chain that will be delivered over the next few months to end users. Organizations will need to revisit how they are provisioning and onboarding new devices to ensure they are not continuing to distribute devices that can be easily exploited by cyber criminals."





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Insyde]] [[Binarly]] [[Fujitsu]] [[Cert/cc]] [[Uefi]] [[Broomhead]] [[ZDNet]]
#### CVE's
[[CVE-2020-27339]] [[CVE-2020-5953]] [[CVE-2021-33625]] [[CVE-2021-33626]] [[CVE-2021-33627]] [[CVE-2021-41837]] [[CVE-2021-41838]] [[CVE-2021-41839]] [[CVE-2021-41840]] [[CVE-2021-41841]] [[CVE-2021-42059]] [[CVE-2021-42060]] [[CVE-2021-42113]] [[CVE-2021-42554]] [[CVE-2021-43323]] [[CVE-2021-43522]] [[CVE-2021-43615]] [[CVE-2021-45969]] [[CVE-2021-45970]] [[CVE-2021-45971]] [[CVE-2022-24030]] [[CVE-2022-24031]] [[CVE-2022-24069]]

