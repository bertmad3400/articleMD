# Microsoft Exchange year 2022 bug in FIP-FS breaks email delivery
### Microsoft Exchange on-premise servers cannot deliver email starting on January 1st, 2022, due to a Year 2022 bug in the FIP-FS anti-malware scanning engine.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-year-2022-bug-in-fip-fs-breaks-email-delivery/
+ Date: 2022-01-01T12:29:32-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/03/10/Exchange1.jpg)

![Microsoft Exchange server bug](https://www.bleepstatic.com/content/hl-images/2021/03/10/Exchange1.jpg)


Microsoft Exchange on-premise servers cannot deliver email starting on January 1st, 2022, due to a "Year 2022" bug in the FIP-FS anti-malware scanning engine.


Starting with Exchange Server 2013, Microsoft enabled the FIP-FS anti-spam and anti-malware scanning engine by default to protect users from malicious email.


Microsoft Exchange Y2K22 bug
----------------------------


According to numerous reports from Microsoft Exchange admins worldwide, a bug in the FIP-FS engine is blocking email delivery with on-premise servers starting at midnight on January 1st, 2022.


Security researcher and Exchange admin Joseph Roosen said that this is caused by Microsoft using a signed int32 variable to store the value of a date, which has a maximum value of 2,147,483,647.


However, dates in 2022 have a minimum value of 2,201,010,001 or larger, which is greater than the maximum value that can be stored in the signed int32 variable, causing the scanning engine to fail and not release mail for delivery.



> 
> According to additional research on this issue, this is happening because Microsoft is using a signed int32 for the date and the new date value of 2,201,010,001 is over the max value of "long" int32 being 2,147,483,647. [@MSFTExchange](https://twitter.com/MSFTExchange?ref_src=twsrc%5Etfw) - Not sure why it was structured this way??
> 
> 
> — Joseph Roosen (@JRoosen) [January 1, 2022](https://twitter.com/JRoosen/status/1477203087421018118?ref_src=twsrc%5Etfw)


When this bug is triggered, an 1106 error will appear in the Exchange Server's Event Log stating, "The FIP-FS Scan Process failed initialization. Error: 0x8004005. Error Details: Unspecified Error" or "Error Code: 0x80004005. Error Description: Can't convert "2201010001" to long."



> 
> Dear [@msexchangeteam](https://twitter.com/msexchangeteam?ref_src=twsrc%5Etfw). The FIP-FS “Microsoft” Scan Engine Failed to Load. Can’t Convert “2201010001” to long.
> 
> 
> — long wtf = 2201010001; (@miketheitguy) [January 1, 2022](https://twitter.com/miketheitguy/status/1477097527593734144?ref_src=twsrc%5Etfw)


Microsoft will need to release an Exchange Server update that uses a larger variable to hold the date to officially fix this bug.


However, for on-premise Exchange Servers currently affected, [admins have found](https://www.reddit.com/r/sysadmin/comments/rt91z6/exchange_2019_antimalware_bad_update/) that you can disable the FIP-FS scanning engine to allow email to start delivering again.


To disable the FIP-FS scanning engine, you can execute the following PowerShell commands on the Exchange Server:



```
Set-MalwareFilteringServer -Identity  -BypassFiltering $true
Restart-Service MSExchangeTransport
```

After the MSExchangeTransport service is restarted, mail will start being delivered again.


Unfortunately, with this unofficial fix, delivered mail will no longer be scanned by Microsoft's scanning engine, leading to more malicious emails and spam getting through to users.


Microsoft is [reportedly aware of the issue](https://docs.microsoft.com/en-us/answers/questions/680488/microsoft-exchange-fip-fs-scan-engine-failed-to-lo.html) and is working on a fix, but there is no ETA on when it will be delivered.


BleepingComputer has also contacted Microsoft with questions related to the bug but has not received a response yet.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Fip-fs]] [[Int32]] [[On-premise]] [[Bleeping Computer]]
