# Axis releases updates for three new vulnerabilities found by security company
### Axis has released firmware updates for all of the vulnerabilities after being notified in June.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/axis-releases-updates-for-three-new-vulnerabilities-found-by-security-company/)
+ Date: October 5, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Nozomi Networks Labs [unveiled](https://www.nozominetworks.com/blog/new-axis-os-security-research-aided-by-transparent-design/) three different vulnerabilities in video recording device software from Axis. Axis has already released firmware updates addressing each issue after being notified about the vulnerabilities in June. 

The issues affected Axis OS Active track 10.7, Axis OS 2016 LTS track 6.50.5.5, Axis OS 2018 LTS track 8.40.4.3, Axis OS 2020 LTS track 9.80.3.5, Axis OS Active track 10.8, Axis OS 2016 LTS track 6.50.5.5, Axis OS 2018 LTS track 8.40.4.3 and Axis OS 2020 LTS track 9.80.3.5.

Axis is a billion-dollar company with offices in more than 50 countries and systems in iconic locations like the White House, Sydney Airport, the Moscow Metro, the Madrid bus system and the City of Houston. 

Researchers with Nozomi Networks Labs bought an Axis Companion Recorder and sought to investigate the cybersecurity features of the equipment. 

They discovered a heap-based buffer overflow (CVE-2021-31986, CVSSv3 6.7), improper recipient validation in network test functionalities (CVE-2021-31987, CVSSv3 4.1) and SMTP header injection in email test functionality (CVE-2021-31988, CVSSv3 5.5).

The researchers found the heap-based buffer overflow vulnerability in the read callback function, which "failed to verify that no more than 'size' multiplied with 'items' number of bytes are copied in the libcurl destination buffer."

They found that the parameters provided are "externally controllable and were insufficiently validated by the server-side code prior to reaching the read callback function."






CVE-2021-31987 is related to the test functions of HTTP, email and TCP recipients, which have blocklist-based security checks to impede interactions with localhost-exposed network services. Nozomi Networks Labs researchers found that this could be circumvented with known bypasses or were incomplete.

"By convincing a victim user into visiting a specifically crafted webpage while logged-in to the Companion Recorder web application, an external remote attacker can interact with internal-only services running on the device, obtaining access to restricted information," the security company wrote. 

"The third vulnerability is due to an SMTP header injection, located in the SMTP test function. By convincing a victim user into visiting a specifically crafted webpage while logged-in to the Companion Recorder web application, an external remote attacker can trick the device into sending malicious emails to other users with arbitrary SMTP header values. This can be abused to perform phishing attacks, spread malware via emails, or disclose internal information."

CVE-2021-31986 and CVE-2021-31988 affect Axis OS Active track 10.7, Axis OS 2016 LTS track 6.50.5.5, Axis OS 2018 LTS track 8.40.4.3, Axis OS 2020 LTS track 9.80.3.5. 

CVE-2021-31987 is found in Axis OS Active track 10.8, Axis OS 2016 LTS track 6.50.5.5, Axis OS 2018 LTS track 8.40.4.3 and Axis OS 2020 LTS track 9.80.3.5.

After Nozomi Networks Labs contacted Axis with the issues in June, the company confirmed them in July and worked with the researchers to verify the firmware updates. 

Nozomi Networks Labs said some devices are not included and will "receive a patch according to their planned maintenance & release schedule."





#### Tags:
[[LTS]] [[Nozomi]] [[SMTP]] [[CVSSv3]] [[ZDNet]]
