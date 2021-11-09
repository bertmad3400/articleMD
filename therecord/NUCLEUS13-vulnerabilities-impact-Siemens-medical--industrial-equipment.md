# NUCLEUS:13 vulnerabilities impact Siemens medical & industrial equipment
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/nucleus13-vulnerabilities-impact-siemens-medical-industrial-equipment/)
+ Date: November 9, 2021
+ Author: Catalin Cimpanu


## Article:
![NUCLEUS:13 vulnerabilities impact Siemens medical & industrial equipment](https://therecord.media/wp-content/uploads/2021/11/Nucleus-13.png)

Security researchers have disclosed today a set of 13 vulnerabilities that impact a crucial Siemens software library that is included with medical devices, automotive, and industrial systems.


Named **NUCLEAUS:13**, the vulnerabilities impact Nucleus NET, the TCP/IP stack included with Nucleus, a real-time operating system owned by Siemens, which typically runs on system-on-a-chip (SoC) boards included inside medical devices, cars, smartphones, Internet of Things devices, industrial PLCs, and many more.


Disclosed today in a [report](https://www.forescout.com/blog/new-critical-vulnerabilities-found-on-nucleus-tcp-ip-stack/) by Forescout and Medigate Labs, the NUCLEUS:13 vulnerabilities can be used to take over, crash, or leak information from devices that run older versions of the Nucleus RTOS.


The worst of these vulnerabilities and the easiest to weaponize is **CVE-2021-31886**, researchers said, a remote code execution (RCE) issue that received a rare 9.8 out of 10 rating, primarily due to its severity.


![Nucleus-13-list](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Nucleus-13-list-527x1024.png)
Forescout said it worked with Siemens and the US ICS-CERT team to have these issues properly reported and fixed before the release of its advisory earlier today.


ICS-CERT has published a [security advisory](https://us-cert.cisa.gov/ics/advisories/icsa-21-103-04) today to raise awareness for the NUCLEUS:13 vulnerabilities among US organizations, while Siemens has released security updates via its private CERT portal, to all of its customers. See PDF [here](https://cert-portal.siemens.com/productcert/pdf/ssa-044112.pdf).


Forescout researcher Stanislav Dashevskyi has also published a proof-of-concept demo showcasing how the NUCLEUS:13 vulnerabilities could be abused in practice to take over vulnerable devices. As Dashevskyi points out in the video, an attacker only needs to have some sort of network connection to a vulnerable device, as an attack only takes seconds to execute.





The NUCLEUS:13 vulnerabilities are the fifth and last part of a research project named Project Memoria, during which Forescout researchers analyzed popular TCP/IP stacks for security flaws.


In total, Project Memoria found 97 vulnerabilities affecting 14 TCP/IP stacks. The list includes:


* **[AMNESIA:33](https://www.forescout.com/research-labs/amnesia33/)**
* **[NUMBER:JACK](https://www.forescout.com/company/blog/numberjack-forescout-research-labs-finds-nine-isn-generation-vulnerabilities-affecting-tcpip-stacks/)**
* **[NAME:WRECK](https://forescout.com/research-labs/namewreck)**
* **[INFRA:HALT](https://www.forescout.com/research-labs/infra-halt/)**
* **[NUCLEUS:13](https://www.forescout.com/blog/new-critical-vulnerabilities-found-on-nucleus-tcp-ip-stack/)**






#### Tags:
[[Forescout]] [[NUCLEUS:13]] [[devices,]] [[TCP/IP]] [[The Record]]
