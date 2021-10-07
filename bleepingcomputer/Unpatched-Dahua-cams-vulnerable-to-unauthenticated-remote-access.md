#  Unpatched Dahua cams vulnerable to unauthenticated remote access
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/unpatched-dahua-cams-vulnerable-to-unauthenticated-remote-access/)
+ Date: October 7, 2021
+ Author: Bill Toulas


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/10/07/cctv_camera.jpg?rand=2064995083)


Unpatched Dahua cameras are prone to two authentication bypass vulnerabilities, and a proof of concept exploit that came out today makes the case of upgrading pressing. 


The authentication bypass flaws are tracked as [CVE-2021-33044](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33044) and [CVE-2021-33045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33045), and are both remotely exploitable during the login process by sending specially crafted data packets to the target device. 


For more details on how that works, you may check out the proof of concept (PoC) that was part of today’s full disclosure, which has been posted [on GitHub](https://github.com/mcw0/DahuaConsole). 


This comes a month after Dahua’s [security advisory](https://www.dahuasecurity.com/support/cybersecurity/details/957) which urged owners of vulnerable models to upgrade their firmware, but considering how neglected these devices are following their initial installation and set up, it’s likely that many of them are still running an old and vulnerable version. 


The list of the affected models is extensive and covers many of Dahua cameras, even some thermal ones. We have searched on Shodan and found over 1.2 million Dahua systems around the world.



![Dahua cameras online around the world](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/number-of-cams.png)Dahua cameras online around the world. Source: Shodan
It is important to clarify that not all of these devices are vulnerable to exploitation, but the list of the affected models contains some widely deployed ones.  


A banned security headache
--------------------------


Dahua Technology is banned from doing business and selling products in the United States, as the Chinese surveillance camera vendor was added onto the U.S. Department of Commerce’s ‘Entity List’ back [in October 2019](https://s3.amazonaws.com/public-inspection.federalregister.gov/2019-22210.pdf). 


However, there are still tens of thousands of Dahua cameras actively used in the country, and some of them may not be so obvious. As a recent report from [The Intercept](https://theintercept.com/2021/07/20/video-surveillance-cameras-us-military-china-sanctions/) details, many cameras sold in the U.S. under American (like Honeywell) or Canadian branding are, in fact, using Dahua hardware and even software. 


How to protect your device
--------------------------


Apart from upgrading your Dahua camera to the latest available firmware version for your model, you should also change the password it came with out of the box with something unique and strong. Leaving the root access credentials to “admin” – “admin” is a sure way to having your video feeds exposed sooner or later. 


Additionally, enable WPA2 encryption if the camera is wireless, and set up a separate, isolated network for your IoTs if possible. 


Note that if your model is cloud-enabled, you can fetch the fixing upgrade automatically from the control interface, instead of visiting the [Dahua download center](https://www.dahuasecurity.com/support/downloadCenter). 


The discovery of the two flaws came on June 13, 2021, so some Dahua cameras remained vulnerable to unauthenticated access for at least 2.5 months, even for owners who applied the firmware update as soon as it came out.




#### Tags:
[[Dahua]] [[Bleeping Computer]]
