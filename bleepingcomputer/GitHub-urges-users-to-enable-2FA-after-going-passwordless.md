# GitHub urges users to enable 2FA after going passwordless
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/github-urges-users-to-enable-2fa-after-going-passwordless/)
+ Date: August 18, 2021
+ Author: Sergiu Gatlan


## Article:
![GitHub urges users to enable 2FA after going passwordless](https://www.bleepstatic.com/content/hl-images/2021/08/18/GitHub.jpg)


 


GitHub urges its user base to toggle on two-factor authentication (2FA) after deprecating password-based authentication for Git operations.


"If you have not done so already, please take this moment to [enable 2FA](https://docs.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication) for your GitHub account," the company's Chief Security Officer Mike Hanley said.


"The benefits of multifactor authentication are widely documented and protect against a wide range of attacks, such as phishing."


Hanley recommends using one of several 2FA options available on GitHub, including physical security keys, virtual security keys built into devices such as phones and laptops, or Time-based One-Time Password (TOTP) authenticator apps.


While SMS-based 2FA is also available, GitHub urges users to choose security keys or TOTPs wherever possible since SMS is less secure given that threat actors can bypass or steal SMS 2FA auth tokens.


GitHub also provides a step-by-step video guide on how you can enable your security key for SSH keys and Git commit verification.



Why is 2FA important?
---------------------


Enforcing passwordless authentication via Git operations is important because it increases GitHub accounts' resilience against takeover attempts by preventing attackers' attempts to use stolen credentials or reused passwords to hijack accounts.


As Alex Weinert, Microsoft's Director of Identity Security, [said](https://techcommunity.microsoft.com/t5/Azure-Active-Directory-Identity/Your-Pa-word-doesn-t-matter/ba-p/731984/?/en-US/index.html) a couple of years ago, "your password doesn't matter, but MFA does! Based on our studies, your account is more than 99.9% less likely to be compromised if you use MFA."


Weinert also [added](https://www.bleepingcomputer.com/news/security/57-percent-of-businesses-use-multi-factor-auth-mfa-says-lastpass/techcommunity.microsoft.com/t5/Azure-Active-Directory-Identity/All-your-creds-are-belong-to-us/ba-p/855124?/en-US/index.html) that the "use of anything beyond the password significantly increases the costs for attackers, which is why the rate of compromise of accounts using any type of MFA is less than 0.1% of the general population."


Google researchers also [commented](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html?/en-US/index.html) that "simply adding a recovery phone number to your Google Account can block up to 100% of automated bots, 99% of bulk phishing attacks, and 66% of targeted attacks."


At the same time, "zero users that exclusively use security keys fell victim to targeted phishing."


GitHub's efforts to secure users' accounts
------------------------------------------


GitHub [reminded users last week](https://www.bleepingcomputer.com/news/security/github-deprecates-account-passwords-for-authenticating-git-operations/) that account passwords will no longer be accepted for authenticating Git operations starting with August 13.


The change was [first announced in July 2020](https://github.blog/2020-07-30-token-authentication-requirements-for-api-and-git-operations/) when GitHub said that authenticated Git operations would require using SSH key or token-based authentication.


GitHub also disabled password authentication via the REST API in November 2020 and added support for [securing SSH Git operations using FIDO2 security keys](https://www.bleepingcomputer.com/news/security/github-now-supports-security-keys-when-using-git-over-ssh/) in May 2021.


Account security was also improved over the years by adding [two-factor authentication](https://github.blog/2013-09-03-two-factor-authentication/), [sign-in alerts](https://github.blog/changelog/2018-11-27-unrecognized-location-sign-in-notifications/), [verified devices](https://github.blog/changelog/2019-07-01-verified-devices/), [blocking the use of compromised passwords](https://github.blog/changelog/2018-07-31-new-improvements-and-best-practices-for-account-security-and-recoverability/), and [WebAuthn support](https://github.blog/2019-08-21-github-supports-webauthn-for-security-keys/).




#### Tags:
[[GitHub]] [[2FA]] [[SSH]] [[Bleeping Computer]]
