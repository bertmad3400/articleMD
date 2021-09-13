# WhatsApp details plans to offer encrypted backups
### Users will have the option of keeping a 64-digit key safe themselves, or have it stored for them on what is claimed to be a secure vault.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/whatsapp-details-plans-to-offer-encrypted-backups/)
+ Date: September 13, 2021 -- 04:30 GMT (05:30 BST)
+ Author: Chris Duckett


## Article:
Unknown

![whatsapp-e2ee-backups-user-password.jpg](https://www.zdnet.com/a/hub/i/r/2021/09/13/c479a909-f5f1-45d8-9dbd-f816af37f093/resize/1200xauto/4c68c08f53355c28903362c293e6ba08/whatsapp-e2ee-backups-user-password.jpg)
 Image: WhatsApp
 WhatsApp [announced](https://engineering.fb.com/2021/09/10/security/whatsapp-e2ee-backups/) on Friday it will be offering its users end-to-end encrypted backups later this year. 

Users will have a choice for how the encryption key used is stored. 

The simplest is for users to keep a record of the random 64-digit key themselves, akin to how Signal handles backups, which they would need to re-enter to restore a backup. 

The alternative would be for the random key to be stored in WhatsApp's infrastructure, dubbed as a hardware security module-based (HSM) Backup Key Vault that would be accessible via a user-created password.

"The password is unknown to WhatsApp, the user's mobile device cloud partners, or any third party. The key is stored in the HSM Backup Key Vault to allow the user to recover the key in the event the device is lost or stolen," the company said in a [white paper](https://www.whatsapp.com/security/WhatsApp_Security_Encrypted_Backups_Whitepaper.pdf) [PDF]. 

"The HSM Backup Key Vault is responsible for enforcing password verification attempts and rendering the key permanently inaccessible after a certain number of unsuccessful attempts to access it. These security measures provide protection against brute force attempts to retrieve the key." 

For redundancy purposes, WhatsApp said the key would be distributed through multiple data centres that operate on a consensus model. 






WhatsApp said it would only know that a key exists in its vault, and would not know the key itself. 

The backups would store message text, as well as photos and videos received, WhatsApp said. 

"The backups themselves are generated on the client as data files which are encrypted using symmetric encryption with the locally generated key," the Facebook-owned company said. 

"After a backup is encrypted, it is stored in the third party storage (for example iCloud or Google Drive). Because the backups are encrypted with a key not known to Google or Apple, the cloud provider is incapable of reading them." 

Earlier this year, WhatsApp delayed enforcing a [take-it-or-leave-it update to its privacy terms](https://www.zdnet.com/article/whatsapp-delays-take-it-or-leave-it-privacy-terms-update-until-may/) until May. 

WhatsApp originally presented users with a prompt to accept its new privacy terms by February 8, or risk not being able to use the app. In the wording used, WhatsApp said the policy would change how it partnered with Facebook to "offer integrations", and that businesses could have used Facebook services to manage WhatsApp chats. 

By June, WhatsApp eventually [dumped](https://www.zdnet.com/article/whatsapp-backtracks-on-app-limitations-if-you-dont-agree-to-privacy-changes/) its update plans. 

### Related Coverage

* [WhatsApp fined $267 million for GDPR violations](/article/whatsapp-fined-267-million-for-gdpr-violations-in-ireland/)
* [WhatsApp to adjust privacy rules in Brazil](/article/whatsapp-to-adjust-privacy-rules-in-brazil/)
* [WhatsApp patches vulnerability related to image filter functionality](/article/whatsapp-patches-read-write-vulnerability-related-to-image-filter-functionality/)
* [Facebook brings Snapchat-like view once photo and video feature to WhatsApp](/article/facebook-brings-snapchat-like-view-once-photo-and-video-feature-to-whatsapp/)
* [WhatsApp chief says government officials, US allies targeted by Pegasus spyware](/article/whatsapp-chief-says-government-officials-us-allies-targeted-by-nso-groups-pegasus-spyware/)





#### Tags:
[[WhatsApp]] [[ZDNet]]
