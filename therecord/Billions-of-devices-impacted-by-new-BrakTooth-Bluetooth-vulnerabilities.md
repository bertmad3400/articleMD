# Billions of devices impacted by new BrakTooth Bluetooth vulnerabilities
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/billions-of-devices-impacted-by-new-braktooth-bluetooth-vulnerabilities/)
+ Date: September 1, 2021
+ Author: Catalin Cimpanu


## Article:
![Billions of devices impacted by new BrakTooth Bluetooth vulnerabilities](https://therecord.media/wp-content/uploads/2021/09/BrakTooth.png)

* Academics found 16 vulnerabilities impacting the Bluetooth software stack of many popular SoC chipsets.
* The same Bluetooth software stacks are also used in 1,400 chipsets, used in laptops, smartphones, industrial, and iOT devices.
* The vulnerabilities can be used to crash, freeze, or take over vulnerable devices.


**A team of security researchers has published details this week about a suite of 16 vulnerabilities that impact the Bluetooth software stack that ships with System-on-Chip (SoC) boards from several popular vendors.**


The vulnerabilities, collectively known as **BrakTooth**, allow attackers to crash or freeze devices or, in the worst-case scenarios, execute malicious code and take over entire systems.


For their tests, researchers said they only examined the Bluetooth software libraries for 13 SoC boards from 11 vendors.


However, subsequent research found that the same Bluetooth firmware was most likely used inside more than 1,400 chipsets, used as the base for a wide assortment of devices, such as laptops, smartphones, industrial equipment, and many types of smart “Internet of Things” devices.


![BrakTooth-affected](https://www-therecord.recfut.com/wp-content/uploads/2021/09/BrakTooth-affected-982x1024.png)
### BrakTooth severity and impact varies per device


The number of affected devices is believed to be in the realm of billions, but the impact is different based on the device’s underlying SoC board and Bluetooth software stack.


The worst vulnerability part of the BrakTooth findings is CVE-2021-28139, which allows remote attackers to run their own malicious code on vulnerable devices via Bluetooth LMP packets.


According to the research team, CVE-2021-28139 affects smart devices and industrial equipment built on Espressif Systems’ ESP32 SoC boards, but the issue is bound to impact many of the other 1,400 commercial products some of which are bound to have reused the same Bluetooth software stack.





Other BrakTooth issues are less severe but still annoying. For example, there are several vulnerabilities that can be used to crash the Bluetooth service on smartphones and laptops by flooding devices with malformed Bluetooth LMP (Link Manager Protocol) packets.


Vulnerable to these attacks are Microsoft Surface laptops, Dell desktops, and several Qualcomm-based smartphone models.





In addition, attackers can also use truncated, oversized, or out-of-order Bluetooth LMP packets to crash devices altogether, which will require a manual reboot, as seen in the demo below.





The research team said that all the BrakTooth attacks could be carried out with off-the-shelve Bluetooth equipment that costs less than $15.


All in all, 16 vulnerabilities were discovered in the 13 SoC chipsets the research team tested.


![Braktooth-CVEs](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Braktooth-CVEs-1024x759.png)
### Not all vendors released patches


All 11 vendors were approached months before researchers published their findings and notified about these security issues.


Despite the lengthy 90+ days warning, not all vendors were able to have patches out in time.


Only Espressif Systems, Infineon (former Cypress), and Bluetrum have released patches so far, while Texas Instruments said they would not be addressing the flaws impacting their chipsets.


![Braktooth-patches](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Braktooth-patches-1024x412.png)
The other vendors acknowledged the researchers’ findings but could not confirm a definite release date for a security patch, citing internal investigations into how each of the BrakTooth bugs impacted their software stacks and product portfolios.


A spokesperson for the Bluetooth Special Interest Group, which governments the development of the Bluetooth standard, told *The Record* they’ve been made aware of these issues but couldn’t pressure vendors into patches since these issues don’t impact the standard itself, but each vendor’s own implementation.


Since patching has not yet been completed, the research team said they don’t plan to release any of the proof-of-concept code to reproduce BrakTooth attacks but have set up a [web form](https://poc.braktooth.com/) instead where vendors can approach them and request the code to test devices on their own.


Details about future patches released after this article’s publication, along with technical details about the BrakTooth vulnerabilities, are available on this [dedicated website](https://braktooth.com/).




---


Other vulnerabilities impacting the Bluetooth protocol and its implementations that have been disclosed over the past two years include the likes of:


* [BLESA](https://www.usenix.org/conference/woot20/presentation/wu)
* [BLURtooth](https://kb.cert.org/vuls/id/589825)
* [BIAS](https://francozappa.github.io/about-bias/)
* [SweynTooth](https://asset-group.github.io/disclosures/sweyntooth/)
* [KNOB](https://www.kb.cert.org/vuls/id/918987/)





#### Tags:
[[Bluetooth]] [[BrakTooth]] [[laptops,]] [[devices.]] [[LMP]] [[The Record]]
