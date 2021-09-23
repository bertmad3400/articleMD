# Google finds adware strain abusing novel file signature evasion technique
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/google-finds-adware-strain-abusing-novel-file-signature-evasion-technique/)
+ Date: September 23, 2021
+ Author: Catalin Cimpanu


## Article:
![Google finds adware strain abusing novel file signature evasion technique](https://therecord.media/wp-content/uploads/2021/09/code-certificate.png)

One of Google’s security teams said it found a malware strain abusing a new technique to evade detection from security products by cleverly modifying the digital signature of its payloads.


Discovered by Neel Mehta, a security researcher for the Google Threat Analysis Group (TAG), the technique was seen abused by an adware strain named **OpenSUpdater**.



> In these new samples, the signature was edited such that an End of Content (EOC) marker replaced a NULL tag for the ‘parameters’ element of the [SignatureAlgorithm](https://datatracker.ietf.org/doc/html/rfc3280#section-4.1.1.2) signing the leaf X.509 certificate. EOC markers terminate indefinite-length encodings, but in this case an EOC is used within a definite-length encoding (l= 13).
> 
> [Neel Mehta, analyst for the Google Threat Analysis Group](https://blog.google/threat-analysis-group/financially-motivated-actor-breaks-certificate-parsing-avoid-detection/)


While the technical explanation is a bit hard to understand for non-technical users, Mehta is referring to a tiny edit the OpenSUpdater gang made in a small field inside the digital signature of their payloads.


On Windows systems, this tiny edit does not impact the operating system’s file signature checks, which when passed, allow the file to run without any security warnings.


However, Mehta says that security products, most of which use the OpenSSL library to parse and extract a file’s signature information, will fail to scan files that had their digital signature modified by this method.


“This is the first time TAG has observed actors using this technique to evade detection while preserving a valid digital signature on PE files,” Mehta explained today.


The Google researcher said he reported the issue to Microsoft so the Redmond-based company can start work on modifying its signature checking algorithms.


Files infected with the OpenSUpdater adware are currently distributed via game cracks and pirated software.


Once they infect a system, the adware is used to download and install unwanted software, part of pay-per-install schemes.


Google said most OpenSUpdater victims are located in the US.





#### Tags:
[[Google]] [[adware]] [[Mehta]] [[OpenSUpdater]] [[The Record]]
