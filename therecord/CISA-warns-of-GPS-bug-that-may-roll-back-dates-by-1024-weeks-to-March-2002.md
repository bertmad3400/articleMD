# CISA warns of GPS bug that may roll back dates by 1,024 weeks, to March 2002
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/cisa-warns-of-gps-bug-that-may-rollback-dates-by-1024-weeks-to-march-2002/)
+ Date: October 22, 2021
+ Author: Catalin Cimpanu


## Article:
![CISA warns of GPS bug that may roll back dates by 1,024 weeks, to March 2002](https://therecord.media/wp-content/uploads/2021/10/date-time-clock.jpg)

The US government is warning companies about a bug in a software library used to synchronize time via the GPS navigational system that will rollback time on unpatched devices by 1,024 weeks to a date of March 2002.


* The bug resides in [gpsd](https://gitlab.com/gpsd/gpsd), a C library for adding GPS support to a device’s firmware.
* Besides providing connectivity to the Global Positioning System (GPS), the library can also be used to obtain a Coordinated Universal Time (UTC) from the GPS system in order to synchronize devices.
* A bug was discovered in this time retrieval feature [in July this year](https://gitlab.com/gpsd/gpsd/-/issues/144).
* [On October 24](https://gitlab.com/gpsd/gpsd/-/issues/144#note_633479883), the bug will trigger a rollback of UTC time to 1024 weeks in the past, to March 3, 2002.
* gpsd versions 3.20 (released December 31, 2019) through 3.22 (released January 8, 2021) contain the bug.
* A fix was released in August 2021, with [gpsd 3.23](https://gpsd.gitlab.io/gpsd/NEWS).


Yesterday, on Thursday, the Cybersecurity and Infrastructure Security Agency (CISA) published a [security advisory](https://us-cert.cisa.gov/ncas/current-activity/2021/10/21/gps-daemon-gpsd-rollover-bug) about this bug and its impending trigger date of October 24, this Sunday.


CISA urged operators of critical infrastructure to update devices to use the latest gpsd library versions, warning that the bug “may cause systems and services to become unavailable or unresponsive.”


Analyzing the bug in a [write-up for ISC SANS on September 29](https://isc.sans.edu/forums/diary/Keeping+Track+of+Time+Network+Time+Protocol+and+a+GPSD+Bug/27886/), security researchers Yee Ching said the bug resides in a legitimate GPS feature called the “[week rollover](https://www.gps.gov/support/user/rollover/)” that resets the week number back to zero every 19.7 years.


Yee said that due to a “bug in some sanity checking code within GPSD” the library subtracted 1024 from the week number, rather than just resetting a counter, effectively rolling back time.





#### Tags:
[[]] [[The Record]]
