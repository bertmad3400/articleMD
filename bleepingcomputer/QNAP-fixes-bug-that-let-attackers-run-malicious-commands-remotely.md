# QNAP fixes bug that let attackers run malicious commands remotely
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/qnap-fixes-bug-that-let-attackers-run-malicious-commands-remotely/)
+ Date: September 30, 2021
+ Author: Sergiu Gatlan


## Article:
![QNAP fixes bugs that let attackers run malicious code remotely](https://www.bleepstatic.com/content/hl-images/2021/09/30/QNAP.jpg)


Taiwan-based network-attached storage (NAS) maker QNAP has released security patches for multiple vulnerabilities that could allow attackers to inject and execute malicious code and commands remotely on vulnerable NAS devices.


Three of the security flaws fixed today by QNAP are high severity [stored cross-site scripting](https://owasp.org/www-community/attacks/xss/#stored-xss-attacks) (XSS) vulnerabilities (tracked as CVE-2021-34354, CVE-2021-34356, and CVE-2021-34355) affect devices running unpatched Photo Station software (releases before 5.4.10, 5.7.13, or 6.0.18).


QNAP also patched a stored XSS Image2PDF flaw impacting devices running software versions released before Image2PDF 2.1.5.


[Stored XSS attacks](https://owasp.org/www-community/attacks/xss/#stored-xss-attacks) allow threat actors to inject malicious code remotely, permanently storing it on the targeted servers following successful exploitation.


The company also addressed a [command injection](https://capec.mitre.org/data/definitions/88.html) bug (CVE-2021-34352) affecting some QNAP end-of-life (EOL) devices running the QVR IP video surveillance software that helps attackers run arbitrary commands.


Successful attacks exploiting the CVE-2021-34352 flaw could lead to the complete takeover of compromised NAS devices.


Three other QVR flaws were [also patched on Monday](https://www.bleepingcomputer.com/news/security/qnap-fixes-critical-bugs-in-qvr-video-surveillance-solution/), as disclosed by QNAP in a security advisory rated with a critical severity rating.


How to secure your NAS device
-----------------------------


Given that QNAP NAS devices have been under a [constant barrage of attacks](https://www.bleepingcomputer.com/tag/qnap/) the last couple of years, customers should immediately update both apps to the latest available releases as soon as possible.


To update Photo Station or Image2PDF to the latest version on your NAS, you need to go through the following procedure:


1. Log into QTS or QuTS hero as administrator.
2. Open the **App Center**, and then click ![](https://www.qnap.com/i/_upload/support/images/magnifier.png). A search box appears.
3. Type "Photo Station" or "Image2PDF" and then press **ENTER**. The application appears in the search results.
4. Click **Update**. A confirmation message appears. **Note:** The **Update** button is not available if you are using the latest version.
5. Click **OK**. The application is updated.


 To update the QVR surveillance software, follow these steps:


1. Log on to QVR as administrator.
2. Go to **Control Panel** > **System Settings** > **Firmware Update**.
3. Under **Live Update**, click **Check for Update**. QVR downloads and installs the latest available update.


QNAP warned in September 2020 of a [surge in ransomware attacks](https://www.bleepingcomputer.com/news/security/qnap-warns-customers-of-recent-wave-of-ransomware-attacks/) encrypting files on publicly exposed NAS storage devices.


As [BleepingComputer reported](https://www.bleepingcomputer.com/news/security/agelocker-ransomware-targets-qnap-nas-devices-steals-data/) at the time, QNAP customers' devices were being hit by AgeLocker ransomware which was targeting older unpatched versions of Photo Station, an app used to upload photos, create albums, and view them remotely.


QNAP also [warned of eCh0raix ransomware attacks](https://www.bleepingcomputer.com/news/security/ongoing-ech0raix-ransomware-campaign-targets-qnap-nas-devices/) attempting to exploit flaws in the Photo Station app starting with June 2020.




#### Tags:
[[QNAP]] [[NAS]] [[QVR]] [[devices.]] [[Image2PDF]] [[Update.]] [[ransomware]] [[Bleeping Computer]]
