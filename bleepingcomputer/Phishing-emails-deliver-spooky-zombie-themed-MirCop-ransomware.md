# Phishing emails deliver spooky zombie-themed MirCop ransomware
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/phishing-emails-deliver-spooky-zombie-themed-mircop-ransomware/)
+ Date: November 4, 2021
+ Author: Bill Toulas


## Article:
![zombies](https://www.bleepstatic.com/content/hl-images/2021/11/04/zombies.jpg?rand=1216207391)


A new phishing campaign pretending to be supply lists infects users with the MirCop ransomware that encrypts a target system in under fifteen minutes.


The actors begin the attack by sending an unsolicited email to the victim, supposedly following up on a previous arrangement about an order.


The email body contains a hyperlink to a Google Drive URL, which, if clicked, downloads an MHT file (webpage archive) onto the victim’s machine.


Google Drive serves to introduce legitimacy to the email and aligns very well with common day-to-day business practices.


For threat actors, simple but key choices like this can distinguish between the victim clicking the URL or sending the email to the spam folder.


Those who open the file can only see a blurred image of what is supposedly a supplier list, stamped and signed for an extra touch of legitimacy.



![Blurred image of suppliers list](https://www.bleepstatic.com/images/news/u/1220909/ransomware/blurred.png)**Blurred image of suppliers list**
When the MHT file iis opened, it will download a RAR archive containing a .NET malware downloader from “hXXps://a[.]pomf[.]cat/gectpe.rar”.


The RAR archive contains an EXE file, which uses VBS scripts to drop and execute the MirCop payload onto the infected system.


The ransomware activates immediately and starts taking screenshots, locks files, changes the background to a horrid zombie-themed image, and offers victims instructions on what to do next.



![Gory image background with instructions](https://www.bleepstatic.com/images/news/u/1220909/ransomware/wallpaper.png)**Gory image background with instructions**  
*Source: Cofense*
According to [Cofense](https://cofense.com/blog/spooky-ransomware-past-segs/), this whole process takes less than 15 minutes from the moment the victim opens the phishing email.


After that, the user is only allowed to open specific web browsers to communicate with the actors and arrange the payment of the ransom.


The actors are not interested in sneaking into the victim’s machine stealthily or staying there for long to conduct cyber-espionage or steal files for extortion.


On the contrary, the attack unfolds rapidly, and the source of trouble becomes quickly evident to the victim


An old but still dangerous strain
---------------------------------


MicroCop is an old ransomware strain that used to deliver absurd ransom demands onto its victims.


That was until Michael Gillespie cracked its encryption and [released a working decryptor for free](https://www.bleepingcomputer.com/news/security/decrypted-microcop-ransomware-demands-48-bitcoins-to-get-your-files-back/).


We were unable to test if that old decryptor works with the payloads dropped in the most recent campaign, but it’s possible that it can still unlock the files.


Cofense says the same variant has been in circulation since June this year, so MicroCop is still out there, and people need to be cautious with handling unsolicited emails. 




#### Tags:
[[ransomware]] [[Bleeping Computer]]
