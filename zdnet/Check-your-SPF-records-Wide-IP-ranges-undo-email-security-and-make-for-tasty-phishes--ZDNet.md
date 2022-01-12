# Check your SPF records: Wide IP ranges undo email security and make for tasty phishes | ZDNet
### With parts of the Australian private sector, governments at all levels, and a university falling foul of wide IP ranges in a SPF record, it might be time to check yours.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/check-your-spf-records-wide-ip-ranges-undo-email-security-and-make-for-tasty-phishes/
+ Date: 2022-01-12 03:19:09
+ Author: Chris Duckett


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/41799707304f849480013ab997333c9e2a19e0b4/2020/09/30/6daed060-c32f-4f90-9f2e-9cb28719ecd5/istock-1201020974.jpg?width=770&height=578&fit=crop&auto=webp)

![salla-spf-email-headers.png](https://www.zdnet.com/a/img/resize/758c0cade950f37eae433768801592df71994720/2022/01/12/0f377699-683c-4f59-8a9d-1a2b404042dc/salla-spf-email-headers.png?fit=bounds&auto=webp)
 Image: Can I Phish/Sebastian Salla
 You've done the right thing by your organisation and made sure that [DMARC and SPF](https://www.zdnet.com/article/australian-government-lags-uk-in-deploying-dmarc-email-spoofing-prevention/) (sender policy framework) records are set in an effort to reduce email spoofing, but all that good work could be undone if the SPF is too permissive in the stated IP range. 


Such a situation was pointed out by Can I Phish CEO Sebastian Salla who [scanned 1.8 million Australian domain records](https://caniphish.com/phishing-resources/blog/compromising-australian-supply-chains-at-scale) in search of email security snafus. 

The mistake Salla was looking for was within SPF records, which handles individual IP addresses, but also IP ranges. If an organisation had entered a wide IP range, and had their email infrastructure sitting on a cloud provider, which reuse IP addresses unless an organisation pays extra for a dedicated IP address, there could be scope to take over an address covered by someone else's SPF record. 

Finding 60,000 IPs pointed towards various regions within Amazon Web Services (AWS), Salla was well on his way, and able to start EC2 instances on AWS that were handed an IP address that another organisation said it had control of. This happened 264 times. 

Among those caught out were Australian Parliament House, the University of Sydney, Mirvac, another major property investment group, and a state government organisation. 

"Each of the affected 264 organisations and their downstream customers are significantly more susceptible to business email compromise and phishing-related attacks. Anyone with a credit card can sign-up for an AWS account, cycle through EC2 instances until they get a desirable IP, request AWS to remove any SMTP restrictions and begin sending SPF authenticated emails as though they are any of these organisations," Salla wrote. 

"When we consider the position that some of these organisations are in, we can better understand the impact. Imagine a parliamentary staffer receiving an email that appears to come from a Minister, or a student receiving an email posing as someone from university admissions and so on... The recipients in these cases have no technical mechanism to determine the real from fake." 






Salla told ZDNet that 69 of the organisations he found have yet to fix the issue, despite being given a 30-day remediation window and working with the Australian Cyber Security Centre (ACSC) on disclosure. While small organisations might have used wide IP ranges due to dynamic address allocation, Salla said large organisations have other considerations even though they can afford to reserve address blocks. 

"Due to the way AWS pricing works, if you reserve an IP address and then don't use it, you get penalised and incur an hourly cost (this is due to the nature of there being limited IPs and AWS not wanted customers to reserve IPs excessively)," he said. 

"So I suspect, a business unit that focuses on cost optimisation in each org, is likely releasing unused IPs which mean people such as myself can come in and take them -- ultimately leading to IP takeover attacks if this activity hasn't been communicated between business units. 

"The ultimate fix is to only list IP addresses that are being actively used by mail servers -- in the event that redundancy/disaster recovery are necessary, there are in-built capabilities within AWS that enable this, such as use of load-balancers or NAT gateways that only use a single IP." 

**See also: [Phishing attacks are harder to spot on your smartphone. That's why hackers are using them more](https://www.zdnet.com/article/phishing-attacks-are-harder-to-spot-on-your-smartphone-thats-why-hackers-are-using-them-more/)**

In response to ZDNet, the ACSC pointed to the Australian government Information Security Manual as well as its advice on [email](https://www.cyber.gov.au/acsc/view-all-content/publications/how-combat-fake-emails) [security](https://www.cyber.gov.au/acsc/view-all-content/publications/marketing-and-filtering-email-service-providers). 

"Organisations can reduce the likelihood of their domains being used to support fake emails by implementing Sender Policy Framework and Domain-based Message Authentication, Reporting and Conformance (DMARC) records in their Domain Name System configuration," an ACSC spokesperson said. 

"DMARC is one of a variety of controls that, when used together, is a highly effective countermeasure for preventing phishing attacks where the attacker attempts to fully impersonate the sending email domain. 

"It is ultimately up to each agency to implement the advice of the Australian Cyber Security Centre, based on that agency's assessment of the cyber threats it faces." 

For its part, the Department of Parliamentary Services said it had fixed the issue. 

"The Department of Parliamentary Services resolved the issue of an incorrect SPF configuration for the vendor and this had no impact on the network," it said. 

The University of Sydney, as is typical, said it took security seriously but would not comment on details of its cyber posture. 

"We do continually review and improve our systems to manage such threats, and can confirm the matters raised in the blog are not a current issue," a spokesperson said. 

At the start of last month, Salla found a [number of sites](https://caniphish.com/phishing-resources/blog/compromised-australian-email-infrastructure) created by local web development company Precedence, which includes a Queensland council and federal member as customers, that had used a /16 address range, covering over a million IP addresses, in the SPF record used across its client base. 

The range was such that Salla said almost any EC2 instance started in Sydney's ap-southeast-2 region would get an address covered by the range. 

"The first EC2 instance I spun up had an authorised IP address and I was able to send myself an SPF authenticated email from this particular city council which went straight into my inbox -- passing all SPF and DMARC checks," Salla wrote. 

###  Related Coverage

* [DMARC inching its way onto Australian government domains](/article/dmarc-inching-its-way-onto-australian-government-domains/)
* [ACSC scanning is allowing Commonwealth entities to avoid being hacked](/article/acsc-scanning-is-allowing-commonwealth-entities-to-avoid-being-hacked/)
* [ASD leaves TikTok ban decisions in departmental hands](/article/asd-leaves-tiktok-ban-decisions-in-departmental-hands/)
* [ACSC offers optional DNS protection to government entities](/article/acsc-offers-optional-dns-protection-to-government-entities/)
* [Rare bright cyber spot: ACSC reports total incidents down 28%](/article/rare-bright-cyber-spot-acsc-reports-total-incidents-down-28/)





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=RTM]]

#### Industry:
[[victim.industry.name=Education]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Ip]] [[Salla]] [[Spf]] [[Aws]] [[Organisations]] [[Dmarc]] [[Ec2]] [[Acsc]] [[ZDNet]]

