# Microsoft releases its Windows 10 November 2021 update
### The big news is that the Windows 10 release cadence is joining Windows 11 and returning to just one feature update a year from now on.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3640973/microsoft-releases-its-windows-10-november-2021-update.html
+ Date: 2021-11-16
+ Author: Lucas Mearian


## Article:
![Article Image](https://images.idgesg.net/images/idge/imported/imageapi/2021/10/22/16/windows-10-fading-100908315-large.jpg?auto=webp&quality=85,70)

Microsoft [today announced the general availability of Windows 10 November 2021](https://blogs.windows.com/windowsexperience/2021/11/16/how-to-get-the-windows-10-november-2021-update/), also known as version 21H2, which includes new security, management, and virtualization features.

Microsoft reiterated that Windows 10 will continue to receive support until October 2025 and said the Windows 10 release cadence will join Windows 11 in returning to just one feature update a year from here on out.

The company also [posted an online comparison](https://www.microsoft.com/en-us/windows/compare-windows-11-home-vs-pro-versions) of the features between the latest version of Windows 10 21H2 and Windows 11.

The catalyst for the change to Windows 10 is its successor, Windows 11, which [debuted Oct. 5](https://www.computerworld.com/article/3635896/microsoft-lets-windows-11-loose-on-the-world.html). Windows 11, which will have its own tweaked servicing model — one feature upgrade annually with 36 months of support due to those running the Enterprise or Education SKUs — will replace the older Windows 10 as the repository of the new.

For IT pros
-----------

Beginning with security, Windows 10 21H2 sees changes to the Universal Windows Platform (UWP) VPN APIs, which includes the ability to implement common web-based authentication schemes and to reuse existing protocols.

Version 21H2 also supports Wi-Fi 6 with Wi-Fi Protected Access 3 Hash-to-Element protocol (WPA3 H2E) to provide better protection from Wi-Fi side-channel attacks that could steal Wi-Fi passwords and other sensitive information.

“In a hybrid work situation, users will now be able to keep their web traffic encrypted when connected to open networks or home networks,” Alan Meeus, a product manager for Windows 10, wrote in [a blog post](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/what-s-new-for-it-pros-in-windows-10-version-21h2/ba-p/2971409).

Windows 10 21H2 also provides security updates for the following products and features: Windows AI Platform, Windows App Platform and Frameworks, Windows Apps, Windows Cryptography, Windows Fundamentals, Windows Input and Composition, Windows Kernel, Windows Media, Windows Office Media, and Windows Virtualization.

Microsoft has also upgraded Windows 10 to enable the provisioning of apps from Azure Virtual Desktop. This allows those apps to run just like local apps, including the ability to copy and paste between remote and local apps. (The functionality is also available in Windows 11.)

In terms of new management features, Microsoft said it worked on closing the gap between Group Policy and mobile device management (MDM) settings. The device configuration settings catalog has been updated to list more than 1,400 settings previously not available for configuration via MDM. The new MDM policies include administrative template (ADMX) policies, such as App Compat, Event Forwarding, Servicing, and Task Scheduler.

(The same changes were made for Windows 11 to enable a consistent policy management experience between the two platforms.)

### Windows 10 Enterprise

An upgrade to Windows 10 Enterprise includes Universal Print, which now supports print jobs of up to 1GB or a series of print jobs from an individual user that add up to 1GB within any 15-minute period.

In addition, Universal Print integrates with OneDrive for web and Excel for web. This allows users of any browser or device connected to the internet to print documents hosted in OneDrive for web to a printer in their organization without installing printer drivers on their devices. Universal Print will also be updated by the end of 2021 to support printing from Microsoft Excel for web.

For organizations with special-purpose devices and environments, such as manufacturing or healthcare systems, or for those who have other needs for longer term device update stability, Microsoft released a new version to the Long-Term Servicing Channel — Long-Term Servicing Channel: Windows 10 Enterprise LTSC 2021.

Windows 10 21H2 is now available through Windows Server Update Services (WSUS) and Windows Update for Business. It can be downloaded from [Visual Studio Subscriptions](https://aex.dev.azure.com/profile/create?account=false&mkt=en-US&reply_to=https%3A%2F%2Fapp.vssps.visualstudio.com%2F_signedin%3Frealm%3Dmy.visualstudio.com%26reply_to%3Dhttps%253A%252F%252Fmy.visualstudio.com%252Fdownloads), the [Software Download Center](https://www.microsoft.com/en-us/software-download/windows10) (via Update Assistant or the Media Creation Tool), and the [Volume Licensing Service Center](https://www.microsoft.com/Licensing/servicecenter/default.aspx)).

### Tool updates

To support the new release, Microsoft has rolled out updated versions of the following tools:

* [Administrative Templates](https://www.microsoft.com/en-us/download/details.aspx?id=103124) (.admx) for Windows 10 21H2 – While natively   
accessible via the C:\Windows\PolicyDefinitions\ folder in Windows, administrative template files can be downloaded separately and used to populate policy settings in the user interface of Group Policy tools, allowing you to manage registry-based policy settings.
* Group Policy settings [reference spreadsheet](https://www.microsoft.com/en-us/download/details.aspx?id=103125) for Windows 10 21H2 – List of the policy settings for computer and user configurations included in the ADMX files delivered for Windows 10, version 21H2.
* Windows 10 Enterprise Evaluation – For IT professionals interested in trying Windows 10 Enterprise on behalf of their organization, Microsoft offers [a free 90-day evaluation](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise) of Windows 10 21H2 and Windows 10 Enterprise LTSC 2021.

Microsoft is also updating resources to manage and deploy updates in an organization, including:

* Windows release [health hub](https://docs.microsoft.com/en-us/windows/release-health/) – The quickest way to stay up to date on update-related news, announcements, and best practices; important lifecycle reminders, and the status of known issues and safeguard holds. Windows 10 Enterprise customers can access greater detail from the Health menu in the Microsoft 365 admin center (see "Windows release health") and receiving important notifications and updates in the Message center.
* Windows 10 [release information](https://docs.microsoft.com/en-us/windows/release-health/release-information) – A list of current Windows 10 versions by servicing options, along with release dates, build numbers, end of service dates, and release history.
* Windows 10 21H2 update history – A list of all updates (monthly and out-of-band) released for Windows 10 21H2, sorted in reverse chronological order. These updates will be available with the first servicing release.

### Additional Updates

* x64 Emulation for Windows on Arm.

Microsoft said it has received questions about the status of x64 emulation in Windows 10. As of now, the update for x64 emulation for Windows is only generally available in Windows 11. For those interested in using x64 emulation, a PC running Windows 11 on Arm is required.

* Microsoft Store

The new [Microsoft Store](https://blogs.windows.com/windowsexperience/2021/06/24/building-a-new-open-microsoft-store-on-windows-11/) started rolling out to Windows 10 PCs on Nov. 10. Microsoft said it rebuilt the store to offer a more modern design and “intuitive search experience to create a more open and profitable environment for developers.”

The November 2021 Update is available initially to users with devices running Windows 10, version 2004 or later available. All editions of Windows 10 2004 will reach end of servicing on Dec. 14, 2021, while Enterprise and Education editions of Windows 10 1909 will reach end of servicing on May 10, 2022. After those dates, devices running versions 1909 and 2004 will no longer receive monthly security and quality updates containing protections from the latest security threats.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Education]] [[victim.industry.name=Healthcare]] [[victim.industry.name=Manufacturing]]

#### Location:
[[victim.city.name=Paris]] [[victim.country.name=France]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[21h2]] [[Wi-fi]] [[Apps]] [[X64]] [[Computerworld]]

