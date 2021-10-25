# BlackMatter ransomware victims quietly helped using secret decryptor
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/blackmatter-ransomware-victims-quietly-helped-using-secret-decryptor/)
+ Date: October 24, 2021
+ Author: Lawrence Abrams


## Article:
![BlackMatter ransomware](https://www.bleepstatic.com/content/hl-images/2021/07/30/BlackMatter-ransomware.jpg)


Cybersecurity firm Emsisoft has been secretly decrypting BlackMatter ransomware victims since this summer, saving victims millions of dollars.


Emsisoft and its CTO [Fabian Wosar](https://twitter.com/fwosar) have been helping ransomware victims recover their files since 2012, when an operation called [ACCDFISA was launched](https://www.bleepingcomputer.com/forums/t/449398/new-ransomware-called-anti-child-porn-spam-protection-or-accdfisa/?p=2659443) as the first modern ransomware.






Since then Wosar and others have been working tirelessly to find flaws in ransomware's encryption algorithms that allow decryptors to be made.


However, to prevent ransomware gangs from fixing these flaws, [Emsisoft](https://www.emsisoft.com/en/) quietly works with trusted partners in law enforcement and incident response to share the news of these decryptors rather than making them publicly available.


A secret BlackMatter decryptor
------------------------------


Soon after the BlackMatter ransomware operation launched, Emsisoft discovered a flaw allowing them to create a decryptor recover victim's files without paying a ransom.


Emsisoft immediately alerted law enforcement, ransomware negotiations firms, incident response firms, CERTS worldwide, and trusted partners with information about the decryptor.


This allowed these trusted parties to refer BlackMatter victims to Emsisoft to recover their files rather than pay a ransom.


"Since then, we have been busy helping BlackMatter victims recover their data. With the help of law enforcement agencies, CERTs and private sector partners in multiple countries, we were able to reach numerous victims, helping them avoid tens of millions of dollars in demands," explains Wosar in a [blog post](https://blog.emsisoft.com/en/39181/on-the-matter-of-blackmatter/) about the BlackMatter decryptor.


Other than referrals, Emsisoft was also contacting victims found through BlackMatter samples and ransom notes publicly uploaded to various sites.


When a BlackMatter samples becomes public, it was possible to extract the ransom note and gain access to the negotiations between the victim and the ransomware gang. After identifying the victim, Emsisoft would privately contact them about the decryptor so they they did not have to pay the ransom.


If Emsisoft could find the ransomware samples and notes, though, other people could as well and have used them to hijack negotiation chats or shared images of the chats on Twitter.


This ultimately led to BlackMatter locking down their negotiation site so that only the victims could gain access, making it impossible for researchers to find victims this way.


 "We have been fighting ransomware for more than ten years, so we understand the frustration the infosec community feels towards ransomware threat actors better than anyone," shared Wosar.


"However, as cathartic as throwing expletives might have felt, it resulted in BlackMatter locking down their platform, and locking us and everyone else out in the process."



![New BlackMatter victim verification system](https://www.bleepstatic.com/images/news/ransomware/b/blackmatter/decryptor/blackmatter-payment-site-verification.jpg)**New BlackMatter victim verification system**
 As victims started refusing to pay, BlackMatter grew increasingly suspicious and angry with ransomware negotiators.


One incident responder and negotiator, told BleepingComputer they began receiving death threats from BlackMatter after none of the victims in an attack paid a ransom.


All good things must come to an end
-----------------------------------


Unfortunately, BlackMatter learned of the decryptor at the end of September and was able to fix the bugs allowing Emsisoft to decrypt victims' files.


"One of the ways BlackMatter may have become aware of the existence of the flaw is by monitoring networks and company communications post breach. It is why we always recommend victims to switch to a secure communications channel, like a dedicated Signal group for example, as well as ensure none of the compromised network is involved in the general recovery processes," Wosar told BleepingComputer.


For those victims who were encrypted before the end of September, Emsisoft can still help through their [ransomware recovery service](https://www.emsisoft.com/en/ransomware-recovery-services/).


Wosar told us that they try to handle as many cases for free, with home users, non-profits, and enterprise victims involved in the global pandemic response receiving free support.



> 
> "Unlike most of the industry, we don't charge per hour but operate on a fixed price basis. The exact fee is usually in the mid 4 figures, but may depend on the exact circumstances. If a victim can't afford to pay us, we generally waive the fee or come to an alternative arrangement. Ultimately, the fee is not designed to make us rich." - Fabian Wosar.
> 
> 
> 


Victims encrypted by BlackMatter after the bug was fixed can no longer be helped but Emsisoft suggests you still contact them to see if there is anything they can learn from newer samples.


Emsisoft has also found vulnerabilities in approximately a dozen active ransomware operations, which can be used to recover victims' encrypted data without a ransom payment.


Emsisoft advises victims to contact law enforcement to report attacks, who can collect valuable indicators of compromise for investigative purposes and refer victims to Emsisoft if a decryptor is available


DarkSide: The precursor to BlackMatter
--------------------------------------


BlackMatter burst into action this summer soon after another notorious ransomware gang known as DarkSide shut down their operation.


The DarkSide gang was a highly technical ransomware operation that [launched in August 2020](https://www.bleepingcomputer.com/news/security/darkside-new-targeted-ransomware-demands-million-dollar-ransoms/) and was known for numerous attacks against organizations worldwide.


However, their [attack on Colonial Pipeline](https://www.bleepingcomputer.com/news/security/largest-us-pipeline-shuts-down-operations-after-ransomware-attack/), the largest fuel pipeline in the United States, brought the [full attention of the US government](https://www.bleepingcomputer.com/news/security/fbi-revil-cybergang-behind-the-jbs-ransomware-attack/) to bear on the gang. This led to their servers being seized and the [US government recovering $4 million](https://www.bleepingcomputer.com/news/security/us-recovers-most-of-colonial-pipelines-44m-ransomware-payment/) of the Colonial Pipeline ransom payment.


![Hacker forum post about seized DarkSide servers and cryptocurrency](https://www.bleepstatic.com/images/news/ransomware/d/darkside/seizure/forum-post.jpg)**Hacker forum post about seized DarkSide servers and cryptocurrency** 
Realizing that they bit off more than they could chew, [DarkSide quickly shut down their operation](https://www.bleepingcomputer.com/news/security/darkside-ransomware-servers-reportedly-seized-operation-shuts-down/) and fled back into the shadows.


However, whether it's greed or the need to be under the spotlight, ransomware gangs always tend to come back under new names.


Such is the case with [DarkSide who returned as BlackMatter](https://www.bleepingcomputer.com/news/security/darkside-ransomware-gang-returns-as-new-blackmatter-operation/) in July.




#### Tags:
[[BlackMatter]] [[ransomware]] [[Emsisoft]] [[Wosar]] [[decryptor]] [[DarkSide]] [[ransom.]] [[However,]] [[Bleeping Computer]]
