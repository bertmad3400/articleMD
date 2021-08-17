# New HolesWarm botnet targets Windows and Linux servers
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/new-holeswarm-botnet-targets-windows-and-linux-servers/)
+ Date: August 16, 2021
+ Author: Catalin Cimpanu


## Article:
![New HolesWarm botnet targets Windows and Linux servers](https://therecord.media/wp-content/uploads/2021/08/HolesWarm-botnet.png)

A new botnet named HolesWarm has been slowly growing in the shadows since June this year, exploiting more than 20 known vulnerabilities to break into Windows and Linux servers and then deploy cryptocurrency-mining malware.


While attacks have primarily been spotted across China, with reports from security firm [Tencent](https://s.tencent.com/research/report/78) and [various](http://apple-dina.com/view/108) [IT](https://zhuanlan.zhihu.com/p/389104715) [bloggers](https://blog.csdn.net/MRQ1734/article/details/118380267), the botnet is expected to expand its reach, and target systems across the globe as its infrastructure and attack capabilities expand in the coming months.


Primarily operated from a command and control server located at [m[.]windowsupdatesupport[.]org](https://otx.alienvault.com/indicator/hostname/m.windowsupdatesupport.org), the botnet has been seen exploiting vulnerabilities in software such as:


* Docker
* Jenkins
* Apache Tomcat
* Apache Struts (multiple bugs)
* Apache Shiro
* Apache Hadoop Yarn
* Oracle WebLogic (CVE-2020-14882)
* Spring Boot
* Zhiyuan OA (multiple bugs)
* UFIDA
* Panwei OA
* Yonyou GRP-U8


While the entry vectors may vary per victim, Tencent Security says that once the malware gets a foothold on an infected system, HolesWarm dumps local passwords, expands to the local network, and then deploys an XMRig-based cryptocurrency mining tool.


While other botnet operators try to hide their presence on infected systems by tethering the crypto-mining process, HolesWarm doesn’t appear to employ this safety mechanism, and per several reports, the botnet often maxs out server CPUs, leading to its discovery.


![HolesWarm-CPU-maxed-out](https://www-therecord.recfut.com/wp-content/uploads/2021/08/HolesWarm-CPU-maxed-out.jpg)Image: enp4s0
Right now, the botnet is just the latest in a long line of crypto-mining botnets that are popping up online on a regular basis. Nothing in its make-up screams technical sophistication, and the HolesWarm operators are just the latest malware coders taking advantage of the large number of servers running out-of-date software.


IOCs are available in the reports linked above, and in the Twitter thread below, from security firm Intezer Labs, which also saw some of the botnet’s earlier attacks.








#### Tags:
[[botnet]] [[HolesWarm]] [[The Record]]
