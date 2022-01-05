# When biometrics can be outsmarted this way, we need to talk
### It’s a sad fact of mobile authentication: the industry tends to initially support the least effective and secure options. Take the recent case of the sleeping woman in China, for instance.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3646129/when-biometrics-can-be-outsmarted-this-way-we-need-to-talk.html
+ Date: 2022-01-03T06:43-05:00
+ Author: Evan Schuman


## Article:
![Article Image](https://images.idgesg.net/images/article/2020/01/cso_nw_digital_identity_security_authentication_access_by_metamorworks_gettyimages-1176067266-100826768-large.jpg?auto=webp&quality=85,70)

It’s one of the sad facts of mobile authentication that the industry tends to initially support the least effective security options. Hence, phones initially supported authentication based on fingerprints (which can be impacted by prescriptions, cleaning products, hand injuries, and dozens of other factors) and then moved on to facial recognition. 

In theory, facial recognition is supposed to be more accurate. Mathematically, that’s fair, as it is examining far more data points than scanning a fingerprint. But the reality in the real world is much more problematic. It requires a precise distance from the phone and yet offers no pre-scan markers for the user to know when they hit it correctly. That’s one reason I see facial recognition reject a scan roughly 40% of the time — even though it will approve a positive scan two seconds later.

In Apple’s early rollout, family members could sometimes unlock each other’s phones. This wasn’t limited to identical twins. [Even mothers and sons can get through the “authentication” of facial recognition](https://www.wired.com/story/10-year-old-face-id-unlocks-mothers-iphone-x/). 

But a recent case in China shows that Apple’s facial recognition issues are still bad. In China, a man approached a sleeping woman (his ex-girlfriend), pulled open her eyelids, got a facial recognition green light, [and was able to withdraw money from her bank account](https://www.vice.com/en/article/epxzja/facial-recognition-theft-alipay-china).

First, this is hardly one of the better ways of getting back with one’s ex. But from a cybersecurity perspective, it reinforces the point that mobile devices need much more stringent authentication methods. 

The best route would be to use weaker methods — such as passwords, PINs, and weaker biometrics — to conveniently access low-priority accounts, such as unlocking the phone to check a weather forecast. But for bank/money access, social media logins, and any connection to enterprise systems, behavioral analytics should be required.

The very nature of behavioral analytics makes it difficult for a thief to impersonate the individual. Taking an unconscious person’s finger or pulling back an eyelid can be done, assuming the thief has physical access to the user and the phone. PINs are unfortunately easy to steal via shoulder surfing, especially for someone with extended physical access.

But mimicking how many typos that user does every 100 words? Or their exact typing speed? Or the angle they tend to hold their phone? Those are personalized and difficult to fake. Yes, *some* behavioral analytics factors are easy to fake, including a user’s IP address, location, and a phone’s fingerprint. That’s why a behavioral analytics deployment needs to use as many factors as possible, mixing easy-to-fake factors with difficult-to-fake ones. 

One of the best things about behavioral analytics is that it operates silently in the background, which means that it’s about as frictionless (for the user) as it is practical. It offers the best of both worlds: it’s a far more stringent and reliable authentication method, but is easier for users than a password or biometrics. 

For IT, that frictionless nature makes users more accepting. Also, that “in the background” nature makes it even more difficult for a thief/intruder, because the attacker can't be certain what the system is checking at any given moment. 

This why CIOs and CISOs shouldn't put a lot of faith in biometrics. Even the most violent and aggressive attack methods — such as putting a gun to a user’ head and ordering them to access sensitive enterprise files — can be thwarted with behavioral analytics. If the fear and nervousness from such an attack increases typos and slows down typing speed, that might be enough for a supervisor to be contacted. If that supervisor then asks for a video session to make sure everything is OK, it might make the attacker leave. (This is especially true if the attacker suspects the supervisor has already sent police and is using the video session questions to just stall for time.)

The reason this is such a critical issue for 2022 is that the steady rise of mobile access to your most sensitive databases on the enterprise (including enterprise cloud accounts) is likely to keep growing. We are now at the point where IT can no longer assume that desktop defenses are sufficient. Even if IT has issued a laptop to all employees with sufficient privileges, there isn't an company out there that would discourage mobile access. As travel slowly returns this year for some segments, the road warrior issues will make a return engagement. Now, though, attackers — especially those with a specific interest in your systems — will be ever more focused on those mobile interactions.

The most popular and amorphous cybersecurity buzzword these days is Zero Trust. Any meaningful Zero Trust rollout needs to start with a far more robust approach to authentication, along with a hard review of access management/privilege control. With mobile devices, authentication has to be *the* overwhelming priority. The path of least resistance is to just piggyback on a mobile device's on-board authentication. That can work *as* long *as* biometrics is just one of a half-dozen factors examined.

 If you’re still skeptical, there's a Chinese ex-boyfriend you need to meet.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=route]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Mining]]

#### Location:
[[victim.country.name=China]] [[victim.continent.name=Asia]] [[victim.country.name=Oman]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[]] [[Computerworld]]

