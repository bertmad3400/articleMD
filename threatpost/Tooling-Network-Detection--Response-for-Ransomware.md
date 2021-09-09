# Tooling Network Detection & Response for Ransomware
### Justin Jett, director of audit and compliance at Plixer, discusses how to effectively use network flow data in the fight against ransomware.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169290)
+ Date: September 8, 2021  3:00 pm
+ Author: Justin Jett


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/09/08142255/gate-e1631125398775.jpg)
Everywhere you look, there are new reports coming out about ransomware. And cybercriminals are becoming more aggressive, demanding even more in ransom payments than ever before. According to Palo Alto Networks’ Unit 42, ransom [payments are up](https://www.paloaltonetworks.com/blog/2021/08/ransomware-crisis/) 82 percent in the first half of 2021, with an average payment amount at a record $570,000.


So, with ransoms increasing and cybercriminals becoming more and more rapacious of users’ data, there must be something organizations can do to stop these attacks.


Stopping Ransomware Before it Gets to Your Critical Data
--------------------------------------------------------


It’s important to remember that we can’t prevent all ransomware from gaining access to our networks, but that doesn’t mean organizations have to let it loose to compromise everything. Well-prepared organizations can reduce the impact of ransomware by making sure they have deployed appropriate network-based security solutions.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Employees, contractors, vendors and myriad other individuals can let cybercriminals gain access to your network — be it via phishing emails or by convincing them to access compromised websites — but the systems that they connect to are usually different than the systems that maintain your critical data. So, while your team members might have access to business-critical data stored on other machines, they don’t (shouldn’t) store it on their laptops.


This is extremely important and works as a de-facto firewall for ransomware attacks because the attacker isn’t accessing the critical data upon entry — they must find it first.


To track where the ransomware is looking for business-critical data, organizations often use a network detection and response (NDR) solution. Unlike legacy, signature-based security solutions, NDR solutions use more advanced technologies, like machine learning, to detect suspicious traffic on the network. To learn more about solving for humans and why NDR matters, see this nearby [article](https://threatpost.com/network-detection-response-human-problem/165332/).


What informs those NDR solutions is important, especially when it comes to ransomware. They must be able to track lateral movement.


While having to restore a single employee computer is cumbersome, it doesn’t come close to having to restore petabytes of data from customer or financial systems that have been compromised by ransomware. The key to stopping ransomware is to stop ransomware from getting on the systems that really matter. But how do you prevent the ransomware from getting to those systems? The solution to this lies in lateral movement.


Tracking Movement Across the Network
------------------------------------


Lateral movement is one of the most common techniques used by malicious actors to progressively move throughout the network as they search for critical data. This data is what the hackers really want, since it pays the most in ransoms (after all, nobody would be willing to pay $570,000 to restore a single employee laptop).


While the idea of lateral movement is straightforward, one of the most important reasons for tracking network connections for for it is that it significantly reduces the dwell time for ransomware infections. Additionally, if the organization can detect the ransomware before it has the opportunity to lock out a system, the ransomware can be completely eliminated before any damage is done. The longer the ransomware is on your network, the more devices will be compromised.


If ransomware is given too much time on the network, even if it doesn’t gain access to your most critical data, it could have an impact on day-to-day operations. By tracking the ransomware’s lateral movement, organizations can see where it moved, and, more importantly, which machines were infected. Doing so reduces the number of machines infected and thus reduces the time to recovery.


Tracking lateral movement is only as good as the data being collected. When new machines or new employees connect to the network, organizations should start monitoring those connections right away. Doing so will provide the most visibility and will enable the organization to track malicious movement from all devices on the network.


Additionally, understanding how malicious software is connecting throughout your network requires having an NDR system [capable of collecting](https://www.gartner.com/reviews/market/network-detection-and-response) network flow data and analyzing it. By leveraging flow data, organizations can quickly determine where ransomware—and other malware—are moving across the network. If organizations can ingest high-fidelity flow data into their NDR system, they will have valuable details relating to the network traffic that will further reduce the amount of time that ransomware is left on the network.


This type of information is exportable via [IPFIX](https://en.wikipedia.org/wiki/IP_Flow_Information_Export) and many network hardware vendors support the protocol.


Packet Capture or Flow Data? Which is Better?
---------------------------------------------


Packet capture offers many benefits to network and security professionals. It gives complete details of every connection happening on the network, which means organizations have the fullest visibility possible. Unfortunately, that absolute visibility comes at an unbearable cost.


While it is theoretically possible to use packet capture to detect historical lateral movement, doing so is both cost-prohibitive and resource-intensive. This is because full packet capture requires storing many gigabytes or more of network connection data, which would also require having potentially thousands of PCAP or similar sensors to collect this data.


After all, most network hardware would suffer significant performance degradation if packet capture were happening on the network directly. Since most malware may reside on a single machine for weeks or months before moving, most packet capture solutions would require IT teams to store terabytes or even petabytes of data in packet capture to maintain the historical data. This simply isn’t realistic, given that high-fidelity flow-based metadata is equally effective at detecting lateral movement while requiring a significantly reduced footprint.


What’s Next for Ransomware?
---------------------------


Ransomware isn’t going away. In fact, it’s only going to get worse. In recent news, Australia recently released a [security alert](https://www.cyber.gov.au/acsc/view-all-content/alerts/lockbit-20-ransomware-incidents-australia) alluding to the expected increase in more sophisticated ransomware. With ransomware-as-a-service (RaaS) growing in popularity over the last few years, their spread makes it easier for malicious actors to harm organizations.


But, by using a flow-based NDR system to detect lateral movement, organizations can quickly stop the ransomware from getting to critical business data and systems, reducing the dwell time and further reducing the impact the ransomware can have on the business.


***Justin Jett is the director of audit and compliance at Plixer.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[ransomware]] [[NDR]] [[data,]] [[ransomware.]] [[data.]] [[network.]] [[network,]] [[cybercriminals]] [[doesn’t]] [[isn’t]] [[ThreatPost]]
