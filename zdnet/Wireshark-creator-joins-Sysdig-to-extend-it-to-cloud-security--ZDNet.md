# Wireshark creator joins Sysdig to extend it to cloud security | ZDNet
### Wireshark, the pro's pro network traffic analysis tool, will soon be extended to cover cloud computing security.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/wireshark-creator-joins-sysdig-to-extend-it-to-cloud-security/
+ Date: 2022-01-13 17:20:21
+ Author: Steven Vaughan-Nichols


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/eeec58ff97c52e9bb4364769de319bb4af3d8c9e/2022/01/13/cfe0e377-c34a-486e-acf0-e8a6ba294773/wireshark.jpg?width=770&height=578&fit=crop&auto=webp)

If you're a real network administrator, you know and love open source [Wireshark](https://www.wireshark.org/). For over 15-years, it's been the tool that professionals use for network traffic protocol analysis. Nothing else even comes close. Now, [Sysdig,](https://sysdig.com/) the container and cloud security company, has hired Gerald Combs, its creator and project leader, to join its open source team. There, Combs will help them with Sysdig-related open-source projects such as  [Falco](https://falco.org/), [Prometheus](https://prometheus.io/), [eBPF](https://ebpf.io/), and [Sysdig Inspect](https://github.com/draios/sysdig-inspect). In addition, Sysdig will sponsor and manage the Wireshark community and extend Wireshark to monitoring and analyzing cloud networks. 


Wireshark is an open source GUI network package capturing tool for those who don't know Wireshark yet. With it, you can monitor network traffic, learn protocols and packet basics, and troubleshoot network problems. For network admins, Wireshark is the de facto standard for checking the health and security of networks at a microscopic level. If you want to know more about how to use Wireshark, I highly recommend Chris Sander's [Practical Packet Analysis: Using Wireshark to Solve Real-World Network Problems](https://assoc-redirect.amazon.com/g/r/https://www.amazon.com/Practical-Packet-Analysis-Wireshark-Real-World/dp/1593278020?tag=zd-buy-button-20&ascsubtag=__COM_CLICK_ID__%7C__VIEW_GUID__%7Cdtp) 
 
 .

Besides being the open-source tool for real-time network packet capture and analysis, you can also save its findings for later viewing and analysis. Armed with this information, you can filter through that traffic to find evidence from day-to-day network problems and attacks from hackers. Wireshark can be used on almost any platform, including Windows, Linux, and macOS.

Wireshark is already the world's foremost and widely-used traffic protocol analyzer, even without a company behind it. More than 60 million downloads have been downloaded in the last 5 years.

A big reason Combs is joining Sysdig is that Loris Degioanni, Sysdig's CTO and Founder, partnered with him to launch Wireshark. 

While studying network analyzers and working on his Ph.D. in Italy, Loris was invited to the United States to do research, which is where he met Gerald. Gerald joined Loris at CACE Technologies in the early 2000s, where they collaborated and grew Wireshark. CACE Technologies was later acquired, and since that time, Gerald has focused on growing the tool and ensuring Wireshark and its community have the resources needed to thrive.

Degioanni added, "Gerald and I have been friends for a long time, starting when Wireshark was called Ethereal. At that time, a capture library that I developed while I was a university student in Italy, WinPcap, was used to port Ethereal to Windows. That was my first contribution to the project. Since the beginning, my work at Sysdig has been heavily inspired by the "packet capture stack" that Gerald and I helped define: Wireshark, [tcpdump, libpcap](https://www.tcpdump.org/), [BPF](https://www.kernel.org/doc/html/latest/bpf/index.html). One of the reasons why Sysdig's instrumentation is universally considered the most accurate, rich, and scalable is that we built it on top of the ideas behind that stack, adapting them to the modern world of cloud and containers. Countless times, during Sysdig's early days, we were inspired by Gerald's work."






"I am excited to be reunited with Loris and explore the opportunity we have to expand Wireshark to the cloud," said Combs, now Sysdig's Director of Open Source Projects. "My move to Sysdig and the subsequent move for Wireshark will give Wireshark the corporate sponsor it needs to continue moving forward. This is a significant milestone for Wireshark, and with Sysdig's backing, we will have the assistance we need to continue to evolve use cases for Wireshark."

"It's amazing to see the lasting heritage of Wireshark, led by Gerald. I can guarantee most of the fortune 2000 companies are actively using Wireshark," said Degioanni. "I am excited to be reunited with Gerald and to advance the project in the same way Sysdig supports Falco and the Sysdig open source project. This move ensures Wireshark will continue to innovate. Our goal at Sysdig is to empower Wireshark."

Looking ahead, Sysdig will back the Wireshark community, including supporting Gerald as its leader. Together they'll make sure Wireshark has the resources it needs to operate and sponsor [SharkFest](https://sharkfestus.wireshark.org/), its international developer conference. Sysdig's open-source team will also contribute to the Wireshark project. Reunited, working together again, Gerald and Loris will investigate new innovative ways to address challenges with securing the cloud. 

Degioanni added, Wireshark "opens up a universe of possibilities. Wireshark is an incredibly important tool. Its UI is part of the muscle memory of every software professional. Its feature set has saved our butts countless times. At the same time, the world is changing quickly. Software today runs in the cloud, orchestrated by Kubernetes. With the help of Gerald, Sysdig wants to invest in making Wireshark even more useful in modern cloud environments. We'll work on expanding its feature set and make sure it remains the cornerstone of troubleshooting and security investigation, even when software is containerized and runs in the cloud."

Finally, another reason for this move is they both want to make sure Wireshark remains a healthy open-source project. The [Log4j](https://thenewstack.io/log4shell-we-are-in-so-much-trouble/) and [OpenSSL](https://www.zdnet.com/article/sloppy-programming-leads-to-openssl-woes/) vulnerabilities have shown that large and small organizations are relying on open-source projects and major trouble comes when critical vulnerabilities are found in these tools. Maintaining the project's health is of the utmost importance considering Wireshark's widespread adoption.

I'm looking forward to seeing what the two friends can do together. I've been a Wireshark user for over a decade. The idea that I'll soon be able to use it in cloud-native environments is an exciting one. Just as it's made network troubleshooting very easy, I can see that it 

**Related stories:**

* [Best online master's in network security 2021: Top picks](https://www.zdnet.com/education/computers-tech/best-online-masters-network-security/).
* [Cybersecurity: Last year was a record year for attacks, and Log4j made it worse](https://www.zdnet.com/article/report-increased-log4j-exploit-attempts-leads-to-all-time-peak-in-weekly-cyberattacks-per-org/).
* [Check your SPF records: Wide IP ranges undo email security and make for tasty phishes](https://www.zdnet.com/article/check-your-spf-records-wide-ip-ranges-undo-email-security-and-make-for-tasty-phishes/).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=Bern]] [[victim.country.name=Switzerland]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Wireshark]] [[Sysdig]] [[Cloud]] [[Open-source]] [[Degioanni]] [[ZDNet]]

