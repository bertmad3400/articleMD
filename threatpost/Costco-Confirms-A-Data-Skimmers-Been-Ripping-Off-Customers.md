# Costco Confirms: A Data Skimmer’s Been Ripping Off Customers
### Big-box behemoth retailer Costco is offering victims 12 months of credit monitoring, a $1 million insurance reimbursement policy and ID theft recovery services.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176320)
+ Date: November 12, 2021  6:19 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/12181547/costco-e1636758959716.jpeg)
Costco has discovered a payment card skimming device at one of its retail stores and has sent out notification letters informing customers that their card data may have been ripped off if they shopped there recently.


Some customers have been aware for weeks that something was fishy and have been [sharing](https://www.reddit.com/r/Costco/comments/q9b8r7/fraudulent_charges_on_costco_visa/) their [suspicions](https://www.reddit.com/r/saskatoon/comments/qjthme/credit_card_skimmer_at_costco/) on [social media](https://twitter.com/MsLutzmann/status/1434226138797072384).



The story was first picked up by [BleepingComputer](https://www.bleepingcomputer.com/news/security/costco-discloses-data-breach-after-finding-credit-card-skimmer/), which reported that the [notification letters](https://www.documentcloud.org/documents/21103155-costco_data_breach_notification_bc_card_skimmer_device) went out sometime this month.


“We recently discovered a payment card skimming device at a Costco warehouse you recently visited. Our member records indicate that you swiped your payment card to make a purchase at the affected terminal during the time the device may have been operating,” Costco said in the letter.


Costco workers removed the device, notified the authorities and is working with law enforcement as they investigate the incident.


Costco said that it found the skimmer during a routine inspection of its PIN pads.


The retailer is recommending that customers check their credit and/or bank statements for suspicious transactions. Costco is also offering victims IDX identity theft protection services, which provide 12 months of credit monitoring, a $1 million insurance reimbursement policy and ID theft recovery services.


Big-Box Big Banana Taken In by Bogus Little Box
-----------------------------------------------


Best known as simply Costco or Costco Wholesale, Costco Wholesale Corporation is an American, multinational corporation that runs a chain of membership-only big-box stores. As of 2021, the National Retail Federation had rated the big-box behemoth as the [sixth-largest retailer](https://nrf.com/resources/top-retailers/top-50-global-retailers/top-50-global-retailers-2021) in the world.


Costco didn’t go into detail about what type of skimmer it found, but it sounds like it was old-school, as in, a physical gadget glommed on top of a regular card scanner so that a payment-card thief can intercept card details from their magnetic strips, then use the details to imprint fresh, new, fraudulent cards.


That’s opposed to digital skimmers, which steal payment card info from e-commerce websites via browsers. A recent example was a [new Magecart threat actor](https://threatpost.com/claires-customers-magecart-payment-card-skimmer/156552/), detected by the Sansec Threat Research Team, that was stealing people’s payment card info from their browsers using a digital skimmer that was using a unique form of evasion to bypass virtual machines (VMs) in order to avoid targeting (and thereby alerting) security researchers.


Detecting a Skimmer: The Wiggle-Jiggle Method
---------------------------------------------


Skimming devices are often disguised and simply laid on top of the existing machine, attached with double-sided tape or another adhesive. Erich Kron, security awareness advocate for [KnowBe4](https://u7061146.ct.sendgrid.net/ls/click?upn=4tNED-2FM8iDZJQyQ53jATUavSzE-2FiwjSkZ-2BMZMLjTD68bBzltWsjOj4iPYBhQEjDk5yhu_q07lK5GAAVvAnbc-2Fr-2FBDhAPhoMvwzp-2Bdh4wgfTcF0AUhu01ZMXdKNJrsN0iCyDU7ehW0N22Ype9yCK1TM6XYzZcULka2hXrkxot-2FYcsNMOW-2Fi7ZSbc4BW4Y4w5w74JadwzoA7WeaS3IzWKxwNbUyLuAakHl1grsx-2BWQXIJtmz3pEF45dC-2BErqRJkS3w0MIZSmm5-2BgipT5O9NlKzSvZ3i9-2BROM8A5mLQbypXvIDPxwcZBN-2BQuBpAMYXVHWHp-2Fz9KA5nOYKP19LBvXFXqqjJQbPmxmLwz-2Bk449QoXT2KMsOukIZmXqVBjPAru-2FG2PLwk55M44YAS8Hp-2FWPqiHF3o9eLeeDlu-2By-2B7OVnhF16RSr1DE-3D), told Threatpost that they typically cover the keypad and the card swipe area and are very hard to see.


“The skimmers typically have an additional set of card readers that saves the magnetic stripe information and records the PIN entry that can be retrieved later from a distance, using Bluetooth or other wireless technologies,” he said, noting that we can expect to see such low-cost skimmers in use more often” as consumers hit the streets making purchases for the holiday season.”


He recommended looking carefully at the card readers and giving them a wiggle to see if the top feels loose. Also, keep a eye out for pens that don’t fit back into the device: “Because skimmer overlays have to be slightly larger than the card reader itself, they will often make it impossible to put the signature pen back in the slot on the side,” Kron said.


And, of course, the standard operating procedure applies when checking out your credit card and bank statements: Keep an eye out for unknown or unusual charges, and report them to your financial institution immediately.


Of course, it’s much easier to detect thieves’ attempts to get at your credit card when they’ve gone the kludgy, model airplane route. All your jiggling won’t detect a skimmer that’s installed internally, though.


To wit, years ago, there was a spate of Bluetooth-enabled, banking-data-gobbling skimmers installed at gas stations in the Southern US. Eventually, 13 alleged thieves [were charged with forging bank cards](https://nakedsecurity.sophos.com/2014/01/23/thieves-skim-card-data-from-us-gas-stations-via-bluetooth-enabled-devices/) using banking details chirped out via Bluetooth to nearby crooks from devices that were impossible for gasoline-buying customers to detect, given that the skimmers were installed internally.


And as far as digital skimmers go, the problem has grown so acute that in March, [Cloudflare created a web security tool](https://www.zdnet.com/article/cloudflare-launches-page-shield-to-thwart-magecart-card-skimming-attacks/) to prevent Magecart-style attacks.


Physical Data Theft? How Quaint
-------------------------------


Randy Watkins, Chief Technology Officer at Managed Detection and Response (MDR) services provider [CRITICALSTART](https://www.criticalstart.com/), told Threatpost on Friday that the type of physical data theft that Costco reported is “typically very isolated.”


“Card skimming devices are used on everything from gas pumps to ATMs, and are typically isolated, only posing a threat to patrons of the breached device,” he said via email. The data that the attacker can steal from a card’s magnetic strip actually depends on the card itself, he said.


“While things like the credit card number, full name, expiration and country code [are] universal, other cards can contain additional information like billing address or rewards account numbers,” Watkins added. He advised that consumers make a habit of checking card slots for any foreign devices (internal or external) before swiping their card – though, again, that won’t help with internally installed, Bluetooth-enabled devices.


Kludgy or no, devices that physically steal data can cause a world of hurt, particularly at a busy, busy retail store like Costco. “It’s sobering how much damage a single credit card skimmer can do at a high traffic location like a retail register that may process nearly a hundred credit cards per day,” noted Chris Clements, VP of Solutions Architecture at [Cerberus Sentinel](https://u7061146.ct.sendgrid.net/ls/click?upn=4tNED-2FM8iDZJQyQ53jATUc1h7F6EeKyqQHDAzxY6FeBG4AZ1lNaZ-2Fme9HKLAKT7P9oQa_q07lK5GAAVvAnbc-2Fr-2FBDhAPhoMvwzp-2Bdh4wgfTcF0AUhu01ZMXdKNJrsN0iCyDU7ehW0N22Ype9yCK1TM6XYzZcULka2hXrkxot-2FYcsNMOW-2Fi7ZSbc4BW4Y4w5w74JadwzoA7WeaS3IzWKxwNbUyLuAakHl1grsx-2BWQXIJtmz3pEF45dC-2BErqRJkS3w0MIZSmm5-2BgipT5O9NlKzSvZ3i9-2F0bAO953jNJ7ChD2ha8s7q8FczFljaE72Kq01FV8U4vUwVa4ieTzzJ9Ptd2Q81KRLk7QpY5GPjqyKk0112cwmgst-2FI1FjC6cON6Mu1ynUxcbNuIQ7TDla8c4AyXD-2F2IyBq8Hzp2o-2BPePRHWeSY1e1E-3D).


“If undetected for even a month, it can compromise thousands of credit cards,” he told Threatpost via email on Friday.


Clements called out the fact that Costco didn’t say how often it does point-of-sale terminal checks like the one that detected this skimmer, but even just one skimmer can cause a lot of damage. As such “retail organizations need to make it a frequent procedure,” he recommended.


“Many skimming devices have become scarily small and advanced, making detection hard for both consumers and retail staff alike. ‘Shimmers,’ or devices used to clone chip-based credit cards, are extremely small and thin, and can be nearly impossible to spot without disassembling the reader completely,” he added. “There are specialized tools that retail organizations can look to for more easy and accurate detection of skimmers.”


Kudos to Costco for Letting Customers Know
------------------------------------------


KnowBe4’s Kron gave Costco a gold star for letting customers know about the skimmer find. “In many cases, especially when skimmers are found on retail credit card processing machines or in gas pumps, the victims are never made aware that they are likely victims,” he said in an email to Threatpost. “Costco has really gone above and beyond by notifying their customers that they may have been a victim, allowing them to check their bank account or credit card statements for fraudulent activity.”


It’s particularly prudent given that Costco doesn’t accept all major credit cards, Kron said, meaning that many members have to process the payment as a debit card. That means the crooks can get their hands on both the card number and the PIN number.


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost on Tues., Nov. 16 at 2 p.m. ET for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” a LIVE, interactive conversation with Eric Kaiser, Uptycs’ senior security engineer, about how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://bit.ly/3bBMX30) ***for the LIVE event and submit your questions ahead of time via the registration page.***




#### Tags:
[[Costco]] [[Threatpost]] [[Kron]] [[ThreatPost]]
