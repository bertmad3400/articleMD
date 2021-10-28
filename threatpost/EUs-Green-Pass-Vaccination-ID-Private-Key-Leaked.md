# EU’s Green Pass Vaccination ID Private Key Leaked
### The private key used to sign the vaccine passports was leaked and is being passed around to create fake passes for the likes of Mickey Mouse and Adolf Hitler. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175857)
+ Date: October 28, 2021  11:34 am
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/28113249/hitler_wax_museum-e1635435181263.jpg)
As of Thursday morning Eastern time, Adolf Hitler and Mickey Mouse could still validate their digital Covid passes, SpongeBob Squarepants was out of luck, and the European Union was investigating a leak of the private key used to sign the EU’s Green Pass vaccine passports.


Two days earlier, on Tuesday, several people reported that they’d found a QR code online that turned out to be a digital Covid certificate with the name “Adolf Hitler” written on it, along with a date of birth listed as Jan. 1, 1900.


On Wednesday, the Italian news agency ANSA [reported](https://www.ansa.it/english/news/general_news/2021/10/27/eu-green-pass-generation-keys-stolen-sources_e231d1e5-8eab-429b-ae6d-c70991469d41.html) that several underground vendors were selling passes signed with the stolen key on the Dark Web, and that the EU had called “several high-level meetings” to investigate whether the theft was an isolated incident.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)  

The private key used to verify Hitler’s pass was reportedly revoked as of Wednesday, but there were multiple reports of working certificates still being sold online. Threatpost confirmed this on Thursday morning by using the official [Verifica C19](https://play.google.com/store/apps/details?id=it.ministerodellasalute.verificaC19&hl=en_GB&gl=US) app to scan a QR code that had been shared on Twitter by a penetration tester.



Adolf’s certificate got the green light, as shown in the screen capture below:


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/28094913/adolf2-scaled.jpg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/28094913/adolf2-scaled.jpg)


Other QR codes [posted to GitHub](https://github.com/denysvitali/covid-cert-analysis/blob/master/RESULTS.md) turned up a validly signed certificate for Mickey Mouse, though SpongeBob’s certificate has since been turned away as the key(s) gets revoked.


 


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/28103652/Mickey-scaled-e1635431827738.jpeg)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/28103652/Mickey-scaled-e1635431827738.jpeg)


A ‘Growing Black Market’ in Forged Vaccine Passports
----------------------------------------------------


Besides fictional or dead characters, the penetration tester who shared the QR code – @reversebrain – noted that this is no laughing matter. “This is worrying,” they said. “If the leak would be confirmed, this means that fake EU Digital COVID Certificate can be forged to any person.”


It wouldn’t be the first time. In June, Germany set up a police task force to battle what the [BBC called](https://www.bbc.com/news/world-europe-57344546) a growing black market in forged vaccine certificates, as scammers communicated via the encrypted Telegram messaging service to dupe people into paying about €100 (£86; $122) for a whole lot of nothing.


Telegram is again featuring in the forged certificates this time around. GitHub user [Emanuele Laface said](https://github.com/ehn-dcc-development/hcert-spec/issues/103) on Tuesday that the encrypted messenger service is where most of the forged Green Passes are being passed around:



> “On various groups (Telegram mainly) are circulating several forged Green Pass with valid signature.” —Emanuele Laface’s Oct. 26 GitHub post
> 
> 


Laface suggested that the leak could encompass more than just one private key. Rather, it could be  that a database of private keys was compromised: a possibility that “may [end] up in a break of the chain of trust in the Green Pass architecture,” they noted.


That chain of trust could be broken in a lot of places: According to [BleepngComputer](https://www.bleepingcomputer.com/news/security/eu-investigating-leak-of-private-key-used-to-forge-covid-passes/), the fake certificates circulating online have been issued from countries including France, Germany, Italy, Netherlands, North Macedonia, Poland, and more, “indicating the issue could very well impact the entire EU.”


EU Is Investigating
-------------------


Threatpost reached out to the European Commission and some EU CERT agencies for an update on investigations into the key leak and will update this story when we hear back. In the meantime, an EU spokesperson told BleepingComputer that officials are aware of “alleged fraudulent manipulations of EU Covid Certificate QR code.”  Its statement continued:



> “As a priority, we are following closely the developments of this incident and are in contact with the relevant member states authorities that are investigating and putting in place remedial actions. We firmly condemn this malicious act, representing an interference in a sensitive and strategic area, at a time when health services in all Member States are under pressure fighting the pandemic. The incident has no impact on the security and integrity of the EU Gateway managed by the Commission.” —EU statement, per BleepingComputer.
> 
> 


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Threatpost]] [[GitHub]] [[ThreatPost]]
