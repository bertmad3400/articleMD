# Kali Linux 2021.4 released with 9 new tools, further Apple M1 support
### ​Kali Linux 2021.4 was released today by Offensive Security and includes further Apple M1 support, increased Samba compatibility, nine new tools, and an update for all three main desktop.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/kali-linux-20214-released-with-9-new-tools-further-apple-m1-support/
+ Date: 2021-12-09T17:58:02-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/06/02/kali-linux-header.jpg)

![Kali Linux](https://www.bleepstatic.com/content/hl-images/2021/06/02/kali-linux-header.jpg)


​Kali Linux 2021.4 was released today by Offensive Security and includes further Apple M1 support, increased Samba compatibility, nine new tools, and an update for all three main desktop.


Kali Linux is a Linux distribution allowing cybersecurity professionals and ethical hackers to perform penetration testing and security audits against internal and remote networks.


With this release, the Kali Linux Team introduces a bunch of new features, including:


* Apple M1 support for the VMware Fusion Public Tech Preview
* Wide compatibility is enabled for Samba
* Making it easier to switch to Cloudflare's package manager mirror
* Kaboxer updated with support for window themes and icon theme
* Updates to the Xfce, GNOME and KDE desktops
* Raspberry Pi Zero 2 W + USBArmory MkII ARM images
* Nine more tools!

Further Apple M1 support
------------------------


It was already possible to install Kali Linux on Parallels on Apple Silicon Macs. 


With Kali Linux 2021.4, you can now also install the distro on the [VMware Fusion Public Tech Preview](https://blogs.vmware.com/teamfusion/2021/09/fusion-for-m1-public-tech-preview-now-available.html) as the new kernel includes the modules needed for the virtual GPU.


Using Kali's installer will automatically detect if you are installing on VMware and install the appropriate packages.


Samba gets wide compatibility
-----------------------------


As insecure protocols are discovered in Samba, they are commonly disabled by default on Linux distributions to increase security.


As Kali Linux is a penetration test distribution, it is better to enable all protocols so that pentesters can find older, vulnerable implementations.


With this release, Offensive Security is configuring Samba for wide compatibility, which means that they are enabling older Samba protocols.



![Samba wide compatibility setting](https://www.bleepstatic.com/images/news/linux/k/kali-linux/2021.4/samba.png)**Samba wide compatibility setting**
Nine new tools added in Kali Linux 2021.4
-----------------------------------------



It wouldn't be a new Kali Linux version without some new tools and utilities, which are listed below:


* [Dufflebag](https://pkg.kali.org/pkg/dufflebag) - Search exposed EBS volumes for secrets
* [Maryam](https://pkg.kali.org/pkg/maryam) - Open-source Intelligence (OSINT) Framework
* [Name-That-Hash](https://pkg.kali.org/pkg/name-that-hash) - Do not know what type of hash it is? Name That Hash will name that hash type!
* [Proxmark3](https://pkg.kali.org/pkg/proxmark3) - if you are into Proxmark3 and RFID hacking
* [Reverse Proxy Grapher](https://pkg.kali.org/pkg/rev-proxy-grapher) - graphviz graph illustrating your reverse proxy flow
* [S3Scanner](https://pkg.kali.org/pkg/s3scanner) - Scan for open S3 buckets and dump the contents
* [Spraykatz](https://pkg.kali.org/pkg/spraykatz) - Credentials gathering tool automating remote procdump and parse of lsass process.
* [truffleHog](https://pkg.kali.org/pkg/trufflehog) - Searches through git repositories for high entropy strings and secrets, digging deep into commit history
* [Web of trust grapher (wotmate)](https://pkg.kali.org/pkg/wotmate) - reimplement the defunct PGP pathfinder without needing anything other than your own keyring

Enhanced ARM support
--------------------


The Kali Linux team continues to improve support for ARM devices with the following changes:


* **All images now use ext4 for their root filesystem**, and **resize the root filesystem on first boot**. This results in a speed-up over previous releases which were using ext3, and a reduced boot time on the first reboot when resize happens.
* **Raspberry Pi Zero 2 W support has been added**, but like the Raspberry Pi 400, there is no Nexmon support.
* Speaking of the **Raspberry Pi Zero 2 W**, since it is so similar to the Zero W, we have also added a **PiTail image** to support the new processor with better performance.
* **Raspberry Pi images now support USB booting** out of the box since we no longer hardcode the root device.
* **Raspberry Pi images now include versioned Nexmon firmware**. A future release of `kalipi-config` will allow you to switch between them, if you would like to test different versions.
* Images that use a vendor kernel will now be able to set the regulatory domain properly, so **setting your country will give access to channels properly for wireless**.
* **Pinebook Pro can now be overclocked**. The big cores get 2GHz and the little cores get 1.5GHz added.
	+ `echo 1 | sudo tee /sys/devices/system/cpu/cpufreq/boost` to enable
	+ `echo 0 | sudo tee /sys/devices/system/cpu/cpufreq/boost` to disable
* **USBArmory MkII image has been added**.

How to get Kali Linux 2021.4
----------------------------


To start using Kali Linux 2021.4, you can upgrade your existing installation or [download ISO images](http://cdimage.kali.org/kali-2021.4/) for new installs and live distributions.


For those updating from a previous version, including installs on the Windows Subsystem for Linux (WSL), you can use the following commands to upgrade to the latest version.



```
echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee /etc/apt/sources.list

sudo apt update && sudo apt -y full-upgrade

cp -i /etc/skel/.bashrc ~/

cp -i /etc/skel/.zshrc ~/

chsh -s /bin/zsh

[ -f /var/run/reboot-required ] && sudo reboot -f
```

Once you are done upgrading, you can see if the upgrade to Kali Linux 2021.4 was successful by using the following command:



```
grep VERSION /etc/os-release
```

A [complete changelog for Kali 2021.4](https://www.kali.org/blog/kali-linux-2021-4-release/) can be found at Kali's website.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Linux]] [[Sudo]] [[M1]] [[Vmware]] [[Bleeping Computer]]
#### urls
http://http.kali.org/kali

