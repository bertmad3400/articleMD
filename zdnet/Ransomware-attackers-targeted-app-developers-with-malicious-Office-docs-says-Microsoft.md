# Ransomware attackers targeted app developers with malicious Office docs, says Microsoft
### Hackers linked to ransomware deployments used a recently discovered flaw to target application developers.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/ransomware-attackers-targeted-app-developers-with-specially-crafted-office-docs-says-microsoft/)
+ Date: September 16, 2021 -- 12:20 GMT (13:20 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft has detailed how it recently saw hackers exploiting a dangerous remote code execution vulnerability in the MSHTML [aka Trident rendering engine](https://www.zdnet.com/article/microsoft-to-make-rendering-engine-changes-with-spartan-ie-in-windows-10/) of Internet Explorer through rigged Office documents and targeted developers.

Microsoft security researchers discovered the flaw being actively exploited on Windows systems in August and [this week's Patch Tuesday update included a patch](https://www.zdnet.com/article/microsoft-september-2021-patch-tuesday-remote-code-execution-flaws-in-mshtml-open-management-fixed/) for the previously unknown bug, tracked as [CVE-2021-40444](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40444).  


The attacks were not widespread and the vulnerability was used as part of an early stage attack that distributed custom Cobalt Strike Beacon loaders. Cobalt Strike is a penetration testing tool. 

**SEE:** [**Don't want to get hacked? Then avoid these three 'exceptionally dangerous' cybersecurity mistakes**](https://www.zdnet.com/article/dont-want-to-get-hacked-then-avoid-these-three-exceptionally-dangerous-cybersecurity-mistakes/)

Rather than the work of state-sponsored hackers, Microsoft found the loaders communicated with infrastructure that it links to several cyber-criminal campaigns, including human-operated ransomware, [according to Microsoft's analysis of the attacks](https://www.microsoft.com/security/blog/2021/09/15/analyzing-attacks-that-exploit-the-mshtml-cve-2021-40444-vulnerability/). 

The social-engineering lure used in some of the attacks suggesting an element of deliberate targeting, Microsoft said: "The campaign purported to seek a developer for a mobile application, with multiple application development organizations being targeted." 

At least one organization that was successfully compromised by this campaign was previously compromised by a wave of similarly themed malware, Microsoft said. In a later wave of activity, however, the lure changed from targeting application developers to a "small claims court" legal threat.






The attackers in this case were using the IE rendering-engine flaw to load a malicious ActiveX control via an Office document. 

Despite the attack gaining access to affected devices, the attackers still relied on stealing credentials and moving laterally to affect the entire organization. Microsoft recommends customers apply Tuesday's patch to fully mitigate the vulnerability, but also recommends hardening the network, cleaning up key credentials, and taking steps to mitigate lateral movement. 

**SEE:** [**Half of businesses can't spot these signs of insider cybersecurity threats**](https://www.zdnet.com/article/half-of-businesses-cant-spot-these-signs-of-insider-cybersecurity-threats/)

Microsoft considers this attack to be the work of an emerging or "developing" threat actor and is tracking the use of the Cobalt Strike infrastructure as DEV-0365. It seems to be operated by a single operator. However, Microsoft believes that follow-on activity, for example, delivered the Conti ransomware. The software giant suggests it could be a command-and-control infrastructure that's sold as a service to other cybercriminals. 

"Some of the infrastructure that hosted the oleObjects utilized in the August 2021 attacks abusing CVE-2021-40444 were also involved in the delivery of BazaLoader and Trickbot payloads — activity that overlaps with a group Microsoft tracks as DEV-0193. DEV-0193 activities overlap with actions tracked by Mandiant as UNC1878," Microsoft notes. 

The BazaLoader malware has been used by [malicious call center operators](https://www.zdnet.com/article/microsoft-warns-these-attackers-can-go-from-first-contact-to-launching-ransomware-in-just-48-hours/) who use social engineering to trick targets into calling operators who attempt to trick victims into voluntarily installing malware. The groups do not use malicious links in emails reaching out to targets, thereby bypassing common email-filtering rules.





#### Tags:
[[Microsoft]] [[ZDNet]]
