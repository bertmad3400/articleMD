# Black Hat: BadAlloc bugs expose millions of IoT devices to hijack
### BadAlloc vulnerabilities impact millions of devices worldwide.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/black-hat-badalloc-bugs-expose-millions-of-iot-devices-to-hijack/)
+ Date: August 6, 2021 -- 11:21 GMT (12:21 BST)
+ Author: Charlie Osborne


## Article:
Unknown

**BLACK HAT USA**: Microsoft researchers have explored in detail how "BadAlloc" vulnerabilities may impact millions of Internet of Things (IoT) and operational technology (OT) devices through their operating systems. 


Speaking to attendees at the [Black Hat](https://www.blackhat.com/us-21/briefings/schedule/index.html#error-badalloc---broken-memory-allocators-led-to-millions-of-vulnerable-iot-and-embedded-devices-23135) cybersecurity conference in Las Vegas, Microsoft Azure Defender for IoT researchers Omri Ben-Bassat and Tamir Ariel said XXX.  

BadAlloc is the name given to a swathe of memory allocation vulnerabilities found in IoT and OT products by Microsoft researchers. [Disclosed in April](https://www.zdnet.com/article/microsoft-finds-memory-allocation-holes-in-range-of-iot-and-industrial-technology/), the bugs could allow "adversaries to bypass security controls in order to execute malicious code or cause a system crash," according to the firm. 

The vulnerabilities exist in memory allocation functions present in at least 17 real-time operating systems (RTOS), SDKs, and self-memory management applications, impacting and impact functions including malloc, calloc, realloc, memalign, and more. 

Impacted products included devices offered by Amazon, Arm, Google, Media Tek, Samsung, and Texas Instruments, and a number of the vulnerabilities have been lurking in devices since the early 90s. 

According [to the team](https://msrc-blog.microsoft.com/2021/04/29/badalloc-memory-allocation-vulnerabilities-could-affect-wide-range-of-iot-and-ot-devices-in-industrial-medical-and-enterprise-networks/), the vulnerabilities can be triggered by "calling the memory allocation function, such as malloc, with the VALUE parameter derived dynamically from external input and being large enough to trigger an integer overflow or wraparound."

The wraparound ensures that the allocated memory remains small, creating a heap overflow, allowing for code execution to take place. 






During the presentation, XXXX

[presentation]

The US Cybersecurity and Infrastructure Security Agency (CISA) has previously [published an advisory](https://us-cert.cisa.gov/ics/advisories/icsa-21-119-04) on the vulnerabilities. Vendors were made aware of the flaws prior to public disclosure. 

====

[QUOTE] 

###  Previous and related coverage

* [Your insecure Internet of Things devices are putting everyone at risk of attack](https://www.zdnet.com/article/your-insecure-internet-of-things-devices-are-putting-everyone-at-risk-of-attack/)  

* [These new vulnerabilities put millions of IoT devices at risk, so patch now](https://www.zdnet.com/article/these-new-vulnerabilities-millions-of-iot-devives-at-risk-so-patch-now/)  

* [IoT security is a mess. These guidelines could help fix that](https://www.zdnet.com/article/iot-security-is-a-mess-these-guidelines-could-help-fix-that/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[IoT]] [[Microsoft]] [[ZDNet]]
