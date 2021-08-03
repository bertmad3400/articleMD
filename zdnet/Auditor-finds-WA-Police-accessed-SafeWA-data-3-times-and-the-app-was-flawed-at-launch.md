# Auditor finds WA Police accessed SafeWA data 3 times and the app was flawed at launch
### WA Health released SafeWA check-in information for purposes other than COVID-19 contact tracing, with six requests being made by the police despite government messaging that the information would only be used to support contact tracing.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/auditor-finds-wa-police-accessed-safewa-data-3-times-and-the-app-was-flawed-at-launch/)
+ Date: August 3, 2021 -- 01:14 GMT (02:14 BST)
+ Author: Asha Barbaschow


## Article:
Unknown

![WA Police](https://www.zdnet.com/a/hub/i/r/2021/06/25/a189f680-09a9-4d72-b95e-1bb603c56ef8/resize/1200xauto/2fe398268834ea9ab8c794d0d6748c17/gettyimages-1215487289.jpg)
 Image: Getty Images
 The Auditor-General of Western Australia has handed down her report into the state's COVID-19 check-in app, SafeWA, revealing that not only did police access its data, but the app had a number of flaws when it was released.

WA Health delivered the [SafeWA app](https://www.zdnet.com/article/western-australia-expands-mandatory-safewa-qr-code-covid-19-register/) in November 2020 to carry out COVID contact tracing.

In its [report](https://audit.wa.gov.au/wp-content/uploads/2021/07/Report_2__SafeWA-Application-Audit.pdf) [PDF], the Office of the Auditor-General (OAG) said it was concerned about the use of personal information collected through SafeWA for purposes other than COVID contact tracing. 

In mid-June, the WA government introduced legislation to keep SafeWA information away from law enforcement authorities after it was revealed the police force [used it to investigate "two serious crimes"](https://www.zdnet.com/article/western-australia-finally-thinks-about-quarantining-covid-check-in-info-from-cops/). The public messaging around the app was that it would be used only for COVID contact tracing purposes.

**See also: [Australia's cops need reminding that chasing criminals isn't society's only need](https://www.zdnet.com/article/australias-cops-need-reminding-that-chasing-crims-isnt-societys-only-need/)**

"In March 2021, in response to our audit questioning around data access and usage, WA Health revealed it had received requests and policing orders under the *Criminal Investigation Act 2006* to produce SafeWA data to the WA Police Force," the report said. 

The WA Police Force ordered access to the data on six occasions and requested access on one occasion. The orders were issued by Justices of the Peace after application by the WA Police Force. 






The WA Police Force was granted orders to access SafeWA data for matters under investigation, including an assault that resulted in a laceration to the lip, a stabbing, a murder investigation, and a potential quarantine breach.

The OAG said WA Health ultimately provided access in response to three of the orders before the passage of the legislation. Applications made to WA Health on December 14, December 24, and March 10 were provided to the cops; applications on February 24, April 1, May 7, and May 27 were not. 

The SafeWA Privacy Policy, which users are required to agree to prior to use, details that WA Health collects, processes, holds, discloses, and uses personal information of people who access and use the SafeWA mobile application. The OAG said it also states that information on individuals may be disclosed to other entities such as law enforcement, courts, tribunals, or other relevant entities.

The information that SafeWA captures includes sensitive personal information such as name, email address, phone number, venue or event visited, time and date, and information about the device used to check-in.  

As of 31 May 2021, over 1.9 million individuals and 98,569 venues were registered in the SafeWA application. The total number of check-in scans between December 2020 and May 2021 exceeded 217 million.  

In addition to police accessing contact tracing data, shortly after the initial release of SafeWA, the app suffered a system outage due to poor management of changes, with the OAG saying this put the availability of SafeWA at risk.

"WA Health has addressed this risk and continues to manage the vendor contract which has required changes as the state's strategy on the use of SafeWA has evolved," the report said.

The app was delivered by GenVis and is hosted in the Amazon Web Services (AWS) cloud. The total contract value was initially AU$3 million, but it has since risen to AU$6.1 million over three years.    

GenVis said it has processes in place to delete check-in data 28 days after collection. Should a member of the public test positive for COVID-19 or qualify as a close contact, WA Health may store a subset of the data relevant to that case indefinitely. The OAG said this is contrary to WA Health's logging and monitoring standard, which requires retention for at least seven years and where possible, for the lifecycle of the system.

Of further concern to the OAG was that WA Health does not monitor SafeWA access logs to identify unauthorised or inappropriate access to SafeWA information.

The OAG also raised issues with WA Health and GenVis' ability to only request, not enforce, that AWS not transfer, store, or process data outside Australia.

WA Health uses provider-managed encryption keys for SafeWA, which are stored in the AWS database, instead of self-managed keys where the cloud provider has no visibility or access to them. 

"WA Health advised us that the current solution is required so that AWS can access keys through software to perform platform maintenance and support the vendor with technical issues," the report said. "Although the likelihood is low, the cloud provider could be required to disclose SafeWA information to overseas authorities as it is subject to those laws."

**See also: [Attorney-General urged to produce facts on US law enforcement access to COVIDSafe](https://www.zdnet.com/article/attorney-general-urged-to-produce-facts-on-us-law-enforcement-access-to-covidsafe/)**

Prior to going live, WA Health identified that SafeWA registration could be completed with an incorrect number or someone else's phone number, the OAG added. 

"This was because SafeWA did not fully verify a user's phone number during the registration process," it said. "Due to the timing of SafeWA development and WA Health's need to balance risk with implementation, this issue was only partially resolved prior to going live. The remaining weaknesses could be exploited to register fake accounts and check-ins."

The issue was resolved in February.

It was not just the cops that may have accessed contact tracing data, however, with the OAG noting it was concerned also about the limited communication around WA Health's use of personal information collected by other government entities, including Transperth SmartRider, Police G2G border crossing pass data, and CCTV footage in its contact tracing efforts. During the audit, the OAG also identified that WA Health's Mothership and Salesforce-based Public Health COVID Unified System (PHOCUS) accesses SafeWA data. 

"When WA Health receives confirmation of a positive COVID-19 case from a pathology clinic, it uses PHOCUS to collate data relevant to the case from several sources," the report says

"WA Health has not provided enough information to the community about other personal information it accesses to assist its contact tracing efforts."

The Mothership contact tracing application, OAG said, has security weaknesses, including a weak password policy and inconsistent use of multi-factor authentication. The OAG is preparing a separate report focused on the Mothership and PHOCUS.

### RELATED COVERAGE

* [Western Australia finally thinks about quarantining COVID check-in info from cops](https://www.zdnet.com/article/western-australia-finally-thinks-about-quarantining-covid-check-in-info-from-cops/)
* [COVIDSafe uploaded 1.65m 'handshakes' and was only used by NSW and Victoria](https://www.zdnet.com/article/covidsafe-uploaded-1-65m-handshakes-and-was-only-used-by-nsw-and-victoria/)
* [328 weaknesses found by WA Auditor-General in 50 local government systems](https://www.zdnet.com/article/328-weaknesses-found-by-wa-auditor-general-in-50-local-government-systems/)
* [Living with COVID-19 creates a privacy dilemma for us all](https://www.zdnet.com/article/living-with-covid-19-creates-a-privacy-dilemma-for-us-all/)





#### Tags:
[[SafeWA]] [[OAG]] [[COVID-19]] [[check-in]] [[data,]] [[Auditor-General]] [[SafeWA,]] [[said.]] [[GenVis]] [[AWS]] [[ZDNet]]
