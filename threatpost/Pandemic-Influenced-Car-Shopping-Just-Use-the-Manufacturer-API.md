# Pandemic-Influenced Car Shopping: Just Use the Manufacturer API
### Jason Kent, hacker-in-residence at Cequence, found a way to exploit a Toyota API to get around the hassle of car shopping in the age of supply-chain woes.

## Information:
+ Source: ThreatPost
+ Link: https://kasperskycontenthub.com/threatpost-global/?p=176740
+ Date: 2021-12-03T20:09:24+00:00
+ Author: Jason Kent


## Article:
![Article Image](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/03120815/noleggio-auto-1024x682-1.jpg)

The pandemic has caused huge disruptions in the supply chain for a wide variety of industries. One of the major areas feeling the global issues is the car industry. Fortunately, I found a way to exploit a manufacturer API to minimize my frustration.


First, some background: Many outlets have widely reported that manufacturers are putting 99 percent of a vehicle together, parking it in a lot somewhere and assuming the missing parts, like computer chips, will be available soon and they’ll be able to make the engines run so the vehicles can be sold. On a recent road trip, I went past the F150 factory and saw the massive parking lot at Kentucky Speedway, filled with factory-new trucks that will not start and are unsellable.


[Infosec Insiders Newsletter](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------


My 2015 Tacoma is getting to the point where I want to make a decision to either finish setting it up for camping, or trade it in and get a newer one to fix up for camping. And thus, I find myself trying to find a new Tacoma, in the middle of the pandemic-induced supply disruption. The problems quickly became irritating as I began my search:


1. 1. Dealership websites might have had accurate inventory three years ago but, now they aren’t worth looking at now;
	2. Cars that are on the website were sold two days ago and the cars that arrived at the dealership yesterday aren’t on the website yet. This delay means that there is no way to see what the dealer has.


Snooping around on various dealership websites I found a link, buried in the page, that lets you pull up an “available” vehicle window sticker. Contained in the sticker is the destination. If I look at the URL for [the page the window sticker is generated on](https://api.toyotainventory.com/vehicles/3TMDZ5BN6NM122105/monroney), it looks like this:


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/03115543/monroney-1024x647.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/03115543/monroney.png)


So, rather than tediously browsing dealer websites to view inaccurate information, I turned to pulling data from the manufacturer API that I had found, to see what is being built and where I can buy it. 


**Finding the Perfect Truck**
-----------------------------


The big group of numbers after “vehicles” is the VIN for a truck I am interested in. The beginning of the VIN is the manufacturer and model, and the numeric part at the end is the serial number for the vehicle. In my research, I tried to just put in the next number higher and this didn’t work. 3TMDZ5BN6NM122106 didn’t get me the same vehicle just created later, it didn’t get me anything. This meant I had to turn to tools to figure out how I can find my next ride. Loading this request into BURP (an intercept proxy that allows me to manipulate requests to webservers), and iterating through large batches was probably going to be necessary.


[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/03120122/Screen-Shot-2021-12-03-at-12.01.05-PM-1024x384.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/03120122/Screen-Shot-2021-12-03-at-12.01.05-PM.png)[![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/03120233/Screen-Shot-2021-12-03-at-12.02.14-PM-1024x472.png)](https://media.threatpost.com/wp-content/uploads/sites/103/2021/12/03120233/Screen-Shot-2021-12-03-at-12.02.14-PM.png)


I set up the requests to iterate through the last four digits of the VIN, finding a few vehicles I could look at and contacting the dealerships regarding availability. If I run this often enough, I can look at vehicles that were created today and contact the dealerships they are not yet in transit to. 


Pulling apart web communications, noticing patterns in the requests being made and finally figuring out how the structure works is what I do for a living. It’s unrealistic to expect the average car buyer to start writing bots to figure out how to find their next vehicle. But a more realistic expectation is for the car manufacturer to spend a bit more time using the technology that they have already built – a database, a set of APIs, a web presence – to give consumers a source of accurate information. 


**Exploitable Flaw or Public Information?**
-------------------------------------------


Is there a security flaw here? This is an “it depends” kind of question. The API exposed is completely public. The way an API is used is to request something via simple query parameters. This API seems to be very simplistic. It looks as if this API was built to segregate traffic from the rest of the inventory systems and to allow someone, perhaps a dealer, to take a quick look at a built vehicle – perhaps for a buyer like me? From a strategy and application-design standpoint, Toyota is doing very well here. Keeping their estate safe from someone looking to attack it means keeping things well-segregated and controlled.


The next question is whether it could be exploited. Absolutely. An understanding of inventory and availability is a core requirement for inventory hoarding, seat spinning and shopping bots (aka “grinch bots”). For now, we will assume it is used to provide a preview of coming vehicles with the hope that Toyota will take steps to use what they have to improve shopping experience. 


In the meantime, I am on my way to a different state to buy a new truck. 


***Jason Kent is the Hacker in Residence at [Cequence Security.](https://www.cequence.ai)***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by visiting our [visiting our microsite](https://threatpost.com/microsite/infosec-insiders-community/).***





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Manufacturing]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Api]] [[Websites]] [[ThreatPost]]

