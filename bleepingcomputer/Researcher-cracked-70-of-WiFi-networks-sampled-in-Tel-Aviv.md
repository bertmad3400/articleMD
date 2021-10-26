# Researcher cracked 70% of WiFi networks sampled in Tel Aviv
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/researcher-cracked-70-percent-of-wifi-networks-sampled-in-tel-aviv/)
+ Date: October 26, 2021
+ Author: Bill Toulas


## Article:
![wifi](https://www.bleepstatic.com/content/hl-images/2021/10/26/wifi-cropped.jpg)


A researcher has managed to crack 70% of a 5,000 WiFi network sample in his hometown, Tel Aviv, to prove that home networks are severely unsecured and easy to hijack.


CyberArk security researcher Ido Hoorvitch first wandered in the city center with WiFi sniffing equipment to gather a sample of 5,000 network hashes to use in the research.


Next, the researcher exploited a flaw that allows the retrieval of a PMKID hash, usually generated for roaming purposes.


To gather PMKID hashes, Hoorvitch used a $50 network card that can act as a monitor and a packet injection tool and sniffed with WireShark on Ubuntu, both free software.



![Logging PMKID hashes on WireShark](https://www.bleepstatic.com/images/news/u/1220909/Security/wireshark.jpg)**Logging PMKID hashes on WireShark**  

Source: CyberArk
The PMKID hash comprises the network’s SSID, the passphrase, the MAC address, and a static integer.



![PMKID hash](https://www.bleepstatic.com/images/news/u/1220909/Security/pmkid(1).jpg)**PMKID hash**
Using a previously discovered [method](https://hashcat.net/forum/thread-7717.html) by Jens “atom” Steube’s (Hashcat’s lead developer), the researcher gathered PMKIDs that would be cracked to derive the password.


"Atom’s technique is clientless, making the need to capture a user’s login in real time and the need for users to connect to the network at all obsolete," explains Hoorvitch in [the report](https://www.cyberark.com/resources/threat-research-blog/cracking-wifi-at-scale-with-one-simple-trick).


"Furthermore, it only requires the attacker to capture a single frame and eliminate wrong passwords and malformed frames that are disturbing the cracking process."


At first, "mask attacks" were launched to determine if any users had set their cellphone number as their WiFi password, which is common in Israel.


Cracking such passwords would be a case of calculating all number options for Israeli phone numbers, and that's ten digits starting with 05, so it's only eight digits.


Using a standard laptop, the researcher cracked 2,200 passwords at an average speed of nine minutes per password using this method.


The next phase of the attack involved a standard dictionary attack, using the ‘Rockyou.txt’ dictionary.


This led to quickly cracking another 1,359 passwords, with most of them using only lower-case characters.



![Total number of cracked passwords.](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Total number of cracked passwords.**  

Source: CyberArk
Poor security practices
-----------------------


By following this simple and inexpensive cracking method, the researcher cracked roughly 70% of the passwords for the sampled WiFi networks.


The research shows that most people are not setting a strong password for their WiFi networks even though they are at risk of being hacked.


If your WiFi password is hacked, anyone can access your home network, change your router's settings, and potentially pivot to your personal devices by exploiting flaws.


Good passwords should be at least ten characters long and have a mix of lower case and upper case letters and symbols and digits.


If you want a password that is easier to remember, you can try a three-word [random passphrase](https://www.worksighted.com/random-passphrase-generator/#passphrase-generator) that contains numeric or special symbols as separators.


Finally, if your router supports roaming or WPS, disable them both, as it trades security for convenience.




#### Tags:
[[WiFi]] [[PMKID]] [[CyberArk]] [[Hoorvitch]] [[Bleeping Computer]]
