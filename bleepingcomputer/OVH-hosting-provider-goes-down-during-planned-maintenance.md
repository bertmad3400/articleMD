# OVH hosting provider goes down during planned maintenance
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/technology/ovh-hosting-provider-goes-down-during-planned-maintenance/)
+ Date: October 13, 2021
+ Author: Sergiu Gatlan


## Article:
![OVH hosting provider goes down during planned maintenance](https://www.bleepstatic.com/content/posts/2021/10/13/OVH.jpg)


OVH, the largest hosting provider in Europe and the third-largest in the world, went down earlier today following what looks like routing configuration issues during planned maintenance.


OVH has 32 data centers with over 300,000 servers on four continents and a total of 20 Tbit/s global network capacity.


It provides web hosting, cloud computing services, and dedicated servers to 1,300,000 enterprise customers worldwide.


Outage caused by bad router configuration
-----------------------------------------


"We will do a maintenance on our routers on VIN DC to improve our routing," the company said on its status page before its servers went down.


"Maintenance is planned for 13/Oct/21 9:00 AM to 10:30 AM ( UTC+2). No impact expected, device will be isolated before the change."


However, due to unknown issues encountered during the planned maintenance, the hosting provider's servers became unreachable, also taking down customers' sites with them.



![OVH maintenance](https://www.bleepstatic.com/images/news/u/1109292/2021/OVH_maintenance.png)*OVH maintenance (BleepingComputer)*
"Following a human error during the reconfiguration of the network on our DC to VH (US-EST), we have a problem on the whole backbone. We are going to isolate the DC VH then fix the conf," OVH founder Octave Klaba [explained](https://twitter.com/olesovhcom/status/1448196879020433409).


"In recent days, the intensity of DDoS attacks has increased significantly. We have decided to increase our DDoS processing capacity by adding new infrastructures in our DC VH (US-EST). A bad configuration of the router caused the failure of the network."


According to reports [[1](https://twitter.com/liotier/status/1448195033635737604), [2](https://twitter.com/bortzmeyer/status/1448191494511337472)], the ongoing outage only affects IPv4 infrastructure, with IPv6 infra still up and reachable over the Internet.




> 
> Suite à une erreur humaine durant la reconfiguration du network sur notre DC à VH (US-EST), nous avons un souci sur la toute la backbone. Nous allons isoler le DC VH puis fixer la conf. <https://t.co/kDakq7FGBO>
> 
> 
> — Octave Klaba (@olesovhcom) [October 13, 2021](https://twitter.com/olesovhcom/status/1448196879020433409?ref_src=twsrc%5Etfw)


When trying to connect to the [OVH website](https://www.ovh.com/fr), users are currently seeing "Error 503: Backend unavailable" errors explaining that "This type of error usually results of an unavailability of servers behind IP Load Balancing."


Visitors are asked to refresh the site or return in a few minutes and reach out to OVH's support team if the problem persists.


The [hosting provider's status page](https://status.ovh.com/) also went down with the company's servers during the maintenance process, with the page now displaying "The connection has timed out. An error occurred during a connection to status.ovh.com," errors.



![OVH loading errors](https://www.bleepstatic.com/images/news/u/1109292/2021/OVH_hosting_errors.png)*OVH loading errors (BleepingComputer)*
Earlier his year, major sites also went offline after OVH data centers from Strasbourg, France, [burnt down in March](https://www.bleepingcomputer.com/news/technology/ovh-data-center-burns-down-knocking-major-sites-offline/).


Its SBG1, SBG2, SBG3, and SBG4 Strasbourg data centers were shut down to contain the damage from the fire that started in SBG2.


The list of impacted clients included videogame maker *[Rust](https://twitter.com/playrust/status/1369611688539009025),*provider of free chess server *[Lichess.org](https://twitter.com/lichess/status/1369543554255757314),* telecom company*[AFR-IX](https://twitter.com/AFR_IXtelecom/status/1369591271350824963)*,encryption utility*[VeraCrypt](https://twitter.com/VeraCrypt_IDRIX/status/1369523849532936193),*news outlet*[eeNews Europe](https://twitter.com/eeNewsEurope/status/1369553694803525635),*cryptocurrency exchange*[Deribit](https://twitter.com/DeribitExchange/status/1369515819546210306)'s* blog and docs sites*,*the art building complex *[Centre Pompidou](https://twitter.com/CentrePompidou/status/1369591294725652480),*and many many others.


The company's founder later [explained](https://www.bleepingcomputer.com/news/security/ovh-data-center-fire-likely-caused-by-faulty-ups-power-supply/) that SBG2 was an older generation center built in 2011 and that OVH was working towards replacing older infra with newer technology.  


*This is a developing story ...*


*Update Oct 13, 04:59 EST:* OVH's network is slowly recovering after it went down 07:20 UTC this morning together with a US router with a faulty configuration.


"Since 08:22 UTC all services are gradually returning following the isolation of network equipment in the US," the company [says](http://travaux.ovh.net/?do=details&id=53798&edit=yep).


Klaba [tweeted](https://twitter.com/olesovhcom/status/1448202696071254016) earlier that the router with the wrong D2 configuration has been cut from the network.



![OVH services status](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)*OVH services status (BleepingComputer)*


#### Tags:
[[OVH]] [[VH]] [[(BleepingComputer)]] [[Klaba]] [[Bleeping Computer]]
