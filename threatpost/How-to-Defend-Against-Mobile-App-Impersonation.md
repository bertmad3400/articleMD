# How to Defend Against Mobile App Impersonation
### Despite tight security measures by Google/Apple, cybercriminals still find ways to bypass fake app checks to plant malware on mobile devices. Dave Stewart, CEO of Approov, discusses technical approaches to defense against this.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176519)
+ Date: November 23, 2021  9:00 am
+ Author: David Stewart


## Article:
Most users who install applications through legitimate channels such as the Google Play Store or the Apple Store do so with complete trust that their information is safe from malicious attacks. This makes sense, because they’re the official app stores for across the globe.


However, despite tight security measures by Google and Apple, cybercriminals still find ways to bypass these checks. They do this through app impersonation.


For instance, since Android lets users side-load and install apps downloaded from non-store sources, cyberattackers take advantage by creating clone apps that mimic legitimate ones. They then use the fake apps to collect data or credentials for malicious use.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


An example was when India banned [TikTok](https://asia.nikkei.com/Business/Technology/India-permanently-bans-TikTok-and-58-other-Chinese-apps). A clone called [TikTok Pro](https://www.news18.com/news/tech/is-tiktok-back-in-india-viral-message-of-tiktok-pro-app-may-steal-your-data-2708241.html) came up immediately with malicious intentions to steal data from users’ devices. Attackers also took advantage of COVID-19 fears to collect user data through [fake tracking apps](https://blog.avast.com/fake-covid-19-tracking-apps-spotted-avast).


Cybercriminals are capitalizing on the remote-work trend as more companies allow employees to access business applications through mobile devices. Additionally, personal internet networks rarely have the kind of security measures available within an office environment, such as firewalls, which [creates ample room](https://threatpost.com/fake-chrome-app-worming-smish-cyberattack/166038/) for attackers to scrape business data.


Below we look at ways to identify app impersonation, tools to defend yourself from attacks and measures to put in place for better security.


2 Types of App Impersonation
----------------------------


In addition to the examples given above, app impersonation occurs in many other ways. Remember, the sole nefarious intent of a cybercriminal is to access user data, backend APIs and business information. Below are the two primary app impersonation methods identified in 2021:


Hackers have found an opportunity through cloning applications by creating similar-looking applications that impersonate legitimate ones. Hackers collect sensitive information such as banking details, credit-card information and biometric information through the cloned applications.


As much as Google Play has implemented more robust security measures, they sometimes prove ineffective because this is purely a cat-and-mouse game; as soon as the rogue mobile apps get pulled out of the store, they come in again in another guise. Moreover, side-loading of apps is inadvisable but still happens, creating another attack vector.


Cybercriminals use the information they steal for malicious purposes like account takeover, to redirect payments or to syphon off rewards points. Or, the objective may be as simple as selling personal information on the Dark Web.


API manipulation is a mechanism aimed at stealing business or personal data, or gaming a company’s business for commercial gain.  It’s carried out by exploiting vulnerabilities or bugs in the APIs themselves, or by using valid credentials which have been stolen from other businesses – or bought on the Dark Web – in order to access back-end systems. Both attack vectors are based on scripts and use API keys which have been extracted from the mobile apps. [Gartner’s research estimates that APIs](https://www.gartner.com/en/webinars/4002323/api-security-protect-your-apis-from-attacks-and-data-breaches) will be the leading attack surface by 2022.


How to Defend against App Impersonation
---------------------------------------


These are three main methods that have proven effective defenses against mobile app impersonation:


Many people believe that protecting mobile apps protects the APIs that they consume. Unfortunately, this is false logic. In reality, a genuine mobile app is a hacking toolbox for bad actors since they can use it to architect and implement fake versions of the app.


Further, they can study the API requests/responses and quickly build a script which generates API sequences which are indistinguishable from genuine mobile app traffic.


It is therefore important to consider API security separately from mobile app security. An effective API-protection tool must be able to verify that incoming API requests are coming from genuine mobile app instances which are operating in uncompromised runtime environments.


Attackers know that if they can get a fake app installed on your mobile device, they can manipulate your intentions as well as extracting valuable business and personal data. Preventing fake apps from entering the official app stores is probably impossible, as is stopping users from side-loading apps from other sources, but what can be done is to ensure that none of these bad apps can communicate with your backend systems.


Mobile app attestation is a highly cryptographically secure method through which an app can be proved to be a genuine instance of the original app which was uploaded into the app stores. If this proof can be passed to the backend system along with each API call, it is possible to shut out all fake apps, regardless of if they came from the app stores or through side-loading.


[Penetration testing](https://blog.approov.io/pentesting-mobile-platforms-a-short-guide-based-on-experience) regularly exposes vulnerabilities by simulating potential attacks on your application to identify loopholes before hackers gain access to them. The best practice is to work with an external pentester, because they’re less familiar with your systems and can independently identify flaws more effectively.


There are two pentesting methods:


Best Practices Against App Impersonation
----------------------------------------


The best defensive tool against app impersonation will protect user information as well as your APIs, so you can focus on building better features and growing your platform.


These tools should integrate into your iOS or Android mobile app by installing an SDK that interacts with a cloud service which can verify the app’s authenticity. A short (~5 minute) lifetime token could be passed to your API backend for instance, to prove that the API request is from a genuine source and meets all the runtime requirements.


Every transaction should also be checked against a security policy that you define, providing an end-to-end security process for your app and your APIs.


***Dave Stewart is CEO at [Approov.](https://www.approov.io/)***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)




#### Tags:
[[apps]] [[API]] [[backend]] [[Google]] [[ThreatPost]]
