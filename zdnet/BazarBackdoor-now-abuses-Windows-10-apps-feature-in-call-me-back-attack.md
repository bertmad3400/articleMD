# BazarBackdoor now abuses Windows 10 apps feature in 'call me back' attack
### AppInstaller.exe has been twisted in a new form of phishing attack.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/bazarloader-now-abuses-windows-10-apps-feature-in-call-me-back-attack/)
+ Date: November 11, 2021
+ Author: Charlie Osborne


## Article:
Unknown

A Microsoft Windows 10 app feature is being abused in a new phishing campaign spreading the BazarBackdoor malware. 


On Thursday, researchers from Sophos Labs said the attack was noticed after the cybersecurity firm's [own employees](https://news.sophos.com/en-us/2021/11/11/bazarloader-call-me-back-attack-abuses-windows-10-apps-mechanism/) were targeted with spam emails -- but rather than being run-of-the-mill, these emails were written with at least a basic level of social engineering.

One of the emails, sent by a "Sophos Main Manager Assistant," the non-existent "Adam Williams," demanded to know why a researcher hadn't responded to a customer's complaint. To make resolution easier, the email helpfully contained a .PDF link to the message.  

However, the link was a trap and revealed a "novel" technique used to deploy the BazarBackdoor malware.  

Sophos says that the company is, at the least, "unfamiliar" with this method, in which the Windows 10 App installer process is exploited to deliver malicious payloads.  

This is how it works: the phishing lure will direct potential victims to a website that uses the Adobe brand and asks users to click on a button to preview a .PDF file. However, if you hovered over the link, the prefix "ms-appinstaller" is displayed.  

![screenshot-2021-11-11-at-09-05-50.png]()![screenshot-2021-11-11-at-09-05-50.png](https://www.zdnet.com/a/img/resize/a71efe1409dfc2601ec6a2331705f4e2f72d0705/2021/11/11/1755bb63-668e-4637-97f2-a2504b20524e/screenshot-2021-11-11-at-09-05-50.png?width=1200&fit=bounds&auto=webp)
 Sophos
 "In the course of running through an actual infection I realized that this construction of a URL triggers the browser [in my case, Microsoft's Edge browser on Windows 10], to invoke a tool used by the Windows Store application, called AppInstaller.exe, to download and run whatever's on the other end of that link," Sophos researcher Andrew Brandt explained.  






In turn, this link points to a text file, named Adobe.appinstaller, which then points to a larger file hosted on a separate URL, Adobe\_1.7.0.0\_x64appbundle.  

A warning prompt then appears as well as a notice that the software has been digitally signed with a certificate issued several months ago. (Sophos has made the certificate authority aware of the abuse).  

Victims are then asked to allow the installation of "Adobe PDF Component," and if they grant permission, the BazarBackdoor malware is deployed and executed in a matter of seconds.  

BazarBackdoor, akin to BazarLoader, communicates over HTTPS but is a distinctive malicious program due to the amount of noisy traffic the backdoor generates. BazarBackdoor is able to exfiltrate system data and has been [linked to Trickbot](https://cofense.com/blog/bazarbackdoor-stealthy-infiltration), as well as the potential deployment of Ryuk ransomware.  

"Malware that comes in application installer bundles is not commonly seen in attacks," Brandt said. "Unfortunately, now that the process has been demonstrated, it's likely to attract wider interest. Security companies and software vendors need to have the protection mechanisms in place to detect and block it and prevent the attackers from abusing digital certificates." 

###  Previous and related coverage

* [RotaJakiro: A Linux backdoor that has flown under the radar for years](https://www.zdnet.com/article/rotajakiro-a-linux-backdoor-that-has-flown-under-the-radar-for-years/)
* [Chinese cybercriminals spent three years creating a new backdoor to spy on governments](https://www.zdnet.com/article/chinese-cybercriminals-spent-three-years-creating-a-new-backdoor-to-spy-on-governments/)
* [Tomiris backdoor discovery linked to Sunshuttle, DarkHalo hackers](https://www.zdnet.com/article/the-tomiris-backdoor-has-now-been-linked-to-sunshuttle-darkhalo-hackers/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Windows]] [[BazarBackdoor]] [[Sophos]] [[ZDNet]]
