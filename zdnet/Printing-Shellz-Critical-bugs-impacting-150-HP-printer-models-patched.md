# Printing Shellz: Critical bugs impacting 150 HP printer models patched
### "Cross-site printing attacks" feature in the research.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/printing-shellz-critical-bugs-impacting-150-hp-printers-patched/)
+ Date: November 30, 2021
+ Author: Charlie Osborne


## Article:
Unknown

![screenshot-2021-11-18-at-12-24-33.png](https://www.zdnet.com/a/img/resize/3a8c15744879950cc5fba1dcc466a5d7715a33f2/2021/11/18/34f27153-3810-4fdd-8223-40800769b2c5/screenshot-2021-11-18-at-12-24-33.png?width=1200&fit=bounds&auto=webp)
 F-Secure
 HP has patched critical flaws impacting approximately 150 printer models. 

Printers are usually connected to business networks -- and potentially forgotten when it comes to security -- so they can easily provide an avenue of attack. Highlighting this issue is [PrintNightmare](https://www.zdnet.com/article/microsoft-fixes-windows-10-printnightmare-flaw-with-this-update/), CVE-2021-34481, a Windows Print Spooler service vulnerability that permits attackers to escalate privileges to system level, which was patched in August. In addition, HP patched a separate, 16-year-old privilege escalation [driver flaw in July](https://www.zdnet.com/article/hp-patches-vulnerable-printer-driver-impacting-millions-of-devices/).


**Also:**[**Microsoft just revealed another Print Spooler bug**](https://www.zdnet.com/article/windows-10-microsoft-just-revealed-another-print-spooler-bug/)

Now, researchers from F-Secure have documented "[Printing Shellz](https://labs.f-secure.com/blog/printing-shellz)," a set of vulnerabilities impacting multifunction printers (MFPs).  

On Thursday, the research team said that their tests involved the HP MFP M725z. However, the vulnerabilities -- dating back to 2013 -- impact an estimated 150 products. These include models in the HP Color LaserJet Enterprise, HP LaserJet Enterprise, HP PageWide, HP OfficeJet Enterprise Color, and HP ScanJet Enterprise 8500 FN1 Document Capture Workstation ranges.

The first issue the researchers discovered was [CVE-2021-39238](https://nvd.nist.gov/vuln/detail/CVE-2021-39238). Assigned a CVSS severity score of 9.3, this potential buffer overflow issue could allow the creation of a "self-propagating network worm capable of independently spreading to other vulnerable MFPs on the same network," according to F-Secure researchers Alexander Bolshev and Timo Hirvonen. 

The second issue, [CVE-2021-39237](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-39237) (CVSS 7.1), is described by HP as an information disclosure bug. F-Secure says this flaw was caused by exposed physical ports, so local access is required as an avenue for attack. 






It's possible to exploit these flaws locally via physical access to the device, such as by printing from USB. And when it comes to CVE-2021-39238, another potential attack vector involves sending an exploit payload directly from a browser via cross-site printing (XSP).  

"These vulnerabilities give attackers an effective way to steal information: defenders are unlikely to proactively examine the security of a printer, and so the attacker can simply sit back and steal whatever information it comes across (via employees printing, scanning, etc)," F-Secure comments. "They could also use the MFP as a pivot point to move through the corporate network."

HP was informed of F-Secure's discoveries on April 29 and has since released two advisories ([1](https://support.hp.com/us-en/document/ish_5000383-5000409-16/hpsbpi03749),[2](https://support.hp.com/us-en/document/ish_5000124-5000148-16/hpsbpi03748)), detailing the vulnerabilities. Patches and firmware updates were released in November.

There is no evidence of exploitation in the wild.  

"Any organizations using affected devices should install the patches as soon as they're available," the researchers say. "While exploiting these issues is somewhat difficult, the public disclosure of these vulnerabilities will help threat actors know what to look for to attack vulnerable organizations." 



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[F-Secure]] [[ZDNet]]
