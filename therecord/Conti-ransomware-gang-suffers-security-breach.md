# Conti ransomware gang suffers security breach
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/conti-ransomware-gang-suffers-security-breach/)
+ Date: November 20, 2021
+ Author: Catalin Cimpanu


## Article:
![Conti ransomware gang suffers security breach](https://therecord.media/wp-content/uploads/2021/11/Conti-1.png)

The Conti ransomware group has suffered an embarrassing data breach after a security firm was able to identify the real IP address of one of its most sensitive servers and then gain console access to the affected system for more than a month.


The exposed server, called a **payment portal** or **recovery site**, is where the Conti gang tells victims to visit in order to negotiate ransom payments.


“Our team detected a vulnerability in the recovery servers that Conti uses, and leveraged that vulnerability to discover the real IP addresses of the hidden service hosting the group’s recovery website,” Swiss security firm Prodaft said in a [37-page report](https://www.prodaft.com/resource/detail/conti-ransomware-group-depth-analysis) published on Thursday, identifying the server as hosted on **217.12.204.135**, an IP address owned by Ukrainian web hosting company ITL LLC.


#### Prodaft exposes Conti IP address & server password


In addition, Prodaft said its researchers maintained access to the server for weeks, during which time they monitored network traffic for IP addresses that connected to the server.


While some connections belonged to victims and their negotiators, Prodaft also monitored SSH connections, which most likely belong to the Conti gang itself.


However, luck wasn’t on the researchers’ side, as all SSH IP addresses belonged to Tor exit nodes, meaning they couldn’t be used to identify Conti operators.


Other pieces of valuable information shared in the Prodaft report also included details about the Conti server OS and its **htpasswd**file that contained a hashed version of the server password.


![Prodaft-Conti-findings](https://www-therecord.recfut.com/wp-content/uploads/2021/11/Prodaft-Conti-findings.png)Image: Prodaft
#### IP exposure causes Conti to scramble for new host


Once published, the report didn’t go unnoticed with the Conti gang, and especially the parts about the breach of its payment portal, the IP leak, and the sharing of their server’s hashed password—details that opened the gang to having its server hijacked by rival ransomware groups.


In a conversation on Thursday night, hours after Prodaft’s findings went live, security researcher MalwareHunterTeam told *The Record* that the Conti gang had taken its payment portal offline.



> So, while both the clearweb and Tor domains of the leak site of the Conti ransomware gang is online and working, both their clearweb and Tor domains for the payment site (which is obviously more important than the leak) is down, possible from some hours ago already…  
> 👀  
> 🤔 [pic.twitter.com/hmzR463tFP](https://t.co/hmzR463tFP)
> 
> — MalwareHunterTeam (@malwrhunterteam) [November 18, 2021](https://twitter.com/malwrhunterteam/status/1461453624429719557?ref_src=twsrc%5Etfw)

 
By Friday, the researcher said that the sudden downtime was preventing all recent Conti victims from negotiating and paying ransoms, extending those downtimes at companies around the world.


MalwareHunterTeam, who has been tracking ransomware gangs since the mid-2010s, described the sudden downtime as uncharacteristic for a ransomware group that generally had a more stable and professionally run infrastructure.


However, the Conti payment portal did eventually come back online Friday night, more than 24h after it was first taken down.


“Looks like Europeans have also decided to abandon their manners and go full-gansta simply trying to break our systems,” the Conti gang said in an insult-filled statement posted on their blog, effectively confirming Prodaft’s findings and their own security breach, in a message that was also meant to reassure its affiliates that their infrastructure was safe again.




> [#Conti](https://twitter.com/hashtag/Conti?src=hash&ref_src=twsrc%5Etfw) [#Ransomware](https://twitter.com/hashtag/Ransomware?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/cWfGfRHd2b](https://t.co/cWfGfRHd2b)
> 
> — 𝕯𝖒𝖎𝖙𝖗𝖞 𝕾𝖒𝖎𝖑𝖞𝖆𝖓𝖊𝖙𝖘 (@ddd1ms) [November 19, 2021](https://twitter.com/ddd1ms/status/1461813586154635268?ref_src=twsrc%5Etfw)



Prodaft said that it shared all its findings with law enforcement “for further legal action against the Conti group and its affiliates.”


However, such findings are typically kept private as much as possible in order to give law enforcement time to take action against cybercrime groups, operations that usually take months.


After its report was published this week, Prodaft was criticized by several security researchers for sharing this sensitive information publicly, which eventually led to the Conti group fortifying its server security.


In fact, one of the reasons why the Conti gang intervened to move and secure its payment portal so quickly is also related to the fact it was hosted in Ukraine, a country that has recently collaborated with Europol and US agencies to arrest ransomware affiliates for the [Clop](https://therecord.media/ukrainian-police-arrest-clop-ransomware-members-seize-server-infrastructure/), [REvil](https://therecord.media/us-arrests-and-charges-ukrainian-man-for-kaseya-ransomware-attack/), and [LockerGoga](https://therecord.media/europol-detains-suspects-behind-lockergoga-megacortex-and-dharma-ransomware-attacks/) gangs.


As a side note, the Conti gang also countered Prodaft’s claims that they’ve [earned $25.5 million from ransom payments since July 2021](https://therecord.media/conti-gang-has-made-at-least-25-5-million-since-july-2021/). Conti operators said that the real number was $300 million, although this is most likely an empty boast, which ransomware gangs often use to promote themselves and the profitability of their attacks.





#### Tags:
[[Conti]] [[IP]] [[Prodaft]] [[ransomware]] [[However,]] [[Prodaft’s]] [[The Record]]
