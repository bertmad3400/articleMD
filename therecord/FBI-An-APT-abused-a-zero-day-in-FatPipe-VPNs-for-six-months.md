# FBI: An APT abused a zero-day in FatPipe VPNs for six months
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/fbi-an-apt-abused-a-zero-day-in-fatpipe-vpns-for-six-months/)
+ Date: November 17, 2021
+ Author: Catalin Cimpanu


## Article:
![FBI: An APT abused a zero-day in FatPipe VPNs for six months](https://therecord.media/wp-content/uploads/2021/09/server-data-center-router.jpg)

The US Federal Bureau of Investigation said it discovered an advanced persistent threat (APT) abusing a zero-day vulnerability in FatPipe networking devices as a way to breach companies and gain access to their internal networks.


“As of November 2021, FBI forensic analysis indicated exploitation of a 0-day vulnerability in the FatPipe MPVPN device software **going back to at least May 2021**,” the agency said in a flash security alert sent out on Tuesday.


The FBI said the vulnerability allowed the hacking group to exploit a file upload function in the device’s firmware and install a webshell with root access.


The FBI said it spotted the hackers abusing the zero-day only against [FatPipe MPVPN devices](https://www.fatpipeinc.com/products/mpvpn/index.php), but the vulnerability also impacted other products, such as [IPVPN](https://www.fatpipeinc.com/products/ipvpn/index.php) and [WARP](https://www.fatpipeinc.com/products/warp/index.php).


All are different types of virtual private network (VPN) servers that companies install at the perimeter of their corporate networks and use to allow employees remote access to internal applications via the internet, acting as mash-up between network gateways and firewalls.


### Patch released yesterday, November 16


The FBI said the zero-day it discovered during its investigation does not currently have its own CVE identifier, but FatPipe has released a patch and additional information via an internal security advisory tracked as FPSA006.


To help IT and security teams check if their FatPipe systems have been hacked and detect the intruder’s webshells, the FBI has also published several indicators of compromise (IOCs) and YARA signatures as part of its alert [[PDF](https://www.ic3.gov/Media/News/2021/211117-2.pdf)].


FatPipe now joins a long list of networking equipment makers that have had their systems abused for cyber intrusions. The list includes the likes of Cisco, Microsoft, Oracle, F5 Networks, Palo Alto Networks, Fortinet, and Citrix, just to name the bigger ones.


Attacks targeting networking devices such as firewalls, VPN servers, network gateways, and load balancers had ramped up during the ongoing COVID-19 pandemic when threat actors realized that these devices are installed almost all large corporate and government networks — as a way to let remote workers connect to internal applications.





#### Tags:
[[FatPipe]] [[zero-day]] [[The Record]]
