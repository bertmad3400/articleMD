# Ad-blocker caught injecting ads in search results
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/ad-blocker-caught-injecting-ads-in-search-results/)
+ Date: October 14, 2021
+ Author: Catalin Cimpanu


## Article:
![Ad-blocker caught injecting ads in search results](https://therecord.media/wp-content/uploads/2021/10/AllBlock-site.png)

Cyber-security firm Imperva said it discovered a malicious browser extension named AllBlock, available for both the Chrome and Opera browsers, that has been injecting ads and referral affiliate codes inside search results.


The discovery took place in August this year when Imperva researchers said they identified a domain that was hosting a malicious script that contained ad injection capabilities.


A subsequent investigation linked the script to infrastructure used by the [AllBlock](https://allblock.net/en/) ad-blocker extension, Imperva researchers Johann Sillam and Ron Masas said in a [report](https://www.imperva.com/blog/the-ad-blocker-that-injects-ads/) published yesterday.


According to their findings, the malicious behavior was described as follows:


* Once users installed the extension, AllBlock would inject code into every new tab.
* The code would block legitimate ads, but it would also collect a list of URLs present on the page.
* The list would be sent to a remote server, which would reply with a list of links that needed to be replaced or injected into the page, usually inside search engine results.
* The links typically contained affiliate codes that allowed scammers to earn profits on new user registrations or product purchases.


Sillam and Masas said they believed the AllBlock extension was part of a larger distribution campaign that most likely involved more malicious browser extensions.


Based on some indicators, like IP addresses and domain names, the Imperva team believed this was part of a malware distribution operation called [PBot](https://medium.com/walmartglobaltech/not-your-same-old-adware-anymore-pbot-updates-6d43b159ab35).


An AllBlock spokesperson did not return an email seeking comment on Imperva’s findings.


At the time of writing, Opera has removed the AllBlock extension from its site, while the Chrome extension is [still available](https://chrome.google.com/webstore/detail/allblock/nfofcmcpljmjdningbllljenopcmdhjf?hl=en) on the official Chrome Web Store.


![AllBlock extension](https://www-therecord.recfut.com/wp-content/uploads/2021/10/AllBlock-1024x808.png)Image: The Record



#### Tags:
[[AllBlock]] [[Imperva]] [[The Record]]
