# Malicious KMSPico installers steal your cryptocurrency wallets
### Threat actors are distributing altered KMSpico installers to infect Windows devices with malware that steals cryptocurrency wallets.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/malicious-kmspico-installers-steal-your-cryptocurrency-wallets/
+ Date: 2021-12-04T12:06:12-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/12/03/disappearing-bitcoin.jpg)

![Cryptocurrency theft](https://www.bleepstatic.com/content/hl-images/2021/12/03/disappearing-bitcoin.jpg)


Threat actors are distributing altered KMSpico installers to infect Windows devices with malware that steals cryptocurrency wallets.


This activity has been spotted by researchers at Red Canary, who warn that pirating software to save on licensing costs isn't worth the risk.


KMSPico is a popular Microsoft Windows and Office product activator that emulates a Windows Key Management Services (KMS) server to activate licenses fraudulently.


According to Red Canary, many IT departments using KMSPico instead of legitimate Microsoft software licenses are much bigger than one would expect.


"We've observed several IT departments using KMSPico instead of legitimate Microsoft licenses to activate systems," explained Red Canary intelligence analyst Tony Lambert. 


"In fact, we even experienced one ill-fated incident response engagement where our IR partner could not remediate one environment due to the organization not having a single valid Windows license in the environment."


Tainted product activators
--------------------------


KMSPico is commonly distributed through pirated software and cracks sites that wrap the tool in installers containing adware and malware.


As you can see below, there are numerous sites created to distribute KMSPico, all claiming to be the official site.



![Most Google Search results for KMSPico return sites that claim to be official](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/KMS_pico.jpg)**Most Google Search results are sites that claim to be official**
A malicious KMSPico installer analyzed by RedCanary comes in a self-extracting executable like 7-Zip and contains both an actual KMS server emulator and [Cryptbot](https://www.bleepingcomputer.com/news/security/fake-vpn-site-pushes-cryptbot-and-vidar-info-stealing-trojans/).


"The user becomes infected by clicking one of the malicious links and downloads either KMSPico, Cryptbot, or another malware without KMSPico," explains a [technical analysis](https://redcanary.com/wp-content/uploads/2021/12/KMSPico-V5.pdf) of the campaign,


"The adversaries install KMSPico also, because that is what the victim expects to happen, while simultaneously deploying Cryptbot behind the scenes."


The malware is wrapped by the [CypherIT](https://www.bleepingcomputer.com/news/security/bitbucket-abused-to-infect-500-000-hosts-with-malware-cocktail/) packer that obfuscates the installer to prevent it from being detected by security software. This installer then launches a script that is also heavily obfuscated, which is capable of detecting sandboxes and AV emulation, so it won't execute when run on the researcher's devices.



![Obfuscated code of Cryptbot](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/obfuscated_code.jpg)**Obfuscated code of Cryptbot**  
*Source: Red Canary*
Moreover, Cryptobot checks for the presence of "%APPDATA%\Ramson," and executes its self-deletion routine if the folder exists to prevent re-infection.


The injection of the Cryptbot bytes into memory occurs through the process hollowing method, while the malware's operational features overlap with previous research findings.


In summary, Cryptbot is capable of collecting sensitive data from the following apps:


* Atomic cryptocurrency wallet
* Avast Secure web browser
* Brave browser
* Ledger Live cryptocurrency wallet
* Opera Web Browser
* Waves Client and Exchange cryptocurrency applications
* Coinomi cryptocurrency wallet
* Google Chrome web browser
* Jaxx Liberty cryptocurrency wallet
* Electron Cash cryptocurrency wallet
* Electrum cryptocurrency wallet
* Exodus cryptocurrency wallet
* Monero cryptocurrency wallet
* MultiBitHD cryptocurrency wallet
* Mozilla Firefox web browser
* CCleaner web browser
* Vivaldi web browser

Because Cryptbot’s operation doesn’t rely on the existence of unencrypted binaries on the disk, detecting it is only possible by monitoring for malicious behavior such as PowerShell command execution or external network communication.


Red Canary shares the following four key points for threat detection:


* binaries containing AutoIT metadata but don’t have “AutoIT” in their filenames
* AutoIT processes making external network connections
* findstr commands similar to findstr /V /R “^ … $
* PowerShell or cmd.exe commands containing rd /s /q, timeout, and del /f /q together

In summary, if you thought that KSMPico is a smart way to save on unnecessary licensing costs, the above illustrates why [that's a bad idea](https://www.bleepingcomputer.com/forums/t/683336/infected-with-malware-after-trying-to-install-kmspico/).


The reality is that the loss of revenue due to incident response, [ransomware attacks](https://www.bleepingcomputer.com/news/security/meet-stop-ransomware-the-most-active-ransomware-nobody-talks-about/), and cryptocurrency theft from installing pirated software could be more than the cost of the actual Windows and Office licenses.





## Tags:

#### Threatactor:
[[threatactor.name=RTM]] [[threatactor.name=Sandworm Team]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=cmd]] [[action.malware.name=cmd]] [[action.malware.name=Exodus]] [[action.malware.name=Exodus]] [[action.malware.name=Net]] [[action.malware.name=Net]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Kmspico]] [[Cryptbot]] [[Windows]] [[Malware]] [[Microsoft]] [[Bleeping Computer]]

