# CISA: GPS software bug may cause unexpected behavior this Sunday
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/technology/cisa-gps-software-bug-may-cause-unexpected-behavior-this-sunday/)
+ Date: October 22, 2021
+ Author: Bill Toulas


## Article:
![gps watch](https://www.bleepstatic.com/content/hl-images/2021/10/22/gps_watch.jpg?rand=261019527)


The Cybersecurity and Infrastructure Security Agency (CISA) warned that GPS deices might experience issues over the weekend because of a timing bug impacting Network Time Protocol  (NTP) servers running the GPS Daemon (GPSD) software.


*"The Network Time Protocol (NTP) has been critical in ensuring time is accurately kept for various systems businesses and organizations rely on. Authentication mechanisms such as Time-based One-Time Password (TOTP) and Kerberos also rely heavily on time. As such, should there be a severe mismatch in time, users would not be able to authenticate and gain access to systems."* - [SANS ISC](https://isc.sans.edu/forums/diary/Keeping+Track+of+Time+Network+Time+Protocol+and+a+GPSD+Bug/27886/)


The bug is set to trigger this Sunday, on October 24th, and the implications are somewhat unpredictable as it could cause systems to become unresponsive or unavailable.


On October 24, 2021, all Network Time Protocol (NTP) servers using GPSD versions [3.20 through 3.22](https://gitlab.com/gpsd/gpsd/-/issues/144) are going to jump back 1024 weeks in time, to March 3, 2002.


The vulnerable versions were released between December 31, 2019, and January 8, 2021, so the affected GPS devices constitute a significant portion of those deployed out there at the moment.


The problem could be severe, but it’s somewhat of a [Y2K bug](https://en.wikipedia.org/wiki/Year_2000_problem), so nobody can be sure about whether or not the devices will actually encounter functional or service reliability issues.


[CISA urges](https://us-cert.cisa.gov/ncas/current-activity/2021/10/21/gps-daemon-gpsd-rollover-bug) the affected owners and operators to update to GPSD version 3.23, released on August 8, 2021, or newer, to avoid all chances of facing problems.




> 
> CURRENT ACTIVIY: On October 24, 2021, Network Time Protocol servers using bugged GPSD versions 3.20-3.22 may rollback the date 1,024 weeks—to March 2002—which may cause systems and services to become unavailable or unresponsive. Learn more: <https://t.co/hlpdQviDJm> [pic.twitter.com/rlZMu1QGoj](https://t.co/rlZMu1QGoj)
> 
> 
> — Cybersecurity and Infrastructure Security Agency (@CISAgov) [October 22, 2021](https://twitter.com/CISAgov/status/1451508642935623690?ref_src=twsrc%5Etfw)


GPS and timekeeping
-------------------


GPSD is a widely-used [service daemon](https://gpsd.gitlab.io/gpsd/) that translates time data into usable information for client applications such as navigation and time-keeping solutions.


It is open-source cross-platform software available for Linux, Unix, macOS, and Android, and it is used in computers, phones, cars, robots, and transaction validation systems.


Accurate timekeeping is of essence to GPS devices, and real-time tracking requires accuracy of at least [100 nanoseconds](https://www.atomic-clock.galleon.eu.com/support/gps-time-accuracy.html). GPS satellites count time in weeks and seconds within the active week.


Every 1024 weeks (almost 20 years) a week number rollover phenomenon takes place in the system due to an integer overflow on the broadcasted ten-digit binary, causing the internal value of the week count to drop to zero.


This is an intrinsic issue that was eventually addressed with additional code that is meant to help the device anticipate the rollover.


While it’s not relevant to the daemon bug, it can give us an indication of the effects of dramatic time shifts of this kind on global positioning systems.


The last time it happened was on April 6, 2019, and it caused [flight cancellations](https://arstechnica.com/information-technology/2019/04/gps-rollover-apparently-cause-of-multiple-flight-delays-groundings/), wireless [network crashes](https://www.cvp.nyc/nyc-wireless-network), and [functional problems](https://mobilesyrup.com/2019/04/05/telus-contacting-customers-in-advance-of-gps-rollover-that-may-affect-some-customers/) on older smartphones.


We’re not saying that Sunday is going to wreak havoc on any GPS-relying systems out there, but chances are that you’re going to stumble upon issues.


Therefore, if you're using a GPS device for work, leisure, or safety, be prepared for the unexpected this Sunday.




#### Tags:
[[GPSD]] [[(NTP)]] [[Bleeping Computer]]
