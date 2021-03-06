# Microsoft: We've switched off this 'critical' MSIX protocol handler but we're working to bring it back | ZDNet
### But disabling the protocol has also made it harder for enterprise organizations to distribute apps from a web page.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/microsoft-weve-switched-off-this-critical-msix-protocol-handler-but-were-working-to-bring-it-back/
+ Date: 2022-02-07 14:43:23
+ Author: Liam Tung


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/4d6efe55c71ac9e4a8a686519ae71817dfddff45/2021/11/16/7c0cdc25-9d34-4c8b-958a-14ae16877a83/the-hands-of-a-computer-hacker-over-a-keyboard.jpg?width=770&height=578&fit=crop&auto=webp)

Microsoft has disabled a Windows App Installer feature after its December Patch Tuesday disclosure that it was being actively exploited to install unwanted apps.   

The flaw was bad news for Windows domains, with Microsoft [confirming that attackers were using this vulnerability](https://www.zdnet.com/article/microsoft-december-2021-patch-tuesday-zero-day-exploited-to-spread-emotet-malware/) to install specially crafted packages and spread the Emotet/Trickbot/Bazaloader malware families. 

The Windows AppX Installer is a Windows 10 feature that allows users to install .appx packages. 

In a blogpost explaining why it's switched off the ms-appinstaller protocol for the MSIX Windows app package format, Microsoft says that an attacker can use that protocol to "spoof App Installer to install a package that the user did not intend to install". 

For now, it appears Microsoft hasn't fully addressed the vulnerability detailed in its December [advisory for CVE-2021-43890](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43890). With  protocol disabled, admins could see the download size for some app packages grow, and create a block for for enterprises that distribute apps directly from a web page versus, say, the Microsoft Store. 

"We are actively working to address this vulnerability," [Microsoft says in a blogpost](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/disabling-the-msix-ms-appinstaller-protocol-handler/ba-p/3119479). "For now, we have disabled the ms-appinstaller scheme (protocol). This means that App Installer will not be able to install an app directly from a web server. Instead, users will need to first download the app to their device, and then install the package with App Installer. This may increase the download size for some packages."

As Microsoft explains, [MSIX brings](https://docs.microsoft.com/en-us/windows/msix/overview) a "modern packaging experience" to legacy Windows apps. "The MSIX package format preserves the functionality of existing app packages and/or install files in addition to enabling new, modern packaging and deployment features to Win32, WPF, and Windows Forms apps," Microsoft notes. 






Microsoft has also [updated its page for installing Windows 10 apps from a web page](https://docs.microsoft.com/en-gb/windows/msix/app-installer/installing-windows10-apps-web) to reflect ms-appinstaller being disabled.

Microsoft has a few workarounds in mind until it is able to re-enable the protocol, including "looking into introducing a Group Policy that would allow IT administrators to re-enable the protocol and control usage of it within their organizations." 

But it notes: "We recognize that this feature is critical for many enterprise organizations. We are taking the time to conduct thorough testing to ensure that re-enabling the protocol can be done in a secure manner." 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Emotet]] [[action.malware.name=Tor]] [[action.malware.name=TrickBot]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[Apps]] [[Ms-appinstaller]] [[Msix]] [[ZDNet]]
#### CVE's
[[CVE-2021-43890]]

