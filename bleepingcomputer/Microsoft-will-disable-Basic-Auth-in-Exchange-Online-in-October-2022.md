# Microsoft will disable Basic Auth in Exchange Online in October 2022
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/microsoft-will-disable-basic-auth-in-exchange-online-in-october-2022/)
+ Date: September 26, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft will disable Basic Auth in Exchange Online in October 2022](https://www.bleepstatic.com/content/hl-images/2021/08/23/Microsoft-Exchange.jpg)


Microsoft announced that Basic Authentication will be turned off for all protocols in all tenants starting October 1st, 2022, to protect millions of Exchange Online users.


This announcement comes after the company postponed the removal of Basic Authentication from Exchange Online until the second half of 2021 because of the COVID-19 pandemic.


"Today, we are announcing that, effective October 1, 2022, we will begin to permanently disable Basic Auth in all tenants, regardless of usage (with the exception of SMTP Auth, which can still be re-enabled after that)," the Exchange Online Team [said](https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-and-exchange-online-september-2021-update/ba-p/2772210) earlier this week.


Microsoft already began disabling basic auth [in June](https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-and-exchange-online-june-2021-update/bc-p/2599824#M31057) for tenants who weren't using it and also explained how customers could re-enable protocols inadvertently affected.


To disable Basic Authentication in Exchange Online before Microsoft fully decommissions it, you need to create and assign auth policies to individual users using the steps detailed on the [Exchange Online support website](https://docs.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/disable-basic-authentication-in-exchange-online).


"Disabling Basic Authentication and requiring Modern Authentication with MFA is one of the best things you can do to improve the security of data in your tenant, and that has to be a good thing," Microsoft said two years ago when it [revealed modern auth will be enforced across Exchange Online tenants](https://www.bleepingcomputer.com/news/security/microsoft-to-force-modern-auth-in-exchange-online-to-enhance-security/).


"The last thing to make clear - this change only affects Exchange Online, we are not changing anything in the Exchange Server on-premises products."


Why is basic auth being disabled?
---------------------------------


While Microsoft did not provide the exact reason why they decided to make this announcement this week, the cause is likely a Guardicore report that revealed how [hundreds of thousands of Windows domain credentials were leaked in plain text](https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-autodiscover-bugs-leak-100k-windows-credentials/) by misconfigured email clients using basic auth.


Amit Serper, Guardicore's AVP of Security Research who authored the report, also disclosed an attack called the 'The ol' switcheroo' that forces an Exchange client to negotiate in basic authentication.




> 
> You're welcome. [pic.twitter.com/9JwhCfa8IF](https://t.co/9JwhCfa8IF)
> 
> 
> — Amit Serper (@0xAmit) [September 24, 2021](https://twitter.com/0xAmit/status/1441395084239454210?ref_src=twsrc%5Etfw)


Basic Authentication (also known as proxy authentication) is an HTTP-based authentication scheme through which apps send credentials with every connection request made to servers, endpoints, or online services, with the username/password pairs often stored locally on the device.


While it dramatically simplifies the authentication process, basic auth also makes it easier for attackers to steal the credentials when the connections are not secured using the Transport Layer Security (TLS) cryptographic protocol.


To make things even worse, enabling multi-factor authentication (MFA) is not easy when using basic auth; therefore, it often isn't used at all.


Modern Authentication (Active Directory Authentication Library (ADAL) and OAuth 2.0 token-based authentication) allows apps to use OAuth access tokens with a limited lifetime and can't be re-used to authenticate on other resources besides those that they were issued for.


After modern auth is toggled on, enabling and enforcing MFA will become more straightforward, with improved data security in Exchange Online as a direct and immediate result.


A demo video on adding MFA to Exchange Online/on-premises mailboxes is available on the [Microsoft Ignite YouTube account](https://www.youtube.com/watch?v=7hoEmEwV8Rk).




#### Tags:
[[Microsoft]] [[MFA]] [[Bleeping Computer]]
