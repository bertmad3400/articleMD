# XE Group exposed for eight years of hacking, credit card theft
### A relatively unknown group of Vietnamese hackers calling themselves 'XE Group' has been linked to eight years of for-profit hacking and credit card skimming.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/xe-group-exposed-for-eight-years-of-hacking-credit-card-theft/
+ Date: 2021-12-08T10:12:35-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/02/02/Online-shopping-card.jpg)

![Credit card theft](https://www.bleepstatic.com/content/hl-images/2021/02/02/Online-shopping-card.jpg)


A relatively unknown group of Vietnamese hackers calling themselves 'XE Group' has been linked to eight years of for-profit hacking and credit card skimming.


The threat actors are thought to be responsible for the theft of thousands of credit cards per day, mainly from restaurants, non-profit, art, and travel platforms.


The actors use publicly available exploits to compromise externally-facing services, prominently Telerik UI flaws, to install credential and payment info stealing malware.


A 2020 Malwarebytes report first outlined the group's activities, but a more in-depth analysis of recent compromises attributed to it was published by Volexity yesterday.


More details emerge
-------------------


Volexity was able to map the infrastructure used by the XE Group in the last three years and shared all the technical details and IOCs on GitHub.


The researchers could find many infected sites carrying the same skimmer thanks to a common technique in loading malicious JavaScript snippets.


"The code used to load the malicious JavaScript from this page reveals that the attacker uses an interesting technique: the JavaScript keyword "object" is used to populate the domain value," the researchers shared in the Volexity report.



![Code added on the compromised sites to load the skimmer](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/loading_js.png)**Code added on the compromised sites to load the skimmer**  
*Source: Volexity*
These types of breaches are categorized as "Magecart" attacks, which is when a threat actor hacks an eCommerce site to add malicious JavaScript that collects customer and payment information as it is submitted. This stolen information is then uploaded to a remote server to be collected by the attackers.


The long-term success of these attacks depends on how well they can remain hidden on a website without being detected by security products.


Uploading the sample of this skimmer to VirusTotal returns a perfect 0/57 detection score, meaning this group's JavaScript is very stealthy against AV detection.



![Skimmer's detection score on VirusTotal](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/score.jpg)**Skimmer's detection score on VirusTotal**
Compared to the 2020 version analyzed by [Malwarebytes](https://blog.malwarebytes.com/threat-analysis/2020/07/credit-card-skimmer-targets-asp-net-sites/), the new report found the following differences:


* There is the additional use of “.join()” and .” replace()” to rebuild obfuscated strings.
* The URI used to send stolen data to pseudo-randomized using arrays of words and random integers.
* Functionality to look for passwords has been removed.
* Additional checks are done within the script to ensure the window has finished loading before running the key functionality.
* Exfiltration URL is now encoded.

All in all, the latest skimmer features subtle improvements over last year’s samples and continues to effectively snatch any form of data that victims enter onto pages that load the malicious JavaScript.


An example of the data that is stolen using this from these websites is:



```
{"rcgnAdultsCheckBoxon”:””,”firstNameTextBox”:”[name]”:,”lastNameTextBox”:”[surname]”:,”birthdateTextBox”:”[date]”,”genderCodeDropDown”:”[gender]”,”emailAddressTextBox”:”[email_address]”,”relationshipDropDown”:”[relation]”,”txtCardNumber”:”1111-2222-3333-4444:”,”ddlExpirationMonth”:”[month]”,”ddlExpirationYear:”[year],”txtSecurityCode”:”[code]"}
```

Looking into the XE Group
-------------------------


Volexity attributes the XE Group's activity to Vietnamese threat actors as several of the domain names used for command and control servers are registered to a person in Vietnam.


While domain registration information can be faked, the researchers linked the registrant, Joe Nguyen, to a GitHub repository using the XE avatar created by someone of the same name.



![GitHub account belonging to an XE Group member](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**GitHub account belonging to an XE Group member**  
*Source: Volexity*
Additionally, the nickname "xethanh" associated with the GitHub repository also had an account on the crdclub[.]su forum where they offered stolen credit card information.


The researchers found similar accounts on other carding forums such as cybercarders[.]su and cardingforum[.]co, so the actor prefers selling the card instead of using them.


"The persona used for the GitHub and carding account, and several of the domains, have a history going back to 2013, which suggests the attacker may have been attempting similar attacks for up to eight years, with only one significant public mention of their activity," explained [Volexity](https://www.volexity.com/blog/2021/12/07/xe-group-exposed-8-years-of-hacking-card-skimming-for-profit/)


Finally, some of the malware files discovered in VirusTotal appear to have been uploaded by Vietnamese users. Threat actors commonly use VirusTotal before launching campaigns to test how well antivirus software can detect their malware.


Defenders can block XE Group attacks using the provided [network indicators](https://github.com/volexity/threat-intel/blob/main/2021/2021-12-06%20-%20XEGroup/indicators/indicators.csv) or detect the threat using [these signatures](https://github.com/volexity/threat-intel/blob/main/2021/2021-12-06%20-%20XEGroup/indicators/yara.yar).





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Vietnam]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Volexity]] [[Xe]] [[Javascript]] [[Github]] [[Virustotal]] [[Malware]] [[Bleeping Computer]]

