# Printing Shellz Vulnerabilities Affected 150+ HP Printers
### The researchers found Printing Shellz vulnerabilities while analyzing an HP MFP. Exploiting the bugs risk network security in an office setup.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2021/12/02/printing-shellz-vulnerabilities-affected-150-hp-printers/
+ Date: 2021-12-02
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2021/12/printer.png)
 Serious security vulnerabilities affecting numerous HP printer models have been discovered which could wreak havoc if exploited. Dubbed “Printing Shellz”, these vulnerabilities allowed a remote attacker to take control of target systems via HP printers.

 Printing Shellz HP Vulnerabilities
----------------------------------

 According to a recent [report](https://labs.f-secure.com/assets/BlogFiles/Printing-Shellz.pdf) from the F-Secure Labs, two researchers discovered some trivial bugs in [HP printers](https://latesthackingnews.com/tag/hp-printers/) that could severely impact target networks.

 Specifically, they tested a multi-function printer (MFP) commonly used in the corporate sector to find any serious bugs. They kept this device as a subject given their numerous functionalities in an office environment. As stated in their report,

 “Modern MFPs have various functionalities from print/fax over e-mail to large-scale integrations with organization directory services, document storage, and authorization and accounting functionalities.  
 If we consider an MFP from a red teaming perspective, it makes a great target for multiple reasons.

 Some of their specified “reasons” include,

 * the significant data that those devices process while printing and scanning,
* the requirement for user authentication that involves processing credentials, hence letting an attacker steal passwords,
* frequent use of USBs with MFPs that allow an adversary to [spread malware](https://latesthackingnews.com/2020/03/25/hackers-spread-malware-with-fake-covid-19-info-app-via-dns-hijacking-routers/) to a connected USB (which would then further spread to the network when connected on other devices),
* their ease of accessibility, especially in public settings, and
* the common “install and forget” installation settings where users seldom remember updating MFPs, hence adding to their potential vulnerabilities.

 All of these risk factors make printers an attractive target for the [threat actors](https://latesthackingnews.com/2021/11/29/threat-actors-used-tardigrade-malware-in-attacks-on-biomanufacturing-firms/).

 Hence, the researchers tested an HP MFP M725z that bears scanner, printer, and fax functionalities that increase its [attack surface](https://latesthackingnews.com/2020/12/07/attack-surface-discovery-do-non-attributable-domain-names-present-a-risk/).

 ### About the bugs

 Briefly, the first vulnerability they noticed was a buffer overflow vulnerability, CVE-2021-39238. Describing this bug in an [advisory](https://labs.f-secure.com/advisories/hp-multi-function-printers-improper-validation-of-an-array-index), F-Secure stated,

 
> The font parser library is vulnerable to a memory corruption issue due to improper validation of an array index (CWE-129). The issue can be exploited remotely using a Cross-Site Printing (XSP) vector as part of a drive-by or social engineering attack via workstations that can communicate directly with the devices’ JetDirect service. It is also possible to trigger and exploit the vulnerability locally using the ‘print from USB’ feature.
> 
> 

 Exploiting this bug could allow an attacker to take control of the device. This would further allow it to access in-process documents, any connected USBs, steal credentials, and move laterally in a “wormable” manner compromising the entire network.

 Whereas the second vulnerability, CVE-2021-39237, was a hardware flaw, describing which, the researchers state in the [advisory](https://labs.f-secure.com/advisories/hp-multi-function-printers-exposed-uart-interfaces),

 
> F-Secure have discovered exposed UART interfaces that provide unlimited access to the shell within the communication board of HP MFPs. One UART interface on the board provides access to the UEFI shell control, the other one to the root Linux shell of the scanner module.
> 
> 

 Planting malicious devices could let the attacker install malicious software, network pivoting, access in-process documents, and steal access credentials.

 HP Deployed Patches
-------------------

 Upon discovering the bugs, the researchers contacted HP to report the matter. While they didn’t test, the researchers explain that the vulnerabilities potentially affect over 150 HP printer models.

 Consequently, HP [deployed](https://support.hp.com/us-en/document/ish_5000383-5000409-16) the [patches](https://support.hp.com/us-en/document/ish_5000124-5000148-16) with the latest firmware updates. Currently, no exploitation of the bugs has been found. Nonetheless, all MFP users should ensure updating their devices to avoid any issues in the future.

 Also, it’s better to keep an eye on firmware updates for printers and other integrated devices to enhance network security.

 The researchers have shared the technical details of their findings in an interesting report that they presented at the Pwn2Own Austin 2021.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Mfps]] [[F-secure]] [[Mfp]] [[Latest Hacking News]]
#### CVE's
[[CVE-2021-39238]] [[CVE-2021-39237]]

