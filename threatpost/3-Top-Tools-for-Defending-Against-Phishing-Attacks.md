# 3 Top Tools for Defending Against Phishing Attacks
### Phishing emails are now skating past traditional defenses. Justin Jett, director of audit and compliance at Plixer, discusses what to do about it.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176463)
+ Date: November 18, 2021  1:49 pm
+ Author: Justin Jett


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/18134711/fish-tropical-e1637261254230.jpg)
Even with the most sophisticated email scanning and phishing detection system available, phishing emails are still a very common intrusion vector for cybercriminals to use to introduce malware, including ransomware, to a business’ network. That’s because 1) increasingly, legitimate systems are used; and 2) phishing emails can also be effective even when employees are highly educated and are good at spotting and reporting them.


Fortunately, there are tactics to protect your network even when the emails can’t be stopped outright.


Increasingly Effective Phishing
-------------------------------


When legitimate email systems are compromised and begin sending out malicious emails from a valid source, the efficacy of phishing is magnified. This was what happened over the weekend when one of the [FBI’s email systems was hacked](https://threatpost.com/fbi-email-hoaxer-ided-vinny-troia/176377/) to send out fake cybersecurity alerts to thousands of people.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


While the email that was sent out didn’t appear to contain any phishing links, it does show that such email compromises can introduce significant security challenges for IT professionals. Most people who received the email would be unlikely to question its legitimacy—even if they looked at the email headers—because the email came from where it said it came from (in the above case, from the FBI).


This type of compromise is extremely dangerous; it renders email authentication mechanisms like [DMARC, SPF and DKIM](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1945.pdf) useless since the email originates from an authorized source; so that means that anti-spam and anti-phishing software is [much more unlikely](https://threatpost.com/bofa-phish-gets-around-dmarc-other-email-protections/156688/) to flag the message as malicious.


Regardless of the actual damage done, the fact remains that such compromises enable malicious actors to execute very effective phishing attacks. So, if the email system has been compromised, what can organizations do to protect their networks from such attacks?


Protecting the Network when Phishing Can’t Be Stopped Outright
--------------------------------------------------------------


There are many resources that network and security professionals should use to protect the business from major attacks. While it would be too exhaustive to list them all, let’s explore a well-rounded, multi-layered approach to try to stop these attacks from gaining control of the network:


Although email security is not infallible, as discussed above, there are some functions within email security that should be enabled so that the likelihood of infection from compromising emails is as low as possible.


One of the most effective ways of stopping phishing attacks is to enable link-protecting in the corporate email settings. Such protections have the email system open any links and remove the ones that lead to malware downloads. Obviously, this protection can’t defend against all nefarious links, but it certainly can help reduce the number of malicious links that make it through to inboxes.


Setting higher spam-filter levels can also help block emails that have malicious intent. These settings use advanced heuristic modeling to look for poorly worded emails, or emails that have wording like other known malicious emails. Again, while not perfect, it’s certainly an important first line of defense.


Hopefully, all organizations already have firewalls in place to block well-known malware from making it onto the network; however, some don’t have systems in place to block malware from spreading once it does enter. Intrusion detection and prevention systems enable organizations to find (detection) and eliminate/alter (prevention) the attack before it can take hold of other systems. These systems are often used as a coordinated effort with the endpoint protection (antivirus) that helps eliminate viruses and common malware.


There is one caveat here: These systems, while very sophisticated, are not as effective at finding relatively new malware or malware that is effective at hiding for long periods of time. This is because the system looks at packets as they traverse the network and thus often misses malicious activity that moves across the network in sporadic time intervals over days or months. Thus, they, like advanced email security, should be included as part of a broader approach that includes other defenses.


Another important prong of a multilayered approach is network detection and response (NDR), which security professionals can use to detect suspicious traffic, and analyze/block malware that makes it through other security systems.


According to [Gartner](https://www.gartner.com/en/documents/3986225/market-guide-for-network-detection-and-response), NDR systems  work by applying “machine learning and other analytical techniques to network traffic” and it “is helping enterprises detect suspicious traffic that other security tools are missing.” Behavioral, flow-based NDR tools complement signature-based detection solutions because they can detect anomalous behavior based on previously known network traffic.


A Balanced Approach
-------------------


These three options, plus user education, endpoint detection and other best practices, can contribute to reducing the effectiveness of advanced phishing attacks. By deploying a multi-layered security approach, even when third-party systems are compromised, security teams are more effective at preventing malware from spreading across their network.


***Justin Jett is the director of audit and compliance at [Plixer](http://www.plixer.com).***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[phishing]] [[emails]] [[malware]] [[attacks.]] [[ThreatPost]]
