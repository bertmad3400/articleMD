# Passport info and healthcare data leaked from Indonesia's COVID-19 test-and-trace app for travelers
### About 1.3 million people had their sensitive personal data, COVID-19 test results and more exposed on an open server.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/passport-info-and-healthcare-data-leaked-from-indonesias-covid-19-test-and-trace-app-for-travellers/)
+ Date: August 30, 2021 -- 21:59 GMT (22:59 BST)
+ Author: Jonathan Greig


## Article:
Unknown

Researchers with vpnMentor have [uncovered a data breach](https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.vpnmentor.com%2Fblog%2Freport-ehac-indonesia-leak%2F&data=04%7C01%7Cjgreig%40redventures.com%7C168abf6408a04da13c5608d96bf95601%7C4289d6102cfd46218c9644a1518ddb0a%7C0%7C0%7C637659542127325235%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=HWoTZFDGcJitEGMVSHqJQvMA8ypTrIEG%2FkpEu8zh0GE%3D&reserved=0) involving the COVID-19 test and trace app created by the Indonesian government for those traveling into the country. 

The 'test and trace app' -- named electronic Health Alert Card or eHAC -- was created in 2021 by the Indonesian Ministry of Health but the vpnMentor team, lead by Noam Rotem and Ran Locar, said it did not have the proper data privacy protocols and exposed the sensitive data of more than one million people through an open server. 

The app was built to hold the test results of those traveling into the country to make sure they were not carrying COVID-19 and is a mandatory requirement for anyone flying into Indonesia from another country. Both foreigners and Indonesian citizens must download the app, even those traveling domestically within the country. 

The eHAC app keeps track of a person's health status, personal information, contact information, COVID-19 test results and other data.


Rotem and Locar said their team discovered the exposed database "as part of a broader effort to reduce the number of data leaks from websites and apps around the world." 

"Our team discovered eHAC's records with zero obstacles, due to the lack of protocols in place by the app's developers. Once they investigated the database and confirmed the records were authentic, we contacted the Indonesian Ministry of Health and presented our findings," the vpnMentor research team said. 

"After a couple of days with no reply from the ministry, we contacted Indonesia's Computer Emergency Response Team agency and, eventually, Google -- eHAC's hosting provider. By early August, we had not received a reply from any of the concerned parties. We tried to reach out to additional governmental agencies, one of them being the BSSN (Badan Siber dan Sandi Negara), which was established to carry out activities in the field of cyber security. We contacted them on August 22nd and they replied on the same day. Two days later, on August 24, the server was taken down." 






The Indonesian Ministry of Health and Foreign Ministry did not respond to requests for comment from ZDNet. 

In their report, the researchers explain that the people who created eHAC used an "unsecured Elasticsearch database to store over 1.4 million records from approximately 1.3 million eHAC users."

On top of the leak of sensitive user data, the researchers found that all of the infrastructure around eHAC was exposed, including private information about local Indonesian hospitals as well as government officials who used the app. 

The data involved in the leak includes user IDs -- which ranged from passports to national Indonesian ID numbers -- as well as COVID-19 test results and data, hospital IDs, addresses, phone numbers, URN ID number and URN hospital ID number. For Indonesians, their full names, numbers, dates of birth, citizenship, jobs and photos were included in the leaked data. 


The researchers also found data from 226 hospitals and clinics across Indonesia as well as the name of the person responsible for testing each traveller, the doctors who ran the test, information about how many tests were done each day and data on what kinds of travelers were allowed at the hospital. 

The leaked database even had personal information for a traveler's parents or next of kin as well as their hotel details and other information about when the eHAC account was created. 

Even eHAC staff members had their names, ID numbers, account names, email addresses and passwords leaked. 

"Had the data been discovered by malicious or criminal hackers, and allowed to accumulate data on more people, the effects could have been devastating on an individual and societal level," the researchers said. 

"The massive amount of data collected and exposed for each individual using eHAC left them incredibly vulnerable to a wide range of attacks and scams. With access to a person's passport information, date of birth, travel history, and more, hackers could target them in complex (and simple) schemes to steal their identity, track them down, scam them in person, and defraud them of thousands of dollars. Furthermore, if this data wasn't sufficient, hackers could use it to target a victim in phishing campaigns over email, text, or phone calls." 


The vpnMentor research team uses "large-scale web scanners" as a way to search for unsecured data stores containing information that shouldn't be exposed.

"Our team was able to access this database because it was completely unsecured and unencrypted. eHAC was using an Elasticsearch database, which is ordinarily not designed for URL use," the researchers added. 

"However, we were able to access it via browser and manipulate the URL search criteria into exposing schemata from a single index at any time. Whenever we find a data breach, we use expert techniques to verify the owner of the database, usually a commercial business." 

The report notes that with all of the data, it would be easy for hackers to pose as health officials and conduct any number of scams on any of the 1.3 million people whose information was leaked. 

Hackers could have also changed data in the eHAC platform, potentially hampering the country's COVID-19 response. 

The researchers noted that they were wary of testing any of these potential attacks out of fear of disrupting the country's efforts to contain COVID-19, which may already be damaged by the government's haphazard management of the database.

The vpnMentor team added that if there was a hack or ransomware attack involving the database, it could have led to the kind of distrust, misinformation and conspiracy theories that have gained a foothold in dozens of countries. 

"If the Indonesian people learned the government had exposed over 1 million people to attack and fraud via an app built to combat the virus, they may be reluctant to engage in broader efforts to contain it -- including vaccine drives," the researchers said. 

"Bad actors would undoubtedly exploit the leak for their gain, jumping on any frustration, fear, or confusion, creating mistruths and exaggerating the leak's impact beyond all reasonable proportion. All of these outcomes could significantly slow down Indonesia's fight against Coronavirus (and misinformation in general) while forcing them to use considerable time and resources to fix their own mess. The result is further pain, suffering, and potential loss of life for the people of Indonesia."

The researchers said the designers of the eHAC system needed to secure the servers, implement proper access rules and made sure to never leave the system, which did not require authentication, open to the internet. 

They urged those who may think their information was affected to contact the Indonesian Ministry of Health directly to figure out what next steps may need to be taken. 

eHAC is far from the only COVID-19 related app to face similar problems. Since the beginning of the pandemic, the emergence of contact tracing apps [has caused worry among researchers](https://s2.washingtonpost.com/2a06c7c/5ef0952dfe1ff654c2022a65/598281039bbc0f6826e088f7/12/49/9460799db8e498ac99aebdacf1fde982) who have [repeatedly shown how faulty these tools can be](https://s2.washingtonpost.com/2a06c7b/5ef0952dfe1ff654c2022a65/598281039bbc0f6826e088f7/11/49/9460799db8e498ac99aebdacf1fde982). 

Just last week, Microsoft [faced significant backlash](https://www.wired.com/story/microsoft-power-apps-data-exposed/) after their Power Apps were found to have exposed 38 million records online, including contact tracing records. 

In May, the personal health information belonging to tens of thousands of Pennsylvanians [was exposed](https://www.post-gazette.com/news/crime-courts/2021/04/29/Contact-tracing-breach-impacts-private-info-of-72K-people-Insight-Global-Pennsylvania/stories/202104290159) following a data breach at a Department of Health vendor. The Department of Health accused a vendor of exposing the data of 72,000 people by willfully disregarding security protocols. 





#### Tags:
[[eHAC]] [[COVID-19]] [[vpnMentor]] [[country.]] [[information,]] [[said.]] [[data,]] [[numbers,]] [[names,]] [[database,]] [[ZDNet]]
