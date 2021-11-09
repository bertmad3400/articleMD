# Rust-proofing the internet with ISRG's Prossimo
### There are efforts afoot to rewrite many fundamental internet programs in Rust to make them safer to use.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/rust-proofing-the-internet-with-isrg-prossimo/)
+ Date: November 9, 2021
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

You know the non-profit [Internet Security Research Group (ISRG)](https://www.abetterinternet.org/) for its [Let's Encrypt](https://letsencrypt.org/) certificate authority, the most popular way of securing websites with TLS certificates. The group wants to do more. Its newest project, [Prossimo](https://www.memorysafety.org/about/), seeks to make many basic internet programs and protocols memory-safe by rewriting them in [Rust](https://www.rust-lang.org/).


Rust, like some other memory-safe programming languages such as Go and Java, prevents programmers from introducing some kinds of memory bugs. All too often memory safety bugs go hand-in-hand with security issues. Unfortunately, much of the internet's fundamental software is written in C, which is anything but memory safe. 

Of course, you can write memory-safe programs in C or C++, but it's difficult. Conversely, you can create memory bugs in Rust if you try hard enough, but generally speaking Rust and Go are much safer than C and C++.

**Also:** [**The most popular programming languages and where to learn them**](https://www.zdnet.com/article/best-programming-language/)

There are many kinds of memory safety bugs. One common type is [out-of-bounds reads and writes](https://cwe.mitre.org/data/definitions/787.html). In these, if you wrote code to track a to-do list with 10 items in C without memory protection measures, users could try to read and write for an 11th item. Instead of an error message, you'd read or write to memory that belonged to another program. In a memory-safe language, you'd get a compile error or crash at run time. A crash is bad news too, but it's better than giving a hacker a free pass into some other's program memory. 

Using that same example, what happens if you delete the to-do list and then ask for the list's first item? A badly written program in a non-memory-safe language will try to fetch from the old memory location in what's called a [use-after-free](https://cwe.mitre.org/data/definitions/416.html) error. This trick is used all the time to steal data and wreak havoc on a poorly secured program. Again, with Rust or Go, you must go far out of way to introduce such a blunder. 

As ISRG's executive director, Josh Aas, explained in a speech at the [Linux Foundation Membership Summit](https://events.linuxfoundation.org/lf-member-summit/): 


> We've only started talking about security seriously recently. The problem is mainly C and C++ code. That's where these vulnerabilities are coming from. New memory safety vulnerabilities come up in widely used software every day. I think it's fair to say that this is out of control. 90% of vulnerabilities in Android; 70% from Microsoft and 80% of zero-day vulnerabilities come from old language memory-based. There are real costs to this stuff every day people get hurt.
> 
> 






Why are they doing this now? Because, Aas explained, "We didn't have great system languages to replace C. Now, we have that option."

So it is that under the Prossimo umbrella, ISRG is sponsoring developers to create memory-safe versions of internet programs. So far this includes a memory-safe TLS library, [Hyper](https://github.com/hyperium/hyper), and module, [mod\_tls](https://github.com/abetterinternet/mod_tls), for the [Apache webserver](https://httpd.apache.org/); a memory-safe [curl](https://curl.se/) data transfer utility; and memory-safe [Rustls](https://www.memorysafety.org/initiative/rustls/), a safer [OpenSSL](https://www.openssl.org/) alternative.

Next up, Prossimo wants to give [Network Time Protocol (NTP)](http://www.ntp.org/) the memory-safe treatment. For now, though, this [NTP project lacks funding](https://www.memorysafety.org/initiative/ntp/). 

Of course, replacing critical C-based programs throughout the internet is a gigantic and complex task. But it's a job that must be done as we grow ever more dependent on the internet for our personal lives, business work, and indeed the entire global economy. 

**Related Stories:**

* [Linus Torvalds on where Rust will fit into Linux](https://www.zdnet.com/article/linus-torvalds-on-where-rust-will-fit-into-linux/)
* [Google backs effort to bring Rust to the Linux kernel](https://www.zdnet.com/article/google-backs-effort-to-bring-rust-to-the-linux-kernel/)
* [Programming languages: The new version of Rust arrives with this long-awaited feature](https://www.zdnet.com/article/programming-languages-the-new-version-of-rust-arrives-with-this-long-awaited-feature/)





#### Tags:
[[memory-safe]] [[ZDNet]]
