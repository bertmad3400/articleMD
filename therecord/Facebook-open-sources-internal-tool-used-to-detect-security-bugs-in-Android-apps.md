# Facebook open-sources internal tool used to detect security bugs in Android apps
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/facebook-open-sources-internal-tool-used-to-detect-security-bugs-in-android-apps/)
+ Date: September 29, 2021
+ Author: Catalin Cimpanu


## Article:
![Facebook open-sources internal tool used to detect security bugs in Android apps](https://therecord.media/wp-content/uploads/2021/09/Mariana-Trench.png)

* Facebook's new Mariana Trench security tool can find security bugs in Android and Java applications.
* Mariana Trench is currently used to find vulnerabilities in the Facebook, Instagram, and WhatsApp Android apps.
* Facebook said the tool can go through its entire Java code base (tens of millions of line of code) in roughly 45 minutes.


**Facebook has open-sourced Mariana Trench, one of its internal security tools, used by its security teams for finding and fixing bugs in Android and Java applications.**


The tool, made available on [GitHub](https://github.com/facebook/mariana-trench/) a few months back but formally released today, has been used internally at Facebook for the past months to find bugs in the Facebook, Instagram, and WhatsApp Android applications.


Under the hood, Facebook said the tool works by analyzing [Dalvik bytecode](https://source.android.com/devices/tech/dalvik/dalvik-bytecode), the format in which Android apps are packaged for distribution.


The benefit of being able to work with Dalvik bytecode is that Mariana Trench (MT) can scan apps with or without direct access to their source code.


Mariana Trench is also the third static code analyzer that Facebook has released so far. Previous releases include:


* [Zoncolan](https://engineering.fb.com/2019/08/15/security/zoncolan/) (August 2019) – a tool for analyzing web apps written in the Hack programming language (used internally at Facebook to find bugs in the Facebook web apps)
* [Pysa](https://engineering.fb.com/2020/08/07/security/pysa/) (August 2020) – a tool for analyzing Python code (used internally to find bugs on the Instagram platform)


Mariana Trench works on the same design as the first two—by looking for “sources” (where data enters a codebase) and “sinks” (where data ends up).


All three tools track how data moves across a codebase to find dangerous “sinks,” such as functions that can execute code and retrieve or interact with sensitive user data.


Once a dangerous sink is found, the tool notifies developers, who can then take action to address reported issues and prevent a tiny code update in a giant codebase from accidentally opening a vulnerability in another part of the code.


### Mariana Trench was built for speed


While there are plenty of static code analyzers built for Java code and Android apps, some of which have been around for decades, Facebook said MT’s main advantage is its speed, with the tool needing around 45 minutes to go through the entire Facebook code base, estimated in the realm of tens of millions of lines of code.


The social network said that tools like Zoncolan, Pysa, and Mariana Trench are essential to its security teams, which are relying more and more on automated bug detection systems.


“In the first half of 2021, over 50 percent of the security vulnerabilities we found across our family of apps were detected using automated tools,” Facebook said today.


More details and the tool’s documentation are available on the [Mariana Trench official website](https://mariana-tren.ch/).





#### Tags:
[[Facebook]] [[Android]] [[apps]] [[applications.]] [[code.]] [[The Record]]
