# Microsoft Teams adds end-to-end encryption for one-to-one calls
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/microsoft-teams-adds-end-to-end-encryption-for-one-to-one-calls/)
+ Date: October 22, 2021
+ Author: Sergiu Gatlan


## Article:
![Microsoft Teams adds end-to-end encryption for one-to-one calls](https://www.bleepstatic.com/content/hl-images/2021/04/27/0_Microsoft-Teams.jpg)


Microsoft has announced the public preview roll-out of end-to-end encryption (E2EE) support for one-to-one Microsoft Teams calls.


While Teams already encrypts data in transit and at rest, it also allows IT administrators to set up automatic recording and transcription of voice calls.


Because of this, Teams calls are not suitable when sharing sensitive info that should remain private between the two call participants.


Starting today, Microsoft Teams is getting end-to-end encryption for 1:1 calls which encrypts the real-time media flow (i.e., video and voice data) so that private one-to-one discussions remain entirely private, with no way for intermediate nodes or parties to decrypt them.


"We’re rolling out this preview of E2EE for unscheduled one-to-one calls today. When both parties in a one-to-one call turn on E2EE, the communication between those two parties in the call is encrypted from end-to-end. No other party, including Microsoft, has access to the decrypted conversation," said Mansoor Malik, Principal Group Product Manager for Microsoft Teams.


"With this release, only the real-time media flow, that is, video and voice data, for one-to-one Teams calls are end-to-end encrypted. Both parties must turn on this setting to enable end-to-end encryption."


Encryption for chat, file sharing, presence, and other content in the calls is also available for Microsoft 365 users (more info is available [here](https://docs.microsoft.com/en-us/microsoft-365/compliance/encryption?view=o365-worldwide)).


How to turn on Teams calls E2EE
-------------------------------


While end-to-end encryption for 1:1 Microsoft Teams calls is disabled by default, IT admins will be able to toggle it on for their entire organizations or only for a specific user group.




IT admins can choose which users in their organization can use the enhanced encryption settings in Teams from the IT Admin modern portal under Enhanced Encryption policies.


They can also manage end-to-end encryption policies using PowerShell scripts and apply them to tenants, users, and groups.


To make end-to-end encryption calls available by using the Teams admin center:


1. Sign in to the Teams admin center and navigate to **Other settings > Enhanced encryption policies**.
2. Name the new policy, then for **End-to-end call encryption**, choose **users can turn it on**, and then select **Save**.
3. Once you’ve finished creating the policy, assign the policy to users, groups, or your entire tenant the same way you manage other Teams policies.



![Enabling E2EE via the Microsoft Teams admin center](https://www.bleepstatic.com/images/news/u/1109292/2021/Teams_E2EE.png)*Enabling E2EE via the Microsoft Teams admin center (Microsoft)*
The feature will be available to users only after they receive the latest Microsoft Teams update. They need to turn on end-to-end encryption in their Team settings.


To turn on end-to-end encryption, users can follow these steps:


1. On the top right of the Teams window, select the profile picture (or the ellipses next to the profile picture).
2. Choose **Settings > Privacy**.
3. Turn on end-to-end encrypted calls by toggling the switch.


End-to-end encrypted calls are available when the two parties use the latest versions of the Teams client for desktops (Windows and Mac) and on mobile (iOS and Android).


Further information on how 1:1 calls are end-to-end encrypted and what Teams features aren't available when end-to-end encryption is turned on can be found in [Malik's blog post](https://techcommunity.microsoft.com/t5/microsoft-teams-blog/use-end-to-end-encryption-for-one-to-one-microsoft-teams-calls/ba-p/2867066).




#### Tags:
[[Teams]] [[end-to-end]] [[Microsoft]] [[one-to-one]] [[E2EE]] [[policies.]] [[Bleeping Computer]]
