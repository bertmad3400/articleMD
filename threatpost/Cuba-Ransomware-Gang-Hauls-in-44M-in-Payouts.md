# Cuba Ransomware Gang Hauls in $44M in Payouts
### The gang is using a variety of tools and malware to carry out attacks in volume on critical sectors, the FBI warned.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176790
+ Date: 2021-12-06T18:29:59+00:00
+ Author: Tara Seals


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/06130820/cuba2-e1638814156705.jpg)

The “Cuba” ransomware gang has settled into a groove, compromising at least 49 entities in five critical sectors in the U.S. as of November, the FBI has warned.


In a [flash alert](https://www.ic3.gov/Media/News/2021/211203-2.pdf), the Feds attributed a rash of attacks on U.S. entities in the financial, government, healthcare, manufacturing and information technology sectors to the group. Collectively, the hits resulted in the extortion of $44 million in ransom payments. That’s a little more than half of the $74 million that the Cuba gang actually demanded across the attacks, indicating that companies [remain split](https://threatpost.com/ransomware-victims-dont-pay-up/166989/) on whether or not to pay up.


The FBI didn’t name specific victims, but last month the bureau also [warned that the group](https://threatpost.com/native-tribal-casinos-ransomware-losses/176060/) is targeting tribal casinos throughout the U.S.



> **We want to know what your biggest cloud security concerns and challenges are, and how your company is dealing with them. Weigh in with our exclusive, anonymous [Threatpost Poll](https://threatpost.com/cloud-security-challenges-poll/176702/)!**
> 
> 


The FBI noted that the Cuba ransomware is distributed using a first-stage implant that acts as a loader for follow-on payloads: the Hancitor malware, which has been around for [at least five years](https://threatpost.com/hancitor-downloader-shifts-attack-strategy/120040/). Hancitor operators gain initial access to target machines using phishing emails, exploitation of [Microsoft Exchange vulnerabilities](https://threatpost.com/tortilla-exchange-servers-proxyshell/175967/), compromised credentials or legitimate Remote Desktop Protocol (RDP) tools, according to the FBI’s alert.


After Hancitor is in place, Cuba ransomware actors also use legitimate Windows services – such as PowerShell, PsExec and Cobalt Strike, the legitimate pen-testing tool that [cybercrooks have turned to](https://threatpost.com/cobalt-strike-cybercrooks/167368/) *en masse* to aid in lateral movement. The tool uses beacons to effectively identify exploitable vulnerabilities inside a target environment.


“A Cobalt Strike beacon [is installed] as a service on the victim’s network via PowerShell,” according to the FBI’s analysis. “Once installed, the ransomware downloads two executable files, which include ‘pones.exe’ for password acquisition and ‘krots.exe,’ also known as KPOT, enabling the Cuba ransomware actors to write to the compromised system’s temporary (TMP) file.”


Once the TMP file is uploaded, KPOT is deleted and the TMP file is executed in the compromised network – a trick meant to cover the ransomware’s tracks.


“The TMP file includes API calls related to memory injection that, once executed, deletes itself from the system,” the alert read. “Upon deletion of the TMP file, the compromised network begins communicating with a reported malware repository located at Montenegro-based domain, teoresp.com.”


The Cuba crooks also use MimiKatz malware to steal credentials from victims, and then use remote desktop protocol (RDP) to log into the compromised network host with a specific user account, the FBI said.


“Once an RDP connection is complete, the Cuba ransomware actors use the Cobalt Strike server to communicate with the compromised user account,” according to the analysis. “One of the initial PowerShell script functions allocates memory space to run a base64-encoded payload. Once this payload is loaded into memory, it can be used to reach the remote command-and-control (C2) server [kurvalarva[dot]com], and then deploy the next stage of files for the ransomware.”


Target files are encrypted with the “.cuba” extension, giving the ransomware its name.


The analysis comes on the heels of a joint FBI/CISA warning for organizations [to be extra-vigilant](https://us-cert.cisa.gov/ncas/current-activity/2021/11/22/reminder-critical-infrastructure-stay-vigilant-against-threats) during the holiday season, when many offices close for days and IT staff may have taken their eyes off the ball.


“Although neither CISA nor the FBI currently have identified any specific threats, recent 2021 trends show malicious cyberactors launching serious and impactful ransomware attacks during holidays and weekends, including Independence Day and Mother’s Day weekends,” according to the warning.


“Ransomware threats are constantly evolving,” Mieng Lim, vice president of product management at Digital Defense by HelpSystems, said via email. “From the commoditization of ransomware through the recent availability of as-a-service tools, to increasingly sophisticated attack strategies, it is a threat landscape that demands constant monitoring and education from organizations and governments alike.”


Organization can take steps to protect themselves by implementing well-known best practices, such as user awareness training on spotting phishing emails, timely patching, email security solutions, regular penetration testing and vulnerability scanning, network segregation, data encryption, remote backups, and having a robust and tested incident-response playbook, Lim added.


“Unfortunately, we live in an era where preventing 100 percent of cyber-risks is no longer possible, but constant vigilance, ongoing cyber-threat education, and a well-planned threat detection and response strategy will go a long way towards keeping your organization’s most sensitive data safe,” Lim noted.


***There’s a sea of unstructured data on the internet relating to the latest security threats.*** ***[REGISTER TODAY](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)*** ***to learn key concepts of natural language processing (NLP) and how to use it to navigate the data ocean and add context to cybersecurity threats (without being an expert!). This [LIVE, interactive Threatpost Town Hall](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article), sponsored by Rapid 7, will feature security researchers Erick Galinkin of Rapid7 and Izzy Lazerson of IntSights (a Rapid7 company), plus Threatpost journalist and webinar host, Becky Bracken.***


[***Register NOW***](https://threatpost.com/webinars/security-threats-natural-language-processing/?utm_source=In+Article&utm_medium=article&utm_campaign=Decoding+the+Data+Ocean:+Security+Threats+%26+Natural+Language+Processing&utm_id=In+Article)***for the LIVE event!***





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Cobalt Strike]] [[action.malware.name=Cuba]] [[action.malware.name=Hancitor]] [[action.malware.name=Mimikatz]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=PsExec]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=Montenegro]] [[victim.continent.name=Europe]] [[victim.country.name=Cuba]] [[victim.continent.name=North and Central America]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Ransomware]] [[Tmp]] [[U.s]] [[Threatpost]] [[Hancitor]] [[Malware]] [[ThreatPost]]

