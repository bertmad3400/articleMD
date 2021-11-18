# Ransomware Phishing Emails Sneak Through SEGs
### The MICROP ransomware spreads via Google Drive and locally stored passwords.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176470)
+ Date: November 18, 2021  4:45 pm
+ Author: Becky Bracken


## Article:
Secure email gateway (SEG) protections aren’t necessarily enough to stop phishing emails from delivering ransomware to employees, especially if the cybercrooks are using legitimate cloud services to host malicious pages.


Researchers are raising the alarm over a phishing email kicking off a Halloween-themed MICROP ransomware offensive, which they observed making its way to a target’s [inbox despite its being secured by an SEG](https://cofensestaging.wpengine.com/blog/spooky-ransomware-past-segs/).


Infection Routine
-----------------


The original email purported to need support for a “DWG following Supplies List,” which is supposedly hyperlinked to a Google Drive URL. The URL is actually an infection link, which downloaded an .MHT file.


“.MHT file extensions are commonly used by web browsers as a webpage archive,” Cofense researchers explained. “After opening the file the target is presented with a blurred out and apparently stamped form, but the threat actor is using the .MHT file to reach out to the malware payload.”


That payload comes in the form of a downloaded .RAR file, which in turn contains an .EXE file.


“The executable is a DotNETLoader that uses VBS scripts to drop and run the MIRCOP ransomware in memory,” according to the analysis.


The campaign is not particularly sophisticated, but the use of Google Drive allowed it to get past SEGs.


“Its opening lure is business-themed, making use of a service – such as Google Drive – that enterprises employ for delivering files,” the researchers explained. “The rapid deployment from the MHT payload to final encryption shows that this group is not concerned with being sneaky. Since the delivery of this ransomware is so simple, it is especially worrying that this email found its way into the inbox of an environment using a SEG.”


The recipient of this Halloween MICROP reported the email as suspicious, leading Cofense to discover the potential new threat.


A Gory Theme, Unusual Use of Skype
----------------------------------


“The MIRCOP ransomware, also known as Crypt888 ransomware, encrypts users’ files to hold them hostage,” a Cofense analysts reported. “After the payment demand is met, the threat actor promises to provide the decryption method. For this attack, the threat actor gives a set of instructions on the wallpaper.”


![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/18153414/wallpaper.png)


The user is also unable to open any applications besides a few web browsers that can give them access to their email address which is used to contact the attacker,” Cofense researchers wrote in a [recent posting](https://cofensestaging.wpengine.com/blog/spooky-ransomware-past-segs/). “The email address is then used to set up the payment required to gain access to the decrypting tool the threat actor claims will unlock the files and applications.”


They added, “The use of Skype as a medium to negotiate is uncommon, as most organized ransomware gangs have dedicated sites or mobile chat apps.”


**Watch Locally Stored Passwords**
----------------------------------


The other interesting aspect of this campaign is a malicious file observed by the Cofense team, named “PI2.exe.” It steals passwords from web browsers including Explorer, Google Chrome, Firefox and Opera, giving the threat actors both lateral access around the network, as well as an entry point for future attacks.


“Looking up the SHA256 hash of this executable on Virus Total, it can be linked to dozens of malicious executables going back to June of this year,” researchers said.


This “tool” indicates that the shift to working outside the office just further exposes business to these kinds of attacks, according to Miclain Keffeler, an application security consultant with nVisium, which is why [local password management](https://threatpost.com/) as well as [reining in cloud permissions](https://threatpost.com/webinars/multi-cloud-security-and-visibility-an-intro-to-osquery-and-cloudquery/) is increasingly imperative, he explained to Threatpost.


“Crypt888 seeks horizontal privilege escalation by stealing passwords that users may have saved locally — inevitably to be used in other ways that could wreak havoc on a business,” Keffeler said. “As the cloud continues to grow, these saved passwords become a key attack vector as they can often grant large amounts of access — with little to no security controls.”


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” an on-demand Town Hall with Eric Kaiser, Uptycs’ senior security engineer, and find out how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://bit.ly/3wf2vTP)**to access the on-demand event!**




#### Tags:
[[ransomware]] [[Cofense]] [[“The]] [[Google]] [[cloud]] [[ThreatPost]]
