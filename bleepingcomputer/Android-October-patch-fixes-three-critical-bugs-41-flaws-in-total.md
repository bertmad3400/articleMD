# Android October patch fixes three critical bugs, 41 flaws in total
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/android-october-patch-fixes-three-critical-bugs-41-flaws-in-total/)
+ Date: October 5, 2021
+ Author: Bill Toulas


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/05/06/Android.jpg?rand=769531342)


Google has released the Android October security updates, addressing 41 vulnerabilities, all ranging between high and critical severity.


On the 5th of each month, Google releases the complete security patch for the Android OS which contains both the framework and the vendor fixes for that month. As such, this update also incorporates fixes for the 10 vulnerabilities that were addressed in the Security patch level 2021-10-01, released a couple of days back. 


The high-severity flaws fixed this month concern denial of service, elevation of privilege, remote code execution, and information disclosure issues.


The three critical severity flaws in the set are tracked as:


* **CVE-2021-0870**: Remote code execution flaw in Android System, enabling a remote attacker to execute arbitrary code within the context of a privileged process.
* **CVE-2020-11264**: Critical flaw affecting Qualcomm’s WLAN component, concerning the acceptance of non-EAPOL/WAPI frames from unauthorized peers received in the IPA exception path.
* **CVE-2020-11301**: Critical flaw affecting Qualcomm’s WLAN component, concerning the acceptance of unencrypted (plaintext) frames on secure networks.


Critical but unexploited
------------------------


None of the [41 flaws addressed this month](https://source.android.com/security/bulletin/2021-10-01) have been reported to be under active exploitation in the wild, so there should be no working exploits for them circulating out there.


Older devices that are no longer supported with security updates now have an increased attack surface, as some of the vulnerabilities fixed this month are excellent candidates for threat actors to create working exploits in the future.


Remember, Android security patches aren’t bound to Android versions, and the above fixes concern all versions from Android 8.1 to Android 11. As such, the OS version isn’t a determining factor in whether or not your device is still supported.


If you have confirmed that your device has reached the EOL date, you should either install a third-party Android distribution that still delivers monthly security patches for your model, or replace it with a new one.


Android fans have been eagerly waiting for the release of version 12, which was rumored for October 4, 2021, but what they got instead was the [source of Android 12 pushed to the Android Open Source Project](https://android-developers.googleblog.com/2021/10/android-12-is-live-in-aosp.html).


This step signifies that the actual release is just around the corner, and OTA upgrade alerts could hit eligible devices, like the Pixel, very soon.




#### Tags:
[[Android]] [[Bleeping Computer]]
