# Phishers impersonate US DOT to target contractors after Senate passed $1 trillion infrastructure bill
### The attackers were trying to harvest Microsoft Office 365 credentials, according to INKY.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/phishers-impersonate-us-department-of-transportation-to-target-contractors-after-senate-passes-1-trillion-infrastructure-bill/)
+ Date: September 15, 2021 -- 17:06 GMT (18:06 BST)
+ Author: Jonathan Greig


## Article:
Unknown

A new phishing campaign has been uncovered targeting companies that may work with the US Department of Transportation. 

The campaign, discovered by security company INKY, found that phishers are impersonating the US Department of Transportation (DOT) in an effort to harvest Microsoft Office 365 credentials, INKY's Roger Kay [wrote in a blog post](https://www.inky.com/blog/attackers-impersonate-u.s.-department-of-transportation-to-harvest-microsoft-credentials). 


Kay noted that the phishing emails peaked around August 16-18, right after the US Senate [passed the $1 trillion infrastructure bill](https://www.cnet.com/tech/senate-passes-1-trillion-bipartisan-infrastructure-package/) on August 10.

Dozens of phishing emails sought to impersonate the DOT, with attackers contacting multiple companies in the engineering, energy architecture industries asking them to submit bids for federal contracts.  

"The basic pitch was, with a trillion dollars of government money flowing through the system, you, dear target, are being invited to bid for some of this bounty," Kay said.

"By creating a new domain, exploiting current events, impersonating a known brand, and launching a credential harvesting operation, the phishers came up with an attack just different enough from known strikes to evade standard detection methods."

Kay explained that attackers sent their phishing emails from "transportationgov[.]net," a newly created domain intended to impersonate the usual government emails that come from .gov addresses. 






Amazon was the new domain's registrar, Kay added, and the site was registered on August 16. 

"In the initial pitch, recipients were told that USDOT was inviting them to submit a bid for a department project by clicking a big blue button that said, 'CLICK HERE TO BID.' Recipients who clicked on the button were led to a site -- transportation.gov.bidprocure.secure.akjackpot[.]com -- with reassuring-sounding subdomains like 'transportation,' 'gov,' and 'secure.' But the base domain -- akjackpot[.]com -- was registered in 2019 and hosts what may or may not be an online casino that appears to cater to Malaysians. Either the site was hijacked, or the site owners are themselves the phishers who used it to impersonate the USDOT," Kay wrote. 

"Once on akjackpot[.]com, the victim was instructed to 'Click on the BID button and sign in with your email provider to connect to the network.' Targets were told to contact 'mike.reynolds@transportationgov[.]us' if there were any questions. However, transportationgov[.]us was another newly created domain registered by the phishers."

The phishers made their website look legitimate by copying the HTML and CSS from the real USDOT website. They even included a real warning on the government site about making sure users check that sites are legitimate US government websites. 

From there, victims were urged to click a red button asking them to bid, bringing up a Microsoft logo above a form meant to harvest Office 365 credentials. 

If a victim made it that far and actually entered their credentials, they were given a CAPTCHA challenge which then took them to a fake error message. From there, they were redirected to the real USDOT website, according to Kay.

"This last move, dumping victims on a real site is an elegant but perhaps unnecessary flourish that phishers often execute as the final step of their sequence. In the con business, this moment is called the 'blow-off' and refers to the time after which the perpetrator has obtained what they were after, but before the mark realizes that they've been duped," Kay said. 

"In the physical world of swindling, the blow-off gives the perpetrator time to getaway. This remnant of older con games sometimes turns up as an artefact in the digital world, where the perpetrators were never 'there' in the first place."





#### Tags:
[[phishers]] [[phishing]] [[emails]] [[USDOT]] [[ZDNet]]
