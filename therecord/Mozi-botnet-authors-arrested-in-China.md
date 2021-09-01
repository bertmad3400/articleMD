# Mozi botnet authors arrested in China
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/mozi-botnet-authors-arrested-in-china/)
+ Date: September 1, 2021
+ Author: Catalin Cimpanu


## Article:
![Mozi botnet authors arrested in China](https://therecord.media/wp-content/uploads/2021/08/Mozi.png)

**The authors of the Mozi IoT botnet have been taken into custody by Chinese law enforcement earlier this year, according to Netlab, the networking security division of Chinese tech giant Qihoo 360.**


Details about the arrests and the suspects’ names have not been made public by Chinese authorities, Netlab researchers have told *The Record.*


The company touted its involvement in the investigation in two blog posts, [one in June](https://mp.weixin.qq.com/s/Su0-uU5JaUrAh8ptTzTCsA) and [one this Monday](https://blog.netlab.360.com/the_death_of_mozi_cn/), claiming that they’ve helped track down the botnet’s infrastructure and its operators.


News of the arrests also come after Microsoft published a [blog post](https://www.microsoft.com/security/blog/2021/08/19/how-to-proactively-defend-against-mozi-iot-botnet/) two weeks ago, describing a new Mozi module that can allow operators to [tamper or redirect its victims’ web traffic](https://therecord.media/mozi-botnet-gains-the-ability-to-tamper-with-its-victims-traffic/).


In its more expansive Monday blog post, Netlab researchers said the module was part of a new set of features the botnet operators rolled out before their arrests, along with a module that installed cryptocurrency miners on infected systems in an attempt to monetize the botnet beyond DDoS attacks.


### It will take months for the botnet to die out


[First spotted in September 2019](https://blog.netlab.360.com/mozi-another-botnet-using-dht/) by Netlab, the botnet quickly grew to [more than 15,000 infected devices](https://blog.lumen.com/new-mozi-malware-family-quietly-amasses-iot-bots/), according to research published by Black Lotus Labs in April 2020.


Under the hood, the botnet worked by infecting one device and then deploying a module that used the same infected system to search for other internet-connected devices and use exploits or easy-to-guess Telnet passwords to propagate to those systems as well.


Netlab said this worm-like module used more than ten exploits but was more than enough for the botnet to reach a massive size in a relatively short period of time.


Prior to its authors’ arrest, Netlab said the botnet peaked at 160,000 infected systems/day in September 2020 and had historically infected more than 1.5 million different devices, with more than half (830,000) located inside China.


![Mozi-distribution-map](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Mozi-distribution-map.png)Image: Netlab
The botnet also used the DHT protocol to create a peer-to-peer (P2P) system between all the infected devices, allowing bots to send updates and operational instructions to each other directly, which also permitted Mozi to continue to operate even without a central command and control (C&C) server.


This design choice makes taking down Mozi and all of its infected systems a rather challenging task as authorities need to shut down each infected system and can’t rely on a central node to send an “uninstall” command.


Furthermore, if infected devices are not cleaned in time, they may end up making new victims via their “worm” module, keeping the botnet alive even if its authors were detained by authorities, something that Netlab researchers themselves pointed out.



> The Mozi botnet samples have stopped updating for quite some time, but this does not mean that the threat posed by Mozi has ended. Since the parts of the network that are already spread across the internet have the ability to continue to be infected, new devices are infected every day. Overall we expect it to oscillate downward in size on a weekly basis but might keep alive for a long time, just like several other botnets that have been terminated by law enforcement agencies in the past.
> 
> Qihoo 360 Netlab


### Similar issue with Hoaxcalls botnet


But this isn’t an issue just for Mozi alone. Today, most IoT botnets have standalone worm-like modules that can live on, even after the botnet authors have been arrested or C&C servers have been taken down.


[Daniel Smith](https://twitter.com/hypoweb), an ERT researcher at security firm Radware, told *The Record* that the takedown of the [Hoaxcall botnet](https://www.radware.com/security/ddos-threats-attacks/threat-advisories-attack-reports/hoaxcalls-evolution/) earlier this year in April has also faced a similar technical issue, with the botnet’s zombie bots continuing to make new victims across the internet for months after.


![Hoaxcall-chart](https://www-therecord.recfut.com/wp-content/uploads/2021/09/Hoaxcall-chart.png)Image: Radware
“I expect Mozi to linger just as long,” Smith told *The Record* when estimating the time it would need for Mozi’s self-propagating infection cycle to die down.


“Because Mozi is a P2P botnet, taking down this botnet in one swoop is incredibly challenging. Even with the authors in jail, the botnet can propagate and infect new devices, but it will slowly begin to die out as network devices are rebooted, updated, or replaced,” Smith said.


“Since the botnet is relatively sophisticated and leverages multiple nodes and modules to propagate Mozi payloads, we expect Mozi to experience a slow death, similar to Hajime and Hoaxcalls.”





#### Tags:
[[botnet]] [[Mozi]] [[Netlab]] [[devices,]] [[blog]] [[time,]] [[The Record]]
