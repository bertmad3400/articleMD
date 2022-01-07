# Codex Exposed Exploring the Capabilities and Risks of OpenAIs Code Generator
### The first of a series of blog posts examines the security risks of Codex, a code generator powered by the GPT-3 engine.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/22/a/codex-exposed--exploring-the-capabilities-and-risks-of-openai-s-.html
+ Date: 2022-01-07
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-cover.png)





In June 2020, OpenAI released version 3 of its [Generative Pre-trained Transformer (GPT-3)](https://github.com/openai/gpt-3), a natural language transformer that took the tech world by storm with its uncanny ability to generate text that could fool readers into thinking it was written by humans. However, GPT-3 was also trained on computer code, and recently OpenAI released a specialized version of its engine, named [Codex](https://openai.com/blog/openai-codex/), tailored to help — or perhaps even replace — computer programmers. Being a generative language model, this new system can take a comment in natural language and “complete” it by generating a fragment of code in the programming language of the user’s choice.


It had already been known that GPT-3 could do this prior to Codex, and this had been demonstrated with different proofs of concept developed by various early adopters. These included applications capable of translating the plain English description of a webpage layout and then implementing correct HTML for the layout, chart generators that could plot a graph of a selected dataset based on a description by a user, and many other notable examples that early adopters managed to develop with very little effort.


The uncanny ability of GPT-3 to manipulate not only human vernacular but also programming jargon in its many variants comes from its unique and massive training set. GPT-3’s most powerful engine consists of a neural network using around 175 billion hyperparameters, trained using a corpus of more than 80 billion word-tokens, taken from sources that included both written human text (such as Wikipedia, public literature, and crawled websites) and code repositories.






![GPT-3’s hyperparameters versus its predecessors’ (in billions)](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-01.jpg)
Figure 1. GPT-3’s hyperparameters versus its predecessors’ (in billions) (Source: Search Engine Watch)





While GPT-3, the general-purpose language transformer that powers Codex, has recently been opened to the public, Codex itself remains a technical preview open to a limited selection of users. Codex powers the functionality of GitHub’s [Copilot](https://copilot.github.com/), a programming assistant available as a plug-in for Visual Studio Code that is able to offer AI-powered autocomplete and code translation on the fly.


Its capabilities are still rough around the edges, but they give a good idea of what the future has in store for programmers and computer scientists — and, of course, malicious users.


If such a system is bound to become a disruptive element in the daily work of computer engineers, it is natural to wonder how this could affect the activities of cybercriminals. With this in mind, we tested the extent of Codex’s capabilities, focusing on the most typical aspects of a cybercriminal: reconnaissance, social engineering, and exploitation.


In a series of blog posts, we explore how Codex’s current capabilities affect a malicious user’s everyday activities, what precautions developers and regular users can take, and how these capabilities might evolve. This is the first part of the series.


***Scavenging for sensitive data***


We know that language transformers are trained on massive corpora of text and source code taken from public repositories. We are unlikely to be the first ones to ask the question of what happens to all the information contained in the public repositories once it is sifted through the fine mesh of GPT-3’s neural network. While the first issues with Copilot’s proposing snippets of copyrighted code had already emerged, we wanted to see if sensitive information was present in GPT-3’s knowledge base and if it was possible to exfiltrate it by exploiting Codex’s code generation.


*Personal and sensitive information leaks through code*


Public repositories can be a treasure trove of sensitive data just waiting to be discovered by malicious actors. In our tests, we found that it is possible to trick Codex into exposing sensitive data being left in the repositories by having it generate code that would eventually require access to the data. 






![Exposing sensitive URLs in Codex’s generated code](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-02.png)
Figure 2. Exposing sensitive URLs in Codex’s generated code




![More code with sensitive URLs](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-03.png)
Figure 3. More code with sensitive URLs




In the examples above, we can see how, by deceitfully asking Codex to generate “code to fetch a specific dataset,” we are presented with URLs containing the information we were looking for as part of the generated code. Granted, when we checked the provided URLs, the data had been long gone, but that seemed to be more related to the data’s being outdated than to the URLs’ being fake or generated.


However, it is important to keep in mind that this issue of outdated information will likely become less of a problem in the future, as soon as language transformers such as GPT-3 are retrained more frequently to take advantage of the latest training sets available.






![Exposed sensitive information](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-04a.png)




![Exposed sensitive information](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-04b.png)




![Exposed sensitive information](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-04c.png)
Figure 4. Exposed sensitive information




URLs are not the only kind of data that could be accidentally exposed by Codex. Personal information on who worked on a certain piece of code, employer information, and even cryptocurrency wallet numbers are also up for grabs. In the example above, while looking for over-the-air firmware SIM numbers, we stumbled upon the name of a developer who, while apparently not employed anymore in the relevant project, was still active in firmware development.


In another case, after we asked Codex to implement a known vulnerability, the name of a vulnerability researcher popped up in the comments of a code snippet. We looked it up and there was indeed a researcher by that name. Even though it is public information, and one can find their GitHub repository once one knows their name, having the name remembered and exposed by GPT-3 might constitute a security risk.


*Credential stuffing*


In addition to personal information, it is also possible to lure Codex into autocompleting credentials and API entry points. In the example below, Codex gave us FedEx and DHL credentials. These credentials might have been for testing, expired, or simply random keystrokes. It is possible that the language model generated something that just “looked right.” However, hackers can be inspired with library names and parameter names to conduct further research.






![Exposed FedEx, DHL, and PayPal credentials](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-05a.png)




![Exposed FedEx, DHL, and PayPal credentials](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-05b.png)
Figure 5. Exposed FedEx, DHL, and PayPal credentials




As a side note, it is interesting to remark that Codex does not really behave like a question-answering system but rather like a very opinionated autocompletion system. This is evidenced by the fact that the completion occasionally involves the request prompt itself. In the example above, the second PayPal prompt was actually filled with information on the PayPal account by Codex itself, as it was in the example “psql” command below, where the initial request prompt was simply “psql”.






![“psql” command filled by Codex](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/gpt-3-part-1/gpt-part1-06.png)
Figure 6. “psql” command filled by Codex




***Conclusion***


The importance of proper data hygiene in code repositories, both public and private, has already been demonstrated in various researches that show the worrying amount of critical information, such as credentials and personal data, left unchecked in repositories all over the internet.


The examples we present here just go to show how this is not at all a marginal issue, but something that will become more and more critical for developers in the near future, as AI engines will scavenge for code to enrich their training corpora, without the capability of effectively filtering out sensitive data, given the ever-increasing size of their training sets.


It becomes essential for developers and DevOps engineers to implement dedicated processes to continuously check for such data and put in place proper techniques to share credentials in a secure way. These include encrypting sensitive data whenever possible and sharing decryption keys only through secure storages, and for data that cannot be stored securely, employing a periodic rotation model to make sure that, by the time it ends up in some training set for a language model, it is already outdated.








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Gpt-3]] [[Urls]] [[Paypal]] [[“psql”]] [[Trend Micro]]

