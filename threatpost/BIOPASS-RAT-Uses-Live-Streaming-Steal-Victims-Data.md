# BIOPASS RAT Uses Live Streaming Steal Victims’ Data
### The malware has targeted Chinese gambling sites with fake app installers.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=167695)
+ Date: July 12, 2021  4:30 pm
+ Author: Becky Bracken


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/05/21090543/Rat-in-drain-pipe-e1621602355728.jpeg)
Online gambling companies in China are being targeted by a new remote access trojan (RAT) which, in addition to its predictable features — like file assessment and exfiltration — takes the novel approach of using live streaming to spy on the screens of its victims.


The malware was identified by a team of threat researchers at Trend Micro, and named [BIOPASS RAT](https://www.trendmicro.com/en_us/research/21/g/biopass-rat-new-malware-sniffs-victims-via-live-streaming.html).


“What makes BIOPASS RAT particularly interesting is that it can sniff its victim’s screen by abusing the framework of Open Broadcaster Software (OBS) Studio, a popular live streaming and video recording app, to establish live streaming to a cloud service via real-time messaging protocol (RTMP),” the Trend Micro team reported. “In addition, the attack misuses the object storage service (OSS) of Alibaba Cloud (Aliyun) to host the BIOPASS RAT Python scripts as well as to store the exfiltrated data from victims.”



Researchers said the [watering-hole attack](https://threatpost.com/cisco-asa-bug-exploited-poc/167274/) typically pops us and looks like a benign support chat window. Once installation begins, the malware checks to see whether the victim is already infected with BIOPASS RAT, the report explained. If so, it stops. If not, the researchers observed, the script will start displaying the fraudulent content on the victim’s screen, which tells the user they need to install either Flash of Silverlight, the Trend Micro team added, directing them to a malicious loader.


Once a new login is created, the malware creates and runs various scheduled tasks which can load Cobalt Strike or a BPS backdoor, the report explained. The task labeled “big.txt” delivers the main BIOPASS RAT functionality, which the Trend Micro team added is compiled with Nuitka, PyArmor and PyInstaller.


**BIOPASS RAT’s ‘Scheduled Tasks’**
-----------------------------------


“We also noticed the path string ‘ServiceHub,’ which is a path to the extracted Python runtime,” the Trend Micro team added. “After the hex decoding of the arguments, we get a Python one-liner that downloads additional Python scripts from the cloud.”


Once BIOPASS RAT is up and running it looks for a backdoor, creates a backdoor, if necessary and adds a timestamp, Trend Micro’s researchers found. Then, it loads a Python script labeled “online.txt” that opens an HTTP server and listens on port numbers:  43990, 43992, 53990, 33990, 33890, 48990, 12880, 22880, 32880, 42880, 52880, or 62880.


“The HTTP server does nothing but returns string “BPSV3″ to request,” the report added. “A second HTTP server will also be created to listen on one of the aforementioned port numbers. The second HTTP server behaves the same as the first but returns a string, ‘dm\_online’, instead. These are the markers of infection as previously mentioned. After the servers are established and running, the backdoor creates an execution root directory in the folder “%PUBLIC%/BPS/V3/”.”


Then BIOPASS RAT will access the root directory and find a file named “bps.key” which has the user ID created for the victim by the command-and-control server (C2). If one isn’t found, the report said, the C2 server will assign one.


**Streaming, Screenshots, Files, Even Network Sniffing**
--------------------------------------------------------


From there BIOPASS RAT gets everything — the desktop is monitored and live streamed to the cloud with RTMP live streaming; PNG screenshots of the desktop are uploaded and a shell command triggers a Python function that can kill itself then restart through its scheduled tasks, the report added.


BIOPASS RAT even collects the victim’s cookies and login data files.


The attacker-controlled account is hosted on Alibaba Cloud OSS, the Trend Micro researchers reported, adding they have not received any response from Alibaba after reporting the malicious activity.


Theyalso detected two worrisome Python plug-ins [deployed by Cobalt Strike](https://threatpost.com/cobalt-strike-cybercrooks/167368/) that grabs WeChat Windows messages.


“The script ‘getwechatdb’ is used for exfiltrating the chat history from the WeChat Windows client,” the report warned. “The script will detect the version of the installed WeChat client and grab the decryption key and the user ID. The predefined list of offsets is used to locate where the decryption key and the user ID are embedded.”


Then the script sends the WeChat messages to the cloud with the associated client ID number and decryption key.


The second plugin can inject malicious code into a target’s web service with WinDivert, which monitors and controls Windows network traffic, the report said.


The team’s research led them to conclude the BIOPASS RAT has many links with [APT41,](https://threatpost.com/apt41-operatives-indicted-hacking/159324/) also known as the [Winnti group](https://threatpost.com/microsoft-exchange-servers-apt-attack/164695/), which regularly uses stolen certificates from game studios for its malware. Trend Micro points out the BIOPASS RAT certificates were stolen from South Korean and Taiwanese game studios.


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***


 


 




#### Tags:
[[BIOPASS]] [[malware]] [[cloud]] [[HTTP]] [[WeChat]] [[Alibaba]] [[Windows]] [[ThreatPost]]
