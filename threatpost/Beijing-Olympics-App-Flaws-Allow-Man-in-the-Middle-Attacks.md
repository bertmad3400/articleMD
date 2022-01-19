# Beijing Olympics App Flaws Allow Man-in-the-Middle Attacks
### Attackers can access audio and files uploaded to the MY2022 mobile app required for use by all winter games attendees – including personal health details.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177748
+ Date: 2022-01-19T13:36:34+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/19082649/winter-olympics.jpeg)

The mobile app that all attendees and athletes of the upcoming [Beijing Winter Olympics](https://olympics.com/en/beijing-2022/schedule/) must use to manage communications and documentation at the event has a “devastating” flaw in the way it encrypts data that can allow for [man-in-the-middle attacks](https://threatpost.com/bluetooth-bug-mitm-attacks/159124/) that access sensitive user information, researchers have found.


MY2022 is an app mandated for use by all attendees – including members of the press and athletes – of the 2022 Olympic Games in Beijing. The problem is, it poses a significant security risk because the encryption used to protect users’ voice audio and file transfers “can be trivially sidestepped” due to two vulnerabilities in how it handles data transport, according to [a blog post](https://citizenlab.ca/2022/01/cross-country-exposure-analysis-my2022-olympics-app/) from Citizen Lab posted online Tuesday.


Additionally, “server responses can also be spoofed, allowing an attacker to display fake instructions to users,” Citizen Lab’s Jeffrey Knockel wrote in the post.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


MY2022 collects info such as health customs forms that transmit passport details, demographic information, and medical and travel history, which are vulnerable due to the flaw, he said. It’s also not clear with whom or which organizations this info is shared.


MY2022 also includes a feature that allow users to report “politically sensitive” content, as well as a censorship keyword list. While the latter is “presently inactive,” it targets a variety of political topics, including domestic issues such as Xinjiang and Tibet as well as references to Chinese government agencies, Knockel wrote.


**Background and Disclosure**
-----------------------------


Researchers disclosed the security issues to the Beijing Organizing Committee for the 2022 Olympic and Paralympic Winter Games on Dec. 3, 2021, giving organizers a deadline of 15 days to respond and 45 days to fix the issues. As of yesterday, Jan. 18, 2022, researchers still hadn’t received a response, according to the post.


Citizen Lab researchers also inspected a Jan. 17 release of version 2.0.5 of MY2022 for iOS to Apple’s App Store, finding that the issues reported still had not been resolved, Knockel wrote. Moreover, that version of the app introduced a new feature called “[Green Health Code](https://www.fmprc.gov.cn/ce/cefi/eng/lsfw/t1904940.htm7vMsaR)” that asks for travel documents and medical info from users that also is vulnerable to the flaws, he added.


MY2022 is being used as part of a closed-loop system implemented due to COVID-19 restrictions that requires all international and domestic attendees to monitor and submit their health status – e.g., a negative test for the virus – to the app on a daily basis.


For domestic users, MY2022 collects personal information including name, national identification number, phone number, email address, profile picture and employment information, and shares it with the Beijing Organizing Committee for the 2022 Olympics. For international users, the app collects users’ demographic information and passport information, as well as the organization to which they belong.


**What’s Not Working**
----------------------


Citizen Lab discovered two security vulnerabilities in the app related to the security of how it transmits user data. Researchers examined version 2.0.0 of the iOS version of MY2022 and version 2.0.1 of the Android version in their analysis.


“Although we were only able to create an account on and thus fully examine the iOS version of MY2022, from our best understanding, the vulnerabilities described below appear to exist in both the iOS and Android versions of MY2022,” Knockel wrote.


The first vulnerability discovered in MY2022 is that it fails to validate SSL certificates, thus failing to validate the party to whom it is sending sensitive, encrypted data, according to the report. This allows an attacker to spoof trusted servers by interfering with the communication between the app and these servers.


“This failure to validate means the app can be deceived into connecting to a malicious host while believing it is a trusted host, allowing information that the app transmits to servers to be intercepted and allowing the app to display spoofed content that appears to originate from trusted servers,” Knockel wrote.


Though some connections the app created weren’t vulnerable, the SSL connections to at least the following servers are: my2022.beijing2022.cn, tmail.beijing2022.cn, dongaoserver.beijing2022.cn, app.bcia.com.cn and health.customsapp.com.


The other vulnerability researchers found in MY2022 is that some sensitive data is being transmitted without SSL encryption or any security at all, according to the report. The app transmits non-encrypted data – including sensitive metadata relating to messages, such as the names of message senders and receivers and their user account identifiers – to “tmail.beijing2022.cn” on port 8099, researchers found.


“Such data can be read by any passive eavesdropper, such as someone in range of an unsecured Wi-Fi access point, someone operating a Wi-Fi hotspot, or an Internet Service Provider or other telecommunications company,” Knockel wrote.


**Fueling the Fire**
--------------------


Researchers believe the app’s flaws may not only violate Google’s Unwanted Software Policy and Apple’s App Store guidelines but also China’s own laws and national standards pertaining to privacy protection, they said.


Indeed, the insecurity of the app is concerning on the eve of the Olympic Games, set to begin on Feb. 4, which have already sparked controversy. As early as February 2021, more than 180 human rights groups had called for governments to boycott the games due to worry that they will legitimize a Chinese regime currently engaging in significant human-rights violations, particularly against Uyghur people in China.


Governments including Canada, the United Kingdom and the United States are diplomatically boycotting the games, which means athletes from these countries can compete but government delegates will not attend the event.


The flaw in MY2022 also is worrying because the Olympics are known to be a major target for cybercriminals. Last year’s Summer Olympics in Japan saw more than [450 million](https://www.zdnet.com/article/nearly-450-million-cyberattacks-attempted-on-japan-olympics-infrastructure-ntt/) attempted cyberattacks, a significant increase from the 180 million attacks that occurred during the 2012 London Summer Olympics.


Unfortunately, the security issues found in MY2022, while concerning, are not unique and are likely found in many [mobile apps](https://threatpost.com/mhealth-apps-millions-cyberattacks/163966/). Such issues have spurred an epidemic of cyberattacks against devices with poor app security, noted one security professional.


“Not all mobile apps are susceptible to [man-in-the-middle](https://threatpost.com/apple-imessage-open-to-man-in-the-middle-spoofing-attacks/102610/) attacks, but most of them do contain undisclosed third parties who can access the same user data as the developer,” Chris Olson, CEO at enterprise digital security platform The Media Trust, wrote in an email to Threatpost. “Mobile users frequently assume that they are safe either because of app store policies, or because they have consented to terms of service – but third parties are not carefully checked by app reviewers, and they are rarely monitored for safety.”


Because of this, these apps “can be hijacked to execute phishing attacks, share sensitive data with fourth or fifth parties, suffer a data breach caused by lax security practices, or worse,” he noted.


*Photo of 2010 Olympic ceremony courtesy of [Tabercil](https://commons.wikimedia.org/wiki/File:2010_Winter_Olympic_-_Womens_downhill_medals.jpg). [Licensing details](https://creativecommons.org/licenses/by/2.0/).*


***Check out our free*** [***upcoming live and on-demand online town halls***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Derusbi]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Rover]] [[action.malware.name=Spark]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=Beijing]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Japan]] [[victim.continent.name=Asia]] [[victim.country.name=United Kingdom]] [[victim.continent.name=Europe]] [[victim.city.name=London]] [[victim.country.name=United Kingdom]] [[victim.continent.name=Europe]] [[victim.country.name=Canada]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[My2022]] [[Knockel]] [[Beijing]] [[Ssl]] [[Apps]] [[ThreatPost]]

