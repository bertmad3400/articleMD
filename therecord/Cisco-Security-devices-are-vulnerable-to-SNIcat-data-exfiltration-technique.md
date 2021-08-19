# Cisco: Security devices are vulnerable to SNIcat data exfiltration technique
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/cisco-security-devices-are-vulnerable-to-snicat-data-exfiltration-technique/)
+ Date: August 18, 2021
+ Author: Catalin Cimpanu


## Article:
![Cisco: Security devices are vulnerable to SNIcat data exfiltration technique](https://therecord.media/wp-content/uploads/2021/08/snicat-logo.png)

Networking equipment vendor Cisco said today that some of its security products fail to detect and stop traffic to malicious servers that abuse a technique called SNIcat to covertly steal data from inside corporate networks.


Affected devices include Cisco firewalls running FTD (Firepower Threat Defense) software, devices running the WSA (Web Security Appliance) modules, and all ISA3000 (Industrial Security Appliance) firewalls.


### What is SNIcat?


[First disclosed in August 2020](https://www.mnemonic.no/blog/introducing-snicat/), **SNIcat** is a data exfiltration technique discovered by Norwegian security firm mnemonic.


In particular, mnemonic researchers discovered that many popular network security devices were checking user traffic against their block-lists **after** the user’s device negotiated a TLS handshake.


Starting from this premise, the mnemonic team developed a simple [proof-of-concept Python script](https://github.com/mnemonic-no/SNIcat) that would take sensitive information from a compromised computer and hide it inside the **TLS Client Hello** packet, which is exchanged at the beginning of a TLS handshake, and before the user’s connection was checked for possible suspicious traffic.


![TLS-handshake](https://www-therecord.recfut.com/wp-content/uploads/2021/08/TLS-handshake.png)Image: mnemonic
Last year, mnemonic said they had limited resources at their disposal and were only able to test a handful of devices for SNIcat exfiltration; however, they said that more vendors were also likely to be blind to this technique.


Today, Cisco became the fourth major network security vendor—after [F5 Networks](https://support.f5.com/csp/article/K20105555), Fortinet, and [Palo Alto Networks](https://security.paloaltonetworks.com/CVE-2020-2035)—to formally admit that its devices can be bypassed using the SNIcat technique.


Check Point said its devices were [not vulnerable](https://community.checkpoint.com/t5/General-Topics/Checkpoints-exposure-to-CVE-2020-2035-and-CVE-2020-15936-SNIcat/m-p/104115/highlight/true#M20004).


Cisco is currently investigating several other device models and is expected to release patches and detection rules. See the company’s [official advisory](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sni-data-exfil-mFgzXqLN) for future updates.


Additional details on the SNIcat technique are also available in the video below, showing the mnemonic team presenting its findings at the Black Hat Europe 2020 security conference.








#### Tags:
[[SNIcat]] [[TLS]] [[The Record]]
