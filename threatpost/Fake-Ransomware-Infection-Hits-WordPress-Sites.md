# Fake Ransomware Infection Hits WordPress Sites
### WordPress sites have been splashed with ransomware warnings that are as real as dime-store cobwebs made out of spun polyester.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176410)
+ Date: November 17, 2021  5:06 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/17164923/Halloween-e1637185777828.jpeg)
Fake red-on-black warnings have been plastered to hundreds of WordPress sites, warning that they’ve been encrypted.


The warnings have at least one ransomware accoutrement that might look convincing at first blush: a countdown clock tick-tick-ticking away, warning site owners that they’ve got seven days, 10 hours, 21 minutes and 9 seconds to fork over 0.1 Bitcoin – about USD $6,000 at the time this story was posted – before the files are encrypted and go up in an irretrievable puff of e-smoke.


That’s a good chunk of change to any small-time user of the open-source content management system (CMS): “Not a negligible sum of money for an average website owner, to say the least!” Sucuri security analyst Ben Martin wrote in a Tuesday [post](https://blog.sucuri.net/2021/11/fake-ransomware-infection-spooks-website-owners.html). It’s most particularly steep given that it’s all smoke and mirrors.


Sucuri first noticed the fake vampire-movie-colored red-on-black warnings on Friday. It started out slow, and then it started to grow: Running a Google Search last week turned up only six results for the ransom demand – “FOR RESTORE SEND 0.1 BITCOIN”. That was up to 291 hits when the website security service provider reported its findings on Tuesday.


The screechy, bleedy, full-caps message:



> SITE ENCRYPTED  
> 
> FOR RESTORE SEND 0.1 BITCOIN: [address redacted]  
> 
> (create file on site /unlock.txt with transaction key inside)
> 
> 


Fortunately, before letting their precious Bitcoin fly out the window, at least one website admin reported the “ransomware” warning to Sucuri.


Tick, Tock, What a Crock
------------------------


The warning was clearly intended to get targets’ adrenaline pumping, instilling a sense of urgency with that ticking countdown clock. It’s a tried-and-true tool in swindlers’ kits, whether you’re talking [romance scams](https://threatpost.com/cybercrooks-304m-romance-scams/163972/), phoney Amazon package-delivery notices [designed to lift credentials](https://threatpost.com/amazon-phishing-campaigns-security-checks/157495/) or a gazillion other “Rush! Rush!” [frauds](https://threatpost.com/coronavirus-propagate-emotet/152404/).


But Sucuri researchers who tracked down and analyzed the fake ransomware said they found a whole lot of nothing. When running an on-site scan for a file that contained the bitcoin address, they found that the phony ransomware alert was just a simple HTML page generated by a bogus plugin, “./wp-content/plugins/directorist/directorist-base.php.”


They shared a screen capture, shown below, that showed the “very basic HTML” used to generate the ransom message:


As far as the countdown timer goes, it was generated by basic PHP, as shown below. The date could be edited “to instill more panic into the request,” Martin wrote. “Remember folks, rule number one about online scams like phishing is instilling a sense of urgency to the victim!”


Scrubbing the Site Clean
------------------------


Removing the infection was a snap: “All we had to do was remove the plugin from the wp-content/plugins directory,” Martin said. However, once they got the main website page back, the researchers found that all of the site’s pages and posts were leading to “404 Not Found” messages.


That was the malicious plugin’s parting shot: It included a basic SQL command that finds any posts and pages with the “publish” status and changes them to “null,” according to Sucuri’s post. The content was all still there in the database, but it couldn’t be viewed.


Again, it was a snap to undo: “This can be reversed with an equally simple SQL command,” according to Sucuri. To wit:



> UPDATE `wp\_posts` SET `post\_status` = ‘publish’ WHERE `post\_status` = ‘null’;
> 
> 


“This will publish any content in the database marked as *null.”* Martin wrote. “If you have other content marked as such, it will re-publish that, but that is certainly better than losing all your website posts and pages.”


Sucuri noted that the malicious plugin did have a file – ./wp-content/plugins/directorist/azz\_encrypt.php – that looked like it might actually be used for file encryption, but researchers didn’t see that file in any of the infections they analyzed – at least, not yet.


Who’s Spooking WordPress Admins?
--------------------------------


Sucuri’s client was located in the southern United States, but their site’s access logs showed multiple requests from a foreign IP address that was interacting with the malicious plugin using the plugin editor feature of wp-admin. “This suggests that the legitimate plugin was already installed on the website and later tampered with by the attackers,” Sucuri said.


“Interestingly, the very first request that we saw from the attacker IP address was from the wp-admin panel, suggesting that they had already established administrator access to the website before they began their shenanigans,” Martin said. “Whether they had brute forced the admin password using another IP address or had acquired the already-compromised login from the black market is anybody’s guess.”


Who Needs Ransomware When Fear Works Just Fine?
-----------------------------------------------


You can see the appeal: Skip the tricky task of creating real, live ransomware, and just head straight to the part where you scare the bejeezus out of people. Dan Piazza, technical product manager for [Stealthbits, now part of Netwrix](https://www.netwrix.com/netwrixstealthbitsmerger), told Threatpost that it’s not surprising to see fake ransomware attacks in the wake of the yearly increase in actual ransomware attacks, “especially considering how low-effort these fake attacks can be,” he said. “Less skilled attackers can take advantage of the growing fear of ransomware and try to profit with simple hacks, rather than well-developed and complex ransomware.”


Saumitra Das, CTO and cofounder of [Blue Hexagon](https://u7061146.ct.sendgrid.net/ls/click?upn=4tNED-2FM8iDZJQyQ53jATURk7nu5DOXPXjQHtUbQPB-2Bo-3DJfdf_q07lK5GAAVvAnbc-2Fr-2FBDhAPhoMvwzp-2Bdh4wgfTcF0AUhu01ZMXdKNJrsN0iCyDU7ehW0N22Ype9yCK1TM6XYzQ9CpkZyf7pccI4YxuRF0BJuYEbml5ScFK0-2F-2FZqd-2FdTfElUJI-2BPizGopBhzAnr1U9puogQQtd150y-2BAZSsWRgg1XAe8FBCRqq3OvsINV06lTiOU4sB5bE6EwwWnIDy4EwcZEC81kqzAmsvBpCglQKTZ2vfO-2FzRBZrFaHXA-2FedQPxAeIII-2FoV2FRWomtPdAii6ke00Vb2xb2B3CWK-2FqW7zSO9hQSFi9mLQ5JkU9r58C8efnEEnClPj-2BdB-2F4enu7uEqQzwufsidZLP565E9VNBrwE-3D), called this one an interesting take on extorting victims – one that “may succeed for site owners who fear loss of business.”


“Ransomware actors are innovating on extorting rather than encryption given that backup technology and its adoption has improved in the last few years,” Das pointed out. “This is just another example of extortion innovation. Attackers are not just encrypting but naming and shaming the brand, exfiltrating data, threatening executives and users as well.”


Even Fake Ransomware Shows Something’s Vulnerable
-------------------------------------------------


Piazza told Threatpost that it doesn’t matter that this attack was fake. The fact is that these WordPress sites were indeed compromised via their most privileged attack surface – “a WordPress Admin,” he said via email.


“Should the attackers have wanted to deploy actual ransomware, then they already had the keys to the kingdom,” Piazza said.


To stay vigilant against real ransomware, Piazza advised that admins make sure that their sites are running the latest updates to the CMS, any plugins they’re using, and any libraries or frameworks they’ve implemented in their source code.


“Patched zero day exploits are still a big target for attackers, as many websites remain on older versions of their software,” he pointed out.


“Access management is also essential, to limit the number of privileged admins or even the lifecycle of those admins,” Piazza continued. “Privileged Access Management software can help here, by providing just-in-time permissions and even admin accounts that only exist when needed.”


Scheduled backups are also a must, he said. “If backups are stored completely separate from the website servers, then it’s easy to get back up and running in the event of compromise.”


He also suggested that multi-factor authentication (MFA) be used for all privileged credentials, pointing to a Microsoft report that [MFA can block over 99.9 percent of account compromise attacks](https://www.microsoft.com/security/blog/2019/08/20/one-simple-action-you-can-take-to-prevent-99-9-percent-of-account-attacks/).


*Image courtesy of [Disney Parks](https://disneyparks.disney.go.com/blog/2016/09/wonderfalldisney-7-photos-of-mickeys-not-so-scary-halloween-party/).*


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost for “***[***An Intro to OSquery and CloudQuery***](https://bit.ly/3wf2vTP)***,” an on-demand Town Hall with Eric Kaiser, Uptycs’ senior security engineer, and find out how this open-source tool can help tame security across your organization’s entire campus.***


[***Register NOW***](https://bit.ly/3wf2vTP)***for the on-demand event!***




#### Tags:
[[website]] [[ransomware]] [[said.]] [[plugin]] [[WordPress]] [[“This]] [[they’ve]] [[it’s]] [[IP]] [[ransomware,]] [[ThreatPost]]