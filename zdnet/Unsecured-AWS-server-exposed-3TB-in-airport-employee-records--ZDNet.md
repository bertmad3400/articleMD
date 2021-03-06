# Unsecured AWS server exposed 3TB in airport employee records | ZDNet
### The exposure impacted airport staff across Colombia and Peru.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/unsecured-aws-server-exposed-airport-employee-records-3tb-in-data/
+ Date: 2022-01-31 13:06:00
+ Author: Charlie Osborne


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/1893bc0782df89e994f509e747a6f877b3d90212/2021/12/14/d488084b-7b98-48d6-8d4f-2b52db0678b6/shutterstock-1461611696.jpg?width=770&height=578&fit=crop&auto=webp)

An unsecured server has exposed sensitive data belonging to airport employees across Colombia and Peru. 


On Monday, the SafetyDetectives cybersecurity team said the server belonged [to Securitas](https://www.safetydetectives.com/news/securitas-leak-report/). The Stockholm, Sweden-based company provides on-site guarding, electronic security solutions, enterprise risk management, and fire & safety services. 

In a report shared with *ZDNet*, *SafetyDetectives* said one of Securitas's AWS S3 buckets was not appropriately secured, exposing over one million files on the internet.  

The server contained approximately 3TB of data dating back to 2018, including airport employee records. While the team was not able to examine every record in the database, four airports were named in exposed files: El Dorado International Airport (COL), Alfonso Bonilla Aragón International Airport (COL), José María Córdova International Airport (COL), and Aeropuerto Internacional Jorge Chávez (PE). 

The misconfigured AWS bucket, which did not require any authentication to access, contained two main datasets related to Securitas and airport employees. Among the records were ID card photos, Personally identifiable information (PII), including names, photos, occupations, and national ID numbers. 

In addition, SafetyDetectives says that photographs of airline employees, planes, fueling lines, and luggage handling were also found in the bucket. Unstripped .EXIF data in these photographs was exfiltrated, providing the time and date the photographs were taken as well as some GPS locations.  

![screenshot-2022-01-27-at-09-34-27.png]()![screenshot-2022-01-27-at-09-34-27.png](https://www.zdnet.com/a/img/resize/6f532a75f723126c62b0e1aafb2bd6e0efad722e/2022/01/27/5a808136-7d7e-4254-9e1d-ecbc60bff980/screenshot-2022-01-27-at-09-34-27.png?fit=bounds&auto=webp)
 SafetyDetectives
 "Considering Securitas' strong presence throughout Colombia and the rest of Latin America, companies in other industries could have been exposed," the researchers say. "It's also probable that various other places that use Securitas' security services are affected." 






Application IDs listed within mobile apps were also stored in the bucket. The IDs were used for airport activities, including incident reports, pointing the researchers to the likely owner in the first place.  

The cybersecurity researchers reached out to Securitas on October 28, 2021, and followed up on November 2 after receiving no response. Securitas engaged in conversation with the team and secured the server on the same day. Swedish CERT was also informed,

ZDNet has reached out to Securitas, and we will update when we hear back.  

**See also**

* ['We're losing control of our data' as breaches reach an all-time high](https://www.zdnet.com/article/data-breaches-reached-an-all-time-high-in-2021/)
* [The biggest data breaches, hacks of 2021](https://www.zdnet.com/article/the-biggest-data-breaches-of-2021/)
* [Enterprise data breach cost reached record high during COVID-19 pandemic](https://www.zdnet.com/article/enterprise-data-breach-cost-reached-record-high-during-covid-19-pandemic/)



---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Derusbi]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Sweden]] [[victim.continent.name=Europe]] [[victim.city.name=Stockholm]] [[victim.country.name=Sweden]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Colombia]] [[victim.continent.name=South America]] [[victim.country.name=Peru]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Securitas]] [[Safetydetectives]] [[(col)]] [[ZDNet]]

