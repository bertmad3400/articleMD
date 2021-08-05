# EU officials investigating breach of Cybersecurity Atlas project
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/eu-officials-investigating-breach-of-cybersecurity-atlas-project/)
+ Date: August 5, 2021
+ Author: Catalin Cimpanu


## Article:
![EU officials investigating breach of Cybersecurity Atlas project](https://therecord.media/wp-content/uploads/2021/05/EU-flag-e1628172877702.jpg)

The European Commission is investigating a breach of its Cybersecurity Atlas project after a copy of the site’s backend database was put up for sale on an underground cybercrime forum on Monday.


[Launched in 2018](https://joinup.ec.europa.eu/collection/egovernment/news/cybersecurity-atlas), the [Cybersecurity Atlas](https://cybersecurity-atlas.ec.europa.eu/) is a Yellow-Pages-like contact list of European organizations with cybersecurity expertise.


Described on its website as a “knowledge management platform to map, categorise and stimulate collaboration between European cybersecurity experts,” the Cybersecurity Atlas project allows cybersecurity experts to sign up and list their contact details on the EC web portal.


The Commission claims that “organisations participating in the Atlas have the opportunity to enlarge their research network, to get in contact with relevant peers, and to improve the organisation visibility.”


#### Member data was public, but questions arise about the breach


On Monday, a threat actor posted a thread on an underground cybercrime forum claiming to have obtained access to the entire Cybersecurity Atlas database, which they were willing to sell via Discord.


![EU-EC-Atlas-data-sale-forum](https://www-therecord.recfut.com/wp-content/uploads/2021/08/EU-EC-Atlas-data-sale-forum-1024x471.png)Image: The Record
*The Record* obtained a copy of this database for reporting purposes with the help of an individual know as [Kelvin Security](https://twitter.com/Ksecureteamlab).


We were quickly able to confirm that the database contained authentic details for cybersecurity companies, universities, research centers, and government organizations across Europe.


This included details such as site usernames, email addresses, institution details, full names of contact persons, and organization addresses and geolocation points that the Atlas project used to plot member details on a map.


![EU-EC-Atlas-sample](https://www-therecord.recfut.com/wp-content/uploads/2021/08/EU-EC-Atlas-sample-1024x751.png)Image: The Record
While by the nature of being a public inventory of contacts details, the data in the Cybersecurity Atlas and its members was supposed to be public and accessible by design, *The Record* was able to confirm that this information was an SQL database dump of the project’s Drupal website rather than being a scrape of data listed on the official site.


This meant that a threat actor breached the Commission’s database servers and gained access to the Cybersecurity Atlas backend.


The sale of already-publicly-listed data was not of concern to *The Record*.


Instead, we were interested in how the threat actor could have abused access to this portal to carry out phishing or watering hole attacks against cybersecurity experts directly from the European Commission’s website, attacks that would have a big chance of succeeding.


“Appropriate measures have been taken immediately, and the relevant Commission services are investigating the matter,” an EC spokesperson told *The Record* this morning after the Atlas website was put into maintenance mode.


“We are working closely with CERT-EU, the Computer Emergency Response Team for all the EU institutions, bodies, and agencies to analyse the incident,” the spokesperson added.


The intrusion comes as CERT-EU said in a June 2021 report that EU organizations suffered more than 1,432 security incidents last year, the highest number of incidents in CERT-EU’s ten years history [[PDF](https://media.cert.europa.eu/static/MEMO/2021/TLP-WHITE-CERT-EU-Threat_Landscape_Report-Volume1.pdf#page=13&zoom=auto,-274,51)].





#### Tags:
[[Cybersecurity]] [[cybersecurity]] [[website]] [[The Record]]
