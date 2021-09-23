# A new APT is targeting hotels across the world
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/a-new-apt-is-targeting-hotels-across-the-world/)
+ Date: September 23, 2021
+ Author: Catalin Cimpanu


## Article:
![A new APT is targeting hotels across the world](https://therecord.media/wp-content/uploads/2021/09/hotel.jpg)

A new advanced persistent threat (APT), a term used to describe state-sponsored cyber-espionage groups, has been spotted mounting attacks against hotels across the world.


Codenamed **FamousSparrow**, this new APT was discovered by Slovak security firm ESET, which said it’s been tracking its attacks as far back as 2019.


“FamousSparrow’s victims are located in Europe (France, Lithuania, the UK), the Middle East (Israel, Saudi Arabia), the Americas (Brazil, Canada, Guatemala), Asia (Taiwan), and Africa (Burkina Faso),” the company said in a report shared with *The Record*.


Besides hotels, other attacks also hit governments, international organizations, engineering companies, and law firms.


“The targeting suggests that FamousSparrow’s intent is cyberespionage,” ESET researchers said today.


### Entering via unpatched web applications


Most of the attacks followed the same pattern, with the group using vulnerabilities in web applications as entry points into its victims’ networks. According to ESET, past attacks exploited security flaws in:


* Microsoft Exchange
* Microsoft SharePoint
* Oracle Opera (business software for hotel management)


Particularly interesting was also the fact that FamouseSparrow was one of the first APTs to mount attacks using the [ProxyLogon](https://therecord.media/tag/proxylogon/) vulnerability in Microsoft Exchange email servers.


ESET said the group weaponized ProxyLogon just one day after Microsoft disclosed the vulnerability’s existence, with the first attacks recorded on March 3, 2021/


Once FamousSparrow had a foothold inside a target network, ESET researchers said the attackers deployed a custom backdoor named SparrowDoor, which they used as a pivot point to orchestrate ways to move laterally inside a hacked organization using public tools like Mimikatz and Metasploit.


But while ESET noted that the FamousSparrow group used tools previously linked to espionage operations carried out by other groups such as [DRDControl [PDF]](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf) and [SparklingGoblin](https://www.welivesecurity.com/2021/08/24/sidewalk-may-be-as-dangerous-as-crosswalk/), researchers also said they aren’t ready just yet to attribute the group to any particular state.


### Hotels are often targeted for intelligence gathering


The group now joins the ranks of other APTs that have historically targeted hotels, such as the infamous [DarkHotel](https://www.kaspersky.com/resource-center/threats/darkhotel-malware-virus-threat-definition), [APT28](https://www.fireeye.com/blog/threat-research/2017/08/apt28-targets-hospitality-sector.html), and the [Rana Group](https://www.clearskysec.com/wp-content/uploads/2019/05/Iranian-Nation-State-APT-Leak-Analysis-and-Overview.pdf), which didn’t target hotels directly but hotel room booking systems.


The purpose of attacking and compromising hotels is simple, as it allows cyber-espionage groups to track the movement of persons of interest.


For the same reason, APTs often also target telcos and airline companies, seeking to gain insight, intercept targets, or track the movements of their targets.





#### Tags:
[[ESET]] [[Microsoft]] [[The Record]]
