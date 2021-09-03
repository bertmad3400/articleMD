# Bluetooth BrakTooth bugs could affect billions of devices
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/bluetooth-braktooth-bugs-could-affect-billions-of-devices/)
+ Date: September 2, 2021
+ Author: Ionut Ilascu


## Article:
![BrakTooth vulnerabilities can enable code execution on affected devices or crash them](https://www.bleepstatic.com/content/hl-images/2021/09/02/braktooth.jpg)


Vulnerabilities collectively referred to as BrakTooth are affecting Bluetooth stacks implemented on system-on-a-chip (SoC) circuits from over a dozen vendors.


The set of issues impact a wide variety of devices, from consumer electronics to industrial equipment. The associated risk ranges from denial-of-service, deadlock condition of the device to arbitrary code execution.


### Wide variety of products impacted


Researchers from the Singapore University of Technology and Design have published details about BrakTooth - a new family of security vulnerabilities in commercial Bluetooth stacks.


They assessed 13 Bluetooth devices from close to a dozen SoC vendors counting Intel, Qualcomm, Texas Instruments, and Cypress.


Digging deeper, the researchers discovered that more than 1,400 product listings are affected by BrakTooth, and the list includes but is not limited to the following types of devices:


* Smartphones
* Infotainment systems
* Laptop and desktop systems
* Audio devices (speakers, headphones)
* Home entertainment systems
* Keyboards
* Toys
* Industrial equipment (e.g. programmable logic controllers - PLCs)


Considering the variety of products affected, saying that BrakTooth affects billions of devices is likely an accurate estimation. 


The [researchers say](https://asset-group.github.io/disclosures/braktooth/) that the risk associated with the BrakTooth set of security flaws ranges from denial-of-service (DoS) by crashing the device firmware, or a deadlock condition where Bluetooth communication is no longer possible, to arbitrary code.


Someone pulling a BrakTooth attack would need an ESP32 development kit, a custom Link Manager Protocol (LMP) firmware, and a computer to run the proof-of-concept (PoC) tool.


![BrakTooth attack scenario](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/BrakToothScenario.jpg)


Of the 16 BrakTooth vulnerabilities, one of them tracked as CVE-2021-28139 presents a higher risk than others because it allows arbitrary code execution.


It affects devices with an ESP32 SoC circuit, which is found in numerous IoT appliances for home or industry automation.


The researchers demonstrate the attack in the video below by changing the state of an actuator using an LMP Feature Response Extended packet:



Devices running on the AX200 SoC from Intel and Qualcomm’s WCN3990 SoC are vulnerable to a DoS condition triggered when sending a malformed packet.


The list of products impacted includes laptops and desktops from Dell (Optiplex, Alienware), Microsoft Surface devices (Go 2, Pro 7, Book 3), and smartphones (e.g. Pocophone F1, Oppo Reno 5G).



The researchers informed all vendors whose products they found to be vulnerable to BrakTooh ahead of the publication of their findings but only some of them have been patched.


![Patch state of BrakTooth vulnerabilities affecting Bluetooth stack](https://www.bleepstatic.com/images/news/u/1100723/2021/Vulnerabilities/BrakToothPatches.jpg)


The vulnerabilities in the Braktooth collection target the LMP and baseband layers. Currently, they’ve been assigned 20 identifiers with a few more pending, and refer to the following 16 issues:


1. Feature Pages Execution (CVE-2021-28139 - arbitrary code execution/deadlock)
2. Truncated SCO Link Request (CVE-2021-34144 - deadlock)
3. Duplicated IOCAP (CVE-2021-28136 - crash)
4. Feature Response Flooding (CVE-2021-28135, CVE-2021-28155, CVE-2021-31717 - crash)
5. LMP Auto Rate Overflow (CVE-2021-31609, CVE-2021-31612 - crash)
6. LMP 2-DH1 Overflow (pending CVE - deadlock)
7. LMP DM1 Overflow (CVE-2021-34150 - deadlock)
8. Truncated LMP Accepted (CVE-2021-31613 - crash)
9. Invalid Setup Complete (CVE-2021-31611 - deadlock)
10. Host Conn. Flooding (CVE-2021-31785 - deadlock)
11. Same Host Connection (CVE-2021-31786 - deadlock)
12. AU Rand Flooding (CVE-2021-31610, CVE-2021-34149, CVE-2021-34146, CVE-2021-34143 - crash/deadlock)
13. Invalid Max Slot Type (CVE-2021-34145 - crash)
14. Max Slot Length Overflow (CVE-2021-34148 - crash)
15. Invalid Timing Accuracy (CVE-2021-34147 and two more pending CVEs - crash)
16. Paging Scan Deadlock (pending CVE - deadlock)




#### Tags:
[[deadlock)]] [[crash)]] [[BrakTooth]] [[LMP]] [[Bluetooth]] [[Bleeping Computer]]
