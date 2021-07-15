# Software maker removes "backdoor" giving root access to radio devices
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/software-maker-removes-backdoor-giving-root-access-to-radio-devices/)
+ Date: July 15, 2021
+ Author: Ax Sharma


## Article:
![radio microphone](https://www.bleepstatic.com/content/hl-images/2021/07/15/radio-on-air.jpeg)


The author of a popular software-defined radio (SDR) project has removed a "backdoor" from radio devices that granted root-level access.


The backdoor had been, according to the author, present in all versions of KiwiSDR devices for the purposes of remote administration and debugging.


Last night, the author pushed out a "bug fix" on the project's GitHub aimed at removing this backdoor silently, which sparked some backlash.


Since then, the author's original forum posts and comments with any mention of "backdoor" have been removed over the last few hours.


Hardcoded password gives root access to all devices
---------------------------------------------------


KiwiSDR is a software-defined radio that can be attached to an embedded computer, like Seeed BeagleBone Green (BBG).


It is provided either as a standalone board or a more complete version featuring BBG, a GPS antenna, and an enclosure.



![KiwiSDR user interface](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/kiwisdr-backdoor-radio/OV_BCB_1_780px.png)**KiwiSDR [user interface](http://kiwisdr.com/quickstart/) with different RF controls**
SDRs are aimed at replacing radio frequency (RF) communication hardware with software or firmware for carrying out signal processing activities that would normally require hardware devices.


The concept is analogous to [software-defined networking](https://en.wikipedia.org/wiki/Software-defined_networking).


Yesterday, Mark Jessop, an RF engineer, and radio operator came across an interesting forum post in which the author of the [KiwiSDR](http://kiwisdr.com/ks/using_Kiwi.html) project admitted to having remote access to all radio receiver devices running the software.




> 
> Interesting post on the KiwiSDR forums. Seems to imply the KiwiSDR author has remote access to all KiwiSDRs? Post has since been modified to remove the last paragraph and the thread locked :-/ <https://t.co/cAi5dS7J49> [pic.twitter.com/elqSsaUJ65](https://t.co/elqSsaUJ65)
> 
> 
> — Mark Jessop (@vk5qi) [July 14, 2021](https://twitter.com/vk5qi/status/1415429408312098819?ref_src=twsrc%5Etfw)


Another user, *M.* dug out a [2017 forum thread](https://twitter.com/TVqQAAMAAAAEAAA/status/1415432284602212352) where KiwiSDR's developer admitted that a backdoor indeed provided them with remote access to all KiwiSDR devices. 


Although the entire KiwiSDR forum site has become inaccessible as of today, an archived copy of the forum post seen by BleepingComputer confirms the contents of the tweet:



![kiwisdr author mentions devices have backdoor](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/kiwisdr-backdoor-radio/backdoor-author-post.jpg)**KiwiSDR software author stated there's a backdoor in all devices giving them remote access**  

Source: BleepingComputer
Furthermore, as of today, over 600 KiwiSDR devices are online with the backdoor still present in them, as [highlighted](https://twitter.com/hackerfantastic/status/1415455024851869696) by *Hacker Fantastic.*


Although these devices are mainly acting as radio receivers, it is worth noting, any remote actor who logs in using the hardcoded master password is granted root-level access to the device's (Linux-based) console.


This can enable adversaries to probe into the IoT devices, take them over, and begin traversing adjacent networks the radio devices are connected to:


"These KiwiSDRs are used for receiving HF radio stations. The backdoor itself doesn't give an attacker any special SDR access, just that they can access the console of the device (Linux) and start pivoting into networks," ethical hacker *[xssfox](https://twitter.com/xssfox)* told BleepingComputer.


An image of the KiwiSDR administration panel obtained by BleepingComputer shows console level access with root access ([notice the #](https://askubuntu.com/a/706190)) is possible:



![kiwisdr panel](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**KiwiSDR remote admin panel provides root access to the device console**
A [video](https://twitter.com/xssfox/status/1415606351464595459) created by *xssfox* demonstrates how the backdoor can be exploited via a simple HTTP GET request, which looks like:


http://radio-device-domain.example.com:8074/admin?su=**kconbyp**
Note: the superuser password (kconbyp) shown above is an older password, SHA256 hash of which [used to be present](http://git.mis.ks.ua/US1GHQ/Beagle_SDR_GPS/commit/e66e67a20bc0c9201c50d5b7e18434fb61766ba8) on KiwiSDR devices. The more recent hash (shown below) is different, indicating "kconbyp" won't work on later versions of KiwiSDR and that a newer master password has been present.


Dev pushes out "bug fix" overnight removing the backdoor
--------------------------------------------------------


As seen by BleepingComputer, as of a few hours ago a fix has been committed to KiwiSDR's GitHub project removing the backdoor code.


The update removes multiple administrative functions, and specifically the code that compares the provided master password against its SHA256 hash:



![kiwisdr author removes backdoor](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**KiwiSDR author removes hardcoded password from devices** ([GitHub](https://github.com/jks-prv/Beagle_SDR_GPS/commit/0edf5fcfb99fdffa2058c86f60c855a306a857ee?branch=0edf5fcfb99fdffa2058c86f60c855a306a857ee&diff=unified#diff-ad090c36f5cf2b493c321e92af0edbf58f44764081e3a058a532f7b387fcc1feL833))
Jessop clarified that there is no indication of KiwiSDR's author having misused the backdoor access, which had been introduced with the intention of debugging KiwiSDR devices in good faith.


He further said KiwiSDR developer has been [extremely responsive](https://twitter.com/vk5qi/status/1415447199350095874) in patching bugs and adding features.


But, like others, the engineer did express concerns, that the master password would transmit over HTTP enabling any Man-in-the-Middle (MitM) threat actor to potentially intercept it and consequently gain remote access to all devices.




> 
> However, given the KiwiSDR is HTTP only, sending what is essentially a 'master' password in the clear is a little worrying. KiwiSDR does not support HTTPS, and it's been stated that it will never support it. (Dealing with certs on it would be a PITA too)
> 
> 
> — Mark Jessop (@vk5qi) [July 14, 2021](https://twitter.com/vk5qi/status/1415440183982391298?ref_src=twsrc%5Etfw)


Some Redditors also expressed that backdoors were never okay, regardless of whether HTTPS was in use:


"No way. Back doors are never okay. Password was sent in the clear, as HTTPS isn't supported. Eventually someone would have exploited this. Hell, someone might have already exploited this and we just don't know about it," said one of the users in a [thread](http://www.reddit.com/r/RTLSDR/comments/okfslu/interesting_post_on_the_kiwisdr_forums_seems_to/h58iawp?utm_source=share&utm_medium=web2x&context=3).


KiwiSDR users should upgrade to the latest version v1.461 released today on [GitHub](https://github.com/jks-prv/Beagle_SDR_GPS/commit/0edf5fcfb99fdffa2058c86f60c855a306a857ee#diff-0f9dd0b75ca4dd0210c8be84066de570e59c0713d22688ac5b26422af8b05021R5) that removes the backdoor from their radio devices.




#### Tags:
[[KiwiSDR]] [[BleepingComputer]] [[GitHub]] [[Jessop]] [[software-defined]] [[HTTP]] [[kconbyp]] [[HTTPS]] [[Bleeping Computer]]
