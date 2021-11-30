# AT&T takes action against DDoS botnet that hijacked VoIP servers
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/att-takes-action-against-ddos-botnet-that-hijacked-voip-servers/)
+ Date: November 30, 2021
+ Author: Catalin Cimpanu


## Article:
![AT&T takes action against DDoS botnet that hijacked VoIP servers](https://therecord.media/wp-content/uploads/2021/11/cell-tower-mobile.png)

AT&T said it’s investigating and has “taken steps to mitigate” a botnet that infected more than 5,700 VoIP servers located inside its network, a spokesperson has told *The Record* earlier today.


All the infected devices were [EdgeMarc Enterprise Session Border Controllers](https://ribboncommunications.com/products/service-provider-products/cloud-and-edge/session-border-controllers/session-border-controllers-edge-appliances), a type of Voice-over-IP server designed to balance and reroute internet telephony traffic from smaller enterprise customers to upstream mobile providers.


According to Netlab, a network security division of Chinese tech giant Qihoo 360, a threat actor used an old exploit ([CVE-2017-6079](https://depthsecurity.com/blog/cve-2017-6079-blind-command-injection-in-edgewater-edgemarc-devices)) to hack into unpatched EdgeMarc servers and install a modular malware strain named EwDoor.



> “[W]e confirmed that the attacked devices were EdgeMarc Enterprise Session Border Controller, belonging to the telecom company AT&T, and that all 5.7k active victims that we saw […] were all geographically located in the US.”
> 
> [Netlab EwDoor report](https://blog.netlab.360.com/warning-ewdoor-botnet-is-attacking-att-customers/)


### AT&T says it saw no evidence of data theft


The Chinese security firm said it’s been tracking the EwDoor botnet and its attacks since late October 2021, during which time the malware went through at least three versions.


An analysis of the malware revealed extensive backdoor and DDoS capabilities, which Netlab researchers suggested could be used to access devices to gather and steal sensitive information, such as VoIP call logs.


But AT&T says it has not seen any evidence to sustain Netlab’s assessment.


“We have no evidence that customer data was accessed,” the company said in an email earlier today.


![EwDoor](https://www-therecord.recfut.com/wp-content/uploads/2021/11/EwDoor.png)Image: Netlab
Netlab said that the 5,700 estimate it provided today was gathered following a brief window of visibility into the botnet’s operations on November 8.


Internet-wide scans suggest that more than 100,000 devices are using the same SSL certificate used on EdgeMarc VoIP servers, but it’s unclear how many of these are vulnerable to CVE-2017-6079 and exposed to attacks.





#### Tags:
[[EdgeMarc]] [[AT&T]] [[it’s]] [[VoIP]] [[malware]] [[Netlab]] [[The Record]]
