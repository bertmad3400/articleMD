# EasyWSL turns Linux docker images into a Windows 10 WSL distro
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/easywsl-turns-linux-docker-images-into-a-windows-10-wsl-distro/)
+ Date: August 15, 2021
+ Author: Lawrence Abrams


## Article:
![WSL](https://www.bleepstatic.com/content/hl-images/2020/09/30/wsl-space-header.jpg)


If you can't find your favorite Windows Subsystem for Linux distribution available in the Microsoft Store, a new program called EasyWSL can convert almost any Linux Docker image into a WSL distro.


The Microsoft Store offers many prebuilt Linux WSL distributions such as Fedora, Ubuntu, Alpine, Kali, Debian, and more.


However, many popular Linux distributions such as ArchLinux or Centos are unavailable or require you to pay for them.


It is also concerning that many of the paid WSL distributions are not created by the original maintainers but third parties, raising concerns that they have tampered.



![Microsoft Store paid-for Centos distributions](https://www.bleepstatic.com/images/news/software/e/easywsl/centos-microsoft-store-search.jpg)**Microsoft Store paid-for Centos distributions**
To make it easier to find Linux distros that are not available in the Microsoft Store, cybersecurity firm [Red Code Labs](https://redcodelabs.io/) has created an open-source project called '[EasyWSL](https://github.com/redcode-labs/easyWSL)' that converts almost any Linux Docker image into WSL.


"I felt that we can somehow bring more of Linux soul into Windows via WSL, something more than Microsoft has to offer in their Store," explained Red Code Labs regarding why they created EasyWSL.


"Basically it was a great idea to use try using Arch and Gentoo and their repos at the first point, but then I realized, why not to somehow get images from Docker Hub, to make the possibilities even bigger."


Even better, as these distros are managed on Docker by the original maintainers, you know that the builds have not been modified to include malicious programs or code.



![EasyWSL program](https://www.bleepstatic.com/images/news/software/e/easywsl/easywsl.jpg)**EasyWSL program**
As you can see, EasyWSL offers a wide-range of Linux distro that you can install, including:


* ArchLinux
* Ubuntu 20.04
* Ubuntu 20.10
* Alpine
* DebianStable
* DebianUnstable
* DebianTesting
* CentOS
* Clear Linux
* Fedora
* Manjaro
* Scientific Linux
* Crux Linux
* Void Linux
* Kali Linux
* OpenSuse Leap
* Parrot Security OS
* Gentoo


However, if the Linux distro you are looking for is unavailable, you can use the EasyWSL to install a Docker image of your choice in WSL.


How to convert a Linux docker image to WSL
------------------------------------------


For example, the popular [Photon distro](https://hub.docker.com/_/photon) is not available from the Microsoft Store, but we can easily install it from Docker using EasyWSL.


To install a custom image, you would select the 'Specify a docker image' option, and when it asks for a docker container, you would enter the name of the distro and the tag to install using the following syntax: 


In Photon's case, the image name is '**photon**' and the tag is '**latest**', as [shown on this page](https://hub.docker.com/_/photon?tab=tags&page=1&ordering=last_updated).


We would then use the '**photon:latest**' container when prompted by EasyWSL, as shown below.



![Installing Photon using EasyWSL](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Installing Photon using EasyWSL**
While almost all Linux Docker images will install without an issue, you may see an error caused by a missing command depending on the post-installation routines.


However, the operating system will install and be usable within WSL.


You should note that after installing a new Linux distribution using EasyWSL, the WSL installation will not appear in the Start Menu.


To launch the new distribution, you can use the `wsl -d [linux\_distro]` command from a command prompt to launch it.


For example, to launch Photon we would use the `wsl -d photon` command.


For those who enjoy using WSL in Windows 10, EasyWSL is definitely a great addition to your toolbox so that you can install the Linux distribution you are looking for.




#### Tags:
[[Linux]] [[Microsoft]] [[EasyWSL]] [[WSL]] [[distro]] [[Windows]] [[Store,]] [[However,]] [[WSL.]] [[Bleeping Computer]]
