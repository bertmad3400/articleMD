# Gmail deploys support BIMI security standard
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/gmail-deploys-support-bimi-security-standard/)
+ Date: July 12, 2021
+ Author: Catalin Cimpanu


## Article:
![Gmail deploys support BIMI security standard](https://therecord.media/wp-content/uploads/2021/07/Gmail.png)

Google has rolled out today support for the new Brand Indicators for Message Identification ([BIMI](https://bimigroup.org/)) standard to all Gmail users as part of an effort to improve email-sender authenticity.


The new standard is hard to comprehend for non-technical users, but it basically allows companies that have implemented email security standards like DMARC, DKIM, and SPF for their email domains to show “authenticated logos” inside email clients.


Since all these security protocols rely on digital certificates and advanced cryptography, the verified logos will only appear for a company’s real email domain and not for spoofed emails sent by scammers or cybercrime groups.


A high-level technical explanation of how BIMI works is available below:


Organizations who authenticate their emails using Sender Policy Framework (SPF) or Domain Keys Identified Mail (DKIM) and deploy DMARC can provide their validated trademarked logos to Google via a Verified Mark Certificate (VMC). BIMI leverages Mark Verifying Authorities, like Certification Authorities, to verify logo ownership and provide proof of verification in a VMC. Once these authenticated emails pass our other anti-abuse checks, Gmail will start displaying the logo in the existing avatar slot.   
  
If companies have implemented SFP, DKIM, DMARC, and have obtained a VMC, they can add a verified logo for all emails sent from their domains by adding a special DMARC DNS record that looks like below and points to a logo URL:   
  
**default.\_bimi TXT “v=BIMI1; l=https://mydomain.com/image.svg;”**


Google had first rolled out BIMI in [a trial last](https://cloud.google.com/blog/products/g-suite/gsuite-security-updates-for-gmail-meet-chat-and-admin) year for a small group of users.


With today’s [announcement](https://cloud.google.com/blog/products/identity-security/bringing-bimi-to-gmail-in-google-workspace), Gmail now joins Yahoo, AOL, and Fastmail as the only email providers to support BIMI-authenticated logos inside their email clients.


Besides the security benefits of having authenticated logos appear next to emails, the BIMI standard also has tangible marketing benefits as well.


According to a 2018 trial with Yahoo users, Verizon said that after adding verified logos next to inbox emails, they saw a 10% increase in customer engagements, as users tended to click on emails with a logo more often, driving traffic to companies which tested the technology.





But as with all new technologies and standards being rolled out, there are also technical hurdles. In the case of BIMI, these hurdles are related to VMCs, the special certificates that companies need to authenticate their logo ownership.


Today, only [DigiCert](https://www.digicert.com/tls-ssl/verified-mark-certificates)and [Entrust](https://www.entrust.com/digital-security/certificate-solutions/products/digital-certificates/verified-mark-certificates) can issue VMCs for BIMI authentication, but in a [press release](https://bimigroup.org/bimi-working-group-announces-gmail-general-availability-of-bimi/), the BIMI team said they expect the list of supporting Certification Authorities to expand in the future.


Below is an animated GIF with how BIMI authenticated logos are expected to look inside Gmail once the standard deploys to the company’s more than two billion users.


![BIMI](https://therecord.media/wp-content/uploads/2021/07/BIMI.gif)Image: Google



#### Tags:
[[BIMI]] [[emails]] [[Google]] [[Gmail]] [[DMARC]] [[DKIM]] [[VMC]] [[The Record]]
