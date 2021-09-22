# This phishing-as-a-service operation is responsible for many attacks against businesses, says Microsoft
### A phishing operation hides in plain sight and turns credential theft into a consumer product.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-phishing-as-a-service-operation-is-responsible-for-many-attacks-against-businesses-says-microsoft/)
+ Date: September 22, 2021
+ Author: Liam Tung


## Article:
Unknown

Microsoft is shining a light on a phishing-as-a-service operation that's selling fake login pages for cloud services like OneDrive that help non-technical cybercriminals steal business user passwords and usernames. 

Phishing kits are nothing new, but this phishing-as-a-service service caught the attention of Microsoft's security teams because it lowers the bar to quality phishing even more. 


That business, called BulletProofLink and a few other names, provides email and web site templates as phishing kits do, but also offers email delivery, hosting services, credential theft. It also claims to provide 'fully undetected' (FUD) links and logs and is available for purchase as a weekly, bi-weekly, monthly, or annual subscription. 

**SEE:** [**Half of businesses can't spot these signs of insider cybersecurity threats**](https://www.zdnet.com/article/half-of-businesses-cant-spot-these-signs-of-insider-cybersecurity-threats/)

As Microsoft outlines, phishing service providers are one link in the chain that can help ransomware gangs unload file-encrypting ransomware pain on targets, chiefly by providing passwords to attackers who can try them out on compromised networks. If the ransomware buyer is lucky, the credentials can include passwords for high-value admin accounts, allowing for greater movement within a compromised network. 

"These [FUD] phishing service providers host the links and pages and attackers who pay for these services simply receive the stolen credentials later on. Unlike in certain ransomware operations, attackers do not gain access to devices directly and instead simply receive untested stolen credentials," [the Microsoft 365 Defender Threat Intelligence Team notes in a blogpost](https://www.microsoft.com/security/blog/2021/09/21/catching-the-big-fish-analyzing-a-large-scale-phishing-as-a-service-operation/).   

Microsoft is concerned about businesses like these because they offer dozens of templates for the login pages of popular web services and allow anyone on a small budget to beat a path to theft or extortion. It currently offers "login scam" pages for Microsoft OneDrive, LinkedIn, Adobe, Alibaba, American Express, AOL, AT&T, Dropbox, and Google Docs. 






It's also worried about "double theft", where the phishing service provider captures the credentials on behalf of one customer and then sells the credentials to other customers.

BulletProofLink markets itself openly on the web and on underground forums, and is also known as BulletProftLink or Anthrax. It's even published 'how-to' videos on YouTube and Vimeo to help customers use its fraud tools. 

Microsoft published its research into this operation to help customers refine email-filtering rules and adopt security technologies it offers. While phishing kits are sold once in a ZIP file with phishing templates to set up a bogus login page or emails, phishing-as-a-service includes the whole package. 

The company caught Microsoft's attention while it was investigating a phishing campaign that was using BulletProofLink services. The campaign used a whopping 300,000 subdomains with a technique Microsoft calls "infinite subdomain abuse", which is where an attacker has compromised a website's domain name system server (DNS) or when a compromised site is configured with a DNS that allows wildcard subdomains.


These subdomains "allow attackers to use a unique URL for each recipient while only having to purchase or compromise one domain for weeks on end", Microsoft says. They're useful before the attacker can simply compromise the DNS of a site and not bother with hacking the site itself. It also allows phishing businesses to create a ton of unique URLs that are hard to detect. 

**SEE:** [**Four months on from a sophisticated cyberattack, Alaska's health department is still recovering**](https://www.zdnet.com/article/four-months-on-from-sophisticated-cyber-attack-alaskas-health-services-is-still-recovering/)

Ransomware service provider models are also influencing how phishing businesses operate. One notable ransomware technique is to steal data before encrypting it and then either sell that data or use it as leverage during extortion attempts. 

"We have observed this same workflow in the economy of stolen credentials in phishing-as-a-service," Microsoft says. 

"With phishing kits, it is trivial for operators to include a secondary location for credentials to be sent to and hope that the purchaser of the phish kit does not alter the code to remove it. This is true for the BulletProofLink phishing kit, and in cases where the attackers using the service received credentials and logs at the end of a week instead of conducting campaigns themselves, the PhaaS operator maintained control of all credentials they resell."   





#### Tags:
[[phishing]] [[Microsoft]] [[ransomware]] [[phishing-as-a-service]] [[BulletProofLink]] [[ZDNet]]
