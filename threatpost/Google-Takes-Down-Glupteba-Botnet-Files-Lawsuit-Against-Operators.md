# Google Takes Down Glupteba Botnet; Files Lawsuit Against Operators
### The malware's unique blockchain-enabled backup C2 scheme makes it difficult to eliminate completely.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176826
+ Date: 2021-12-07T17:13:51+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/05/19122836/Botnet2-e1621441729944.jpg)

Google’s Threat Analysis Group (TAG) has disrupted the blockchain-enabled botnet known as Glupteba, which is made up of around 1 million compromised Windows and internet of things (IoT) devices.


In tandem, Google also filed a lawsuit against the botnet’s operators.


Glupteba, already a formidable presence worldwide, grows at a rate of thousands of new devices per day, according to TAG. It spreads via fake pirate software, fake YouTube videos, malicious documents, traffic distribution systems and more, researchers said. Once installed, it sets about stealing users’ credentials and data, mining cryptocurrencies on infected hosts, and setting up proxies to funnel other internet traffic through infected machines and routers.



> **We want to know what your biggest cloud security concerns and challenges are, and how your company is dealing with them. Weigh in with our exclusive, anonymous [Threatpost Poll](https://threatpost.com/cloud-security-challenges-poll/176702/)!**
> 
> 


“And at any moment, the power of the Glupteba botnet could be leveraged for use in a powerful ransomware or distributed denial-of-service (DDoS) attack,” Google noted in its lawsuit, shared with Threatpost on Tuesday.


The botnet’s operators also offer a slate of underground cybercrime-as-a-service offerings.


“While analyzing Glupteba binaries, our team identified a few containing a git repository URL: git.voltronwork[dot] com, researchers explained. “This finding sparked an investigation that led us to identify, with high confidence, multiple online services offered by the individuals operating the Glupteba botnet. These services include selling access to virtual machines loaded with stolen credentials (dont[.]farm), proxy access (awmproxy), and selling credit-card numbers (extracard) to be used for other malicious activities such as serving malicious ads and payment fraud on Google Ads.”


To defang the beast, TAG disrupted “key command-and-control infrastructure so those operating Glupteba should no longer have control of their botnet — for now,” the group’s vice president of security Royal Hansen and general counsel Halimah DeLaine Prado said in a [Tuesday posting](https://blog.google/technology/safety-security/new-action-combat-cyber-crime/).


The operation included terminating 63 million Google Docs used to distribute Glupteba, 1,313 Google accounts, 908 cloud projects and 870 Google Ads accounts; and, working with CloudFlare and others, taking down servers and placing warning interstitial pages in front of malicious domains.


However, Hansen and Prado acknowledged that “Glupteba’s use of blockchain technology as a resiliency mechanism is notable here … the decentralized nature of blockchain allows the botnet to recover more quickly from disruptions, making them that much harder to shut down.”


Elaborating in a [separate post](https://blog.google/threat-analysis-group/disrupting-glupteba-operation/), TAG researchers added that “the operators of Glupteba are likely to attempt to regain control of the botnet using a backup command-and-control mechanism that uses data encoded on the Bitcoin blockchain.”


Specifically, the C2 uses HTTPS to communicate with infected devices; however, if for some reason that communication is disrupted, the infected systems can retrieve backup domains encrypted in the latest transaction from various Bitcoin wallet addresses.


As the takedowns of [Emotet](https://threatpost.com/emotet-resurfaces-trickbot/176362/) and [TrickBot](https://threatpost.com/trickbot-takedown-crimeware-apparatus/160018/) showed, these types of networks do tend to resurge weeks or months after technical action is taken. So, as an extra layer of disruption, Google also filed a lawsuit in the Southern District of New York against Russian nationals Dmitry Starovikov and Alexander Filippov.


The two are being sued for computer fraud and abuse, trademark infringement, violations under the Racketeer Influenced and Corrupt Organizations Act (RICO), tortious interference of business relationships, unjust enrichment, and other allegations.


“Our litigation was filed against the operators of the botnet, who we believe are based in Russia,” Hansen and Prado wrote. “We also filed a temporary restraining order to bolster our technical disruption effort. If successful, this action will create real legal liability for the operators.”


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Emotet]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=S-Type]] [[action.malware.name=Spark]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]]

#### Industry:
[[victim.industry.name=Agriculture]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Botnet]] [[Google]] [[Glupteba]] [[Threatpost]] [[Hansen]] [[ThreatPost]]

