# Fortinet, Shopify and more report issues after root CA certificate from Lets Encrypt expires
### Experts had been warning for weeks that there would be issues resulting from the expiration of root CA certificates provided by Lets Encrypt.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/fortinet-shopify-others-report-issues-after-root-ca-certificate-from-lets-encrypt-expires/)
+ Date: September 30, 2021
+ Author: Jonathan Greig


## Article:
Unknown

A number of websites and services reported issues on Thursday thanks to the expiration of a root certificate provided by Let's Encrypt, one of the largest providers of HTTPS certificates. 

At around 10 am ET, IdentTrust DST Root CA X3 expired according to Scott Helme, founder of Security Headers. He has been tracking the issue and explained [millions of websites rely on Let's Encrypt services](https://www.zdnet.com/article/lets-encrypt-issues-1-billionth-web-security-certificate/) and without them, some older devices will no longer be able to verify certain certificates. 

Let's Encrypt operates as a free non-profit that makes sure the connections between your device and the internet are secure and encrypted. 

Despite advance warning that the expiration date would would be on September 30, when the deadline hit, dozens of users reported issues with a variety of services and websites.

Helme told ZDNet that he confirmed issues with Palo Alto, Bluecoat, Cisco Umbrella, [Catchpoint](https://status.catchpoint.com/incidents/f5yl89kygf12), Guardian Firewall, Monday.com, PFsense, Google Cloud Monitoring, Azure Application Gateway, OVH, Auth0, [Shopify](https://www.shopifystatus.com/incidents), Xero, QuickBooks, Fortinet, Heroku, Rocket League, InstaPage, Ledger, [Netlify](https://answers.netlify.com/t/ways-to-work-around-ssl-caused-build-failures-server-certificate-verification-failed/44945) and Cloudflare Pages, but noted that there may be more. 

"There are a couple of ways to solve this depending on what the exact problem is but it boils down to: The service/website needs to update the certificate chain they are serving to clients or, the client talking to the website/service needs an update," Helme explained.

"For the affected companies it's not like everything is down, but they're certainly having service issues and have incidents open with staff working to resolve. In many ways I've been talking about this for over a year since it last happened, but it's a difficult problem to identify. it's like looking for something that could cause a fire: it's really obvious when you can see the smoke!"






Some sites posted notices on their website about potential issues and many have resolved the issues. Shopify [posted](https://www.shopifystatus.com/incidents) a note on its incident page that by about 3:30 pm, merchant and company partners who were struggling to login had their services restored. Merchant authentication for Support interactions have also been restored, the company said. 

Fortinet told ZDNet they were aware of and have investigated the issue relating to the expired root CA certificate provided by Lets Encrypt.   

"We are communicating directly with customers and have provided a temporary workaround. Additionally, we are working on a longer-term solution to address this edge case issue directly within our product," the company said in a statement. 

Digital certificates expert Tim Callan said all modern digital systems depend on certificates for their continued operation, including those that secure our cyber and physical environments. 

"If software depends on an expired root to validate the trust chain for a certificate, then the certificate's trust will fail and in most cases the software will cease to function correctly. The consequences of that are as broad and varied as our individual systems are, and many times cascading failures or 'downstream' failures will lead to problems with entirely different systems than the one with the original certificate trust problem," Callan said. 

"IT systems that enforce or monitor security policies can stop working. Alerting and reporting systems can fail. Or, if the processes that humans depend on to do our work stop functioning, often those people will find "workarounds" that are fundamentally insecure."

Callan added that outages can occur when developers embedded in lines of business operations or other skunkworks projects "obtain certificates" without the knowledge of central IT and then move on to new tasks or otherwise fail to monitor the lifecycle of these certificates. 

He noted that most systems will be able to weather a root expiration because of modern root chaining capabilities that allow another root to establish trust. 

"However, legacy systems or those with previously unaddressed (or unknown) certificate handling bugs are at risk for failures like these to occur. In the event of a commonly used root from a popular CA, the risk of these failures goes up considerably," Callan explained.

TechCrunch [reported](https://techcrunch.com/2021/09/21/lets-encrypt-root-expiry/) that devices that may face issues include older macOS 2016 and Windows XP (with Service Pack 3) as well as older versions of Playstations and any tools relying on OpenSSL 1.0.2 or earlier. 

Other experts said PlayStations 4s or earlier devices that have not had their firmware upgraded will not be able to access the Internet. Devices like Android 7.1.1 or earlier will also be affected.

According to Callan, most modern software allows the use of sophisticated trust chains that allow root transitions without requiring the replacement of production certificates. But those that are old or poorly designed or containing trust chain handling bugs may not handle this transition correctly, leading to various potential failures. 

As many of the affected companies have since done, Callan suggested enterprises take an inventory of the systems using certificates and the actual certificates in use before ensuring that software has the latest root certificates in its root store.

"By identifying where potential failure points occur, IT departments can investigate these systems ahead of time to identify problem areas and implement fixes. If you can set up a version of the system in a sandbox environment, then it's easy to test expected behaviour once the root expiration occurs," Callan said. 

"Just set the client system clock forward to a date after the expiration date to ensure certificate chaining will work correctly. Alternately, you can manually uninstall or distrust the root that is set to expire (in the sandbox environment, of course) to assure yourself that systems are only using the newer roots."

He added that the popularity of DevOps-friendly architectures like containerization, virtualization and cloud has greatly increased the number of certificates the enterprise needs, while radically decreasing their average lifespan.

"That means many more expiration events, much more administration time required, and greatly increased risk of a failed renewal," he said. 

Digital Shadows senior cyber threat analyst Sean Nikkel told ZDNet that Let's Encrypt put everyone on notice back in May about the expiration of the Root CA today and offered alternatives and workarounds to ensure that devices would not be affected during the changeover. 

They have also kept a running forum thread open on this issue with fairly quick responses, Nikkel added.

"A not-great practice that's been floated already as a workaround to the problem is allowing untrusted or invalid certificates. Users should be cautious about making a move that potentially opens the door to attackers using compromised certificates," Nikkel said.  

"Some users have recommended settings allowing for expired certificates from trusted issuers; however, these can also have malicious uses. In any case, administrators should examine the best solution for them but also understand the risks to any workarounds. Alternatively, administrators can look at alternate trust paths by using the intermediate certificate that Let's Encrypt has set up or following suggested configurations from their May bulletin."





#### Tags:
[[certificates.]] [[said.]] [[ZDNet]] [[Nikkel]] [[ZDNet]]
