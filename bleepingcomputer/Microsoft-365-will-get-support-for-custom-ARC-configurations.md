# Microsoft 365 will get support for custom ARC configurations
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-365-will-get-support-for-custom-arc-configurations/)
+ Date: October 24, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft 365 will get support for custom ARC configurations](https://www.bleepstatic.com/content/hl-images/2021/10/22/Microsoft_365.jpg)


Microsoft is working on adding custom Authenticated Received Chain (ARC) configuration support to Microsoft Defender for Office 365.


[ARC](https://tools.ietf.org/html/rfc8617) is an authentication mechanism that provides an authenticated "chain of custody" for messages that allows all intermediaries handling an email between the originating server to the recipient mailbox to see what other entities handled it previously.






Enabling ARC for Office 365 hosted mailboxes prevents email authentication results from failing due to modifications made during the routing by intermediaries such as forwarding rules or mailing lists, before reaching a recipient's inbox. Thus, email  authentication assessment results are preserved at each step during the delivery process across intermediaries.


"Email senders use authentication mechanisms like SPF, DKIM, DMARC to authenticate emails, but some legitimate intermediate services may potentially make changes to the email, which might cause the email to fail authentication at subsequent hop," Microsoft [explains](https://www.microsoft.com/microsoft-365/roadmap?featureid=85684) on the Microsoft 365 roadmap.


"With this change, admins will be able to add trusted intermediaries in the Microsoft 365 Defender portal to allow Microsoft to honor these ARC signatures, thereby allowing legitimate messages."


Being able to customize ARC configurations to include additional trusted intermediaries enables them to alter messages with attribution and links their signatures to their domain name, thus keeping the ARC chains intact.


Microsoft estimates that this new feature will be generally available worldwide on web platforms next year, starting in March 2022.


Improving anti-spoofing detection since 2019
--------------------------------------------


ARC supplements the [DMARC](https://tools.ietf.org/html/rfc7489) and [DKIM](https://tools.ietf.org/html/rfc4871) email authentication protocols as part of Internet Mail Handlers' ongoing effort to combat email spoofing, especially when dealing with forwarded messages.


DMARC.org [announced ARC](https://dmarc.org/2015/10/global-mailbox-providers-deploying-dmarc-to-protect-users/) in 2015, IETF's DMARC Working Group adopted it as an official work item in June 2016, and published [the specification](https://www.rfc-editor.org/info/rfc8617) three years later, in July 2019.


Microsoft [enabled ARC](https://www.bleepingcomputer.com/news/microsoft/office-365-enables-arc-for-enhanced-anti-spoofing-detection/) for all Office 365 hosted mailboxes three months later, in October 2019, to improve anti-spoofing detection within Office 365.


Redmond also announced earlier in 2021 that Defender for Office 365 would make it easier for security teams to [identify users and domains targeted in impersonation-based phishing attacks](https://www.bleepingcomputer.com/news/security/office-365-will-help-admins-find-impersonation-attack-targets/).


Office 365 customers will also be notified by Defender for Office 365 of [suspected nation-state hacking activity](https://www.bleepingcomputer.com/news/security/microsoft-to-alert-office-365-users-of-nation-state-hacking-activity/) detected within their tenants.




#### Tags:
[[Microsoft]] [[DMARC]] [[Bleeping Computer]]
