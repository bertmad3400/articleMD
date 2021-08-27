# Windows 10 upgrades blocked by old CryptoPro SCP versions
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-10-upgrades-blocked-by-old-cryptopro-scp-versions/)
+ Date: August 27, 2021
+ Author: Sergiu Gatlan


## Article:
![Windows 10 upgrades blocked by old CryptoPro SCP versions](https://www.bleepstatic.com/content/posts/2021/08/27/Windows-10.jpg)


Microsoft has applied a compatibility hold on systems running older versions of CryptoPro CSP, blocking them from being offered or installing Windows 10, version 2004 or later.


Luckily, [CryptoPro CSP](https://www.cryptopro.ru/products/csp) is a software solution developed by a Russian company according to tech specifications agreed with the country's Federal Security Service (FSB), which drastically lowers the number of Windows users potentially affected by this safeguard.



It loads libraries for the [Russian GOST cryptographic algorithm](https://en.wikipedia.org/wiki/GOST_(block_cipher)) to encrypt Internet connections in office suites, web browsers, and other software, and for authorization via electronic signature on Russian government portals.


Upgrades blocked due to compatibility issue
-------------------------------------------


"A compatibility issue has been found between older versions of омпаниякриптопр риптопроcsp [CryptoPro CSP] and Windows 10, version 20H1 or Windows 10, version 2004," Microsoft [says](https://support.microsoft.com/en-us/topic/kb5006024-updating-to-windows-10-version-2004-or-a-later-version-with-a-certain-app-installed-df42c4e1-bdc1-4d92-b972-47ed13546784) in a newly published support article.


"If an incompatible version of омпаниякриптопр риптопроcsp is installed, your device might start to update to a later version of Windows 10 but might roll back to a previously installed version."


Customers who run an older CryptoPro CSP version on a computer running Windows 10 2004 or later will be blocked from upgrading their systems and prompted to uninstall the app due to compatibility issues.


The Windows 10 Setup screen will also display this message: "The following things need your attention to continue the installation and keep your windows settings, personal files, and apps."


Microsoft has applied this compatibility hold to prevent issues that could directly impact the customers' user experience.



![CryptoPro CSP safeguard hold message](https://www.bleepstatic.com/images/news/u/1109292/2021/CryptoPro%20CSP%20safeguard%20hold%20message.png)*Image: Microsoft*
Uninstall or upgrade CryptoPro CSP as a workaround
--------------------------------------------------


Microsoft also provides a workaround to allow users of impacted systems to update their computers to the latest Windows 10 version.


"To mitigate the safeguard, you must install the latest version of CryptoPro CSP which should be compatible with Windows 10, version 20H1 and Windows 10, version 2004," Microsoft says.


After you have updated the app to the latest version, you should be able once again to update your system to a later version of Windows 10. 


It can require up to 48 hours before a Windows 10 2004 or 20H2 update is offered through Windows Update if no other safeguards are affecting your device.


If you can't immediately update the CryptoPro CSP app, you can still [manually force upgrade it to Windows 10 2004](https://www.bleepingcomputer.com/news/microsoft/windows-10-2004-update-not-offered-heres-how-to-get-it-now/) using the Media Creation Tool, the Windows 10 Upgrade Assistant, or a Windows 10 2004 ISO.


You can use this [guided walk-through](https://support.microsoft.com/en-us/help/10164/fix-windows-update-errors) or this [update problems troubleshooter](https://support.microsoft.com/help/4089834) to get around any update installation issues.


However, you should know that manually updating by circumventing upgrade blocks could make your Windows 10 device unusable.




#### Tags:
[[Windows]] [[Microsoft]] [[CryptoPro]] [[Bleeping Computer]]
