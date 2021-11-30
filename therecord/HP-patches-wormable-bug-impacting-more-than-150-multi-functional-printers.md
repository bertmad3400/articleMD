# HP patches wormable bug impacting more than 150 multi-functional printers
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/hp-patches-wormable-bug-impacting-more-than-150-multi-functional-printers/)
+ Date: November 30, 2021
+ Author: Catalin Cimpanu


## Article:
![HP patches wormable bug impacting more than 150 multi-functional printers](https://therecord.media/wp-content/uploads/2021/07/HP-printer.jpg)

* Security firm F-Secure finds two security flaws in HP printers, including one that can be used for wormable attacks.
* HP has released security updates for more than 150 multi-functional printers on November 1, 2021.
* Impacted models include the HP LaserJet, PageWide, and ScanJet lines.


Hewlett Packard has released security updates earlier this month to address a vulnerability that impacts more than 150 models from the company’s line of multi-functional printers.


Tracked as CVE-2021-39238, the vulnerability can be used to create wormable exploits that can self-replicate and spread to other HP printers inside internal networks or over the internet.


Discovered earlier this year by Alexander Bolshev and Timo Hirvonen, two security researchers at Finish security firm F-Secure, a [patch](https://support.hp.com/us-en/document/ish_5000383-5000409-16/hpsbpi03749) was made available on the HP website on November 1.


Bolshev and Hirvonen described the issue as a buffer overflow in the printer’s font parser. They say exploit code can abuse this buffer overflow to gain control over a printer’s firmware to steal data or assemble devices into botnets, all while leaving little evidence of exploitation behind.


The F-Secure team said that attacks that abuse CVE-2021-39238 could be mounted in various ways, such as attacking internet-exposed devices or by loading the exploit code on a website or inside an ad. Users on corporate networks, or those who view the ad, will have the code reach out to ports on their internal network in order to exploit local HP printers.


![HP-attack](https://www-therecord.recfut.com/wp-content/uploads/2021/11/HP-attack.png)Image: F-Secure
Furthermore, the malicious code can also be loaded on a USB drive that gets plugged into an HP printer to print documents or inside PDF files sent to a targeted company’s employees.


### A second HP bug is harder to exploit


In addition, Bolshev and Hirvonen said they discovered [a second bug](https://support.hp.com/us-en/document/ish_5000124-5000148-16/hpsbpi03748), tracked as CVE-2021-39237, which impacts the printer’s communications board.


Luckily, this bug can only be exploited with physical access to a vulnerable device, and an attack takes up to five minutes to execute, compared to the first one, which only takes a few seconds.


While the F-Secure researchers say the two vulnerabilities require some technical skills to exploit, the two bugs can be very attractive to attackers.


“These vulnerabilities give attackers an effective way to steal information: defenders are unlikely to proactively examine the security of a printer, and so the attacker can simply sit back and steal whatever information it comes across (via employees printing, scanning, etc),” Bolshev and Hirvonen said.


“They could also use the MFP as a pivot point to move through the corporate network. Because there are no decent tools to perform forensics on embedded devices, this would make it easy for an attacker to infiltrate an organization and accomplish their goals without leaving evidence that would lead back to the MFP.”


### HP LaserJet, PageWide, and ScanJet printers impacted


F-Secure said it hasn’t seen any threat actors exploiting the two vulnerabilities so far and recommended that companies apply the two HP patches released earlier this month.


Models listed as vulnerable include some of HP’s top-shelf products such as its LaserJet, PageWide, and ScanJet lines.


According to [Statista](https://www.statista.com/statistics/541347/worldwide-printer-market-vendor-shares/), HP is currently the world’s largest printer vendor with a market share of almost 25%.


![Printer-market-share](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Printer-market-share.png)Image: Statista



#### Tags:
[[F-Secure]] [[Bolshev]] [[LaserJet,]] [[PageWide,]] [[ScanJet]] [[Hirvonen]] [[printer’s]] [[The Record]]
