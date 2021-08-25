# Critical F5 BIG-IP bug impacts customers in sensitive sectors
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/critical-f5-big-ip-bug-impacts-customers-in-sensitive-sectors/)
+ Date: August 25, 2021
+ Author: Ionut Ilascu


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/03/10/F5.jpg)


BIG-IP application services company F5 has fixed more than a dozen high-severity vulnerabilities in its networking device, one of them being elevated to critical severity under specific conditions.


The issues are part of this month’s delivery of security updates, which addresses almost 30 vulnerabilities for multiple F5 devices.


### Critical bug for sensitive sectors


Of the thirteen high-severity flaws that F5 fixed, one becomes critical in a configuration “designed to meet the needs of customers in especially sensitive sectors” and could lead to complete system compromise.


The issue is now tracked as CVE-2021-23031 and affects BIG-IP modules Advanced WAF (Web Application Firewall) and the Application Security Manager (ASM), specifically the Traffic Management User Interface (TMUI).


Normally, it is a privilege escalation with an 8.8 severity score that can be exploited by an authenticated attacker with access to the Configuration utility to run arbitrary system commands, which could lead to complete system compromise.


For customers using the [Appliance Mode](https://support.f5.com/csp/article/K12815), which applies some technical restrictions, the same vulnerability comes with a critical rating of 9.9 out of 10.


F5’s [security advisory for CVE-2021-23031](https://support.f5.com/csp/article/K41351250) does not provide many details on why there are two severity ratings, but notes that there is a “limited number of customers” that are impacted by the critical variant of the bug unless they install the updated version or apply mitigations.


For organizations where updating the devices is not possible, F5 says that the only way to defend against possible exploitation is to limit access to the Configuration utility only to completely trusted users.


Except for CVE-2021-23031, the dozen high-severity security bugs that F5 addressed this month come with risk scores between 7.2 and 7.5. Half of them affect all modules, five impact the Advanced WAF and ASM, and one affects the DNS module.





| CVE / Bug ID | Severity | CVSS score | Affected products | Affected versions | Fixes introduced in |
| [CVE-2021-23025](https://support.f5.com/csp/article/K55543151) | High | 7.2 | BIG-IP (all modules) | 15.0.0 - 15.1.0  

14.1.0 - 14.1.3  

13.1.0 - 13.1.3  

12.1.0 - 12.1.6  

11.6.1 - 11.6.5 | 16.0.0  

15.1.0.5  

14.1.3.1  

13.1.3.5 |
| [CVE-2021-23026](https://support.f5.com/csp/article/K53854428) | High | 7.5 | BIG-IP (all modules) | 16.0.0 - 16.0.1  

15.1.0 - 15.1.2  

14.1.0 - 14.1.4  

13.1.0 - 13.1.4  

12.1.0 - 12.1.6  

11.6.1 - 11.6.5 | 16.1.0  

16.0.1.2  

15.1.3  

14.1.4.2  

13.1.4.1 |
| BIG-IQ | 8.0.0 - 8.1.0   

7.0.0 - 7.1.0  

6.0.0 - 6.1.0 | None |
| [CVE-2021-23027](https://support.f5.com/csp/article/K24301698) | High | 7.5 | BIG-IP (all modules) | 16.0.0 - 16.0.1  

15.1.0 - 15.1.2  

14.1.0 - 14.1.4 | 16.1.0  

16.0.1.2  

15.1.3.1  

14.1.4.3 |
| [CVE-2021-23028](https://support.f5.com/csp/article/K00602225) | High | 7.5 | BIG-IP (Advanced WAF, ASM) | 16.0.0 - 16.0.1  

15.1.0 - 15.1.3  

14.1.0 - 14.1.4  

13.1.0 - 13.1.3 | 16.1.0  

16.0.1.2  

15.1.3.1  

14.1.4.2  

13.1.4 |
| [CVE-2021-23029](https://support.f5.com/csp/article/K52420610) | High | 7.5 | BIG-IP (Advanced WAF, ASM) | 16.0.0 - 16.0.1 | 16.1.0  

16.0.1.2 |
| [CVE-2021-23030](https://support.f5.com/csp/article/K42051445) | High | 7.5 | BIG-IP (Advanced WAF, ASM) | 16.0.0 - 16.0.1  

15.1.0 - 15.1.3  

14.1.0 - 14.1.4  

13.1.0 - 13.1.4  

12.1.0 - 12.1.6 | 16.1.0  

16.0.1.2  

15.1.3.1  

14.1.4.3  

13.1.4.1 |
| [CVE-2021-23031](https://support.f5.com/csp/article/K41351250) | High


--


Critical - Appliance mode only

 | 8.8


--


9.9

 | BIG-IP (Advanced WAF, ASM) | 16.0.0 - 16.0.1  

15.1.0 - 15.1.2  

14.1.0 - 14.1.4  

13.1.0 - 13.1.3  

12.1.0 - 12.1.5  

11.6.1 - 11.6.5 | 16.1.0  

16.0.1.2  

15.1.3  

14.1.4.1  

13.1.4  

12.1.6  

11.6.5.3 |
| [CVE-2021-23032](https://support.f5.com/csp/article/K45407662) | High | 7.5 | BIG-IP (DNS) | 16.0.0 - 16.0.1  

15.1.0 - 15.1.3  

14.1.0 - 14.1.4  

13.1.0 - 13.1.4   

12.1.0 - 12.1.6 | 16.1.0   

15.1.3.1  

14.1.4.4 |
| [CVE-2021-23033](https://support.f5.com/csp/article/K05314769) | High | 7.5 | BIG-IP (Advanced WAF, ASM) | 16.0.0 - 16.0.1  

15.1.0 - 15.1.3  

14.1.0 - 14.1.4  

13.1.0 - 13.1.4  

12.1.0 - 12.1.6 | 16.1.0  

15.1.3.1  

14.1.4.3  

13.1.4.1 |
| [CVE-2021-23034](https://support.f5.com/csp/article/K30523121) | High | 7.5 | BIG-IP (all modules) | 16.0.0 - 16.0.1  

15.1.0 - 15.1.3 | 16.1.0   

15.1.3.1 |
| [CVE-2021-23035](https://support.f5.com/csp/article/K70415522) | High | 7.5 | BIG-IP (all modules) | 14.1.0 - 14.1.4 | 14.1.4.4 |
| [CVE-2021-23036](https://support.f5.com/csp/article/K05043394) | High | 7.5 | BIG-IP (Advanced WAF, ASM, DataSafe) | 16.0.0 - 16.0.1 | 16.1.0  

16.0.1.2 |
| [CVE-2021-23037](https://support.f5.com/csp/article/K21435974) | High | 7.5 | BIG-IP (all modules) | 16.0.0 - 16.1.0  

15.1.0 - 15.1.3  

14.1.0 - 14.1.4  

13.1.0 - 13.1.4  

12.1.0 - 12.1.6  

11.6.1 - 11.6.5 | None |


The flaws range from authenticated remote command execution to cross-site scripting (XSS) and request forgery, to insufficient permission and denial-of-service.


The full list of vulnerabilities of security fixes includes less severe bugs (medium and low) and is available in [F5's advisory](https://support.f5.com/csp/article/K50974556).


The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has released a [notification](https://us-cert.cisa.gov/ncas/current-activity/2021/08/25/f5-releases-august-2021-security-advisory) about F5’s security advisory, encouraging users and administrators to review the information from the company and install the software updates or apply the necessary mitigations.




#### Tags:
[[BIG-IP]] [[F5]] [[(all]] [[modules)]] [[(Advanced]] [[WAF,]] [[ASM)]] [[high-severity]] [[CVE-2021-23031]] [[Bleeping Computer]]
