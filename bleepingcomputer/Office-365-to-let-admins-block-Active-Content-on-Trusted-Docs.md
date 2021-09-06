# Office 365 to let admins block Active Content on Trusted Docs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/office-365-to-let-admins-block-active-content-on-trusted-docs/)
+ Date: September 5, 2021
+ Author: Sergiu Gatlan


## Article:
![Office 365 to let admins block Active Content on Trusted Docs](https://www.bleepstatic.com/content/hl-images/2020/10/15/Office--365-headpic.jpg)


Microsoft plans to allow Office 365 admins ensure that end-users can't ignore organization-wide policies set up to block active content on Trusted Documents.


Redmond says trusted docs are files with active content (e.g., ActiveX controls, macros, and Dynamic Data Exchange (DDE) functions that don't require user interaction) that open without warnings after the content has been enabled.



[Trusted documents](https://support.microsoft.com/en-us/topic/trusted-documents-cf872bd8-47ec-4c02-baa5-1fdba1a11b53) will automatically open without prompts even if altered by adding new (potentially malicious) active content, bypassing Office's [Protected View](https://support.microsoft.com/en-us/topic/what-is-protected-view-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653), which opens files from potentially unsafe locations as read-only.


"However, the prompt appears if the file was moved since you last trusted the file. After a document is trusted, it does not open in Protected View. Therefore, you should trust documents only if you trust the source of the file," Microsoft explains.


Part of an ongoing Office security hardening effort
---------------------------------------------------


"We are changing the behavior of Office applications to enforce policies that block Active Content (ex. macros, ActiveX, DDE) on Trusted Documents," Microsoft said on the Microsoft 365 Roadmap.


"Previously, Active Content was allowed to run in Trusted Documents even when an IT administrator had set a policy to block it."


As part of an ongoing effort towards Office security hardening, the IT administrators' choice to block Active Content even for trusted files will now always take precedence over the user's choice to trust a document.


This would translate in all documents with embedded active content being opened in Protected View, despite a user's willingness to ignore security warnings reminding them that all active content has been disabled.


Microsoft plans to roll out this new feature by the end of October, making it generally available worldwide in all environments.



![Office 'Enable Content' prompt](https://www.bleepstatic.com/images/news/u/1109292/2021/Office%20Enable%20Content%20prompt.jpg)*Office 'Enable Content' prompt (Microsoft)*
In related news, Redmond is also updating Defender for Office 365 to [protect users from embedded email threats](https://www.bleepingcomputer.com/news/microsoft/microsoft-will-add-secure-preview-for-office-365-quarantined-emails/) when previewing quarantined emails.


In May, Microsoft [updated the security baseline for Microsoft 365 Apps for enterprise](https://www.bleepingcomputer.com/news/security/office-365-security-baseline-adds-macro-signing-jscript-protection/) (formerly Office 365 Professional Plus) to protect from unsigned macros and JScript code execution attacks.


In March, it also [added XLM macro protection](https://www.bleepingcomputer.com/news/security/microsoft-office-365-gets-protection-against-malicious-xlm-macros/) for Microsoft 365 customers to block malware abusing Office VBA macros and PowerShell, JScript, VBScript, MSHTA/Jscript9, WMI, or .NET code, which are regularly used to deploy malicious payloads via Office document macros.




#### Tags:
[[Microsoft]] [[Bleeping Computer]]
