# Threat Group Takes Aim Again at Cloud Platform Provider Zoho
### Attackers that previously targeted the cloud platform provider have shifted their focus to additional products in the company’s portfolio.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176732
+ Date: 2021-12-03 13:17:47+00:00
+ Author: Elizabeth Montalbano


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/01/05170820/cloud_web_app.jpg)

State-backed adversaries expanded attacks against cloud platform company [Zoho and its ManageEngine](https://threatpost.com/zoho-password-manager-flaw-godzilla-webshell/176063/) ServiceDesk Plus software, a help desk and asset management  solution. A recent campaign marks an uptick in attacks against the firm’s platform, which have also included past targeting of Zoho’s ADSelfService Plus.


This most recent campaign, reported by [Palo Alto Networks Unit 42 this week](https://unit42.paloaltonetworks.com/tiltedtemple-manageengine-servicedesk-plus/), dovetails warnings in September by the FBI, CISA and the U.S. Coast Guard Cyber Command (CGCYBER) of similar attacks. That targeting included an unspecified APT exploiting a then zero-day vulnerability in Zoho’s password management solution called ADSelfService Plus.


According to researchers, the APT shifted its focus to organizations running Zoho’s ManageEngine ServiceDesk Plus. The recent attacks expand the number of recent Zoho victims impacted by the APT from nine to 13.  

[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


In the Unit 42 report, authored by Robert Falcone and Peter Renals, researchers said the most recent activity was tracked between late October and November. During that time, attackers began reconnaissance efforts against a U.S. financial organization running a vulnerable version of ManageEngine ServiceDesk Plus, they wrote.


“In the days that followed, we observed similar activity across six other organizations, with exploitation against one U.S. defense organization and one tech organization beginning as early as Nov. 3,” researchers said.


Unit 42 is now tracking the two active attack fronts against Zoho’s ManageEngine as the “TitledTemple” campaign and have evidence to believe that the attackers are from China, though “attribution is still ongoing,” the researchers said.


Back in November, Unit 42 said it observed correlations between the tactics and tooling used in ADSelfService Plus campaigns and Threat Group 3390, also known as TG-3390 and Emissary Panda or APT27.


Findings by Microsoft Threat Intelligence Center’s (MSTIC) tied the September Zoho attacks targeting its ManageEngine ADSelfService Plus also suspect threat actor DEV-0322 is behind the campaign. The advanced persistent threat group operates out of China, according Microsoft threat researchers.


**Unpatched ServiceDesk Plus Installs Under Attack**
----------------------------------------------------


On Nov. 22, Zoho released a [security advisory](https://pitstop.manageengine.com/portal/en/community/topic/security-advisory-for-cve-2021-44077-unauthenticated-rce-vulnerability-in-servicedesk-plus-versions-up-to-11305-22-11-2021) alerting customers of active exploitation against newly registered [CVE-2021-44077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44077) found in Manage Engine ServiceDesk Plus, a help desk and asset management software.


The vulnerability, which allows for unauthenticated remote code execution, impacts ServiceDesk Plus versions 11305 and below. Unit 42 researchers believe that attackers have been exploiting this bug in unpatched versions, though they have not found any publicly available proof of concept code for an exploit.


Researchers also have observed the APT uploading a new dropper to the victim systems that, similar to the ADSelfService attacks, deploys a Godzilla webshell, they said. This “provides the actor with further access to and persistence in compromised systems,” researchers said.


However, though attackers used the same webshell secret key – 5670ebd1f8f3f716 – in both TiltedTemple attacks, the Godzilla webshell used in the ServiceDesk Plus attack observed by researchers was not a single Java Server Pages (JSP) file, which was seen before.


Instead, the webshell was installed as an Apache Tomcat Java Servlet Filter, which allow for the filtering of inbound requests or outbound responses. “In this particular case, this allows the actor to filter inbound requests to determine which requests are meant for the webshell,” researchers explained.


“It appears that the threat actor leveraged publicly available [code](https://github.com/Scorpio-m7/tomcat-backdoor) called tomcat-backdoor to build the filter and then added a modified Godzilla webshell to it,” researchers wrote, adding that the use of a publicly available tool with documentation written in Chinese fits in with the profile of the actor that researchers already had observed.


This change also signifies a couple of things for the tactic used in the attacks, they said. The fact that the Godzilla webshell is installed as a filter means that there is no specific URL that the actor will send their requests to when interacting with the webshell, researchers explained. Additionally, the Godzilla webshell filter also can bypass a security filter that is present in ServiceDesk Plus to stop access to webshell files, they said.


**Over Half of Internet-Connected Installs Vulnerable**
-------------------------------------------------------


Researchers used Xpanse capabilities to discover the scope of the problem, finding that there are currently more than 4,700 internet-facing instances of ServiceDesk Plus globally, with 2,900, or 62 percent, vulnerable to exploitation.


“In light of these recent developments, we would advance our characterization of the threat to that of an APT(s) conducting a persistent campaign, and leveraging a variety of initial access vectors, to compromise a diverse set of targets globally,” researchers wrote.


So far, organizations that have been attacked comprise multiple sectors, including technology, energy, healthcare, education, finance and defense industries. Of four new victims since the originally discovered campaign—which targeted nine organizations–two were compromised through vulnerable ADSelfService Plus servers while two were compromised through ServiceDesk Plus software, they said.


“We anticipate that this number will climb as the actor continues to conduct reconnaissance activities against these industries and others, including infrastructure associated with five U.S. states,” researchers warned.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://bit.ly/3bBMX30)***for the LIVE event!***





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]] [[threatactor.name=Putter Panda]] [[threatactor.name=Threat Group-3390]] [[threatactor.name=Threat Group-3390]] [[threatactor.name=Threat Group-3390]] [[threatactor.name=Threat Group-3390]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Emissary]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=P.A.S. Webshell]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Finance]] [[victim.industry.name=Healthcare]]

#### Location:
[[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Servicedesk]] [[Webshell]] [[Zoho]] [[Adselfservice]] [[Manageengine]] [[Godzilla]] [[U.s]] [[“in]] [[ThreatPost]]
#### CVE's
[[CVE-2021-44077]]

