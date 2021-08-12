# Microsoft to require admin rights before using Windows Point and Print feature
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-to-require-admin-rights-before-using-windows-point-and-print-feature/)
+ Date: August 10, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft to require admin rights before using Windows Point and Print feature](https://therecord.media/wp-content/uploads/2021/08/Microsoft-Windows-Update.jpg)

**Microsoft has released today a security update that will change the default behavior of the “Point and Print” feature to mitigate a severe security issue disclosed last month.**


First added in Windows 2000, the [Point and Print](https://docs.microsoft.com/en-us/windows-hardware/drivers/print/introduction-to-point-and-print) feature works by connecting to a print server to download and install necessary print drivers every time a user creates a connection to a remote printer without providing installation media.


Earlier this year, [Jacob Baines](https://twitter.com/Junior_Baines/), a reverse engineer for Dark Wolf Solutions (currently at Dragos), found that threat actors inside a company’s network could abuse the Point and Print feature to run a malicious print server and force Windows systems to download and install malicious drivers.


Since Point and Print ran with SYSTEM privileges, the feature effectively provided threat actors with an easy way to gain admin rights inside any large corporate or government network.


### Desperate times call for desperate measures


Microsoft initially tried to patch the issue—tracked as [CVE-2021-34481](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-34481)—last month, but the patches were deemed incomplete.


Today, the company took another approach. Since the vulnerability is exploiting a design flaw, Microsoft chose today to change the default behavior of the Point and Print feature.


While until now, any user could add a new printer to a Windows computer, Microsoft says that after today’s Patch Tuesday, only admin users will be able to add or update a printer with drivers from a remote print server.


“This change will take effect with the installation of the security updates released on August 10, 2021, for all supported versions of Windows,” [Microsoft said today](https://msrc-blog.microsoft.com/2021/08/10/point-and-print-default-behavior-change/).


“This change may impact Windows print clients in scenarios where non-elevated users were previously able to add or update printers. However, **we strongly believe that the security risk justifies this change**,” the OS maker added.


For companies and users who don’t want to block printer installations inside their networks, Microsoft has also provided a registry key to continue allowing the old behavior, with the registry key detailed [here](https://support.microsoft.com/en-us/topic/873642bf-2634-49c5-a23b-6d8e9a302872). However, Microsoft also warns of the risks:



> Disabling this mitigation will expose your environment to the publicly known vulnerabilities in the Windows Print Spooler service and we recommend administrators assess their security needs before assuming this risk.
> 
> Microsoft Security Response Center


While today’s mitigation came after Baines’ discovery, Microsoft also hopes that this change in the Point and Print feature will also help prevent other attacks against the Print Spooler service, which after a year of various bug disclosures ([PrintNightmare](https://therecord.media/poc-released-for-dangerous-windows-printnightmare-bug/), [PrintDemon](https://windows-internals.com/printdemon-cve-2020-1048/), [FaxHell](https://windows-internals.com/faxing-your-way-to-system/), [Evil Printer](https://media.defcon.org/DEF%20CON%2028/DEF%20CON%20Safe%20Mode%20presentations/DEF%20CON%20Safe%20Mode%20-%20Zhipeng-Huo%20and%20Chuanda-Ding%20-%20Evil%20Printer%20How%20to%20Hack%20Windows%20Machines%20with%20Printing%20Protocol.pdf), and [CVE-2020-1337](https://voidsec.com/cve-2020-1337-printdemon-is-dead-long-live-printdemon/)) is now looking like Swiss cheese.


### Baines presented his findings at Def Con


Baines, who recently presented details about the Point and Print CVE-2021-34481 bug at the Def Con security conference, also released a tool called [Concealed Position](https://github.com/jacob-baines/concealed_position/) that can be used to test networks for his attack method.


The researcher’s Def Con talk is embedded below:








#### Tags:
[[Microsoft]] [[Windows]] [[The Record]]
