# SolarWinds Issues Hotfix for Zero-Day Flaw Under Active Attack
### Microsoft alerted the company to a security vulnerability in its Serv-U Managed File Transfer and Secure FTP products that a cyberattacker is using to target a “limited” amount of customers.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167704)
+ Date: July 13, 2021  8:58 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/01/11123618/solarwind-1-e1619800325586.jpg)
SolarWinds has issued a hotfix for a zero-day remote code execution (RCE) vulnerability already under active, yet limited, attack on some of the company’s customers.


Microsoft alerted the company about the flaw, which affects its [Serv-U Managed File Transfer Server](https://www.solarwinds.com/serv-u-managed-file-transfer-server) and [Serv-U Secured FTP](https://www.solarwinds.com/ftp-server-software) products. Specifically, the vulnerability exists in the latest Serv-U version 15.2.3 HF1 released on May 5 of this year, as well as all prior versions, the company said in a [security advisory](https://www.solarwinds.com/trust-center/security-advisories/cve-2021-35211) posted over the weekend.



Microsoft provided a proof-of-concept (PoC) exploit to SolarWinds, demonstrating how a threat actor who successfully exploits the vulnerability could run arbitrary code with privileges, according to the advisory.


“An attacker could then install programs; view, change or delete data; or run programs on the affected system,” the computing giant said.


Though the current threat appears to be from a sole actor and “involves a limited, targeted set of customers,” SolarWinds wanted to remedy the situation before it could escalate, the company said. “Our joint teams have mobilized to address it quickly,” according to the advisory.


SolarWinds does not currently know many customers may be directly affected by the flaw, nor has it identified the ones who were targeted. The company is recommending that all customers using the affected products update now, which can be done by accessing the company’s [customer portal](https://customerportal.solarwinds.com/).


Unrelated to Supply-Chain Attack
--------------------------------


Indeed, SolarWinds likely still has fresh memories of a [global supply-chain attack](https://threatpost.com/solarwinds-attackers-dhs-emails/165110/) targeting the company’s technology that was discovered late last year and stretched well into 2021. That attack occurred when [a state-sponsored APT](https://threatpost.com/solarwinds-hack-linked-turla-apt/162918/) injected malicious code into normal software updates for SolarWinds Orion network-management platform.


Specifically, attackers installed the Sunburst/Solorigate backdoor inside SolarWinds.Orion.Core.BusinessLayer.dll, a SolarWinds digitally signed component of Orion. From there, the threat actors mounted a [massive cyberespionage campaign](https://threatpost.com/solarwinds-default-password-access-sales/162327/) that hit nine U.S. government agencies, Microsoft and other tech companies, as well as about 100 other victims.


SolarWinds stressed in its advisory that the latest vulnerability is not related to that [previous scenario](https://threatpost.com/solarwinds-hack-seismic-shift/165758/) — which [cost the company $3.5 million](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001739942/48bd02f7-3c52-4abc-a5e9-60401f9a4e8b.pdf) in investigation and remediation expenses — in any way.


“All other SolarWinds and N-able (formerly SolarWinds MSP) are not affectedby this vulnerability,” the company wrote. “This includes the Orion Platform, and all Orion Platform modules.”


In fact, the company even included a complete list of products “not known to be affected by this security vulnerability” in the advisory for good measure, perhaps to stave off any potential panic or doubt that news of the latest vulnerability might inspire.


Indeed, one security expert took to Twitter to advise organizations to keep a cool head over the news and take preemptive measures rather than raise an immediate alarm.


“I know there’s a tendency to panic because it’s SolarWinds … but I’d suggest avoiding panic and taking proactive actions for defense and response instead,” [tweeted](https://twitter.com/likethecoins/status/1414681417053835265) Katie Nickels, director of intel at security operations firm Red Canary.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 




#### Tags:
[[SolarWinds]] [[Microsoft]] [[Serv-U]] [[ThreatPost]]
