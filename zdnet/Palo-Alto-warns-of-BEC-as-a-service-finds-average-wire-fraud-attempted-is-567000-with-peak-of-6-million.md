# Palo Alto warns of BEC-as-a-service, finds average wire fraud attempted is $567,000 with peak of $6 million
### Business email compromise continues to be one of the leading ways cybercriminals scam victims out of millions of dollars, according to Palo Alto Networks' researchers.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/palo-alto-warns-of-bec-as-a-service-finds-average-wire-fraud-attempted-is-567000-with-peak-of-6-million/)
+ Date: October 21, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Business email compromise (BEC) continues to cost victims thousands -- and sometimes millions -- of dollars, according to a new report from Palo Alto Networks' threat research group Unit 42.

The security team pored through hundreds of BEC cases, finding the average wire fraud attempted was $567,000 and the highest was $6 million. Among the hundreds of BEC cases Unit 42 tackled since the beginning of last year, researchers found that 89 percent of victims failed to turn on multi-factor authentication or follow best practices for its implementation.

BEC is often cited by the FBI as one of the most lucrative cybercrimes, and the law enforcement agency reported last year that it led to [$1.87 billion in losses](https://www.fbi.gov/news/stories/2019-internet-crime-report-released-021120). Victims, according to Palo Alto researchers, typically want to avoid reputational harm and often don't go public, which has made BEC a relatively silent threat.

Unit 42 said its security consultants spend thousands of hours on BEC investigations, "combing through logs to identify unauthorized activity, determine how unauthorized access occurred and find security gaps that need to be addressed."

"Attackers targeted hundreds of employees at an insurance company with phishing emails. These emails led to an attempt to get login credentials through spoofed Microsoft 365 email login pages that looked identical to legitimate ones set up by that firm. The attackers succeeded in gaining access to a few of those accounts, which belonged to employees who hadn't set up MFA, which led in turn to gaining access to sensitive data on an internal Sharepoint site," wrote Unit 42 researchers Jenna Garbett and Sama Manchanda. 

"Attackers gained access to the email accounts of two employees at one client organization that failed to disable legacy authentication for synchronizing email boxes via IMAP4 and POP3. That gave the threat actors access to everything in both mailboxes for over a month, enabling them to collect personally identifiable information (PII) from the victims' contacts. This is one of the most common ways of bypassing MFA, especially in hybrid environments that have legitimate use for legacy protocols."

The researchers provided other examples, including one involving threat actors who "compromised multiple users at a job placement agency, then used those accounts to circulate job postings that asked recipients to provide personal data." 






They set up rules that moved all responses to hidden folders and forwarded them to an external account, the two researchers added. They noted in the blog that most of the top email platforms – including Microsoft's 365 and Exchange, as well as Google Workspace – offer multiple options for implementing MFA, making it difficult to understand why so many BEC victims fail to enable it. 

But sometimes even MFA isn't enough. 

Unit 42 shared the story of one executive with a US financial services firm that relies on a widely used MFA mobile app for protection of his email, customer files and other sensitive data. 

"His iPhone kept pinging him with MFA requests to access his email, interrupting him on a day packed with customer meetings. He was annoyed by the intrusion, figuring it was some kind of system error, and rejected each request so he could focus on work. He thought it was over when the requests stopped," Garbett and Manchanda wrote. 

"Months later, however, he learned he had mistakenly authorized one of those many requests, unknowingly granting an attacker unfettered access to his email. He learned about the compromise when his bank flagged suspicious wire transfers totalling nearly $1 million and our investigation uncovered the exposure of data belonging to the company, its employees and clients." 

The blog post notes that the company was able to recover the stolen funds, but that in many cases incidents like this are costly from a reputational standpoint and from the time and resources needed to rectify the situation. 

Deputy director of threat intelligence for Unit 42 Jen Miller-Osborn told ZDNet that they initially decided to look into ransomware to see how much that has grown and that effort led them to look deeper into their BEC work because the amount of money lost is "orders of magnitude higher than ransomware."

"It's something that is little understood and tends to not get as much press. Everyone talks about ransomware now, there's a lot more awareness around it. But BEC is still flying under the radar even though it is the type of attack that costs businesses the most amount of money, bar none. It's the highest," Miller-Osborn said.

"Similar to ransomware, we're seeing an increasing number of attackers getting into BEC and we're also seeing it mature into -- like Ransomware-as-a-service -- BEC-as-a-service. They're becoming more tech savvy. They've been in the commodity space and are starting to include publicly disclosed vulnerabilities. They're becoming more professional."

BEC scammers are now prolific at mining LinkedIn and other sites for information that can help further their scams. 

She explained that education, more stringent MFA, legacy authentication controls, network protections, account permissions, audit logging and event monitoring are some of the ways organizations and people can protect themselves from BEC. 

"With everyone working remotely, there are people who may not have gotten into BEC before who now, just like ransomware, they decided to shift into to make money. And I think the issues that we see with how difficult it is to effectively stop these ransomware campaigns, also points to how difficult it is for BEC, or even harder, because BEC involves a lot of social engineering components that you don't typically see with other attacks," she said.

"They'll actually get on the phone and call people and try to get them to do things. They have money mules in other countries to help them move the money around. It's a lot more people-based and in many cases, a lot of BEC scams don't involve any malware, so there's nothing that you could have seen. Nothing malicious attached to phishing emails. There was nothing a firewall or endpoint could have detected."





#### Tags:
[[MFA,]] [[MFA]] [[ransomware]] [[ZDNet]]
