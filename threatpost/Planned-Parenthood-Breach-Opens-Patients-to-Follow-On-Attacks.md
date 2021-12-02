# Planned Parenthood Breach Opens Patients to Follow-On Attacks
### Cyberattackers made off with addresses, insurance information, dates of birth, and most worryingly, clinical information, such as diagnosis, procedures, and/or prescription information.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176718)
+ Date: December 2, 2021  2:29 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/02142821/planned-parenthood.jpg)
Planned Parenthood’s Los Angeles (PPLA) division has been hacked, with cyberattackers making off with sensitive personal health information for at least 400,000 patients.


In a data-breach notice ([PDF](https://oag.ca.gov/system/files/EXPERIAN_H1202_Planned%20Parenthood%20of%20Los%20Angeles_L01_SAS_1.pdf)) filed with the state of California, the organization said that it had detected the intrusion on Oct. 17, when it took its systems offline. A subsequent investigation determined that the intruders had access to the network beginning on Oct. 9. During that time, they exfiltrated files containing addresses, insurance information, dates of birth and, most worryingly, clinical information, such as diagnosis, procedures and/or prescription information.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The clinical data is highly sensitive: Planned Parenthood offers a variety of sexual health services, including annual well-woman exams, birth control, cervical and testicular cancer screenings, prenatal care, sexual education, vasectomies, and abortions.


Planned Parenthood spokesperson John Erickson [told the Washington Post](https://www.washingtonpost.com/nation/2021/12/01/los-angeles-planned-parenthood-hack/) that the attackers also installed ransomware, but he provided no information about whether the effort was successful in encrypting files or if the organization paid a ransom. Threatpost has reached out to PPLA for clarification.


**Politically Motivated?**
--------------------------


Coming on the eve of oral arguments being delivered in a [sure-to-be landmark](https://www.cbsnews.com/live-updates/supreme-court-mississippi-abortion-case-oral-arguments-2021-12-01/) Supreme Court case about abortion rights, the breach has ironic timing, given Planned Parenthood’s status as a favorite villain among anti-abortion advocates.


“This is devastating news at a time when political tensions are raging as the Supreme Court actively debates a direct challenge to 1973 Roe v. Wade,” Jane Grafton, vice president of Gurucul, said via email. “Women’s personal procedures and diagnosis are just that: personal. Having them stolen for potential exposure puts women in the political cross hairs. Securing medical records has never been more important. We can only hope that this information stays out of the public eye.”


While it’s not clear if this incident was politically motivated, the group has been subject to “hacktivist” hits before, including an incident in 2015 that resulted in the data of hundreds of employees being [doxxed online](https://www.latimes.com/business/la-fi-planned-parenthood-hacked-20150727-story.html).


“Planned Parenthood is the most trusted women’s healthcare provider in this country, and antiabortion extremists are willing to do anything to stop women from accessing the reproductive healthcare they are seeking,” Dawn Laguens, executive vice president of Planned Parenthood, said at the time.


Earlier this year, the group’s Metropolitan Washington branch [disclosed](https://www.washingtonpost.com/dc-md-va/2021/04/16/data-breach-planned-parenthood-dc/) a 2020 breach that saw data thieves make off with patient and donor dates of birth, medical data, and Social Security and financial information.


**Patients: Beware Follow-On Attacks**
--------------------------------------


If the data has been stolen as part of a [double-extortion attempt](https://threatpost.com/double-extortion-ransomware-attacks-spike/154818/) – in which attackers threaten to leak data publicly unless a ransom is paid – that carries one set of security concerns. However, the richness of the data in question lends itself to follow-on attacks, researchers noted. And the ramifications for PPLA’s patients could be extensive.


“The PII/PHI that has been stolen from Planned Parenthood go beyond the usual threat actor’s desire for identity data to resell on the Dark Web,” said Garret Grajek, CEO at YouAttest. “Given that not only was standard identity information stolen, but the theft was coupled with medical background and procedure data, the ramifications of malicious use of this data are easy to imagine…previous hacks on medical institutions have shown a proclivity to both social and technical hacking methods.”


For instance, fraudsters could mount convincing social-engineering efforts such as payment-card-harvesting phishing emails asking patients to “confirm their billing information.” Identity theft and insurance fraud are also concerns; and there’s always the possibility of patient blackmail and extortion or just basic harassment, including physical threats.


“Patients are encouraged to review statements from their healthcare providers or health insurers and contact them immediately if they see charges for services they did not receive,” the branch said in the statement.


**Fallout for Planned Parenthood**
----------------------------------


Meanwhile, PPLA itself could find itself in trouble, warned Josh Brewton, vCISO at Cyvatar, starting with reputational brand damage.


“If the organization cannot secure its most precious data (patient information), how can individuals trust medical services received will be kept between them and the medical professionals?” he said via email. “This is precisely why medical facilities are held to a high standard of information security (HIPAA).”


If PPLA is shown to have been negligent in its application of the required HIPAA security and privacy rules, it may be liable for civil and possible criminal charges, he added.


Further, “just because an organization is compliant with their sector’s mandatory law/standard (HIPAA/NIST/CMMC/etc.) does not mean that they are secure,” he said. “Having the right people, process, and technology in place while utilizing these frameworks will ensure that you have done your due diligence in providing a safe place for business, client and other sensitive information.”


[Incident-response playbooks](https://threatpost.com/3-guideposts-incident-response-plan/176019/) are one way to do that, according to Kev Breen, director of cyber-threat research at Immersive Labs.


“It is not possible to prevent a determined attacker, so security teams have to assume a breach can happen at any time,” he said via email. “This is why having incident-response playbooks in place are vital. These playbooks should not just focus on security teams alone, but on all stakeholders across the organization from legal to marketing teams. These plans should not sit on a dusty shelf until you need them – they should be practiced and updated consistently.”


Gary Ogasawara, CTO at Cloudian, also noted that perimeter defenses are not enough.


“When it comes to sensitive data in particular, encrypting data both in flight and at rest is essential to keep cybercriminals from reading it or making it public in any intelligible form,” he told Threatpost. “In addition, and most importantly, organizations should have an immutable (unchangeable) backup copy of their data which prevents such criminals from altering or deleting that data and ensures the ability to recover the uninfected backup copy in the event of an attack, without paying ransom.”


In any event, organizations like Planned Parenthood should be more diligent than most, Cyvatar’s Brewton concluded.


“Planned Parenthood is an institution that sparks a lot of emotions on each side of the aisle. With this emotion comes personal and political investments. This investment from all sides paints a giant target on the organization’s back,” he said.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://bit.ly/3bBMX30)***for the LIVE event!***




#### Tags:
[[Threatpost]] [[PPLA]] [[“This]] [[email.]] [[ThreatPost]]
