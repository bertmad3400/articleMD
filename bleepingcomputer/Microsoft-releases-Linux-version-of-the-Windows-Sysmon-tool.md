# Microsoft releases Linux version of the Windows Sysmon tool
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-linux-version-of-the-windows-sysmon-tool/)
+ Date: October 14, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft loves Linux header](https://www.bleepstatic.com/content/hl-images/2021/10/14/microsoft-loves-linux-header.jpg)


Microsoft has released a Linux version of the very popular Sysmon system monitoring utility for Windows, allowing Linux administrators to monitor devices for malicious activity. 


For those not familiar with [Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) (aka System Monitor), it is a Sysinternals tool that monitors a system for malicious activity and then logs any detected behavior into system log files.


Sysmon's versatility comes from the ability to create custom configuration files that administrators can use to monitor for specific system events that may indicate malicious activity is occurring on the system.


Sysmon ported to Linux
----------------------


Today, Microsoft's Mark Russinovich and a cofounder of the Sysinternals utility suite, announced that Microsoft had released Sysmon for Linux as an open-source [project on GitHub](https://github.com/Sysinternals/SysmonForLinux).


Unlike Sysmon for Windows, Linux users will be required to compile the program themselves and ensure that they have all the required dependencies, with instructions provided on the project's GitHub page.


It is important to note that to compile Sysmon, you must first also install the [SysinternalsEBPF project](https://github.com/Sysinternals/SysinternalsEBPF).


Once Sysmon is compiled, you can see a help file by typing `sudo ./sysmon -h`, as shown in the screenshot below.



![Sysmon for Linux help file](https://www.bleepstatic.com/images/news/software/s/sysinternals/sysmon/sysmon-for-linux/sysmon-help.jpg)**Sysmon for Linux help file**  
*Source: BleepingComputer*
To use the program, you first need to accept the end-user license agreement with the following command:


Then you can launch Sysmon with or without a configuration file using one of the following commands:


To create your own Sysmon configuration file, you would need to use `./sysmon -s` command to view the current version's configuration schema and see what directives are available.


To learn more about creating a Sysmon configuration file, you can consult the [official documentation](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) or use [SwiftOnSecurity's template](https://github.com/SwiftOnSecurity/sysmon-config/blob/master/sysmonconfig-export.xml) as an example.



![Basic Windows Sysmon config file that enables DNSQuery Logging](https://www.bleepstatic.com/images/news/software/s/sysinternals/sysmon/10-release/enable-dnsquery.jpg)**Basic Windows Sysmon config file that enables DNSQuery Logging**
Once started, Sysmon will begin logging events to the `/var/log/syslog` file. If you did not specify a configuration file to restrict what is logged, you will find that your syslog file quickly grows as new processes are launched and terminated.


For example, in the screenshot below, you can see an event showing the 'adduser' command terminating after I used it to create a new user.



![Sysmon evensts logged to /var/log/syslog](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Sysmon events logged to /var/log/syslog**  
*Source: BleepingComputer*
To make it easier to filter the logs for specific events, you can use the **sysmonLogView** utility to show the events you are looking for.


The current events IDs that Sysmon for Linux is capable of logging are listed below:


* 1: SYSMONEVENT\_CREATE\_PROCESS
* 2: SYSMONEVENT\_FILE\_TIME
* 3: SYSMONEVENT\_NETWORK\_CONNECT
* 4: SYSMONEVENT\_SERVICE\_STATE\_CHANGE
* 5: SYSMONEVENT\_PROCESS\_TERMINATE
* 6: SYSMONEVENT\_DRIVER\_LOAD
* 7: SYSMONEVENT\_IMAGE\_LOAD
* 8: SYSMONEVENT\_CREATE\_REMOTE\_THREAD
* 9: SYSMONEVENT\_RAWACCESS\_READ
* 10: SYSMONEVENT\_ACCESS\_PROCESS
* 11: SYSMONEVENT\_FILE\_CREATE
* 12: SYSMONEVENT\_REG\_KEY
* 13: SYSMONEVENT\_REG\_SETVALUE
* 14: SYSMONEVENT\_REG\_NAME
* 15: SYSMONEVENT\_FILE\_CREATE\_STREAM\_HASH
* 16: SYSMONEVENT\_SERVICE\_CONFIGURATION\_CHANGE
* 17: SYSMONEVENT\_CREATE\_NAMEDPIPE
* 18: SYSMONEVENT\_CONNECT\_NAMEDPIPE
* 19: SYSMONEVENT\_WMI\_FILTER
* 20: SYSMONEVENT\_WMI\_CONSUMER
* 21: SYSMONEVENT\_WMI\_BINDING
* 22: SYSMONEVENT\_DNS\_QUERY
* 23: SYSMONEVENT\_FILE\_DELETE
* 24: SYSMONEVENT\_CLIPBOARD
* 25: SYSMONEVENT\_PROCESS\_IMAGE\_TAMPERING
* 26: SYSMONEVENT\_FILE\_DELETE\_DETECTED
* 255: SYSMONEVENT\_ERROR


As you can see, many of these events do not apply to Linux, such as the Registry or WMI events, so you will need to adjust your configuration accordingly.


Sysmon is a powerful tool widely used in Windows environments as part of an organization's security toolbox.


With its addition to Linux, a whole new segment of system administrators can utilize it to provide free system monitoring for malicious activity.




#### Tags:
[[Sysmon]] [[Linux]] [[Microsoft]] [[Bleeping Computer]]
