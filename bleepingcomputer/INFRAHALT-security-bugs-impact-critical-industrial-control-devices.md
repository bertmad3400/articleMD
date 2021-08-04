# INFRA:HALT security bugs impact critical industrial control devices
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/infra-halt-security-bugs-impact-critical-industrial-control-devices/)
+ Date: August 4, 2021
+ Author: Ionut Ilascu


## Article:
![INFRA:HAT vulnerability set affects the NicheStack TCP/IP stack](https://www.bleepstatic.com/content/hl-images/2021/08/04/INFRA_HALT.jpg)


High-severity and critical vulnerabilities collectively referred to as INFRA:HALT are affecting all versions of NicheStack below 4.3, a proprietary TCP/IP stack used by at least 200 industrial automation vendors, many in the leading segment of the market.


The stack is commonly found on real-time operating systems (RTOS) powering operational technology (OT) and industrial control system (ICS) devices to provide internet and network functionality.


### Remote code execution risk


INFRA:HALT is a set of 14 vulnerabilities jointly discovered by Forescout Research Labs and JFrog Security Research. It is part of Forescout's [Project Memoria](https://www.forescout.com/research-labs/project-memoria/) Research ([Amnesia:33](https://www.forescout.com/research-labs/amnesia33/), [NUMBER:JACK](https://www.forescout.com/blog/numberjack-forescout-research-labs-finds-nine-isn-generation-vulnerabilities-affecting-tcpip-stacks/), [NAME:WRECK](https://www.forescout.com/research-labs/namewreck/)) that focuses on the security of TCP/IP stacks.


The bugs range from remote code execution, denial of service (DoS), and information leak to TCP spoofing and DNS cache poisoning.


Most are high-severity security issues, but two of them - CVE-2020-25928 and CVE-2020-31226 - are deemed critical. Forescout researchers assessed their severity score at 9.8 and 9.1, respectively.


They impact the DNS client and the HTTP server components of the stack, allowing a remote attacker to execute code on the vulnerable device to take full control over it.


To trigger CVE-2020-25928, an attacker would need to send a crafted DNS packet as a response to a DNS query from the vulnerable device, Forescout and [JFrog researchers explain](https://jfrog.com/blog/infrahalt-14-new-security-vulnerabilities-found-in-nichestack/) in a joint [technical report](https://www.forescout.com/resources/infrahalt-discovering-mitigating-large-scale-ot-vulnerabilities/) published earlier today.


![exploiting CVE-2020-25928 for remote code execution](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/InfraHalt-25928.jpg)


Stanislav Dashevskyi, one of the Forescout researchers that investigated the INFRA:HALT collection of vulnerabilities, demonstrated CVE-2020-25928 in a video by attacking the programmable logical controller (PLC) managing an industrial fan.


Not long after initiating the attack, the PLC could no longer activate the fan and needed a restart to regain control over the fan.



The attack requires only four steps to crash the PLC:


1. Device 1, vulnerable to INFRA:HALT, sends a DNS request to the DNS server as part of its normal operations
2. The attacker sends a forged DNS response containing malicious shellcode to Device 1
3. When Device 1 attempts to parse the DNS response, its logic is hijacked and the attacker gets remote control over it. The device is instructed to establish a TCP connection with Device 2, the internal PLC connected to the HVAC, and to send a malicious FTP packet that exploits a 0-day in this PLC
4. The PLC crashes, forcing the fan control to stop working


Of the 14 INFRA:HALT vulnerabilities, ten have been rated with a high-severity score, two are low severity and two are critical:


![List of INFRA:HALT vulnerabilities](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/InfraHaltVulns.jpg)


 


### Plenty of vulnerable devices


NicheStack, also known as InterNiches, is maintained by HCC Embedded. The library is present in devices from around 200 vendors. An [old website](https://web.archive.org/web/20201022200519/http:/www.iniche.com:80/company/manylogos.php) version from the company lists big names among its customers: Emerson, Honeywell, Mitsubishi Electric, Rockwell Automation, Schneider Electric, and Siemens.


A search on Shodan on March 8 revealed that more than 6,400 devices running a vulnerable version of the stack. The number is likely lower today.


Looking at data collected from its appliances monitoring more than 13 million customer devices, Forescout found 2,500 systems from 21 vendors to be vulnerable to INFRA:HALT.


Almost half (46%) of these devices were deployed in industrial control systems in the Energy and Power sector. A quarter of them were in the VoIP industry and 18% were in the networking sector.


![Breakdown per industry of devices vulnerable to INFRA:HALT](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


### Mitigation options


HCC Embedded has addressed all INFRA:HALT vulnerabilities with [patches](https://www.hcc-embedded.com/support/security-advisories) that are available on request. Updating to version 4.3 of NicheStack is currently the only solution for complete protection against this set of security issues.


For the many cases where patching is not possible right away, Forescout and JFrog have prepared a [script that detects devices running NicheStack](https://github.com/Forescout/project-memoria-detector) and a set of mitigations that could prevent compromise:


* Confine and segment vulnerable devices from the rest of the network until they can be patched


**CVE-2020-25928, CVE-2020-25767, CVE-2020-25927, CVE-2021-31228, CVE-2020-25926 [DNSv4 client]:**


* Disable the DNSv4 client if not needed, or block DNSv4 traffic. Because there are several vulnerabilities that facilitate DNS spoofing attacks, using internal DNS servers may be not sufficient (attackers may be able to hijack the request-response matching)


**CVE-2021-31226, CVE-2021-31227 [HTTP server]:**


* Disable the HTTP server if not needed, or whitelist HTTP connections


**CVE-2021-31400, CVE-2021-31401, CVE-2020-35684 [TCP]**


* Monitor traffic for malformed IPv4/TCP packets and block them (having a vulnerable device behind a properly configured firewall should be sufficient


**CVE-2020-35685 [TCP]**


* Use the recommendations we outlined in Forescout’s [NUMBER:JACK report](https://www.forescout.com/company/blog/numberjack-forescout-research-labs-finds-nine-isn-generation-vulnerabilities-affecting-tcpip-stacks/), whenever it is feasible


**CVE-2020-35683 [ICMPv4]**


* Monitor traffic for malformed ICPMv4 packets and block them




#### Tags:
[[DNS]] [[Forescout]] [[INFRA:HALT]] [[PLC]] [[NicheStack]] [[JFrog]] [[HTTP]] [[Bleeping Computer]]
