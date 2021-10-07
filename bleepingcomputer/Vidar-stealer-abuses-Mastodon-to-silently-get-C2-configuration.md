# Vidar stealer abuses Mastodon to silently get C2 configuration
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/vidar-stealer-abuses-mastodon-to-silently-get-c2-configuration/)
+ Date: October 7, 2021
+ Author: Bill Toulas


## Article:
![](https://www.bleepstatic.com/content/hl-images/2021/10/07/Mastodon.jpg?rand=379998728)


The Vidar stealer has returned in a new campaign that abuses the Mastodon social media network to get C2 configuration without raising alarms. 


The particular malware [has been active](https://www.bleepingcomputer.com/news/security/fake-vpn-site-pushes-cryptbot-and-vidar-info-stealing-trojans/) since at least October 2018 and we've seen it in [numerous different campaigns](https://www.bleepingcomputer.com/news/security/gandcrab-operators-use-vidar-infostealer-as-a-forerunner/). The reason why it’s so widely deployed is that it remains effective in its job and is also easy to source through Telegram channels and underground forums where it sells for as little as $150. 


The data that Vidar attempts to steal from infected machines includes the following:


* All popular browser information such as passwords, cookies, history, and credit cards details.
* Cryptocurrency wallets.
* Files according to regex strings given by the TA.
* Telegram credentials for Windows versions.
* File transfer application information (WINSCP, FTP, FileZilla)
* Mailing application information.


What makes this particular campaign standout is how Vidar abuses Mastodon, the popular open-source social media network, to obtain dynamic configuration and C2 connectivity.


The threat actors set up accounts on Mastodon and then add the IP of the C2 that the stealer will use on their profile's description section. 



![Actor's Mastodon profile with C2 URL on the description](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/mastodon%20profile.png)Actor's Mastodon profile with C2 URL on the description. Source: Cyberint
The idea is to secure communications from the compromised machine to the configuration source, and since Mastodon is a trusted platform, it shouldn’t raise any red flags with security tools. At the same time, Mastodon a relatively under-moderated space so these malicious profiles are unlikely to be spotted, reported, and removed. 


Researchers at [Cyberint](https://blog.cyberint.com/vidar-stealer-abuses-mastadon-social-network), who discovered this campaign, report that each C2 they observed contained between 500 and 1,500 different campaign IDs, indicative of the wide scale of Vidar’s deployment. 


Upon execution, a POST request is sent for the configuration, and then Vidar fetches its six DLL dependencies from the C2 server via a series of GET requests. These are legitimate third-party DLLs for networking services, MS Visual Studio runtime, etc. 



![HTTP Post request for fetching dependency](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/dependency%20request.png)HTTP Post request for fetching dependency. Source: Cyberint
By utilizing these DLLs, Vidar steals data like email credentials, chat account details, web-browsing cookies, etc., compresses everything into a ZIP archive, and then exfiltrates the archive to the attackers via an HTTP POST.. 


Once this is done, Vidar kills its own process and deletes the DLLs and the main executable, in an attempt to wipe all evidence of its presence in the victim’s machine. The later the victim realizes their credentials were stolen, the more opportunities for exploitation the actors will have. 


To avoid having to deal with a nasty Vidar infection, take into account the common delivery channels. These are typically unsolicited emails that make bold claims about pending orders, payments, and package deliveries. 


Another method of distribution is via direct messages on popular social media platforms, or even through laced game cracks downloaded via torrent.




#### Tags:
[[Vidar]] [[C2]] [[Bleeping Computer]]
