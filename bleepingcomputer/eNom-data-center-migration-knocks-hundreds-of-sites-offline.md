# eNom data center migration knocks hundreds of sites offline
### A data center migration from eNom web hosting provider caused unexpected domain resolution problems that are expected to last for a few hours.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/enom-data-center-migration-knocks-hundreds-of-sites-offline/
+ Date: 2022-01-16T14:42:46-05:00
+ Author: Ionut Ilascu


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/05/04/dns-header.jpg)

![](https://www.bleepstatic.com/content/hl-images/2021/05/04/dns-header.jpg)


A data center migration from eNom web hosting provider caused unexpected domain resolution problems that are expected to last for a few hours.


Customers started to complain that they could no longer access their websites and emails due to Domain Name System (DNS) issues.



> 
> Enom services are down impacting access to websites and email.
> 
> 
> — Ken Westin (@kwestin) [January 16, 2022](https://twitter.com/kwestin/status/1482741278659940353?ref_src=twsrc%5Etfw)


  

My google apps gmail is not getting email, turns out DNS is not working because [@enom](https://twitter.com/enom?ref_src=twsrc%5Etfw) is doing "a datacenter move" that ran into problems. What medieval times are these when a datacenter move brings down DNS for organizations? Advance warning would have been nice [@enomsupport](https://twitter.com/enomsupport?ref_src=twsrc%5Etfw).



> — Pieter Viljoen (@pieter727) [January 16, 2022](https://twitter.com/pieter727/status/1482747188270665730?ref_src=twsrc%5Etfw)


The company said that it received reports of domains using eNom nameservers that were failing to resolve and acknowledged the problem.



"We are receiving some reports of domains using our nameservers which are failing to resolve. Owing to the migration we are unable to research and fully address the issue until the migration is complete. This is not an expected outcome from the migration, and we are working to address it as a priority" - [eNom](https://enomstatus.com/)



After looking into the issue, the company has found that the domain resolution problems are affecting a few hundred domains. eNom estimates that the outage would last for a few hours.


eNom customers affected by the problem can't change the nameservers because eNom is down and all they can do is wait for the migration to complete:



"What's absolutely nuts about this is we can not change our NameServers due to eNom itself is down (going on 24 hours now). Never in my life have I been in a situation where I can't route around network issue at the root domain records level. We are totally trapped!" - [eNom customer](https://www.reddit.com/r/sysadmin/comments/s4ucsk/enom_dns_down_anything_on_nameservicescom_etc/hsvx0fy/)



An initial maintenance notice from the company said that the data center migration would take 12 hours, between 6 AM PST and 6 PM PST on Saturday, January 15.


During this period, enom.com and enomcentral.com would be unavailable and customers would not be able to log into their account from the web interface and the API would be down.


While some management actions would not be possible, the company said that DNS resolution and email services would remain operational.


In subsequent updates on the progress of the data center migration progress, the company announced multiple extensions for completing the process, the latest one being for January 16, 12:00 PM PST.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=route]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Enom]] [[Dns]] [[Nameservers]] [[Bleeping Computer]]

