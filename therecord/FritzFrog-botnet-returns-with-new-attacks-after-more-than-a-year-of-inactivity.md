# FritzFrog botnet returns with new attacks after more than a year of inactivity
### After causing havoc throughout 2020, the operators of the FritzFrog botnet have returned with new attacks in 2022 after ceasing any activity last year.

## Information:
+ Source: The Record
+ Link: https://therecord.media/fritzfrog-botnet-returns-with-new-attacks-after-more-than-a-year-of-inactivity/
+ Date: 2022-02-10T14:00:41+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2022/02/FritzFrog.png)

After causing havoc throughout 2020, the operators of the FritzFrog botnet have returned with new attacks in 2022 after ceasing any activity last year.


First spotted in January 2020, the FritzFrog botnet operated by using SSH brute-force attacks to gain access to remote servers and deploy cryptominers.


Its attacks compromised more than 500 servers, Guardicore (now part of Akamai) [reported at the time](https://www.guardicore.com/labs/fritzfrog-a-new-generation-of-peer-to-peer-botnets/), including servers belonging to banks, universities, medical centers, and telecom companies.


But activity from the botnet generally stopped towards the end of the year for unknown reasons.


In a new report today, Akamai said that FritzFrog is now back in full swing, with improved code and launching attacks far more intense than it did back in 2020.


The botnet still relies on SSH brute-force attacks to infect new systems and still uses a peer-to-peer (P2P) architecture to control infected hosts, but some improvements were also made, such as:


* adding support for a Tor proxy network to mask brute-force attacks;
* the use of the SCP protocol to copy itself to breached systems;
* the incorporation of a blocklist system to exclude certain servers from being infected;
* and, code additions to prepare the botnet to attack WordPress sites.


Just like before, once servers are infected, the attackers will use the access to mine the Monero cryptocurrency.


Akamai said its systems are currently seeing around 500 FritzFrog-related incidents per day and that the botnet has already infected more than 1,500 systems.


“These were server machines belonging to organizations of various sizes and sectors, including healthcare, higher education, and government. We found infected machines in a European television channel network, a Russian manufacturer of healthcare equipment, and multiple universities in East Asia,” the company said today.


Approximately 37% of infected nodes were located in China, Akamai added, but victims were also spread out all over the world, with a spread suggesting random targeting.


Based on other clues researchers found, they currently believe the FritzFrog operator may be located in China or is trying to masquerade as someone living in China.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Miner-C]] [[action.malware.name=Net]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Finance]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Information]]

#### Location:
[[victim.continent.name=Asia]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.continent.name=Europe]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Botnet]] [[Fritzfrog]] [[Brute-force]] [[The Record]]

