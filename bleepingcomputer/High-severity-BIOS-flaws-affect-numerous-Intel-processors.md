# High severity BIOS flaws affect numerous Intel processors
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/high-severity-bios-flaws-affect-numerous-intel-processors/)
+ Date: November 15, 2021
+ Author: Bill Toulas


## Article:
![intel](https://www.bleepstatic.com/content/hl-images/2021/01/26/Intel-CPU.jpg?rand=778037260)


Intel has disclosed two high-severity vulnerabilities that affect a wide range of Intel processor families, allowing threat actors and malware to gain higher privilege levels on the device.


The flaws were discovered by SentinelOne and are tracked as CVE-2021-0157 and CVE-2021-0158, and both have a CVSS v3 score of 8.2 (high).


The former concerns the insufficient control flow management in the BIOS firmware for some Intel processors, while the latter relies on the improper input validation on the same component.


These vulnerabilities could lead to escalation of privilege on the machine, but only if the attacker had physical access to vulnerable devices.


The affected products, according to [Intel's advisory](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00562.html), are the following:


* Intel® Xeon® Processor E Family
* Intel® Xeon® Processor E3 v6 Family
* Intel® Xeon® Processor W Family
* 3rd Generation Intel® Xeon® Scalable Processors
* 11th Generation Intel® Core™ Processors
* 10th Generation Intel® Core™ Processors
* 7th Generation Intel® Core™ Processors
* Intel® Core™ X-series Processors
* Intel® Celeron® Processor N Series
* Intel® Pentium® Silver Processor Series


Intel hasn't shared many technical details around these two flaws, but they advise users to patch the vulnerabilities by applying the available BIOS updates.


This is particularly problematic because motherboard vendors do not release BIOS updates often and don't support their products with security updates for long.


Considering that 7th gen Intel Core processors came out five years ago, it's doubtful that MB vendors are still releasing security BIOS updates for them.


As such, some users will be left with no practical way to fix the above flaws. In these cases, we would suggest that you set up a strong password for accessing the BIOS settings.


A third vulnerability affects cars
----------------------------------


A third flaw for which Intel released a separate advisory on the same day is CVE-2021-0146, also a high-severity (CVSS 7.2) elevation of privilege flaw.



> 
> “Hardware allows activation of test or debug logic at runtime for some Intel(R) processors which may allow an unauthenticated user to potentially enable escalation of privilege via physical access.” - [Intel's advisory](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00528.html)
> 
> 
> 


This bug affects the following products:



![Affected Intel products](https://www.bleepstatic.com/images/news/u/1220909/Tables/table(1).jpg)**Affected Intel products**  
*Source: Intel*
Intel has released a firmware update to mitigate this flaw, and users will get it through patches supplied by the system manufacturer.


Positive Technologies, who discovered and reported the bug to Intel, says that the flaw could allow threat actors to gain access to highly sensitive information.  
  

“One example of a real threat is lost or stolen laptops that contain confidential information in encrypted form,” [says Mark Ermolov](https://www.ptsecurity.com/ww-en/about/news/positive-technologies-discovers-vulnerability-in-intel-processors-used-in-laptops-cars-and-other-devices/).


“Using this vulnerability, an attacker can extract the encryption key and gain access to information within the laptop. The bug can also be exploited in targeted attacks across the supply chain.”


“For example, an employee of an Intel processor-based device supplier could, in theory, extract the Intel CSME firmware key and deploy spyware that security software would not detect."


Positive Technologies says that the flaw also affects several car models that use the Intel Atom E3900, including the Tesla Model 3.


Users should apply a BIOS update from the device vendor to address this flaw, so check your manufacturer's website regularly.


Remember, it's always a good idea to backup your data on a separate system or removable media before applying any of these patches, as there's always a chance of something going wrong with the update.These flaws mainly impact systems in industrial and corporate environments exposed to physical access by many people.


As for the cars, this should be exploitable only by service points and car mechanics who will access the vehicle's internals.




#### Tags:
[[Intel®]] [[Xeon®]] [[CoreTM]] [[Bleeping Computer]]
