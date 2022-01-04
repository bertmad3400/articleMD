# US govt provides new guidelines for authentication systems
### The National Institute of Standards and Technology (NIST) released new authentication system recommendations, highlighting multiple erroneous approaches in currently established practices.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/us-govt-provides-new-guidelines-for-authentication-systems/
+ Date: 2022-01-04T15:59:31-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/04/biometric-authentication.jpg)

![Fingerprint authentication](https://www.bleepstatic.com/content/hl-images/2022/01/04/biometric-authentication.jpg)


The National Institute of Standards and Technology (NIST) released new authentication system recommendations, highlighting multiple erroneous approaches in currently established practices.


NIST is a non-regulatory governmental agency in the United States, and among its responsibilities is the development of standards to defend against unauthorized access to state agent accounts and computer systems.


Its public reports are to be taken as official practice recommendations and are scientifically substantiated.


While this new report outlines authentication requirements for government agencies, they are also excellent guidelines for all fields and user levels.


On passwords
------------


On the strength of passwords, NIST underlines that the requirements of using special characters, for example !$#%&, are obsolete since users still tend to add something that will keep the password memorable.


Due to this, threat actors can predict what characters a user will add based on password composition rules at particular sites.


The preferable approach for websites would require users to use long passwords that are much harder to crack.


For this, NIST notes that websites must allow space characters to set multi-word phrases, which can still be memorable while significantly increasing entropy.


Currently, most sites will reject spaces or other special characters because SQL attacks rely on their use. Unfortunately, this rejection frustrates users who often switch to a weaker password.


Additionally, NIST suggests that websites check user passwords against a "black-listed" dictionary and reject them if any matches are found.


This dictionary could contain passwords leaked in public data breaches, context-specific words, and derivatives, while the system should also detect and reject repetitive or sequential characters.


On biometric authentication
---------------------------


NIST underlines that biometric authentication is probabilistic and not deterministic, and can be spoofed using high-resolution pictures or scan.


Therefore, NIST's guidelines require that biometric authentication only be used along with multi-factor authentication such as a security key or OTP authenticator.


"Biometrics SHALL be used only as part of multi-factor authentication with a physical authenticator (*something you have*)," reads the new [NIST guidelines](http://pages.nist.gov/800-63-3/sp800-63b.html).


Furthermore, government agencies will need to confirm that the biometric sensor resists tampering and that it is confirmed before taking biometric samples from a user.


"An authenticated protected channel between sensor (or an endpoint containing a sensor that resists sensor replacement) and verifier SHALL be established and the sensor or endpoint SHALL be authenticated prior to capturing the biometric sample from the claimant."


On 2FA and MFA
--------------


NIST suggests that software-based OTP generators that are so widely used today should not facilitate the cloning of the secret key onto multiple devices or should at least discourage it.


Moreover, time-based cryptographic nonces should be changed at least every 2 minutes, and each OTP value associated with a given nonce shall be accepted only once.


A nonce (number once) is a random or pseudo-random number that can only be used once as part of a cryptographic authentication protocol.


In single-factor and multi-factor OTP authenticators, if the output to combine the key and nonce is obtained using an approved block cipher or hash function, the result should be truncated to as few as six decimal digits (20 bits of entropy).


As for USB cryptographic authenticators, NIST says their challenge nonce shall be at least 64 bits in length and should also be statistically unique (derived by using a random bit generator).


Embrace strong passwords
------------------------


Finally, strong and unique passwords remain the simplest form of secure authentication, which is why we can't get rid of them despite [expert predictions](https://www.cnet.com/tech/services-and-software/gates-predicts-death-of-the-password/).


Those providing password-based sites and services should make an effort to raise the bar on what is allowed to use and deter people from picking easy-to-guess or common passwords.


From a user's perspective, install a password manager and let it generate as long passwords as allowed on each site. 


As password-managers commonly utilize web browser extensions that autofill your password, you will not be required to remember and can benefit from strong and unique passwords at every site you visit.


Alternatively, you can use random phrases consisting of at least four words (the more, the better) and always enable 2FA when the option is available.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Information]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Otp]] [[Websites]] [[Multi-factor]] [[Bleeping Computer]]

