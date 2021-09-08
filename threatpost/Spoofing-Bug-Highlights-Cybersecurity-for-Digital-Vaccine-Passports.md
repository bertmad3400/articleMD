# Spoofing Bug Highlights Cybersecurity for Digital Vaccine Passports
### Australian immunization app bug lets attackers fake vaccine status.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169287)
+ Date: September 8, 2021  1:28 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/08131614/vax-passport-e1631121391280.jpg)
Three weeks after an independent researcher found a critical bug in the Services Australia COVID-19 digital vaccine certificate that would allow an attacker to falsify someone’s vaccine status, it still hasn’t been fixed.


Researcher Richard Nelson looked into [the security behind a new digital vaccine passport](https://www.bankinfosecurity.com/researcher-bug-allows-covid-19-vaccination-status-spoofing-a-17468) app from the Australian government’s Express Plus Medicare program, which automatically pulls someone’s vaccine status from the Australian Immunization Register. Bars, restaurants and other businesses rely on vaccination proof like this to protect the public from the spread of COVID-19.


Nelson found the flaw and shared his findings publicly on Aug. 18:



> 
> This should not be anywhere near this easy to fool (I’m not vaccinated.. yet) [pic.twitter.com/faTQws7XhX](https://t.co/faTQws7XhX)
> 
> 
> — Richard Nelson (@wabzqem) [August 18, 2021](https://twitter.com/wabzqem/status/1427899005304938497?ref_src=twsrc%5Etfw)
> 
> 



Nelson tweeted his work because he was unable to get in touch with Services Australia, the organization which oversees the [COVID-19 digital vaccine application](https://medium.com/@wabz?p=8231a5b31ca8), he explained.


“I did report it there in the hopes that someone might forward it on, but did not get a response until days later,” Nelson wrote. “I also eventually reported it via ReportCyber and ASD [Australian Signals Directorate] did forward it on to Services Australia, and [I] never heard back.”


**After No Response, Nelson Went Public**
-----------------------------------------


So, Nelson went wide and public with the disclosure.


“Ultimately, I want to report these issues responsibly and use my expertise to help them get fixed (for free) and not have to wonder if the person sitting next to me in a restaurant has forged their vaccine cert or not,” he added.


**Vax Passport Cybersecurity in Focus**
---------------------------------------


As governments turn to [vaccine passports and contact-tracing](https://threatpost.com/covid-contact-tracing-exposed-fake-vax-cards/168821/) solutions to slow the spread of COVID-19, it’s critical that users have confidence in both the accuracy of the vaccine data, as well as basic privacy protections. If the security isn’t there, no one will use them.


A new NordVPN Vaccines Passport Privacy Study found that currently, 66 percent of those polled would get a vaccine passport if it were required for travel. But another poll from January found that 75 percent of respondents have fears about vaccine databases getting breached.


“The coronavirus pandemic has created the ideal environment for bad actors to prey on people’s fears and vulnerabilities during this period of uncertainty,” Daniel Markuson, digital privacy expert at NordVPN, told Threatpost. “With vaccine data in their hands, vaccine fraudsters [will take hold of every channel](https://threatpost.com/covid-contact-tracing-exposed-fake-vax-cards/168821/) available, including vaccine passports, vaccination cards, human chips and vaccine health records to try to capitalize on it.”


Researchers from Avanan have already documented attackers [spoofing vaccine-pass emails](https://www.avanan.com/blog/new-attack-spoofs-vaccine-passes-to-steal-credentials) from England’s National Health Service (NHS) for travel and events.


Absent a more responsive mechanism for reporting security flaws, particularly for government-run applications and technology, users can take important precautions as the demand for vaccine passports rises around the globe.


**Government App Security**
---------------------------


Unlike in other places around the globe, digital identity cards are making inroads in the U.S. in only a limited way so far. Just last week, Apple announced that eight states are planning to roll out [digital IDs and drivers’ licenses](https://threatpost.com/digital-state-ids-rollouts-privacy/169136/) for iPhone, despite security concerns from the security community and civil rights groups. And New York State [is introducing](https://covid19vaccine.health.ny.gov/excelsior-pass-and-excelsior-pass-plus) the Excelsior Pass for mobile vaccine-status proof.


For those using paper cards, Sailpoint security chief Ryan Case warns that users should avoid taking and storing photos of their vaccine cards, which could be exposed if storage systems like iCloud of Google Drive were compromised. On the digital passport front, Case also recommends having remote wipe functionality accessible in case a device is lost; having strong device encryption and passwords; and regularly updating apps for the latest security.


The heated politics that surround vaccine passports in the U.S. has put the country at a particular disadvantage in developing secure systems, Case added.


“The U.S. does not have a universal acceptance of verification applications with variations leveraged by states, airlines, health tracking wallets, even shopping apps,” Case told Threatpost. “Because of this assortment of diversity in digital cards, including vaccination ones, security and risk-management operations will likely not be as well-equipped as places like the E.U., which released a universal vaccination card in July. Universal adoption and consolidation of the technology reduce the complexity of applying appropriate security controls and managing risk. The U.S. has a long way to go.”


Jon Gaines with nVisium chalks the threat up to one of simple input validation.


“Unfortunately, this is just another example of a vulnerability that is as old as the internet itself, which is a lack of user input validation,” Gained told Threatpost. “In this specific case, it’s a tightrope to walk because to properly validate this input, it would need to be sent to a Services Australia server — and somehow confirm that the individual has actually been vaccinated.”


Gaines supposes that the rush to release the application was to blame and recommends an overhaul of the code.


“At this point, it would probably require a large revamp of the application to resolve this vulnerability,” he added.


**It’s time to evolve threat hunting into a pursuit of adversaries.**[**JOIN**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**Threatpost and Cybersixgill for**[**Threat Hunting to Catch Adversaries, Not Just Stop Attacks**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**and get a guided tour of the dark web and learn how to track threat actors before their next attack.**[**REGISTER NOW**](https://threatpost.com/webinars/threat-hunting-catch-adversaries/?utm_source=ART&utm_medium=ART&utm_campaign=September_Cybersixgill_Webinar)**for the LIVE discussion on Sept. 22 at 2 p.m. EST with Cybersixgill’s Sumukh Tendulkar and Edan Cohen, along with independent researcher and vCISO Chris Roberts and Threatpost host Becky Bracken.**




#### Tags:
[[cards,]] [[U.S.]] [[added.]] [[Threatpost.]] [[ThreatPost]]
