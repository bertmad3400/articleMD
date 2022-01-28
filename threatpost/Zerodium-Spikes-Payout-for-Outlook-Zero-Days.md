# Zerodium Spikes Payout for Outlook Zero-Days
### The sweetened deal came on the same day that Trustwave SpiderLabs published a new way to bypass Outlook security to deliver malicious links to victims.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178089
+ Date: 2022-01-28T16:54:06+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/28114907/MicrosoftOutlook-scaled-e1643388571356.jpeg)

Zerodium has jacked up its offering price for Microsoft Outlook zero-day exploits.


Act fast if you have the goods and the moral equanimity to make up to $400,000 for a zero-click, remote-code execution (RCE) exploit.


The price spike is only temporary, with the end date still to be determined, according to a Thursday [post](https://zerodium.com/temporary.html) from Zerodium: runner of high-end, high-dollar, third-party bug-bounty programs.



> “We are temporarily increasing our payout for Microsoft Outlook RCEs from $250,000 to $400,000. We are looking for zero-click exploits leading to remote code execution when receiving/downloading emails in Outlook, without requiring any user interaction such as reading the malicious email message or opening an attachment. Exploits relying on opening/reading an email may be acquired for a lower reward.” –Zerodium
> 
> 


As well, Zerodium has increased payout to $200,000 for zero-click, RCE exploits affecting the Mozilla Thunderbird browser.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Similar to the Outlook exploits it’s hunting for, Zerodium is looking for zero-click exploits that can achieve RCE in Thunderbird when targets are receiving or downloading emails, all without users having to lift a finger.




“[Zero-click](https://threatpost.com/pegasus-spyware-uses-iphone-zero-click-imessage-zero-day/168899/)” means that targets neither have to read a malicious email message nor open a rigged attachment. Zerodium said that it might still want to purchase those “they need to click” exploits, too – that is, for a lower price.


The Trigger
-----------


Zerodium’s newly keen zeal for Outlook exploits came on the same day that Trustwave SpiderLabs [published](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/cve-2020-0696-microsoft-outlook-security-feature-bypass-vulnerability/) details about a new way to bypass an Outlook security feature to deliver malicious links to victims.


As SpiderLabs lead threat architect Reegun Richard Jayapaul explained yesterday, he discovered the issue after coming across several emails bypassing the email security system while he was investigating a malware campaign. He didn’t see any bypass techniques being used, though. “Instead, the flood of spear-phishing emails made the email security system allow some of the emails, at which point I began my research on Microsoft Outlook,” he wrote.


SpiderLabs found that the specially crafted malicious link parsing on the security system was weak. “This is not about detection bypass; it is more about the link parser of the email security systems that cannot identify the emails containing the link,” Jayapaul said.


It turns out that SpiderLabs found a variation of a vulnerability, tracked as CVE-2020-0696, that Microsoft initially [dealt with](https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2020-0696) in February 2020.


The security feature bypass vulnerability occurs in Microsoft Outlook when it improperly handles the parsing of URI formats. Successful exploitation requires an attacker to use the bypass in conjunction with another vulnerability, such as a RCE vulnerability, before they could run arbitrary code.


Because of improper hyperlink translation, the initial Outlook security feature bypass allowed an attacker using Outlook for Mac to completely bypass Outlook’s email security systems and send a clickable, malicious link – SpiderLabs used the example below – to a victim on Outlook for Windows.


http://trustwave[.]com with hyperlinked file:///malciouslink


The maliciously crafted link initially only seemed to work if the attacker uses Microsoft Outlook for Mac and their intended victim is on Microsoft Outlook for Windows.


Exploitable on Windows and Mac Outlook Clients
----------------------------------------------


However, as SpiderLabs researchers later came to find out, the vulnerability can be exploited on both Windows and macOS Outlook client if a legitimate link is hyperlinked with “http:/://maliciouslink.”Jayapaul explained that the email system strips out the “:/” characters and deliver the link as “http://maliciouslink,” bypassing [Microsoft ATP Safelink](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-links?view=o365-worldwide) and other email security products.


“As per the CVE-2020-0696 patch, links with URI schemes will alert as a warning popup; also ‘:/’ characters are stripped when delivered to users,” the researcher explained – an SpiderLabs had originally found that when sending the http://trustwave[.]com with hyperlinked file:///malciouslink vector with hyperlink file:///trustwave.com, the email is delivered on the victim’s’ Microsoft Outlook for Windows’ as file:///trustwave.com,” SpiderLabs explained. “The link file:///trustwave.com then translates to http://trustwave.com after clicking.


“During this transmission from sender to receiver, the link file:///trustwave.com is not recognized by any email security systems and is delivered to the victim as a clickable link.”


The initial test was done on Microsoft M365 security feature “Safelink protection” and later tested and confirmed on multiple email security systems, SpiderLabs confirmed.


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Spiderlabs]] [[Zerodium]] [[Emails]] [[Windows]] [[Zero-click]] [[Rce]] [[Hyperlinked]] [[File:///trustwave.com]] [[ThreatPost]]
#### urls
http://trustwave.com file:///malciouslink http:/://maliciouslink.”Jayapaul http://maliciouslink,” file:///trustwave.com, file:///trustwave.com,” file:///trustwave.com http://trustwave.com
#### CVE's
[[CVE-2020-0696]]

