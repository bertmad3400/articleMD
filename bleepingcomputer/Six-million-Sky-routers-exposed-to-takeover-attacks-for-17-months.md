# Six million Sky routers exposed to takeover attacks for 17 months
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/six-million-sky-routers-exposed-to-takeover-attacks-for-17-months/)
+ Date: November 19, 2021
+ Author: Bill Toulas


## Article:
![modem_router](https://www.bleepstatic.com/content/hl-images/2021/11/19/modem_router.jpg?rand=827220111)


Around six million Sky Broadband customer routers in the UK were affected by a critical vulnerability that took over 17 months to roll out a fix to customers.


The disclosed vulnerability is a [DNS rebinding flaw](https://www.bleepingcomputer.com/news/security/bluestacks-flaw-lets-attackers-remotely-control-android-emulator/) that threat actors could easily exploit if the user had not changed the default admin password, or a threat actor could brute-force the credentials.


The result of the exploitation would be to compromise the customer's home network, change the router's configuration, and potentially pivot to other internal devices.


The DNS rebinding attack on Sky routers
---------------------------------------


DNS rebinding attacks are used to bypass a browser security measure called Same Origin Policy (SOP), which blocks a site from sending requests to websites other than its own origin. This origin is usually the domain you visited in the browser.


This security measure was introduced to block one website from stealing cookies for another site, accessing data on other sites, or performing other cross-domain attacks.


As SOP focuses on the domain name rather than the IP address, the goal is to trick a browser into thinking a script was talking to the original domain, but in reality, is talking to an internal IP address (127.0.01/192.168.0.1).


This is where DNS Rebinding attacks come into play, and when conducted properly, leads to a whole slew of attacks.


For the attack to work, the victim has to be tricked into clicking a malicious link or visiting a malicious website. This could easily be done by a threat actor sending Sky customers phishing emails, social media posts, SMS texts containing links to the malicious site.


Once the victim visits the site, an iframe would be displayed that requests data from an attacker-controlled subdomain.


This script then loads a JavaScript payload on the iframe, which performs consecutive HTTP requests to the server, with the latter responding with its IP address.


After a few seconds, the server stops responding to these requests, and this triggers the re-initiation of the browser's connection to the domain, so a new DNS request is sent.


However, this time, the server replies with the target's IP address (192.168.0.1), which is the victim's router.


As the browser thinks it is still communicating with the origin domain, it will allow the remote website's script to send requests to the router's internal IP address (192.168.0.1).



![The DNS re-binding attack flow](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/diagram(1).jpg)**The DNS re-binding attack flow**  
*Source: PenTestPartners*
"After the connection from the JavaScript payload to the target router was established, the attacker could communicate with the internal web server and could make requests that would change settings in the same way that would normally happen from a clients web browser," explained PenTestPartners in [their report](https://www.pentestpartners.com/security-blog/skyfail-6-million-routers-left-exposed/).


Using this vulnerability, the researchers created a PoC exploit that could perform a variety of malicious activity on the router, including:


* Log in as the administrator with default credentials (user: admin – password: sky)
* Change the admin password (necessary to enable remote management)
* Collect and display the SSID name and WPA2 password
* Enable remote management


A demonstration of this exploit can be see in the video below created by PenTestPartners as part of their report.



This PoC works on the following router models, which correspond to roughly six million users:


* Sky Hub 3, 3.5, and Booster 3 (ER110, ER115, EE120)
* Sky Hub 2 and booster 2 (SR102, SB601)
* Sky Hub (SR101)
* Sky Hub 4 and Booster 4 (SR203, SE210) – limited impact due to shipping these with random passwords


Fix took 17 months to roll out
------------------------------


The PenTestPartners team reported their findings on May 11, 2020, and Sky acknowledged the issue and set a fixing date for November 2020.


That was over the standard 90 days of vulnerability disclosure, but the researchers accepted it without objection since the ISP was dealing with unusual traffic burdens from the COVID-19 lockdown.


The fixing patch never came, and Sky eventually revised the plan, promising to fix 50% of the affected models by May 2021, which was fulfilled.


With the other half still vulnerable and PenTestPartners feeling that Sky was not acting with much urgency, the researchers contacted the press in August as a way to apply additional pressure.


Eventually, on October 22, 2021, Sky emailed to say that Sky had fixed 99% of all vulnerable routers via an update.


This was over 17 months since the initial disclosure, leaving users vulnerable to DNS rebinding attacks during a period when many of them worked from home.




#### Tags:
[[DNS]] [[IP]] [[PenTestPartners]] [[domain,]] [[Bleeping Computer]]
