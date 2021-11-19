# Malicious Python packages caught stealing Discord tokens, installing shells
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/malicious-python-packages-caught-stealing-discord-tokens-installing-shells/)
+ Date: November 19, 2021
+ Author: Catalin Cimpanu


## Article:
![Malicious Python packages caught stealing Discord tokens, installing shells](https://therecord.media/wp-content/uploads/2021/07/PyPI-logo.png)

The operators of the Python Package Index (PyPI) have removed this week 11 Python libraries from their portal for various malicious behaviors, including the collection and theft of user data, passwords, and Discord access tokens and the installation of remote access shells for remote access to infected systems.


According to the security team at DevOps platform JFrog, which discovered this set of malicious libraries, the 11 packages had been downloaded and installed **more than 30,000 times** before the packages were spotted and reported.


Worth mentioning is that the packages did not appear to have been developed by the same author, as each contained a slightly different malicious behavior and method of exfiltrating data from infected systems, as detailed in the table below.




| P**ackage** | **# of downloads** | **Automated detection indicators** | **Description** |
| --- | --- | --- | --- |
| importantpackageimportant-package | 6305**12897** | Shell process with obfuscated input   | Hidden connectback shell to psec.forward.io.global.prod.fastly.net, using the [trevorc2 client](https://github.com/trustedsec/trevorc2/blob/master/agents/trevorc2_client.py) |
| pptest | **10001** | Suspicious version² | Uses DNS to send `hostname+'|'+os.getcwd()+'|'+str(self.get_wan_ip())+'|'+local_ip_str` |
| ipboards | 946 | Sensitive file handling Suspicious version | Dependency confusion, sends user info (username, hostname) via DNS tunneling to b0a0374cd1cb4305002e.d.requestbin.net |
| owlmoon | 3285 | `eval` with obfuscated input  | Discord token stealer trojan. Sends tokens to https://discord.com/api/webhooks/875931932360331294/wA0rLs3xX\_2JgqlfqEfpYoL9zer\_Qs7hpsMbwaDl6-UByE\_ZRHiXm0t1lr-o\_3RFBqBR |
| DiscordSafety | 557 | `exec` with obfuscated input | Discord token stealer trojan. Sends tokens to https://tornadodomain.000webhostapp.com/stlr.php?token= |
| trrfab | 287 | Sensitive file handling Suspicious version  | Dependency confusion, sends user info (id, hostname, /etc/passwd, /etc/hosts, /home) to yxznlysc47wvrb9r9z211e1jbah15q.burpcollaborator.net |
| 10Cent1010Cent11 | 490490 | Shell spawning Suspicious version | Connectback shell to hardcoded address 104.248.19.57 |
| yandex-yt | 4183 | Suspicious version | Prints pwned message and directs to https://nda.ya.ru/t/iHLfdCYw3jCVQZ, could be a malicious domain (currently seems inactive) |
| yiffparty | 1859 | `eval` with obfuscated input | Discord token stealer trojan. Sends tokens to https://discord.com/api/webhooks/875931932360331294/wA0rLs3xX\_2JgqlfqEfpYoL9zer\_Qs7hpsMbwaDl6-UByE\_ZRHiXm0t1lr-o\_3RFBqBR |


Ten of the eleven packages were outright malicious, as it is clear from the table above. One, named yandex-yt, appears to be some sort of test or joke, but one that could easily turn into a malware delivery channel.


One important observation is that two of the 11 packages also abused a new technique called [dependency confusion](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610), a technique where attackers register packages with names that might be used inside closed corporate networks, hoping that their public package gets pulled when the corporate package was deleted and the dependency tree was not updated.


JFrog researchers have published an [in-depth analysis](https://jfrog.com/blog/python-malware-imitates-signed-pypi-traffic-in-novel-exfiltration-technique/) for each of the 11 malicious PyPI packages they have discovered.


This marks the second time this year when JFrog researchers have discovered malicious Python libraries after finding [another eight](https://therecord.media/python-packages-caught-attempting-to-steal-discord-tokens-credit-card-numbers/) earlier this year, in July.





#### Tags:
[[confusion,]] [[trojan.]] [[The Record]]
