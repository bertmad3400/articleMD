# This banking Trojan abuses YouTube to manage remote settings
### The spam-spread malware is another headache for Latin America in the cybersecurity realm.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-banking-trojan-abuses-youtube-to-manage-remote-settings/)
+ Date: September 17, 2021 -- 10:10 GMT (11:10 BST)
+ Author: Charlie Osborne


## Article:
Unknown

A banking Trojan has been detected that abuses YouTube, Pastebin, and other public platforms in order to spread and control compromised machines. 


On Friday, ESET wrapped up a series on banking Trojans present in Latin America -- [including Janeleiro](https://www.zdnet.com/article/meet-janeleiro-a-new-banking-trojan-striking-corporate-targets/), a new malware sample similar to Casbaneiro, Grandoreiro, and Mekotio -- but this one does not just hit that region; instead, campaigns have been detected across Brazil, Mexico, and Spain. 

In a blog post, the cybersecurity researchers said that the Trojan, named Numando, has been active since 2018. Written in Delphi, this financial malware displays fake overlay windows to dupe victims into submitting sensitive data, such as the credentials used to access financial services. 

As is the case for many banking Trojan variants, Numando is spread almost "exclusively" through spam and phishing campaigns, ESET says. 

These attempts are not exactly sophisticated, as of the time of writing, no more than a few hundred victims have been traced. As a result, it appears that Numando is "considerably less successful" than other Latin American Trojans, including Mekotio and Grandoreiro.  

It's likely that the operator's lack of sophistication has contributed to a low infection rate. In recent campaigns, spam sent to distribute Numando are composed of a phishing message and a .ZIP attachment included with the email.  

A decoy .ZIP file is downloaded, together with an actual .ZIP file that contains a .CAB archive -- bundled with a legitimate software app -- an injector, and the Trojan. The malware is hidden in a large .BMP image file, of which samples are below: 

![screenshot-2021-09-17-at-08-23-42.png]()![screenshot-2021-09-17-at-08-23-42.png](https://www.zdnet.com/a/hub/i/r/2021/09/17/510f728e-598b-4dc9-a450-e5f1a41befc9/resize/1200xauto/1a5b2cace87c37e06f7d34e20257fadd/screenshot-2021-09-17-at-08-23-42.png)
 ESET
 




If the software app is executed, the injector is side-loaded and the malware is then decrypted using an XOR algorithm and a key. 

Once installed on a target machine, Numando will create fake overlay windows when a victim visits financial services. If users submit their credentials, they are stolen and sent to the malware's command-and-control (C2) server.  

Numando also abuses public services including Pastebin and YouTube to manage its remote configuration settings.  

"The format is simple -- three entries delimited by ":" between the DATA:{ and } markers," ESET explained. "Each entry is encrypted separately the same way as other strings in Numando -- with the key hardcoded in the binary. This makes it difficult to decrypt the configuration without having the corresponding binary, however, Numando does not change its decryption key very often, making decryption possible." 

Google was informed of the videos found by the cybersecurity team and the ones that have been detected have since been taken down.  

![screenshot-2021-09-17-at-08-26-42.png]()![screenshot-2021-09-17-at-08-26-42.png](https://www.zdnet.com/a/hub/i/r/2021/09/17/6c1d5928-fd23-400e-a35b-ab1032658cce/resize/1200xauto/67852e64e77a4e3a624572e3248d954c/screenshot-2021-09-17-at-08-26-42.png)Example YouTube remote config upload


 ESET
 Numando is also able to simulate mouse clicks and keyboard actions, hijack PC shutdown and restart functions, take screenshots, and kill browser processes.  

"Unlike most of the other Latin American banking trojans covered in this series, Numando does not show signs of continuous development," ESET says. "There are some minor changes from time to time, but overall the binaries do not tend to change much." 

In other recent Trojan news, in May, Kaspersky [unmasked Bizarro](https://www.zdnet.com/article/bizarro-banking-trojan-surges-across-europe/), a prolific Trojan detected recently across Europe. Bizarro has honed in on the customers of at least 70 banks across countries including Brazil, Argentina, and Chile, but now appears to be focused on European victims.   

###  Previous and related coverage

* [Bizarro banking Trojan surges across Europe](https://www.zdnet.com/article/bizarro-banking-trojan-surges-across-europe/)  

* [Meet Janeleiro: a new banking Trojan striking company, government targets](https://www.zdnet.com/article/meet-janeleiro-a-new-banking-trojan-striking-corporate-targets/)  

* [Malicious apps on Google Play dropped banking Trojans on user devices](https://www.zdnet.com/article/malicious-apps-on-google-play-dropped-banking-trojans-on-user-devices/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[Numando]] [[ESET]] [[malware]] [[.ZIP]] [[ZDNet]]
