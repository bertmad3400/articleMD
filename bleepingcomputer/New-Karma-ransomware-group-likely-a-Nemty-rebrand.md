# New Karma ransomware group likely a Nemty rebrand
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-karma-ransomware-group-likely-a-nemty-rebrand/)
+ Date: October 19, 2021
+ Author: Bill Toulas


## Article:
![karma yin yang](https://www.bleepstatic.com/content/hl-images/2021/10/19/KARMA.jpg)


Threat analysts at Sentinel Labs have found evidence of the Karma ransomware being just another evolutionary step in the strain that started as JSWorm, became Nemty, then Nefilim, Fusion, Milihpen, and most recently, Gangbang.


The name Karma has been used by ransomware actors [back in 2016](https://www.bleepingcomputer.com/news/security/researcher-finds-the-karma-ransomware-being-distributed-via-pay-per-install-network/), but there is no relation between that group and the one that emerged this year.


JSWorm [first appeared in 2019](https://www.bleepingcomputer.com/forums/t/698141/jsworm-ransomware-jsworm-jurasik;-jsworm-decrypttxt-support/), and went through a series of rebrands over the next two years, while always retaining code similarities that were enough for researchers to make the connection. 



![The evolution of JSWorm](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/evolution(1).png)**The evolution of JSWorm,**Source: Kaspersky
Similarities go wide and deep
-----------------------------


The [report](http://www.sentinelone.com/labs/karma-ransomware-an-emerging-threat-with-a-hint-of-nemty-pedigree/) is based on the analysis of eight samples taken from an equal number of ransomware attacks in June 2021, all having notable code similarities to Gangbang and Milihpen variants that appeared around January 2021.


The extent of similarities ranges to the exclusion of folders, file types, and the debug messages used by the seemingly unrelated strains.



![Various functional similarities between the two strains.](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/similarieis.jpg)**Various functional similarities between the two strains.**  

Source: Sentinel Labs
Another noteworthy similarity can be spotted when conducting a “bindiff” on Karma and Gangbang samples, seeing an almost unchanged ‘main()’ function.



![Similarities in 'main()' function](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Similarities in 'main()' function**  

Source: Sentinel Labs
From the perspective of the encryption scheme used, there has been an evolution across the samples, with the earlier ones using the Chacha20 encryption algorithm and the most recent samples switching to Salsa20.


Another change that was introduced along the way was to create a new thread for the enumeration and the encryption, possibly to achieve a more reliable outcome.


The authors of the malware have also added support for command line parameters on the latest versions.


All in all, the work on the malware and the tight compilation dates of the analyzed samples reflect the fact that Karma is currently under active development.


In terms of the victim communication and the extortion method, Karma follows the typical approach of dropping ransom notes, stealing data from compromised systems, and following up for a double-extortion process. 


Historically, Nemty targeted mostly Chinese firms in the engineering and manufacturing sector, leveraging [exposed RDPs](https://www.bleepingcomputer.com/news/security/new-nemty-ransomware-may-spread-via-compromised-rdp-connections/) and published VPN exploits to infiltrate to vulnerable networks. 


Karma could be a temporary rebrand
----------------------------------


In a private discussion that BleepingComputer had with the researcher who signs the analysis, Antonis Terefos, we got the following assessment on Karma’s current state:



> 
> The Nemty onion leak page ‘Corporate Leaks’ currently is running on (Onion) version 2 which will be deprecated soon, and the last leak there was observed on 20th of July. Karma’s leak page was created on 22nd of May and first leak occurred on the 1st of September. 
> 
> 
> With the current data at hand, the Karma ransomware and its onion pages appears to be another rebrand of Nemty and Corporate leaks. Code-wise the main differences appear on the encryption algorithm, which is an area of experimentation for many ransomware authors. 
> 
> 
> 


Indeed, ‘Corporate Leaks’ has gone dormant around the same time that Karma Leaks appeared as the group’s new data leak portal.


Notably, the new portal has also entered a short period of inactivity lately, with the most recent victim listed there being from 20 days ago.


All that said, Karma could be just a short-term station in the continuation of a [long-term](https://securelist.com/evolution-of-jsworm-ransomware/102428/) ransomware operation from a group that pretends to be less than they really are.




#### Tags:
[[ransomware]] [[Source:]] [[Nemty]] [[Bleeping Computer]]
