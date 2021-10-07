# Microsoft is disabling Excel 4.0 macros by default to protect users
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-is-disabling-excel-40-macros-by-default-to-protect-users/)
+ Date: October 7, 2021
+ Author: Lawrence Abrams


## Article:
![Excel](https://www.bleepstatic.com/content/hl-images/2021/03/19/excel-header.jpg)


​Microsoft will soon begin disabling Excel 4.0 XLM macros by default in Microsoft 365 tenants to protect customers from malicious documents.


Excel 4.0 macros, or XLM macros, were first added to Excel in 1992 and allowed users to enter various commands into cells that are then executed to perform a task.



![Malicioux XLS document with obfuscated Excel 4.0 macro](https://www.bleepstatic.com/images/news/Microsoft/m/microsoft-365/disable-excel-4-macros/malicious-excel_4-document.jpg)**Malicious XLS document with obfuscated Excel 4.0 macro**
While VBA macros were introduced in Excel 5.0, threat actors continue to XLM macros twenty years later in malicious documents that download malware or perform other unwanted behavior.


Malicious campaigns utilizing Excel 4.0 XLM macros include ones for malware, such as [TrickBot](https://twitter.com/h2jazi/status/1331342523462258696), [Qbot](https://twitter.com/elceef/status/1396916046188195849), [Dridex](https://twitter.com/jcarndt/status/1260998505541353472), [Zloader](https://twitter.com/elceef/status/1392177026078056455), and many more.


Due to their continued abuse, Microsoft has been recommending users switch from and disable Excel 4.0 XLM macros for years in favor of VBA macros. This recommendation is because VBA macros support the [Antimalware Scan Interface (AMSI)](https://docs.microsoft.com/en-us/windows/desktop/amsi/antimalware-scan-interface-portal), which can be used by security software to scan macros for malicious behavior.


To disable Excel 4.0 macros, Windows admins can use group policies to disable the feature, and users can disable it via the Excel Trust Center using the ***Enable XLM macros when VBA macros are enabled***setting.



![Enable XLM macros when VBA macros are enabled in Excel Trust Center](https://www.bleepstatic.com/images/news/Microsoft/m/microsoft-365/disable-excel-4-macros/trust-center-setting.jpg)**Enable XLM macros when VBA macros are enabled in Excel Trust Center**
Microsoft to disable Excel 4.0 macros in all tenants
----------------------------------------------------


Instead of waiting for organizations to disable XLM macros on their own, Microsoft announced yesterday that they would be disabling Excel 4.0 macros by default starting in October in preview builds and then moving onto the current channel in November.


"We are introducing a change to the Excel Trust Center Macro settings to provide a more secure experience for users by default. This new default behavior will disable Excel 4.0 macros," explained an advisory in the Microsoft 365 message center.


Microsoft will begin disabling Excel 4.0 macros in all tenants using this rollout schedule:


* Insiders-Slow: will rollout in late October and be complete in early November.
* Current Channel: will rollout in early November and be complete in mid-November.
* Monthly Enterprise Channel (MEC): will begin and complete rollout in mid-December.


Microsoft will not be making any changes for users who have manually configured this setting or configured it via group policies.


When the change rolls out, the ***Enable XLM macros when VBA macros are enabled setting*** will be unchecked by default, which disables XLM macros.


Microsoft states that users who wish to enable XLM macros after this rollout has finished can do so in the Excel Trust Center.


*H/T [Omri Segev Moyal](https://twitter.com/GelosSnake)*




#### Tags:
[[XLM]] [[Microsoft]] [[VBA]] [[macros,]] [[Bleeping Computer]]
