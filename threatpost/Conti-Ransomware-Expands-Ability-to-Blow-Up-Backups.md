# Conti Ransomware Expands Ability to Blow Up Backups
### The Conti ransomware gang has developed novel tactics to demolish backups, especially the Veeam recovery software. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175114)
+ Date: September 29, 2021  11:43 am
+ Author: Lisa Vaas


## Article:
Good at identifying and obliterating backups? Speak Russian? The notorious Conti ransomware [group](https://threatpost.com/affiliate-leaks-conti-ransomware-playbook/168442/) may find you a fine hiring prospect.


That’s according to a [report](https://www.advintel.io/post/backup-removal-solutions-from-conti-ransomware-with-love) published on Wednesday by cyber-risk prevention firm Advanced Intelligence, which details how Conti has honed its backup destruction to a fine art – all the better to find, crush and kill backed-up data. After all, backups are a major obstacle to encouraging ransomware payment.


A Conti Primer
--------------


Palo Alto Networks has [described the gang](https://unit42.paloaltonetworks.com/conti-ransomware-gang/) as a standout, and not in a good way: “It’s one of the most ruthless of the dozens of ransomware gangs that we follow,” the firm said. As of June, Conti had spent more than a year attacking organizations where IT outages can threaten lives: Hospitals, emergency number dispatch carriers, emergency medical services and law-enforcement agencies.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


An example: In May, Ireland’s department of health services was [still reeling](https://threatpost.com/conti-ransomware-fail-costly/166263/) a week after a Conti ransomware attack that wasn’t even all that successful. Officials said at the time that the attack would cost tens of millions of Euros to repair, even though the attackers didn’t manage to encrypt systems.


Its expertise in demolishing backups has helped Conti to rain down destruction. According to AdvIntel head of research Yelisey Boguslavskiy and CEO and chairman Vitali Kremez, Conti – a top-tier Russian-speaking ransomware group that specializes in [double extortion](https://threatpost.com/double-extortion-ransomware-attacks-spike/154818/) – bases its negotiation strategies on the premise that the majority of targets who pay the ransom are “motivated primarily by the need to restore their data.”


The two-slap whammy of double extortion entails both data encryption and the threat to publish that seized data, but according to AdvIntel’s collection of Conti ransomware samples, Conti views victims’ desire to avoid the publishing of their data as only a secondary goal – most particularly if those victims can rely on backups instead of having to pay.


“If the victim has the ability to restore the files via backups, the chances of successful ransom payment to Conti will be minimized, even despite the fact that the risk of data publishing persists,” the researchers wrote.


Conti’s Backup-Obliteration Methodology
---------------------------------------


AdvIntel has found that Conti builds its backup removal expertise from the ground up, starting at the “team development level.” Namely, when the ransomware-as-a-service (RaaS) gang recruits for workers to invade networks, they’re clear that their penetration-tester candidates need top-notch skills at finding and obliterating backups.


“While selecting network intruders for their divisions also known as ‘teams,’ Conti is particularly clear that experience related to backup identification, localization and deactivation is among their top priorities for a successful pentester,” according to AdvIntel’s analysis. “This backup focus implemented within the partnership-building process enables Conti to assemble teams, equipped with knowledge and skills aimed at backup removal.”


Veeam Vivisection
-----------------


Conti has focused most particularly on developing new ways to compromise backup software from disaster-recovery firm [Veeam](https://www.veeam.com/).


In one such campaign observed by AdvIntel in the past year, as is its wont, Conti used [Cobalt Strike beacon](https://threatpost.com/cobalt-strike-cybercrooks/167368/): The legitimate, commercially available tool used by network penetration testers and whose usage by crooks has gone mainstream in the world of crimeware.


Conti routinely initiates its attacks by installing the Cobalt Strike beacon backdoor via spam messages, then leverages another legitimate tool: The remote-management agent [Atera](https://www.advintel.io/post/secret-backdoor-behind-conti-ransomware-operation-introducing-atera-agent), which gives the gang persistence in an infected network. Conti also uses Ngrok, a cross-platform application that exposes local server ports to the internet, to establish a tunnel to the local host for data exfiltration.


Next, Conti operators find and impersonate a privileged backup user in order to grant themselves Veeam backup privileges.


The attackers typically use a weaponized Rclone – a command line program used to manage files on cloud storage – for data exfiltration of the Veeam backups. Finally, to ensure that the victim has been kneecapped and won’t be able to recover, the Conti attackers lock the victim’s system and manually remove the Veeam backups.


AdvIntel outlined the backup removal steps in the chart below:


“With the Veeam account compromise, Conti has a method to deal with backup software to ‘force’ ransom payment,” according to the firm’s writeup.


Veeam’s Response
----------------


Veeam responded to AdvIntel’s findings by saying that there’s not much the firm can do after the attackers have taken over a domain admin account. The company’s statement:



> “When the attackers have access to the domain admin account there is little [Veeam] can do to protect our installation. That’s why we usually recommend using a separate domain to run backup software, this could protect [a Veeam] instance in case … the primary domain is compromised. Another approach to protect from ransomware would be to use immutable repositories, [which] can be considered safe (if configured correctly), because they allow only appending new data, not altering/purging existing backups.” —Veeam statement.
> 
> 


How to Stop Conti’s Backup Destruction
--------------------------------------


AdvIntel offered these mitigations and recommendations to keep Conti backup removal attacks:


***Rule #1 of Linux Security:** No cybersecurity solution is viable if you don’t have the basics down. [**JOIN**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) Threatpost and Linux security pros at Uptycs for a LIVE roundtable on the [**4 Golden Rules of Linux Security**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar). Your top takeaway will be a Linux roadmap to getting the basics right! [**REGISTER NOW**](https://threatpost.com/webinars/4-golden-rules-linux-security/?utm_source=ART&utm_medium=ART&utm_campaign=September_Uptycs_Webinar) and join the **LIVE event on Sept. 29 at Noon EST**. Joining Threatpost is Uptycs’ Ben Montour and Rishi Kant who will spell out Linux security best practices and take your most pressing questions in real time.*




#### Tags:
[[Conti]] [[ransomware]] [[Veeam]] [[AdvIntel]] [[Linux]] [[AdvIntel’s]] [[backups.]] [[ThreatPost]]
