# ‘I’m Calling About Your Car Warranty’, aka PII Hijinx
### Black Hat: Researchers created 300 fake identities, signed them up on 185 legit sites, then tracked how much the sites used signup PII to pester the accounts.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168375)
+ Date: August 4, 2021  5:34 pm
+ Author: Threatpost


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/04173120/spam-call.jpg)
LAS VEGAS – When you sign up on a new website, where does that information go? Some researchers decided to find out. On Wednesday, they released their preliminary information at a Black Hat USA 2021 session called [Use and Abuse of Personal Information](https://www.blackhat.com/us-21/briefings/schedule/#use--abuse-of-personal-information-22688).


Researchers created 300 fake identities, signing them up on 185 legitimate websites ranging from Target to Fox News, with each identity used on a single website. Then they tracked how many email messages, phone calls, text messages and other responses were received based on the personally identifiable information (PII) used to register.


Those email messages and phone calls add up to a lot of wasted time, researchers said. On average, signing up for a website creates responses resulting in an hour of wasted time due to distractions – and some websites created up to 20 hours of distraction.  




The research was performed by the [Hume Center for National Security and Technology](https://hume.vt.edu/) at Virginia Polytechnic Institute and State University in Blacksburg, VA. Researchers presenting at Black Hat were Alan Michaels, director of electronic systems, and Kiernan George, who at the time was a graduate student.


Surprising and Unsurprising Results
-----------------------------------


Researchers said they were surprised by some of the results. For example, they found most of the companies hoarded the PII rather than selling it to other organizations. Only 10 of the 300 accounts showed indications of shared data, though there was some degree of cookie scraping, particularly with Twitter and TikTok, Michaels said.


Researchers also found that the sites best at detecting fake accounts were Facebook – which detected six out of eight fake accounts right off the bat and detected the other two within a week – and WeChat, which required a legitimate Chinese phone number.


Moreover, interest from non-U.S. companies was primarily associated with Black Friday shopping rather than with politics.


What wasn’t a surprise? The sort of phone calls the fake identities received, from vehicle warranties to Social Security scams to free hotel rooms.


Do You Read Privacy Policies?
-----------------------------


A team of students also read the privacy policies of the sites to which the fake identities signed up. They created a 50-item rubric to track the quality of the privacy policies and how well the sites themselves followed the policies.


Interestingly, there wasn’t much of a correlation between the amount of material sent and the quality of the privacy policies, Michaels said.


What that means is “The lawyers aren’t talking to the computer scientists,” Michaels said.


Next Steps
----------


The university has created an open-source dataset of the research, [available on GitHub](https://github.com/humeESL/Use-and-Abuse-PII), that contains the raw data (16,436 email message, 3,482 phone calls, 949 voicemail messages and 774 text messages), as well as the 300 fake identities, 171 privacy policies with scoring rubrics, and the scripts and tools used for automating analysis.


The Hume Center is now planning a further test with 50,000 to 100,000 fake identities, with automation to give the fake identities the ability to respond to the messages they receive, Michaels said. Because the 300-identity test was only passive – that is, the accounts didn’t respond to any of the email messages, phone calls, or text messages they received – the messages gradually trailed off over time, the researchers said.


In addition, because the research was hosted at a university, that may have affected some of the results. For example, while the researchers received 1,423 email attachments, none were found to be malicious. Researchers later surmised that the university system had stripped off malicious attachments.


Areas of future research include whether any of the fake identities show up on the dark web, the researchers said.


[Editor’s note: Sharon Fisher is a digital nomad who writes about entrepreneurship. You can find more of her work [here](https://authory.com/SharonFisher).]


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.




#### Tags:
[[said.]] [[Michaels]] [[identities,]] [[calls,]] [[ThreatPost]]
