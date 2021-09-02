# Bluetooth Bugs Open Billions of Devices to DoS, Code Execution
### The BrakTooth set of security vulnerabilities impacts at least 11 vendors’ chipsets.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169159)
+ Date: September 2, 2021  2:32 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/02140504/Shark-Teeth.jpg)
Researchers have disclosed a group of 16 different vulnerabilities collectively dubbed BrakTooth, which impact billions of devices that rely on Bluetooth Classic (BT) for communication.


According to an academic paper from the University of Singapore, the bugs are found in the closed commercial BT stack used by [at least 1,400 embedded chip components](https://launchstudio.bluetooth.com/Listings/Search), that can lead to a host of attack types – mainly denial of service (DoS) via firmware crashes (the term “brak” is actually Norwegian for “crash”). One of the bugs can also lead to arbitrary code execution (ACE).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The team analyzed 13 pieces of BT hardware from 11 vendors; so far, there have been 20 CVEs assigned across them; with four vulnerabilities pending CVE assignments from Intel and Qualcomm. Some of the bugs are patched, others are in the process of being patched; but, researchers said [in the paper](https://asset-group.github.io/disclosures/braktooth/), “it is highly probable that many other products (beyond the ≈1400 entries observed in Bluetooth listing) are affected by BrakTooth,” including BT system-on-chips (SoCs), BT modules or additional BT end products.


Potentially, billions of devices could be affected worldwide, researchers said.


Here’s a table of the 16 bugs:


And here’s a list of known affected vendors:


The researchers uncovered three main attack scenarios for the bugs, the most severe of which results in ACE on internet-of-things (IoT) devices.


**Arbitrary Code Execution for Smart Home Devices**
---------------------------------------------------


The most critical vulnerability (CVE-2021-28139) affects ESP32 SoCs, a series of low-cost, low-power SoC microcontrollers with integrated Wi-Fi and dual-mode Bluetooth, from the vendor Espressif. These are commonly found in IoT appliances used in industry automation, smart-home device, personal fitness gadgets and more.


“A lack of out-of-bounds check in ESP32 BT Library allows the reception of a mutated LMP\_feature\_response\_ext,” according to the paper. “This results in the injection of eight bytes of arbitrary data outside the bounds of Extended Feature Page Table.”


To exploit it, an attacker who knows the firmware layout of a target device can write a known function address (JMP Addr.) to the offset pointed by Features Page field.


Researchers successfully forced ESP32 into erasing data housed in devices’ non-volatile random-access memory (NVRAM), which retains data without applied power. They were also able to disable both BT and Wi-Fi on the device; and most concerningly, control the general-purpose input/output (GPIO) of the device if the attacker knows addresses to attached functions-controlling actuators. GPIO is used to communicate the ON/OFF signals received from connected switches, or the digital readings received from connected sensors, to the CPU.


“This has serious implications if such an attack is applied to Bluetooth-enabled smart home products,” the researchers warned.


**DoSing Laptops & Smartphones**
--------------------------------


The second attack scenario can lead to DoS in laptops and smartphones. Researchers were able to achieve this using gear containing Intel AX200 SoCs and Qualcomm WCN3990 SoCs.


One of the DoS bugs (CVE-2021-34147) exists because of a failure in the SoC to free resources upon receiving an invalid LMP\_timing\_accuracy\_response from a connected BT device (i.e., a “slave,” according to the paper:


“The attacker can exhaust the SoC by (a) paging, (b) sending the malformed packet, and (c) disconnecting without sending LMP\_detach,” researchers wrote. “These steps are repeated with a different BT address (i.e., BDAddress) until the SoC is exhausted from accepting new connections. On exhaustion, the SoC fails to recover itself and disrupts current active connections, triggering firmware crashes sporadically.”


The researchers were able to forcibly disconnect slave BT devices from Windows and Linux laptops, and cause BT headset disruptions on Pocophone F1 and Oppo Reno 5G smartphones.


Another DoS bug (CVE pending) affects only devices using the Intel AX200 SoC.


It’s triggered when an oversized LMP\_timing\_accuracy\_request (i.e., bigger than 17 bytes) is sent to an AX200 slave.


“This temporarily corrupts AX200 firmware, which responds incorrectly during a subsequent BT connection and eventually disables the paging scan procedure,” researchers explained. “Thus, scanning AX200 works, but no connection is established from an external BT device.”


Aside from disconnecting master BT devices connected to a vulnerable laptop and leading to sporadic BT firmware crashes, this state of affairs can also be used for man-in-the-middle (MiTM) attacks. Bad actors can easily trick a user into connecting to the attacker’s BT hardware instead of the legitimate device, researchers noted – with persistence.


“Indeed, the user needs to manually re-enable BT to restore functionality,” they said, adding, “Due to the number of smartphones and laptops vulnerable to such attacks, and the common use of BT connectivity during video-conference calls and music streaming, updating the affected devices is essential.”


**BT Audio Product Freezes**
----------------------------


A third attack scenario was discovered while probing various BT speakers (specifically the Mi Portable Bluetooth Speaker – MDZ-36-DB, BT Headphone and BT Audio Modules) and an unbranded BT audio receiver.


They all are variously subject to a series of bugs (CVE-2021-31609 andCVE-2021-31612, failures when sending oversized LMP packets; CVE-2021-31613, truncated packets; CVE-2021-31611, starting procedures out-of-order; and CVE-2021-28135, CVE-2021-28155 and CVE-2021-31717, feature response flooding).


Successful exploits can “freeze” devices, requiring the user to manually turn on unresponsive devices afterwards. For the Xiaomi MDZ-36-DBs and JBL TUNE 500BTs, this can be done while the user is actively playing music, researchers noted.


“Although issues were found in SoCs targeted to audio products, the BT implementation can be reused in a number of SoCs destined to different BT products,” they added.


These are just a few of the possible exploit scenarios; a full vulnerability listing with descriptions [can be found here](https://asset-group.github.io/disclosures/braktooth/disclosure.html#x1-150008.1).


The researchers [have released](https://poc.braktooth.com/) a BrakTooth proof-of-concept (PoC) tool for vendors producing BT SoCs, modules and products – available for them to use to check their gear’s vulnerability.


BlueTooth vulnerabilities are particularly concerning given the vast footprint that they can impact, and unfortunately, they’re not that uncommon. For more, please see Threatpost’s recent previous BlueTooth bug coverage:


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





#### Tags:
[[AX200]] [[Bluetooth]] [[ESP32]] [[“This]] [[SoCs]] [[(i.e.,]] [[ThreatPost]]
