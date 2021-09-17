# How surveillance capitalism will totally transform the domain name system
### APNIC's Geoff Huston predicts a world where paranoid apps add 'oblivion' to the DNS to protect privacy. Their privacy, not yours.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/how-surveillance-capitalism-will-totally-transform-the-domain-name-system/)
+ Date: September 17, 2021 -- 03:57 GMT (04:57 BST)
+ Author: Stilgherrian 


## Article:
Unknown

![concept word DNS on cubes on a beautiful gray blue background](https://www.zdnet.com/a/hub/i/r/2020/11/12/04331d02-c3c4-47c6-9b82-957f0929455c/resize/1200xauto/53aab3595b0e2b13cf9824a4f56b2b3f/istock-1224413361.jpg)
 Image: Getty Images/iStockphoto
 The economics of surveillance capitalism and a world of paranoid apps will transform the domain name system (DNS), says Geoff Huston, chief scientist at APNIC Labs, part of the Asia Pacific Network Information Centre. 


Knowing the domain names of the websites you visit, or servers that apps access on your behalf, is valuable intelligence. DNS traffic is especially valuable because it reflects what users are doing in real time. 

"The names you asked for, and when you ask for them, say an awful lot about you," Huston said in his [presentation](https://www.youtube.com/watch?v=ftn9zIdhoEA&t=413s) to the APNIC 52 conference on Wednesday. 

"The network betrays you. You're leaving big, filthy, muddy footprints on the carpet, mate. We can see where you're going. And that's the problem," he said. 

"Real-time data, right here, right now. Not last week, not last month. This second. You couldn't get more valuable." 

Others with more noble motives are monitoring DNS traffic too, looking for the telltale signs of malicious activity, such as the rapidly-changing domain names used by botnets. 

And as Edward Snowden revealed in 2013, the members of the Five Eyes signals intelligence agencies are also keen on sucking up all that DNS traffic. 






"All kinds of folk actually spread DNS information all over the place," Huston said. 

"The problem is, it doesn't matter what your motives are, good or bad. Sniffing is sniffing. An invasion of privacy is invasion of privacy, irrespective of the colour of the hat you're wearing. And this is not good." 

###  Grafting privacy onto decades-old protocols

The core DNS protocols date back to the 1980s, and they're based on a domain name structure that was developed in the 1970s. Everything happens out in the open, unencrypted. 

"How can we stop folk crowding around the digital exhaust pipe sniffing these fumes?" asks Huston. 

There are methods for preventing third parties from snooping on your DNS traffic, but they haven't seen wide adoption. 

One way to make DNS surveillance more difficult is to use a public open DNS server, such as Google's 8.8.8.8, Cloudflare's 1.1.1.1, OpenDNS, or Quad9 rather than your local ISP's servers -- because ISPs have been known to sell their DNS logs to advertisers. 

That can be combined with using an encrypted DNS connection, such as [DNS over TLS](https://en.wikipedia.org/wiki/DNS_over_TLS), [DNS over HTTPS](https://en.wikipedia.org/wiki/DNS_over_HTTPS) (DoH), or DNS over the more lightweight [QUIC](https://en.wikipedia.org/wiki/QUIC) protocol. 

If you do that, you're doing a "tolerably good job" of hiding in the crowd, Huston said. 

"But that first part of the bargain? I've got to trust Google. Yeah right. I've got to trust the very folk who are experts in assembling my profile." 

To put it another way: If we have to compromise our privacy to a third party, which third party represents the least risk to us, both now and in the future? It's a difficult choice. 

But wait. Maybe we don't have to compromise our privacy at all. 

###  Enter Oblivious DNS, a cryptographically private DNS name space

One innovative solution is Oblivious DNS, first written up as a [draft engineering standard](https://datatracker.ietf.org/doc/html/draft-annee-dprive-oblivious-dns-00) in 2018 and a [formal paper](https://odns.cs.princeton.edu/pdf/pets.pdf) [PDF] in 2019. 

"The concept is delightfully simple," Huston wrote in 2020, although some might argue with his use of the word "simple" once they read his [explanation](https://blog.apnic.net/2020/12/16/improving-the-privacy-of-dns-and-doh-with-oblivion/). 

ODNS uses a chain of DNS servers interacting via a pipeline of encrypted transactions. The details will be fascinating for DNS aficionados, but the overall strategy is easy to explain. 

The DNS server close to you knows who you are, so it can return the answer to you, but not what your query was because it's encrypted. 

The DNS server at the other end knows what DNS query it has to resolve, because you used that server's public key to encrypt the transaction, but not who asked for it. 

A similar approach called Oblivious DoH (ODoH), described in a [draft standard](https://datatracker.ietf.org/doc/html/draft-pauly-dprive-oblivious-doh-02) in 2020, wraps the entire DNS transaction in an encrypted envelope. 

The advantage of ODoH is that it doesn't try to cram everything into the existing DNS packet format, meaning it can be slightly more elegant. The disadvantage is that it requires separate infrastructure from the existing DNS. 

But why would anyone pay for all this? 

###  Huston's future of bloated, paranoid apps

"In terms of economics, the DNS is a wasteland," Huston told APNIC 52. 

"I don't pay for queries, you don't pay for queries. Who funds all this? Well, my ISP funds a lot of it. And it sort of comes out of what I pay them," he said. 

That means there's no incentive for ISPs to improve DNS privacy. 

"For ISP fees, the DNS becomes a part of Mr Cost, it's not Mr Income, and so there's a lot of resistance to making Mr Cost grow bigger because that's the way you basically kill your business." 

The public servers are there, but who funds them? And how many users will change their DNS settings on their devices anyway? 

"In some ways, improving the DNS is a labour of love. It's not a labour for wealth and profit," Huston said. 

"Most folk just simply use their ISP's resolver, because that's the one you're paying for, and that's the one person who actually has an obligation to do this for you... So by and large, open DNS resolvers aren't really going to take the DNS and run away over the hills." 

Huston thinks there's one place where the privacy-protecting DNS protocols might take hold, though it won't be for your benefit: inside the apps on your devices. 

Facebook's mobile app, for example, weighs in at more than 200 megabytes because it contains an entire operating system, including an entire network stack. 

"Facebook is paranoid about a number of things. It's paranoid about the platform snooping on it. It's paranoid about other applications on the same platform snooping on the Facebook app," Huston said. 

"Facebook is incredibly valuable. It's spent a lot of time and money understanding me, and assembling a profile of me that it can sell to advertisers. The last thing it wants to do is to give any of that information away to anyone else. It's their data," he said. 

"Applications that divorce themselves from the DNS infrastructure as we know it is an inevitable and near-term future." 

Huston sees this progression as part of broader, historical waves of change that have "played out right now in front of our very eyes". 

The internet has gradually been transforming from network-centric services, to platform-centric services, to application-centric services. 

"The DNS is being swept up with this, and almost every single part of the DNS changes as soon as the DNS becomes sucked into application space," he said. 

"Single coherent namespace? Nah, historical rubbish. Because the entire namespace then becomes application-centric, and different applications will have a different namespace to suit their needs." 

### Related Coverage

* [Security researchers warn of TCP/IP stack flaws in operational technology devices](/article/security-researchers-warn-of-tcpip-stack-flaws-in-operational-technology-devices/)
* [OMIGOD: Azure users running Linux VMs need to update now](/article/omigod-azure-users-running-linux-vms-need-to-update-now/)
* [Bitdefender releases universal decryptor for REvil/Sodinokibi victims hit before July 13](/article/bitdefender-releases-universal-decryptor-for-revilsodinokibi-victims-hit-before-july-13/)
* [Google is backing security reviews of these key open source projects](/article/google-is-backing-security-reviews-of-these-key-open-source-projects/)
* [OWASP updates top 10 vulnerability ranking for first time since 2017](/article/owasp-updates-top-10-vulnerability-ranking-for-first-time-since-2017/)





#### Tags:
[[DNS]] [[Huston]] [[said.]] [["The]] [[apps]] [[ISP]] [[APNIC]] [[it.]] [[ZDNet]]
