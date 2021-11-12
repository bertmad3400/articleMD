# RHEL 8.5 delivers key container improvements
### The latest version of Red Hat Enterprise Linux is ready to run on Windows, Linux, and macOS.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/rhel-8-5-arrives/)
+ Date: November 12, 2021
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

[RHEL 8.5](https://www.redhat.com/en/blog/whats-new-rhel-85), the newest version of [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux), is out. As Joe Brockmeier, Red Hat Blogs' Editorial Director, said, "Whether you're deploying RHEL on-prem, in the public cloud, at the edge -- or all of the above -- RHEL 8.5 has improvements that users will be eager to dig into." 

He's not wrong.


In particular, as we continue to move to a container and [Kubernetes](https://kubernetes.io/)-based world, RHEL 8.5 comes with significant container improvements. These include: 

* **Containerized Podman:**The RHEL 8 Podman container image is now generally available and can help unlock the usage of Podman in cloud [continuous integration/delivery (CI/CD)](https://www.hpe.com/us/en/insights/articles/continuous-integration-and-delivery-tool-basics-1807.html) systems, on [Windows Subsystem for Linux (WSL) 2](https://docs.microsoft.com/en-us/windows/wsl/), under [Docker Desktop](https://www.docker.com/products/docker-desktop) on macOS, and (of course) on RHEL 6, 7 and 8. You can use the Podman container image to help develop and run other container images.
* **Verify container image signatures by default:** In RHEL 8.5, users can pull container images with confidence. Out of the box, RHEL 8.5 will check container image signatures to verify that they are, in fact, from Red Hat and haven't been tampered with or manipulated.
* **Native OverlayFS as a Rootless container user:** RHEL 8.5 offers better performance when building and running rootless containers, with native support for OverlayFS.

Returning to RHEL basics, its web console, which is based on the open-source [Cockpit](https://cockpit-project.org/) project, now enables you to live patch the kernel from it. Previously, you could only keep your Linux running while updating the kernel in real-time by using the shell. 

The updated web console also includes an enhanced-performance metrics page. With this, you can more easily identify high CPU, memory, disk, and network resource usage spikes and their causes. In addition, you can also more easily export metrics to a [Grafana](https://grafana.com/) server for a deeper look at what's going on in your servers.

[Red Hat](https://www.redhat.com/en) is also continuing to integrate its [Ansible](https://www.ansible.com/) [DevOps](https://www.zdnet.com/article/what-is-devops-an-executive-guide-to-agile-development-and-it-operations/) program into RHEL. RHEL's system roles now use Ansible roles and modules to configure, automate, and manage RHEL services. Its new or enhanced system roles include: 

* **RHEL system role for VPN:** Reduces the time to configure VPN tunnels and reduces the risk of misconfiguration or use of non-recommended settings. Also supports host-to-host and mesh VPN configurations.
* **RHEL system role for Postfix:** In tech preview for some time, the RHEL system role for Postfix is fully supported with RHEL 8.5. It enables administrators to skip the manual configuration of Postfix, automating how you install, configure, and start the server, as well as specify custom settings to better control how Postfix works in your environment.
* **RHEL system role for timesync:**Uses a new Network Time Security (NTS) option as part of the existing timesync system role.
* **RHEL system role for Storage:** Adds support for LVM (Logical Volume Manager) VDO (Virtual Data Optimizer) volumes and volume sizes that can be expressed as a percentage of the pool's total size.

There are numerous other improvements as well. This includes OpenJDK 17, the latest open-source reference implementation of [Java SE](https://www.oracle.com/java/technologies/downloads/). And, for better network and system security, RHEL now includes [network time security (NTS)](https://www.internetsociety.org/blog/2020/08/everything-you-need-to-know-about-network-time-security/) for [Network Time Protocol (NTP)](https://www.techtarget.com/searchnetworking/definition/Network-Time-Protocol). 






In addition -- showing how much things have changed since Microsoft and Red Hat were at each other's throats -- RHEL now comes with a system role for Microsoft SQL Server. This enables IT administrators and DBAs to automatically and quickly install, configure, and tune SQL Server. It also now includes [Microsoft's latest .NET 6 release](https://www.zdnet.com/article/microsoft-makes-visual-studio-2022-and-net-6-generally-available/). The new [NET 6](https://devblogs.microsoft.com/dotnet/announcing-net-6/) is now available for Windows, Linux, and macOS. It provides a unified platform across cloud, desktop, IoT, and mobile apps.

In short, RHEL 8.5 is ready to run today on any platform you care to name. 

Want to know more? Check out the [RHEL system roles overview](https://access.redhat.com/articles/3050101) to learn how to install and use RHEL system roles.

**Related Stories:**

* [The first fruits of CentOS Stream: Red Hat Enterprise Linux 9 Beta](https://www.zdnet.com/article/the-first-fruits-of-centos-stream-red-hat-enterprise-linux-9-beta/)
* [Red Hat expands Linux offerings for research and academic organizations](https://www.zdnet.com/article/red-hat-expands-linux-offerings-for-research-and-academic-organization/)
* [With Whitehurst stepping down, where do IBM and Red Hat go from here?](https://www.zdnet.com/article/with-whitehurst-stepping-down-where-do-ibm-and-red-hat-go-from-here/)





#### Tags:
[[RHEL]] [[Linux]] [[Podman]] [[configure,]] [[Microsoft]] [[ZDNet]]
