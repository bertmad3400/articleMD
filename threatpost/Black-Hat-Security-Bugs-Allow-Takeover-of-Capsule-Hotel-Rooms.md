# Black Hat: Security Bugs Allow Takeover of Capsule Hotel Rooms
### A researcher was able to remotely control the lights, bed and ventilation in “smart” hotel rooms via Nasnos vulnerabilities.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168376)
+ Date: August 4, 2021  5:14 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/04170941/capsule-e1628111400872.jpg)
LAS VEGAS – A series of vulnerabilities in internet of things (IoT) devices often found in connected hotel rooms allowed a researcher to take control of multiple rooms’ amenities – and punish a loud neighbor.


An inadvertent bug hunt began when Kya Supa, security consultant at LEXFO, was traveling overseas on vacation. He spent a few nights in a so-called “capsule hotel,” which refers to accommodations that consist of tiny rooms stacked side-by-side. In an effort to make up for space constraints, these kinds of digs tend to offer a few electronic bells and whistles, and according to Supa, this particular hotel was no different.


In a Wednesday session at Black Hat 2021, “Hacking a Capsule Hotel – Ghost in the Bedrooms,” Supa explained that an iPod touch given at check-in allows customers to control their lights, change the position of their adjustable beds and control the ventilation fans.



All well and good. Supa wouldn’t have looked under the hood of the technology allowing the room control except for the fact that a noisy neighbor prompted him to see if he could bypass any security protections to take control of other bedrooms in the hotel. It turns out that he was able to do just that using six different exploits that were chained together.


“I met my friend ‘Bob,'” the researcher explained. “This neighbor woke me up two times during last day. He woke me up because he was making phone calls at 2 a.m. in the morning, and he was speaking really loudly. So, the second night I went to see him and I asked him politely to speak more quietly. He told me ‘Yeah, sure, no problem.’ But there was no change.”


Supa went on to further travels but came back to the same hotel a few days later – and “Bob” was still there, exhibiting the same behavior. So, the researcher decided to do a little pen testing.


**Taking Stock of the Capsule Hotel Room**
------------------------------------------


“The iPod touch comes with an application that helps to control your bedroom, and it’s connected to devices using Bluetooth or Wi-Fi,” Supa explained. “So there must be a way to communicate with whatever is controlling the bedroom.”


An exploration of the bedroom revealed the presence of a Nasnos CS8020 remote, which can be used to control up to five Nasnos devices – the same ones that the iPod touch connects to. It’s used in case the iPod touch is lost or if the application doesn’t work.


He also deduced the presence of a Nasnos CS8700 router within each room’s wall, which enables the control of the Nasnos devices over Wi-Fi, either from the iPhone touch or the remote (and potentially from Android smartphones or other iOS devices).


Armed with the knowledge of what the room’s IoT architecture looked like, he moved into the exploitation phase.


**Exploiting Nasnos Router Vulnerabilities**
--------------------------------------------


The iPod touch in this case has a single application that a hotel visitor is allowed to access, with simple buttons linking to the various “smart room” features.


“When I first tried to exit the application, I saw that it wasn’t possible,” Supa said. “I cannot exit the application or turn off the iPod touch, but when I triple-tapped on the bottom, I notice that a passcode was asked for. By searching on the internet I found that this behavior was due to an iOS feature called Guided Access.”


Guided Access limits a device to specific applications and allows users to control which features are available – a form of parental controls. It can be overridden with a passcode, but Supa found that the protection is only configured at run time.


“This means the protection is no longer present if we reboot the device,” he explained. “Yes, we cannot turn off the iPod…but we can still drain its battery, connect it to power afterwards and reboot the device. Once you do that, the protection is no longer present and we can access everything – other applications and the iPod touch settings.”


In examining the iPod touch’s device settings, the researcher found that it was enrolled in a mobile device management (MDM) solution, with two saved Wi-Fi networks. One of these was named Nasnos-CS8700, and it was protected using only WEP – a very old encryption method that’s been [crackable for nearly 20 years](https://en.wikipedia.org/wiki/Wired_Equivalent_Privacy).


In fact, it’s quite easy to retrieve a WEP key, the researcher explained.


“You can return a WEP key by capturing around 80,000 packets [from the access point],” he explained, which he was able to do with a simple JavaScript payload that continuously generates address resolution protocol (ARP) requests. ARP broadcasts a request packet to all the machines on a given network and asks if any of them know they are using that particular IP address. Supa set up a rogue access point (AP) using his Android smartphone, connected the iPod touch to it, cached the payload, connected the iPod touch back to the Nasnos AP and executed the code. Soon he was able to retrieve the key, after which he found that the router was accessible with default credentials.


“The password starts with 123, and I will let you guess what goes after,” Supa said.


He connected his laptop to the vulnerable AP using the credentials in order to set up a man-in-the-middle architecture to inspect traffic flowing from the router. The iPod touch connected to the rogue Android AP, while the Android AP was also connected to a Wi-Fi card in Supa’s laptop. Meanwhile, a second Wi-Fi card in the laptop was connected to the Nasnos AP, and thanks to IP forwarding, the researcher was able to observe that packets were being sent to the Nasnos router on TCP port 8000 with no authentication or encryption necessary.


“After that, I just developed a program that sends the same packets [from the laptop to the router] depending on the action needed,” he said. “This means we are now able to control the bedroom from a laptop. But can we control all bedrooms?”


In other words, could he mess with “Bob?”


**Controlling All Capsule Bedrooms**
------------------------------------


The first thing Supa needed to do was figure out if the Wi-Fi key is generated dynamically or set manually.


To find out, he reverse-engineered an application from Nasnos that’s available on Google Play store. It allows users to set up the Wi-Fi configuration of a Nasnos router. In examining the app, Supa came across another vulnerability: Packets are sent to the router on UDP port 988 as part of the remote configuration service, but it doesn’t require authentication for configuring (or reconfiguring) the router.


This didn’t reveal whether the keys are static or dynamic, however. But when coming back to the capsule hotel the second time, Supa was assigned a different room.


“I noticed a similarity with the Wi-Fi key of my old bedroom – only the four last characters seemed to change,” he said. “If this is the case across all 119 bedrooms, this will mean there are only 65,536 possibilities, which is nothing…we can launch a dictionary attack with a file containing all the possible keys.”


Armed with a list of keys, the next step was matching the correct key to the right SSID for “Bob.”


“I used my laptop to turn on the light of each SSID’s room, and when I noticed a change in his room, I knew that it was the access point I was looking for,” Supa explained. “I went and tried to imagine the best scenario I could for ‘Bob.’ A good one would be to create a script that every two words would transform the bed into a sofa and back again, turn on and off the lights and so on. Convince him there are ghosts.”


**Unpatched Vulnerabilities?**
------------------------------


In all, Supa found six different bugs:


Supa said that he contacted both Nasnos and the hotel about the weaknesses.


“The hotel was really cool and took this issue seriously,” he said. “It’s now using a new architecture so it’s not possible to exploit vulnerabilities in that hotel anymore.”


However, Nasnos did not respond to his report, he said, so if non-random keys are used in all of its routers, many other environments are susceptible to similar exploits.


Nasnos did not immediately respond to a request for comment.


**Worried about where the next attack is coming from? We’ve got your back.****[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****for our upcoming live webinar,****[How to Think Like a Threat Actor](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****, in partnership with Uptycs. Find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on Aug. 17 at 11AM EST for this****[LIVE](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)****discussion.**




#### Tags:
[[Nasnos]] [[iPod]] [[Wi-Fi]] [[“I]] [[explained.]] [[said.]] [[Android]] [[“This]] [[“The]] [[it’s]] [[ThreatPost]]
