# APT groups from China, Russia, and India adopt novel attack technique
### State-sponsored hacking groups, also known as advanced persistent threats (APTs), have adopted this year a new attack technique called RTF Template Injection, which has brought a new twist and made their attacks harder to detect and stop.

## Information:
+ Source: The Record
+ Link: https://therecord.media/apt-groups-from-china-russia-and-india-adopt-novel-attack-technique/
+ Date: 2021-12-01T10:02:44+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2021/12/RTF-template-injection.png)

State-sponsored hacking groups, also known as advanced persistent threats (APTs), have adopted this year a new attack technique called “RTF Template Injection,” which has brought a new twist and made their attacks harder to detect and stop.


In a [report](https://www.proofpoint.com/us/blog/threat-insight/injection-new-black-novel-rtf-template-inject-technique-poised-widespread) today, email security firm Proofpoint said that APTs from China, Russia, and India are already exploiting this technique, which they also expect to see adopted by financially-motivated threat actors as well.


### What is RTF Template Injection?


Called **RTF Template Injection**, this attack isn’t new per-se, but a variation of a [classic template injection attack](https://attack.mitre.org/techniques/T1221/) that has been known for years, hence its inclusion in the MITRE ATT&CK framework already.


The technique revolves around a Microsoft Office feature where users can create a document using a pre-defined template. These templates can be stored locally or downloaded from a remote server for attacks known as “[remote template injections](https://blog.sunggwanchoi.com/remote-template-injection/).”


The idea is that attackers can send malicious Office files—such as DOC, XLS, or PPT—to victims that are benign but then load malicious code via the template feature when the Office app needs to render the content.


Attacks abusing template injections have been taking place for years but saw a surge in 2020, when “remote template injection” became a popular technique with some APT groups.


But these attacks all exploited Office files, and especially Word documents. The new variation of this attack is that, instead of using Word or other Office files, Proofpoint says that threat actors have now started launching attacks with classic [Windows RTF](https://en.wikipedia.org/wiki/Rich_Text_Format) (rich text format) files, which also support the ability to arrange their content using a template stored on a remote URL.


According to Proofpoint, threat actors are putting together RTF files with lures that may interest their targets, are crafting a template that contains malicious code that runs malware, and are editing the RTF files to load the template when the file is opened. These documents are then sent to victims using email spear-phishing attacks, hoping that victims open the documents.


Although users must click a button that says “*Enable Editing*” or “*Enable Content*,” which is a known security warning and blocks the automatic execution of the template’s malicious code, this feature hasn’t been efficient at blocking Office attacks in years, as most users can be tricked into clicking the buttons with some clever document designs.


### APTs using this technique: TA423, Gamaredon, and DoNoT


As for who’s using this technique, Proofpoint has identified three state-sponsored groups, such as **TA423**(China), **Gamaredon**(Russia), and **DoNoT**(India).


The first to use this technique were DoNot and TA423, which began using RTF documents with malicious templates as early as March this year, when DoNoT registered its first domains, before launching the first attacks a month later.


![RTF-template-injection-attacks-timeline](https://therecord.media/wp-content/uploads/2021/12/RTF-template-injection-attacks-timeline-1024x506.png)Image: Proofpoint
Subsequent DoNoT attacks using RTF Template Injection attacks were seen through July, while TA423 attacks were seen as recently as late September when the group targeted Malaysian energy companies connected to deep-water energy exploration. 


Gamaredon, a group that was recently exposed by Ukraine as being [controlled by the Russian FSB intelligence service](https://therecord.media/ukraine-discloses-identity-of-gamaredon-members-links-it-to-russias-fsb/), is the most recent APT to adopt this technique, most notably in an October campaign that used RTF files crafted to look like Ukrainian governmental files.


Concluding its report on this new technique, Proofpoint believes that the effectiveness of Office remote template injection attacks in recent years suggests that RTF remote template injection attacks are also here to stay.


“While this method currently is used by a limited number of APT actors with a range of sophistication, the technique’s effectiveness combined with its ease of use is likely to drive its adoption further across the threat landscape,” Proofpoint researchers said, suggesting that besides other APT groups, financially-motivated threat actors, such as botnet and ransomware groups may also abuse it as well.


“This well-established trickle-down pattern may be accelerated in this case based on the minimal effort needed to weaponize RTF attachments before deploying in active phishing campaigns,” Proofpoint’s Michael Raggi said.





## Tags:

#### Threatactor:
[[threatactor.name=Gamaredon Group]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=India]] [[victim.continent.name=Asia]] [[victim.country.name=Malaysia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Asia]] [[victim.country.name=Russia]] [[victim.continent.name=Europe]] [[victim.country.name=Ukraine]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Rtf]] [[Proofpoint]] [[Ta423]] [[Donot]] [[Gamaredon]] [[The Record]]

