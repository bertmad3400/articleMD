# VMware ESXi Servers Encrypted by Lightning-Fast Python Script
### The little snippet of Python code strikes fast and nasty, taking less than three hours to complete a ransomware attack from initial breach to encryption.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175374)
+ Date: October 6, 2021  4:34 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/10/06161649/python-e1633551421879.jpeg)
Researchers have discovered a new Python ransomware from an unnamed gang that’s striking ESXi servers and virtual machines (VMs) with what they called “sniper-like” speed.


[Sophos said](https://www.sophos.com/en-us/press-office/press-releases/2021/10/sophos-researchers-uncover-new-python-ransomware-targeting-an-esxi-server-and-virtual-machines.aspx) on Tuesday that the ransomware is being used to compromise and encrypt VMs hosted on an ESXi hypervisor in operations that, soup-to-nuts, are taking less than three hours to complete from initial breach to encryption.


“This is one of the fastest ransomware attacks Sophos has ever investigated, and it appeared to precision-target the ESXi platform,” Andrew Brandt, principal researcher at Sophos, was quoted as saying in a press release that accompanied his in-depth [report](https://news.sophos.com/en-us/2021/10/05/python-ransomware-script-targets-esxi-server-for-encryption/).


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Brandt noted that it’s rare to see the Python coding language used for ransomware. But its use makes sense, he explained, given that Python comes pre-installed on Linux-based systems such as ESXi, and thus makes Python-based attacks possible on these systems.


Targeting ESXi Is a No-Brainer
------------------------------


While the choice of Python for the ransomware is fairly distinctive, going after ESXi servers is anything but. Attackers love VMware’s ESXi (formerly known as ESX), which is a bare-metal hypervisor that installs easily onto servers and partitions them into multiple VMs.


While that makes it easy for multiple VMs to share the same hard-drive storage, it sets systems up to be one-stop shopping spots for attacks, since attackers can encrypt the centralized virtual hard drives used to store data from across VMs. In other words, one hit locks up scads of VMs.


That’s how AT&T Cybersecurity’s [Alien Labs](https://cybersecurity.att.com/blogs/labs-research/revils-new-linux-version) explained it in July, shortly after the REvil ransomware threat actors came up with a [Linux variant](https://threatpost.com/linux-variant-ransomware-vmwares-nas/167511/) that likewise targeted VMware ESXi, as well as its network-attached storage (NAS) devices.


Later that month, [HelloKitty joined](https://threatpost.com/linux-variant-of-hellokitty-ransomware-targets-vmware-esxi-servers/167883/) the growing list of ransomware bigwigs going after the juicy target. DarkSide has also targeted ESXi servers: In June, [AT&T Alien Labs analyzed](https://cybersecurity.att.com/blogs/labs-research/darkside-raas-in-linux-version) the Linux version of the DarkSide ransomware, which it called one of the most active ransomwares in the previous quarter.


In short, everybody in ransomware-land craves ESXi pwnage: It’s like hitting the jackpot at the slots.


“ESXi servers represent an attractive target for ransomware threat actors because they can attack multiple VMs at once, where each of the VMs could be running business-critical applications or services,” Brandt explained. “Attacks on hypervisors can be both fast and highly disruptive.”


A Squashed Attack Timeline
--------------------------


Sophos was investigating a ransomware attack when it came across the new, uber-fast Python script. The attack started in the wee hours – 12:30 a.m. – on a Sunday morning, when the ransomware operators broke into a TeamViewer account belonging to a user who had admin access but who didn’t have multi-factor authentication (MFA) enabled. Here’s a timeline of what followed:


Ten minutes in, the attackers were looking for network targets, using the Advanced IP Scanner tool for reconnaissance. Sophos’s investigators believe that the network’s ESXi server was vulnerable because it had an [active shell](https://linuxcommand.org/lc3_lts0010.php) that an IT team was using for commands and updates. According to Sophos’ report, ESXi servers have a built-in SSH service called the ESXi Shell that administrators can enable, but which is typically disabled by default.


“This organization’s IT staff was accustomed to using the ESXi Shell to manage the server, and had enabled and disabled the shell multiple times in the month prior to the attack,” according to Brandt’s report. “However, the last time they enabled the shell, they failed to disable it afterwards. The criminals took advantage of this fortuitous situation when they found the shell was active.”


The attackers downloaded an SSH client called Bitvise, and used it to log into a VMware ESXi server they identified using Advanced IP Scanner.


Three hours after the attackers scanned the network, they used the pilfered admin credentials to log into the ESXi Shell. Then they copied a file named “fcker.py” to the ESXi datastore, which houses the virtual disk images used by the VMs that run on the hypervisor, Brandt explained.


The Python script uses the vim-cmd command functions of the ESXi Shell to produce a list of the names of all VMs installed on the server, then shuts them all down, he said. Only after the VMs are all powered off will the script begin encrypting the datastore volumes.


Then, the Python script slithers through, picking off VMs one after another, Brandt recounted: “One by one, the attackers executed the Python script, passing the path to datastore disk volumes as an argument to the script. Each individual volume contained the virtual disk and VM settings files for multiple virtual machines.”


The ransomware snippet uses just a single instruction for each file it encrypts, invoking the open-source tool OpenSSL to encrypt the files with this command:


*openssl rsautil -encrypt -inkey pubkey.txt -pubin -out [filename].txt*


Sophos investigators managed to nab a copy of the Python script, in spite of the attackers having apparently overwritten it with other data before deleting the file. The “other data” meaning, specifically, the curse word “f–k.” [*Redacted by Ed.*]


“Finally, it deletes the files that contain the directory listings, the names of the VMs and itself by overwriting those files before deleting them,” Brandt wrote.


This Baby Python Has Sharp Fangs
--------------------------------


Weighing in at only 6KB, It’s an itty-bitty thing that can do a whole lot of damage.


“The script contains variables that the attacker can configure with multiple encryption keys, email addresses, and where they can customize the file suffix that gets appended to encrypted files,” Brandt wrote. Specifically, the Python script embeds, as variables, the file suffix it appends to encrypted files (ext), and email addresses (mail, mail2) to be used to contact the attacker for payment of the ransom.


It also embeds the ransom note text shown below.


Encryption Keys-R-Us
--------------------


While walking through the code, Sophos investigators noted multiple, hardcoded encryption keys, as well as a routine for generating even more encryption key pairs. They found that odd, Brandt said.


“Normally, an attacker would only need to embed the ‘public key’ that the attacker generated on their own machine and would be used to encrypt files on the targeted computer(s),” he noted. “But this ransomware appears to create a unique key every time it is run.”


It turned out that the attackers executed the script once for each ESXi datastore they wanted to encrypt. Each time it executed, the script generated a unique key pair to use in encrypting files. In the case that Sophos investigated, the attackers targeted three datastores, each time with individual executions of the script, “so the script created three unique key pairs, one for each datastore,” according to the writeup.


Those keys weren’t going anywhere, though, given that the script had no ability to transmit them anywhere. But the attackers obviously didn’t want to leave them sitting around where victims could use them to decrypt their locked files without paying a dime in ransom, so the script wrote out a copy of the secret key, then encrypts it, using the embedded, hardcoded public key.


“The script runs a routine that lists all the files in the path that’s provided to the script during execution,” the report continued. “For each file, the script generates a unique, 32-byte random code it calls the aeskey, and then encrypts the file using the aeskey as a salt into the /tmp path. Finally, it prepends the aeskey value to the encrypted file and appends a new file suffix to the name, overwrites the contents of the original file with the word fuck then deletes the original file, and moves the encrypted version from /tmp to the datastore location where the original file was stored.”


Endpoint Protection on ESXi Servers Is Lacking
----------------------------------------------


While Linux variants of malware that can be used to target systems such as ESXi are still “relatively uncommon,” endpoint protection on these kinds of servers is even rarer, Brandt said.


He passed on advice for hardening ESXi or other hypervisors, including standard security best practices such as:


“In the case of ESXi, use of the ESXi Shell is something that can be toggled on or off from either a physical console at the machine itself, or through the normal management tools provided by VMware,” Brandt advised. “Administrators should only allow the Shell to be active during use by staff, and should disable it as soon as maintenance (such as the installation of patches) is complete.”


VMware has also [published a list](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-E9B71B85-FBA3-447C-8A60-DEE2AE1A405A.html) of best practices for administrators of their ESXi hypervisors on how to secure them and limit the attack surface on the hypervisor itself.


***Check out our free*** [***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***




#### Tags:
[[ESXi]] [[ransomware]] [[VMs]] [[Brandt]] [[Sophos]] [[datastore]] [[hypervisor]] [[ESXi,]] [[VMs.]] [[Linux]] [[ThreatPost]]
