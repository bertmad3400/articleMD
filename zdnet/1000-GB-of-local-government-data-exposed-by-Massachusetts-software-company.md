# 1,000 GB of local government data exposed by Massachusetts software company
### A group of ethical researchers found over 80 misconfigured Amazon S3 buckets holding data related to about 100 municipalities across the Northeast.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/1000-gb-of-local-government-data-exposed-by-massachusetts-software-company/)
+ Date: July 22, 2021 -- 12:00 GMT (13:00 BST)
+ Author: Jonathan Greig


## Article:
Unknown

More than 1,000 GB of data and over 1.6 million files from dozens of municipalities in the US were left exposed, according to [a new report](https://www.wizcase.com/blog/us-municipality-breach-report/) from a team of cybersecurity researchers with security company WizCase. 


All of the towns and cities appeared to be connected through one product: mapsonline.net, which is owned by a Massachusetts company called PeopleGIS. The company provides information management software to local governments across Massachusetts, New Hampshire and Connecticut. 

Ata Hakçıl and his team discovered more than 80 misconfigured Amazon S3 buckets holding data related to these municipalities. The data ranged from residential records like deeds and tax information to business licenses and job applications for government positions. 

Due to the sensitive nature of the documents, many of the forms included people's email address, physical address, phone number, driver's license number, real estate tax information, license photographs and photos of property. 

The researchers shared redacted photos of the data available. 

"The data of these municipalities was stored in several misconfigured Amazon S3 buckets that were sharing similar naming conventions to MapsOnline. Due to this, we believe these cities are using the same software solution," the report said. 

"Our team reached out to the company and the buckets have since been secured."






Not every municipality had the same information exposed, and the report said the types of files leaked varied. The researchers were not able to provide an estimate on the number of people affected by the exposure because of how varied the forms were. 

The security company deployed a scanner that found 114 Amazon Buckets connected to PeopleGIS and named similarly. According to the report, 28 were configured correctly while "86 were accessible without any password nor encryption."

The researchers did not have a definitive reason for why some buckets were properly secured and others were not. 

They suggested that PeopleGIS simply "created and handed over the buckets to their customers (all municipalities), and some of them made sure these were properly configured."

Another theory involved a potential situation where different employees at PeopleGIS -- without clear guidelines -- created and configured each bucket. 

The third theory was that the municipalities themselves created the buckets with basic guidelines from PeopleGIS "about the naming format but without any guidelines regarding the configuration."

The researchers said this "would explain the difference between the municipalities whose employees knew about it or not."

"The breach could lead to massive fraud and theft from citizens of those municipalities. The highly-sensitive nature of the data contained within a local government's database, from phone numbers to business licenses to tax records, are highly susceptible to exploitation by bad actors," the report said. 

"Much of this information is supposed to be only accessible by the government and the citizens, meaning someone could potentially defraud an individual by posing as a government official."

PeopleGIS did not respond to requests for comment. 





#### Tags:
[[PeopleGIS]] [[ZDNet]]
