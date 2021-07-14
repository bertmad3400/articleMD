# China’s Great Firewall is blocking around 311k domains, 41k by accident
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/chinas-great-firewall-is-blocking-around-311k-domains-41k-by-accident/)
+ Date: July 11, 2021
+ Author: Catalin Cimpanu


## Article:
![China’s Great Firewall is blocking around 311k domains, 41k by accident](https://therecord.media/wp-content/uploads/2021/07/China-map.png)

* Academics tested 534 million domains during a nine-month period between April and December 2020.
* They found that the Chinese Great Firewall blocks 311,000 domains.
* Most of the blocked sites are newly registered domains, followed by sites hosting business and pornographic content.


**In the largest study of its kind, a team of academics from four US and Canadian universities said they were able to determine the size of China’s Great Firewall internet censorship capabilities.**


In a research project that lasted nine months, from April to December 2020, academics developed a system called **GFWatch**that accessed domains from inside and outside China’s internet space and then measured how the Great Firewall (GFW) would tamper with the connection at the DNS level in order to prevent Chinese users from accessing a domain, or an external entity accessing Chinese internal sites.


![GFW-poisoning](https://www-therecord.recfut.com/wp-content/uploads/2021/07/GFW-poisoning.png)
Using GFWatch, researchers said they tested 534 million distinct domains, accessing around 411 million domains on a daily basis in order to record and then verify that the blocks were persistent.


After nine months of compiling data, they found that China’s Great Firewall currently blocks around 311,000 domains, with 270,000 blocks working as intended, while 41,000 domains appear to have been blocked by accident.


The research team said these latter domains appear to have been blocked accidentally when Chinese authorities tried to block a shorter domain and used a broad DNS filtering regular expression (regex) that did not account for situations where that shorter domain was also part of a longer domain name, indirectly banning other sites.


For example, researchers said that when Chinese authorities blocked access to reddit.com, they also accidentally blocked access to booksreddit.com, geareddit.com, and 1,087 other sites.


![GFW-overblocked-strings](https://www-therecord.recfut.com/wp-content/uploads/2021/07/GFW-overblocked-strings.png)
The research team also used the list of 311,000 blocked domains to determine what type of content Chinese authorities usually block.


Using domain categorization services like FortiGuard, researchers said that around 40% of the blocked sites were newly registered domains and which Chinese authorities decided to block by default until they could categorize and whitelist their content.


However, when removing these results, the research team said that the most blocked domains usually hosted business-related content, followed by domains hosting pornography, and then domains dedicated to information technology (IT).


Other types of blocked domains included sites hosting tools to avoid the Great Firewall blocks, gambling sites, personal blogs, entertainment sites, news and media sites, and domains hosting malicious/malware content.


![GFW-blocked-list](https://www-therecord.recfut.com/wp-content/uploads/2021/07/GFW-blocked-list.png)
Furthermore, as the project took place and the coronavirus pandemic grew in intensity last year, researchers also spotted COVID-19-related domains being added to the GFW filtering rules in real time.


This included blocks for domains like covid19classaction.it, covid19song.info, covidcon.org, ccpcoronavirus.com, covidhaber.net, and covid-19truth.info, with some of the sites being dedicated to blaming the coronavirus pandemic on the Chinese state.


### Around 1,800 popular domains blocked by the Great Firewall


“We find that most domains blocked by the GFW are unpopular and do not appear on lists of most popular websites,” researchers said.


Of a sample of 138,700 domains, academics said that only 1.3% (~1,800) sites are among the top 100,000 most popular sites on the internet (according to the Tranco ranking).


In addition, using GFWatch, the researchers said they also spotted cases where China’s DNS-based blocks—which usually involve altering DNS records returned to Chinese users—have also accidentally polluted DNS records outside China’s internet space, inside the networks of several DNS providers, for at least 77,000 sites.


Additional details about the study and its results can be found in a research paper titled “*[How Great is the Great Firewall? Measuring China’s DNS Censorship](https://arxiv.org/abs/2106.02167),*” authored by academics from Stony Brook University, the University of Massachusetts, University of California, Berkeley, and the Citizen Lab at the University of Toronto, in Canada.





#### Tags:
[[000]] [[DNS]] [[GFWatch]] [[GFW]] [[The Record]]
