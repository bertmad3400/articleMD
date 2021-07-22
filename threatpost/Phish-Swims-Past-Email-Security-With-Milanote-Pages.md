# Phish Swims Past Email Security With Milanote Pages
### The “Evernote for creatives” is anchoring a rapidly spiking phishing campaign, evading SEGs with ease.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168021)
+ Date: July 22, 2021  4:53 pm
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2019/09/26105755/fish-1.jpg)
The Milanote app, billed as the “Evernote for creatives” by reviewers, has attracted the notice of cybercriminals who are abusing it to carry out credential-stealing campaigns that skate past secure email gateways (SEGs), researchers said.


Milanote is [a tool](https://milanote.com) for organizing and collaborating on creative projects. Users can arrange their projects into handy visual boards that can be shared and collaboratively edited, with the ability to add notes, images, links, files and so on. It counts several heavy hitters as customers, including Chanel, Facebook, Google, Nike and Uber, among many others.


According to analysis from Avanan [released](https://www.avanan.com/blog/new-attack-leverages-milanote-to-host-phishing-content) Thursday, attackers are looking to hook victims by starting off with a simple email. It has the subject line, “Invoice for Project Proposal.” The email body is pretty bare-bones, saying only, “Hello. See attached invoice for the above referenced project. Please contact me if you have questions or need additional information. Thank you.” It doesn’t contain any personalization, logos or other social-engineering aspects.



“The email itself is pretty standard issue,” Gil Friedrich, CEO and co-founder of Avanan, told Threatpost in an interview. “It gets attention with the subject of ‘Invoice for Project Proposal.’ It’s certainly not the most sophisticated effort in the world, however, it understands what emails can get past static scanners, including, in this case, Milanote.”


Should a target open the attachment, a document opens that contains one line (“I have shared a file with you. Please click link[s] below to download”) followed by a clickable button that says “Open Docs.”


If the person clicks the button, they’re taken to a page hosted in the Milanote service:


Getting Past Security
---------------------


From a cybercriminal point of view, convincing people to click that many times may be a downside to the approach, but the phish isn’t flagged by most SEGs or traditional security systems because the malicious URL is buried so deep in the attack chain. Having a legitimate service involved in the mix helps too, researchers noted.


“[Most] use static scanners to scan attachments or links for malicious payloads,” according to the writeup. “In response, hackers are bypassing those detection mechanisms by nesting the payloads in deeper layers within legitimate services, fooling the static scanners. This is part of a larger trend of hackers utilizing legitimate services to host malicious content. Because the scanner doesn’t go that deep, hackers can leverage these services to host their content and easily send it to users.”


Cybercriminals are implementing this trick in ever-greater numbers, according to Friedrich, across many services.


“All sorts of attacks utilizing static links are skyrocketing,” he told Threatpost. “For example, we’ve seen tremendous phishing attacks leveraging a number of different sites that are Allow Listed – [Google Docs](https://threatpost.com/google-docs-host-attack/166998/), MailGun, HostGator,  among others. We expect this to continue to grow in the near future.”


Cybercriminals Target Collaboration Apps
----------------------------------------


Another aspect of the trend is that with the rise of collaboration platforms, cybercriminals have turned to them to find new ways to social-engineer and evade defenses.


“Work and communication don’t happen on just email. As we’ve seen throughout the pandemic, [work happens everywhere](https://threatpost.com/beyond-zoom-safe-slack-collaboration-apps/154446/),” Friedrich said. “We’re talking to people on Zoom, sharing thoughts on Slack, using whiteboards on Jamboard and thousands of other services. Email is still incredibly important, of course, but there are other places where information is transmitted.”


For hackers, this widens the potential target list.


“Instead of just email, hackers can bring malicious links to where users are. For many of these collaboration apps, it provides an easy in for hackers,” Friedrich said. “Users might have their guard down on such sites, given they haven’t had the same phishing training there. It becomes an easy way to score up a lot of potential targets.”


To protect themselves from the Milanote attack and other similar offensives, users should embrace best practices around phishing, Friedrich advised.


“That means inspecting links before opening, being wary of unfamiliar senders, showing caution around emails about invoices and payments, picking up on any inconsistencies in the sender address and paying close attention to spelling and grammar,” he said.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 


 




#### Tags:
[[Milanote]] [[Friedrich]] [[Threatpost]] [[phishing]] [[ThreatPost]]
