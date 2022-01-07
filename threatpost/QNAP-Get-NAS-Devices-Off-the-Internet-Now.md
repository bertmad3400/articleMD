# QNAP: Get NAS Devices Off the Internet Now
### There are active ransomware and brute-force attacks being launched against  internet-exposed, network-attached storage devices, the device maker warned.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=177452
+ Date: 2022-01-07T16:14:21+00:00
+ Author: Lisa Vaas


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2020/12/07104403/QNAP-NAS.jpg)

Get your internet-exposed, network-attached storage (NAS) devices off the internet now, Taiwanese manufacturer QNAP warns: Ransomware and brute-force attacks are widely targeting all network devices.


“The most vulnerable victims will be those devices exposed to the Internet without any protection,” QNAP [said](https://www.qnap.com/en/security-news/2022/take-immediate-actions-to-secure-qnap-nas) on Friday, urging all QNAP NAS users to follow security-setting instructions that the Taiwanese NAS maker included in its alert.


First off, to check whether your NAS is exposed to the internet, QNAP instructed device owners to open the device’s [Security Counselor](https://www.qnap.com/solution/security-counselor/en/): a built-in security portal that integrates anti-virus and anti-malware software.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


**“Your NAS is exposed to the Internet and at high risk if there shows ‘The System Administration service can be directly accessible from an external IP address via the following protocols: HTTP’ on the dashboard.” —QNAP**


QNAP directed customers to [this site](https://www.qnap.com/en/how-to/faq/article/disable-unnecessary-port-forwarding) to figure out which router ports are exposed to the internet.


Fending Off Attacks Against Exposed NAS Devices
-----------------------------------------------


If your NAS device turns out to be exposed to the internet, QNAP recommended taking these two steps to secure it:


1. **Disable the Port Forwarding function of the router.** Go to the management interface of your router, check the Virtual Server, NAT or Port Forwarding settings, and disable the port forwarding setting of NAS management service port (port 8080 and 433 by default).
2. **Disable the UPnP function of the QNAP NAS.** Go to myQNAPcloud on the QTS menu, click the “Auto Router Configuration,” and unselect “Enable UPnP Port forwarding.”


 


QNAP also provides [detailed instructions](https://www.qnap.com/en/security-advisory/nas-201911-01) on how to prevent malware infections, including via password hygiene, enabling IP and account access protection to prevent brute force attacks, disabling SSH and Telnet connections if you don’t use these services, and avoiding the use of default port numbers such as 22, 443, 80, 8080 and 8081.


A Plague of Ransomware Attacks
------------------------------


QNAP didn’t specify which ransomware gangs or strains are involved in the ongoing attacks, but QNAP device owners have suffered through more than their share over the past few years.


That includes repeated targeting by operators wielding eCh0raix ransomware. aka [QNAPCrypt](https://threatpost.com/linux-ransomware-nas-servers/146441/).


In August 2021, Palo Alto Network Unit 42 researchers put out a report about a [new variant of eCh0raix](https://threatpost.com/ech0raix-ransomware-variant-qnap-synology-nas-devices/168516/) that was exploiting a critical bug, [CVE-2021-28799](https://nvd.nist.gov/vuln/detail/CVE-2021-28799) – an improper authorization vulnerability that gives attackers access to hard-coded credentials so as to plant a backdoor account – in the Hybrid Backup Sync (HBS 3) software on QNAP’s NAS devices. Users had started reporting attacks that abused what turned out to be the same flaw in April 2021.


eCh0raix was also used [to target](https://www.anomali.com/blog/the-ech0raix-ransomware) QNAP NAS servers in 2019, in targeted attacks that brute-forced weak credentials and exploited known vulnerabilities. QNAP also came under attack by operators [inflicting Qlocker](https://www.qnap.com/static/landing/2021/qlocker/response/da-dk/) ransomware in April 2021.


**Password** **Reset:** **[On-Demand Event](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/):** Fortify 2022 with a password security strategy built for today’s threats. This [Threatpost Security Roundtable](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/), built for infosec professionals, centers on enterprise credential management, the *new* password basics and mitigating post-credential breaches. Join Darren James, with Specops Software and Roger Grimes, defense evangelist at KnowBe4 and Threatpost host Becky Bracken. **[Register & Stream this FREE session today](https://threatpost.com/webinars/password-reset-claiming-control-of-credentials-to-stop-attacks/)** – sponsored by Specops Software.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=route]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Taiwan]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Qnap]] [[Nas]] [[Ransomware]] [[Ech0raix]] [[ThreatPost]]
#### CVE's
[[CVE-2021-28799]]

