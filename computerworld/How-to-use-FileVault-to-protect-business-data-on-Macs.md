# How to use FileVault to protect business data on Macs
### If you use Macs for business, you should be familiar with FileVault. Apple’s built-in disk encryption system for macOS can help protect corporate data.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3643332/how-to-use-filevault-to-protect-business-data-on-macs.html
+ Date: 2021-12-02
+ Author: Jonny Evans


## Article:
![Article Image](https://images.idgesg.net/images/idge/imported/imageapi/2021/03/30/11/filevault-macos-icon-100882745-large.jpg?auto=webp&quality=85,70)

If you run a business on Macs (and [many companies do](https://blogs.computerworld.com/article/3640399/jamf-ceo-welcomes-apple-business-essentials.html)) then you should become familiar with FileVault, the disk encryption system that's built into macOS. When used properly, it makes it extremely hard for any malicious person to access your company’s confidential data in the event your Mac is lost or stolen.

**What's the problem FileVault tries to solve?**
------------------------------------------------

Most businesses possess various forms of sensitive data. This might include corporate  or supplier data, confidential order books, financial records, contact names and addresses, and more. That information has business value, but if compromised could also place you, your employees, or your customers at risk. In many industries, protection of such information is mandatory and legally required.

Apple’s FileVault makes it much harder for unauthorized users to extract this kind of data from company Macs. It does so by encrypting the data on the Mac and decrypting it only once an appropriate login is used. FileVault encyrypts and decrypts data in the background, so the system can be used while the it does.

**What is FileVault?**
----------------------

Apple introduced FileVault in 2005 with Mac OS X Panther (10.3). At that time, it only protected a user’s Home folder. The technology has evolved since then and now offers XTS-AES 128 data encryption for the whole disk, protected by a 256-bit key.

When it comes to business, IT can manage FileVault using most available MDM systems and consoles.  When a Mac is protected by FileVault, no one can access its data unless they have the FileVault decryption key or user account credentials.

The current implementation of FileVault is available on both recent Intel and Apple Silicon Macs.

**How to enable FileVault**
---------------------------

FileVault is not enabled by default.

To enable it you must be an [Admin user](https://support.apple.com/en-gb/guide/mac-help/aside/gloscddf7f3c/12.0/mac/12.0) on your Mac. If so, you can open *System Preferences>Security & Privacy* and check the *FileVault* tab.

You will be given two choices, to protect the Mac using your iCloud account and password, or to use a Recovery Key. The first option is fine for personal users, but most enterprises will probably use a Recovery Key.

It is very important to note your login password and the recovery key generated for you when you enable FileVault. That’s because if you forget them both, all the data on your Mac will be unavailable to you. One protection here is that console-based MDM-based systems may be able to remotely assign new keys.

**NB:** Once you enable FileVault, it cannot be turned off until the first full encrypt has taken place. That first encryption can take time, depending on how much information you have on your Mac. Subsequently, in the event the passphrase or recovery key is changed the entire volume must be decrypted and re-encrypted.

**Know your limits**
--------------------

It is extremely important to note that an individual user who cannot recall their password or recovery key will never be able to access that data, as they will eventually need to delete and reinstall macOS.

However, a business that makes use of a modern MDM system to manage its Macs can also assign institutional recovery keys that can be managed and stored from the MDM console. That’s useful as it means that if a user forgets their password, IT can use the recovery key to reset FileVault and [assign a new password](https://www.applemust.com/jamf-just-made-macs-even-easier-to-use-in-the-enterprise/) to get them back in.

**What to consider when creating passcodes**
--------------------------------------------

Companies should consider passcode policy for FileVault volumes. A generalization is that longer passcodes are stronger passcodes (so long as they aren’t 12345678910), but it’s also important to consider passcode rotation schedules and alphanumeric codes. In my experience, the challenge with the FileVault recovery key is that since it is used so infrequently, it is very easy to forget the code. This is one code that needs to be written down and locked away somewhere, even if you use a [transposition cipher](https://www.britannica.com/topic/transposition-cipher) to secure that written key.

#### [Also read: [How to stay as private as possible on the Mac](https://www.computerworld.com/article/3598254/how-to-stay-as-private-as-possible-on-the-mac.html)]

**Some Macs already encrypt**
-----------------------------

Macs equipped with an Apple T2 Security chip automatically encrypt data already. It’s still worth using FileVault with those systems as it enhances the inherent protection by requiring your login password to decrypt your data.

Apple maintains a list of Macs that make use of the T2 Security Chip [here](https://support.apple.com/en-us/HT208862).

**Should all your Macs be protected by FileVault?**
---------------------------------------------------

As a rule of thumb, any Mac that carries or has access to personal or sensitive business data should use FileVault encryption.

**What are the consequences of using FileVault?**
-------------------------------------------------

Other than the complete loss of data in the event you forget your passcodes and lose access to your Mac, the biggest negative outcome when using FileVault is that I/O performance can sometimes be affected.

**What can I use instead of FileVault?**
----------------------------------------

Though FileVault has the big advantage of being Mac-native, some businesses may prefer to use alternative solutions such as [VeraCrypt](https://www.veracrypt.fr/code/VeraCrypt/).

**Where can I find out more about FileVault?**
----------------------------------------------

Apple’s current advice on use of FileVault in macOS Monterey is [available here](https://support.apple.com/kb/index?page=search&src=support_book_welcome&locale=en_GB&bookid=5e2077d8bc16862b7fd64110d1406f84&rurl=https%3A%2F%2Fsupport.apple.com%2Fen-gb%2Fguide%2Fmac-help%2Fwelcome%2Fmac&title=macOS+User+Guide&query=FileVault).

*Please follow me on [Twitter](https://twitter.com/jonnyevans_cw), or join me in the [AppleHolic’s bar & grill](https://mewe.com/join/appleholics_bar_and_grill) and [Apple Discussions](https://mewe.com/join/apple_discussions) groups on MeWe.*





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Filevault]] [[Mdm]] [[Passcodes]] [[Computerworld]]

