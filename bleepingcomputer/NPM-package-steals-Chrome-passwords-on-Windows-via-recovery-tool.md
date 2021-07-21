# NPM package steals Chrome passwords on Windows via recovery tool
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/npm-package-steals-chrome-passwords-on-windows-via-recovery-tool/)
+ Date: July 21, 2021
+ Author: Ax Sharma


## Article:
![npm](https://www.bleepstatic.com/content/hl-images/2017/08/04/npm.png)


New npm malware has been caught stealing credentials from the Google Chrome web browser by using legitimate password recovery tools on Windows systems.


Additionally, this malware listens for incoming connections from the attacker's C2 server and provides advanced capabilities, such as screen and camera access, directory listing, file lookup, file upload, and shell command execution.


As seen by BleepingComputer, the identified packages have been sitting on the npm registry since 2018 and scored over 2,000 total downloads at the time of writing.


Uses ChromePass utility to 'recover' Chrome passwords
-----------------------------------------------------


Today, researchers at ReversingLabs have disclosed their findings on two malicious npm packages that secretly steal passwords from your Chrome web browser.


These packages are called:


* **nodejs\_net\_server** - over 1,300 total downloads
* **temptesttempfile** - over 800 total downloads


These packages were discovered by ReversingLabs' Titanium Platform static analysis engine that employed [machine learning](https://blog.reversinglabs.com/blog/introducing-explainable-machine-learning) algorithms.


But, the primary focus of the report is on *nodejs\_net\_server* which contains the core malware functionality.


The malware targets Windows machines to steal user credentials and also sets up a persistent remote backdoor for the attacker to conduct surveillance activities.


To facilitate its credential-stealing activities, the malware—specifically "nodejs\_net\_server," uses the legitimate [ChromePass](https://www.nirsoft.net/utils/chromepass.html) freeware utility for Windows.


ChromePass is a password recovery tool for Windows systems aimed at extracting passwords from the user's Chrome web browser:



![ChromePass utility](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/reversinglabs-npm-malware/chromepass.gif)**ChromePass password recovery utility**(NirSoft)
This utility is packed inside the npm package with cryptic or misleading names, such as *a.exe.*


Regardless, such ChromePass executables have previously been flagged by VirusTotal as [malicious](https://www.virustotal.com/gui/file/0291e6c35ad5ed041579b75496fa212f04eb1c9d73f639349ddaa01e5da10906/detection).


The "nodejs\_net\_server" has had 12 versions published to date, with the latest one 1.1.2 measuring about 40 MB in size uncompressed.


In later versions, though, the malware is seen launching *TeamViewer.exe*to avoid raising red flags.


Abuses npm configuration options to gain persistence
----------------------------------------------------


Most malicious npm packages caught thus far rely on [typosquatting](https://www.bleepingcomputer.com/news/security/malicious-npm-project-steals-discord-accounts-browser-info/) or [dependency confusion](https://www.bleepingcomputer.com/news/security/researcher-hacks-over-35-tech-firms-in-novel-supply-chain-attack/) to infect developers.


But, that's not the case with these packages, and it isn't yet known how these packages managed to get so many downloads.



![npm nodejs_net_server](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/reversinglabs-npm-malware/npm-package-page(1).jpeg)**nodejs\_net\_server download page on the npm registry** (BleepingComputer)
"We haven't found any obvious typosquatting target by analyzing the package name."


"It is unclear to us how the author intended to trick users into installing the package. We can however see download activity on the package statistics page."


"We have contacted NPM to take the package down. We are still waiting on their security team to respond," ReversingLabs' chief software architect and co-founder, Tomislav Pericin told BleepingComputer in an email interview.


Interestingly, as soon as the package is installed by the developer, it attempts to gain persistence on the Windows machine by abusing the well-known npm configuration option, "[bin](https://docs.npmjs.com/cli/v7/configuring-npm/package-json#bin)".


The "bin" option in the package's manifest file, package.json, is aimed at hijacking the popular "jstest" package, should it be pre-installed on a developer's machine.


"[jstest](https://www.npmjs.com/package/jstest)" is a cross-platform JavaScript testing framework downloaded over 36,000 times to date—meaning, high chances a NodeJS developer would have it.



![package.json for nodejs_net_server](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**package.json for nodejs\_net\_server**(BleepingComputer)
But, having "jstest" pre-installed is by no means a prerequisite for the malicious package to run. Its presence merely helps the malware achieve persistence on the infected machines:


"JSTest doesn't need to be installed for this attack to work. Package installation hijacks the command 'jstest' if it was already assigned."


"Running that command would ensure that malware gets persistence and that it executes the backdoor functionality," Pericin further told BleepingComputer.


The "jstest" file loaded by the malware attempts to overwrite the contents of the existing "jstest" [symlink](https://en.wikipedia.org/wiki/Symbolic_link), and further adds another JS file ("test.js") as a Windows service which would now run persistently.



![malware attempts to gain persistence using jstest](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Malware attempts to achieve persistence by adding the lib/test.js script as a Windows service**(BleepingComputer)
This newly added Windows service opens up port 7353 that the attacker to connect to and perform various surveillance activities, including:


* reverse host and port configuration
* directory content listing
* file upload and search
* shell command execution
* screen and camera access and recording via the bundled *ffmpeg* executable
* password-stealing from Chrome browser using the bundled ChromePass recovery utility



![Windows service script](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Malware opens up a socket connection on port 7353**(BleepingComputer)
As for *temptesttempfile,* the package is minimal with just two files, and only implements the remote shell functionality of *nodejs\_net\_server*, making it seem like a test package as the name suggests.


Oops! Malware author exposes their own passwords
------------------------------------------------


In an unexpected twist, some versions of *nodejs\_net\_server* contain text files with usernames and plaintext passwords of the malware author, extracted from Chrome.


ReversingLabs suspects this to be an accident on the author's part:


"Fun fact related to versions that contain the password recovery tool is that the package author accidentally published their own, stored login credentials."


"It appears that the published versions 1.1.1 and 1.1.2 from the NPM repository include the results of testing the *ChromePass* tool on the author's personal computer."


"These login credentials were stored in the 'a.txt' file located in the same folder as the password recovery tool named 'a.exe,'" said ReversingLabs reverse engineer Karlo Zanki in a [blog post](https://blog.secure.software/groundhog-day-npm-package-caught-stealing-browser-passwords).


Zanki's observation was also confirmed by BleepingComputer when we noticed two files, *a.txt*, and *b.txt* with plaintext credentials, sittingin the aforementioned versions of "nodejs\_net\_server."



![passwords included in malware](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**NPM malware includes list of passwords believed to be the malware author's**(BleepingComputer)
Over the last few months, attacks on open source ecosystems including, [npm](https://www.bleepingcomputer.com/news/security/new-linux-macos-malware-hidden-in-fake-browserify-npm-package/), [PyPI](https://www.bleepingcomputer.com/news/security/malicious-pypi-packages-hijack-dev-devices-to-mine-cryptocurrency/) and [RubyGems](https://www.bleepingcomputer.com/news/security/malicious-rubygems-packages-used-in-cryptocurrency-supply-chain-attack/) have grown steadily.


With recent reports of ongoing [dependency hijacking](https://blog.sonatype.com/pypi-and-npm-flooded-with-over-5000-dependency-confusion-copycats) attacks flooding open source repos, the problem isn't going away anytime soon.


ReversingLabs believes, understanding what's inside your software, or having a Software Bill of Materials (SBOM) is a critical step in defending against these supply chain attacks.


"Package repositories offer conveniences for rapid application development, but also come with risks."


"Understanding the package dependency tree, or software bill of materials, has become a critical part of defense against software supply chain attacks."


"Every component should be looked with scrutiny before installation, or there's a chance malicious code can slip by unnoticed."


"We are yet to see a malicious repository package embed itself in the final release image, but that seems like it's only a matter of time with the current state of things," concluded Pericin in his interview with BleepingComputer.




#### Tags:
[[malware]] [[BleepingComputer]] [[npm]] [[nodejs_net_server]] [[Windows]] [[ChromePass]] [[ReversingLabs]] [[jstest]] [[1]] [[NPM]] [[Bleeping Computer]]
