# Multiple governments involved in coordinated takedown of REvil ransomware group: Reuters
### After widespread speculation, US officials reportedly worked with the private sectors and other unnamed countries to disrupt REvil's operation.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/multiple-governments-involved-in-coordinated-takedown-of-revil-ransomware-group-reuters/)
+ Date: October 21, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Cybersecurity experts [have told Reuters](https://www.reuters.com/technology/exclusive-governments-turn-tables-ransomware-gang-revil-by-pushing-it-offline-2021-10-21/) that law enforcement officials from multiple countries were involved in the disruption of the REvil ransomware gang, which [went dark for the second time on Sunday](https://www.zdnet.com/article/revil-ransomware-operators-claim-group-is-ending-activity-again-happy-blog-now-offline/).

Rumors and questions about the group's most recent disappearance dominated conversation this week after Recorded Future security expert Dmitry Smilyanets [shared multiple messages on Twitter](https://twitter.com/ddd1ms/status/1449734801016119299) from '0\_neday' -- a known REvil operator -- discussing what happened on the cybercriminal forum XSS. He claimed someone took control of the group's Tor payment portal and data leak website.

In the messages, 0\_neday explains that he and "Unknown" -- a leading representative of the group -- were the only two members of the gang who had REvil's domain keys. "Unknown" disappeared in July, leaving the other members of the group to assume he died. 

The group resumed operations in September, but this weekend, 0\_neday wrote that the REvil domain had been accessed using the keys of "Unknown." 

In another message, 0\_neday said, "The server was compromised, and they were looking for me. To be precise, they deleted the path to my hidden service in the torrc file and raised their own so that I would go there. I checked on others -- this was not. Good luck, everyone; I'm off."

Now Reuters has confirmed that law enforcement officials from the US and other countries, alongside a number of cybersecurity experts, were behind the actions 0\_neday described on Sunday. 

VMWare head of cybersecurity strategy Tom Kellerman and other sources told Reuters that the governments hacked REvil's infrastructure and forced it offline. 






The FBI and White House did not respond to requests for comment. 

Jake Williams, CTO of BreachQuest, told ZDNet that REvil being compromised has been talked about in closed CTI groups since at least October 17. 

"It was known no later than the 17th that core group members behind REvil were almost certainly compromised. By standing up the Tor hidden services, someone demonstrated they had the private keys required to do so. This was effectively the end of REvil, which was already having trouble attracting affiliates after its infrastructure went offline in July following the Kaseya attack," Williams said. 

"To attract affiliates, REvil had been offering up to 90% profit shares, but were still finding few takers. After the Tor hidden service was turned on, demonstrating possession of the private keys, it was obvious that the group had been breached and they would be unable to attract new affiliates for operations. A big open question in my mind is whether re-enabling the Tor hidden services was a counterintelligence mistake by law enforcement or was an intentional act to send a message. There are certainly arguments for either case."

The FBI [has faced backlash](https://www.zdnet.com/article/congress-demands-briefing-from-fbi-on-decision-not-to-share-kaseya-decryption-keys/) in recent weeks because they recently revealed that they managed to obtain a universal decryption key for the hundreds of victims affected by the [ransomware attack on Kaseya](https://www.zdnet.com/article/updated-kaseya-ransomware-attack-faq-what-we-know-now/).

But FBI officials told Congress that they [held off providing the keys](https://www.zdnet.com/article/fbi-decision-to-withhold-kaseya-ransomware-decryption-keys-stirs-debate/) to victims for weeks because they were planning a multi-country effort to take down REvil's infrastructure. REvil ended up [closing shop](https://www.zdnet.com/article/revil-websites-down-after-governments-pressured-to-take-action-following-kaseya-attack/) before the operation could be undertaken, and the FBI eventually handed out the keys to victims and helped a company [create a universal decryptor](https://www.zdnet.com/article/bitdefender-releases-universal-decryptor-for-revilsodinokibi-victims-hit-before-july-13/). 

Reuters reported that [when the group resurfaced in September](https://www.zdnet.com/article/revil-ransomware-group-resurfaces-after-brief-hiatus/), they actually restarted the servers that had been taken over by law enforcement officials. This led to the most recent law enforcement action, according to Reuters, which added that the operation is still ongoing. 

Williams noted that it appears likely that at least some arrests were involved, pointing back to the original messages from 0\_neday.

"The launch of the hidden service indicates someone else possesses the private keys for their hidden services. While the keys could potentially have been acquired purely through hacking back, it's hard to imagine that's the case given Unknown's disappearance as well. The obvious conclusion is that it's likely Unknown (or a close coconspirator) was arrested, though the arrest may have been enabled via hacking back operations," Williams said. 

For those hit with ransomware after the group's return, Williams said it was unlikely that the government had decryption keys or that the remaining gang members would release them.

"After the July disruptions, it's believed that REvil reset the campaign keys used by each affiliate. Core REvil user 0\_neday announced that campaign keys would be given to REvil affiliates so they could continue negotiating with their victims. It seems unlikely at this point that the US government has a master key for REvil," Williams explained. 

"After the backlash over not releasing the campaign key used in the Kaseya attack, it's hard to believe the government would risk more negative publicity. Individual affiliates may release their campaign keys, but it seems doubtful at this time that the core REvil group will."





#### Tags:
[[REvil]] [[0_neday]] [[Reuters]] [[ransomware]] [[ZDNet]]
