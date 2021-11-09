# Multiple BusyBox Security Bugs Threaten Embedded Linux Devices
### Researchers discovered 14 vulnerabilities in the ‘Swiss Army Knife’ of the embedded OS used in many OT and IoT environments. They allow RCE, denial of service and data leaks.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176098)
+ Date: November 9, 2021  9:00 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/01164740/Linux-OS.jpg)
Researchers have discovered 14 critical vulnerabilities in a popular program used in embedded Linux applications, all of which allow for denial of service (DoS) and 10 that also enable remote code execution (RCE), they said.


One of the flaws also could allow devices to leak info, according to researchers from JFrog Security and Claroty Research, in a report shared with Threatpost [on Tuesday](https://jfrog.com/blog/unboxing-busybox-14-new-vulnerabilities-uncovered-by-claroty-and-jfrog/).


The two firms teamed up to take a deeper dive into BusyBox, a software suite used by many of the world’s leading operational technology (OT) and internet of things (IoT) devices—such as programmable logic controllers (PLCs), human-machine interfaces (HMIs) and remote terminal units (RTUs). Shachar Menashe, senior director security research for JFrog, partnered with Vera Mens, Uri Katz, Tal Keren and Sharon Brizinov of Claroty Research on the report.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Touted as a “Swiss Army Knife” of [embedded Linux](https://threatpost.com/botnet-powered-by-25000-cctv-devices-uncovered/118948/), BusyBox is comprised of useful Unix utilities called applets that are packaged as a single executable. The program includes a full-fledged shell, a DHCP client/server, and small utilities such as cp, ls, grep and others.


The discovery of the flaws are significant because of the proliferation of BusyBox not just for the embedded Linux world, but also for numerous Linux applications outside of devices, Menashe said in an email to Threatpost.


“These new vulnerabilities that we’ve disclosed only manifest in specific cases, but could be extremely problematic when exploitable,” he said. However, the good news for the security of devices using BusyBox is that generally the vulnerabilities require a bit of effort to exploit, researchers reported.


**Breakdown of Flaws**
----------------------


The vulnerabilities are being tracked with CVE IDs from CVE-2021-42373 through CVE-2021-42386, and affect different versions of BusyBox ranging from 1.16-1.33.1, depending on the flaw. They also affect a variety of applets, including one each separately affecting “man,” “lzma/unizma” and “ash”; two separate flaws affecting “hush”; and nine separate flaws affecting “awk,” the applet with the most vulnerabilities.


Because the applets are not daemons, each flaw can only be exploited if the vulnerable applet is fed with untrusted data, typically through a command-line argument, researchers wrote. The team published a comprehensive breakdown of each vulnerability, which applet it affects, and its potential for exploitation in its report.


Overall, 40 percent of the firmware using BusyBox that researchers inspected include a BusyBox executable file linked with one of the affected applets, making the problem  “extremely widespread among Linux-based embedded firmware,” they wrote. However, the vulnerabilities don’t currently pose a critical threat to affected devices for a number of reasons, researchers noted in the analysis, including the aforementioned exploit complexity.


**Complex to Exploit**
----------------------


For example, potentially the most dangerous of the flaws is CVE-2021-42374, an out-of-bounds heap read in unlzma that can lead to both DoS and an information leak. However, as researchers explained in detail, it can only be used to attack to the device when a crafted lzma-compressed input is decompressed.


Lzma is a compression algorithm that uses dictionary compression, and encodes its output using a range encoder, researchers explain. Two specific coding conditions need to be met to exploit the flaw: “buffer\_pos = 0” and “rep0 = offset + dict\_size,” researchers wrote.


To meet these conditions, an attacker needs to prepare a specifically crafted lzma encoded stream that, when decoded, will fulfill these conditions and ultimately leak device memory, they said.


While the DoS vulnerabilities are more trivial to exploit, their impact is usually mitigated by the fact that applets almost always run as a separate forked process, researchers added.


Finally, most of the RCE flaws—particularly those present in the “awk” applet — are also tricky to exploit because “it is quite rare (and inherently unsafe) to process an awk pattern from external input,” they wrote.


Still, Menashe recommended that devices using BusyBox be upgraded to the latest version and that developers ensure that none of affected applets are being used, in order to avoid threat actors taking advantage of any of the vulnerabilities.


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost on Tues., Nov. 16 at 2 p.m. ET for “[An Intro to OSquery and CloudQuery](https://bit.ly/3wf2vTP),” a LIVE, interactive conversation with Eric Kaiser, Uptycs’ senior security engineer, about how this open-source tool can help tame security across your organization’s entire campus.***


***[Register NOW](https://bit.ly/3wf2vTP) for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at [becky.bracken@threatpost.com](mailto:becky.bracken@threatpost.com).***


 


 


 




#### Tags:
[[BusyBox]] [[applets]] [[applet]] [[wrote.]] [[Linux]] [[said.]] [[However,]] [[ThreatPost]]
