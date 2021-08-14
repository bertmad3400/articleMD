# GitHub deprecates account passwords for authenticating Git operations
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/github-deprecates-account-passwords-for-authenticating-git-operations/)
+ Date: August 12, 2021
+ Author: Sergiu Gatlan


## Article:
![GitHub deprecates account passwords for authenticating Git operations](https://www.bleepstatic.com/content/hl-images/2021/05/10/GitHub-headpic.jpg)


GitHub has announced today that account passwords will no longer be accepted for authenticating Git operations starting tomorrow.


This change was [first announced last year](https://github.blog/2020-07-30-token-authentication-requirements-for-api-and-git-operations/), in July, when GitHub said that authenticated Git operations would require using an SSH key or token-based authentication.



GitHub also deprecated password-based authentication for authenticating via the REST API beginning with November 13, 2020.


"Starting on August 13, 2021, at 09:00 PST, we will no longer accept account passwords when authenticating Git operations on GitHub.com," the company [said](https://github.blog/changelog/2021-08-12-git-password-authentication-is-shutting-down/).


"Instead, token-based authentication (for example, personal access, OAuth, SSH Key, or GitHub App installation token) will be required for all authenticated Git operations."


If you're still using a username and password to authenticate Git operations, you should take the following steps to avoid disruption when the new requirements are enacted tomorrow:


1. For developers, if you are using a password to authenticate Git operations with GitHub.com today, you must begin using [a personal access token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token) over HTTPS (recommended) or SSH key by August 13, 2021, to avoid disruption. If you receive a warning that you are using an outdated third-party integration, you should update your client to the latest version.
2. For integrators, you must authenticate integrations using the web or [device authorization](https://github.blog/changelog/2020-07-27-oauth-2-0-device-authorization-flow/) flows by August 13, 2021, to avoid disruption. For more information, see [Authorizing OAuth Apps](https://docs.github.com/en/developers/apps/authorizing-oauth-apps) and [the announcement on the developer blog](https://developer.github.com/changes/2020-02-14-deprecating-password-auth/).


If you want to ensure that you're no longer using password-based authentication, you can [enable two-factor authentication](https://help.github.com/en/github/authenticating-to-github/configuring-two-factor-authentication), which requires OAuth or personal access tokens for all authenticated operations via Git and third-party integrations.


If you already have two-factor authentication enabled for your GitHub account, you will **not** be affected by this authentication change in any way since you're already using token- or SSH-based authentication.


GitHub has improved account security over the years by adding [two-factor authentication](https://github.blog/2013-09-03-two-factor-authentication/), [sign-in alerts](https://github.blog/changelog/2018-11-27-unrecognized-location-sign-in-notifications/), [verified devices](https://github.blog/changelog/2019-07-01-verified-devices/), [blocking the use of compromised passwords](https://github.blog/changelog/2018-07-31-new-improvements-and-best-practices-for-account-security-and-recoverability/), and [WebAuthn support](https://github.blog/2019-08-21-github-supports-webauthn-for-security-keys/).


The enforced token-based authentication for authenticating Git operations increases GitHub accounts' resilience against takeover attempts by preventing attackers from using stolen credentials or reused passwords to hijack accounts.


In May, GitHub also added support for [securing SSH Git operations using FIDO2 security keys](https://www.bleepingcomputer.com/news/security/github-now-supports-security-keys-when-using-git-over-ssh/) for added protection from takeover attempts.




#### Tags:
[[GitHub]] [[SSH]] [[token-based]] [[authentication,]] [[two-factor]] [[Bleeping Computer]]
