# ‘Glowworm’ Attack Turns Power Light Flickers into Audio
### Researchers have found an entirely new attack vector for eavesdropping on Zoom and other virtual meetings.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168501)
+ Date: August 9, 2021  5:06 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/09171939/light-e1628543996123.jpg)
Virtual meetings are vulnerable to a new, exotic attack called Glowworm, which measures an audio output device’s LED power light changes and converts them to audio reproductions — allowing cyberattackers to listen to sensitive conversations.


As an increasing amount of business is being conducted over platforms like [Microsoft Teams](https://threatpost.com/microsoft-teams-tabs-bec/166909/), [Zoom](https://threatpost.com/zoom-settlement-85m-security-investment/168445/), [Skype](https://threatpost.com/windows-zero-days-israeli-spyware-dissidents/167865/) and others, the findings present an entirely new attack vector for such [electronic communications](https://threatpost.com/nsa-warns-public-networks-are-hacker-hotbeds/168268/).


A team of researchers at Ben-Gurion University have published a paper on the [Glowworm vector](https://ad447342-c927-414a-bbae-d287bde39ced.filesusr.com/ugd/a53494_8b7d9f301c024d7eabe84ab0bff6a7cb.pdf), which is technically known as a Telecommunications Electronics Material Protected from Emanating Spurious Transmissions ([TEMPEST](https://www.techopedia.com/definition/25316/telecommunications-electronics-material-protected-from-emanating-spurious-transmissions-tempest#:~:text=Technically%2C%20TEMPEST%20is%20a%20coverword,Protected%20from%20Emanating%20Spurious%20Transmissions.)) attack — the U.S. National Security Agency designation for unintentional digital signals which can be picked up and used to compromise data security.


Federal agencies are required to [protect classified information](https://www.gao.gov/products/nsiad-86-132) from TEMPEST attacks.


In this case, the spurious transmission is a nearly imperceptible flicker on a speaker, USB hub, splitters or microcontroller LED power.


“By exploiting imperceptible changes in the intensity of a device’s power indicator LED, which are caused by the changes in the device’s power consumption, Glwowworm is capable of recovering speech,” the team explained in a video accompanying the release of their paper.


“Our experiments show that many products of various manufacturers are vulnerable to the Glowworm attack,” the team explained.


**Glowworm Experiment**
-----------------------


The researchers demonstrated how a Glowworm attack might work by pointing a telescope with an electro-optical sensor from 35 meters away at speakers connected to laptop. The sensor was aimed at the speakers’ power-indicator LED and the laptop screen was not visible.


The team was successfully able to capture a statement played on the speakers and translated by Glowworm.


While most business being conducted over platforms like Skype is far from sensitive enough to attract eavesdroppers armed with telescopes and Glowworm, the finding is a good reminder that manufacturers can’t always be relied upon to consider these types of TEMPEST attacks, despite the government’s best efforts.


“This is a very interesting attack that for the overwhelming number of users has no real risk,” John Bambenek from Netenrich told Threatpost in response to the paper. “That said, for devices and environments where espionage is important, physical security remains key. No visibility from unprotected space should be possible into highly sensitive environments and devices should be designed to be segmented so sensitive information can’t be gleaned because manufacturers were too lazy to put LEDs on a clear line in the box.”


**Worried about where the next attack is coming from? We’ve got your back.**[**REGISTER NOW**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**for our upcoming live webinar,**[**How to Think Like a Threat Actor**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**, in partnership with Uptycs. Find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on Aug. 17 at 11AM EST for this**[**LIVE**](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**discussion.**


 


 




#### Tags:
[[device’s]] [[ThreatPost]]
