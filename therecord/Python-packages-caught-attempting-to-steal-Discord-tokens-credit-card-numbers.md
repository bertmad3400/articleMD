# Python packages caught attempting to steal Discord tokens, credit card numbers
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/python-packages-caught-attempting-to-steal-discord-tokens-credit-card-numbers/)
+ Date: July 29, 2021
+ Author: Catalin Cimpanu


## Article:
![Python packages caught attempting to steal Discord tokens, credit card numbers](https://therecord.media/wp-content/uploads/2021/07/PyPI.png)

The operators of the Python Package Index (PyPI), the official repository for Python components, have removed eight libraries this week that contained malicious code.


Discovered by the JFrog security team, formerly known as VDOO, the eight packages can be grouped into two categories based on the malicious operations they performed.


Two of the eight allowed a remote attacker to run malicious commands on a victim’s device by making the infected host connect to an attacker’s IP address on TCP port 9009, and then execute any malicious Python code provided by this server.


**PyPI packages allowing RCE:**[**pytagora**](https://pypi.org/project/pytagora/#description), [**pytagora2**](https://pypi.org/project/pytagora2/)(uploaded by a user named **leonora123**)


The other six PyPI packages worked primarily as stealers. Once installed on a developer’s computer, they collected data from the infected host with a focus on general system information, Discord tokens (scraped from predetermined disk locations), and payment card information (extracted from locally installed browsers such as Google, Opera, Brave, and Yandex).


**Python packages acting as stealers:** [**noblesse**](https://pypi.org/project/noblesse/), [**genesisbot**](https://pypi.org/project/genesisbot/), [**are**](https://pypi.org/project/aryi/), [**suffer**](https://pypi.org/project/suffer/), [**noblesse2**](https://pypi.org/project/noblesse2/), [**noblessev2**](https://pypi.org/project/noblessev2/) (first three developed by user **xin1111**, while the last three by user **suffer**)


Based on statistics gathered through third-party service Pepy, the JFrog team said the eight libraries were downloaded more than 30,000 before being removed from the PyPI portal.


An in-depth [technical report](https://jfrog.com/blog/malicious-pypi-packages-stealing-credit-cards-injecting-code/) about each library’s technical capabilities is available on the JFrog blog.




---


This week’s incident is also not that out of the ordinary. Malicious packages make it on the official PyPI repository on a regular basis, along with the official repositories of many other programming languages.


For example, security researchers previously discovered malicious PyPI packages that contained a [hidden backdoor targeting Linux systems](https://blog.reversinglabs.com/blog/suppy-chain-malware-detecting-malware-in-package-manager-repositories), PyPI packages that [opened reverse shells on infected hosts](https://www.zdnet.com/article/twelve-malicious-python-libraries-found-and-removed-from-pypi/), and PyPI packages that [stole SSH and GPG keys](https://www.zdnet.com/article/two-malicious-python-libraries-removed-from-pypi/).


Furthermore, Discord tokens have also been at the center of incidents on the npm (JavaScript) repository at least on two [different](https://www.zdnet.com/article/malicious-npm-package-caught-trying-to-steal-sensitive-discord-and-browser-files/) [occasions](https://blog.sonatype.com/discord.dll-successor-to-npm-fallguys-).


This particular batch of malicious libraries is of particular interest to their victims because they also might have collected payment card information that could be abused for fraudulent transactions.


While Discord tokens can be revoked and SSH keys can be changed, dealing with fraudulent transactions and canceling and changing payment cards is a far lengthier and complicated process that many victims will now have to get ahead of.





#### Tags:
[[PyPI]] [[JFrog]] [[The Record]]
