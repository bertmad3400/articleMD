# State-backed hackers increasingly use RTF injection for phishing
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/state-backed-hackers-increasingly-use-rtf-injection-for-phishing/)
+ Date: December 1, 2021
+ Author: Bill Toulas


## Article:
![Phishing](https://www.bleepstatic.com/content/hl-images/2021/04/16/malware-phishing-header.jpg)


Three APT hacking groups from India, Russia, and China, were observed using a novel RTF (rich text format) template injection technique in their recent phishing campaigns.


This technique is a simple yet effective method to retrieve malicious content from a remote URL, and threat analysts expect it to reach a wider audience of threat actors soon.


Researchers at Proofpoint spotted the first cases of weaponized RTF template injection in March 2021, and since then, actors have been steadily optimizing the technique.


A simple method to fetch payloads
---------------------------------


Rich Text Format (RTF) files are a document format created by Microsoft that can be opened using Microsoft Word, WordPad, and other applications found on almost all operating systems.


When creating RTF files, you can include an RTF Template that specifies how the text in the document should be formatted. These templates are local files imported into an RTF viewer before displaying the contents of the file to format it correctly.


While RTF Templates are meant to be hosted locally, threat actors are now abusing this legitimate functionality to retrieve a URL resource instead of a local file resource.


This substitution allows threat actors to load malicious payloads into an application like Microsoft Word or [perform NTLM authentication against a remote URL](https://www.bleepingcomputer.com/news/security/understanding-the-windows-credential-leak-flaw-and-how-to-prevent-it/) to steal Windows credentials. Furthermore, as these files are transferred as RTF Templates, they are more apt to bypass the detection phishing lures as they are not initially present in the RTF files.


Creating remote RTF Templates is very simple as all a threat actor has to do is add the `{\*\template URL}` command into an RTF file using a hex editor, as shown below.



![A URL-hiding example created by Proofpoint's researchers](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/hex_hiding_url.jpg)**A URL-hiding example created by Proofpoint's researchers**  
*Source: Proofpoint*
The method is also viable on doc.rtf files opened in Microsoft Word, forcing the app to retrieve the resource from the specified URL before serving the content to the victim, as shown below.



![Microsoft Word retrieving the external resource](https://www.bleepstatic.com/images/news/u/1220909/Phishing/word_retrieving.jpg)**Microsoft Word retrieving the external resource**  
*Source: Proofpoint*
Cases of abuse in the wild
--------------------------


Proofpoint has observed this payload retrieval method on phishing campaigns by the pro-Indian hacking group DoNot Team, the Russia-linked Gamaredon hacking group, and the TA423 threat actors.


A timeline of the observed activities is shown below.



![Timeline of activities relevant to RTF template injection](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Timeline of activities relevant to RTF template injection**  
*Source: Proofpoint*
RTF files can parse 16-bit Unicode characters, so threat actors have been using Unicode instead of plaintext strings for the injected URL resource to evade detection.



![Using Unicode to hide the URL resource](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)Using Unicode to hide the URL resource  

Source: Proofpoint
However, in some samples retrieved by the DoNot Team campaigns, Proofpoint noticed a failure to pass Microsoft Word's checks, resulting in an error message about the remote source being invalid.


Since these errors are generated before the decoy content is served to the target, the chances of success for DoNot's phishing attempts drop significantly.


TA423, on the other hand, didn't obfuscate the injected URLs, exchanging higher risk for detection and analysis for error-free loading on Microsoft Word.



![TA423 lure using RTF Template injection](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**TA423 lure using RTF Template injection**  
*Source: Proofpoint*
Finally, in the case of Gamaredon, the researchers sampled RTF documents that impersonated Ukrainian government organizations to deliver an MP3 file as a remote resource.



![MP3 file fetched as an external resource](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**MP3 file fetched as an external resource**  
*Source: Proofpoint*
As RTF Template injections are easily accomplished using a hex editing tool and are not as heavily detected by antivirus scanners, they stand to become more widely used by threat actors.


"The viability of XML Office based remote template documents has proven that this type of delivery mechanism is a durable and effective method when paired with phishing as an initial delivery vector," explained Proofpoint in their report.


"While this method currently is used by a limited number of APT actors with a range of sophistication, the technique's effectiveness combined with its ease of use is likely to drive its adoption further across the threat landscape."


Furthermore, as the malicious content is retrieved from a remote URL, it allows the threat actors to dynamically modify their campaigns in real-time to use new payloads or different malicious behaviors.


To defend against this threat, you should avoid downloading and opening RTF files arriving via unsolicited emails, scan them with an AV scanner, and keep your Microsoft Office up to date by applying the latest available security updates.


Proofpoint also shared YARA signatures that admins can use to detect RTF files modified to include remote RTF Templates.




#### Tags:
[[RTF]] [[Proofpoint]] [[Microsoft]] [[phishing]] [[URL]] [[below.]] [[DoNot]] [[Unicode]] [[Bleeping Computer]]
