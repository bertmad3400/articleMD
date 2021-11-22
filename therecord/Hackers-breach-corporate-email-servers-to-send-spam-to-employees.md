# Hackers breach corporate email servers to send spam to employees
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/hackers-breach-corporate-email-servers-to-send-spam-on-employees/)
+ Date: November 22, 2021
+ Author: Catalin Cimpanu


## Article:
![Hackers breach corporate email servers to send spam to employees](https://therecord.media/wp-content/uploads/2021/11/email.jpg)

A threat actor has hacked Microsoft Exchange email servers across the world in order to gain access to their internal messaging capabilities and send malicious emails to company customers and employees in the hopes of infecting them with malware.


In a [report](https://www.trendmicro.com/en_us/research/21/k/Squirrelwaffle-Exploits-ProxyShell-and-ProxyLogon-to-Hijack-Email-Chains.html) on Friday, security firm Trend Micro said the attackers specifically targeted Exchange servers that haven’t been patched for old vulnerabilities like **ProxyLogon**(CVE-2021-26855) and **ProxyShell**(CVE-2021-34473 and CVE-2021-34523).


Once the attackers gained access to the server, Trend Micro said they used a Powershell feature to read and interact with the server email storage system, and they hijacked existing conversations by inserting and sending new replies to all participants.


![TM-Squirrelwaffle-chain](https://www-therecord.recfut.com/wp-content/uploads/2021/11/TM-Squirrelwaffle-chain.png)Image: Trend Micro
According to researchers, the replies contained links to malicious Excel documents that contained malicious macro scripts that, when a user allowed to run, would install a version of the **Squirrelwaffle** malware.


[First spotted in September 2021](https://security-soup.net/squirrelwaffle-maldoc-analysis/), this is a new malware operation that was built on the model of cybercrime services like Emotet, Dridex, and TrickBot, allowing the Squirrelwaffle gang to rent access to their botnet of infected systems to other gangs.


Supported by a vast spam operation, the Squirrelwaffle gang was seen as Emotet’s replacement—until Emotet itself [made a comeback last week](https://therecord.media/emotet-botnet-returns-after-law-enforcement-mass-uninstall-operation/).


![TM-Squirrelwaffle-chain-execution](https://www-therecord.recfut.com/wp-content/uploads/2021/11/TM-Squirrelwaffle-chain-execution.png)Image: Trend Micro
### A clever new technique bound to be replicated


The incidents noted by Trend Micro also mark a rare instance where a threat actor breached an email server just to run a spam campaign.


“The attacker also did not drop or use tools for lateral movement after gaining access to the vulnerable Exchange servers, so that no suspicious network activities will be detected,” the Trend Micro team explained.


“Additionally, no malware was executed on the Exchange servers that will trigger any alerts before the malicious email is spread across the environment.”


Trend Micro also noted that delivering malicious spam using this technique to reach a company’s own users, on the internal domain, also decreased the possibility of security tools detecting or stopping the attack, as email getaways would not be able to filter or quarantine any of the emails sent this way.


The originality and effectiveness of this technique almost ensure that this new spam method is now bound to be replicated by other groups.


Patching Exchange servers is one way of keeping systems safe, but there are countless other Exchange bugs that could be abused as an entry point, so keeping Exchange servers up to date with security patches at all times is recommended.





#### Tags:
[[Squirrelwaffle]] [[The Record]]
