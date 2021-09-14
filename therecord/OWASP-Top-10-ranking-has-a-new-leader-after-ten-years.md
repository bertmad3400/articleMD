# OWASP Top 10 ranking has a new leader after ten years
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/owasp-top-10-ranking-has-a-new-leader-after-ten-years/)
+ Date: September 14, 2021
+ Author: Catalin Cimpanu


## Article:
![OWASP Top 10 ranking has a new leader after ten years](https://therecord.media/wp-content/uploads/2021/09/ranking-top.jpg)

The **OWASP Top 10**, a list of the most dangerous web vulnerabilities, has been updated after four years, and, after more than a decade, there is a new vulnerability at the top of the ranking.


Created in the mid-2000s, the list is curated by the Open Web Application Security Project, a nonprofit foundation that’s made up of security experts from around the world.


While it is not an official document, the OWASP Top 10 is often used in cybersecurity circles as a way to evaluate the importance and severity of vulnerabilities in web-based apps.


For example, bug bounty platforms use the OWASP Top 10 list to classify bugs that need to be patched right away or deserve higher monetary rewards.


Because the web programming landscape and its applications are constantly evolving as new programming languages and techniques are incorporated, OWASP experts usually get together once every three-four years to update the Top 10 ranking, moving entries in or out and up and down the list to reflect the current web app ecosystem.


The ranking was updated the last time in November 2017.


But last week, the OWASP team released for public comment a [draft](https://owasp.org/Top10/) of its upcoming list, one that comes with a complete shake-up and even a new leader.


![OWASP-Top-10-2021](https://www-therecord.recfut.com/wp-content/uploads/2021/09/OWASP-Top-10-2021.png)Image: OWASP
In a press release, the OWASP foundation explained its most recent update and ranking shifts:


**[A01:2021-Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)** moves up from the fifth position; 94% of applications were tested for some form of broken access control. The 34 CWEs mapped to Broken Access Control had more occurrences in applications than any other category.  
  
**[A02:2021-Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)** shifts up one position to #2, previously known as Sensitive Data Exposure, which was broad symptom rather than a root cause. The renewed focus here is on failures related to cryptography which often leads to sensitive data exposure or system compromise.  
  
**[A03:2021-Injection](https://owasp.org/Top10/A03_2021-Injection/)** slides down to the third position. 94% of the applications were tested for some form of injection, and the 33 CWEs mapped into this category have the second most occurrences in applications. Cross-site Scripting is now part of this category in this edition.  
  
[**A04:2021-Insecure Design**](https://owasp.org/Top10/A04_2021-Insecure_Design/) is a new category for 2021, with a focus on risks related to design flaws. If we genuinely want to “move left” as an industry, it calls for more use of threat modeling, secure design patterns and principles, and reference architectures.  
  
**[A05:2021-Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)** moves up from #6 in the previous edition; 90% of applications were tested for some form of misconfiguration. With more shifts into highly configurable software, it’s not surprising to see this category move up. The former category for XML External Entities (XXE) is now part of this category.  
  
**[A06:2021-Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)** was previously titled Using Components with Known Vulnerabilities and is #2 in the industry survey, but also had enough data to make the Top 10 via data analysis. This category moves up from #9 in 2017 and is a known issue that we struggle to test and assess risk. It is the only category not to have any CVEs mapped to the included CWEs, so a default exploit and impact weights of 5.0 are factored into their scores.  
  
[**A07:2021-Identification and Authentication Failures**](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/) was previously Broken Authentication and is sliding down from the second position, and now includes CWEs that are more related to identification failures. This category is still an integral part of the Top 10, but the increased availability of standardized frameworks seems to be helping.  
  
[**A08:2021-Software and Data Integrity Failures**](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/) is a new category for 2021, focusing on making assumptions related to software updates, critical data, and CI/CD pipelines without verifying integrity. One of the highest weighted impacts from CVE/CVSS data mapped to the 10 CWEs in this category. Insecure Deserialization from 2017 is now a part of this larger category.  
  
**[A09:2021-Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)** was previously Insufficient Logging & Monitoring and is added from the industry survey (#3), moving up from #10 previously. This category is expanded to include more types of failures, is challenging to test for, and isn’t well represented in the CVE/CVSS data. However, failures in this category can directly impact visibility, incident alerting, and forensics.  
  
[**A10:2021-Server-Side Request Forgery**](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/) is added from the industry survey (#1). The data shows a relatively low incidence rate with above average testing coverage, along with above-average ratings for Exploit and Impact potential. This category represents the scenario where the industry professionals are telling us this is important, even though it’s not illustrated in the data at this time. 


The 2021 ranking is also the first time since 2007 that the “Injection” vulnerability category has not been at the top of the ranking.


The reason for this is because web apps are getting more and more complex, and oftentimes, they are just a collection of APIs, with their own set of configuration options that, when combined, leave the door open for misconfigurations, unprotected endpoints, or unforeseen interactions.




| 2021 | 2017 | 2013 |
| --- | --- | --- |
| Broken Access Control | Injection | Injection |
| Cryptographic Failures | Broken Authentication | Broken Authentication and Session Management |
| Injection | Sensitive Data Exposure | Cross-Site Scripting (XSS) |
| Insecure Design | XML External Entities (XXE) | Insecure Direct Object References |
| Security Misconfiguration | Broken Access Control | Security Misconfiguration |
| Vulnerable and Outdated Components | Security Misconfiguration | Sensitive Data Exposure |
| Identification and Authentication Failures | Cross-Site Scripting (XSS) | Missing Function Level Access Control |
| Software and Data Integrity Failures | Insecure Deserialization | Cross-Site Request Forgery (CSRF) |
| Security Logging and Monitoring Failures | Using Components with Known Vulnerabilities | Using Components with Known Vulnerabilities |
| Server-Side Request Forgery | Insufficient Logging & Monitoring | Unvalidated Redirects and Forwards |




| 2010 | 2007 | 2004 |
| --- | --- | --- |
| Injection | Cross-Site Scripting (XSS) | Unvalidated Input |
| Cross-Site Scripting (XSS) | Injection Flaws | Broken Access Control |
| Broken Authentication and Session Management | Malicious File Execution | Broken Authentication and Session Management |
| Insecure Direct Object References | Insecure Direct Object Reference | Cross Site Scripting |
| Cross-Site Request Forgery (CSRF) | Cross-Site Request Forgery (CSRF) | Buffer Overflow |
| Security Misconfiguration | Information Leakage and Improper Error Handling | Injection Flaws |
| Insecure Cryptographic Storage | Broken Authentication and Session Management | Improper Error Handling |
| Failure to Restrict URL Access | Insecure Cryptographic Storage | Insecure Storage |
| Insufficient Transport Layer Protection | Insecure Communications | Application Denial of Service |
| Unvalidated Redirects and Forwards | Failure to Restrict URL Access | Insecure Configuration Management |


OWASP is expected to approve the ranking by the end of the year.


While a draft, the ranking is expected to remain the same, barring massive negative feedback, which doesn’t appear to have happened since the new Top 10 list has been revealed last week.








#### Tags:
[[OWASP]] [[CWEs]] [[The Record]]
