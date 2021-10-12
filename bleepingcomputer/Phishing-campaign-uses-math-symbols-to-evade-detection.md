# Phishing campaign uses math symbols to evade detection
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/review/security/phishing-campaign-uses-math-symbols-to-evade-detection/)
+ Date: October 12, 2021
+ Author: Bill Toulas


## Article:
![phishing](https://www.bleepstatic.com/content/hl-images/2021/10/12/Phishing.jpg?rand=1468339167)


Phishing actors are now using mathematical symbols on impersonated company logos to evade detection from anti-phishing systems.


One notable case spotted by analysts at INKY involves the spoofing of Verizon, a large U.S.-based telecommunication service provider.


In this case, the actors are using a square root symbol, a logical NOR operator, or the checkmark symbol itself, all helping to create a slight optical differentiation that could trick [AI-based spam detectors](https://www.microsoft.com/security/blog/2021/08/04/spotting-brand-impersonation-with-swin-transformers-and-siamese-neural-networks/).



![Phishing message using the square root symbol in the Verizon logo](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/message%20voice(1).png)**Phishing message using the square root symbol in the Verizon logo**  

Source: INKY
For many people who don't keep up with the latest logo changes though, these slightly altered logos look good enough, so the delivery success and user engagement rates have better chances of staying high.


You have fake voicemail
-----------------------


All three spoofing types masquerade as voicemail notifications containing an embedded ‘Play’ button, that when clicked, take the user to a phishing portal that was crafted to look like a Verizon website.


The landing domain is clearly not part of Verizon’s official webspace, with one example given in the report being sd9-08[.]click.



![A cloned Verizon site used as the phishing page of the campaign](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/phishing%20site(1).png)**A cloned Verizon site used as the phishing page of the campaign**  

Source: INKY
The actors bet on the carelessness of the target, as otherwise, the spoofed site looks pretty convincing. Also, Inky has found that this phishing campaign relied on recently-registered domains that were unreported.


The logo on the cloned site is the genuine one as the phishing actors stole most of the HTML and CSS elements from the real Verizon site.


Scrolling down on the fake page, the visitor will find the alleged voicemail, but they are only allowed to access it if they provide their Office365 account credentials on the sign-in form.


The first attempt will result in getting an “incorrect password” message, while the second attempt is generating a bogus error that ends the login procedure.


This is done for the phishing actors to ensure that the victim hasn’t mistyped their password in the first attempt, so it’s essentially a “quality assurance” step.



![Bogus error generated after the victim enters their credentials twice on the phishing site](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Bogus error message generated after the victim enters their credentials twice on the phishing site**  

Source: INKY
When you receive email of this kind, proper scrutiny is an important factor to not falling victims to these scams. Never click on embedded buttons, always validate the URL of the site you’re about to enter any credentials, and finally, consider the  realism of the situation.


In this case, a message from Verizon is urging recipients to enter their Office365 credentials, which does not make sense in this situation. If the contents of an email do not make sense for whatever reason, it's usually phishing and the email should be junked. 




#### Tags:
[[phishing]] [[Verizon]] [[Source:]] [[Bleeping Computer]]
