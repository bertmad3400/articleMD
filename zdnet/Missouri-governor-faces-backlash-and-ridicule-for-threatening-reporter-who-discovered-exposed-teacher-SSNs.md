# Missouri governor faces backlash and ridicule for threatening reporter who discovered exposed teacher SSNs
### Governor Mike Parson called a St. Louis Post-Dispatch reporter a "hacker" and threatened criminal prosecution because he notified state officials about a database that exposed the sensitive information of 100,000 educators.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/missouri-governor-faces-backlash-and-ridicule-for-threatening-reporter-who-discovered-exposed-teacher-ssns/)
+ Date: October 14, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Missouri governor Mike Parson is facing criticism from technologists and journalists after he issued a [scathing, technologically inaccurate statement threatening to arrest](https://twitter.com/GovParsonMO/status/1448697768311132160) a reporter for discovering that the social security numbers of school teachers, administrators and counselors across Missouri were vulnerable to public exposure due to flaws on a website maintained by the state's Department of Elementary and Secondary Education.

St. Louis Post-Dispatch reporter Josh Renaud [wrote a story on Thursday](https://www.stltoday.com/news/local/education/missouri-teachers-social-security-numbers-at-risk-on-state-agencys-website/article_f3339700-ece0-54a1-9a45-f300321b7c82.html?utm_campaign=snd-autopilot&utm_medium=social&utm_source=undefined_stltoday) indicating that the newspaper discovered issues with a web application that allowed anyone to search through a database of certifications and credentials belonging to more than 100,000 of the state's teachers. Payment data and social security numbers were also vulnerable due to the issue. 

The newspaper contacted the department and the pages were removed. All of this was done before the story was published to give the state time to rectify the vulnerability. The newspaper also held off on publishing the story to allow other state agencies to fix similar vulnerabilities in other web applications. 

State officials said they [were investigating](https://dese.mo.gov/media/pdf/educator-data-incident-commissioner-letter) how long the data was exposed. But later in the day, Parson [held a press conference](https://www.kansascity.com/news/politics-government/article254998002.html) where he bashed Renaud and the newspaper, threatening legal action for their decision to notify the state about the issue. 

He then doubled down on the threats in [a Twitter thread](https://twitter.com/GovParsonMO/status/1448697768311132160) that drew widespread ridicule and outrage from technology experts who questioned whether the governor and his team truly understood what they were discussing.

Parson claimed that "an individual took the records of at least three educators, decoded the HTML source code, and viewed the SSN of those specific educators." 

He said his office notified the Cole County prosecutor and the Highway Patrol's Digital Forensic Unit and ordered them to investigate what happened. 






"Upon receiving this notice, DESE immediately contacted the Missouri Office of Administration ITSD, who programs and maintains the web application, to remove public access to the portal and update the code. This matter is serious," Parson wrote. 

"The state is committing to bring to justice anyone who hacked our system and anyone who aided or encouraged them to do so -- in accordance with what Missouri law allows AND requires. A hacker is someone who gains unauthorized access to information or content. This individual did not have permission to do what they did. They had no authorization to convert and decode the code." 

Parson went on to say that Renaud committed an offense because it is a crime to "access, take and examine personal information without permission."

"This data was not freely available and had to be converted and decoded. The state does not take this matter lightly and we are working to strengthen our security to prevent this incident from happening again," Parson said. 

"The state is owning its part, and we are addressing areas in which we need to do better than we have done before. We will not rest until we clearly understand the intentions of this individual and why they were targeting Missouri teachers."

[Other local news outlets](https://www.kansascity.com/news/politics-government/article254998002.html) noted that Parson has long expressed a deep hatred for the state's major news outlets over their coverage of his handling of the COVID-19 crisis and his [penchant for doling out no-bid contracts](https://www.kansascity.com/news/coronavirus/article245420605.html). 

Even members of Parson's own party criticized him for his statements, with Republican Rep. Tony Lovasco [writing on Twitter](https://twitter.com/tonylovasco/status/1448672694065668105) that it was "clear the Governor's office has a fundamental misunderstanding of both web technology and industry standard procedures for reporting security vulnerabilities. 

"Journalists responsibly sounding an alarm on data privacy is not criminal hacking," Lovasco said. 

The St. Louis Post-Dispatch defended Renaud in a statement and said he did the right thing by reporting his findings to DESE before it could be exploited.

"For DESE to deflect its failures by referring to this as 'hacking' is unfounded," said the newspaper's lawyer,  Joseph Martineau, in a statement provided for Renaud's story. 

![fbro79gwyaysmzh.jpg]()![fbro79gwyaysmzh.jpg](https://www.zdnet.com/a/img/resize/a72e6206f418570ce0be4083deab6d477efadbfb/2021/10/14/930581a0-12f7-487e-b6f3-7de2256b69fd/fbro79gwyaysmzh.jpg?width=470&fit=bounds&auto=webp)
 Governor Parson
 The governor's statements were thoroughly bashed by experts who noted that what Renaud did was as simple as pressing the F12 key on certain devices. 

BreachQuest CTO Jake Williams told ZDNet that organizations should be careful not to shoot the messenger when security vulnerabilities are disclosed. 

"This is certainly not hacking in any sense of the word. It appears that the reporter used a publicly available web application intended to facilitate searching for teacher certifications. When the results were displayed, the reporter simply viewed the source code of the web page and found the social security numbers," Williams said.

"While Governor Parson said the reporter 'decoded the HTML source code' in reality they simply used the feature built into every web browser since the dawn of the Internet. Because HTTP is stateless, many web applications store their status in hidden form fields so they can be passed from the browser back to the server with every request. It seems likely that these hidden form fields included the social security number of the teacher. The question of whether this was a crime might be more black and white if the reporter had enumerated all records before reporting the issue." 

Williams noted that even Parson's mention of only three records taken seems to contradict any malicious intent. 

He added that instead of focusing on this so-called hacking, Parson should be concerned about the security of the state's applications, particularly those that are available for public use. Renaud's story noted that the state has previously faced criticism for its data collection practices. 

"Finding a flaw like this in 2021 should frankly be embarrassing for the state. It wouldn't be the first time that a politician has fired on all cylinders claiming that accessing publicly available information was hacking," Williams said. 

"Threatening a reporter with legal action is almost always a bad idea and usually creates an unintended Streisand Effect."

Vectra technical director Tim Wade said the situation underscored the need to protect security researchers operating in the public good and the backlash they typically face for discovering vulnerabilities. 

The outrage directed toward those who discover data loss and vulnerabilities needs to be redirected to the root causes of why these security failures continue to occur to the detriment of individual safety, Wade added.  

He noted that most courts recognize limits to protections from unlawful search when activities occur clearly in a public context and explained that it's hard to imagine that the low-technical sophistication of the behaviors described, with a tool as common as a web browser, constitutes anything but the digital equivalent of observations made in a public context.

John Bambenek, principal threat hunter at Netenrich, said government leaders should be thanking people who notify their government of problems, not threatening them.

"Throughout human history, emperors have responded to those telling them they were wearing no clothes by lashing out in anger at the audacity of those who'd dare say such a thing," Bambenek said. 

"Life would be better if they, you know, just put on pants. I'm sure every actual criminal hacker on the planet noticed this tirade and you can bet their adjusting their targeting accordingly."





#### Tags:
[[Renaud]] [[said.]] [[DESE]] [[ZDNet]]
