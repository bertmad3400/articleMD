# Security company warns of Mitsubishi industrial control vulnerabilities
### Nozomi Networks Labs has discovered five vulnerabilities affecting Mitsubishi safety PLCs.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/security-company-warns-of-mitsubishi-industrial-control-vulnerabilities/)
+ Date: August 5, 2021 -- 03:02 GMT (04:02 BST)
+ Author: Jonathan Greig


## Article:
Unknown

Cybersecurity company Nozomi Networks Labs [has warned](https://www.nozominetworks.com/blog/new-research-uncovers-5-vulnerabilities-in-mitsubishi-safety-plcs) the industrial control system (ICS) security community about five vulnerabilities affecting Mitsubishi safety PLCs.

In a new report, the company said Mitsubishi acknowledged the issues -- which are focused on the authentication implementation of the MELSOFT communication protocol -- after they were discovered at the end of 2020. 

The Japanese manufacturing giant has devised a strategy to patch the issues but Nozomi Networks Labs said software updates for safety PLCs or medical devices often take longer to deploy than other software products. Vendors must go through specific certification processes before patches can be released, the report explained. 

"Depending on the type of device and regulatory framework, the certification procedure could be required for each individual software update," Nozomi Networks Labs researchers wrote.

"While waiting for the patch development and deployment process to be completed, we deployed detection logic for customers of our Threat Intelligence service. At the same time, we started researching more general detection strategies to share with asset owners and the ICS security community at large."

The researchers noted that the vulnerabilities they found "likely" affect more than one vendor and said they were concerned that "asset owners might be overly reliant on the security of the authentication schemes bolted onto OT protocols, without knowing the technical details and the failure models of these implementations."

The security company disclosed the first batch of vulnerabilities [through ICS-CERT](https://us-cert.cisa.gov/ics/advisories/icsa-20-175-01) in January 2021 and another batch more recently, but patches are still not available. 






Mitsubishi has [released a number of mitigations](https://www.mitsubishielectric.com/en/psirt/vulnerability/index.html) and Nozomi Networks Labs urged customers to assess their security posture in light of the advisories. 

The report specifically leaves out technical details or proof of concept documents in an effort to protect systems that are still being secured. 

Researchers discovered the vulnerabilities while researching MELSOFT, which is used as a communication protocol by Mitsubishi safety PLCs and corresponding engineering workstation software GX Works3. 

They found that Authentication with MELSOFT over TCP port 5007 is implemented with a username/password pair, which they said are "effectively brute-forceable" in some cases. 

The team tested multiple methods that gave them access to systems and found that there are even instances where attackers can reuse session tokens generated after successful authentication.

"An attacker that can read a single privileged command containing a session token is able to reuse this token from a different IP after it has been generated, within a window of a few hours," the report said.

"If we chain together some of the identified vulnerabilities, several attack scenarios emerge. It's important to understand this approach as real world attacks are often executed by exploiting several vulnerabilities to achieve the final goal." 

Once an attacker gains access to a system, they can then take measures to lock other users out, forcing the last-ditch option of physically shutting down the PLC to prevent further harm.

Nozomi Networks Labs suggested asset owners protect the link between the engineering workstation and the PLC so that an attacker cannot access the MELSOFT authentication or authenticated packets in cleartext. 

They also suggest protecting access to the PLC so an attacker cannot actively exchange authentication packets with the PLC.





#### Tags:
[[Nozomi]] [[Mitsubishi]] [[MELSOFT]] [[PLC]] [[ZDNet]]
