# Digital State IDs Start Rollouts Despite Privacy Concerns
### Eight states are introducing drivers licenses and identification cards available for use on Apple iPhones and Watches, but critics warn about the dangers of eliminating the use of a paper-based system entirely.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169136)
+ Date: September 2, 2021  7:28 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/02071602/digital-drivers-license-e1630581382983.png)
Apple has unveiled the first eight states that will roll out digital IDs and drivers licenses on its mobile devices, despite critics’ concerns that the introduction of purely digital forms of identification will raise privacy, security and equanimity issues.


Arizona and Georgia will be the first states to introduce the ability for their residents to add their driver’s license or state ID to Wallet on their iPhone and Apple Watch, the company said Wednesday. Connecticut, Iowa, Kentucky, Maryland, Oklahoma and Utah will follow.


The plan is in cooperation with the Transportation Security Administration (TSA), which also will establish certain airport security checkpoints and lanes for people wanting to use their digital DLs and IDs to pass through, as the United States government begins testing the rollout.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“The addition of driver’s licenses and state IDs to Apple Wallet is an important step in our vision of replacing the physical wallet with a secure and easy-to-use mobile wallet,” said Jennifer Bailey, Apple’s vice president of Apple Pay and Apple Wallet, in [a press statement](https://www.apple.com/newsroom/2021/09/apple-announces-first-states-to-adopt-drivers-licenses-and-state-ids-in-wallet/) unveiling the news.


Apple first unveiled a plan to provide digital ID in its iOS in June at the company’s Worldwide Developers Conference. The technology will be available with the release of iOS 15, which is expected sometime this autumn.


**Keeping It Secure**
---------------------


To assuage security fears that come with storing people’s identity on its devices, Apple is asserting that state DLs and IDs stored in Wallet on iPhone and Apple Watch will “take full advantage of the privacy and security” built into the devices, the company said.


Apple’s mobile ID implementation supports the [ISO 18013-5 mDL](https://www.iso.org/standard/69084.html), or mobile driver’s license standard being used by the government for storing digital identities. Apple played an active role in developing the standard, which the company said sets clear guidelines for the industry about how to protect consumers’ privacy when presenting an ID or driver’s license through a mobile device, the company said.


Moreover, Apple devices will encrypt ID data to protect it against potential theft by threat actors, with DLs and IDs stored in Wallet presented digitally through encrypted communication directly between the device and the identity reader, the company said. This precludes the need for users to unlock, show or hand over their device to someone.


Additionally, the use of Face ID and Touch ID will ensure that only the person who added the ID to the device can present it or view it on the device, according to Apple.


**Icelandic Snafu**
-------------------


Despite these security protections, there already has been a major issue with a rollout in Iceland of digital DLs that used Apple’s [Wallet passes](https://developer.apple.com/documentation/walletpasses), distributed via the [Passkit API](https://developer.apple.com/documentation/passkit) for digital identities. A [report](https://syndis.is/2021/09/01/e-license) by security firm Syndis outlined key flaws in the use of Apple Wallet passes for Iceland’s rollout in January 2020.


Wallet passes are distributed as PKPass files—which are in essence a signed .ZIP archive that contains multiple files with a digital signature to detect if the files have been changed. Although the digital signature sounds good on the surface, the report outlined “two main problems with it” that allowed people to forge or modify their digital DLs.


“First, it is sufficient to have an Apple developer account to obtain a signing certificate for wallet passes, and therefore they can be obtained by anyone,” according to the report. “Thus, anyone can alter the license and obtain a new valid license by updating the manifest and signing with their own signing key, thereby creating a e-license near indistinguishable from one issued by the government.”


Another issue was that Android devices did not have any available apps upon rollout to validate the signature, so people with Android smartphones “can alter the contents of the license to your heart’s content, and the Android wallet apps will have no problem importing the new and improved license,” researchers wrote.


The Icelandic government also took a big misstep by not immediately upon rollout introducing scanner technology to digitally scan the IDs automatically on appointed devices—which will be the case in the United States. This meant that people had to physically look at the ID on the device to verify someone’s identity, allowing for various exploitations of the technology, according to the report.


For example, teenagers in Iceland who wanted to enter bars and clubs in Iceland’s capital of Reykjavik began altering digital IDs using screenshots to make themselves appear older, thus gaining entry into establishments where it was not legal for them to be.


“It is disappointing to see how a truly useful and popular idea has been mishandled and poorly implemented,” according to the report. “E-licenses are clearly a system that people want, but with the regular news stories about forgery, the risk of public distrust in the system increases. The main lesson to take away from this case is that security should never be an afterthought.”


**Privacy and Other Concerns**
------------------------------


Indeed, privacy and civil-rights advocacy groups in the United States also are concerned about how an improperly implemented and managed move from a card-based national identity system to one that is fully digital can lead to myriad problems.


Privacy and individual-rights groups like the Electronic Frontier Foundation (EFF), the American Civil Liberties Union (ACLU) and the Electronic Privacy Information Center (EPIC) believe that if digital IDs are not designed carefully, they could eventually lead to a scenario “in which every time we walk through a door or buy coffee, a record of the event is collected and aggregated,” the EFF wrote in a [blog post](https://www.eff.org/deeplinks/2021/07/dhss-flawed-plan-mobile-drivers-licenses) published in late July.


The EFF’s blog post was a response to the unveiling by the Department of Homeland Security (DHS) of proposed minimum standards to govern digital DLs and IDs ahead of their rollout. The EFF, ACLU and EPI also collectively [released joint comments](https://www.eff.org/document/2021-07-29-aclu-eff-epic-comments-re-dhss-mdl) raising concerns over the use of digital ID technology and the potentially dangerous precedent it could set to track people and their data, expose their data to security threats, or require people to show proof of identity for every-day activities.


The privacy groups also pointed out that digital IDs can also lead to further marginalization of people who are already at a disadvantage in society and may not have the financial means to own a smartphone, something “that could have significant implications for equity and fairness in American life,” they said in their public comments.


In the worst case, the privacy groups argued, a badly executed digital ID system “would make it nearly impossible to engage in online activities that aren’t tied to our verified, real-world identities, thus hampering the ability to engage in constitutionally protected anonymous speech and facilitating privacy-destroying persistent tracking of our activities and associations,” they wrote.


These concerns have been seen playing out in the COVID-19 pandemic response in some parts of the world. The European Union (EU) has already rolled out the [EU Digital Covid Certificate](https://ec.europa.eu/info/live-work-travel-eu/coronavirus-response/safe-covid-19-vaccines-europeans/eu-digital-covid-certificate_en), which assigns citizens a QR code through which their status as vaccinated, recently tested or recovered from COVID-19 can be accessed. The so-called “green passport” is required to different degrees in various countries for entering public places such as restaurants, cafes, shopping malls and attending events.


In some places, people who only have a paper proving COVID-19 vaccination status are being denied entry into public spaces because they have not signed up for the digital program and thus do not have a QR code, observers said — perhaps due to the ease of [faking vaccine records](https://threatpost.com/telegram-forged-covid-19-vaccine-cards/166093/).


Cities in the United States, such as New York and San Francisco, have since followed suit with similar vaccine-status requirements, with New York also permitting people to do it digitally using something called the [Excelsior Pass,](https://covid19vaccine.health.ny.gov/excelsior-pass) which the EFF noted [could have](https://www.eff.org/deeplinks/2021/08/vaccine-passport-missteps-we-should-not-repeat) data security problems.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***



 




#### Tags:
[[DLs]] [[driver’s]] [[devices,]] [[Apple’s]] [[said.]] [[report.]] [[Android]] [[COVID-19]] [[ThreatPost]]
