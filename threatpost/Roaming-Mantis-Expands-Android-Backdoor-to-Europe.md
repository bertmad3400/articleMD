# Roaming Mantis Expands Android Backdoor to Europe
### The 'smishing' group lives up to its name, expanding globally and adding image exfiltration to the Wroba RAT it uses to infect mobile victims.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=178247
+ Date: 2022-02-07T17:32:14+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/02/07122107/praying-mantis-scaled-e1644254560868.jpeg)

The Roaming Mantis Android malware campaign has buzzed into Europe, quickly infesting France in particular, where there have been 66,789 downloads of the group’s specific remote access trojan (RAT) as of January.


The campaign pushes the Android RAT known as Wroba (aka Moqhao or XLoader) onto victim devices. According to research from Kaspersky, it has been updated with the ability to exfiltrate images and galleries from a victim device, which potentially paves the way for lifting sensitive information from things like drivers’ licenses, abusing stored QR codes for payment services, or even for blackmail or sextortion.


Roaming Mantis has been [on the move since 2018](https://threatpost.com/roaming-mantis-swarms-globally-spawning-ios-phishing-cryptomining/132149/), mostly observed in Japan, South Korea and Taiwan. Now, its arrival in France has resulted in that country seeing the highest volume of attacks worldwide, according to researchers at Kaspersky. There have also been detections in Germany.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“The actor is focusing on expanding infection via smishing to users in Europe,” Kaspersky researchers noted in a [Monday writeup](https://securelist.com/roaming-mantis-reaches-europe/105596/). “The campaign in France and Germany was so active that it came to the attention of the German police and French media.”


The campaign typically spreads via “smishing” – i.e., SMS-based phishing, usually impersonating Google Chrome or a region-specific entity such as Yamato Transport in Japan.


“Typically, the smishing messages contain a very short description and a URL to a landing page,” they explained. “If a user clicks on the link and opens the landing page, there are two scenarios: iOS users are redirected to a phishing page imitating the official Apple website, while the Wroba malware is downloaded on Android devices.”


The Wroba RAT has a feature that checks the region of the infected device in order to display a phishing page in the corresponding language. In the past, it has checked for Asian regions, but Germany and France have been added as well, according to Kaspersky.


Interestingly, researchers also found that for non-targeted regions, the landing page blocks the connection from the source IP address, so the user just receives a fake “404” error page.


**Recent Obfuscation Updates**
------------------------------


The criminal group behind Roaming Mantis has recently updated some of its other tactics and tools, including adding various obfuscation techniques to the proceedings in order to evade detection.


“First, the actor changed the programming language from Java to Kotlin, a programming language designed to interoperate fully with Java,” researchers explained. “Then…the data structure of the embedded payload…was also modified.”


The first-stage payload, a loader that fetches Wroba, is now encased in a carapace of junk code, the researchers found. It’s an .ELF file was embedded into the .APK file that’s downloaded to the device. The .ELF file uses Java Native Interface (JNI) to install the second-stage payload, for decryption and also part of the loading feature, according to the researchers.


“The loader function takes each section of data from the embedded data, except the junk data,” they explained. “Then, the encrypted payload is XORed using the embedded XOR key. After the XOR operation, as with previous samples, the data is decompressed using zlib to extract the payload, a Dalvik Executable (DEX) file.”


The decrypted payload is then saved and executed to infect the malicious main module on victim devices.


**Stealing Images**
-------------------


As for the Wroba backdoor itself, the RAT has received two new data-stealing commands: “get\_photo” and “get\_gallery.” This brings the total number of embedded backdoor commands to 21, according to Kaspersky.


“These new backdoor commands are added to steal galleries and photos from infected devices,” researchers noted. “This suggests the criminals have two aims in mind. One possible scenario is that the criminals steal details from such things as driver’s licenses, health insurance cards or bank cards, to sign up for contracts with QR code payment services or mobile payment services. The criminals are also able to use stolen photos to get money in other ways, such as blackmail or sextortion.”


They added, “We predict these attacks will continue in 2022 because of the strong financial motivation.”


***Check out our free***[***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Derusbi]] [[action.malware.name=Elise]] [[action.malware.name=Expand]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]] [[action.malware.name=ZLib]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Asia]] [[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.country.name=South Korea]] [[victim.continent.name=Asia]] [[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Wroba]] [[Kaspersky]] [[Android]] [[“the]] [[Phishing]] [[ThreatPost]]

