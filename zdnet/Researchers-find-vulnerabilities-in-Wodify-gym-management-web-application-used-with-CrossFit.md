# Researchers find vulnerabilities in Wodify gym management web application used with CrossFit
### The tool, used widely among CrossFit boxes, is vulnerable to attacks that would let hackers see and change workout data as well as financial information.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/researchers-find-vulnerabilities-in-wodify-gym-management-web-application/)
+ Date: August 13, 2021 -- 19:44 GMT (20:44 BST)
+ Author: Jonathan Greig


## Article:
Unknown

A cybersecurity researcher has [discovered several new vulnerabilities](https://labs.bishopfox.com/advisories/wodify) within Wodify's gym management web application that gives an attacker the ability to extract workout data, personal information and even financial information. 

Wodify's gym management web application is used widely among CrossFit boxes in the US and other countries to help them grow. The software is in use at more than 5,000 gyms for things like class scheduling and billing. 

But Dardan Prebreza, senior security consultant for Bishop Fox, explained in a report that a slate of vulnerabilities "allowed reading and modifying the workouts of all users of the Wodify platform." 

Through the attack, access "was not limited to a single gym/box/tenant, so it was possible to enumerate all entries globally and modify them," Prebreza added, noting that an attacker could hijack a user's session, steal a hashed password, or the user's JWT through the Sensitive Information Disclosure vulnerability. 

"Thus, a combination of these three vulnerabilities could have a severe business and reputational risk for Wodify, as it would allow an authenticated user to modify all their production data, but also extract sensitive PII," Prebreza said.  

"Additionally, compromising administrative gym user accounts could allow an attacker to modify the payment settings, and thus, have a direct financial impact, as the attacker could eventually get paid by the gym members instead of the legitimate gym owner(s). An authenticated attacker could read and modify all other users' workouts data, extract PII, and eventually gain access to administrative accounts with the aim of financial gains." 

Prebreza rated the vulnerability risk level high because it could cause severe reputational damage and financial ramifications to Wodify gyms and boxes that could have their payment settings tampered with. 






Wodify did not respond to ZDNet's request for comment about the vulnerabilities. 

Prebreza's report includes a timeline that shows the vulnerabilities were discovered on January 7 before Wodify was contacted on February 12. Wodify acknowledged the vulnerabilities on February 23 but did not respond to further requests for information. 

Wodify CEO Ameet Shah was contacted and he connected the Bishop Fox team with Wodify's head of technology, who held meetings with the company throughout April to address the issues. 

On April 19, Wodify confirmed that the vulnerabilities would be fixed within 90 days but from there, repeatedly pushed back the patch date for the problems. First the company pledged to release a patch in May but they pushed it to June 11 before pushing it again to June 26.

Wodify did not respond to Bishop Fox for another month, admitting that they were pushing the patch back to August 5. 

With more than half a year passed since the vulnerabilities were uncovered, Bishop Fox said they told Wodify they would publicly disclose the vulnerabilities on August 6, eventually releasing the report on August 13. 

Wodify has not confirmed if there is actually a patch yet, and Bishop Fox urged customers to get in touch with the company. 

"The Wodify application was affected by insufficient authorization controls, allowing an authenticated attacker to disclose and modify any other user's workout data on the Wodify platform," Prebreza explained. 

"The data modification example in the report was performed with consent on a collaborator's account, and the proof-of-concept payload was removed following the screenshot. However, the ability to modify data means that an attacker could modify all workout results and insert malicious code to attack other Wodify users, including instance or gym administrators."

The vulnerabilities ranged from insufficient authorization controls to sensitive information disclosure and stored cross-site scripting, which can be leveraged in other attacks, according to the study. 

While attackers would be able to change all of a Wodify users' workout data, profile pictures and names, the attack also allows for the ability to insert malicious code that could go after other Wodify users, including gym administrators.

Prebreza said the Wodify application was vulnerable to four instances of stored cross-site scripting, one of which "allowed an attacker to insert malicious JavaScript payloads into workout results." 

"Any user that viewed the page with the stored payload would execute the JavaScript and perform actions on behalf of the attacker. If an attacker gained administrative access over a specific gym in this manner, they would be able to make changes to payment settings, as well as access and update other users' personal information," Prebreza noted. 

"Alternatively, an attacker could craft a payload to load an external JavaScript file to perform actions on behalf of the user. For example, the payload could change a victim's email and take over the account by issuing a password reset (note: changing the email address did not require providing the current password). An attacker could similarly leverage the Sensitive Information Disclosure vulnerability to retrieve a victim's hashed password or JWT (i.e., session token)."

Erich Kron, security awareness advocate at KnowBe4, said this was an unfortunate case of an organization not taking a vulnerability disclosure seriously. 

"While the initial thought of just wiping someone's workout history may seem insignificant to many, the fact that an attacker can access the account and associated information, possibly including payment methods and personal information, is a real problem," Kron said. 

"Even just the workout information can be sensitive if the wrong person uses it to find patterns, for example the days and times a CEO for an organization typically works out, and uses it for malicious purposes. Organizations that create software should always have a process in place for dealing with reported vulnerabilities such as this, and must take them seriously."





#### Tags:
[[Wodify]] [[Prebreza]] [[data,]] [[JavaScript]] [[ZDNet]]
