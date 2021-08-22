# Mozi botnet gains the ability to tamper with its victims’ traffic
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/mozi-botnet-gains-the-ability-to-tamper-with-its-victims-traffic/)
+ Date: August 20, 2021
+ Author: Catalin Cimpanu


## Article:
![Mozi botnet gains the ability to tamper with its victims’ traffic](https://therecord.media/wp-content/uploads/2021/08/botnet-globe-map.png)

A new version of Mozi, a botnet that targets routers and IoT devices, is now capable of tampering with the web traffic of infected systems via techniques such as DNS spoofing and HTTP session hijacking, a capability that could be abused to redirect users to malicious sites.


Spotted by the Microsoft security team, these new capabilities are part of a revamped Mozi malware version that has recently begun targeting network gateway equipment manufactured by Netgear, Huawei, and ZTE.


“Network gateways are a particularly juicy target for adversaries because they are ideal as initial access points to corporate networks,” Microsoft said in a [report](https://www.microsoft.com/security/blog/2021/08/19/how-to-proactively-defend-against-mozi-iot-botnet/) on Thursday.


“By infecting routers, [Mozi] can perform man-in-the-middle (MITM) attacks—via HTTP hijacking and DNS spoofing—to compromise endpoints and deploy ransomware or cause safety incidents in OT facilities,” the company warned.


![Mozi-attack-flow](https://www-therecord.recfut.com/wp-content/uploads/2021/08/Mozi-attack-flow.png)Image: The Record
In addition, the new Mozi version also uses “clever persistence techniques that are specifically adapted to each gateway’s particular architecture.”


This allows Mozi operators to avoid having their malware erased during a device reboot and increase dwell times on infected devices, a feature that not all IoT malware strains possess.


#### Better persistence leads to more complex attacks


In turn, a prolonged infection time enables Mozi operators to plan and orchestrate attacks of a higher complexity than just flinging packets at a target as part of a DDoS attack.


In particular, Microsoft said it has now seen Mozi deploy modules on the infected network gateway that intercept DNS and HTTP requests.


The new Mozi versions can now tell infected gateways to answer DNS requests for specific domains with a custom IP address and send users to an attacker-controlled server—a technique that could help Mozi operators run phishing operations.


In addition, Microsoft said that another module allows the Mozi malware to hijack HTTP sessions and then inject malicious content inside web traffic.


This could be used to silently perform an HTTP 301 redirect that sends users from legitimate sites to malicious alternatives, or it can be used to inject malicious JavaScript code into legitimate sites, code that can be used to log keystrokes or steal passwords.


Microsoft said the Mozi botnet operators are currently exploiting weak Telnet passwords and nearly a dozen unpatched vulnerabilities to gain access to vulnerable devices. However, the OS maker did not provide any details about what vulnerabilities the botnet was exploiting or the Netgear, Huawei, and ZTE network gateway models that Mozi was seen attacking.




---


Prior to these recent developments, Mozi had been a botnet that has primarily engaged in executing DDoS attacks.


[First spotted in September 2019](https://blog.netlab.360.com/mozi-another-botnet-using-dht/) by Netlab, the botnet grew to [more than 15,000 infected devices](https://blog.lumen.com/new-mozi-malware-family-quietly-amasses-iot-bots/) by April 2020, according to Lumen’s Black Lotus Labs.


While there have been hundreds of IoT botnets that have infected devices across the past few years, Mozi has been one of the few that used DHT, a BitTorrent-like P2P protocol to interlink and control infected bots, according to an [IBM X-Force report](https://securityintelligence.com/posts/botnet-attack-mozi-mozied-into-town/).


Organizations like [ISC SANS](https://isc.sans.edu/forums/diary/Scanning+for+SOHO+Routers/26638/), [CUJO](https://cujo.com/upx-anti-unpacking-techniques-in-iot-malware/), and [Elastic](https://www.elastic.co/blog/collecting-and-operationalizing-threat-data-from-the-mozi-botnet) have also published reports about the Mozi botnet throughout 2020 and 2021, reports that show the botnet never went away but continued to operate in the shadows before deploying its new version.





#### Tags:
[[Mozi]] [[botnet]] [[HTTP]] [[Microsoft]] [[DNS]] [[malware]] [[IoT]] [[The Record]]
