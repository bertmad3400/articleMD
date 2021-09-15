# Microsoft fixes OMIGOD bugs in secret Azure app
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/microsoft-fixes-omigod-bugs-in-secret-azure-app/)
+ Date: September 15, 2021
+ Author: Catalin Cimpanu


## Article:
![Microsoft fixes OMIGOD bugs in secret Azure app](https://therecord.media/wp-content/uploads/2021/09/peek.png)

* The four bugs affect OMI, an app that Microsoft has been silently installing on Azure Linux VMs.
* Collectively known as OMIGOD, the four bugs have been fixed last month in the OMI v1.6.8.1 client.
* The app has no auto-update mechanism, so most Azure Linux VMs remain vulnerable unless a manual patch.


**As part of its monthly Patch Tuesday security updates, Microsoft has patched a collection of four vulnerabilities in OMI, a mostly unknown application that the company has been silently installing on most Linux-based Azure virtual machines and related systems.**


Called Open Management Infrastructure (OMI), the app is the Linux equivalent of Microsoft’s Windows Management Infrastructure (WMI), a service that collects data from local environments and synchronizes it with a central management server.


Unbeknownst to most Azure customers is that Microsoft silently installs OMI clients with all Linux-based Azure virtual machines.


The client runs with root privileges, and its role is to integrate the VM with centralized Microsoft management tools like the Open Management Suite (OMS), Azure Insights, Azure Automation, and others.


### OMIGOD bug opens Azure environments to easy takeovers


In a report published on Tuesday, cloud security firm Wiz said it found a collection of four security flaws in the OMI client that could allow threat actors to hijack Azure Linux VMs.


Collectively tracked as [OMIGOD](https://www.wiz.io/blog/secret-agent-exposes-azure-customers-to-unauthorized-code-execution), the four are detailed below:


* [CVE-2021-38647](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38647) – Unauthenticated RCE as root (Severity: 9.8)
* [CVE-2021-38648](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38648) – Privilege Escalation vulnerability (Severity: 7.8)
* [CVE-2021-38645](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38645) – Privilege Escalation vulnerability (Severity: 7.8)
* [CVE-2021-38649](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38649) – Privilege Escalation vulnerability (Severity: 7.0)


Of the four, the first is the most serious issue, as it can allow a threat actor to take over an Azure Linux VM just by sending a malformed packet over the internet.


“This is a textbook RCE vulnerability that you would expect to see in the 90’s – it’s highly unusual to have one crop up in 2021 that can expose millions of endpoints,” said Wiz security researcher Nir Ohfeld.


“With a single packet, an attacker can become root on a remote machine by simply removing the authentication header,” Ohfeld added.


“It’s that simple,” the researcher said.


Once inside a network, the attacker can repeat the attack on other nearby systems for a full network compromise, according to the Wiz team.


![Wiz-gif-OMIGOD](https://therecord.media/wp-content/uploads/2021/09/Wiz-gif-OMIGOD.gif)Image: Wiz
While CVE-2021-38647 is as bad as it gets, Ohfeld said there’s also a sunny side, as the ports through which this bug can be exploited are not exposed over the internet by default.



> If you have OMI listening on ports 5985, 5986, 1270 we advise limiting network access to those ports immediately in order to protect from the RCE vulnerability (CVE-2021-38647).
> 
> Wiz security researcher Nir Ohfeld


But if customers disable their Azure environment firewall or allow connections to these ports, all their systems are vulnerable to attacks.


Furthermore, even if those ports aren’t enabled, attackers can still abuse the OMI client through the other three OMIGOD bugs by tricking an Azure user into opening or interacting with a malicious file that exploits any of the three bugs in order for the attacker’s code to gain root access.


### No automatic patching mechanism


But while Microsoft has released patches for these four critical OMI vulnerabilities, Ohfeld said that there’s no built-in auto-update mechanism in the app, meaning that all Azure Linux VMs remain vulnerable to attacks unless each and every user manually updates the client themselves — something that’s probably not going to happen, mainly because users didn’t know the app was installed on their systems in the first place.


Customers who’d like to apply patches can download and install the [OMI client v1.6.8.1](https://github.com/microsoft/omi/releases/tag/v1.6.8-1) that was released last month on GitHub.


“I think that the most interesting thing here is that the RCE is really easy to exploit,” Alon Schindel, threat research lead for Wiz, told *The Record* in a conversation today. “We’ve already seen some people on Twitter that were able to do so.”


 



#### Tags:
[[OMI]] [[Linux]] [[Microsoft]] [[RCE]] [[(Severity:]] [[Ohfeld]] [[The Record]]
