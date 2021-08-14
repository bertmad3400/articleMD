# This 'unique' phishing attack uses Morse code to hide its approach
### Attackers turn to Morse code's dots and dashes in invoicing phishing campaign.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-unique-phishing-attack-uses-morse-code-to-hide-its-approach/)
+ Date: August 13, 2021 -- 09:58 GMT (10:58 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft has revealed the inner-workings of a phishing attack group's techniques that uses a 'jigsaw puzzle' technique plus unusual features like Morse code dashes and dots to hide its attacks.

The group is using invoices in Excel HTML or web documents to distribute forms that capture credentials for later hacking efforts. The technique is notable because it bypasses traditional email filter systems.

"The HTML attachment is divided into several segments, including the JavaScript files used to steal passwords, which are then encoded using various mechanisms. These attackers moved from using plaintext HTML code to employing multiple encoding techniques, including old and unusual encryption methods like Morse code, to hide these attack segments," [Microsoft Security Intelligence says](https://www.microsoft.com/security/blog/2021/08/12/attackers-use-morse-code-other-encryption-methods-in-evasive-phishing-campaign/). 


"In effect, the attachment is comparable to a jigsaw puzzle: on their own, the individual segments of the HMTL file may appear harmless at the code level and may thus slip past conventional security solutions. Only when these segments are put together and properly decoded does the malicious intent show," it said.

**SEE:** [**This new phishing attack is 'sneakier than usual', Microsoft warns**](https://www.zdnet.com/article/microsoft-watch-out-for-this-sneakier-than-usual-phishing-attack/)

The main aim of the attack is to acquire usernames and passwords, but it is also collecting profit data such as IP address and location to use for subsequent breach attempts. "This phishing campaign is unique in the lengths attackers take to encode the HTML file to bypass security controls," Microsoft said.

The attacks fall within the category of [business email compromise](https://www.zdnet.com/article/microsoft-disrupted-this-large-cloud-based-business-email-scam-operation/) – [a highly profitable scam that outsizes the ransomware cybercrime industry](https://www.zdnet.com/article/business-email-compromise-23-charged-over-sophisticated-fraud-ring/). 






"The XLS.HTML phishing campaign uses social engineering to craft emails mimicking regular financial-related business transactions, specifically sending what seems to be vendor payment advice. In some of the emails, attackers use accented characters in the subject line," Microsoft says. 

Excel and the finance-related subject is the hook that's meant to encourage victims to hand over credentials. 

"Using xls in the attachment file name is meant to prompt users to expect an Excel file. When the attachment is opened, it launches a browser window and displays a fake Microsoft Office 365 credentials dialog box on top of a blurred Excel document. Notably, the dialog box may display information about its targets, such as their email address and, in some instances, their company logo."

**SEE:** [**Malware developers turn to 'exotic' programming languages to thwart researchers**](https://www.zdnet.com/article/malware-developers-turn-to-exotic-programming-languages-to-thwart-researchers/)

The Morse Code element of the attack is used in conjunction with JavaScript, the most popular programming language for web development. 

"Morse code is an old and unusual method of encoding that uses dashes and dots to represent characters. This mechanism was observed in the February ("Organization report/invoice") and May 2021 ("Payroll") waves," Microsoft notes.

"In the February iteration, links to the JavaScript files were encoded using ASCII then in Morse code. Meanwhile in May, the domain name of the phishing kit URL was encoded in Escape before the entire HTML code was encoded using Morse code." The use of Morse code in phishing attacks was spotted by [Bleeping Computer's Lawrence Abrams](https://www.bleepingcomputer.com/news/security/new-phishing-attack-uses-morse-code-to-hide-malicious-urls/) in February.





#### Tags:
[[Microsoft]] [[phishing]] [[HTML]] [[ZDNet]]
