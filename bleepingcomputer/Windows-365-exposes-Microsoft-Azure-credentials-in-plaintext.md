# Windows 365 exposes Microsoft Azure credentials in plaintext
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/windows-365-exposes-microsoft-azure-credentials-in-plaintext/)
+ Date: August 13, 2021
+ Author: Lawrence Abrams


## Article:
![Microsoft bug](https://www.bleepstatic.com/content/hl-images/2021/05/26/Microsoft-Defender_(1).jpg)


A security researcher has figured out a way to dump a user's unencrypted plaintext Microsoft Azure credentials from Microsoft's new Windows 365 Cloud PC service using Mimikatz.


Mimikatz is an open-source cybersecurity project created by [Benjamin Delpy](https://twitter.com/gentilkiwi) that allows researchers to test various credential stealing and impersonation vulnerabilities.



"It's well known to extract plaintexts passwords, hash, PIN code and kerberos tickets from memory. mimikatz can also perform pass-the-hash, pass-the-ticket, build Golden tickets, play with certificates or private keys, vault, ... maybe make coffee?," explains the project's [GitHub page](https://github.com/gentilkiwi/mimikatz/wiki).


While created for researchers, due to the power of its various modules, it is commonly used by threat actors to dump plaintext passwords from the memory of the LSASS process or perform pass-the-hash attacks using NTLM hashes.


Using this tool, threat actors can spread laterally throughout a network until they control a Windows domain controller, allowing them to take over the Windows domain.


Windows 365 credentials can be dumped in plaintext
--------------------------------------------------


On August 2nd, Microsoft launched their [Windows 365 cloud-based desktop service](https://www.bleepingcomputer.com/news/microsoft/microsofts-windows-365-cloud-pc-service-is-live-costs-from-24-to-162/), allowing users to rent Cloud PCs and access them via remote desktop clients or a browser.


Microsoft offered free trials of virtual PCs that [quickly ran out](https://www.bleepingcomputer.com/news/microsoft/microsoft-halts-windows-365-trials-after-running-out-of-servers/) as people rushed to get their free Cloud PC for two months.


Delpy told BleepingComputer that he was one of the lucky few who could get a free trial and began testing the new service's security.


He found that the brand new service allows a malicious program to dump the Microsoft Azure plaintext email address and passwords for logged-in users.




> 
> Would you like to try to dump your [#Windows365](https://twitter.com/hashtag/Windows365?src=hash&ref_src=twsrc%5Etfw) Azure passwords in the Web Interface too?  
>   
> 
> A new [#mimikatz](https://twitter.com/hashtag/mimikatz?src=hash&ref_src=twsrc%5Etfw) release is here to test!  
> 
> (Remote Desktop client still work, of course!)  
>   
> 
> > <https://t.co/Wzb5GAfWfd>  
>   
> 
> cc: [@awakecoding](https://twitter.com/awakecoding?ref_src=twsrc%5Etfw) [@RyMangan](https://twitter.com/RyMangan?ref_src=twsrc%5Etfw) [pic.twitter.com/hdRvVT9BtG](https://t.co/hdRvVT9BtG)
> 
> 
> — Benjamin Delpy (@gentilkiwi) [August 7, 2021](https://twitter.com/gentilkiwi/status/1424123713969172481?ref_src=twsrc%5Etfw)


The credential dumps are being done through a [vulnerability he discovered in May 2021](http://twitter.com/gentilkiwi/status/1397263983221039105?ref_src=twsrc%5Etfw) that allows him to dump the plaintext credentials for users logged into a Terminal Server.


While a user's Terminal Server credentials are encrypted when stored in memory, Delpy says he could trick the Terminal Service process into decrypting them for him.


"Even better, I asked the terminal server process to decrypt them for me (and technically, terminal server process ask the kernel to decrypt it for itself)," Delpy told BleepingComputer in a conversation about his findings.


"Because only the Terminal Server can ask for this kind of own decryption, I had to trick it to decrypt the credentials for me :),"


BleepingComputer used a free Cloud PC trial on Windows 365 to test this technique. After connecting through the web browser and launching mimikatz with Administrative privileges, we entered the "`ts::logonpasswords`" command and mimikatz quickly dumped our login credentials in plaintext, as shown below.



![Mimikatz listing my Azure account credentials in plaintext](https://www.bleepstatic.com/images/news/Microsoft/w/windows-365/dump-credentials/windows-365-miikatz.jpg)**Mimikatz listing my Azure account credentials in plaintext**
This works over the web browser as it's still using the Remote Desktop Protocol.


So, what's the big deal?
------------------------


You may be wondering what the big deal is if you need to be an Administrator to run mimikatz and you already know your Azure account credentials.


In the above scenario, you are right, and it is not a big deal.


However, what happens if a threat actor gains access to your Windows PC device to run commands?


For example, let's say that you open a phishing email with a malicious attachment on your Windows 365 Cloud PC that sneaks through Microsoft Defender.


Once you enable the malicious macros in the document, it can install a remote access program so that a threat actor can access the Cloud PC.


From there, it is trivial to gain administrative privileges using a vulnerability like [PrintNightmare](https://www.bleepingcomputer.com/news/microsoft/remote-print-server-gives-anyone-windows-admin-privileges-on-a-pc/) and then dump your clear-text credentials with mimikatz.


Using these credentials, the threat actor can spread laterally through other Microsoft services and potentially a company's internal network.


"It’s exactly like dumping passwords from a normal session. If I can dump your password in TS sessions I can use it on other systems where you can have more privilege, data, etc," explained Delpy.


"It's common for lateral movements and gaining access to more privileged data on others systems. Particularly useful on VDI systems where others users are also logged in."


Delpy says he would typically recommend 2FA, smart cards, Windows Hello, and [Windows Defender Remote Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/remote-credential-guard) to protect against this method. However, these security features are not currently available in Windows 365.


As Windows 365 is geared towards the enterprise, Microsoft will likely add these security features in the future, but for now, it is important to be aware of this technique.




#### Tags:
[[Windows]] [[Microsoft]] [[Cloud]] [[Delpy]] [[mimikatz]] [[BleepingComputer]] [[Bleeping Computer]]
