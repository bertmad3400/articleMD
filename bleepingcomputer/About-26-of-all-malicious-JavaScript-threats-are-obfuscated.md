# About 26% of all malicious JavaScript threats are obfuscated
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/about-26-percent-of-all-malicious-javascript-threats-are-obfuscated/)
+ Date: October 19, 2021
+ Author: Bill Toulas


## Article:
![javascript](https://www.bleepstatic.com/content/hl-images/2021/09/20/java.jpg?rand=1843796080)


A research that analyzed over 10,000 samples of diverse malicious software written in JavaScript concluded that roughly 26% of it is obfuscated to evade detection and analysis.


Obfuscation is when easy-to-understand source code is converted into a hard to understand and confusing code that still operates as intended.


Threat actors commonly use obfuscation to make it harder to analyze malicious scripts and to bypass security software.


Obfuscation can be achieved through various means like the injection of unused code into a script, the splitting and concatenating of the code (breaking it into unconnected chunks), or the use of hexadecimal patterns and tricky overlaps with function and variable naming.


Obfuscation on the rise
-----------------------


Akamai researchers have analyzed 10,000 JavaScript samples including malware droppers, phishing pages, scamming tools, Magecart snippets, cryptominers, etc.


At least [26% of them use some form of obfuscation](https://www.akamai.com/blog/security/over-25-percent-of-malicious-javascript-is-being-obfuscated) to evade detection, indicating an uptick in the adoption of this basic yet effective technique.


Most of these obfuscated samples appear to have similar code because they were bundled by the same packers, so their code structure looks similar even if the function is different.



![Code structure similarities](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/samples.jpg)**Code structure similarities**  

Source: Akamai
Akamai plans to present more details about how they are focusing their detection efforts on the packing techniques instead of the file code itself in the upcoming [SecTor conference](https://sector.ca/sessions/javascript-obfuscation-its-all-about-the-packers/).


Benign sites also use it
------------------------


But not all obfuscation is malicious or tricky. As the report explains, about 0.5% of the 20,000 top-ranking websites on the web (according to Alexa), also use obfuscation techniques.


These cases can be attributed to the following:


* Websites are trying to conceal some of their client-side code functionality from competitors.
* The JavaScript snippets they’re using were obfuscated by a third-party provider.
* Sensitive information like email addresses needs to be hidden from public view.


As such, detecting malicious code based on the fact that is obfuscated isn’t enough on its own, and further correlation with malicious functionality needs to be made.


This mixing with legitimate deployment is precisely what makes the detection of risky code challenging, and the reason why obfuscation is becoming so widespread in the threat landscape.




#### Tags:
[[JavaScript]] [[Bleeping Computer]]
