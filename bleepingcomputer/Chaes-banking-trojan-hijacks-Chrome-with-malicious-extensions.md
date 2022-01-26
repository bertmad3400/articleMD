# Chaes banking trojan hijacks Chrome with malicious extensions
### A large-scale campaign involving over 800 compromised WordPress websites is spreading banking trojans that target the credentials of Brazilian e-banking users.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/chaes-banking-trojan-hijacks-chrome-with-malicious-extensions/
+ Date: 2022-01-26T11:39:18-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/09/23/Chrome.jpg)

![Google Chrome](https://www.bleepstatic.com/content/hl-images/2021/09/23/Chrome.jpg)


A large-scale campaign involving over 800 compromised WordPress websites is spreading banking trojans that target the credentials of Brazilian e-banking users.


The trojan used in this campaign is called 'Chaes,' and according to researchers from Avast, its been actively spreading since late 2021.


Although the security firm notified the Brazilian CERT, the campaign is ongoing, with hundreds of websites still compromised with malicious scripts that push the malware.


The attack chain
----------------


When the victim visits one of the compromised websites, they are served with a pop-up that requests them to install a fake Java Runtime app.



![Warning urging the user to download Java](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/java.jpg)**Warning urging the user to download Java**  
*Source: Avast*
The MSI installer contains three malicious JavaScript files (install.js, sched.js, sucesso.js) that prepare the Python environment for the next stage loader.


The sched.js script adds persistence by creating a Scheduled Task and a Startup link, and sucesso.js is responsible for reporting the status to the C2.


Meanwhile, the install.js script performs the following tasks:


* Check for Internet connection (using google.com)
* Create %APPDATA%\\\\extensions folder
* Download password-protected archives such as python32.rar/python64.rar and unrar.exe to that extensions folder
* Write the path of the newly created extensions folder to HKEY\_CURRENT\_USER\\Software\\Python\\Config\\Path
* Performs some basic system profiling
* Execute unrar.exe command with the password specified as an argument to unpack python32.rar/python64.rar
* Connect to C2 and download 32bit and 64bit \_\_init\_\_.py scripts along with two encrypted payloads. Each payload has a pseudo-random name.


![The Chaes infection chain](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/infection.png)**The Chaes infection chain**  
*Source: Avast*
The Python loader chain unfolds in memory and involves loading multiple scripts, shellcode, and Delphi DLLs until everything is in place for executing the final payload within a Python process.


The final stage is undertaken by instructions.js, which fetches the Chrome extensions and installs them on the victim’s system. Finally, all extensions are launched with the proper arguments.


Chrome extensions
-----------------


Avast [says they have seen](https://decoded.avast.io/anhho/chasing-chaes-kill-chain/) five different malicious Chrome browser extensions installed on victim's devices, including:


* **Online** – Fingerprints the victim and writes a registry key.
* **Mtps4** – Connects to the C2 and waits for incoming PascalScripts. Also capable of capturing a screenshot and displaying it in full screen to hide malicious tasks running in the background.
* **Chrolog** – Steals passwords from Google Chrome by exfiltrating the database to the C2 through HTTP.
* **Chronodx** – A loader and JS banking trojan that runs silently in the background and waits for a Chrome launch. If the browser is opened, it will close it immediately and reopen its own instance of Chrome that makes banking info collection possible.
* **Chremows** – Targets Mercado Libre online marketplace credentials.


![Closing and relaunching Chrome](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Closing and relaunching Chrome**  
*Source: Avast*
At this time, the Chaes campaign is still ongoing, and those who have been compromised will remain at risk even if the websites are cleaned.


Avast claims that some of the compromised websites abused for dropping the payloads are very popular in Brazil, so the number of infected systems is likely large.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Chaes]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Brazil]] [[victim.continent.name=South America]]

### Autogenerated Tags:
[[Websites]] [[C2]] [[Bleeping Computer]]

