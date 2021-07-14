# Unpatched Critical RCE Bug Allows Industrial, Utility Takeovers
### The ‘ModiPwn’ bug lays open production lines, sensors, conveyor belts, elevators, HVACs and more that use Schneider Electric PLCs.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167751)
+ Date: July 13, 2021  4:04 pm
+ Author: Tara Seals


## Article:
A critical remote code-execution (RCE) vulnerability in Schneider Electric programmable logic controllers (PLCs) has come to light, which allows unauthenticated cyberattackers to gain root-level control over PLCs used in manufacturing, building automation, healthcare and enterprise environments.


If exploited, attackers could impact production lines, sensors and conveyor belts in factory settings, according to the researchers at Armis who discovered the bug – as well as affect devices familiar to the everyday consumer, such as elevators, HVACs and other automated devices.


The vulnerability (CVE-2021-22779), which takes advantage of undocumented commands in device code, impacts the Modicon M340, M580 and other models from the Modicon series, according to Armis, which dubbed it “ModiPwn.” It’s technically an authentication bypass by spoofing vulnerability, researchers said, and it rates 9.8 out 10 on the CVSS vulnerability-rating scale, making it critical. It’s one of a slew of bugs addressed by the vendor on Tuesday.



Any attack would begin with gaining network access to the same network to which the targeted Modicon PLC is attached, researchers said – a positive mitigation in that the extra, required first step makes it harder for an attacker to be successful.


However, “through this access, the attacker can leverage undocumented commands in the UMAS protocol and leak a certain hash from the device’s memory,” according to Armis’ analysis, [released on Tuesday](https://www.armis.com/research/modipwn/). UMAS is a proprietary protocol used to configure and monitor Schneider PLCs.


Researchers added, “Using this hash, the attacker can take over the secure connection between the controller and its managing workstation to reconfigure the controller with a password-less configuration. This will allow the attacker to abuse additional undocumented commands that lead to remote-code-execution — a full takeover of the device.”


This takeover can then be used to install malware on the controller, alter its operation and then hide the attack’s breadcrumbs from the workstation that manages the controller, they added.


**No Patch Available**
----------------------


Schneider has [released a set of mitigations](https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2021-194-01) for the bug, but no full patch is available yet.


“Armis and Schneider Electric have worked together to ensure the proper security mitigations are being provided. We urge all affected organizations to take action now,” said Ben Seri, with Armis, in a statement. “The trouble with these legacy devices found in OT environments is that historically, they have evolved over unencrypted protocols. It will take time to address these weak underlying protocols. In the meantime, organizations operating in these environments should ensure that they have visibility over these devices to see where their points of exposure lie. This is crucial to preventing attackers from being able to control their systems – or even hold them to ransom.”


**Schneider’s Slew of ICS Patches**
-----------------------------------


“ModiPwn” is just one of the security holes addressed by the ICS giant on Tuesday. In all, Schneider [released](https://www.se.com/ww/en/work/support/cybersecurity/security-notifications.jsp) dozens of new patches and mitigations for various flaws across its entire product portfolio (most of them rating medium or high-severity), and updates for many other existing advisories.


Two other critical bugs stood out, however: One addressed by the vendor is [CVE-2021-22772](https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2021-194-05), which carries a CVSS score of 9.1 and affects the Easergy T200 grid-automation platform. It’s arises because of missing authentication for critical functions, which can allow attackers to carry out unauthorized operations.


A third critical issue ([CVE-2021-22707](https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2021-194-06)) exists in the vendor’s smart-city EVlink Parking and other gear. It has a CVSS score of 9.4 and stems from the use of hard-coded credentials. Attackers could exploit it to issue unauthorized commands to the charging station web server with administrative privileges, according to Schneider.


No in-the-wild attacks have been spotted, researchers said, but these kinds of vulnerabilities in industrial control systems have opened the door to concerning attacks in the past. The [Triton malware](https://threatpost.com/understanding-triton-and-the-missing-final-stage-of-the-attack/134895/), for example, was spotted in 2018 targeting the Triconex Safety Instrumented System (SIS) from Schneider within petrochemical plants in Saudi Arabia. SIS are the last line of automated safety defense for industrial facilities, designed to prevent equipment failure and catastrophic incidents such as explosions or fire.


A handful of other malware also has targeted the physical process of ICS, such as the [infamous Stuxnet](https://threatpost.com/stuxnet-apts-gossip-girl/143595/) strain that was used to disrupt the Iranian nuclear program and the Industroyer/Crash Override malware that [caused a power blackout](https://threatpost.com/notpetya-linked-to-industroyer-attack-on-ukraine-energy-grid/138287/) in Ukraine.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 




#### Tags:
[[Armis]] [[malware]] [[PLCs]] [[Modicon]] [[CVSS]] [[mitigations]] [[ICS]] [[ThreatPost]]
