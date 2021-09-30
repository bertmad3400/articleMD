# Apple Pay with VISA lets hackers force payments on locked iPhones
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/apple-pay-with-visa-lets-hackers-force-payments-on-locked-iphones/)
+ Date: September 29, 2021
+ Author: Ionut Ilascu


## Article:
![Apple Pay with Visa cards allow limitless transactions from locked iPhone](https://www.bleepstatic.com/content/posts/2021/09/29/ApplePayVisaPay.jpg)


Academic researchers have found a way to make fraudulent payments using Apple Pay from a locked iPhone with a Visa card in the digital wallet with express mode enabled.


The method is akin to a digital version of pickpocketing. It works over the air even if the iPhone is in a bag or in someone’s pocket and there is no transaction limit.


### Ticket-gate payment trick


Looking into relay attacks on contactless payments, researchers at the University of Birmingham and the University of Surrey in the U.K. found that iPhone devices confirm transactions under certain conditions.


For a payment to go through, iPhone users need to authorize it by unlocking the phone using Face ID, Touch ID, or a passcode.


In some scenarios, though, such as paying for public transportation, unlocking the device makes the payment process cumbersome for the user.


Apple Pay solved the problem with Express Transit, a feature that allows a transaction to go through without unlocking the device.


![Express Transit feature](https://www.bleepstatic.com/images/news/u/1100723/2021/ExpressTransit.png)


Express Transit works for specific services, like ticket gates, with card readers that send a non-standard sequence of bytes that bypass the Apple Pay lock screen.


In combination with a Visa card, “this feature can be leveraged to bypass the Apple Pay lock screen, and illicitly pay from a locked iPhone, using a Visa card, to any EMV reader, for any amount, without user authorisation.”


The researchers were able to emulate a ticket-barrier transaction by using a Proxmark device acting as a card reader communicating with the target iPhone and an Android phone with an NFC chip that communicated with a payment terminal.


![Attack setup for Apple Pay transactions from a locked iPhone](https://www.bleepstatic.com/images/news/u/1100723/2021/setup_apple.png)


As seen in the image above, the method is an active man-in-the-middle replay and relay attack where the Proxmark replays the “magic bytes” to the iPhone to trick it into believing that it’s a ticket-gate transaction so user authentication to authorize the payment is not needed.


The attack is more complicated than this, though. The [researchers explain](https://practical_emv.gitlab.io/) that certain flags need to be set by modifying some bits to enable offline data authentication for online transactions, used in readers that may have intermittent connectivity (e.g. transit system entries).



“The attack works by first replaying the Magic Bytes to the iPhone, such that it believes the transaction is happening with a transport EMV reader. Secondly, while relaying the EMV messages, the Terminal Transaction Qualifiers (TTQ), sent by the EMV terminal, need to be modified such that the bits (flags) for Offline Data Authentication (ODA) for Online Authorizations supported and EMV mode supported are set.”



### Raising the limit


Digging deeper into the issue, the researcher discovered that they could modify the Card Transaction Qualifiers (CTQ) responsible for setting contactless transactions limits.


This modification is to trick the card reader that the authentication step on the mobile device has been completed successfully. During the experiment, the researchers were able to make a GBP 1,000 transaction from a locked iPhone. They tested the attack successfully on iPhone 7 and iPhone 12.



### Vulnerability not fixed


The tests were successful only with iPhone and Visa cards. With Mastercard, a check is performed to make sure that a locked iPhone accepts transactions only from card readers with a transit merchant code.


Trying the method with Samsung Pay, the researchers found that transactions are always possible with locked Samsung devices. However, the value is always zero and transport providers charge for tickets based on data associated with these transactions.


The findings of this research have been sent to both Apple and Visa in October 2020 and May 2021, respectively, but neither fixed the problem.


Instead, the two companies passed the burden of a fix to one another, so the vulnerability is still present and can be exploited with off-the-shelf hardware and software.


The details of the research are available in a paper titled “[Practical EMV Relay Protection](https://practical_emv.gitlab.io/assets/practical_emv_rp.pdf),” to be presented at the 2022 IEEE Symposium on Security and Privacy.


Its authors are Andreea-Ina Radu and Tom Chothia from the University of Birmingham, and Christopher J.P. Newton, Ioana Boureanu, and Liqun Chen from the University of Surrey.




#### Tags:
[[iPhone]] [[EMV]] [[Bleeping Computer]]
