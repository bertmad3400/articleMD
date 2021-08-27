# Academics bypass PINs for Mastercard and Maestro contactless payments
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/academics-bypass-pins-for-mastercard-and-maestro-contactless-payments/)
+ Date: August 27, 2021
+ Author: Catalin Cimpanu


## Article:
![Academics bypass PINs for Mastercard and Maestro contactless payments](https://therecord.media/wp-content/uploads/2021/08/Maestro-card.jpg)

A team of scientists from a Swiss university has discovered a way to bypass PIN codes on contactless cards from Mastercard and Maestro.


The now-patched vulnerability would have allowed cybercriminals to use stolen Mastercard and Maestro cards to pay for expensive products without needing to provide PINs on contactless payments.


### The attack basics


Discovered by a team from the Department of Computer Science at the ETH Zurich university, the attack is extremely stealthy and could be easily deployed in a real-world scenario if new bugs in contactless payment protocols are discovered.


The general idea behind the attack is for an attacker to interpose itself between the stolen card and a vendor’s Point-of-Sale (PoS) terminal, in what security researchers would normally call a Man/Person/Meddler-in-the-Middle (MitM) scenario.


To achieve this, an attacker would require:


* a stolen card
* two Android smartphones
* a custom-made Android app that can tamper with a transaction’s fields


The app is installed on both smartphones, which will act as emulators. One smartphone will be placed near the stolen card and act as a PoS emulator, tricking the card into initiating a transaction and sharing its details, while the second smartphone will act as a card emulator and be used by a crook to feed modified transaction details to a real-life PoS terminal inside a store.


![card-relay_attack](https://www-therecord.recfut.com/wp-content/uploads/2021/08/card-relay_attack.png)
From a PoS operator’s point of view, the attack looks like a customer is paying with their mobile payments app, but, in reality, the crook is feeding modified transaction details obtained from a stolen card.


### The initial Visa PIN bypass (2020)


The research team used this attack scheme last year when they discovered a way to bypass PINs on Visa contactless payments.


The attack, described in a September 2020 research paper titled “[The EMV Standard: Break, Fix, Verify](https://arxiv.org/abs/2006.08249),” allowed researchers to intercept Visa contactless payment details and then modify the transaction details to tell a real-life PoS terminal that the PIN and the card owner’s identity had already been verified and confirmed on the device, so the PoS didn’t need to perform these checks.


While the attack appeared too good to be true, researchers said they successfully tested it with Visa Credit, Visa Debit, Visa Electron, and V Pay cards in the real world to complete transactions of 200 Swiss francs, above the PIN requirement limit for Swiss banks.


### The follow-up Mastercard and Maestro PIN bypass (2021)


But the ETH Zurich team continued their research following their initial findings and focused on bypassing PINs on other types of cards that didn’t use the Visa contactless payments protocol.


In a research paper published earlier this year in February and presented at the USENIX security conference earlier this month, the research team said they identified a similar issue with contactless payments from Mastercard and Maestro cards.


The difference in this attack is that instead of telling the PoS terminal that the PIN had already been verified, the researchers are tricking the PoS terminal into thinking that the incoming transaction comes from a Visa card instead of Mastercard/Maestro—by modifying the card’s legitimate Application Identifier (AID) with Visa’s AID: A0000000031010.


This activates the PoS terminal’s Visa-specific kernel, which then proceeds to contact the issuing bank to verify the card. At this point, the attacker performs the older Visa attack from last year and pays for a product without providing a PIN.


The researchers said they successfully tested this attack with Mastercard Credit and Maestro cards, performing transactions of up to 400 Swiss francs during their research.


A demo video of this attack is available below, showing how easy and fast the attack is, and how store clerks have no chance at distinguishing a crook using this technique from a legitimate buyer paying with their smartphone.





The research team said it disclosed its two PIN bypasses to both Visa and Mastercard (which also owns the Maestro brand).


Mastercard rolled out fixes to its network earlier this year, but Visa appears to have not addressed this issue.


The payments processor did not return a request for comment last year when this reporter covered the first bypass, and neither did this year, after the team’s USENIX talk.


The research team said they would not be releasing their Android app that facilitates these attacks in order to prevent widespread abuse of this technique and their research.


Additional details about this attack are available in a paper titled “[Card Brand Mixup Attack: Bypassing the PIN in non-Visa Cards by Using Them for Visa Transactions](https://www.usenix.org/conference/usenixsecurity21/presentation/basin).”





#### Tags:
[[contactless]] [[Mastercard]] [[Android]] [[The Record]]
