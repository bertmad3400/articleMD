# New Gummy Browser attack lets hackers spoof tracking profiles
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-gummy-browser-attack-lets-hackers-spoof-tracking-profiles/)
+ Date: October 20, 2021
+ Author: Bill Toulas


## Article:
![gummybears](https://www.bleepstatic.com/content/hl-images/2021/10/20/gummybears.jpg)


University researchers in the US have developed a new fingerprint capturing and browser spoofing attack called Gummy Browsers. They warn how easy the attack is to carry out and the severe implications it can have.


A digital fingerprint is a unique online identifier associated with a particular user based on a combination of a device's characteristics. These characteristics could include a user's IP address, browser and OS version, [installed applications](https://www.bleepingcomputer.com/news/security/cross-browser-tracking-vulnerability-tracks-you-via-installed-apps/), active add-ons, cookies, and even how the user moves their mouse or types on the keyboard.


Websites and advertisers can use these fingerprints to confirm a visitor is a human, track a user between sites, or for targeted advertising.


Digital fingerprints are so valuable that they are [sold on dark web marketplaces](https://www.bleepingcomputer.com/news/security/criminal-market-sells-over-60k-digital-identities-for-5-200/), so threat actors and scammers can spoof users' online identities to make account takeovers easier or for ad fraud.


Gummy Browsers
--------------


The 'Gummy Browsers' attack is the process of capturing a person's fingerprint by making them visit an attacker-controlled website and then using that fingerprint on a target platform to spoof that person's identity.



!['Gummy Browsers' attack overview](https://www.bleepstatic.com/images/news/u/1220909/Security/overview.jpg)**'Gummy Browsers' attack overview**  
*Source: Arxiv.org*
After generating a fingerprint of a user using existing or custom scripts, the researchers developed the following method to spoof the user on other sites:


* **Script injection** – Spoofing the victim’s fingerprint by executing scripts (with Selenium) that serve values extracted by the JavaScript API calls.
* **Browser setting** and **debugging tool** – Both can be used to change the browser attributes to any custom value, affecting both the JavaScript API and the corresponding value in the HTTP header.
* **Script modification** – Changing the browser properties with spoofed values by modifying the scripts embedded in the website before they are sent to the webserver.


By capturing the victim's fingerprint only once, the researchers said they they could trick state-of-the-art fingerprinting systems such as FPStalker and Panopliclick for extensive periods.


"Our results showed that Gummy Browsers can successfully impersonate the victim’s browser transparently almost all the time without affecting the tracking of legitimate users," the researchers explain in an [Arxiv paper](http://arxiv.org/pdf/2110.10129.pdf) published yesterday.


"Since acquiring and spoofing the browser characteristics is oblivious to both the user and the remote web-server, Gummy Browsers can be launched easily while remaining hard to detect"


Their tests returned a true positive rate of 0.9 and raised no alarms to alert the spoofed user that their online 'identity' was stolen.



![True positive rate (TPR) diagrams. ](https://www.bleepstatic.com/images/news/u/1220909/Security/tpr%20diagrams.jpg)**True positive rate (TPR) diagrams.**  
*Source: Arxiv.org*
Attack can be heavily abused
----------------------------


The researchers state that threat actors can easily use the Gummy Bear attack to trick systems utilizing fingerprinting.


"The impact of Gummy Browsers can be devastating and lasting on the online security and privacy of the users, especially given that browser-fingerprinting is starting to get widely adopted in the real world," warned the researchers.


"In light of this attack, our work raises the question of whether browser fingerprinting is safe to deploy on a large scale."


The attack can spoof a user's identity to make a script appear as a human rather than a bot and be served targeted ads to perform ad fraud.


The Gummy Bear attack may also help bypass security features used to detect legitimate users in authentication services. Examples of authentication systems said to be using fingerprinting include Oracle, Inauth, and SecureAuth IdP.


Finally, many banks and retail sites use fingerprinting as part of their fraud detection mechanisms, which can be bypassed by spoofing a legitimate user's identity.




#### Tags:
[[]] [[Bleeping Computer]]
