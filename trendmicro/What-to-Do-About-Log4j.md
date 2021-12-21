# What to Do About Log4j
### Learn more about some tactical measures people are already taking, and some strategic guidance for what to do after the immediate crisis abates.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/21/l/log4j.html
+ Date: 2021-12-21
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/what-to-do-about-log4j/log4j-rnp.jpg)





What to Do About Log4j 


Log4j poses some deep challenges to IT. In this article I’ll discuss some tactical measures people are already taking now and over the next week or two, and some strategic guidance for what to do after the immediate crisis abates.


The Problem


Log4j is a very useful tool incorporated in much Java code. There are so many places in code where a programmer wants to take some data and put it into a log, or some other kind of repository, for later action. Log4j does this – it takes a string and copies it from one place (the userid field in a login screen, for instance) and puts it somewhere else (the input area for an authentication process, for instance). Log4j does much more than a simple CTL-C/CTL-V though. Log4j also examines the string and interprets it.


Interpretation is generally risky, because unless the program sanitizes the code, things can go quite wrong. As the brilliant XKCD comic “Exploits of a Mom” points out:






![Exploits of a Mom](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/what-to-do-about-log4j/xkcd-comic.png)
Source: https://xkcd.com/327/ 





Log4j does not sanitize inputs.


Tactical Measures


The first challenge is to find out where your code and applications might have the vulnerability. There are tools to scan for the presence of the string ”log4j” including Snyk and others. These will find any places in your source code libraries that have calls to the code. The next step is to verify whether that source code was ever actually deployed into your production environment. Sometimes developers use logging during code development to take a snapshot of the variables and key points, just to make sure that the program is behaving appropriately. When it’s time to deploy that code, the snapshots are disabled – they never run in the real world.


If you have deployed code into production using Log4j, you should consider one of the following actions:


1. Rebuild the package using the most current version of Log4j, which at this moment is 2.17.xx. But please check the Apache Foundation for the most current fix level.
2. Disable the application, or the server or virtual machine running it, until you can remediate the build.
3. Install an IPS rule that will block inputs with the “log4j” string – but note that bad actors are developing ways to obscure that string, such as encoding it in base64 so it passes a text scan, etc.
4. Disable logging until you can remediate the code. This may mean commenting out the Log4j reference, which may cause the application to lose some functionality – such as you may no longer be able to process messages from one user to another. Incidentally, this was where the defect was first reported: players In Minecraft discovered that if they put commands to Log4j in the message box, they weren’t sent but actually executed.


Other tools can test and application’s input fields to check if the application behaves properly. These tools do this by providing a safe, harmless string that will cause the bug to reveal itself – without causing any damage. The test may put a string into an input field that should be rejected as invalid if things are properly locked down, but may display the message “Hello, world” if the bug is present.


Once you identify applications in production with the vulnerability, the choices are like those for an application deployed with vulnerable source code: shut it off, put an IPS rule in place to block (most) attacks, stop logging, or shut down the server running it. 


Strategic Guidance


A colleague asked me if logging was a bad idea. I assured them that no, logging was good, and in fact a crucial element of many applications. Applications process userids, passwords, messages, and log entries by using log4j (in Java) or something like it (in other programming environments). The trick is to determine what kinds of messages you want to process, and whether you want the logging tool to perform any interpretation of the message. The problem becomes complex when you realize that your software doesn’t run in a vacuum, but in a context provided by lots of other software from many other sources. One proposal is to build a Software Bill of Materials (SBOM) listing all the components used to construct the application, like the ingredients listed on a can of food. We use the ingredients list to guide us away from allergens and help us maintain a healthy diet. An SBOM will help us diagnose tainted software beyond whatever we might learn from today’s Software Asset Management Database. Admittedly, many organizations do not have a comprehensive SAMDB today. Fixing that should become a greater priority considering the current problems.


Next Steps


By providing the ingredients for the canned software (COTS) we use, along with the knowledge we can get from a good software bill of materials, diagnosing and fixing future incidents like log4j will become much less traumatic and much more efficient.


For security teams working around the clock in response to the log4j vulnerability, check out our [free assessment tool](/en_us/apache-log4j-vulnerability.html).  




What do you think? Follow me on Twitter to continue the conversation: [@WilliamMalikTM.](https://www.twitter.com/@WilliamMalikTM)








## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[Log4j]] [[Trend Micro]]
#### urls
https://xkcd.com/327/

