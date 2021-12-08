# Malicious npm packages caught stealing Discord tokens, environment variables
### The Node Package Manager (npm) security team has removed 17 JavaScript libraries this week that contained malicious code to collect and steal Discord access tokens and environment variables from users' computers.

## Information:
+ Source: The Record
+ Link: https://therecord.media/malicious-npm-packages-caught-stealing-discord-tokens-environment-variables/
+ Date: 2021-12-08T22:09:49+00:00
+ Author: Catalin Cimpanu


## Article:
![Article Image](https://therecord.media/wp-content/uploads/2021/12/npm-computer.png)

The Node Package Manager (npm) security team has removed 17 JavaScript libraries this week that contained malicious code to collect and steal Discord access tokens and environment variables from users’ computers.


“Luckily, these packages were removed before they could rack up a large number of downloads (based on npm records) so we managed to avoid a scenario similar to [our last PyPI disclosure](https://therecord.media/malicious-python-packages-caught-stealing-discord-tokens-installing-shells/), where the malicious packages were downloaded tens of thousands of times before they were detected and removed,” [said](https://jfrog.com/blog/malicious-npm-packages-are-after-your-discord-tokens-17-new-packages-disclosed/) Andrey Polkovnychenko and Shachar Menashe, two security researchers at DevOps security firm JFrog, and the ones who spotted and reported the malicious packages to the npm team.


Polkovnychenko and Menasche said that if a developer had downloaded and installed any of these libraries, they would have executed malicious code on their systems that either installed malware or collected data to send back to the attackers.


Four of the npm JavaScript libraries contained functions to collect Discord access tokens, which effectively act as authentication cookies and can allow attackers to hijack an infected developer’s Discord account.


A fifth npm package contained a copy of [PirateStealer](https://github.com/Stanley-GF/PirateStealer), a piece of malware that could also extract other data from Discord apps and accounts, such as payment card details, login credentials, and personal information.


Another set of eleven libraries included functions that collected environment variables, which are details from a developer’s local programming environment. These variables normally store user and OS information, but in some cases, they can also contain API keys and login credentials, something that an attacker would definitely be interested in collecting.


And last but not least, a 17th package also downloaded and installed a full-blown remote access trojan that granted the threat actor full control over a developer’s computer.




| **Package** | **Version** | **Payload** | **Infection Method** |
| prerequests-xcode | 1.0.4 | Remote Access Trojan (RAT) | Unknown |
| discord-selfbot-v14 | 12.0.3 | Discord token grabber | Typosquatting/Trojan |
| discord-lofy | 11.5.1 | Discord token grabber | Typosquatting/Trojan |
| discordsystem | 11.5.1 | Discord token grabber | Typosquatting/Trojan |
| discord-vilao | 1.0.0 | Discord token grabber | Typosquatting/Trojan |
| fix-error | 1.0.0 | PirateStealer (Discord malware) | Trojan |
| wafer-bind | 1.1.2 | Environment variable stealer | Typosquatting |
| wafer-autocomplete | 1.25.0 | Environment variable stealer | Typosquatting |
| wafer-beacon | 1.3.3 | Environment variable stealer | Typosquatting |
| wafer-caas | 1.14.20 | Environment variable stealer | Typosquatting |
| wafer-toggle | 1.15.4 | Environment variable stealer | Typosquatting |
| wafer-geolocation | 1.2.10 | Environment variable stealer | Typosquatting |
| wafer-image | 1.2.2 | Environment variable stealer | Typosquatting |
| wafer-form | 1.30.1 | Environment variable stealer | Typosquatting (wafer-*) |
| wafer-lightbox | 1.5.4 | Environment variable stealer | Typosquatting (wafer-*) |
| octavius-public | 1.836.609 | Environment variable stealer | Typosquatting (octavius) |
| mrg-message-broker | 9998.987.376 | Environment variable stealer | Dependency confusion |


However, while JFrog deserves credit for its recent discovery, the incident is not an isolated incident. This year, both JFrog and fellow DevOps security firm Sonatype have found tens of malicious libraries uploaded on both the npm (JavaScript) and PyPI (Python) package repositories, and all signs point to some sort of process automation in the creation of these malicious packages at scale.


There could be a lot to comment about how both npm and PyPI are to blame for this situation and for the wave of malicious libraries that are constantly being found on their platforms.


Neither service manually reviews package uploads, which has practically left the door open and invited such threat actors on their platforms.


However, we’d only sound like a broken record in the same ol’ discussion that many security researchers have had on this topic for years, all of which have led to no change to how the two package repositories handle package submissions.


Instead, a clear trend this year is the sheer number of malicious npm and PyPI packages that have targeted the theft of Discord tokens.


As Polkovnychenko and Menasche point out, this could be explained by the increasing number of malware operations that use Discord accounts to host their payloads or collect information from their victims, in a trend also spotted by [RiskIQ](https://www.riskiq.com/blog/external-threat-management/discord-cdn-abuse-malware/), [Check Point](https://blog.checkpoint.com/2021/10/21/using-discord-infrastructure-for-malicious-intent/), [Sophos](https://news.sophos.com/en-us/2021/07/22/malware-increasingly-targets-discord-for-abuse/), and [Zscaler](https://www.zscaler.com/blogs/security-research/discord-cdn-popular-choice-hosting-malicious-payloads).


Since malware authors wouldn’t want to create these accounts themselves, it makes sense to hijack or buy access to legitimate accounts for their operations.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Npm]] [[Pypi]] [[Malware]] [[Polkovnychenko]] [[Jfrog]] [[Stealertyposquatting]] [[The Record]]

