# Official FBI email server hacked, used to send fake threat
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/official-fbi-email-server-hacked-used-to-send-fake-threat/)
+ Date: November 13, 2021
+ Author: Catalin Cimpanu


## Article:
![Official FBI email server hacked, used to send fake threat](https://therecord.media/wp-content/uploads/2021/05/FBI.jpg)

**A group of unidentified hackers have compromised one of the FBI’s email servers and have sent out a massive wave of spam emails containing a warning about a (fake) cyberattack that was allegedly taking place.**


The attack, which took place in the early hours of the US East Coast morning, impacted an email server that the FBI was using for some sort of public ticketing and alerting system, Carel Bitter, Chief Data Officer at Spamhaus, told *The Record* in an interview today.


Bitter, who was the [first to spot the attacks](https://twitter.com/spamhaus/status/1459450061696417792), said he notified the FBI as soon as his organization detected the attack, but, by that point, FBI employees were also aware of the incident.


The Spamhaus exec said FBI offices had been swamped with phone calls and emails from worried organizations that were seeking additional information about the supposed attack.


While the emails were obviously warning about a fake threat, they caused panic among some recipients because the messages passed SPF and DKIM security checks, meaning they were sent from the actual FBI servers and passed everyone’s spam filters.


### The Vinny Troia saga


However, while the emails passed cryptographic checks, the message they carried was obvious non-sense.


On top of numerous spelling mistakes that an organization like the FBI would never make in the text of a security alert, the messages were pretty blatantly trying to frame Vinny Troia, the founder of NightLion Security, as the perpetrator of a “sophisticated chain attack.”


In a copy of the email embedded below, the hackers tried to trick organizations into believing that the FBI had detected Troia trying to steal data from their networks.


![FBI-spam](https://www-therecord.recfut.com/wp-content/uploads/2021/11/FBI-spam.png)Image: Spamhaus

> **Urgent: Threat actor in systems**  
> Our intelligence monitoring indicates exfiltration of several of your virtualized clusters in a sophisticated chain attack. We tried to blackhole the transit nodes used by this advanced persistent threat actor, however there is a huge chance he will modify his attack with fastflux technologies, which he proxies trough multiple global accelerators. We identified the threat actor to be [REDACTED], whom is believed to be affiliated with the extortion gang TheDarkOverlord, We highly recommend you to check your systems and IDS monitoring. Beware this threat actor is currently working under inspection of the NCCIC, as we are dependent on some of his intelligence research we can not interfere physically within 4 hours, which could be enough time to cause severe damage to your infrastructure.
> 
> 


But all of this was a ruse, as Marcus Hutchins, a malware analyst from Kryptos Logic, [pointed out on Twitter today](https://twitter.com/MalwareTechBlog/status/1459577828790386688).


“Vinny Troia wrote a book revealing information about hacking group TheDarkOverlord,” Hutchins said.


“Shortly after, someone began [erasing ElasticSearch clusters](https://www.zdnet.com/article/a-hacker-has-wiped-defaced-more-than-15000-elasticsearch-servers/) leaving behind his name. Later his Twitter was hacked, [then his website](https://www.zdnet.com/article/hacker-breaches-security-firm-in-act-of-revenge/),” he added.


“Now a hacked FBI email server is sending this.”


### FBI confirms hack; takes down server


An FBI spokesperson [confirmed the hack](https://www.fbi.gov/news/pressrel/press-releases/fbi-statement-on-incident-involving-fake-emails) earlier today.


The agency said it was aware of the incident and investigating and that it had taken down the compromised server in the meantime to stop the spam.


Because the email server appears to have been used for some sort of automated emailing system, Bitter told *The Record* that he believed the hackers exploited some sort of vulnerability in software running on the server to send these messages; however, this was just a theory based on the currently available information.


As for the size of the attack, Bitter said the attackers appear to have used databases of public email addresses to send out the spam emails.


Possible sources appear to the American Registry for Internet Numbers ([ARIN](https://www.arin.net/)) database, which holds emails that were used to register web domains across North America, which can be easily scraped and compiled by any threat actor, although there are signs that other sources were also used.








#### Tags:
[[emails]] [[attack,]] [[today.]] [[Troia]] [[The Record]]
