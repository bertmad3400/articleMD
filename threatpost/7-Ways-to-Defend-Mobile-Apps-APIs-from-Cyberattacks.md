# 7 Ways to Defend Mobile Apps, APIs from Cyberattacks
### David Stewart, CEO, Approov, discusses the top mobile attack routes the bad guys use and the best defenses organizations can deploy against them. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169144)
+ Date: September 2, 2021  8:51 am
+ Author: David Stewart


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2017/07/06223721/AdobeStock_72773662-e1630586165222.jpeg)
There are two essential elements driving progress in today’s digital-first economy: Mobile applications and the application programming interfaces (APIs) that allow  those applications to communicate and exchange data with each other.


The growth in these two technologies has exposed users and their data to significant security threats, namely:


Mobile app security threats have arisen over the years. Below are some alarming statistics:


Read on for the top attack routes the bad guys use and the best defenses organizations can deploy against them.


How Bad Actors Exploit Mobile Attack Surfaces To Hack Your Device
-----------------------------------------------------------------


Mobile applications work with the assumption that legitimate users use your app without malicious intentions. As a result, hackers will use attack surfaces to extract confidential information they can use to penetrate your device. There are five attack surfaces that bad actors target to gain access to your data:


The Process of Targeting Your Applications
------------------------------------------


A cybercriminal can launch an attack across the surfaces above through the detailed process we outline below:


There are four ways of preparing an attack:


After preparing the paths to gain access and collect information, these are the methods hackers use to execute their attack strategy:


7 Ways To Protect Mobile Apps and APIs from Attackers
-----------------------------------------------------


Below are the best strategies to protect your mobile applications from hackers:


Approve secure connections only after authenticating the identity of the server request. To authenticate user identities, implement Secure Sockets Layer/ Transport Layer Security (SSL/TLS) protocols on the app’s transport channels that scan sensitive data such as credentials and tokens.


You should also use certificate pinning and industry-approved certificates signed by trusted Certificate Authority providers to prevent self-signed certificates.


Input validation checks if credentials and login information is structured appropriately to prevent harmful code from accessing your app.


Validation takes place before a mobile application accepts the user’s personal information. This process protects the app from attackers injecting destructive code into your app.


Input validation should also apply to your third-party vendors and partners. Attackers might try to hack your app by pretending to be your service provider or a trusted regulator.


Your mobile app’s data storage is another avenue that attackers can target. Vulnerabilities occur in storage places such as SQL databases, cookies, configuration files and binary data stores. Additionally, dangerous actors circumvent poorly implemented security features by bypassing encryption libraries. A common avenue that attackers target is jail-broken or rooted devices. When the owner jail-breaks/roots their device, they undermine the gadget’s in-built security, making it easier for hackers to gain access.


To protect your data stores from attackers, encrypt local files that contain sensitive information using your device’s security library. You can also reduce the number of app requests and permissions to prevent apps from gaining access.


To reduce insecure and low-quality code instances, apply secure coding practices such as the [OWASP Secure Coding Guidelines](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/migrated_content) and use status analysis tools such as [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) to check the security of your work during the development process.


Maintain consistent, secure coding principles that do not result in vulnerable code.


Once your code is ready to deploy, don’t forget to apply an obfuscation tool such as [ProGuard](https://www.guardsquare.com/proguard) to place a cloak around your labors and keep prying eyes off it.


There are multiple ways to ensure proper authorization and authentication to protect mobile apps from attacks:


Reverse engineering is one way that hackers apply to attack an app’s integrity. To prevent such scenarios, limit the client’s capabilities and retain most of the app’s functionality to the server’s side. For example, reduce user functionality and client-side permissions to prevent hackers from gaining access to your codebase. API keys are a security risk on their own and are difficult to hide in a mobile app. So protect their illegitimate use by ensuring that a second, independent factor is required by the backend server alongside the API key to mitigate the risk.


***David Stewart is CEO at Approov.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***


 




#### Tags:
[[app’s]] [[app.]] [[ThreatPost]]
