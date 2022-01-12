# Chrome will limit access to private networks, citing security reasons
### Google says that its Chrome browser will soon block internet websites from querying and interacting with devices and servers located inside local private networks, citing security reasons and past abuse from malware operations.

## Information:
+ Source: The Record
+ Link: https://therecord.media/chrome-will-limit-access-to-private-networks-citing-security-reasons/
+ Date: 2022-01-12T14:49:23+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2021/06/Chrome.png)

Google says that its Chrome browser will soon block internet websites from querying and interacting with devices and servers located inside local private networks, citing security reasons and past abuse from malware operations.


The change will take place through the implementation of a new W3C specification called [Private Network Access (PNA)](https://wicg.github.io/private-network-access/) that will be rolled out in the first half of the year.


The new PNA specification adds a mechanism inside the Chrome browser through which internet sites can ask systems inside local networks for permission before establishing a connection.



> Chrome will start sending a CORS preflight request ahead of any private network request for a subresource, which asks for explicit permission from the target server. This preflight request will carry a new header, ***Access-Control-Request-Private-Network: true***, and the response to it must carry a corresponding header, ***Access-Control-Allow-Private-Network: true***.
> 
> [Eiji Kitamura and Titouan Rigoudy, Google](https://developer.chrome.com/blog/private-network-access-preflight/)


If local devices, such as servers or routers fail to respond, internet websites will be blocked from connecting.


#### Browser have been used as proxies for attacks on local networks


The new PNA specification is one of the most important security features that will be added to Chrome in recent years.


Since the early 2010s, cybercrime groups have realized that they could use browsers as a “proxy” that relays connections to a company’s internal network.


For example, a malicious website could contain code that tries to access an IP address like 192.168.0.1, which is the typical address for most router administration panels, and accessible only from a local network.


When users access this kind of malicious site, their browser can make an automated request to their router without the user’s knowledge, sending malicious code that can bypass the router’s authentication and modify router settings.


These types of attacks are not just theoretical and have taken place before, with examples detailed [here](https://www.proofpoint.com/us/blog/threat-insight/home-routers-under-attack-dnschanger-malware-windows-android-devices) and [here](https://www.documentcloud.org/documents/21177481-team-cymru-soho-pharming).


Variation of this internet-to-local network attacks could also target other local systems, such as internal servers, domain controllers, firewalls, or even locally-hosted applications (via the http://localhost domain or other locally-defined domains).


![private-networks](https://therecord.media/wp-content/uploads/2022/01/private-networks.png)Image: Google
By introducing the PNA specification inside Chrome and its permission negotiation system, Google wants to prevent such automated attacks from being possible.


According to Google, a version of PNA has already been shipped with Chrome 96, released in November 2021, but full support will be rolled out in two phases this year, with the Chrome 98 (early March) and Chrome 101 (late May) releases, as detailed below:


1. In Chrome 98:


* Chrome sends preflight requests ahead of private network subresource requests.
* Preflight failures only display warnings in DevTools, without otherwise affecting the private network requests.
* Chrome gathers compatibility data and reaches out to the largest affected websites.
* We expect this to be broadly compatible with existing websites.


1. In Chrome 101 at the earliest:


* This will begin *only* if and when compatibility data indicates that the change is safe enough and we’ve outreached directly when necessary.
* Chrome enforces that preflight requests must succeed, otherwise failing the requests.
* [A deprecation trial](https://developer.chrome.com/blog/origin-trials/#deprecation-trials) starts at the same time to allow for websites affected by this phase to request a time extension. The trial will last for at least 6 months.






## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=route]] [[action.malware.name=S-Type]] [[action.malware.name=UPPERCUT]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Google]] [[Websites]] [[Pna]] [[The Record]]
#### ipv4-adresses
192.168.0.1
#### urls
http://localhost

