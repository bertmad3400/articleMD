# Hackers are disguising their malicious JavaScript code with a hard-to-beat trick
### Akamai might have found a better way to detect malicious obfuscated JavaScript code.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/hackers-are-disguising-their-malicious-javascript-code-with-hard-to-beat-trick/)
+ Date: October 20, 2021
+ Author: Liam Tung


## Article:
Unknown

Over 25% of malicious JavaScript code is obfuscated by so-called 'packers', a software packaging method that has given attackers a way of evading signature-based detection, according to security and content delivery network provider Akamai. 

Packers work by compressing or encrypting code to make that code unreadable and non-debuggable — resulting in 'obfuscated' code that is difficult for antivirus to detect. 


JavaScript packers aren't a new threat. As Secureworks noted as far back as 2008, JavaScript packers became a popular alternative to JavaScript libraries because they were good at reducing the number of bytes downloaded on each page in order to support richer web applications of the time. 

**SEE:**[**This new ransomware encrypts your data and makes some nasty threats, too**](https://www.zdnet.com/article/this-new-ransomware-encrypts-your-data-and-makes-some-nasty-threats-too/)

"Computer hackers have taken advantage of the acceptance of these packers as suboptimal network optimization tactics and are using them as a way to evade and bypass security controls on the gateway and at the host," [SecureWorks noted then](https://www.secureworks.com/research/thepacker). 

Akamai notes that some of the world's most popular websites contain obfuscated JavaScript for business reasons. 

The company highlights that packers are still a large scale problem, aiding the spread of phishing pages, malware droppers and scams like [the Magecart attacks on online payment systems](https://www.zdnet.com/article/visas-plan-against-magecart-attacks-devalue-and-disrupt/). At [the SecTor 2021 conference in November](https://sector.ca/in-person/) researchers will present a new "technique that profiles the unique functionality of packers to detect JavaScript prior to it being obfuscated, regardless of the original code."






Instead of a signature or hash, the JavaScript code is detected by the techniques the packer introduces, according to Akamai. 

To show how it's profiling packers, Akamai looked at four pieces of JavaScript code from four unrelated malicious files. Two of the snippets were for phishing, one was a malware dropper, and the fourth a Magecart scammer. 

**SEE:** [**This is how Formula 1 teams fight off cyberattacks**](https://www.zdnet.com/article/this-is-how-formula-1-teams-fight-off-cyberattacks/)

"These four examples are the output of the same unique packer functionality being used to obfuscate any given JavaScript code," Akamai explains. 

"By profiling packers and their functionality, we evaluated 30,000 benign and malicious JavaScript files and were able to see that at least 25% of the malicious files used one of five profiled packer functionalities."

The research also found that 0.5% of benign files from the top 20,000 top-ranked websites on Alexa.com used packer obfuscation techniques. Akamai argues then that obfuscation isn't a strong enough signal for malicious code and suggests detection will require machine learning to differentiate between malicious and benign obfuscated JavaScript code. 





#### Tags:
[[JavaScript]] [[ZDNet]]
