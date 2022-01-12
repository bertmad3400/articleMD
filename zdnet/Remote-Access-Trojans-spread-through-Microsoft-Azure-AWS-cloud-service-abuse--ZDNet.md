# Remote Access Trojans spread through Microsoft Azure, AWS cloud service abuse | ZDNet
### It seems that one or two Trojans aren't enough for your average cyberattacker.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/remote-access-trojans-spread-through-microsoft-azure-aws-cloud-service-abuse/
+ Date: 2022-01-12 13:03:00
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/11f9ff4eb7423fd5c17d394ddbe157bee742a6e3/2017/10/20/539fdef4-aaf3-407b-a820-252eaca5d4ab/istock-trojan-horse.jpg?width=770&height=578&fit=crop&auto=webp)

A recent campaign leveraging public cloud infrastructure is deploying not one, but three commercial Remote Access Trojans (RATs).


Nanocore, Netwire, and AsyncRAT payloads are being deployed from public cloud systems in what Cisco Talos suggests is a way for cyberattackers to avoid having to own or manage their own private, paid infrastructure -- such as through ['bulletproof' hosting](https://www.zdnet.com/article/group-pleads-guilty-to-running-bulletproof-hosting-service-for-criminal-gangs-malware-payloads/) which may eventually capture the interest of law enforcement.

This abuse allows cybercriminals to leverage the resources of cloud services managed by vendors including Microsoft Azure and Amazon Web Services (AWS) for malicious purposes.  

"These types of cloud services like Azure and AWS allow attackers to set up their infrastructure and connect to the internet with minimal time or monetary commitments," Talos says. "It also makes it more difficult for defenders to track down the attackers' operations." 

On Wednesday, Cisco Talos researchers Chetan Raghuprasad and Vanja Svajcer said that [a new campaign](https://blog.talosintelligence.com/2022/01/nanocore-netwire-and-asyncrat-spreading.html) based on public cloud infrastructure was discovered in October 2021 and the majority of victims are based in the US, Canada, and Italy – however, a handful appear to be from Spain and South Korea.  

The attack chain begins in a typical fashion: through a phishing email, often disguised as an invoice.  

These messages have .ZIP files attached which, once opened, reveal an ISO image. The ISO file is equipped with a malicious loader for the Trojans through either JavaScript, a Windows batch file, or a Visual Basic script.  






If a victim attempts to load the disk image, these scripts will trigger. Designed to deploy Nanocore, Netwire, and AsyncRAT, the scripts will reach out to a download server to snag a payload – and this is where a public cloud service comes into play.  

However, the downloader scripts use obfuscation techniques to hide these activities. The JavaScript contains four layers of obfuscation with each new, malicious process generated after the previous layer is peeled back; the batch file contains obfuscated commands that run PowerShell to pick up its payload, and the VBScript file also utilizes PowerShell commands. 

A PowerShell dropper built with HCrypt was also detected.  

The attackers behind the campaign manage a variety of payload hosts, command-and-control (C2) servers, and malicious subdomains. The majority detected, so far, are hosted on Azure and AWS.   

"Some of the download servers are running the Apache webserver application," the researchers say. "The HTTP servers are configured to allow the listing of open directories that contain variants of NanocoreRATs, Netwire RAT, and AsyncRATs malware." 

In addition, the operators abuse DuckDNS, a legitimate dynamic DNS service for pointing subdomains at IP addresses. The service is used to manage malware downloads via malicious DuckDNS subdomains and to mask the names of the C2 hosts, according to Talos.  

Netwire, Nanocore, and AsyncRAT are popular commercial Trojan strains that are widely used by threat actors to remotely access and hijack vulnerable machines, steal user data, and conduct surveillance by means including audio and camera capture. 

"Defenders should monitor traffic to their organization and implement robust rules around the script execution policies on their endpoints," the researchers commented. "It is even more important for organizations to improve email security to detect and mitigate malicious email messages and break the infection chain as early as possible." 

###  Previous and related coverage

* [Indian Patchwork hacking group infects itself with remote access Trojan](https://www.zdnet.com/article/indian-patchwork-hacking-group-infect-themselves-with-remote-access-trojan/)
* [ObliqueRAT Trojan now lurks in images on compromised websites](https://www.zdnet.com/article/obliquerat-trojan-now-hides-in-images-on-compromised-websites/)
* [New Windows RAT can be controlled via a Telegram channel](https://www.zdnet.com/article/new-windows-rat-can-be-controlled-via-a-telegram-channel/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Threatactor:
[[threatactor.name=Patchwork]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=NanoCore]] [[action.malware.name=Net]] [[action.malware.name=NETWIRE]] [[action.malware.name=ObliqueRAT]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=South Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=Spain]] [[victim.continent.name=Europe]] [[victim.country.name=Canada]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cloud]] [[Netwire]] [[Talos]] [[Nanocore]] [[Asyncrat]] [[Powershell]] [[ZDNet]]

