# You can post LinkedIn jobs as almost ANY employer — so can attackers
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/you-can-post-linkedin-jobs-as-almost-any-employer-so-can-attackers/)
+ Date: August 19, 2021
+ Author: Ax Sharma


## Article:
![linkedin](https://www.bleepstatic.com/content/hl-images/2021/08/19/linkedin2.png)


EXCLUSIVE: Anyone can create a job listing on the leading recruitment platform LinkedIn on behalf of just about any employer—no verification needed.


And worse, the employer cannot easily take these down.


Now, that might be nothing new, but the feature and lax verification on career websites pave the ways for attackers to post bogus listings for malicious purposes.


The attackers can, for example, use this social engineering tactic to collect personal information and resumes from professionals who believe they are applying to a legitimate company, without realizing their data may be sold or used for phishing scams.


We are hiring! Oh wait...
-------------------------


This week, Harman Singh, a security expert and managing consultant at [Cyphere](https://thecyphere.com/), shared a "feature" with BleepingComputer that was quite unsettling for him to come across.


"Anyone can post a job under a company's LinkedIn account and it appears exactly the same as a job advertised by a company."


"I have checked it but stopped short of posting a job, but it goes fine till the preview," Singh told BleepingComputer in an email interview.


While some may already be aware of this "feature," for others it might be an appalling finding.



![linkedin test job posting](https://www.bleepstatic.com/images/news/u/1164866/2021/Aug-2021/linkedin-job-posting/job-post-wizard.png)**Creating a bogus LinkedIn job posting on behalf of BleepingComputer from an unaffiliated account**
"For example, if Google's LinkedIn company page is vulnerable, we will be able to post a job on their behalf and add some parameters to redirect applicants to a new website where we can harvest [personal information and credentials] and what not usual tricks of social engineering," Singh further told BleepingComputer.


In tests by BleepingComputer, I used an unaffiliated LinkedIn account and was able to successfully publish a new job posting on behalf of BleepingComputer, almost anonymously.


The job listing would appear authentic as if coming straight from BleepingComputer. It also did not show the user account that created the posting—an option set by the user who posts the job, rather than the employer.


And, within hours of the listing going live, applications started coming in:



![job applications](https://www.bleepstatic.com/images/news/u/1164866/2021/Aug-2021/linkedin-job-posting/bleeping-job-posting.png)**Submitted applications arrive within hours of creating test listing**(BleepingComputer)
In a brief test, BleepingComputer had also leveraged LinkedIn's "Easy Apply" option such that any resumes uploaded by an applicant would come straight to **a test email account**, as opposed to LinkedIn redirecting the applicant to an external website.


We found that using a test email account for collecting applicants' personal information and resumes would leave no indication of any suspicious activity to the applicant or the employer, unlike when redirecting the applicant to a website that may appear "phishy" right away.



![resumes arriving via email](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Resumes arrive via email to test mailbox**
Fraudulent listings and phishing scams
--------------------------------------


Singh believes this feature has been abused in the past and could become a hotbed for phishing campaigns.


Although pen-testers and red teams can find good use of the feature, for reconnaissance and social engineering, Singh states the same feature can be misused by threat actors to target the public for various kinds of frauds and phishing scams.


Granted, LinkedIn job scams are nothing new, the ones [reported thus far](https://www.titanhq.com/blog/the-fake-job-offer-scam-on-linkedin/) mostly rely on someone creating a fake profile and touting themselves as the "recruiter" of a company.


This attack, on the other hand, enables anyone to create a job listing straightaway on behalf of virtually any organization, without even revealing their identity.


Restricting who can post jobs under your company
------------------------------------------------


As an employer, what steps can you take then to prevent unauthorized parties and threat actors from creating bogus job listings using your brand?


In 2019, although LinkedIn did release a [blog post](http://web.archive.org/web/20210819110205/https://www.linkedin.com/pulse/how-spot-avoid-online-job-scams-biron-clark/) with some tips on spotting and avoiding common job scams, it falls short of addressing the particular issue described here.


BleepingComputer confirmed in our tests that you **cannot take down** a bogus job posting yourself, even as the super-admin of your company's page.


Following the admin link to the job posting via official BleepingComputer's LinkedIn account showed an error to the administrator:



![linkedin page admin has no access](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Company page's admin does not have access to take down or manage job postings created by unauthorised users**
Fortunately, there may be some steps that businesses can take to deter unauthorized job postings.


For example, in a test by BleepingComputer, we could not create jobs on behalf of certain employers, such as Google:



![google posting failed](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Creating a LinkedIn job posting on behalf of Google fails** (BleepingComputer)
By default, there isn't a way for the administrator of a LinkedIn company page to restrict job listings from *anyone*, but emailing LinkedIn's safety team does that job:


"You can manually email to the LinkedIn trust and safety team to get those options enabled that allow you to block unauthorised posts, and only allow authorised team members to post jobs," Singh told BleepingComputer, while sharing the team's email address:


tns-SAFE@linkedin.com
However, as this email address is not shared online by Linked, unless you knew of its existence and the ability to block this "feature," you are vulnerable to this type of attack.


Additionally, Singh suggests informing your recruitment and HR teams to periodically monitor your company's LinkedIn pages and report any bogus postings to LinkedIn as a workaround, albeit a slower one.


BleepingComputer reached out to LinkedIn to learn more:


"We work every day to keep our members safe and keep fraud off our platform," a LinkedIn spokesperson told BleepingComputer.


"When job searching, safety means knowing the recruiter they're chatting with is who they say they are, that the job you’re excited about is real and authentic, and how to spot fraud."


"Posting fake content, misinformation and fraudulent jobs are clear violations of our terms of service. Before jobs are posted, we use automated and manual defences to detect and address fake accounts or suspected fraud."


But, contrary to the claim, their automated systems did not detect tests by BleepingComputer, and the test listings were not removed until after our email to LinkedIn.


"Whenever we find fake posts, we work to remove them quickly and we're constantly investing in new ways to improve detection."


"That includes providing tools for companies to require work email verification before posting to LinkedIn," concluded the company in their statement.


Until there is a more permanent solution, LinkedIn users and employers should [report suspicious job listings](https://www.linkedin.com/help/linkedin/answer/86030) as spam or scam for review by LinkedIn.


*Update 9:42 PM ET: Changed headline to convey one can post jobs for 'almost' any employer, based on our test with certain employers (e.g. Google), that didn't succeed due to the workarounds listed above.*




#### Tags:
[[LinkedIn]] [[BleepingComputer]] [[BleepingComputer,]] [[phishing]] [[example,]] [[BleepingComputer.]] [[employer,]] [[Bleeping Computer]]
