# Facebook, Instagram, and WhatsApp back online after BGP fix
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/technology/facebook-instagram-and-whatsapp-back-online-after-bgp-fix/)
+ Date: October 4, 2021
+ Author: Lawrence Abrams


## Article:
![Facebook](https://www.bleepstatic.com/content/hl-images/2021/05/11/Facebook-headpic.jpg)


Facebook, Instagram, and WhatsApp are starting to come back online after a BGP routing issue caused an over five-hour worldwide outage.


Today, at approximately 11:50 AM EST, [all three websites were suddenly unreachable](https://www.bleepingcomputer.com/news/technology/facebook-whatsapp-and-instagram-down-due-to-dns-outage/), with browsers displaying DNS errors when attempting to open them.


When attempting to connect directly to the following Facebook DNS servers, it was also impossible to reach them.



![Unable to connect to Facebook's DNS servers](https://www.bleepstatic.com/images/news/u/1109292/2021/Facebook_DNS_down.png)**Unable to connect to Facebook's DNS servers**
As the DNS protocol tells your operating system and browsers the IP address of a website, with the DNS servers unreachable, it was impossible to connect to them.


BGP routing issue caused outages
--------------------------------


While at first, the issue appeared to be DNS related, it was later learned that that the problem was far worse than that.


As explained by Giorgio Bonfiglio, a Principal TAM at Amazon AWS, various Facebook routing prefixes had suddenly disappeared from the Internet's BGP routing tables, effectively making it impossible to connect to any services hosted on their IP addresses.




> 
> A bunch of Facebook networks has just disappeared from the internet: [pic.twitter.com/j07LrmAAdW](https://t.co/j07LrmAAdW)
> 
> 
> — Giorgio Bonfiglio (@g\_bonfiglio) [October 4, 2021](https://twitter.com/g_bonfiglio/status/1445056923309649926?ref_src=twsrc%5Etfw)


[BGP or the Border Gateway Protocol](https://www.cloudflare.com/en-gb/learning/security/glossary/what-is-bgp/) makes the modern-day Internet work and how a computer on one side of the world can connect to a device on the other.


To make it easier to understand, the BGP routing protocol is similar to an Internet "postal system," facilitating traffic from one (autonomous) system of networks to another. 


When a network wants to be seen on the Internet, they need to advertise their routes, or prefixes, with the rest of the world.


If those prefixes are removed, no one else on the Internet knows how to connect to their servers.


As Facebook configured their organization to use a domain registrar and DNS servers hosted on their own routing prefix, when those prefixes were removed, no one could connect to those IP addresses and the services running on to op of them.


Starting at 5 PM EST, the Facebook routing prefixes began to be seen on the BGP routing table at other networks. With these prefixes now being advertised on the Internet, users could connect to Facebook, Instagram, and WhatsApp once again.




> 
> Still trending positive: "HTTP/1.1 503 No server is available for the request"  
>   
> 
> (the absolutely fun thing here is I don't use Facebook - I'm just so passionate about outages and reliability in general) [pic.twitter.com/VLNNh725zQ](https://t.co/VLNNh725zQ)
> 
> 
> — Giorgio Bonfiglio (@g\_bonfiglio) [October 4, 2021](https://twitter.com/g_bonfiglio/status/1445141815770980353?ref_src=twsrc%5Etfw)


It is unclear what caused today's outage, but it was likely due to a configuration error, like many other BGP-related outages in the past.


BleepingComputer has reached out to Facebook to learn more about today's outage but has not heard back at this time.


Our earlier emails bounced as their emails servers were unreachable as well due to the outage.


As more detailed information becomes available, we will post an update with the new information.




#### Tags:
[[Facebook]] [[DNS]] [[BGP]] [[them.]] [[IP]] [[Giorgio]] [[Bleeping Computer]]
