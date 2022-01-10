# URL Parsing-Library Bugs Allow DoS, RCE, Spoofing & More
### Dangerous security bugs stemming from widespread inconsistencies among 16 popular third-party URL-parsing libraries could affect a wide swath of web applications.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177493
+ Date: 2022-01-10T17:55:00+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2022/01/10123612/library2-e1641836188118.jpg)

Eight different security vulnerabilities arising from inconsistencies among 16 different URL parsing libraries could allow denial-of-service (DoS) conditions, information leaks and remote code execution (RCE) in various web applications, researchers are warning.


The bugs were found in third-party web packages written for various languages, and[, like Log4Shell](https://threatpost.com/apache-log4j-log4shell-mutations/176962/) and other [software-supply chain threats](https://threatpost.com/malicious-pypi-code-packages/176971/), could have been imported to hundreds or thousands of different web apps and projects. Those afflicted are Flask (a micro web framework written in Python), Video.js (an HTML5 video player), Belledonne (free VoIP and IP video phone), Nagios XI (network and server monitoring) and Clearance (password authentication for Ruby).


*[Skip to a rundown of the issues.](#parsing_bugs)*


**Understanding URL Parsing Confusion**
---------------------------------------


URL parsing is the process of breaking down a web address into its underlying components, in order to correctly route traffic across different links or into different servers. URL parsing libraries, which are available for various programming languages, are usually imported into applications in order to fulfill this function.


“URLs are actually built from five different components: scheme, authority, path, query and a fragment,” researchers from the Claroty Team82 research division and Synk wrote in [an analysis](https://security.claroty.com/URLparserconfusion) on Monday. “Each component fulfills a different role, be it dictating the protocol for the request, the host which holds the resource, which exact resource should be fetched and more.”


According to a combined analysis, security holes crop up thanks to differences in the way each library goes about its parsing activities.


Team82 and Synk examined 16 different URL parsing libraries, including: urllib (Python), urllib3 (Python), rfc3986 (Python), httptools (Python), curl lib (cURL), Wget, Chrome (Browser), Uri (.NET), URL (Java), URI (Java), parse\_url (PHP), url (NodeJS), url-parse (NodeJS), net/url (Go), uri (Ruby) and URI (Perl).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Across them, they identified five categories of inconsistencies in how these libraries parse components:


* Scheme Confusion: A confusion involving URLs with missing or malformed Scheme
* Slash Confusion: A confusion involving URLs containing an irregular number of slashes
* Backslash Confusion: A confusion involving URLs containing backslashes (\)
* URL Encoded Data Confusion: A confusion involving URLs containing URL Encoded data
* Scheme Mix-ups: A confusion involving parsing a URL belonging to a certain scheme without a scheme-specific parser


The problem is that these inconsistencies can create vulnerable code blocks, thanks to two main web-app development issues, according to the report:


* **Multiple Parsers in Use:** Whether by design or an oversight, developers sometimes use more than one URL parsing library in projects. Because some libraries may parse the same URL differently, vulnerabilities could be introduced into the code.
* **Specification Incompatibility:** Different parsing libraries are written according to different web standards or URL specifications, which creates inconsistencies by design. This also leads to vulnerabilities because developers may not be familiar with the differences between URL specifications and their implications (e.g., what should be checked or sanitized).


As an example of a real-world attack scenario, slash confusion could lead to server-side request forgery (SSRF) bugs, which could be used to achieve RCE. Researchers explained that different libraries handle URLs with more than the usual number of slashes (https:///www.google.com, for instance) in different ways: Some of them ignore the extra slash, while others interpret the URL as having no host.


In the case of the former (the approach of most modern browsers as well as cURL), accepting malformed URLs with an incorrect number of slashes can lead to SSRF, researchers explained: “[Libraries that do not] ignore extra slashes…will parse this [malformed] URL as a URL with an empty authority (netloc), thus passing the security check comparing the netloc (an empty string in this case) to google.com. However, since cURL ignores the extra slash, it will fetch the URL as if it had only two slashes, thus bypassing the attempted validation and resulting in a SSRF vulnerability.”


URL confusion is also responsible for the [Log4Shell patch bypass](https://threatpost.com/apache-patch-log4shell-log4j-dos-attacks/177064/), according to Claroty, because two different URL parsers were used inside the JNDI lookup process: One parser was used for validating the URL, and another for fetching it.


“Depending on how each parser treats the Fragment portion (#) of the URL, the Authority changes too,” researchers explained. “In order to validate that the URL’s host is allowed, Java’s URI class was used, which parsed the URL, extracted the host, and checked if the host is on the whitelist of allowed hosts. And indeed, if we parse this URL using Java’s URI, we find out that the URL’s host is 127.0.0.1, which is included in the whitelist. However, on certain operating systems (mainly macOS) and specific configurations, when the JNDI lookup process fetches this URL, it does not try to fetch it from 127.0.0.1, instead it makes a request to 127.0.0.1#.evilhost.com. This means that while this malicious payload will bypass the allowedLdapHost localhost validation (which is done by the URI parser), it will still try to fetch a class from a remote location.”


**URL Parsing Security Bugs**
-----------------------------


In their analysis, researchers came across eight high-severity vulnerabilities in third-party web-applications resulting from URL parsing confusion. All of them have been patched, they said, except for those found in unsupported versions of Flask, so developers should refresh their apps with the updated versions:


1. Flask-security open redirect (Python, [CVE-2021-23385](https://snyk.io/vuln/SNYK-PYTHON-FLASKSECURITY-1293234))
2. Flask-security-too open redirect (Python, [CVE-2021-32618](https://snyk.io/vuln/SNYK-PYTHON-FLASKSECURITYTOO-1293190))
3. Flask-User open redirect (Python, [CVE-2021-23401](https://snyk.io/vuln/SNYK-PYTHON-FLASKUSER-1293188))
4. Flask-unchained open redirect (Python, [CVE-2021-23393](https://snyk.io/vuln/SNYK-PYTHON-FLASKUNCHAINED-1293189))
5. Belledonne’s SIP Stack null pointer dereference (DoS) (C, [CVE-2021-33056](https://claroty.com/research/cve-2021-33056/))
6. Video.js cross-site scripting (XSS) (JavaScript, [CVE-2021-23414](https://snyk.io/vuln/SNYK-JS-VIDEOJS-1533429))
7. Nagios XI open redirect (PHP, [CVE-2021-37352](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-37352))
8. Clearance open redirect (Ruby, [CVE-2021-23435](https://snyk.io/vuln/SNYK-RUBY-CLEARANCE-1577284))


Open-redirect vulnerabilities are popular for exploitation because they enable spoofing, phishing and man-in-the-middle attacks (MITM). They occur when a web application accepts a user-controlled input that specifies a URL that the user will be redirected to after a certain action. When a user logs into a website, for example, they could be redirected to a malicious look-alike site.


Researchers explained that typically, open-redirect attacks are thwarted via validation: “The web server validates the given URL and allows only URLs that belong to the same site or to a list of trusted domains.”


URL library confusion can interfere with proper validation, as is the case with the Clearance bug. The vulnerable function inside Clearance (a popular third-party add-on for Ruby’s Rails framework that enables simple and secure email and password authentication) is “return\_to,” researchers noted. This function is meant to be called after a login/logout procedure and should redirect the user safely to the page they requested earlier. However, it can be subverted if a target can be convinced to click on a URL with the following syntax: http://www.victim.com/////evil.com.


“Since Rails ignores multiple slashes in the URL, the path segment will arrive in its entirety to be parsed in Clearance (/////evil.com),” researchers explained. “Since URI.parse trims off two slashes, the resulting URL will be ///evil.com. Whenever the server redirects the user to this URL, ///evil.com, the browser will convert this network path relative reference to the absolute http://evil.com URL pointing to the evil.com domain (host).”


**Belledonne VoIP Crashing**
----------------------------


One of the more interesting bugs was found in Belledonne’s Linphone, a free voice-over-IP softphone, SIP client and service used for audio and video calls. It suffers from scheme confusion thanks to how it handles SIP-message parsing, according to the analysis, which is when a URL-parsing library gets confused by a missing scheme (the “http” or similar portion of a web address).


“By looking into the URL parsing functionality of Belledone, we’ve found [a] piece of code parsing the SIP URL inside the to/from SIP headers,” researchers explained. “Belledone parses the SIP URL as a generic URL and checks if the scheme is either SIP or SIPs using strcasecmp, checking if the given URL is a SIP URL.”


However, a Belledonne generic\_uri accepts URLs created by the different URL components, without requiring specific components to be present, they explained.


“This means a URL containing only a path is a valid URL, while not having a URL scheme,” they concluded. “Using this, we’ve supplied a URL containing only a single slash (/), resulting in the URL’s scheme being NULL. Then, when Belledone uses strcasecmp, it compares a NULL pointer (because no scheme was supplied), resulting in a NULL pointer dereference and the application’s crash.”


The team created a proof-of-concept exploit code that was able to crash any remote user’s application by simply making a malicious VoIP call, “requiring zero interaction from the attacked user.”


Team82 and Synk researchers noted that “many possible vulnerabilities could arise, ranging from an SSRF vulnerability, which could result in remote code execution, all the way to an open-redirect vulnerability which could result in a sophisticated phishing attack.” To protect their apps, developers should adopt the following best practices, they said:


**Use as few parsers as possible.** “We recommend you to avoid using a URL parser at all, and it is easily achievable in many cases,” researchers said.


**Transfer a parsed URL across a microservice environment.** “If microservices are implemented in different frameworks or programming languages, they will likely use different URL parsers,” they noted. “To avoid this problem you can simply parse a URL at the front-end microservice and transfer it further in its parsed form.”


**Understand differences in parsers involved with application business logic**. Sometimes the use of multiple parsers can’t be avoided, so developers need to be aware about differences in parsing behaviors.


**Always canonicalize the URL before parsing.** Always make sure that applications remove multiple forward/backward slashes, white-spaces and control characters to return URLs to their proper forms before parsing.


***Password******Reset: [On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):*** *Fortify 2022 with a password-security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the new password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken.****[Register & stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)****– sponsored by Specops Software.*


 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=FTP]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Url]] [[Urls]] [[Belledonne]] [[(python)]] [[(python]] [[Third-party]] [[Apps]] [[Voip]] [[Team82]] [[Synk]] [[ThreatPost]]
#### ipv4-adresses
127.0.0.1
#### urls
https:///www.google.com, http://www.victim.com/////evil.com. http://evil.com
#### CVE's
[[CVE-2021-23385]] [[CVE-2021-32618]] [[CVE-2021-23401]] [[CVE-2021-23393]] [[CVE-2021-33056]] [[CVE-2021-23414]] [[CVE-2021-37352]] [[CVE-2021-23435]]

