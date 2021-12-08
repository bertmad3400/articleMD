# AWS, Other Cloud Services Affected by Flaws in Eltima SDK
### Researchers have found a number of high-security vulnerabilities in third-party driver software – bugs that originated in a library created by network virtualization firm Eltima – that leave about a dozen cloud services used by millions of users worldwide open to privilege-escalation attacks.  That includes Amazon WorkSpaces, Accops and NoMachine, among others: all apps that

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176852
+ Date: 2021-12-08T18:54:12+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/08133732/cloud-security-e1638988664504.jpeg)

Researchers have found a number of high-security vulnerabilities in third-party driver software – bugs that originated in a library created by network virtualization firm Eltima – that leave about a dozen cloud services used by millions of users worldwide open to privilege-escalation attacks.


That includes Amazon WorkSpaces, Accops and NoMachine, among others: all apps that enable remote desktop access by using the Eltima SDK (software development kit) to enable the company’s “[USB Over Ethernet](https://www.eltima.com/products/usb-over-ethernet/)” product. USB Over Ethernet enables sharing of multiple USB devices over Ethernet, allowing users to connect to devices such as webcams on remote machines anywhere in the world as if the devices were physically plugged into their own computers.


The flaws are in the USB Over Ethernet function of the Eltima SDK, not in the cloud services themselves. Because of code-sharing between the server side and the end user apps, they affect both clients – such as laptops and desktops running Amazon WorkSpaces software – and cloud-based machine instances that rely on services such as Amazon Nimble Studio AMI that run in Amazon Cloud.


The flaws allow attackers to escalate privileges so that they can launch a slew of malicious actions, including to kick the knees off the very security products that users depend on for protection. Specifically, the vulnerabilities can be used to “disable security products, overwrite system components, corrupt the operating system, or perform malicious operations unimpeded,” SentinelOne Senior Security Researcher Kasif Dekel said in a [report](https://www.sentinelone.com/labs/usb-over-ethernet-multiple-privilege-escalation-vulnerabilities-in-aws-and-other-major-cloud-services/) published on Tuesday.



> **We want to know what your biggest cloud security concerns and challenges are, and how your company is dealing with them. Weigh in with our exclusive, anonymous [Threatpost Poll](https://threatpost.com/cloud-security-challenges-poll/176702/)!**
> 
> 


SentinelOne traced the vulnerabilities to two drivers that are responsible for USB redirection – “wspvuhub.sys” and “wspusbfilter.sys” – that could lead to a buffer overflow that allows an attacker to jack up privileges so as to execute arbitrary code in the kernel.


“An attacker with access to an organization’s network may also gain access to execute code on unpatched systems and use this vulnerability to gain local elevation of privilege,” SentinelOne noted. “Attackers can then leverage other techniques to pivot to the broader network, like lateral movement.”


Not Yet Seen in the Wild
------------------------


The cybersecurity firm hasn’t detected in-the-wild use of the vulnerabilities, of which there are dozens.


The firm reported the flaws last quarter, and they’ve since been fixed by the vendors. The full list of affected products includes Amazon Nimble Studio AMI, Amazon NICE DCV, Amazon WorkSpaces, Amazon AppStream, NoMachine, Accops HyWorks, Accops HyWorks DVM Tools, Eltima USB Network Gate, Amzetta zPortal Windows zClient, Amzetta zPortal DVM Tools, FlexiHub and Donglify.


Some of the updates are automatically applied, while others require customers to take action. The vendors’ responses:


* Accops’s [advisory page](https://blogs.accops.com/responsible-disclosure-security-vulnerability-in-accops-usb-redirection-driver/)
* NoMachine’s [advisory page](https://knowledgebase.nomachine.com/SU10S00227)


SentinelOne’s post also includes instructions on a manual update that’s necessary on AWS for users that have either maintenance turned off or AlwaysOn WorkSpaces with OS updates turned off.


As well, just because there’s no sign yet of in-the-wild exploitation, SentinelOne still recommends “revoking any privileged credentials deployed to the platform before the cloud platforms have been patched and checking access logs for irregularities.”


The Tip of the Iceberg
----------------------


Other cloud services using the same libraries are probably affected as well, according to SentinelOne’s advisory: “While we have confirmed these vulnerabilities for AWS, NoMachine and Accops, our testing was limited in scope to these vendors, and we believe it is highly likely other cloud providers using the same libraries would be vulnerable,” the firm said.


As well, given that SentinelOne hasn’t tested both client side and server side vulnerabilities in the products it did check out, there could be yet more vulnerabilities in the analyzed vendors’ products.


Code Flaws Ripple Through the Supply Chain
------------------------------------------


The security holes, which are also found in Eltima SDK-derived products and proprietary variants, have been “unwittingly inherited by cloud customers,” Dekel wrote.


SentinelOne pointed out that vulnerabilities in third-party code such as the ones found in Eltima’s SDK could spread far and wide, potentially endangering “huge” numbers of products, systems and, ultimately, users: everything and everybody downstream in the cloud supply chain.


Recent instances of the code supply chain’s vulnerability have included four Microsoft zero-day vulnerabilities in the Azure cloud platform’s Open Management Infrastructure (OMI) – a software that many don’t even realize is embedded in a host of services – that [showed up in September](https://threatpost.com/azure-zero-day-supply-chain/169508/). Dubbed “[OMIGOD](https://threatpost.com/azure-zero-day-supply-chain/169508/)” both for the infrastructure’s name and because that’s how researchers reacted when they discovered them, the weaknesses demonstrated a massive security blind spot.


Another example showed up in June, when [cryptominer code bombs showed up](https://threatpost.com/cryptominers-python-supply-chain/167135/) in the Python Package Index (PyPI): a code repository created in the Python programming language.


SentinelOne pointed to the pandemic-fueled need to adopt new work models to support work-from-home (WFH) staff. “This required organizations to make use of various solutions that allow WFH employees to securely access their organization’s assets and resources.” according to its writeup.


The result has been a booming market for WFH products, but security “has not necessarily evolved accordingly,” the advisory said.


*Image courtesy of [Blue Coat Photos](https://www.flickr.com/photos/111692634@N04/15921560456).* [*Licensing details.*](https://creativecommons.org/licenses/by-sa/2.0/)


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** [***REGISTER TODAY***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This*** [***LIVE, interactive Threatpost Town Hall***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***, sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***  

[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article) ***for the LIVE event!***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Derusbi]] [[action.malware.name=Elise]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cloud]] [[Sentinelone]] [[Eltima]] [[Accops]] [[Usb]] [[Workspaces]] [[Nomachine]] [[Sdk]] [[Threatpost]] [[ThreatPost]]

