# ‘PwnedPiper’: Devastating Bugs in >80% of Hospital Pneumatics
### Podcast: Blood samples aren’t martinis. You can’t shake them. But bugs in pneumatic control systems could lead to that, RCE or ransomware. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168277)
+ Date: August 2, 2021  4:58 pm
+ Author: Lisa Vaas


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/02152007/pneumatic-tube-e1627932019256.jpeg)
Researchers have discovered nine vulnerabilities – collectively dubbed PwnedPiper – in the pneumatic tube systems (PTS) used in more than 80 percent of major hospitals in North America.


The bugs, in Swisslog Healthcare’s Translogic PTS, include hard-coded passwords, unencrypted connections and unauthenticated firmware updates that could lead to remote code execution (RCE). The flaws could give an unauthenticated attacker root control and could let bad actors take over Nexus stations.


The nine critical vulnerabilities are in the Nexus Control Panel, which powers all current models of Translogic pneumatic tube system (PTS) stations sold by [Swisslog Healthcare](https://www.swisslog-healthcare.com/). “All current firmware versions of this device are susceptible to these vulnerabilities,” Armis researchers said.



After an attacker hijacks a Nexus station, it’s all downhill from there, as Armis [reported](https://www.armis.com/research/pwnedpiper) on Monday, with potential ransomware attacks in the mix. “By compromising a Nexus station, an attacker can leverage it for reconnaissance purposes, including harvesting data from the station, such as RFID credentials of any employee that uses the PTS system, details about each station’s functions or location, as well as gain an understanding of the physical layout of the PTS network,” Armis said in a release. “From there, an attacker can take over all Nexus stations in the tube network, and hold them hostage in a sophisticated ransomware attack.”


The Translogic PTS system, used by more than 3,000 hospitals worldwide, is the pneumatic version of a hospital’s veins, arteries and capillaries: The tubes deliver medications, blood, and lab samples throughout a hospital. Modern PTS systems are IP-connected, which enables them to offer advanced features. But in spite of their prevalence, these systems’ security “has never been thoroughly analyzed or researched,” Armis asserted.


Armis’ statement quoted Nadir Izrael, co-founder and CTO at Armis: “This research sheds light on systems that are hidden in plain sight but are nevertheless a crucial building block to modern-day healthcare.”Understanding that patient care depends not only on medical devices, but also on the operational infrastructure of a hospital is an important milestone to securing healthcare environments.”


Were an attacker to take over this tube network, the result could include denial-of-service (DoS), sophisticated ransomware or full blown meddler-in-the-middle (MiTM) attacks that could kneecap a targeted hospital’s critical inner workings.


Attack Scenario
---------------


As an example of how these bugs could lead to compromise up to and including ransomware, Armis outlined a scenario in which an attacker gains access to low-grade internet-of-things (IoT) device to get into a hospital’s network, such as an IP camera that’s connected to the internet. 


From there, they can gain access to the hospital’s internal networks and target the Translogic PTS systems, which are also connected to the hospital’s internal networks. After that, five of the PipedPiper bugs can be used to achieve RCE. 


The attacker can continue by exploiting one of the bugs to compromise a Nexus station. An intruder could then harvest logins from the station, such as the RFID credentials of any staffer who uses the PTS system, details about the system and the layout of the PTS network. 


Moving laterally, the attacker could then compromise all Nexus stations, be they at the hospital’s blood bank, its pharmacy or its lab, for example. The attacker could then trap  medical items in the tubes, shutting down the stations one by one and posting ransomware notes on the stations’ displays. 


“In this volatile state, the hospital’s operations can be severely derailed,” Armis detailed. “Medications supplied to departments, timely delivery of lab samples, and even blood units supplied to operating rooms all depending on constant availability of the PTS.”


Armis doesn’t know of any active exploits, and eight of the nine bugs have been fixed.


The Trouble That Advanced Features Present
------------------------------------------


Translogic PTS system is an advanced system in that it integrates with other hospital systems. While integration presents multiple benefits, such as staff authentication via RFID, it also means that information shared between systems could be leaked or manipulated by an attacker in the case of a system compromise.


Armis gave some examples of what problems a PTS compromise could look like:


Unclogging the Arteries
-----------------------


All of the bugs are patched except one that affects legacy systems. Swisslog said that older station models that are IP-connected (such as the IQ station) share code with the Nexus Control Panel, and are thus likely to be affected by some of these vulnerabilities. Swisslog no longer supports older stations and won’t be releasing a patch for them, according to Armis.


The new, patched version of Nexus Control Panel – version 7.2.5.7 – mitigates the majority of the vulnerabilities. One remaining vulnerability, CVE-2021-37160, is due to be patched in a future release.


Armis discovered the bugs on May 1 and has since been working with Swisslog to understand their impact, to develop and test a patch, and to develop mitigation steps. Swisslog released a [security advisory](https://www.swisslog-healthcare.com/en-us/customer-care/security-information/cve-disclosures) today, Tuesday, that details these flaws:


Cue The Legacy System Upgrading Nightmare
-----------------------------------------


Armis Strategic Product Director Sumit Sehgal joined Threatpost podcast on Tuesday for a deep dive into the PwnedPiper bugs and how this problem goes far beyond the pneumatic tubes. In fact, in spite of the fact that there are multiple flavors of Swisslogic Translogic PTS, they’re all running a deprecated version of Linux that can essentially give an attacker “unfettered access through root” that could enable them “to fully control that Linux environment within the control within the control panel,” he said.


The flaws in the control panel control system allows attackers to not only mess with the functioning of the pneumatic tube system, but it’s also at the very heart of other hospital systems. That makes the Swisslogic PTS “A potential unprotected and malicious endpoint in the environment of the healthcare IT health system,” Sehgal said.


Good luck to the healthcare organizations who’ll be dealing with these critical patches and to those running legacy systems, for whom patching is a nightmare scenario of untangling system dependencies.


For Seghal’s advice on how to prioritize, stay tuned: We’ll have a link to the podcast available here shortly. In the meantime, Armis’ mitigations are below, and you can check out the transcript below that.


Mitigations in the Meantime
---------------------------


Patching vulnerable Translogic PTS stations is “essential,” Armis researchers emphasized, but for those hospitals that can’t exactly spin on a dime, they offered these mitigations to detect and prevent attacks:


Outside of that, good practice includes hardening the access to sensitive systems such as PTS solutions through the use of network segmentation, as is limiting access to such devices through strict firewall rules, researchers advised.


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)Worried about where the next attack is coming from? We’ve got your back. **[REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)** for our upcoming live webinar, How to **Think Like a Threat Actor**, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on **[Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar)**.


Lightly Edited Transcript
-------------------------


**Lisa Vaas:**  Hi, and welcome to the Threatpost podcast. Today we’re joined by Armis Strategic Product Director Sumit Sehgal.


He’s the healthcare pro at Armis, which is an industrial controls cybersecurity outfit. He’s also the former CISO of Boston Medical. We’re really pleased to get him on the show to talk about serious vulnerabilities discovered in pneumatic tube systems.


Sumit could you please give us a quick overview of the PwnedPiper vulnerabilities and how they can be used against hospitals?


**Sumit Sehgal:** Absolutely. Thank you for having me. The focus of this research was looking at control systems that healthcare organizations, specifically hospitals utilize as a foundational element of providing care.


And the Swisslog pneumatic tube system is a critical part of that ecosystem of delivery of care, because it’s largely prevalent in a big piece of the healthcare environment in the U.S. As well as globally. Secondly, it’s been around for more than 30, I would say 20, 30 years at the very minimum.


Right? So where we focused on was the elements of what a pneumatic tube system does in a healthcare environment, which in this case is move, essentially things like lab samples, blood samples, medications from Point A to point B where they’re needed in high urgency scenarios, as well as there is components of the Swisslog.


Pneumatic tube systems that are used for messaging delivery with systems like nurse call management solutions or clinical quality management solutions as well, that look at how care’s being delivered. So what we did in our research is we went through and looked at the control systems, which in this case are called the Nexus control panels that are part of these systems.


Now, one thing to know is. This is not just one type of systems Swisslog pneumatic tube systems come in many different shapes and flavors and different healthcare organizations run different versions of those. But in general, they all use the same standardized hardware behind the scenes. The summary off the PwnedPiper vulnerabilities is that we discovered 9 vulnerabilities that all have been identified through CVE numbers. That’s visible on our website. High-level summary of those are there’s two vulnerabilities that deal with hard-coded passwords for user and root accounts that can be accessed through unsecured Telnet servers.


There’s a privilege escalation vulnerability that can, again, leverage hard-coded credentials to get root access, and then there’s memory corruption vulnerabilities that exist in the TLP 20 protocol. That’s utilized by the pneumatic tube system to process either priority for the transfer of a canister from Point A to point B or in making sure that the canisters from point A to point B reached the correct destination, then they don’t get rerouted or stop in the process. The last ones that we saw were denial of service and then a design flaw that deals with former upgrades on the control panel, which in this case are unencrypted and unauthenticated, which may be an avenue for an attacker to potentially either interrupt the former update procedure or do remote code execution on that.


**Lisa Vaas:** Great. And at this point you don’t know of any active exploits.


**Sumit Sehgal:** that we are aware of. Correct.


**Lisa Vaas:** But the worst of these could lead to a ransomware attack?


**Sumit Sehgal:** Yes. The reason I say that is most of the control panel software behind the scenes runs a deprecated version of Linux behind the scenes and essentially giving somebody unfettered access through root allows them to fully control that Linux environment within the control within the control panel.


So the control system in the control panel, that allows them to not only mess with the functioning of the pneumatic tube system, but it also functions at that point As a potential unprotected and malicious endpoint in the environment of the healthcare IT health system.


**Lisa Vaas:** And this could lead to persistence as well?


**Sumit Sehgal:** Yes, because of this persistence, not only within the control system, but because it has that for connectivity and it’s unknown and it’s at that point fully, essentially to fully own from an access and network topology perspective. There are other reconnaissance downstream and upstream that can be done.


Since you have access to the full Linux distro and the, the attacker can upload additional tools.


**Lisa Vaas:** That’s bad. So the patch only covers eight out of the nine vulnerabilities, the patch that was released today Tuesday morning? So there’s still an issue for legacy systems, which are not going to get a patch.


Can we talk about that? How complicated it is that whole ecosystem?


**Sumit Sehgal:**  It is important for healthcare organizations to understand the criticality of the workflows that are affected by the pneumatic tube solution in their environment and they should be leveraging not just in time scans, but a real time vulnerability management process that allows them to bring together the findings that they receive from a security perspective and really help them articulate how do those security vulnerabilities impact the clinical risk side? That second part is very, very important because that is what they need to prioritize, how they deal with this. For not only the, the ninth one that hasn’t been patched, but like you said, for legacy. Other legacy ecosystem parts that may be in their environment.


Pneumatic tubes is just one part of it. A healthcare organization should not forget about things like water control systems, water control systems are essential. Part of things like irrigation during surgeries.


If you don’t have proper water, you can’t do procedures. Same thing with gas and suction. Oxygen is a critical component of care. Same thing with elevator control systems. You can’t move patients. If you have a 30-floor building that you’re doing care in, right. If the elevator’s out.


So those are examples of the industrial control system that are leveraged in healthcare organizations that serve as the bedrock on top of which the medical devices function appropriately to be able to provide care. So there’s legacy that you have to deal with from a syslog perspective, there’s legacy from an ecosystem of industrial control system and OT operating technologies that healthcare physicians have.


And then there’s legacy in the medical device ecosystem state that folks need to also understand that help understand the whole ecosystem of what roles these devices play and how information flows through them as it’s going upstream and downstream in the path of a patient journey.


**Lisa Vaas:** We take so much of this for granted. Whenever it comes to industrial control systems, I’m always just caught off guard somehow. Oh, yeah, there there’s that too. Like the elevators and the water irrigation and surgery. Thank you for painting that vivid picture of what’s at stake here. And it’s a different scenario when it comes to prioritization, depending on what kind of hospital you’re talking about, right?


**Sumit Sehgal:** There is. Depending upon the scope, like every industry, this complexity where practices and healthcare specific specifically in hospitals go back 40, 50 years.


I give the example of. Number one, there’s a difference of scale. So a large academic medical center that has 150,000 visits going on in the E.R. Is going to function differently from a priority perspective, with one that only has 20,000 visits going on in a year, right. They may have different kinds of patients.


They may be focused on different areas of the different specialties of making the revenue targets to maintain operations. So when I talk about prioritizing, it’s very important to match information, security, vulnerability, and risk output to clinical safety and clinical quality.


That’s what that process does, is it helps you identify for the health system you’re in, in the market that you’re in and for the patient mix that you’re treating. With the appropriate specialty, where should you focus in on? Because when you’re dealing with something like this and the ecosystem in general, it can be overwhelming for any size of health decision to deal with this quickly at scale, it just doesn’t work, especially when these are environments, these ecosystems have been around for 20, 30 years. Right? So, so there’s a process that needs to happen. There’s obviously change management that needs to be done appropriately. So, so we are not introducing additional potential patient safety problems by fixing. Issues as well.


**Lisa Vaas:** Yeah, that would be bad.


Well, we wish the best of luck to the healthcare organizations that are dealing with this. Godspeed in getting the patches installed. And thank you so much to Armis. You guys really keep an eye on industrial controls, security, and we’re always interested in the stuff that you do.


So thank you for this.


**Sumit Sehgal:** Yeah, industrial controls and healthcare stuff as well.


**Lisa Vaas:** Healthcare of course, and every place where those intersect, which is a lot of places. Well, great. Thank you so much, Sumit. I really appreciate you coming today.


**Sumit Sehgal:** Absolutely. Thank you for the opportunity.




#### Tags:
[[Armis]] [[Sumit]] [[it’s]] [[there’s]] [[Swisslog]] [[Vaas:]] [[Sehgal:]] [[Translogic]] [[hospital’s]] [[system,]] [[ThreatPost]]
