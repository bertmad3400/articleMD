# Secret terrorist watchlist with 2 million records exposed online
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/secret-terrorist-watchlist-with-2-million-records-exposed-online/)
+ Date: August 16, 2021
+ Author: Ax Sharma


## Article:
![usa](https://www.bleepstatic.com/content/hl-images/2020/12/07/US-Capitol--Congress.jpg)


A secret terrorist watchlist with 1.9 million records, including classified "no-fly" records was exposed on the internet.


The list was left accessible on an Elasticsearch cluster that had no password on it.


Millions of people on no-fly and terror watchlists exposed
----------------------------------------------------------


July this year, Security Discovery researcher Bob Diachenko came across a plethora of JSON records in an exposed Elasticsearch cluster that piqued his interest.


The 1.9 million-strong recordset contained sensitive information on people, including their names, country citizenship, gender, date of birth, passport details, and no-fly status.


The exposed server was indexed by search engines Censys and ZoomEye, indicating Diachenko may not have been the only person to come across the list:



![exposed watchlist records](https://www.bleepstatic.com/images/news/u/1164866/2021/Aug-2021/tsc-list-leak/tsc-records.jpg)**An excerpt from exposed watchlist records**([Bob Diachenko](https://twitter.com/MayhemDayOne/status/1417174479323680775))
The researcher told BleepingComputer that given the nature of the exposed fields (e.g. passport details and "no\_fly\_indicator") it appeared to be a no-fly or a similar terrorist watchlist.


Additionally, the researcher also noticed some oblique fields such as "tag," "nomination type," and "selectee indicator," that weren't imminently understood by him.


"That was the only valid guess given the nature of data plus there was a specific field named 'TCS\_ID'," Diachenko told BleepingComputer, which indicated to him the source of the recordset could be the Terrorist Screening Center (TSC).


FBI's [TSC](https://www.fbi.gov/about/leadership-and-structure/national-security-branch/tsc) is used by multiple federal agencies to manage and share consolidated information for counterterrorism purposes.


The agency maintains the classified watchlist called the Terrorist Screening Database, sometimes also referred to as the "[no-fly list](https://en.wikipedia.org/wiki/No_Fly_List)."


Such databases are regarded as highly sensitive in nature, considering the vital role they play in aiding national security and law enforcement tasks.


Terrorists or reasonable suspects who pose a national security risk are "nominated" for placement on the secret watchlist at the government's discretion.


The list is referenced by airlines and multiple agencies such as the Department of State, Department of Defense, Transportation Security Authority (TSA), and Customs and Border Protection (CBP) to check if a passenger is allowed to fly, inadmissible to the U.S. or assess their risk for various other activities.


Server taken offline 3 weeks after DHS notified
-----------------------------------------------


The researcher discovered the exposed database on July 19th, interestingly, on a server with a Bahrain IP address, not a US one.


However, the same day, he rushed to report the data leak to the U.S. Department of Homeland Security (DHS).


"I discovered the exposed data on the same day and reported it to the DHS."


"The exposed server was taken down about three weeks later, on August 9, 2021."


"It's not clear why it took so long, and I don't know for sure whether any unauthorized parties accessed it," writes Diachenko in his [report](https://www.linkedin.com/pulse/americas-secret-terrorist-watchlist-exposed-web-report-diachenko/).


The researcher considers this data leak to be serious, considering watchlists can list people who are suspected of an illicit activity but not necessarily charged with any crime.


"In the wrong hands, this list could be used to oppress, harass, or persecute people on the list and their families."


"It could cause any number of personal and professional problems for innocent people whose names are included in the list," says the researcher.


Cases, where people [landed on the no-fly list](https://www.aclu.org/news/national-security/i-refused-to-become-an-fbi-informant-and-the-government-put-me-on-the-no-fly-list/) for refusing to become an informant, aren't unheard of.


Diachenko believes this leak could therefore have negative repercussions for such people and suspects.


"The TSC watchlist is highly controversial. The ACLU, for example, has for many years [fought against](https://www.aclu.org/cases/kashem-et-al-v-barr-et-al-aclu-challenge-government-no-fly-list?redirect=national-security/latif-et-al-v-holder-et-al-aclu-challenge-government-no-fly-list) the use of a secret government no-fly list without due process," continued the researcher.


Note, it is not confirmed if the server leaking the list belonged to a U.S. government agency or a third-party entity.


BleepingComputer has reached out to the FBI and we are awaiting their response.




#### Tags:
[[watchlist]] [[no-fly]] [[Diachenko]] [[U.S.]] [[Bleeping Computer]]
