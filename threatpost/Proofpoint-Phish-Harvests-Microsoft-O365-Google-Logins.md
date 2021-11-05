# Proofpoint Phish Harvests Microsoft O365, Google Logins
### A savvy campaign impersonating the cybersecurity company skated past Microsoft email security.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=176038)
+ Date: November 5, 2021  11:12 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/06/03094019/phish-fish-e1591191632979.jpg)
Phishers are impersonating Proofpoint, the cybersecurity firm, in an attempt to make off with victims’ Microsoft Office 365 and Google email credentials.


According to researchers at Armorblox, they spotted one such campaign lobbed at an unnamed global communications company, with nearly a thousand employees targeted just within that one organization.


“The email claimed to contain a secure file sent via Proofpoint as a link,” they explained [in a posting](https://www.armorblox.com/blog/proofpoint-credential-phishing/) on Thursday. “Clicking the link took victims to a splash page that spoofed Proofpoint branding and contained login links for different email providers. The attack included dedicated login page spoofs for Microsoft and Google.”


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The email lure was a file purportedly linked to mortgage payments. The subject line, “Re: Payoff Request,” was geared to fool targets into thinking it was part of ongoing correspondence, which adds an air of legitimacy while also lending urgency to the proceedings.


“Adding ‘Re’ to the email title is a tactic we have observed scammers using before – this signifies an ongoing conversation and might make victims click the email faster,” according to the analysis.


If users clicked on the “secure” email link embedded in the message, they were taken to the splash page with Proofpoint branding and the login spoofs.


“Clicking on the Google and [Office 365 buttons](https://threatpost.com/office-365-phishing-campaign-kasperskys-amazon-ses-token/175915/) led to dedicated spoofed login flows for Google and Microsoft respectively,” researchers explained. “Both flows asked for the victim’s email address and password.”


Because the phish replicated workflows that already exist in many users’ daily lives (i.e., receiving email notifications when files are shared with them via the cloud), attackers were banking on users not questioning the emails too much, researchers noted.


“When we see emails we’ve already seen before, our brains tend to employ [System 1 thinking](https://www.scientificamerican.com/article/kahneman-excerpt-thinking-fast-and-slow/) and take quick action,” according to the analysis.


In terms of infrastructure, the email was sent from a compromised but legitimate email account belonging to a fire department in Southern France. This helped the phish evade detection by Microsoft’s native email security filters, according to Armorblox, which noted that the emails were marked with a spam risk level of “1.” In other words, they weren’t flagged as spam at all.


Also, the phishing pages were hosted on the “greenleafproperties[.]co[.]uk” parent domain.


“The domain’s WhoIs record shows it was last updated in April 2021,” researchers said. “The URL currently redirects to ‘cvgproperties[.]co[.]uk.’ The barebones website with questionable marketing [increases] the possibility that this is a dummy site.”


Attacks like these use social engineering, brand impersonation and the use of legitimate infrastructure to bypass traditional email security filters and users’ eye tests. To protect against such campaigns, Armorblox offered the following advice:


***Cybersecurity for multi-cloud environments is notoriously challenging. OSquery and CloudQuery is a solid answer. Join Uptycs and Threatpost on Tues., Nov. 16 at 2 p.m. ET for “[An Intro to OSquery and CloudQuery](https://bit.ly/3wf2vTP),” a LIVE, interactive conversation with Eric Kaiser, Uptycs’ senior security engineer, about how this open-source tool can help tame security across your organization’s entire campus.***


***[Register NOW](https://bit.ly/3wf2vTP) for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at [becky.bracken@threatpost.com](mailto:becky.bracken@threatpost.com).***




#### Tags:
[[Microsoft]] [[Google]] [[“The]] [[Proofpoint]] [[emails]] [[ThreatPost]]
