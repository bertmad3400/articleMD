# BrewDog exposed data for over 200,000 shareholders and customers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/brewdog-exposed-data-for-over-200-000-shareholders-and-customers/)
+ Date: October 8, 2021
+ Author: Bill Toulas


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/10/08/BrewDog_headpic.jpg?rand=2143086897)


BrewDog, the Scottish brewery and pub chain famous for its crowd-ownership model and the tasty IPAs, has irreversibly exposed the details of 200,000 of its shareholders and customers. 


The exposure lasted for over 18 months and the point of the leak was the firm’s mobile app, which gives the ‘Equity Punks’ community access to information, discounts at bars, and more. 


As detailed in a [PenTestPartners report](https://www.pentestpartners.com/security-blog/free-brewdog-beer-with-a-side-order-of-shareholder-pii/), the problem lies in the app’s API, and more specifically, its token-based authentication system. The security blunder comes from the fact that these tokens were hard-coded into the mobile application instead of being transmitted to it following a successful user authentication event. 


As such, anyone was free to append any customer ID to the end of the API endpoint URL, and access sensitive PII (personally identifiable information) for that customer. 


Details that could be exposed in this simple way include the following: 


* Name
* Date of Birth
* Email address
* Gender
* All previously used delivery addresses
* Telephone number
* Number of shares held
* Shareholder number
* Bar discount amount
* Bar discount ID – used to create the QR code
* Number of referrals
* Type of beer previously purchased



![App user details exposed as a result of abusing the API](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/response.jpg)App user details exposed as a result of abusing the API. - PenTestPartners
While these IDs aren’t sequential, they do follow a system that would provide something better to try out instead of just entering random numbers. 


Apart from the fact that anyone could access the sensitive details of other app users, shareholders and customers of BrewDog, the implications of this finding also hit the company itself. An abuser of the flaw could get endless free beer and discounts by generating QR codes from "loaded" accounts. 


The discovery of the flaw came all the way back in March 2020, when PTP researchers analyzed app version 2.5.5. Even though BrewDog’s team was informed of the details immediately, they failed to secure their token system on multiple subsequent releases that followed. 


Eventually, the issue was patched with version 2.5.13 which came out on September 27, 2021. BrewDog though chose not to disclose anything important in the changelog notice of that release, which reflects their general stance in dealing with the incident. 



![Release notes don't disclose addressing a massive data leak](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/app%20notice.jpg)Release notes don't disclose addressing a massive data leak risk. - PenTestPartners
The researcher reports that BrewDog downplayed the importance of his findings, failed to address the issues timely, and made claims of seeing no evidence of a data breach repeatedly. 


From a practical perspective, even if the company was actively looking for signs of a breach, there wouldn’t be any due to the silent way this flaw could be exploited. 


To our knowledge, BrewDog has not informed its shareholders and customers of the possibility of their data having been breached. We have reached out to them for a comment but we have not heard back yet. 


Due to the nature of the exposed data, the company will also have to inform UK’s data protection officer, as PII falls under GDPR which is [still applicable](https://ico.org.uk/for-organisations/dp-at-the-end-of-the-transition-period/data-protection-and-the-eu-in-detail/the-uk-gdpr/) in the country.




#### Tags:
[[PenTestPartners]] [[BrewDog]] [[Bleeping Computer]]
