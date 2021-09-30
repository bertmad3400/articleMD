# Researchers discover bypass 'bug' in iPhone Apple Pay, Visa to make contactless payments
### The security issue relates to Visa and Apple's transmit mode.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/researchers-discover-bypass-bug-in-iphone-visa-apple-pay-to-make-contactless-payments/)
+ Date: September 30, 2021
+ Author: Charlie Osborne


## Article:
Unknown

UK academics have uncovered mobile security issues in Visa and Apple payment mechanisms that could result in fraudulent contactless payments.


On Thursday, academics from the UK's University of Birmingham and University of Surrey revealed the technique, in which attackers could bypass an Apple iPhone's lock screen to access payment services and make contactless transactions.  

A paper on the research, "[Practical EMV Relay Protection](https://practical_emv.gitlab.io/assets/practical_emv_rp.pdf)," (.PDF) is due to be published at the 2022 IEEE Symposium on Security and Privacy, and has been authored by Andreea-Ina Radu, Tom Chothia, Christopher J.P. Newton, Ioana Boureanu, and Liqun Chen. 

According to the paper, the 'vulnerability' occurs when Visa cards are set up in Express [Transit mode](https://support.apple.com/en-gb/HT212171) in an iPhone's wallet feature. Express mode has been designed with commuters in mind, when they may want to quickly tap and pay at a turnstile to access rail, for example, rather than hold up a line due to the need to go through further identity authentication.  

The researchers say that the issue, which only applies to Apple Pay and Visa, is caused by the use of a unique code -- nicknamed "magic bytes" -- that is broadcast by transit gates and turnstiles to unlock Apple Pay.  

By using standard radio equipment, they were able to perform a relay attack, "fooling an iPhone into thinking it was talking to a transit gate," according to the team.

An experiment was conducted using an iPhone with a Visa transit card set up, a Proxmark -- to act as a reader emulator -- an NFC-enabled Android phone, which acted as a card emulator, and a payment terminal: the overall aim being to make a payment on a locked device to an EMV (smart payment) reader.






If an intended victim is in close proximity, whether held by someone or stolen, the attack can be triggered by capturing and then broadcasting the "magic bytes" and then modifying a set of other variables, as explained below: 


> "While relaying the EMV messages, the Terminal Transaction Qualifiers (TTQ), sent by the EMV terminal, need to be modified such that the bits (flags) for Offline Data Authentication (ODA) for Online Authorizations supported and EMV mode supported are set.  
> 
> Offline data authentication for online transactions is a feature used in special-purpose readers, such as transit system entry gates, where EMV readers may have intermittent connectivity and online processing of a transaction cannot always take place. These modifications are sufficient to allow relaying a transaction to a non-transport EMV reader, if the transaction is under the contactless limit." 
> 
> 

The attack has [been demonstrated](https://practical_emv.gitlab.io/) in the video below. The experiment was performed with an iPhone 7 and an iPhone 12. Transactions over the contactless limit may also potentially be modified, but this requires additional value changes. 


The experiment is an interesting one, although in the real world, this attack technique may not be feasible on a wider scale. It should also be noted that authorization protocols are only one layer of payment protection, and financial institutions often implement additional systems to detect suspicious transactions and mobile fraud. The overall fraud level on Visa's global network is recorded as below 0.1%.

Speaking to ZDNet, the researchers said that Apple was first contacted on October 23, 2020. The team then reached out to Visa in January, followed by a video call in February, and then a report was submitted to Visa's vulnerability reporting platform on May 10, 2021. 

The academics say that while acknowledged by both parties, who have been spoken to "extensively," the issue remains unfixed.

"Our work shows a clear example of a feature, meant to incrementally make life easier, backfiring and negatively impacting security, with potentially serious financial consequences for users," Radu commented. "Our discussions with Apple and Visa revealed that when two industry parties each have partial blame, neither are willing to accept responsibility and implement a fix, leaving users vulnerable indefinitely." 

In a statement, Visa told us:


> "Visa cards connected to Apple Pay Express Transit are secure and cardholders should continue to use them with confidence. Variations of contactless fraud schemes have been studied in laboratory settings for more than a decade and have proven to be impractical to execute at scale in the real world. Visa takes all security threats very seriously, and we work tirelessly to strengthen payment security across the ecosystem."
> 
> 

The research was conducted as part of the [TimeTrust](https://www.surrey.ac.uk/surrey-centre-cyber-security/research/trusted-computing-and-systems) trusted computing project and was funded by the UK National Cyber Security Centre (NCSC). 

ZDNet has reached out to Apple and we will update when we hear back. 

###  Previous and related coverage

* [This cryptocurrency miner is exploiting the new Confluence remote code execution bug](https://www.zdnet.com/article/this-cryptocurrency-miner-is-exploiting-the-new-confluence-remote-code-execution-bug/)  

* [Critical Zoom vulnerability triggers remote code execution without user input](https://www.zdnet.com/article/critical-zoom-vulnerability-triggers-remote-code-execution-without-user-input/)  

* [RCE is back: VMware details file upload vulnerability in vCenter Server](https://www.zdnet.com/article/rce-is-back-vmware-details-file-upload-vulnerability-in-vcenter-server/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[EMV]] [[iPhone]] [[contactless]] [[UK]] [[ZDNet]]
