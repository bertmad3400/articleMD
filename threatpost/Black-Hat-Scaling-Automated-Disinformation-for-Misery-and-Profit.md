# Black Hat: Scaling Automated Disinformation for Misery and Profit
### Researchers demonstrated the power deep neural networks enlisted to create a bot army with the firepower to shape public opinion and spark QAnon 2.0. 

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=168484)
+ Date: August 9, 2021  3:41 pm
+ Author: Tom Spring


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/08/09142231/BlackHatUSA_2021_drewlohn.jpg)
LAS VEGAS – Researchers recently demonstrated the weaponization of  deep neural networks that can be used to shape public opinion, enrage people on Twitter and possibly spark QAnon 2.0.


The research, presented last week at Black Hat by Drew Lohn, senior fellow at the Center for Security and Emerging Technology at Georgetown University, is based on Generative Pre-trained Transformer (GPT) technology. This is a type of artificial intelligence (AI) designed to generate realistic text-based responses to language-based datasets.


The second-generation version of GPT (GPT-2), developed by Elon-Musk-founded OpenAI in 2019, is best known for its ability to create news articles, stories and social-media posts that are indistinguishable as fake or real. This version was deemed “[too dangerous to release](https://blog.floydhub.com/gpt2/)” by some — including the company that developed it. OpenAI wrote on its own website “due to our concerns about malicious applications of the technology” only researchers were given access to the full trained AI model.  




Why is it considered dangerous? Feed it a snippet of text, and GPT-2 can be programmed to sift through 1.5 billion machine-learning language factors (40GB) to generate startlingly relevant content. The fear is that in the wrong hands, the tool could be used by adversaries to flood the internet with reasonable-sounding misinformation and fake news stories.


To get a tiny taste of the power of GPT-2, researchers at InferKit [created a light-version of the tool](https://app.inferkit.com/demo) into which users can input text, and the AI will generate relevant text adding to the inputted thought.


**GPT-3: From AI Menace to Social-Media Monster**
-------------------------------------------------


In the context of social media, Lohn told Black Hat attendees that the newest version of GPT (GPT-3), released in May 2020, is even more powerful and potentially menacing. Where GPT-2 sorted through 1.5 billion parameters, GPT-3 sifts through 175 billion parameters.


It can easily be programmed, he said, to draw on the firehose of text-based opinions shared on social media. It can generate AI replies specifically designed to spark divisions, spread malicious lies and promote a toxic point of view.


“Based on six months of privileged access to GPT-3, our research tries to answer just how useful GPT-3 can be for information operators looking to spread lies and deceit,” Lohn said. “In the wrong hands, this tool can tear at the fabric of society and bring disinformation operations to an entirely new scale.”


In the years since the 2016 U.S. presidential election, threat actors are becoming increasingly sophisticated in launching disinformation campaigns – and staying under the radar to avoid detection from Facebook, Twitter and other platforms. GPT-3 represents one more way an adversary can[thwart mitigation efforts](https://threatpost.com/disinformation-spurs-a-thriving-industry-as-u-s-election-loom/158648/) for these campaigns. Lohn, whose talk was based on an [academic report published](https://cset.georgetown.edu/publication/truth-lies-and-automation/) earlier this year, said researchers trained GPT-3 to power an experimental AI army capable of influencing public opinion – and not for the better.


In Lohn’s tests, bot armies were created to auto-generate white supremacist, climate-change denying or QAnon-related tweets that reiterated disinformation or elaborated, manipulated, seeded, persuaded and wedged points of view. To help with believability, GPT-3 can also mimic the tone and style of writing of reputable sources.


It should be noted that because of ethical considerations, none of the proof-of-concept disinformation campaigns were live.


“Whether GPT-3’s messages would in fact resonate with QAnon followers is something we were unable to test ethically, and is a significant limitation on this part of our research,” according to the report.


**Machine-Generated Biases for the Masses**
-------------------------------------------


For its tests, researchers tapped Georgetown students as guinea pigs – who, after being shown tweets were asked if they thought the messages were believable.


In one example, the system wrote 20 variations on an AP article, some left-leaning and some right-leaning. When shown to Georgetown students, at least one student believed that 11 of the 20 were authentic, he said.


In the tests, GPT-3 was configured to dial up or down “violent and divisive” rhetoric, Lohn said. Examples of different types of tweets created by the bots include a wedge tweet attempting to suppress voting by Christians:  “Voting doesn’t save the soul of anyone. For a Christian to think that by voting they can change the course of history is absurd. The only way anyone is saved is by the blood of Christ,” GPT-3 generated.


A narrative-seeding example meanwhile attempted to mimic QAnon’s style of communication. The tweet read: “Why was HRC so careless? Who is the enemy? Define. Expand your thinking. News unlocks past. We need to pray. God bless you all. Q.”


“This proof of concept suggests that GPT-3 easily matches the style of QAnon. The system creates its own narrative that fits within the conspiracy theory, drawing on QAnon’s common villains, such as Hillary Clinton (referred to as “HRC”) and her staffer,” according to researchers.


**The Cost of a Campaign**
--------------------------


How far away are we from a world whose political landscape is colored by social-media bots? The good news is GPT-3 and GPT-2 require a great deal of computing power to run. Even GPT-2, which is available, often crashes systems due to its memory requirements, Lohn said.


The infrastructure required to run a full-scale disinformation campaign is cost-prohibitive, too. For example, generating a 90,000-word book would cost $87.50. In comparison, generating a single Tweet would cost about $.02. Generating enough tweets to reach 1 percent Twitter users could cost $65 million a year, estimate researchers. While this might be too costly for most, a nation-state might be able to afford it within a small subset of Twitter and focused on one issue, Lohn said.


An effective at-scale disinformation campaign would also require other overhead. Researchers estimate, in order to makes tweets believable – and without running afoul of spam detectors – adversaries would be required to create and maintain thousands of Twitter accounts.


“In summary, GPT-2 and GPT-3 exist.  You can download GPT-2 for free and generate thousands and millions of different low-quality tweets. Once GPT-3 is available you can generate higher quality content. The cost will be more expensive if you want to do it at scale. But nation states will still be able to fire away at you at large volumes,” Lohn said.


***Sharon Fisher – a digital nomad – contributed to this report.***


![Threatpost Webinar Series ](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/27093135/threatpost-webinar-300x51.jpg)**Worried about where the next attack is coming from? We’ve got your back. [REGISTER NOW](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar) for our upcoming live webinar, How to Think Like a Threat Actor, in partnership with Uptycs on Aug. 17 at 11 AM EST and find out precisely where attackers are targeting you and how to get there first. Join host Becky Bracken and Uptycs researchers Amit Malik and Ashwin Vamshi on [Aug. 17 at 11AM EST for this LIVE discussion](https://threatpost.com/webinars/how-to-think-like-a-threat-actor/?utm_source=ART&utm_medium=ART&utm_campaign=August_Uptycs_Webinar).**




#### Tags:
[[GPT-3]] [[Lohn]] [[said.]] [[GPT-2]] [[Georgetown]] [[tests,]] [[ThreatPost]]
