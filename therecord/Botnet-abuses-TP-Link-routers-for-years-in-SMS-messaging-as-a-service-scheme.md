# Botnet abuses TP-Link routers for years in SMS messaging-as-a-service scheme
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/botnet-abuses-tp-link-routers-for-years-in-sms-messaging-as-a-service-scheme/)
+ Date: October 7, 2021
+ Author: Catalin Cimpanu


## Article:
![Botnet abuses TP-Link routers for years in SMS messaging-as-a-service scheme](https://therecord.media/wp-content/uploads/2021/10/TP-Link-MR6400.jpg)

Since at least 2016, a threat actor has hijacked TP-Link routers as part of a botnet that abused a built-in SMS capability to run an underground Messaging-as-a-Service operation.


Across the years, these infected routers were used to send out betting tips, verification codes, confirmation for online payments and donations, and for sending cryptic messages—which researchers have yet to crack their meaning.


![SMS-botnet-football](https://www-therecord.recfut.com/wp-content/uploads/2021/10/SMS-botnet-football-1024x460.png)Image: Neumann, Eberhardt
The botnet’s existence was revealed today at the Virus Bulletin 2021 security conference, in a [talk](https://vblocalhost.com/presentations/from-match-fixing-to-data-exfiltration-a-story-of-messaging-as-a-service-maas/) by Acronis security researcher Robert Neumann and Search-Lab’s Gergely Eberhardt.


In a report and interview with *The Record*, Neumann said he first started digging into the botnet in May 2018 after he was asked to investigate a hacked 4G-capable router that yielded a huge phone bill for its owner—most of which came from a large number of outgoing SMS messages sent from the SIM card that was inserted into the device.


What happened next was one of the most challenging and convoluted findings in Neumann’s career, part of an investigation that spanned three years and involved gathering clues and logs from multiple victims in order to piece together the botnet’s attacks and operations.


### Botnet was comprised of TP-Link MR6400 routers


The first step was finding how the hackers got in. Neumann said that clues in how the botnet operated suggested that the threat actor might have exploited a vulnerability [disclosed in 2015](https://packetstormsecurity.com/files/131378/TP-LINK-Local-File-Disclosure.html) that could be used to access files on TP-Link routers, the same as the one that was hacked, without needing to authenticate first.


Neumann said he was able to reproduce an exploit that used the 2015 flaw to access one of the router’s LTE functions that were responsible for “the sending of SMS messages, reading both incoming and outgoing SMS queues, gathering SIM lock information and modifying LAN and time settings.”


The researcher said that this interface was only found on [TP-Link MR6400](https://service-provider.tp-link.com/lte-router/tl-mr6400/), a 4G capable router that was typically installed to provide internet access in locations where wired or fiber optics cables could not be used.


While the vulnerability was removed from later versions of this router model’s firmware, Neumann said that thousands of devices had been available online at the time, many of which have remained unpatched, even to this day.


### The types of SMS messages sent from devices


“Whoever discovered the vulnerability first in 2016 started to exploit it by running football-themed campaigns for over a year,” Neumann said.


The theory is that the threat actor hijacked the routers, organized them into an easy-to-control botnet, and then started offering the ability to send cheap SMS messages to various entities.


![SMS-botnet-samples](https://www-therecord.recfut.com/wp-content/uploads/2021/10/SMS-botnet-samples.png)Image: Neumann, Eberhardt
While Neumann told *The Record*that he wasn’t able to track down any ads for this service, the wide variety of SMS-sending campaigns suggests the existence of a pretty broad customer base willing to pay for this service rather than use the much more expensive SMS gateway servers offered by legitimate telecommunications providers.


Who built the botnet is still a mystery, as Neumann said this mesh of hacked routers provided “complete anonymity” for its creator(s), who only had to commercialize it for a quick buck.


### Botnet is now on the decline


“The exploitation of these devices has not stopped; however, it seems to have reduced greatly over the years compared to its peak in 2018,” the researcher said.


“The lack of interest from cybercriminals, the updating of the device’s firmware to a non-vulnerable version, moving on to a newer vulnerable model with greater market share or the enabling of specific barring [of SMS sending functions] on the SIM cards could be all contributing to the decline,” he added.


This research is also Neumann’s second deep-dive investigation into ancient botnets. Akin to an IoT cybersecurity archeologist, Neumann previously found and wrote about a now-defunct botnet that he named [Cereals](https://www.forcepoint.com/blog/x-labs/botnets-nas-nvr-devices), and which had been exclusively used for eight years to download anime cartoons from file-sharing portals.





#### Tags:
[[Neumann]] [[SMS]] [[botnet]] [[TP-Link]] [[The Record]]
