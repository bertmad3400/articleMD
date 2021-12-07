# Rust takes a major step forward as Linux's second official language | ZDNet
### Linux is getting more Rust in it by the day.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/rust-takes-a-major-step-forward-as-linuxs-second-official-language/
+ Date: 2021-12-07 16:29:46
+ Author: Steven J. Vaughan-Nichols


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/b4d0dbc2f65bf5f8ac6eb365774427876a8e0be6/2021/07/15/8d7d0acf-85fa-4fc4-8e79-445c5eceede4/rust-programming-language-a-long-road-ahead-for-the-linux-kernal.jpg?width=770&height=578&fit=crop&auto=webp)

It wasn't that long ago that the very idea that another language besides C would be used in the Linux kernel would have been laughed at. Things have changed. Today, not only is [Rust](https://www.rust-lang.org/), the high-level system language moving closer to Linux, it's closer than ever with the [next "patch series to add support for Rust as a second language to the Linux kernel."](https://lkml.org/lkml/2021/12/6/461)


The biggest change in these new packages is that the Rust code proposed for the kernel now relies on the stable Rust compiler rather than the beta compilers. Going forward, Rust on Linux will be migrating every time a new stable Rust compiler is released. Currently, it's using [Rust 1.57.0](https://blog.rust-lang.org/2021/12/02/Rust-1.57.0.html).

By doing this, as Linux kernel and lead Rust on Linux, developer Miguel Ojeda, put it, "By upgrading the compiler, we have been able to take off the list a few unstable features we were using." This, in turn, means Rust on Linux will be more stable. 

Looking ahead, Ojeda wrote, "We will keep upgrading until we do not rely on any unstable features; at which point we may want to start declaring a minimum Rust version is supported like it is done, e.g. GCC and Clang.

Senior Linux kernel developer Greg Kroah-Hartman had told me he believes "[drivers are probably the first place for" Rust to appear in Linux](https://www.theregister.com/2021/11/10/where_rust_fits_into_linux/) since "they are the 'end leaves' of the tree of dependencies in the kernel source. They depend on core kernel functionality, but nothing depends on them."

This has been coming for several years now. At the virtual [2020 Linux Plumbers Conference,](https://www.linuxplumbersconf.org/blog/2020/) where the top Linux kernel developers hash out Linux's future, the idea of introducing [Rust as the kernel's second language](https://linuxplumbersconf.org/event/7/contributions/804/attachments/641/1168/barriers-to-in-tree-rust.pdf) was introduced.

While Linus Torvalds is sure, Linux won't end up being written in Rust. But then, that's not the goal. No one's going to rewrite the kernel's 25 million lines of C in Rust.






Led by Josh Triplett, Rust language lead, and Nick Desaulniers, a Google engineer, they proposed using the system-level Rust language inside the kernel. Why? Because it's much safer than C, especially at handling memory errors.

As Ryan Levick, a Microsoft principal cloud developer advocate, explained, "[Rust is completely memory safe](https://msrc-blog.microsoft.com/2019/07/22/why-rust-for-safe-systems-programming/)." Since roughly two-thirds of security issues can be traced back to handling memory badly, this is a major improvement. In addition, "Rust prevents those issues usually without adding any runtime overhead," Levick said.

[Torvalds sees the advantages](https://www.zdnet.com/article/linus-torvalds-looks-at-the-future-of-linux-kernel-developers-and-development/). While he's encouraging a [slow but steady approach to introducing Rust into Linux](https://lore.kernel.org/lkml/CAKwvOdmuYc8rW_H4aQG4DsJzho=F+djd68fp7mzmBp3-wY--Uw@mail.gmail.com/T/#u), he has also said that using Rust interfaces for drivers and other non-core kernel programs makes sense: "I'm convinced it's going to happen. It might not be Rust, but it is going to happen that we will have different models for writing these kinds of things, and C won't be the only one."

So, as Ojeda told *ZDNet* this summer, "[The project is not finished,](https://www.zdnet.com/article/rust-in-the-linux-kernel-why-it-matters-and-whats-happening-next/) but we are ready to get mainlined if high-level maintainers accept the current changes and prefer that we work inside the kernel. Most of the work is still ahead of us." 

Still, work well underway now. I expect to see the first Rust code in the Linux kernel sometime in 2022.



---

**Related stories:**

* [Linus Torvalds on where Rust will fit into Linux](https://www.zdnet.com/article/linus-torvalds-on-where-rust-will-fit-into-linux/).
* [Rust in the Linux kernel: Why it matters and what's happening next](https://www.zdnet.com/article/rust-in-the-linux-kernel-why-it-matters-and-whats-happening-next/).
* [Linus Torvalds: Juggling chainsaws and building Linux](https://www.zdnet.com/article/linus-torvalds-juggling-chainsaws-and-building-linux/).



---





## Tags:

#### Threatactor:
[[threatactor.name=RTM]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]] [[action.malware.name=RTM]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Linux]] [[Ojeda]] [[Torvalds]] [[ZDNet]]

