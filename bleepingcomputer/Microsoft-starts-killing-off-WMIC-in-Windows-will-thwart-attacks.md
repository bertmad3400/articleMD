# Microsoft starts killing off WMIC in Windows, will thwart attacks
### Microsoft is moving forward with removing the Windows Management Instrumentation Command-line (WMIC) tool, wmic.exe, starting with the latest Windows 11 preview builds in the Dev channel.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-starts-killing-off-wmic-in-windows-will-thwart-attacks/
+ Date: 2022-02-10 20:44:01+00:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/05/26/Microsoft-Defender.jpg)

![Windows shield](https://www.bleepstatic.com/content/hl-images/2021/05/26/Microsoft-Defender.jpg)


Microsoft is moving forward with removing the Windows Management Instrumentation Command-line (WMIC) tool, wmic.exe, starting with the latest Windows 11 preview builds in the Dev channel.


WMIC.exe is a built-in Microsoft program that allows command-line access to the Windows Management Instrumentation.


Using this tool, administrators can query the operating system for detailed information about installed hardware and Windows settings, run management tasks, and even execute other programs or commands.


Microsoft announced last year that they had begun deprecating wmic.exe in Windows Server in favor of Windows PowerShell, which also includes the ability to query Windows Management Instrumentation.


"The WMIC tool is deprecated in Windows 10, version 21H1 and the 21H1 General Availability Channel release of Windows Server. This tool is superseded by [Windows PowerShell for WMI](https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/07-working-with-wmi)," explains the list of [deprecated Window features](https://docs.microsoft.com/en-us/windows/deployment/planning/windows-10-deprecated-features).


"Note: This deprecation only applies to the [command-line management tool](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic). WMI itself is not affected."


As first noted by security researcher [Grzegorz Tworek](https://twitter.com/0gtweet/status/1491340578810114054), Microsoft has now begun removing WMIC from Windows clients, starting with Windows 11 preview builds in the Dev channel.



![WMIC.exe removed from Windows 11 'Dev' preview builds](https://www.bleepstatic.com/images/news/Microsoft/windows-11/w/wmic-deprecation/wmic-deprecated-in-windows-11.jpg)**WMIC.exe removed from Windows 11 'Dev' preview builds**
BleepingComputer has independently confirmed that from at least build 22523 and later, WMIC is no longer available in Windows 11 preview builds in the 'Dev' channel, but Microsoft could have removed it in earlier builds.


We will likely see Microsoft expanding the deprecation of WMIC.exe to Windows 11 general release and possibly Windows 10 in the future.


While the removal of WMIC.exe may cause some of your scripts or daily administration tasks to no longer function, you can easily port these tasks to PowerShell.


WMIC is commonly abused by threat actors
----------------------------------------


In Windows systems, LoLBins (living-off-the-land binaries) are Microsoft-signed executables that threat actors abuse to evade detection while performing malicious tasks.


Some legitimate Windows tools abused by threat actors include but are not limited to [Microsoft Defender](https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-can-ironically-be-used-to-download-malware/), [Windows Update](https://www.bleepingcomputer.com/news/security/windows-update-can-be-abused-to-execute-malicious-programs/), [CertUtil](https://www.bleepingcomputer.com/news/security/certutilexe-could-allow-attackers-to-download-malware-while-bypassing-av/), and even the [Windows Finger command](https://www.bleepingcomputer.com/news/security/windows-finger-command-abused-by-phishing-to-download-malware/).


WMIC.exe has long [been considered a LOLBIN](https://lolbas-project.github.io/) as it is abused by threat actors for a wide range of malicious activities.


For example, ransomware encryptors commonly use the WMIC command to delete Shadow Volume Copies so that victims can't use them to recover files.



```
WMIC.exe shadowcopy delete /nointeractive
```

Other threat actors have used WMIC to query for the [list of installed antivirus software](https://www.bleepingcomputer.com/news/security/gootkit-malware-bypasses-windows-defender-by-setting-path-exclusions/) and [even uninstall them](https://www.bleepingcomputer.com/news/security/the-avcrypt-ransomware-tries-to-uninstall-your-av-software/).



```
WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get displayName,productState /format:list

wmic product where ( Vendor like "%Emsisoft%" ) call uninstall /nointeractive & shutdown /a & shutdown /a & shutdown /a;
```

Other malware has been seen [using WMIC to add exclusions to Microsoft Defender](https://www.bleepingcomputer.com/news/security/iobit-forums-hacked-to-spread-ransomware-to-its-members/) so that their malware won't be detected when launched.



```
WMIC /Namespace:\\root\Microsoft\Windows\Defender class MSFT_MpPreference call Add ExclusionPath=\"
WMIC /Namespace:\\root\Microsoft\Windows\Defender class MSFT_MpPreference call Add ExclusionPath=\"\Temp\\"
WMIC /Namespace:\\root\Microsoft\Windows\Defender class MSFT_MpPreference call Add ExclusionExtension=\".dll\"
WMIC /Namespace:\\root\Microsoft\Windows\Defender class MSFT_MpPreference call Add ExclusionProcess=\"rundll32.exe\"
```

A [phishing campaign recently used CSV files](https://www.bleepingcomputer.com/news/security/malicious-csv-text-files-used-to-install-bazarbackdoor-malware/) to infect devices with the used WMIC to launch a PowerShell command that downloads and installs the BazarBackdoor malware.



![CSV file using WMIC command to launch PowerShell](https://www.bleepstatic.com/images/news/malware/b/bazaloader/csv-file/malicious-csv-file.jpg)**CSV file using WMIC command to launch PowerShell**  
*Source: BleepingComputer*
By removing WMIC, a wide range of malware and attacks will no longer work correctly as they will not be able to execute various commands needed to conduct their attack.


Furthermore, BleepingComputer has seen ransomware strains that relied on WMIC to look up CPU information, and, when they could not do so, they failed to run correctly.


Unfortunately, threat actors will just see this as a bump in the road and replace WMIC with other methods, but disruption, even for a short time, is worth it.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Bazar]] [[action.malware.name=certutil]] [[action.malware.name=Expand]] [[action.malware.name=Orz]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Wmic]] [[Microsoft]] [[Wmic.exe]] [[Powershell]] [[Malware]] [[Namespace:\\root\microsoft\windows\defender]] [[Msft_mppreference]] [[Bleepingcomputer]] [[Bleeping Computer]]

