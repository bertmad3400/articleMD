# Researchers warn of severe risks from ‘Printjack’ printer attacks
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/researchers-warn-of-severe-risks-from-printjack-printer-attacks/)
+ Date: November 23, 2021
+ Author: Bill Toulas


## Article:
![printer](https://www.bleepstatic.com/content/hl-images/2021/06/30/Printer.jpg?rand=399956048)


A team of Italian researchers has compiled a set of three attacks called 'Printjack,' warning users of the significant consequences of over-trusting their printer.


The attacks include recruiting the printers in DDoS swarms, imposing a paper DoS state, and performing privacy breaches.


As the researchers point out, modern printers are still vulnerable to elementary flaws and lag behind other IoT and electronic devices that are starting to conform with cybersecurity and data privacy requirements.


By evaluating the attack potential and the risk levels, the researchers found non-compliance with GDPR requirements and the ISO/IEC 27005:2018 (framework for managing cyber-risks).


This lack of in-built security is particularly problematic when considering how omnipresent printers are, being deployed in critical environments, companies, and organizations of all sizes.


Finding exploitable printers
----------------------------


A paper titled 'You Overtrust Your Printer' by [Giampaolo Bella](https://www.dmi.unict.it/giamp/) and Pietro Biondi explains how Shodan was used to scan European countries for devices with a publicly accessible TCP port 9100, typically used for raw TCP/IP printing jobs.


This search resulted in tens of thousands of IPs responding to the port query, with Germany, Russia, France, Netherlands, and the UK having the most exposed devices.


While port 9100 can be configured for other jobs besides printing, it’s the default port for that service, so most of these results are likely related to printing.



![Sample of scan results](https://www.bleepstatic.com/images/news/u/1220909/Tables/printer%20numbers.jpg)**Sample of scan results**  
*Source: Arxiv*
Taking part in DDoS attacks
---------------------------


The first type of Printjack attack is to recruit the printer in a DDoS swarm, and threat actors can do this by exploiting a known RCE vulnerability with a publicly available PoC. 


The researchers use [CVE-2014-3741](https://nvd.nist.gov/vuln/detail/CVE-2014-3741) as an example but underline that at least a few dozen other vulnerabilities are available in the MITRE database.


Considering that there are 50,000 exposed devices in the top ten EU countries alone, putting in the effort to recruit them for DDoS attacks isn't unlikely at all.


Printers that fall victims to this attack are more likely to be unresponsive, consume more power, and generate more heat, while their electronics will suffer from accelerated decay.


DoSing the printer itself
-------------------------


The second attack is a 'paper DoS attack' achieved by sending repeated print jobs until the victim runs out of paper from all trays.


This situation doesn't sound like a catastrophe, but it could still cause business disruption, so it's not about ink and paper cost but service downtime and incident response.


The researchers explain that this attack is easy to carry out by writing a simple Python script executed within the target network, creating a printing job loop that repeats a thousand times.



![Script used for placing the printer in DoS state](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/python_script.jpg)**Script used for placing the printer in DoS state**  
*Source: Arxiv*
Infringing owner’s privacy
--------------------------


In the most severe type of Printjack attacks, there's the potential to carry out "man in the middle" attacks and eavesdrop on the printed material.


Because no printing data is sent in encrypted form, if an attacker exploited a vulnerability on the printer's network, they could theoretically retrieve data in plaintext form.


For demonstration, the researchers used Ettercap to interpose between the sender and the printer, and then Wireshark intercepted a PDF file sent for printing.


To carry out this attack, the actor must have local access or must have exploited a vulnerability over a node of the target network.



![Sniffed PDF file](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Sniffed PDF file**  
*Source: Arxiv*
Not a new problem
-----------------


The lack of solid security frameworks on printers is an issue that has been raised numerous times in recent years, especially after printers became internet-connected.


In 2018, an actor nicknamed '[TheHackerGiraffe](https://www.bleepingcomputer.com/news/security/chromecast-hacker-calls-it-quits-after-hearing-fbi-is-looking-into-him/)' caused a large-scale disturbance by hijacking 100,000 printers to promote the PewDiePie YouTube channel for fun.


In 2020, CyberNews did something similar, forcing [28,000 printers](https://cybernews.com/security/we-hacked-28000-unsecured-printers-to-raise-awareness-of-printer-security-issues/) to print out guidelines on securing them.


In 2021, researchers discovered a high severity flaw affecting millions of printers from various manufacturers, which went undetected and unfixed for a whopping [16 years](https://www.bleepingcomputer.com/news/security/16-year-old-bug-in-printer-software-gives-hackers-admin-rights/).


Printer vendors need to upgrade their devices' security and data handling processes, both on the hardware and software levels.


Similarly, users and businesses need to stop treating their printers as a negligible element of their daily computing, falsely assuming that printers can have no real risk to them or their data.


"Well beyond the technicalities of the attacks lies a clear lesson learned. Printers ought to be secured equally as other network devices such as laptops normally are," Bella and Biondi conclude in [their paper](https://arxiv.org/pdf/2111.10645.pdf).


"A few appropriate security measures can be envisaged. For example, if user access to a laptop is normally authenticated, then so should be user access to the web-server-based admin panel of a printer, which often allows, for example, printer reset, printer name change, access to list of printed file names, etc."


"Similarly, remote connection to a port of a laptop will be bound to authentication to some daemon and, likewise, sending a print job should require an extra level of authentication to the printer."




#### Tags:
[[DDoS]] [[Arxiv]] [[Bleeping Computer]]
