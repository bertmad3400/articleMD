# Critical Valve Bug Lets Gamers Add Unlimited Funds to Steam Wallets
### Valve plugs an API bug found in its Steam platform that that abused the Smart2Pay system to add unlimited funds to gamer digital wallets. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168710)
+ Date: August 16, 2021  4:50 pm
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2018/08/01084854/Steam-logo.jpg)
A security researcher helped Valve, the makers of the gaming platform Steam, plug an easy-to-exploit hole that allowed users to add unlimited funds to their digital wallet. Simply by changing the account’s email address, the exploit allowed anyone to artificially boost their digital billfold to anything they wanted.


Steam Wallet funds are exclusive to the Steam platform and are used to purchase in-game merchandise, subscriptions and Steam-related content. Valve restricts Steam credits (or money) from being transferred outside its network for purchase or trading. However, there are several unsanctioned ways to convert wallet funds into actual dollars.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Working for the HackerOne bug-bounty program, security researcher DrBrix, [reported the bug last Monday](https://hackerone.com/reports/1295844). By Wednesday, Valve plugged the hole and paid DrBrix $7,500 for identifying the bug.


**The Hack: Turning $1 into $100 or $1M**
-----------------------------------------


The bug, which has since been patched, was exploited by abusing Valve’s own application programming interface (API) used to communicate with the third-party web payment firm Smart2Pay, owned by Nuvei.


According to DrBrix, the hack allowed an attacker to intercept the POST request sent from Valve to Smart2Pay. This was done via modifying the Steam user’s email address used by Smart2Pay as it passed through the Valve API.


“Firstly you will have to change yours steam account email to something like (I will explain why in next steps, amount100 is the important part): brixamount100abc@█████,” the researcher wrote.


This allows the attacker to manipulate communications between Valve and Smart2Pay, circumventing the cryptographic hash used to protect transaction data.


“We can’t change parameters as there is Hash field with signature, however signature is generated like that hash (ALL\_FIELDS\_NAMES\_VALUES\_CONTACTED),” DrBrix wrote. “So with our special email we can move parameters in a way that will change amount for us.”


Where the Valve parameters might be,


“hash(MerchantID1102MerchantTransactionID█████Amount2000…..)” the attacker can turn $1 into $100 simply by changing the format of the email request.


“So with our special email we can move parameters in a way that will change amount for us. For example, we can change original Amount=2000 to Amount2=000 and after contacting it still will be Amount2000. Then we can change email from CustomerEmail=brixamount100abc%40████ to CustomerEmail=brix&amount=100&ab=c%40█████████ by this we are adding new field amount with our value,” DrBrix wrote.


Valve first rated the bug as of moderate importance. However, after investigating, it escalated the bug to critical in nature, scoring it “9-10”, with the highest possible rating 10.


Valve did not return a Threatpost press request for comment.


“We have changed the severity assessment to Critical, reflecting the potential cost to the business, and applied a bounty accordingly,” wrote Valve in a HackerOne thread thanking DrBrix for the tip.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11 AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[DrBrix]] [[wrote.]] [[ThreatPost]]
