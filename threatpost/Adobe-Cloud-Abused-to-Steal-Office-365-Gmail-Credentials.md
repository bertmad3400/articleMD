# Adobe Cloud Abused to Steal Office 365, Gmail Credentials
### Threat actors are creating accounts within the Adobe Cloud suite and sending images and PDFs that appear legitimate to target Office 365 and Gmail users, researchers from Avanan discovered.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177625
+ Date: 2022-01-13T14:00:54+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/06/29072304/Adobe-Logo.jpg)

Attackers are leveraging Adobe Creative Cloud to target Office 365 users with malicious links that appear to be coming legitimately from Cloud users but instead direct victims to a link that steals their credentials, researchers have discovered.


Researchers from Avanan, a Check Point company, first discovered the ongoing campaign in December when they stopped one of the attacks, according to [a report](https://www.avanan.com/blog/sharing-malicious-files-within-adobe-cloud) published Thursday.


[Adobe Creative Cloud](https://www.adobe.com/creativecloud.html) is a popular suite of apps for file-sharing and creating and includes widely used apps such as Photoshop and Acrobat.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Though attackers are primarily targeting Office 365 users – a [favorite target](https://threatpost.com/office-365-persistent-cyberattacks/160010/) among threat actors – researchers have seen them hit Gmail inboxes as well, Jeremy Fuchs, cybersecurity research analyst at Avanan, told Threatpost.


The attack vector works like this: An attacker creates a free account in Adobe Cloud, then creates an image or a PDF file that has a link embedded within it, which they share by email to an [Office 365](https://threatpost.com/office-365-persistent-cyberattacks/160010/) or Gmail user.


“Think of it like when you create a Docusign,” Fuchs explained to Threatpost. “You create the document and then send it to the intended recipient. On the receiving end, they get an email notification, where they click to be directed to the link.”


Though the links inside the documents sent to users are malicious, they themselves are not hosted within Adobe Cloud but, rather, from another domain controlled by attackers, he added.


**How the Campaign Works**
--------------------------


Researchers shared screenshots of the attack they observed in the report. One shows attackers sending what looks like a legitimate PDF called Closing.pdf sent from Adobe with a button that says “Open” to open the file.


When the user clicks on the link, he or she is redirected to an Adobe Document Cloud page that includes an “Access Document” button that supposedly leads them to the Adobe PDF. However, that link actually leads to “a classic” credential-harvesting page, which is hosted outside the Adobe suite, according to the report.


Attackers can use this model for sending various legitimate-looking Adobe Cloud documents or images to unsuspecting users, Fuchs told Threatpost.


**Designed to Evade Detection**
-------------------------------


Though the second screenshot shared in the report includes text with grammatical errors that should alert a user that it’s suspicious if they are paying attention, generally the campaign has been created to evade detection from both end users and email scanners, researchers said.


For one, the notification comes straight from Adobe, a company that users trust and which is also on most scanner “Allow Lists,” researchers said. Additionally, the spoofed email looks just like a traditional email that an end user would receive from Adobe, they said.


“Though the several hops to get to the final page may cause some red flags from discerning end-users, it won’t stop all who are eager to receive their documents, especially when the title of the PDF – in this case ‘Closing’ – can instill urgency,” researchers wrote in the report.


Researchers at this point don’t know who is behind the campaign, which for now is sticking to its goal of harvesting credentials, though “that could change,” Fuchs told Threatpost.


**Avoiding Compromise**
-----------------------


Researchers suggested a number of ways security professionals and end users can avoid falling victim to the campaign. One is to inspect all Adobe cloud pages for grammar and spelling, and to hover over links to ensure the intended page is legitimate, they said in the report.


Security pros also should deploy email protection that doesn’t rely on static Allow Lists but instead use solutions that include dynamic, AI-driven analysis, researchers advised. Allow Lists can let malicious emails slip through when attackers use spoofed emails that appear to be from trusted entities.


Finally, Avanan advised that organizations install security solutions that can open PDF files in a sandbox and inspect all links to detect potentially malicious intent, according to the report.


**Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the *new* password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & Stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Derusbi]] [[action.malware.name=Elise]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cloud]] [[Threatpost]] [[Pdf]] [[Fuchs]] [[Avanan]] [[ThreatPost]]

