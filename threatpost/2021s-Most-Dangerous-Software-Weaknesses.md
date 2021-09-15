# 2021’s Most Dangerous Software Weaknesses
### Saryu Nayyar, CEO at Gurucul, peeks into Mitre’s list of dangerous software bug types, highlighting that the oldies are still the goodies for attackers.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169458)
+ Date: September 14, 2021  4:05 pm
+ Author: Saryu Nayyar


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2019/09/03102603/Software-Patch.jpg)
Mitre Corp. recently updated its [list of the top 25 most dangerous software bugs](https://cwe.mitre.org/top25/archive/2021/2021_cwe_top25.html), and it’s little surprise that a number of them have been on that list for years. The Common Weakness Enumeration (CWE) list represents vulnerabilities that have been widely known for years, yet are still being coded into software and being bypassed by testing. Both developers and testers presumably know better by now, but still keep making the same mistakes in building applications.


We’ll review the vulnerabilities that seem to consistently make the top 25 list over the years. But first, how do these mistakes come about? There are a variety of reasons.


In many cases, developers simply don’t have security at the tops of their minds as they are coding the application. Their primary goal is to get the business logic right.


In cases where a particular algorithm doesn’t seem to be working right, developers have been known to turn off security restrictions until it behaved as expected. Developers lose face when their application has a logic bug, but not when there is a potential security vulnerability, because these are largely hidden until they are exploited.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


Testers have a more direct responsibility for ensuring applications are secure, but usually have limited tools and expertise for doing so. They are almost always testing code in isolation, often with no database, APIs or network. Without a way to look into memory, or create illegal commands, and interpret the results in terms of an attack, they are limited in their ability to identify security vulnerabilities.


There is also still the overriding perception within technical groups that security is the responsibility of the IT production group, not necessarily of the developers. After all, IT has significant tooling to define and manage an application and network perimeter, such as firewalls and anti-malware, that is designed to protect the entire infrastructure. The focus on security in production often means that there is less of a focus in development and test.


It’s all part of a culture where security vulnerabilities are largely hidden from view because they typically don’t affect the function of the application, until an attack succeeds and systems or data are lost.  While it would be most effective to focus attention on security during the entire application lifecycle, it is still critical to be vigilant in production.


Common Vulnerabilities Are Still On the List
--------------------------------------------


What follows have been common security holes for decades, and it looks like they are not leaving the Mitre list anytime soon.  They allow old but reliable attacks for a broad range of attackers worldwide, who frequently succeed in breaking into systems and organizations using them.


Manipulating memory remains one of the most popular ways of attacking a system. If an attacker is in possession of a specific memory address within an executable application, he can use it to enter values or commands that exceed the size of that memory space. Once outside of the memory space, attackers can insert executable software, making it possible to take over a computer or raise permission levels.


There are many ways of taking advantage of buffer and memory overruns for attacks. If developers haven’t limited variable lengths, an overrun can allow an attacker to write malicious code directly into application memory. At the very least, it’s possible to use this technique to interfere with application execution, causing it to crash or return incorrect results.


Attackers can use web features in order to plant malicious scripts. In this case, attackers can upload scripts into unprotected client-side web pages, to be executed when others open that page. Protecting against this involves prohibiting web applications from downloading files, and many developers neglect to add this restriction.


Many development teams continue to let attackers download scripts onto third-party web sites, and testers have a difficult time identifying this type of attack, because it’s not clear where the malicious scripts are coming from. The result is that those users innocently visiting those web pages may inadvertently and unknowingly download malware onto their systems.


Many developers focus on making sure an application returns the desired result above all else. In some applications, one common way of doing this is to give all user queries administrative access to the database. While that often works, it has consequences.


First, it opens up database administrative access to any application user. That means anyone who uses the application can use SQL commands to modify the database. Using SQL escape characters, attackers can enter SQL commands into the web interface and have them executed by the database.


Second, it keeps the database connection open for all. It’s never logged out after each individual use. That means that you don’t have to be an authorized user to find an open database. That makes the integrity of your data questionable on an ongoing basis.


This is another memory manipulation trick. When an application needs memory for a variable, it either programmatically allocates that memory, or the underlying platform (JVM or .NET Runtime). When the application is done with that memory, either it or the platform returns it to the free memory list.


If an attacker has managed to get the memory address, he can gain access to the free memory list, and insert malicious software into free memory. The next time that memory is allocated, it is allocated with a payload that can cause harm. Further, the memory isn’t wiped clean when it is returned to the free memory list, enabling attackers to read the contents of that memory.


There are some commercial debuggers that are able to look into a running process and let programmers or attackers obtain information using memory locations. While these types of debuggers are needed, any tool that lets attackers look into specific memory addresses to determine their contents has the potential to be used as a hacking tool.


Other Cyberattacks Fill the Plate
---------------------------------


The Mitre list contains other common attacks, including missing or improper authentication, incorrect permissions and unprotected credentials.


However, the most popular attacks still remain those that have been around almost since the dawn of the public internet. Until dev and test teams are able to internalize some of the most significant vulnerabilities over the last two decades and develop strategies to reliably counter them, count on both firewalls and security analytics approaches to be the most effective approach to protecting against software vulnerabilities.


***Saryu Nayyar is CEO at Gurucul.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[database.]] [[it’s]] [[don’t]] [[memory,]] [[memory.]] [[SQL]] [[ThreatPost]]
