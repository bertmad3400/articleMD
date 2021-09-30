# Apple Pay with Visa Hacked to Make Payments via Unlocked iPhones
### Researchers have demonstrated that someone could use a stolen, unlocked iPhone to pay for thousands of dollars of goods or services, no authentication needed.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175229)
+ Date: September 30, 2021  11:26 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/30111110/Apple-Pay-transit-e1633014684466.jpg)
An attacker who steals a locked iPhone can use a stored Visa card to make contactless payments worth up to thousands of dollars without unlocking the phone, researchers are warning.


The problem is due to unpatched vulnerabilities in both the Apple Pay and Visa systems, according to an academic team from the Universities of Birmingham and Surrey, backed by the U.K.’s National Cyber Security Centre (NCSC). But Visa, for its part, said that Apple Pay payments are secure and that any real-world attacks would be difficult to carry out.


The team explained that fraudulent tap-and-go payments at card readers can be made using any iPhone that has a Visa card set up in “Express Transit” mode. Express Transit allows commuters around the world, including those riding the New York City subway, the Chicago El and the London Underground, to tap their phones on a reader to pay their fares without unlocking their devices.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“An attacker only needs a stolen, powered-on iPhone,” according to a writeup ([PDF](https://practical_emv.gitlab.io/assets/practical_emv_rp.pdf)) published this week. “The transactions could also be relayed from an iPhone inside someone’s bag, without their knowledge. The attacker needs no assistance from the merchant.”


In a proof-of-concept video, the researchers showed a £1,000 payment being sent from a locked iPhone to a standard, non-transit Europay, Mastercard and Visa (EMV) credit-card reader.


**Exploiting Apple Pay Express Transit Mode**
---------------------------------------------


The attack is an active man-in-the-middle replay and relay attack, according to the paper. It requires an iPhone to have a Visa card (credit or debit) set up as a transit card in Apple Pay.


The attackers would need to set up a terminal that emulates a legitimate ticket barrier for transit. This can be done using a cheap, commercially available piece of radio equipment, researchers said. This tricks the iPhone into believing it’s connecting to a legitimate Express Transit option, and so, therefore, it doesn’t need to be unlocked.


“If a non-standard sequence of bytes (Magic Bytes) precedes the standard ISO 14443-A WakeUp command, Apple Pay will consider this [to be] a transaction with a transport EMV reader,” the team explained.


Once this malicious reader-spoofing terminal is live, the next step is to intercept and relay the payment-authorization signals from Apple Pay via the emulator to everyday, non-transit contactless payment readers – such as those found in shops. This is something the researchers were able to do with a special application they created, running on an Android phone. The application modifies the communications coming to and from the iPhone.


“While relaying the EMV messages, the Terminal Transaction Qualifiers (TTQ) sent by the EMV terminal need to be modified,” they explained. Specifically, it turns on the “Offline Data Authentication (ODA) for Online Authorizations” feature as well as the “EMV mode supported” setting.


“These modifications are sufficient to allow relaying a transaction to a non-transport EMV reader, if the transaction is under the contactless limit,” according to the writeup. The contactless limit is the top payment amount someone can make using the technology without officially authenticating to the phone via biometrics or passcode.


However, the researchers found that they could also make transactions over the contactless limit with just another tweak to the communications. To do so, “the Card Transaction Qualifiers (CTQ) sent by the iPhone, need to be modified such that the bit (flag) for Consumer Device Cardholder Verification Method is set…The CTQ value appears in two messages sent by the iPhone and must be changed in both occurrences.”


They explained, “This tricks the EMV reader into believing that on-device user authentication has been performed (e.g. by fingerprint).”


The team posted a PoC demo video:


**Visa, Apple Pay Flaws Remain Unpatched**
------------------------------------------


This attack is made possible by a combination of flaws in both Apple Pay and Visa’s systems, the academic team noted.


“The details of this vulnerability have been disclosed to Apple (Oct 2020) and to Visa (May 2021),” according to the writeup. “Both parties acknowledge the seriousness of the vulnerability, but have not come to an agreement on which party should implement a fix.”


However, Visa and Apple aren’t exactly “acknowledging the seriousness” of the problem, considering their official statements regarding the findings.


“Variations of contactless-fraud schemes have been studied in laboratory settings for more than a decade and have proven to be impractical to execute at scale in the real world,” Visa said [in a statement](https://www.bbc.com/news/technology-58719891) to the BBC, adding that its fraud-detection systems would flag any suspicious transactions.


Apple meanwhile shifted the responsibility to Visa and told the outlet, “We take any threat to users’ security very seriously. This is a concern with a Visa system, but Visa does not believe this kind of fraud is likely to take place in the real world given the multiple layers of security in place. In the unlikely event that an unauthorized payment does occur, Visa has made it clear that their cardholders are protected by Visa’s zero-liability policy.”


However, in the paper, the researchers said that fraud detection seems futile in the face of the attack: “back-end fraud detection checks have not stopped any of our test payments,” they wrote.


Threatpost has reached out for more reaction.


For now, users can protect themselves by not using Visa as a transport card in Apple Pay, and if they do, by remotely wiping the device if lost or stolen. The bug does not affect other types of payment cards or payment systems – Mastercard on Apple Pay or Visa on Samsung Pay, for instance, are safe from such attacks, the researchers noted.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





#### Tags:
[[iPhone]] [[contactless]] [[EMV]] [[However,]] [[ThreatPost]]
