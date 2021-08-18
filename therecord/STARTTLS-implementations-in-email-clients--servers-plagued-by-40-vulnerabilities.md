# STARTTLS implementations in email clients & servers plagued by 40+ vulnerabilities
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/starttls-implementations-in-email-clients-servers-plagued-by-40-vulnerabilities/)
+ Date: August 18, 2021
+ Author: Catalin Cimpanu


## Article:
![STARTTLS implementations in email clients & servers plagued by 40+ vulnerabilities](https://therecord.media/wp-content/uploads/2021/08/nostarttls.png)

A group of German academics said they discovered more than 40 security flaws in the implementation of the STARTTLS feature in today’s most popular email clients and email servers.


Also known as [Opportunistic TLS](https://en.wikipedia.org/wiki/Opportunistic_TLS), **STARTTLS** refers to a set of protocol extensions used by email clients and servers to upgrade older email protocols like POP3, IMAP, and SMTP from sending data via a plaintext connection to a secure TLS-encrypted channel.


Developed in the late 90s, STARTTLS worked by checking if a connection could be set up via TLS and then negotiating the TLS connection with all involved parties before sending the email data.


Although the entire STARTTLS negotiation process was fragile and prone to errors, STARTTLS came at a time when there was no broad support for encrypted connections in email clients and email servers. Lacking better alternatives at the time, most users and servers admins chose to enable STARTTLS as a temporary solution until TLS support got broader adoption across the internet.


Today, things have changed. Almost all major email clients and email servers support a pure TLS-only mode where all old protocols like POP3, IMAP, and SMTP are funneled by default via an encrypted channel that safeguards email communications from tampering or wiretapping, with email clients refusing to send emails if a secure TLS connection can’t be established.


However, there are still millions of email clients and hundreds of thousands of email servers where STARTTLS is supported and still enabled.


### Users advised to move from STARTTLS to TLS-only modes


In a [research project](https://nostarttls.secvuln.info/) presented at the [USENIX 2021 security conference](https://www.usenix.org/conference/usenixsecurity21/presentation/poddebniak) last week, academics said they found more than 40 vulnerabilities in STARTTLS client and server implementations that could be abused to downgrade STARTTLS connections to plaintext forms, intercept email communications, steal passwords, or tamper with email inboxes.


While these attacks required a MitM (Man/Meddler-in-the-Middle) position in order to interact with the STARTTLS initial negotiation process, the research team said that “**these vulnerabilities are so common that we recommend to avoid using STARTTLS when possible**” and that users and administrators should move to update their clients and servers to using TLS-only connections as soon as possible.


![STARTTLS+TLS-options](https://www-therecord.recfut.com/wp-content/uploads/2021/08/STARTTLSTLS-options.png)Thunderbird client connection security settings
The good news is that the researchers have spent the past few months working with email client and server vendors to patch the 40+ vulnerabilities they discovered.


While users have the option to apply these patches and continue using STARTTLS to be safe from attacks, researchers advise that users update their client and server settings and set TLS-only as the default email communication security setting by default, something that other security experts have also been recommending [since 2014](https://www.agwa.name/blog/post/starttls_considered_harmful) already.


Below is a summary of the issues discovered by the research team and the affected email clients and email servers.


### Summary of STARTTLS client vulnerabilities


![STARTTLS-client-list](https://www-therecord.recfut.com/wp-content/uploads/2021/08/STARTTLS-client-list.png)
##### Response Injection (Buffering)




| Product | Protocol | Status | Links |
| --- | --- | --- | --- |
| Apple Mail (macOS) | SMTP/POP3/IMAP | Fixed in macOS High Sierra 10.13.6/Big Sur 11.4 | [CVE-2020-9941](https://nvd.nist.gov/vuln/detail/CVE-2020-9941), [CVE-2021-30696](https://nvd.nist.gov/vuln/detail/CVE-2021-30696) |
| Apple Mail (iOS/iPadOS) | SMTP/POP3/IMAP | Fixed in iOS/iPadOS 14.0 | [CVE-2020-9941](https://nvd.nist.gov/vuln/detail/CVE-2020-9941) |
| Mozilla Thunderbird | IMAP | Fixed in 78.7.0 | [CVE-2020-15685](https://nvd.nist.gov/vuln/detail/CVE-2020-15685), [Vendor advisory](https://www.mozilla.org/en-US/security/advisories/mfsa2021-05/), [Bug report (restricted)](https://bugzilla.mozilla.org/show_bug.cgi?id=1622640) |
| Claws Mail | SMTP/POP3/IMAP | Fixed in 3.17.6 for SMTP/POP3, See libEtPan for IMAP | [CVE-2020-15917](https://nvd.nist.gov/vuln/detail/CVE-2020-15917) |
| Mutt | IMAP/SMTP/POP3 | Fixed in 1.14.4 | [CVE-2020-14954](https://nvd.nist.gov/vuln/detail/CVE-2020-14954) |
| NeoMutt | IMAP/SMPT/POP3 | Fixed in 2020-06-19 | [Commit/Patch](https://github.com/neomutt/neomutt/commit/fb013ec666759cb8a9e294347c7b4c1f597639cc), see also [CVE-2020-14954](https://nvd.nist.gov/vuln/detail/CVE-2020-14954) |
| Evolution | SMTP/POP3 | Fixed in 3.36.4 (evolution-data-server) | [CVE-2020-14928](https://nvd.nist.gov/vuln/detail/CVE-2020-14928) |
| LibEtPan (Mail Framework for C Language) | IMAP/SMTP/POP3 | Fixed in repository, unreleased | [CVE-2020-15953](https://nvd.nist.gov/vuln/detail/CVE-2020-15953) |
| Exim (MTA sending) | SMTP | Unfixed (reported privately) | – |
| Gmail (iOS/iPadOS) | SMTP/IMAP | Unfixed (reported privately) | – |
| Mail.ru, MyMail | SMTP | Unfixed (reported privately, report closed as not applicable) | – |
| Yandex | SMTP/IMAP | Unfixed (reported privately) | – |
| PHP (stream\_socket\_enable\_crypto) | SMTP/POP3/IMAP | Unfixed | [Bug report (private)](https://bugs.php.net/bug.php?id=80008) |


##### Negotiation and Tampering bugs




| Product | Description | Protocol | Status | Links |
| --- | --- | --- | --- | --- |
| Gmail (Android) | Leak of emails | IMAP | Fixed (retested in 2021.07.11.387440246) | – |
| Gmail (Go) | Leak of emails | IMAP | Fixed (retested in 2020.10.15.341102866) | – |
| Samsung Email | Leak of emails | IMAP | Fixed (untested) | – |
| Alpine | Untagged responses accepted before STARTTLS | IMAP | Unknown (reported via email) | – |
| Trojitá | Untagged responses accepted before STARTTLS | IMAP | Unknown | [Bug report](https://bugs.kde.org/show_bug.cgi?id=432353) |
| Mozilla Thunderbird | Server responses prior to STARTTLS processed | IMAP | Fixed in 78.12 | [CVE-2021-29969](https://nvd.nist.gov/vuln/detail/CVE-2021-29969), [Vendor advisory](https://www.mozilla.org/en-US/security/advisories/mfsa2021-30/) |
| KMail | STARTTLS ignored when “Server requires authentication” not checked | SMTP | Unknown | [Bug report](https://bugs.kde.org/show_bug.cgi?id=423423) |
| Sylpheed | STARTTLS stripping | IMAP | Unknown | [Bug report](https://sylpheed.sraoss.jp/redmine/issues/322) |
| OfflineIMAP | STARTTLS stripping | IMAP | Unknown | [Bug report](https://github.com/OfflineIMAP/offlineimap/issues/669) |
| GMX / Web.de Mail Collector | STARTTLS stripping | POP3/IMAP | Fixed | – |
| Mail.ru, MyMail, Email app for Gmail | STARTTLS Stripping | SMTP | Unfixed (report closed as not applicable) | – |


##### Avoiding Encryption via IMAP PREAUTH




| Product | Status | Links |
| --- | --- | --- |
| Apple Mail (iOS/iPadOS) | Reported February 2020, Re-reported August 2021, Unfixed | – |
| Mozilla Thunderbird | Fixed in 68.9.0 | [CVE-2020-12398](https://nvd.nist.gov/vuln/detail/CVE-2020-12398) |
| Alpine | Fixed in 2.23 | [CVE-2020-14929](https://nvd.nist.gov/vuln/detail/CVE-2020-14929), [Commit](https://repo.or.cz/alpine.git/commit/000edd9036b6aea5e6a06900ecd6c58faec665ab) |
| Mutt | Fixed in 1.14.3 | [CVE-2020-14093](https://nvd.nist.gov/vuln/detail/CVE-2020-14093) |
| NeoMutt | Fixed in Release 2020-06-19 | [Commit/Patch](https://github.com/neomutt/neomutt/commit/9909cde1f332d2f641c6aec0eb92adf0a150c7e5), see also [CVE-2020-14093](https://nvd.nist.gov/vuln/detail/CVE-2020-14093) |
| GMX / Web.de Mail Collector | Fixed | – |


##### Certificate Validation




| Product | Protocol | Description | Status | Links |
| --- | --- | --- | --- | --- |
| OfflineIMAP | IMAP | Accepts untrusted certificates | Unknown | [Bug report](https://github.com/OfflineIMAP/offlineimap/issues/669) |
| GMX / Web.de Mail Collector | POP3/IMAP | Accepts untrusted certificates | Still allows self-signed | – |
| Yandex | SMTP/IMAP | Accepts untrusted certificates | Unknown (report closed as not eligible) | – |
| Mail.ru, MyMail | SMTP | Accepts untrusted certificates (SMTP, IMAP) | Unknown (report closed as duplicate) | – |
| Outlook (Android & iOS) | SMTP/IMAP | Certificate hostname not checked (SMTP, IMAP) | Unknown (report closed as low/medium severity) | – |
| Geary | SMTP/IMAP | Accepting an untrusted certificate creates a permanent trust exception for all certificates | Fixed in 3.36.3 | [CVE-2020-24661](https://nvd.nist.gov/vuln/detail/CVE-2020-24661) |
| Trojitá | SMTP | Accepts untrusted certificates | Fixed in repository (77ddd5d4) (no official releases) | [CVE-2020-15047](https://nvd.nist.gov/vuln/detail/CVE-2020-15047) |
| Ruby Net::SMTP | SMTP | Only checks hostname, ignores certificate signature | Fixed in 2.7.2 | [Bug report](https://hackerone.com/reports/980249) |


##### Crashes




| Product | Protocol | Description | Status | Links |
| --- | --- | --- | --- | --- |
| Alpine | IMAP | Crash when LIST or LSUB send before STARTTLS | Unknown (reported via email) | – |
| Balsa | IMAP | Nullptr dereference when TLS required and PREAUTH send | Fixed in 2.5.10 | [CVE-2020-16118](https://nvd.nist.gov/vuln/detail/CVE-2020-16118) |
| Balsa | IMAP | Stack overflow due to repeated BAD answer to CAPABILITY command | Fixed in 2.6.2 (no release yet) | [Bug Report](https://gitlab.gnome.org/GNOME/balsa/-/issues/48) |
| Balsa | IMAP | Crash on untagged EXPUNGE response | Fixed in commit 26e554ac (no release yet) | [Bug Report](https://gitlab.gnome.org/GNOME/balsa/-/issues/54) |
| Evolution | IMAP | Invalid free when no auth mechanisms in greeting | Fixed in >3.35.91 | [CVE-2020-16117](https://nvd.nist.gov/vuln/detail/CVE-2020-16117) |


##### Miscellaneous




| Product | Protocol | Description | Status | Links |
| --- | --- | --- | --- | --- |
| KMail | POP3 | Setup wizard in POP3 defaults to unencrypted connections | Fixed in 20.08 | [Bug Report](https://bugs.kde.org/show_bug.cgi?id=423426) |
| KMail | POP3 | Config shows “encrypted”, but it isn’t | Fixed | [CVE-2020-15954](https://nvd.nist.gov/vuln/detail/CVE-2020-15954) |
| KMail | SMTP/IMAP | Dialog loop “forces” the user to accept invalid certificates | Unknown | [Bug Report](https://bugs.kde.org/show_bug.cgi?id=423424) |
| Mozilla Thunderbird | POP3 | Infinite loop when POP3 server replies with -ERR to STLS command | Unknown | [Bug Report](https://bugzilla.mozilla.org/show_bug.cgi?id=1641882) |
| Trojitá | SMTP/IMAP | Hard to choose implicit TLS due to typo (German) | Fixed | [Bug Report](https://bugs.kde.org/show_bug.cgi?id=416942) |
| Trojitá | SMTP | SMTP defaults to plaintext on port 587 | Unknown | [Bug Report](https://bugs.kde.org/show_bug.cgi?id=432354) |


### Summary of STARTTLS server vulnerabilities


![STARTTLS-server-list](https://www-therecord.recfut.com/wp-content/uploads/2021/08/STARTTLS-server-list.png)
##### Command Injection (Buffering)




| Product | Protocol | Status | Links |
| --- | --- | --- | --- |
| Nemesis (used by GMX / Web.de, provider) | POP3/IMAP | Fixed (reported privately) | – |
| Interia.pl (provider) | SMTP/POP3/IMAP | Fixed (reported privately) | – |
| Yahoo (only MTA-to-MTA, provider) | SMTP | Unfixed (reported privately) | – |
| Yandex (provider) | SMTP/POP3/IMAP | Unfixed (reported privately) | – |
| s/qmail | SMTP | Fixed in 4.0.09 | [CVE-2020-15955](https://nvd.nist.gov/vuln/detail/CVE-2020-15955) |
| Coremail | SMTP/POP3/IMAP | Unfixed (reported via CERT) | – |
| Citadel | SMTP/POP3/IMAP | Unfixed | [CVE-2020-29547](https://nvd.nist.gov/vuln/detail/CVE-2020-29547), [Bug report](https://uncensored.citadel.org/dotgoto?room=Citadel%20Security) |
| Gordano GMS | POP3/IMAP | Unfixed | [CVE-2021-37844](https://nvd.nist.gov/vuln/detail/CVE-2021-37844) |
| recvmail | SMTP | Fixed in 3.1.2 (reported privately) | – |
| SmarterMail | POP3 | Fixed in Build 7537 | [CVE-2020-29548](https://nvd.nist.gov/vuln/detail/CVE-2020-29548) |
| Burp Collaborator | SMTP | Fixed in 2020.9.2 | [Bug report](https://hackerone.com/reports/953219), [Vendor release notes](https://portswigger.net/burp/releases/professional-community-2020-9-2) |
| Dovecot | SMTP | Fixed in 2.3.14.1 and 2.3.15 | [CVE-2021-33515](https://nvd.nist.gov/vuln/detail/CVE-2021-33515) |
| Mercury/32 | SMTP/POP3/IMAP | Fixed in 4.90 | [CVE-2021-33487](https://nvd.nist.gov/vuln/detail/CVE-2021-33487) |
| QMail Toaster (1.4.1) | SMTP | Project discontinued | – |
| Courier | POP3 | Fixed in 1.1.5 (reported privately), known since 2013 | [Discussion from 2013](https://sourceforge.net/p/courier/mailman/courier-imap/thread/525D3389.4080507@csi.uned.es/), [CVE-2021-38084](https://nvd.nist.gov/vuln/detail/CVE-2021-38084), [Fix](https://sourceforge.net/p/courier/mailman/message/37329216/) |
| PHP (stream\_socket\_enable\_crypto) | SMTP/POP3/IMAP | Unfixed | [Bug report (private)](https://bugs.php.net/bug.php?id=80008) |


##### Session Fixation




| Product | Protocol | Status | Links |
| --- | --- | --- | --- |
| Citadel | POP3/IMAP | Reported via forum, unfixed | [Forum with report](https://uncensored.citadel.org/dotgoto?room=Citadel%20Security), [CVE-2021-37845](https://nvd.nist.gov/vuln/detail/CVE-2021-37845) |
| IPswitch IMail | POP3/IMAP | Reported via Mail, unfixed | [CVE-2021-37846](https://nvd.nist.gov/vuln/detail/CVE-2021-37846) |


##### Miscellaneous Issues




| Product | Protocol | Description | Status | Links |
| --- | --- | --- | --- | --- |
| Nemesis (used by GMX / Web.de, provider) | SMTP | Advertises authentication before STARTTLS even though it is disabled | Fixed (reported via Bugbounty) | – |





#### Tags:
[[STARTTLS]] [[(reported]] [[TLS]] [[TLS-only]] [[(report]] [[servers.]] [[emailsIMAPFixed]] [[Web.de]] [[(no]] [[The Record]]
