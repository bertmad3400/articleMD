# LightBasin hacking group breaches 13 global telecoms in two years
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/lightbasin-hacking-group-breaches-13-global-telecoms-in-two-years/)
+ Date: October 19, 2021
+ Author: Ionut Ilascu


## Article:
![LightBasin hacking group breaches 13 global telecoms in two years](https://www.bleepstatic.com/content/hl-images/2021/04/16/computer-hacker.jpg)


A group of hackers that security researchers call LightBasin has been compromising mobile telecommunication systems across the world for the past five years.


Since 2019, the group hacked into more than a dozen telecommunication companies and maintained persistence through custom malware, to steal data that would serve intelligence organizations.


### Hopping through GPRS networks


LightBasin is active since at least 2016 and targets Linux and Solaris servers in particular, although it did interact with Windows systems where needed, in their mission to steal subscriber information and call metadata.


In a report today, CrowdStrike cybersecurity company says that the threat actor is a sophisticated group with strong operational security (OPSEC) strategy.


The researchers pieced together LightBasin activity starting from an incident they investigated at one telecommunications company. They learned that the adversary would hop from one compromised network to another via an SSH connection and “previously established implants.”


Among the telecommunications systems that LightBasin targeted are External DNS (eDNS) servers, Service Delivery Platform (SDP) systems, and SIM/IMEI provisioning, all of which are part of the General Packet Radio Service (GPRS) network that enables roaming between mobile operators.


During their investigation, CrowdStrike found that the threat actor first accessed an eDNS server through an SSH connection from the network of another compromised company.


The researchers found evidence of LightBasin brute-forcing their way on the system by trying the default credentials for the targeted system.


Following a successful compromise, the threat actor installed and executed custom malware that is currently tracked as SLAPSTICK - a backdoor for the Solaris Pluggable Authentication Module (PAM) that gives access to the system based on a hardcoded password.


With backdoor access to the target Solaris system, LightBasin could steal passwords to pivot to other systems and establish persistence through the same method.


At a later time, the hackers accessed multiple eDNS servers from a compromised telco through an implant that CrowdStrike named PingPong.


PingPong would receive commands through an ICMP request to set a TCP reverse shell to an IP address and port specified in the packet.



“eDNS servers are usually protected from general external internet access by firewalls; the magic packet PingPong listens for would most likely have to be sent from other compromised GPRS network infrastructure” - [CrowdStrike](https://www.crowdstrike.com/blog/an-analysis-of-lightbasin-telecommunications-attacks/)



The researchers say that they noticed reverse shells created by the PingPong implant that talked via the TCP port 53 (default for DNS) to servers from other telecommunication companies in other parts of the world.


To maintain a low profile, LightBasin also added iptables rules to the eDNS server that allowed SSH communication from five compromised companies.


Additionally, the actor used a trojanized version of the iptables utility that removed output containing the first two octets from IP addresses belonging to other hacked companies, making it more difficult for admins to find the modified rules.


### Novel technique to move data between networks


CrowdStrikes notes that LightBasin relies on a novel technique to move traffic via the telecommunications network, which involved specific software emulation and the use of TinyShell, a common open-source Unix backdoor.


The actor created a bash script that combined the TinyShell backdoor and publicly available software (sgsnemu2) that emulates GPRS network access points - the so-called Serving GPRS Support Nodes (SGSNs) - to move traffic between networks via specific mobile stations.


Although the script ran on the system at all times, it only executed specific steps during a half-hour window every day, similar to a scheduled task.


The role of the SGSN emulator was to establish an alternate communication route if TinyShell failed to connect to the command and control (C2) IP address via a route added on the interface tun0.


CrowdStrike explains:



“ If connectivity to the IP address fails, the script executes the SGSN emulator in a loop, attempting to connect to a set of nine pairs of International Mobile Subscriber Identity (IMSI) and Mobile Subscriber Integrated Services Digital Network (MSISDN) numbers that are used as arguments to the SGSN emulator; these numbers identify specific mobile devices, or mobile stations, for the SGSN emulator to create tunnels to. This process generates Packet Data Protocol (PDP) context requests for mobile stations with the IMSI/MSISDN number pairs until a connection is established. If a connection is established, the SGSN emulator creates a connection to the device via the GPRS Tunnelling Protocol (GTP), and utilizes the interface tun0 for the connection.”



Once this step completes successfully, TinyShell can use the tun0 interface to talk to the actor’s C2 server. If no successful connection occurs at the end of the 30-minute window, the bash script kills both the SGSN emulator and the TinyShell implant.


In its report today, CrowdStrike also lists a set of utilities and malware that LightBasin uses in their operations:


* CordScan - network scanning and packet capture utility that can fingerprint and fetch information specific to telecommunication protocols
* SIGTRANslator - an ELF binary that can send and receive data via telecommunication-specific protocols (SIGTRAN)
* Fast Reverse Proxy - open-source reverse proxy tool
* Microsocks Proxy - open-source lightweight SOCKS5 proxy server
* ProxyChains - open-source tool that links proxies together and forces network traffic through the chain


LightBasin is also known as UNC1945 and has been [profiled](https://www.mandiant.com/resources/live-off-the-land-an-overview-of-unc1945) by cybersecurity company Mandiant in November 2020 as an actor that compromised managed service providers (MSP) to reach targets in the financial and professional consulting industries.


Mandiant notes that the adversary targeted Oracle Solaris systems and relied in its activity on vulnerability exploits, tools, and malware for multiple operating systems.


The researchers said that UNC1945 showed “a disciplined interest in covering or manipulating their activity, and displayed advanced technical abilities during interactive operations.”


While there is no attribution from neither Mandiant nor CrowdStrike, the latter found a clue suggesting that the developer of SIGTRANslator has some knowledge of the Chinese language.




#### Tags:
[[LightBasin]] [[CrowdStrike]] [[SGSN]] [[GPRS]] [[Solaris]] [[IP]] [[open-source]] [[TinyShell]] [[SSH]] [[eDNS]] [[Bleeping Computer]]
