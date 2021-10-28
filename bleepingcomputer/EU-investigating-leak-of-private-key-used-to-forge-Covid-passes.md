# EU investigating leak of private key used to forge Covid passes
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/eu-investigating-leak-of-private-key-used-to-forge-covid-passes/)
+ Date: October 28, 2021
+ Author: Ax Sharma


## Article:
![EU Commission flag ](https://www.bleepstatic.com/content/hl-images/2021/04/06/EU-flag.jpg)


The private key used to sign EU Digital Covid certificates has been reportedly leaked and is being circulated on messaging apps and online data breach marketplaces.


The key has also been misused to generate forged certificates, such as those for Adolf Hitler, Mickey Mouse, Sponge Bob—all of which are being recognized as valid by the official government apps.


The Digital Covid certificate, or the "Green Pass" helps European Union residents travel across borders seamlessly by proving that they have either been vaccinated against COVID-19, received a negative test result, or successfully recovered from COVID-19.


Valid 'Adolf Hitler' Covid certificate generated
------------------------------------------------


This week, users reported seeing the private key for EU Digital Covid certificates circulating on messaging apps, like Telegram.


The private key is used to sign "Green Pass," European Union's equivalent of a vaccine passport, and/or proof of negative COVID-19 status that can help travelers cross borders seamlessly.


"On various groups (Telegram mainly) are circulating several forged Green Pass with valid signature... There is the possibility that a database of private keys is compromised and this may [end] up in a break of the chain of trust in the Green Pass architecture," [stated](https://github.com/ehn-dcc-development/hcert-spec/issues/103) GitHub user Emanuele Laface.


Threat actors who can get their hands on the private key could easily forge digital certificates or QR codes that may then be recognized as 'legitimate' by the official government apps.


Such is the case for a fake Adolf Hitler Green Pass certificate which is being recognized valid by the official Verifica C19 apps, according to penetration tester *reversebrain*:




> 
> Try to scan this QR code with the official government APP "Verifica C19"  
>   
> 
> 2/3 [pic.twitter.com/2y65c4vsc9](https://t.co/2y65c4vsc9)
> 
> 
> — reversebrain (@reversebrain) [October 26, 2021](https://twitter.com/reversebrain/status/1453095038284615682?ref_src=twsrc%5Etfw)


The penetration testerlater reported, the forged certificates were [no longer being recognized](https://twitter.com/reversebrain/status/1453281511818600455) by the government's Verifica C19 apps, indicating the leaked private key had been revoked.


However, tests by BleepingComputer conducted today reveal both the Android and iOS versions of the Verifica C19 app are still treating the QR code for the Adolf Hitler certificate as valid:



![EU Digital Covid Certificate for Adolf Hitler recognized as valid](https://www.bleepstatic.com/images/news/u/1164866/2021/Oct-2021/eu-covid-pass-private-key-leak/covid-pass-adolf-hitler.jpeg)**EU Digital Covid Certificate for Adolf Hitler recognized as valid** (BleepingComputer)
Our tests were conducted via Verifica C19 app version 1.1.5, released October 19th on [Google Play](http://play.google.com/store/apps/details?id=it.ministerodellasalute.verificaC19&hl=en_GB&gl=US), and October 26th on the [Apple App store](http://apps.apple.com/it/app/verificac19/id1565800117).


Additionally, forged certificates for "Mickey Mouse," "Sponge Bob," and [other fictional characters](https://github.com/denysvitali/covid-cert-analysis/blob/master/RESULTS.md) were successfully recognized by the app, as seen by BleepingComputer.


EU vaccination passports on sale for $300
-----------------------------------------


BleepingComputer also observed multiple users posting private keys on underground forums and discussing methods to "make EU green pass."


"Recently the European Union is making the green pass mandatory for many activities, I see that there are several sites that can perfectly read the QR code by decrypting it, I wanted to know if someone is able to re-encrypt data and generate QR code in short, generate a false green pass," asked one forum member.


Some traders are seen offering "Covid European passports with the entry as vaccinated in Poland," each at a price of $300.



![forum trade covid pass eu](https://www.bleepstatic.com/images/news/u/1164866/2021/Oct-2021/eu-covid-pass-private-key-leak/forum-covid-eu-passs.jpg)**Users trading keys and forged certificates on forums**(BleepingComputer)
The QR codes contained in the EU Digital COVID Certificates include a digital signature to protect against their falsification. When the certificate is checked using the official apps, the QR code is scanned and the signature is verified.


The official government docs [state](http://ec.europa.eu/info/live-work-travel-eu/coronavirus-response/safe-covid-19-vaccines-europeans/eu-digital-covid-certificate_en#how-does-it-help-free-movement) that each issuing body, such as a hospital, a test centre, a health authority, has its own digital signature key. All of these private keys are stored in a secure database in each country.


But, it is also not clear if the key compromise impacts every single EU country or issuing bodies from select countries only.


According to the QR code data seen by BleepingComputer, the fake certificates circulating online have been issued from different countries—France, Germany, Italy, Netherlands, North Macedonia, Poland, and so on, indicating the issue could very well impact the entire EU.


EU Government aware and investigating the 'malicious act'
---------------------------------------------------------


BleepingComputer reached out to [CERT](https://en.wikipedia.org/wiki/Computer_emergency_response_team) teams of different EU nations and it seems the issue is being investigated:


"We are aware of alleged fraudulent manipulations of EU Covid Certificate QR code and have seen the reports," an EU spokesperson told BleepingComputer.


"As a priority, we are following closely the developments of this incident and are in contact with the relevant member states authorities that are investigating and putting in place remedial actions."


"We firmly condemn this malicious act, representing an interference in a sensitive and strategic area, at a time when health services in all Member States are under pressure fighting the pandemic."


"The incident has no impact on the security and integrity of the EU Gateway managed by the Commission," concludes the Commission in their statement to us.


The fact that anybody is able to forge cryptographically-valid COVID certificates brings into question the authenticity of even legitimate certificates issued by EU government bodies.


Should this be the case, the private key would need to be revoked by the government authorities for the entire EU, thereby invalidating both forged and legitimate COVID certificates.


As such, by the time the situation is resolved and the private keys are reset, holders of legitimate EU Digital Covid certificates will very likely need to generate fresh Green Passes.




#### Tags:
[[apps,]] [[Verifica]] [[C19]] [[BleepingComputer]] [[Bleeping Computer]]
