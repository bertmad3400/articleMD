# US govt sites showing porn, viagra ads share a common software vendor
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/us-govt-sites-showing-porn-viagra-ads-share-a-common-software-vendor/)
+ Date: September 17, 2021
+ Author: Ax Sharma


## Article:
![capitol building and eggplant](https://www.bleepstatic.com/content/hl-images/2021/09/17/capitol-eggplant.png)


Multiple U.S. government sites using .gov and .mil domains have been seen hosting porn and spam content, such as Viagra ads, in the last year.


A security researcher noticed all of these sites share a common software vendor.


United States of Porn
---------------------


Security researcher Zach Edwards has traced the issue down to these .gov and .mil domains using a common software product provided by Laserfiche, a government contractor.


Laserfiche provides services to the FBI, CIA, U.S. Treasury, the military, and many more government bodies.


The software product called Laserfiche Forms contains a vulnerability that has allowed threat actors to push malicious and spam content on reputable government sites.



![gov sites indexed by google](https://www.bleepstatic.com/images/news/u/1164866/2021/Sep-2021/gov-vuln/google-results.jpg)**Gov sites with spam content indexed by Google**(BleepingComputer)
"This vulnerability created phishing lures on .gov and .mil domains that would push visitors into malicious redirects, and potentially target these victims with other exploits," Edwards told *Motherboard* who [first reported](https://www.vice.com/en/article/pkb5qy/why-government-and-military-sites-are-hosting-porn-and-viagra-adsovernm) on the researcher's findings.


Edwards, who has been [tracking](https://twitter.com/thezedwards/status/1438546541652832259) the flaw down for over a year has caught websites of [U.S. Senator Jon Tester](https://twitter.com/thezedwards/status/1375118316021280772) and the Minnesota National Guard [[1](http://web.archive.org/web/20210914181655/https://webcache.googleusercontent.com/search?q=cache%3Acxm1jQe2uNEJ%3Ahttps%3A%2F%2Fminnesotanationalguard.ng.mil%2Fdocuments%2F2019%2F12%2Ffamily-statement-for-sgt-kort-m-plantenberg.pdf+&cd=6&hl=en&ct=clnk&gl=us), [2](https://archive.is/sPMG3)] sending users to Viagra product pages, for example.


He shared a video demonstrating the vulnerability in action and says he's seen this behavior "on probably 50 different government subdomains."



This isn't the only attack vector leveraged by spammers. Previously, attackers have [abused the open redirect functionality](https://www.bleepingcomputer.com/news/security/us-government-sites-abused-to-redirect-users-to-porn-sites/) on government websites like that of the National Weather Service website sites to boost SEO for their content and redirect users to porn sites.


Laiserfiche releases cleanup tool, not all versions fixed
---------------------------------------------------------


Laserfiche has now released a security advisory for the vulnerability, along with instructions on how to clean up your website from spam content.


According to the company, the root cause of the issue is an unauthenticated File Upload vulnerability.


Parts of Laserfiche Forms contain a public form that has a [file upload field](https://doc.laserfiche.com/laserfiche.documentation/11/administration/en-us/Default.htm#../Subsystems/Forms/Content/Forms/Form-Fields/File-Upload.htm). This can be accessed by unauthenticated actors to upload files to your web portal and make their content temporarily accessible on the web.


"The vulnerability described here in this advisory is being exploited in a way where an unauthenticated third party can use Laserfiche Forms to temporarily host uploaded files for distribution," states the company in the [security advisory](https://support.laserfiche.com/kb/1014315/laserfiche-forms-portal-file-upload-vulnerability).


"Valid customer form submission data is not impacted and is not accessible to the third party. The security updates address this vulnerability by reducing the time frame where the temporary file download link is active."


It appears some government clients have followed the remediation steps as accessing the aforementioned search results, previously showing spam content, are now throwing errors via the Laserfiche Forms instance:



![vendor throws error](https://www.bleepstatic.com/images/news/u/1164866/2021/Sep-2021/gov-vuln/vendor-error.jpeg)**Govt sites running Laserfiche Forms now throw errors when spam links accessed**(BleepingComputer)
However, Edwards isn't quite satisfied as Laserfiche [hasn't fixed](http://twitter.com/thezedwards/status/1438563722285309956) the vulnerability for all versions of its product that are still in widespread use, among [other reasons](https://twitter.com/thezedwards/status/1438699019442683909).


"Note that not all versions of the update are available immediately," says Laserfiche.


"We feel that it is important to notify our solution providers and customers of the vulnerability and the updates that are available now. Security updates for select prior versions of Laserfiche Forms are expected soon."


Laserfiche has released a [cleanup tool](https://support.laserfiche.com/kb/1014322/laserfiche-forms-public-portal-file-cleanup-tool) that clients can use to purge unauthorized uploads made to their web portals.




#### Tags:
[[Laserfiche]] [[U.S.]] [[.gov]] [[.mil]] [[Bleeping Computer]]
