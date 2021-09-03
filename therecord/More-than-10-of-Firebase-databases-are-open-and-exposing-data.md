# More than 10% of Firebase databases are open and exposing data
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/more-than-10-of-firebase-databases-are-open-and-exposing-data/)
+ Date: September 3, 2021
+ Author: Catalin Cimpanu


## Article:
![More than 10% of Firebase databases are open and exposing data](https://therecord.media/wp-content/uploads/2021/09/Firebase.png)

After years and years of warnings not to leave crucial databases exposed online without authentication, it appears that many Firebase administrators have failed to understand the dangers of these practices, and sensitive user data can still be easily found online with a few basic scripts or search queries.


In a research project conducted in July 2021 and published this week on Wednesday, cybersecurity firm Avast said it found [nearly 19,300 Firebase databases](https://decoded.avast.io/vladimirmartyanov/research-shows-over-10-of-sampled-firebase-instances-open/) from a grand total of 180,300 that were left exposed online without authentication.


“10.7% of the tested DBs were open, exposing the data to unauthenticated users, due to misconfiguration by the app developers,” said Avast security researcher [Vladimir Martyanov](https://twitter.com/ffb7d579).



> “This is quite a large percentage.”
> 
> Vladimir Martyanov, Avast security researcher


Developed in 2012 as a real-time database specifically built to be used as the backend of modern websites and mobile apps, Firebase is one of [today’s most popular database engines](https://db-engines.com/en/ranking).


Acquired by Google in 2014, Firebase is available as a cloud-hosted data storage system, with most databases hosted on a firebaseio.com subdomain.


Over the years, Firebase has become the go-to database for most Android and iOS applications, primarily due to its ability to handle huge data loads in almost near real-time.


However, ever since its earliest days, security researchers have found that many app developers have been having a hard time configuring their systems, which would often leave user data exposed online and accessible to anyone.


A [2018 study](https://www.techmeme.com/180629/p2#a180629p2) found 3,046 apps (2,446 Android and 600 iOS) mobile applications were exposing over 113 GBs of data via over 2,271 misconfigured Firebase databases.


[Two years later](https://www.comparitech.com/blog/information-security/firebase-misconfiguration-report/), as Firebase’s popularity grew, a subsequent study found more than 24,000 Android applications exposing user data through their Firebase backends, showing that despite warnings, developers were still not taking security seriously enough.


Furthermore, since most databases are hosted on the firebaseio.com domain, databases that didn’t require a password were also often [indexed by search engines](http://ghostlulz.com/google-exposed-firebase-database/), allowing anyone to find these systems with simple queries. While Google intervened to filter its search results, other search engines are still surfacing Firebase backends, even today, data that is regularly farmed by underground data brokers.


For its part, Google introduced [advanced authentication features](https://firebase.google.com/docs/database/security) in 2016; however, as Martyanov’s research shows, there are still 19,300 Firebase backends still exposed online.








#### Tags:
[[Google]] [[Android]] [[The Record]]
