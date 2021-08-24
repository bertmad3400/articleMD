# Microsoft Spills 38 Million Sensitive Data Records Via Careless Power App Configs
### Data leaked includes COVID-19 vaccination records, social security numbers and email addresses tied to American Airlines, Ford, Indiana Department of Health and New York City public schools. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168885)
+ Date: August 23, 2021  7:18 pm
+ Author: Tom Spring


## Article:
![leaky data](https://media.threatpost.com/wp-content/uploads/sites/103/2018/12/19164049/breach-2018-year-in-review.jpg)
For months, Microsoft’s Power Apps portals exposed personal data tied to 38 million records ranging from COVID-19 vaccination status, social security numbers and email addresses. Consumers most impacted by what is being called a “platform issue” are those doing business with American Airlines, Ford, the Indiana Department of Health and New York City public schools.


Microsoft describes its Power Apps as a “suite of apps, services, and connectors, as well as a data platform, that provides a rapid development environment to build custom apps for your business needs.” The tool is used by developers to build applications that share data locally or with the cloud.


On Monday, [UpGuard Research revealed](https://www.upguard.com/breaches/power-apps) Microsoft’s Power Apps management portal had inadvertently leaked the data of 47 businesses totaling the exposure of 38 million personal records. It asserted that Microsoft’s Power Apps platform was flawed in the way it forced customers to configure their data as private or public. Microsoft does not consider the leaky data issue a vulnerability, rather a configuration issue that can be improved on its part.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Besides data sets previously mentioned, researchers outlined what they found as:


**American Airlines:** A collection of 398,890 “contact” records, which included full names, job titles, phone numbers, and email addresses. A second “test” Collection of data included 470,400 records, which included full names, job titles, phone numbers, and email addresses.


**Denton County, TX:** A total of 632,171 records spilled included vaccination types, appointment dates and times, employee IDs, full names, email addresses, phone numbers and data of birth. “The list ‘contactVaccinationSet’ had 400,091 records with fields for full names and vaccination types, and ‘contactset’ had 253,844 records with full names and email addresses,” researchers wrote.


**J.B. Hunt Transport Services:** The transportation logistics firm made public 905,228 records that included customer full names, email addresses, physical addresses and phone numbers. Over a quarter million of the records also included US social security numbers.


**Microsoft’s own The Global Payroll Services Portal:** Researchers found 332,000 records of Microsoft employees and contractors with their @microsoft.com email address, full name, phone numbers that appear to be for personal use.


**How Microsoft’s Power Apps Blew It**
--------------------------------------


UpGuard said the data leak is tied to how the Power Apps platform juggles the use of the Open Data Protocol (OData) with its application programming interface (APIs). For example, some data handled within the Power Apps platform needs to be public and other related data sets need to be private.


“In cases like registration pages for COVID-19 vaccinations, there are data types that should be public, like the locations of vaccination sites and available appointment times, and sensitive data that should be private, like the personally identifying information of the people being vaccinated,” UpGuard wrote.


Researchers discovered sensitive private user data, which should have been private, was being segregated, but still publicly accessible. The issue, UpGuard explained, is Microsoft’s configuration options for data sharing and storing sensitive data in Power Apps “create(s) the potential for data leaks.”


Researchers zeroed in on the OData APIs used by Power Apps for retrieving and storing public and private/sensitive data. More specifically, it focused on how data (such as personal identifiable information) is stored and formatted into “Table Permissions” for sharing – or not. The crux of the issue boiled down to configuration settings that instruct a Power Apps user to “set the Enable Table Permissions Boolean value on the list record to true.”


“If those configurations are not set and the OData feed is enabled, anonymous users can access list data freely,” researchers wrote.


**It’s a Feature, Not a Bug, Microsoft**
----------------------------------------


During the course of its researcher, UpGuard discovered the OData misconfiguration by Microsoft customers (and even Microsoft itself) to be widespread and systemic. “Empirical evidence suggests a warning in the technical documentation is not sufficient to avoid the serious consequences of misconfiguring OData list feeds for Power Apps portals,” wrote researchers.


UpGuard notified Microsoft of the data leakage in June 24, 2021. Microsoft promptly began to investigate claims its Power Apps were responsible for spilling millions of sensitive-data records. And on June 29 it asserted that the platform worked as planned.


“The case was closed, and the Microsoft analyst informed us that they had “determined that this behavior is considered to be by design,” Microsoft wrote.


Over the proceeding weeks, UpGuard continued to find massive data exposures tied to the way Power Apps handled OData via its API.


“Microsoft would later take action after we had notified some of the most severe exposures. We spent the next few weeks analyzing the data for indicators of sensitivity and reaching out to affected organizations,” according to the UpGuard report.


**Shoot the Messenger**
-----------------------


For all of UpGuard’s attempts to shed light onto Microsoft’s Power Apps problems, it was persona non grata by not only Microsoft, but also others it notified of data leaks. Reaction to UpGuard’s data discovery of sensitive COVID-19 vaccine records being publicly exposed by the state of Indiana was typical.


Researchers notified Indiana’s deputy chief technology officer on July 2 of its publicly accessible stores of sensitive data. While data was removed by July 7, on August 17 the State of Indiana issued a press release publicly acknowledging the data exposure, it also accused UpGuard of “improperly” accessing the data claiming it was done as a ploy to drum up business from the state.


“UpGuard has never approached Indiana or any other company notified of a breach for business, and there is no merit to [the press] statement. On the contrary, UpGuard has provided hours of unremunerated support in service of Indiana Department of Health and the people it serves,” UpGuard wrote. It also verified to the state, as with other impacted configuration issue, all publicly accessible data discovered by UpGuard has been destroyed.


**Microsoft Takes Action to Help Customers**
--------------------------------------------


Since UpGuard’s disclosure of the issue, Microsoft released a tool for checking Power Apps portals for leaky data. It also plans to change the product so that table permissions will be enforced by default, UpGuard said.


“To diagnose configuration issues, the [Portal Checker](https://docs.microsoft.com/en-us/powerapps/maker/portals/admin/portal-checker-analysis) can be used to detect lists that allow anonymous access. More importantly, newly created Power Apps portals will [have table permissions enabled by default](https://docs.microsoft.com/en-us/powerapps/maker/portals/important-changes-deprecations#table-permission-changes-for-forms-and-lists-on-new-portals). Tables configurations can still be changed to allow for anonymous access, but defaulting to permissions enabled will greatly reduce the risk of future misconfiguration,” UpGuard wrote.


It added, UpGuard agrees with Microsoft’s stance that the issue is not a software vulnerability, rather a platform issue that “requires code changes to the product.”


“It is a better resolution to change the product in response to observed user behaviors than to label systemic loss of data confidentiality an end user misconfiguration, allowing the problem to persist and exposing end users to the cybersecurity risk of a data breach,” UpGuard said. “Ultimately, Microsoft has done the best thing they can, which is to enable table permissions by default and provided tooling to help Power Apps users self-diagnose their portals.”




#### Tags:
[[Apps]] [[UpGuard]] [[Microsoft]] [[Microsoft’s]] [[wrote.]] [[OData]] [[names,]] [[COVID-19]] [[addresses.]] [[issue,]] [[ThreatPost]]
