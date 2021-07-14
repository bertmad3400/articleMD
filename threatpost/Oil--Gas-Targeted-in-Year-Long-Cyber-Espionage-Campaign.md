# Oil & Gas Targeted in Year-Long Cyber-Espionage Campaign
### A global effort to steal information from energy companies is using sophisticated social engineering to deliver Agent Tesla and other RATs.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167639)
+ Date: July 8, 2021  4:29 pm
+ Author: Tara Seals


## Article:
![oil and gas](https://media.threatpost.com/wp-content/uploads/sites/103/2020/04/21091631/oil-and-gas.jpg)
A sophisticated campaign targeting large international companies in the oil and gas sector has been underway for more than a year, researchers said, spreading common remote access trojans (RATs) for cyber-espionage purposes.


According to Intezer analysis, spear-phishing emails with malicious attachments are used to drop various RATs on infected machines, including [Agent Tesla](https://threatpost.com/agent-tesla-microsoft-asmi/163581), AZORult, Formbook, Loki and Snake Keylogger, all bent on stealing sensitive data, banking information and browser information, and logging keyboard strokes.


While energy companies are the main targets, the campaign also has gone after a handful of organizations in the IT, manufacturing and media sectors, researchers said. Victims have been found around the world, including in Germany, United Arab Emirates (UAE) and the United States, but the primary targets are South Korean companies.



“The attack also targets oil and gas suppliers, possibly indicating that this is only the first stage in a wider campaign,” researchers noted in a [Wednesday posting](https://www.intezer.com/blog/research/global-phishing-campaign-targets-energy-sector-and-its-suppliers/). “In the event of a successful breach, the attacker could use the compromised email account of the recipient to send spear-phishing emails to companies that work with the supplier, thus using the established reputation of the supplier to go after more targeted entities.”


One of the targeted companies is “drastically” different from the others, researchers noted, which may offer a clue as to the nature of the cyberattackers.


“The company is FEBC, a religious Korean Christian radio broadcaster that reaches other countries outside of South Korea, many of these countries which downplay or ban religion,” according to Intezer. “One of FEBC’s goals is to subvert the religion ban in North Korea.”


**The Spear-Phishing Attack Vector**
------------------------------------


To kick off the attack, the adversaries send emails tailored to employees at each company being targeted, researchers said. The recipient email addresses range from generic addresses (info@target\_company[.]com, sales@target\_company[.]com) to specific people within companies, suggesting varying levels of reconnaissance work on targets.


To lend a tricky sense of legitimacy, the email addresses used in the “From” field are typosquatted or spoofed, meant to look like emails from actual companies that would be familiar to the targets.


[Typosquatting](https://threatpost.com/malformed-url-prefix-phishing-attacks-spike-6000/164132/) involves registering a domain name that mimics a legitimate domain, with a slight deviation such as including a hyphen or swapping out a letter. For instance, swapping a lowercase “L” with an uppercase “I” is a well-known tactic. Many of the email addresses in this particular campaign used the format of “sender@company-co.kr” instead of sender@company.co.kr, researchers said – a tell-tale difference that’s easy to miss if one is just skimming.


“The contents and sender of the emails are made to look like they are being sent from another company in the relevant industry offering a business partnership or opportunity,” according to Intezer. “The emails are formatted to look like valid correspondence between two companies.”


Other efforts to seem legitimate include making references to executives and using the physical addresses, logos and emails of legitimate companies in the body of the emails. They also include requests for quotations (RFQ), contracts and referrals/tenders to real projects related to the business of the targeted company, according to the posting.


**Malware Disguised in Bogus PDF Attachments**
----------------------------------------------


Each email has a malicious attachment with a seemingly complementary name related to the contents of the email body, according to Intezer. In actuality, it contains .NET malware, usually an .IMG, .ISO or .CAB file. These are all file types that are commonly used by attackers to evade detection from email-based antivirus scanners, researchers said: IMG/ISO files are part of the Universal Disk Format (UDF) which are disk images commonly used for DVDs; while Cabinet (.CAB) files are a type of archive file.


The files are, however, disguised as PDFs, using faux file extensions and icons in an effort to look less suspicious. Once the user double-clicks on the file, the content of the file is mounted, and the user can click the file to be executed.


Intezer also noted that to bypass detection from standard antivirus, the execution of the malware is fileless, meaning that it is loaded into memory without creating a file on disk.


**A Social-Engineering Bonanza**
--------------------------------


While the technical aspects of the campaign are fairly routine, the cyberattackers really shine when it comes to social engineering and doing their homework on their targets, researchers said.


As an example, one email purported to be sent from Hyundai Engineering, and referenced a real combined cycle power plant project in Panama. The email asks the receiver to submit a bid for the supply of equipment to the project and offers further details and requirements “in the attached file” (containing the malware). The email also gives a hard deadline for bid submissions.


Another example involved a typosquatted email supposedly sent by Barend Jenje from GustoMSC, asking the recipient to sign an attached, purported non-disclosure agreement. GustoMSC is based in the Netherlands, specializing in offshore equipment and technology for the oil and gas industry. The email references the real Dunkirk offshore wind farm project, which is run by a consortium made up of several companies, two of which are mentioned in the email.


Another email that Intezer researchers analyzed was sent to an employee at GS E&C, a Korean contractor engaged in various global power plant projects. The email invited the person to submit both technical and commercial offers for the items described in the attachment, which pretended to be a material take off (MTO) document.


It was allegedly sent by Rashid Mahmood from China Petroleum Engineering & Construction Corp. (CPECC), and it contained a reference to the expansion project of an oil field in Abu Dhabi called BAB, which is the oldest operating field in the UAE.


“The content of the emails demonstrates that the threat actor is well-versed in business-to-business (B2B) correspondence,” researchers said. “This extra effort made by the attacker is likely to increase the credibility of the emails and lure victims into opening the malicious attachments.”


As good as the campaigners are at building credibility, some of the emails do contain red-flag mistakes. For instance, while the address provided in the above example is the actual address of CPECC in UAE, it said “reginal headquarter” instead of “regional headquarters.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[emails]] [[Intezer]] [[UAE]] [[malware]] [[ThreatPost]]
