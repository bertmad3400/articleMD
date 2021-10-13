# Student finds zero-days in Exterity devices while rick-rolling school district
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/student-finds-zero-days-in-exterity-devices-while-rick-rolling-school-district/)
+ Date: October 13, 2021
+ Author: Catalin Cimpanu


## Article:
![Student finds zero-days in Exterity devices while rick-rolling school district](https://therecord.media/wp-content/uploads/2021/10/Exterity.jpg)

An Illinois teenager has found a zero-day vulnerability in Exterity IPTV systems during a [rick-roll prank](https://en.wikipedia.org/wiki/Rickrolling) he pulled off on his school district before graduation.


On April 30, this year, Minh Duong and a group of close friends took over all networked TVs and other displays inside the six high-schools part of the Indian Township High School District 214 to play Rick Astley’s infamous “Never Gonna Give You Up” song disguised as an important announcement.


The hack, detailed in a step-by-step [blog post](https://whitehoodhacker.net/posts/2021-10-04-the-big-rick) published last week, involved scanning the school network for connected devices, analyzing their firmware for bugs, and deploying a payload for a carefully timed attack that took over school TV and displays during a recess to prevent interfering with classes or other exams.


The result of all this careful planning was a resounding success, as documented on social media by some of the district’s students.








The hack also took years to arrange, Minh told *The Record* in an email interview last Thursday.


“The earliest scan log I could find in our archive was timestamped on November 28, 2017, and we started documenting network resources on December 3,” Minh told us.


“At the time, we were most interested in the security cameras since they seemed to be the more critical issue; anyone on the network could connect to any camera at any building without authentication,” Minh added.


### Exterity zero-days still unpatched


But a crucial part in successfully executing the prank was a series of privilege escalation vulnerabilities in Exterity IPTV products that the district was using to stream and control its internal security cameras and networked displays.


“One of these bugs was a simple GTFO-bin, but the other two are novel vulnerabilities that I cannot (and should not) publish,” he explained.


Minh, who is now attending the University of Illinois at Urbana-Champaign, said he contacted the vendor about reporting the two zero-days but did not hear back from the company.


“I can’t confirm if these issues have been patched at some point down the road since all their firmware updates are locked behind a customer portal, but I can say that they are present in late 2020 updates,” he told us.


An Exterity spokesperson did not respond to a request for comment.


### District officials had a sense of humor


As for Minh and his friends, none got in trouble with their local school district administration.


A big part in this played the comprehensive report Ming sent to the school’s IT staff, detailing their findings and how the hack was executed.


“In my initial communication with the D214 administration, the director labeled the Big Rick as a ‘white-hat hack’ and I still disagree with that statement months later,” Minh said, sharing with *The Record* that he still has questions and regrets about the prank, months after it happened.


“I expected feedback criticizing the decisions I made regarding responsible disclosure, and I completely agree with the statements they carried: I should have asked for permission, what I did was illegal, and I was lucky to not have been arrested. I never believed what I did was ‘ok,’ even when others told me it was,” Minh told us.



> I hope this will be the most unethical thing I will ever do security-wise.
> 
> Minh Duong


Minh said he is now “definitely looking for a career in cybersecurity.”





#### Tags:
[[Minh]] [[Exterity]] [[us.]] [[The Record]]
