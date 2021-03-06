# Vulnerabilities In Garrett Metal Detectors Allowed Remote Attacks
### The vulnerabilities affected the Garrett iC module empowering walk-through metal detectors with network connectivity. Bugs fixed now.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2021/12/29/vulnerabilities-in-garrett-walk-through-metal-detectors-allow-remote-attacks/
+ Date: 2021-12-29
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2021/12/walk-through-metal-detector.jpg)
 Researchers from Cisco Talos have elaborated on the security vulnerability they discovered in Garret metal detectors.

 Garrett is an American firm producing handheld and walk-through metal detectors for various consumers. Hence, any vulnerabilities in the products can pose a significant security risk.

 Specifically, the researchers found the vulnerabilities in the walk-through metal detectors from Garett. The bugs typically impacted two products – Garrett PD 6500i or Garrett MZ 6100 – affecting the Garrett iC module that provides network connectivity to the two detectors.

 Exploiting the bugs could allow an adversary to hack the detectors remotely and execute malicious commands. Describing the impact of such attacks, the researchers stated in their [post](https://blog.talosintelligence.com/2021/12/vuln-spotlight-garrett-metal-detector.html),

 
> An attacker could manipulate this module to remotely monitor statistics on the metal detector, such as whether the alarm has been triggered or how many visitors have walked through. They could also make configuration changes, such as altering the sensitivity level of a device, which potentially poses a security risk to users who rely on these metal detectors.
> 
> 

 Briefly, the researchers found the following bugs in the metal detectors,

 * Four stack-bases buffer overflow vulnerabilities ([CVE-2021-21901](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1353), [CVE-2021-21903](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1355), [CVE-2021-21905, and CVE-2021-21906](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1357)), leading to remote code execution.
* Four directory traversal bugs ([CVE-2021-21904](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1356), [CVE-2021-21907](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1358), [CVE-2021-21908, and CVE-2021-21909](https://talosintelligence.com/vulnerability_reports/TALOS-2021-1359)), allowing an authenticated attacker to read/write/delete files on the device.
* Single race condition ([CVE-2021-21902](https://blog.talosintelligence.com/2021/12/vuln-spotlight-garrett-metal-detector.html)) flaw allowing authenticated session hijacking.

 Mitigations And Patches
-----------------------

 The researchers found the nine vulnerabilities in Garrett Metal Detectors iC Module CMA, version 5.0. Following their report, the vendors worked on developing fixes for the glitches. Hence, they have patched the bugs in the latest release.

 Thus, the researchers advise all users to update their respective metal detectors with the latest firmware version to receive the patches.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Garrett]] [[Latest Hacking News]]
#### CVE's
[[CVE-2021-21901]] [[CVE-2021-21903]] [[CVE-2021-21905]] [[CVE-2021-21906]] [[CVE-2021-21904]] [[CVE-2021-21907]] [[CVE-2021-21908]] [[CVE-2021-21909]] [[CVE-2021-21902]]

