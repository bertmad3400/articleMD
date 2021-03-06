# SonicWall shares temp fix for firewalls stuck in reboot loop
### Following a stream of customer reports that started yesterday evening, security hardware manufacturer SonicWall has provided a temporary workaround for reviving next-gen firewalls running SonicOS 7.0 stuck in a reboot loop.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/technology/sonicwall-shares-temp-fix-for-firewalls-stuck-in-reboot-loop/
+ Date: 2022-01-21T06:36:25-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/04/29/Sonicwall.jpg)

![SonicWall](https://www.bleepstatic.com/content/hl-images/2021/04/29/Sonicwall.jpg)


Following a stream of customer reports that started yesterday evening, security hardware manufacturer SonicWall has provided a temporary workaround for reviving next-gen firewalls running SonicOS 7.0 stuck in a reboot loop.


SonicWall's [Gen7 firewalls](https://www.sonicwall.com/products/firewalls/gen-7/) are the company's newest firewall devices providing users with encrypted traffic inspection, malware analysis, and cloud app security capabilities.


Gen7 models include TZ series firewalls for SMBs and branches, NSa series firewalls for mid-sized enterprises, NSsp series firewalls for large enterprises, data centers, and service providers, and NSv series virtual firewalls.


"If you have noticed the firewall has been stuck at a reboot loop starting from 9:30 PM EST ON 20 Jan 2022 onwards," SonicWall [said](https://www.sonicwall.com/support/knowledge-base/gen7-firewall-inaccessible-reboot-loop-from-20th-jan-2022/220121010044507/) in an advisory published today.


Based on complaints shared by admins online [[1](https://www.reddit.com/r/sonicwall/comments/s90sb3/is_something_going_on_right_now/), [2](https://www.reddit.com/r/sysadmin/comments/s93kv3/sonicwall_gen_7_outage/), [3](https://www.reddit.com/r/sysadmin/comments/s953vp/for_those_having_gen7_sonicwall_boot_looping/)], the issue is widespread and affects devices from all Gen7 firewall series.


Workaround available
--------------------


Until a patch is released to address this bug, SonicWall has provided a temporary fix that requires admins to disable incremental updates to IDP, GAV, and SPY signature databases from the internal Diag menu.


The procedure needed to stop affected SonicWall firewalls from continuously rebooting requires you to go through the following steps:


1. Unplug the WAN connection (If you are unable to login to the firewall)
2. Login to the firewall from the LAN
3. Navigate to The Diag page. This can be reached by typing in the LAN IP of the SonicWall in the browser, with a IP/sonicui/7/m/mgmt/settings/diag at the end. (EXAMPLE: 192.168.168.168/sonicui/7/m/mgmt/settings/diag)
4. Click on internal settings to access the internal settings page or diag page. Please search for the option "Enable Incremental updates to IDP, GAV, and SPY signature databases"  

DISABLE (Uncheck) this setting and select ACCEPT. It is important to select Accept for the setting to take effect.  
![SonicWall incremental updates option](https://www.bleepstatic.com/images/news/u/1109292/2022/SonicWall%20incremental%20updates%20option.png)
5. Plug the WAN Connection and restart the firewall.
6. Monitor the firewall if this addresses the issue else reach out to support for further assistance.

While SonicWall didn't explain what was causing the issue, admins who had to fix the problem on their end [say](https://www.reddit.com/r/sysadmin/comments/s93kv3/sonicwall_gen_7_outage/htkbv9f/) that it has to do with "with security service licensing, unable to phone home or something as long as the WAN is plugged in."


Earlier this month, SonicWall also confirmed that some of its [Email Security and firewall products have been hit by the Y2K22 bug](https://www.bleepingcomputer.com/news/security/sonicwall-y2k22-bug-hits-email-security-firewall-products/), leading to message log updates and junk box failures starting with January 1, 2022.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Sonicwall]] [[Firewalls]] [[Gen7]] [[Admins]] [[Bleeping Computer]]
#### ipv4-adresses
192.168.168.168

