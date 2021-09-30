# Thousands of University Wi-Fi Networks Expose Log-In Credentials
### Certificate misconfigurations of the EAP protocol in Eduroam (and likely other networks globally) threaten Android and Windows users.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175157)
+ Date: September 30, 2021  7:29 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/30071950/Corpus-Christi-College-University-of-Cambridge-England-e1633000805684.jpg)
Multiple configuration flaws in a free Wi-Fi network used by numerous universities can allow access to usernames and passwords of students and faculty who connect to the system from Android and Windows devices, researchers have found.


A research team from WizCase, led by researcher Ata Hakçıl, reviewed 3,100 configurations of Eduroam at universities throughout Europe, finding that more than half of them have issues that can be exploited by threat actors. The misconfiguration danger could extend to other organizations globally as well, they added.


Eduroam provides free Wi-Fi connections at participating institutions. It assigns students, researchers and faculty members log-in credentials that allow them to obtain internet connectivity across different institutions by using credentials from their own university.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Specifically, researchers discovered flaws in the implementation of the Extensible Authentication Protocol (EAP) that Eduroam uses, which provides different stages of authentication as people connect to the network. Some of those authentication phases aren’t configured properly in some universities, opening security holes, they said.


“Any students or faculty members using Eduroam or similar EAP-based Wi-Fi networks in their faculties with the wrong configuration are at risk,” researchers wrote in [a report posted](https://www.wizcase.com/blog/eduroam-vulnerability-report/) Wednesday. “If you are using an Android device and have Eduroam Wi-Fi set to auto-connect, malicious people could capture your plaintext username and password by only getting 20 or so meters in range of you.”


**Network ‘Evil Twin’**
-----------------------


For the research, WizCase examined various configuration-setup guides and set up a test environment with different attack scenarios. Overall, their findings showed that in most of the universities with misconfigured networks, threat actors can configure an “evil twin” Eduroam network that a user would think was the real network, particularly on Android devices.


“This could result in these devices automatically sending their stored credentials in order to connect to the evil twin Wi-Fi network for users not using eduroamCAT,” which is Eduroam’s catalog application which handles certificate checks, they wrote.


Researchers stressed that the problem is not the fault of any technical vulnerability from Eduroam’s services or technology, but from erroneous configuration instructions that the universities’ own network administrators provide to those setting up access, they said.


Indeed, while each institution provides resources and people to help keep Eduroam running, there is no centralized management for the network — either as a whole or at each university where the system is in place, researchers observed. This means that “a simple misconfiguration could make it the target of hackers,” they said.


Researchers further pinpointed the problem by breaking down the multiple sequential phases of EAP authentication, finding that poor implementation of the last stage of this authentication, called “Inner Authentication,” is the root of the issue.


In EAP, Inner Authentication is done in one of two ways. One way is to use Plain Authentication Protocol (PAP), which transfers the credentials of the users to the authentication server in plaintext, relying on the Outer Authentication to completely encrypt the traffic using a server certificate.


The other way uses Microsoft Challenge Handshake Authentication Protocol version 2 (MSCHAPv2, which recognizes there may be failures in the “Outer Authentication” stage, and transfers the password in a hashed, non-plaintext form, researchers said.


The vulnerable universities use the former.


**Botched Certificate Checks**
------------------------------


The problem lies in that not every OS implements the certificate check to secure the connection properly—Android being among those OSes, researchers wrote.


“When a network with the same Wi-Fi name appears, Android devices will not check whether this certificate is trustworthy or not, and will not even notify the user about the certificate before connecting,” they explained.


This means if an Android user has enabled auto-connect for a network using a server certificate, Android devices will automatically attempt to connect to this network and send stored credentials, and the user is none the wiser, researchers said.


Even an OS that implements certificate checks properly can expose data because often a user doesn’t know what a certificate check means, and so will allow the connection to continue even if they are receive an alert about the certificate, they added. This means that the issue can occur on Windows as well if a system is misconfigured, researchers said.


However, iOS devices aren’t vulnerable to the issue because they don’t allow connections to EAP networks without installing the EAP configuration file, which enforces the validity of the server-side certificate, researchers said.


Of the 3,100 Euroam participating university configurations reviewed by WizCase, 2,100 scattered across Europe are potentially affected by the problem, researchers said. It could be mitigated by reverting to the second method of Inner Authentication, according to the firm.


WizCase contacted Eduroam in December to disclose their findings, receiving a response on the same day, researchers said. Eduroam representatives said they are aware of “Eduroam identity providers who do not follow the requirements of the Eduroam policy, and leave their own users unprotected,” agreeing with researchers’ assessment that this behavior is “unacceptable,” according to WizCase. It’s unclear if Eduroam contacted its customers to alert them to the issue.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[Eduroam]] [[said.]] [[Wi-Fi]] [[Android]] [[EAP]] [[certificate,]] [[ThreatPost]]
