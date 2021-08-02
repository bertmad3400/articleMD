# Microsoft: Watch out for this 'sneakier than usual' phishing attack
### Microsoft issues an alert over a 'crafty' phishing campaign.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-watch-out-for-this-sneakier-than-usual-phishing-attack/)
+ Date: August 2, 2021 -- 12:14 GMT (13:14 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft's Security Intelligence team has issued an alert to Office 365 users and admins to be on the lookout for a "crafty" phishing email with spoofed sender addresses. 


Microsoft put out an alert after observing an active campaign targeting Office 365 organizations with convincing emails and several techniques to bypass phishing detection, including an Office 365 phishing page, Google cloud web app hosting, and a compromised SharePoint site that urges victims to type in their credentials. 

**SEE:** [**Network security policy**](https://www.techrepublic.com/resource-library/whitepapers/network-security-policy/?ftag=CMG-01-10aaa1b) **(TechRepublic Premium)**

"An active phishing campaign is using a crafty combination of legitimate-looking original sender email addresses, spoofed display sender addresses that contain the target usernames and domains, and display names that mimic legitimate services to try and slip through email filters," the Microsoft Security Intelligence team [said in an update](https://twitter.com/MsftSecIntel/status/1421232634357714947).  

"The original sender addresses contain variations of the word "referral" and use various top-level domains, including the domain com[.]com, popularly used by phishing campaigns for spoofing and typo-squatting."




> The emails use a SharePoint lure in the display name as well as in the message, which poses as a "file share" request for supposed "Staff Reports", "Bonuses", "Pricebooks", and other content, with a link that navigates to the phishing page. [pic.twitter.com/c33awiAeH4](https://t.co/c33awiAeH4)
> 
> — Microsoft Security Intelligence (@MsftSecIntel) [July 30, 2021](https://twitter.com/MsftSecIntel/status/1421232638992347139?ref_src=twsrc%5Etfw)




Phishing continues to be a tricky problem for businesses to stamp out, [requiring regularly updated phishing awareness training](https://www.zdnet.com/article/phishing-awareness-training-wears-off-after-a-few-months/) and technical solutions, such [as multi-factor authentication on all accounts](https://www.zdnet.com/article/multi-factor-authentication-use-it-for-all-the-people-that-access-your-network-all-the-time/) – which [both Microsoft and CISA](https://www.zdnet.com/article/kaseya-ransomware-attack-us-launches-investigation-as-gang-demands-giant-70-million-payment/) highly recommend. 

Phishing is a key component of business email compromise (BEC) attacks, which cost [Americans more than $4.2 billion last year, according to the FBI's latest figures](https://www.zdnet.com/article/microsoft-disrupted-this-large-cloud-based-business-email-scam-operation/). It's far more costly than high-profile ransomware attacks. BEC, which relies on compromised email accounts or email addresses that are similar to legitimate ones, are difficult to filter as they blend within normal, expected traffic.   






The phishing group is using Microsoft SharePoint in the display name to entice victims to click the link. The email poses as a "file share" request to access bogus "Staff Reports", "Bonuses", "Pricebooks", and other content hosted in a supposed Excel spreadsheet. It also contains a link that navigates to the phishing page and plenty of Microsoft branding.

While convincing Microsoft logos are littered across the email, the main phishing URL relies on a Google storage resource that points the victim to the Google App Engine domain AppSpot – a place to host web applications.

"The emails contain two URLs that have malformed HTTP headers. The primary phishing URL is a Google storage resource that points to an AppSpot domain that requires the user to sign in before finally serving another Google User Content domain with an Office 365 phishing page," Microsoft notes. 

**SEE:**[**Ransomware: Paying up won't stop you from getting hit again, says cybersecurity chief**](https://www.zdnet.com/article/ransomware-paying-up-wont-stop-you-from-getting-hit-again-says-cybersecurity-chief/#link=%7B%22linkText%22:%22Ransomware:%20Paying%20up%20won't%20stop%20you%20from%20getting%20hit%20again,%20says%20cybersecurity%20chief%22,%22target%22:%22_blank%22,%22href%22:%22https://www.zdnet.com/article/ransomware-paying-up-wont-stop-you-from-getting-hit-again-says-cybersecurity-chief/%22,%22role%22:%22standard%22,%22absolute%22:%22%22%7D)

The second URL is embedded in the notifications settings links the victim to a compromised SharePoint site. Both URLs require sign-in to get to the final page, allowing the attack to bypass sandboxes. 

This campaign is "sneakier than usual", Microsoft notes.  

Microsoft has been touting its 'Safe Links' Defender for Office 365 phishing protection feature [that 'detonates' phishing email at the point a user clicks on a link](https://www.zdnet.com/article/microsoft-teams-just-got-this-new-protection-against-phishing-attacks/) that matches its list of known phishing pages. 

Microsoft has also [published details on GitHub](https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries/blob/master/Email%20Queries/referral-phish-emails.md) about the infrastructure linked to the spoofed emails imitating SharePoint and other products for credential phishing. 

"The operator is also known to use legitimate URL infrastructure such as Google, Microsoft, and Digital Ocean to host their phishing pages," Microsoft notes. 





#### Tags:
[[phishing]] [[Microsoft]] [[Google]] [[SharePoint]] [[emails]] [[URL]] [[notes.]] [[ZDNet]]
