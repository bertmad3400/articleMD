# Academics discover hidden layer in China’s Great Firewall
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/academics-discover-hidden-layer-in-chinas-great-firewall/)
+ Date: October 2, 2021
+ Author: Catalin Cimpanu


## Article:
![Academics discover hidden layer in China’s Great Firewall](https://therecord.media/wp-content/uploads/2021/10/China.jpg)

A team of academics from the University of Maryland has discovered a previously hidden layer in China’s Great Firewall censorship system.


Introduced in the late 90s, the Great Firewall (GFW) is a system of middleboxes installed at China’s internet exchange points and internet service providers that allow the government to intercept internet traffic, sniff on its content, and block connections to websites and servers the state doesn’t deem acceptable.


While there are different censorship mechanisms inside China’s Great Firewall that cater to different protocols, its most potent and technically advanced system is the one meant for dealing with HTTPS encrypted web traffic.


Today, this HTTPS censorship mechanism includes two separate systems.


The first, and the oldest, is the one that works by intercepting HTTPS connections in their incipient stages and then looking at a connection data field called SNI, which exposes the domain a user is trying to access.


Even if Chinese censors can’t decrypt the content of the actual HTTPS connection, this SNI field allows the Chinese government to block users from accessing unwanted sites.


The second, [introduced last year](https://geneva.cs.umd.edu/posts/china-censors-esni/esni/), is similar to the first but caters to HTTPS connections that use modern protocols that encrypt the SNI field (as eSNI).


Because this system can’t view what domain users are trying to access, this censorship mechanism is much more blunt because the GFW simply blocks all connections where eSNI fields are detected.


This second system is not broadly deployed, as censors are still testing its capabilities, and very few HTTPS connections are using eSNI in the first place.


### Academics find parallel HTTPS SNI filtering system


But in a research paper [[PDF](https://geneva.cs.umd.edu/papers/foci21.pdf)] published this week, academics from the University of Maryland revealed they found a secondary HTTPS SNI filtering system working in parallel with the first.


“This was actually an accidental discovery, and something we stumbled onto back in 2019,” Kevin Bock, a Ph.D. candidate in the computer science department at the University of Maryland, told *The Record* in an email.


“We started finding weird strategies where [Geneva](https://geneva.cs.umd.edu/) [*a censorship evasion system*] was defeating censorship in the first part of the TLS handshake (where censorship was understood to be occurring), but still failed deeper in the handshake.


“We didn’t fully understand it at the time, but since then, our tooling and understanding of the GFW has improved, and now we understand these strange results,” Bock added.


“We don’t know exactly what this is, but it seems specific to HTTPS – we do not see the same behavior on the other protocols they censor,” the researcher told *The Record*.


“We don’t have any evidence that suggests it’s a test system or dev layer – my gut says that most likely this is just a second set of middleboxes running in parallel with the first, acting as redundancy.”


Bock and his colleagues say the system is just as effective as the first layer in censoring HTTPS traffic, even if it intervenes in the latter stages of a connection.


![China-GFW-Censorship](https://www-therecord.recfut.com/wp-content/uploads/2021/10/China-GFW-Censorship.png)
“This is actually not the first time we’ve discovered the GFW is running multiple middleboxes in parallel – this is just the first time we’ve seen them do it as redundancy for the same protocol,” Bock said.


“A few years ago, a common mental model for the GFW was that it acted a single monolithic entity. In our[paper [PDF]](https://geneva.cs.umd.edu/papers/come-as-you-are.pdf) in 2020, we found evidence that the GFW was actually comprised of different sets of middleboxes running in parallel with each other, each to censor different protocols (so the HTTP censorship middlebox in the GFW is a different system from their HTTPS censorship, and each has its own weaknesses).


“This discovery means that the GFW is now running at least three different middleboxes in parallel to censor HTTPS: two for SNI-based connections and another family of middleboxes entirely to censor ESNI-based connections,” the researcher added.


Below is Bock presenting his team’s findings at the SIGCOMM FOCI 2021 conference.








#### Tags:
[[HTTPS]] [[GFW]] [[middleboxes]] [[SNI]] [[“We]] [[China’s]] [[“This]] [[The Record]]
