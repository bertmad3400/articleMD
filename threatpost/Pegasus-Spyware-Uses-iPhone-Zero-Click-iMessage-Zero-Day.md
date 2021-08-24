# Pegasus Spyware Uses iPhone Zero-Click iMessage Zero-Day
### Cybersecurity watchdog CitizenLab saw the new zero-day FORCEDENTRY exploit successfully deployed against iOS versions 14.4 & 14.6, blowing past Apple’s new BlastDoor sandboxing feature to install spyware on the iPhones of Bahraini activists – even one living in London at the time.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168899)
+ Date: August 24, 2021  1:51 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/20141444/white-pegasus-e1626804896117.jpg)
A never-before-seen, zero-click iMessaging exploit has been allegedly used to illegally spy on Bahraini activists with NSO Group’s Pegasus spyware, according to cybersecurity watchdog Citizen Lab.


The digital researchers are calling the new iMessaging exploit FORCEDENTRY.


In a [report](https://citizenlab.ca/2021/08/bahrain-hacks-activists-with-nso-group-zero-click-iphone-exploits/) published on Tuesday, researchers said that they’ve identified nine Bahraini activists whose iPhones were inflicted with Pegasus spyware between June 2020 and February 2021. Some of the activists’ phones suffered zero-click iMessage attacks that, besides FORCEDENTRY, also included [the 2020 KISMET exploit](https://threatpost.com/zero-click-apple-zero-day-pegasus-spy-attack/162515/).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The activists included three members of [Waad](https://www.aldemokrati.org/) (a secular Bahraini political society), three members of the [Bahrain Center for Human Rights](https://bahrainrights.net/), two exiled Bahraini dissidents, and one member of [Al Wefaq](https://en.wikipedia.org/wiki/Al_Wefaq) (a Shiite Bahraini political society), Citizen Lab wrote.


At least one of the activists lived in London when the exploit was unleashed, Citizen Lab said. That’s a new twist, given that researchers have only seen the Bahraini government spying in Bahrain and Qatar, never in Europe. It could mean that the activist in London “may have been hacked by a Pegasus operator associated with a different government.” Citizen Lab suggested.


At least four of the targets were attacked by LULU: a Pegasus operator that Citizen Lab attributes with “high confidence” to the Bahraini government, which has a history of using commercially available spyware.


One of the activists was targeted in 2020 several hours after they revealed during an interview that their phone was infected with Pegasus in 2019.


New iPhone Zero-Click Exploit Popped Up in February
---------------------------------------------------


Citizen Lab first observed NSO Group deploying the new zero-click FORCEDENTRY iMessage exploit – which circumvents Apple’s BlastDoor feature – in February 2021. Apple had just [introduced BlastDoor](https://threatpost.com/apple-ios-imessage-blastdoor/163479/), a structural improvement in iOS 14 meant to block message-based, zero-click exploits like this – the month before. BlastDoor was supposed to prevent this type of Pegasus attack by acting as what Google Project Zero’s Samuel Groß [called](https://googleprojectzero.blogspot.com/2021/01/a-look-at-imessage-in-ios-14.html) a “tightly sandboxed” service responsible for “almost all” of the parsing of untrusted data in iMessages.


So much for all that. “We saw the FORCEDENTRY exploit successfully deployed against iOS versions 14.4 and 14.6 as a zero-day,” Citizen Lab said. “With the consent of targets, we shared these crash logs and some additional phone logs relating to KISMET and FORCEDENTRY with Apple, Inc., which confirmed they were investigating.”


Apple Responds
--------------


Ivan Krstić, head of Apple Security Engineering and Architecture, told Threatpost on Tuesday that attacks such as the ones described by Citizen Lab are highly targeted and thus nothing to worry about … for most people, at any rate. In a statement, Krstić said that such attacks are “highly sophisticated, cost millions of dollars to develop, often have a short shelf life, and are used to target specific individuals.”


As such, they’re “not a threat to the overwhelming majority of our users,” Krstić wrote, although Apple continues to “try to protect all of its customers and is constantly adding new protections for their devices and data.”


Another Apple spokesperson noted to Threatpost that BlastDoor isn’t the end-all, be-all when it comes to securing iMessage, that Apple has significantly boosted defenses in iOS 15 and will continue to do so. Security is, after all, a dynamic process, and Apple is constantly working to respond to new threats as they emerge, the spokesperson said.


What to Do If You’re Not ‘Most People’
--------------------------------------


Besides Apple’s iMessage, NSO Group has a track record of exploiting other messaging apps, such as [WhatsApp](https://threatpost.com/whatsapp-hack-nso-group-investigation/149696/), in order to deliver its malware. Still, Citizen Lab thinks that in this particular case, with these particular attacks, disabling iMessage and FaceTime might have thwarted the threat actors. “Disabling iMessage and FaceTime would not offer complete protection from zero-click attacks or spyware,” researchers noted.


Plus, it has tradeoffs: “Disabling iMessage means that messages exchanged via Apple’s built-in Messages app would be sent unencrypted (i.e., ‘green messages’ instead of ‘blue messages’), making them trivial for an attacker to intercept,” according to the report.


Of course, there are other end-to-end encrypted messaging apps to consider when it comes to minimizing your attack surface. Taylor Gulley, senior application security consultant at app security provider nVisium, told Threatpost on Tuesday that disabling widely used methods of communication can at least force attackers to jump through more hoops, given that it forces them “to invest more time and effort into discovering new exploits for the avenues that remain.”


To minimize attack surface via messaging, that means limiting the number of messaging apps installed, only accepting messages from known contacts, and preventing those messages received from automatically fetching media, Gulley noted. “All of these act as additional barriers between you and a malicious message.”


Gulley pointed out that there have been a number of vulnerabilities in recent years for both iOS and Android messaging apps.


 


Hank Schless, senior manager of security solutions at endpoint-to-cloud security company Lookout, noted that there’s an Android version of Pegasus known as Chrysaor, [uncovered in 2017](https://threatpost.com/android-variant-of-notorious-pegasus-spyware-found/124781/) by Lookout and Google. It has almost the exact same capabilities on Android as Pegasus does on iOS, Schless said, including gaining root access to the target device and being able to read anything on the device even if it’s in an app with encrypted messaging.


Chrysaor differs from Pegasus in that it doesn’t rely on zero-day vulnerabilities in order to infect the device, Schless said in an email. Rather, it relies on a well-known rooting technique called Framaroot.


Still, the attack chains of both Pegasus and Chrysaor are the same: “The attacker sends the targeted individual a socially engineered message across any platform with messaging capabilities and silently delivers the vicious surveillanceware to the device,” he described. “Unfortunately, this means that targets are at risk regardless of the OS their device runs on. It also means that almost no data is safe, since root access to a device gives the attacker control and access to everything.”


An attempted jailbreak or root of a device is one of the biggest signs of malware being present on the device, Schless said. Admins of mobile apps – including Lookout – “can set policies that block a device from the internet and alert the user as soon as that malicious functionality is detected” he noted.


A better option than either Android or iOS may be to use an open-source messaging app built from the ground up with security in mind, such as Signal, Gulley said via email. That gives you two fallbacks: “Auditing the code yourself as a user or to some degree, relying on the community to audit it for you.”


Open source apps aren’t necessarily any more secure than proprietary apps, Gulley suggested, but at least they can be independently audited. “Despite their best intentions, securing your data and device is secondary to these companies who — let’s be honest — are ultimately there to make money off ads, devices, and services,” the consultant observed. “If these kinds of zero-day flaws were easy to discover, they would be less likely to have been created in the first place. This is evident by the fact that numerous open- and closed-source apps have been exploited by zero-day attacks — an unfortunate reality that will continue well into the future.”


NSO Group Sort of Responds
--------------------------


NSO Group said in a statement given to [Bloomberg](https://www.bloomberg.com/news/articles/2021-08-24/report-finds-nso-group-s-spyware-used-on-bahraini-activists) that it hadn’t yet seen the report, but nonetheless, the company questions Citizen Lab’s methods and motives. “If NSO receives reliable information related to the misuse of the system, the company will vigorously investigate the claims and act accordingly,” according to its statement.


Threatpost reached out to NSO Group with a number of questions, the first being whether or not anybody at the Israeli company has gotten around to reading Citizen Lab’s report yet. We also asked NSO Group to explain what specific questions it has about Citizen Lab’s “methods and motives;” what source, and the nature of the information, that it would consider reliable; example(s) of when NSO Group has launched an investigation into misuse of its technology; and what the outcome has been.


An NSO Group spokesperson said that these questions are addressed in the company’s Transparency and Responsibility Report ([PDF](https://www.nsogroup.com/wp-content/uploads/2021/06/ReportBooklet.pdf)), which claims that since 2016, it’s cut off five customers following an investigation of misuse. The pamphlet doesn’t identify the customers.


Lookout’s Schless pointed out that ever since Lookout and Citizen Lab first discovered Pegasus back in 2016, NSO has maintained the stance that its spyware is only sold to a handful of intelligence communities within countries that have been thoroughly vetted for human rights violations. “Their proactive statements about the Citizen Lab is just another attempt at maintaining this narrative in the media,” he said. “The recent exposure of 50,000 phone numbers linked to targets of NSO Group customers was all people needed to see right through what NSO claims.”


Schless called  Citizen Lab “a leader in the security research field” that “openly works together with private sector organizations to ensure that the world is made aware of threats across the Internet as a means to stay safer and more secure.”


Add This to the Growing Pile
----------------------------


As far as NSO Group’s own methods and motives go, they’re getting beaucoup scrutiny in the courts and in protests by infuriated citizens and lawmakers around the world. It’s on the hot seat in these cases:


**Budapest**: Last month, about 1,000 people [protested](https://www.reuters.com/world/europe/hungarians-protest-against-alleged-illegal-surveillance-with-pegasus-spyware-2021-07-26/) and Hungary’s opposition [called for ministerial resignations](https://www.theguardian.com/news/2021/jul/28/call-for-hungarian-ministers-to-resign-in-wake-of-pegasus-revelations) from Viktor Orbán’s far-right government over allegations that it secretly, illegally surveilled journalists, media owners and opposition political figures with Pegasus.


**India**: Also in July, [protests erupted](https://www.timesofisrael.com/protests-erupt-in-indias-parliament-over-israeli-spyware-scandal/) in India’s parliament, with the opposition party calling Prime Minister Narendra Modi’s government’s alleged use of NSO Group’s military-grade Pegasus to spy on political opponents and others “a national security threat.”


**France**: Last month, French President Emmanuel Macon [switched his phone and number](https://www.bbc.com/news/world-europe-57937867) after reports that he, along with 14 French ministers, were allegedly flagged for potential Pegasus surveillance by Morocco. French lawmakers [launched an investigation](https://threatpost.com/french-launch-nso-probe-after-macron-believed-spyware-targe/167986/) into the allegations.


**California**: [Facebook’s suing](https://threatpost.com/facebooks-nso-group-lawsuit-whatsapp-spying/157571/) NSO Group in U.S. federal court over alleged spying on WhatsApp users. In December 2020, a roster of tech companies [filed amicus briefs](https://blogs.microsoft.com/on-the-issues/2020/12/21/cyber-immunity-nso/) in support of its legal action, including Microsoft, Google, Cisco, and VMWare.


**United Nations**: Also in July, the UN human rights chief [decried](https://news.un.org/en/story/2021/07/1096142) the widespread use of Pegasus to illegally undermine the rights of those under surveillance, including journalists and politicians, calling it “extremely alarming” and saying that it confirmed “some of the worst fears” surrounding the potential misuse of such technology. Human rights experts working with the UN [called for a moratorium](https://www.ohchr.org/EN/NewsEvents/Pages/DisplayNews.aspx?NewsID=27379&LangID=E) on the sale and transfer of spyware and other surveillance technology until they’ve instituted “robust regulations that guarantee its use in compliance with international human rights standards.”


**Amnesty International**: The human rights group has [accused](https://threatpost.com/amnesty-international-targeted-by-nation-state-spyware/134630/) Saudi Arabia of using Pegasus to spy on its employees. In 2019, Amnesty announced that it was taking the Israeli Ministry of Defense (MoD) [to court](https://nakedsecurity.sophos.com/2019/05/21/amnesty-sues-maker-of-pegasus-the-spyware-let-in-by-whatsapp-zero-day/) to force it to revoke NSO Group’s export license.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[NSO]] [[Bahraini]] [[zero-click]] [[iMessage]] [[said.]] [[Threatpost]] [[apps]] [[Schless]] [[Group’s]] [[Android]] [[ThreatPost]]
