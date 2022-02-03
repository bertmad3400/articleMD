# Codex Exposed Helping Hackers in Training
### How useful is the Codex code generator as a potential training tool?

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/22/a/codex-exposed-helping-hackers-in-training.html
+ Date: 2022-02-03
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-cover.png)





*In June 2020, OpenAI released version 3 of its* [*Generative Pre-trained Transformer (GPT-3)*](https://github.com/openai/gpt-3)*, a natural language transformer that took the tech world by storm with its uncanny ability to generate text seemingly written by humans. But GPT-3 was also trained on computer code, and recently OpenAI released a specialized version of its engine, named* [*Codex*](https://openai.com/blog/openai-codex/)*, tailored to help — or perhaps even replace — computer programmers.*


*In a series of blog posts, we explore different aspects of Codex and assess its capabilities with a focus on the security aspects that affect not only regular developers but also malicious users. This is the fourth and final part of the series. (Read the* [*first*](/en_us/research/22/a/codex-exposed--exploring-the-capabilities-and-risks-of-openai-s-.html)*,* [*second*](/en_us/research/22/a/codex-exposed-how-low-is-too-low-when-we-generate-code.html)*, and* [*third*](/en_us/research/22/a/codex-exposed-task-automation-and-response-consistency.html) *parts.)*


Codex’s sales pitch remains that of a coding *assistant*: a tool aimed at reducing the time and effort a programmer must put in to perform repetitive tasks, learning new skills and finding solutions to known, recurrent problems.


These capabilities will be appreciated not only by experienced programmers watching their time spent on boilerplate code get shorter, but also by newcomers, amateur programming students who are now able to take advantage of a smart assistant’s suggestions, which are drawn from the collective experience of the codebase it was trained on.


So, what possibilities does a coding assistant like Codex offer to hackers in training, or to budding malicious actors trying to learn the malicious tricks of the trade? To answer this question, we put ourselves in the shoes of a rookie hacker and tried to see how Codex could help us improve and learn new skills.


*Coding a keylogger from scratch*


As a first example, we asked Codex to write a keylogger. Initially, the system took this quite literally, as its output was code that *gets a keystroke and logs it*using Python’s logging facility. As with an infamous paper clip–shaped helper tool from a renowned office suite, this was literally correct, but not what we wanted.






![Our first attempt at writing a keylogger (Query highlighted in red)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-1.png)
Figure 1. Our first attempt at writing a keylogger (Query highlighted in red)





In our second attempt, our directive was more precise, requiring the keylogger to also dump its memory to a file. Given the more specific task, the system still failed at it, by pivoting from the concept of “keylogger” to the wider concept of “spyware” and implementing functionality typical of this kind of tool, such as grabbing screenshots.






![Trying to write a keylogger that would also dump the memory to file (Query highlighted in red)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-2a.png)




![Trying to write a keylogger that would also dump the memory to file (Query highlighted in red)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-2b.png)
Figure 2. Trying to write a keylogger that would also dump the memory to file (Query highlighted in red)




This is indeed an interesting outcome as it shows some sort of “serendipity” by finding related functionality. It also shows the didactic value of tools such as Codex for a novice hacker, who would benefit by learning this natural progression in developing more advanced features in spyware. This is currently not actionable since it is a purely random occurrence, but one can imagine this becoming more deterministic in the future, with code generators being able to suggest and implement complementing functions based on the user request, behavior, and general context.


*Generating attacks on online banking, commerce and payment platforms*


Moving on to a more advanced topic, web injects are a hacking technique widely used in financially motivated crimes. Using this technique, an attacker injects HTML or JavaScript code into a webpage before it is displayed, and is thus capable of modifying or collecting the information typed by a user before it sent to a web server. As a possible scenario for this attack: modifying some payment requests so that those requests are correctly displayed to the user, but changed to an attacker-controlled account at the time they would be sent to the merchant server. Another scenario could be stealing credit card data or authentication credentials, typed in a web form or stored on a user device, by sending them not just to the financial institution or a web portal, but also to an attacker-controlled server for collection.


With this in mind, we decided as an experiment to double-check if Codex might have any information related to several companies from the financial industry, and tried to generate a code inject using a keyword combination in the query in the form of “company name” + “web login inject”.


In the first experiment, the right domain for online banking was generated together with code related to interception of authentication cookies. Just several keywords were enough to get an initial code scaffold that could help nonmature attackers. In the second example, only the company name was changed and as a result we got more generic code, where the potential target was highlighted only in the function names while the bodies of functions were related to the task.






![Generating web injects for different banking institutions (Queries highlighted in red)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-3a.png)




![Generating web injects for different banking institutions (Queries highlighted in red)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-3b.png)
Figure 3. Generating web injects for different banking institutions (Queries highlighted in red)




A third experiment was related to another type of attack called login brute-forcing. For this, we passed to Codex the keywords “code brute force paypal”. The engine generated a function with the correct URLs for login and authenticated home, but with an outdated redirection URL. The function body matched the task we requested to automate. It included error-handling routines and implemented a dictionary-based password brute-force attack by submitting a form with user-agent, login, and password and analyzing the results of the processed form.


In a real-world scenario, extra code might be needed to rotate credentials and source IP addresses and introduce random delays to avoid detection or triggering antifraud systems/IPS rules. In other words, the generated code “as is” is a valid proof of concept, but it requires more work to be scalable and suitable for attacks in the wild. 






![Code for generated PayPal brute-forcing (Query highlighted in red)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-4.png)
Figure 4. Code for generated PayPal brute-forcing (Query highlighted in red)




*Phishing pages and malicious SEO*


A typical activity for both experienced and inexperienced malicious actors is user phishing and social engineering, so we put Codex to the test to see how well it could perform the task.


At present, Codex does not seem to be the perfect tool for generating phishing pages. Quite the contrary, in fact. When we asked it to generate a PayPal login page with the aim of having a page resembling PayPal but pointing to a server controlled by malicious actors, we got exactly the opposite: a page not resembling PayPal at all but pointing to PayPal endpoints. We consider this to be just a temporary setback, however. As with the improvements of AI models and language transformers, the day when the perfect phishing page can be generated with a single command might not be too far off.






![Trying to generate a PayPal phishing page (Query highlighted in red)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-5.png)
Figure 5. Trying to generate a PayPal phishing page (Query highlighted in red)




On the other hand, there is a sort of a malicious (or black hat) SEO activity that involves creating many webpages filled with specific keywords and garbage words or sentences that do not make any sense, and may or may not be grammatically correct (now detected by most search engines). It would not be too hard for a search engine to eradicate such pollution, because the pages may contain sentences without grammar, or sentences picked up from canned templates, and the pages usually look ugly.


However, there is where we see a potential misuse of Codex to generate tons of grammatical sentences with paid-for keywords that even read well, unless the reader knows the subject well enough to figure out any unreasonable parts. In the examples below, the screenshot on the left is a typical meaningless page for malicious SEO, while on the right is a well-composed one that can now be generated at a very low cost using Codex.






![Generated SEO page with malformed sentences (top) versus Codex-generated SEO page with proper grammar (bottom)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-6a.png)




![Generated SEO page with malformed sentences (top) versus Codex-generated SEO page with proper grammar (bottom)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-part-4/gpt-part4-6b.png)
Figure 6. Generated SEO page with malformed sentences (top) versus Codex-generated SEO page with proper grammar (bottom)




On a similar note, pages made by nonnative English-speaking malicious actors tend to suffer from spelling errors and odd grammar. In this case, Codex could come to help in generating fluent and native-sounding English text just by responding to the right prompt keywords. The result might be better than writing a phishing page in their own language and making a pass in Google Translate.


Trying to draw a general conclusion on the subject matter from our experiments, we have to say that, for malicious actors, Codex represents a double-edged sword. While experienced actors might still find some value in Codex’s coding assistant capabilities, as it stands, they certainly have better tools, handcrafted and tailored around their specific needs, to perform their daily tasks. On the other hand, for newcomers and hackers in training, Codex, while still unable to completely substitute a regular hacker in code generation, offers an interesting platform to bootstrap their activity and improve their skills.


*Overall conclusion*


OpenAI’s Codex offers a lot of usability and helps developers save time and learn programming languages. At the same time, it exposes several shady aspects and limitations of its capabilities. It is important that the general public be made aware of some of these, as they could be taken advantage of by malicious actors in multiple ways:


* Answering questions for which it is not developed, Codex could expose sensitive data present in the source code used to train it. As a result, malicious actors could use Codex to [collect sensitive data](/en_us/research/22/a/codex-exposed--exploring-the-capabilities-and-risks-of-openai-s-.html) about targets, specific to their IT infrastructures and employees. Its answers could expose connection strings, hard-coded credentials and access tokens, internal systems naming, names and structures of databases, links to assets and documents that are not indexed by search engines, and names, contacts, and roles of employees. If proper data hygiene was already a critical aspect for every company to enforce, it becomes even more critical now that AI engines could use such sensitive data into their training sets.
* While we have seen its limited capabilities to generate low-level code, Codex can help in [crawling, parsing, and processing data and code](/en_us/research/22/a/codex-exposed-how-low-is-too-low-when-we-generate-code.html). It can understand existing code and it can be used in binary parsing. It can determine which binaries — for both Linux and Windows platforms — a  particular snippet of binary code belongs to. Codex can also successfully generate code for crawling and parsing webpages. Such actions could be helpful to malicious actors with low maturity in making a step forward in their development.
* Codex’s [nondeterministic nature](/en_us/research/22/a/codex-exposed-task-automation-and-response-consistency.html), however, precludes fully automated code generation. Two equal or similar requests can lead to different implementations. Because of this, for many types of projects, malicious or not, the task of filtering and fixing the response might very well end up being more labor-intensive than, say, resorting to a more traditional solution to achieve the same end result.
* Creating keyloggers, web injects, and phishing pages, and even fixing grammar for phishing emails, as discussed in this blog post, is a niche where Codex can produce valuable results and save time for malicious actors.


Trying to draw a general conclusion on the subject from our experiments, we are inclined to say that, for malicious actors, Codex represents a double-edged sword. While experienced actors might still find some value in Codex’s coding assistant capabilities, as it stands, they certainly have better tools, handcrafted and tailored around their specific needs, to perform their daily tasks. On the other hand, for newcomers and hackers in training, Codex, while still unable to completely substitute a regular hacker in code generation, offers an interesting platform to bootstrap their activities and improve their skills.








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Phishing]] [[Paypal]] [[Keylogger]] [[Red)]] [[Seo]] [[(query]] [[Openai]] [[Trend Micro]]

