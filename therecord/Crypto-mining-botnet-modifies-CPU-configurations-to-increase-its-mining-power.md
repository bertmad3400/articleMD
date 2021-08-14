# Crypto-mining botnet modifies CPU configurations to increase its mining power
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/crypto-mining-botnet-modifies-cpu-configurations-to-increase-its-mining-power/)
+ Date: August 12, 2021
+ Author: Catalin Cimpanu


## Article:
![Crypto-mining botnet modifies CPU configurations to increase its mining power](https://therecord.media/wp-content/uploads/2021/08/Intel-hardware.jpg)

A crypto-mining botnet is modifying CPU configurations on hacked Linux servers in order to increase the performance and output of its cryptocurrency mining code.


The attacks, detected by cloud security firm Uptycs, represent the first instances where a threat actor modifies a processor’s MSR to disable a CPU feature called hardware prefetcher.


Enabled by default on most CPUs, [hardware prefetching](https://www.techarp.com/bios-guide/cpu-hardware-prefetch/) allows a processor to load data in its cache memory based on the operations that are likely to be required in the near future.


When the CPU deals with repetitive computations, hardware prefetching can help improve performance.


[Model-specific registers (MSR](https://en.wikipedia.org/wiki/Model-specific_register)) are a set of control registers available on x86 CPUs that can be used to manage various features, including enabling and disabling hardware prefetching.


### Someone read the documentation


In a [report](https://www.uptycs.com/blog/cryptominer-elfs-using-msr-to-boost-mining-process) published last week, Uptycs researchers said they spotted a crypto-mining botnet in June 2021 that was breaching Linux servers, downloading the Linux MSR driver, and then disabling hardware prefetching before installing a version of XMRig, a common app used for cryptocurrency mining by both legitimate users and malware gangs.


Uptycs believes the attacker got the idea to disable hardware prefetching after reading the [XMRig documentation](https://github.com/xmrig/xmrig/blob/master/doc/CPU.md#wrmsr), where it is claimed that XMRig can gain a 15% speed boost if the feature is disabled.


Right now, the attacks are limited to Linux servers, Uptycs said.


Per the company’s report, the botnet has been seen using exploits for [CVE-2020-14882](https://nvd.nist.gov/vuln/detail/CVE-2020-14882) and [CVE-2017-11610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-11610) to gain access to Linux systems running [Oracle WebLogic](https://www.oracle.com/middleware/technologies/weblogic.html) or [Supervisord](http://supervisord.org/) before disabling hardware prefetching and installing XMRig.


Prior to the attacks spotted this summer, Uptycs said the same botnet had been active [since at least December 2020](https://www.intezer.com/blog/research/new-golang-worm-drops-xmrig-miner-on-servers/) and had previously targeted servers running MySQL, Tomcat, Oracle WebLogic, and Jenkins, suggesting that the botnet could easily switch targets and target other web-based technologies if it needed to.





#### Tags:
[[botnet]] [[Linux]] [[prefetching]] [[Uptycs]] [[The Record]]
