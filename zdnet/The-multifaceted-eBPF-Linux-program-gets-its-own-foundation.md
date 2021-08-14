# The multifaceted eBPF Linux program gets its own foundation
### The eBPF program started as just a network filter, but it's become Linux's swiss-army knife tool and now its future will be in the hands of the eBPF Foundation.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/the-multifaceted-ebpf-linux-program-gets-its-own-foundation/)
+ Date: August 13, 2021 -- 20:16 GMT (21:16 BST)
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

Back in 1992, the [Berkeley Packet Filter (BPF)](http://www.tcpdump.org/papers/bpf-usenix93.pdf) was introduced in Unix circles as a new, much faster network packet filter. That was nice, but far from revolutionary. Years later, in 2014, it was modified and brought into the Linux kernel as [extended BPF (eBPF)](https://prototype-kernel.readthedocs.io/en/latest/bpf/). There it would add radical new features to Linux and it's being used for numerous, useful Linux-based projects and [eBPF is moving on from Linux into Windows](https://www.zdnet.com/article/porting-linuxs-ebpf-to-windows-10-and-windows-server/) as well.  


What's so special about it? Simple, [eBPF enables you to run programs in the Linux kernel](https://www.zdnet.com/article/netflix-bpf-is-a-new-type-of-software-we-use-to-run-linux-apps-securely-in-the-kernel/) without changing the kernel source code or adding additional modules. In effect, it acts like a lightweight, sandbox virtual machine (VM) inside the Linux kernel space. There, programs that can run in eBPF run much faster, while taking advantage of kernel features unavailable to other higher-level Linux programs. 

As Thomas Graf, [Isovalent](https://isovalent.com/)'s CTO & Co-Founder and Chair of the eBPF Governing Board explained:  


> Historically, the operating system has always been an ideal place to implement observability, security, and networking functionality due to the kernel's privileged ability to oversee and control the entire system. At the same time, an operating system kernel is hard to evolve due to its central role and high requirement towards stability and security. The rate of innovation at the operating system level has thus traditionally been lower compared to functionality implemented outside of the operating system.  
> 
> EBPF fundamentally changes this formula. By allowing sandboxed programs to run within the operating system, eBPF enables developers to create eBPF programs that add capabilities to the operating system at runtime. The operating system then guarantees safety and execution efficiency as if natively compiled with the aid of a Just-In-Time (JIT) compiler and verification engine. This has led to a wave of [eBPF-based projects](https://ebpf.io/projects/) covering a wide array of use cases, including next-generation networking, observability, and security functionality.
> 
> 

This has changed the way operating systems and infrastructure services work together. It bridged the gap between kernel and user-space programs. EBPF has also enabled developers to combine and apply logic across multiple subsystems which were traditionally completely independent.

These new programs include Linux kernel debuggers, such as [bpftrace](https://github.com/iovisor/bpftrace); cloud-native security software with [Falco](https://falco.org/), and Kubernetes security applications using [Hubble](https://github.com/cilium/hubble). That's a lot of new, important programs and more are coming. So, it only made sense to form a new foundation for the project: The [Linux Foundation](https://www.linuxfoundation.org/)'s sponsored eBPF Foundation. 

You can judge how important people see it by its founding members. These include Facebook, Google, Isovalent, Microsoft, and Netflix. Why? Because it's already useful for them. For instance, Facebook is using eBPF as the primary software-defined load balancer in its data centers, and Google is using [Cilium](https://cilium.io/) to bring eBPF-based networking and security to its managed Kubernetes offerings [GKE](https://cloud.google.com/kubernetes-engine) and [Anthos](https://cloud.google.com/anthos). 

This explosion of eBPF-based projects is making it one of the most influential technologies in the infrastructure software world. So, Graf said, "the demand is high to optimize collaboration between projects and ensure that the core of eBPF is well maintained and equipped with a clear roadmap and vision for the bright future ahead of eBPF. This is where the eBPF Foundation comes in, and establishes an eBPF steering committee to take care of the technical direction and vision of eBPF. Additionally, with the port of eBPF to the Windows kernel and additional ports to other platforms on the way, the question of eBPF program portability and eBPF runtime requirements becomes more important and requires coordination." 






Want to know more? Go to the free and virtual [eBPF Summit](https://ebpf.io/summit-2021/), on August 18-19, 2021. You'll be glad you did. EBPF is bringing fundamental changes to networking, security, and applications across the entire infrastructure stack from PCs to the cloud. 

**Related Stories:** 

* [Porting Linux's eBPF to Windows 10 and Windows Server](https://www.zdnet.com/article/porting-linuxs-ebpf-to-windows-10-and-windows-server/)
* [Patch now: Linux file system security hole, dubbed Sequoia, can take over systems](https://www.zdnet.com/article/patch-now-linux-file-system-security-hole-dubbed-sequoia-can-take-over-systems/)
* [New Relic open sources Pixie, its Kubernetes-native in-cluster observability platform](https://www.zdnet.com/article/new-relic-open-sources-pixie-its-kubernetes-native-in-cluster-observability-platform/)





#### Tags:
[[eBPF]] [[Linux]] [[Windows]] [[EBPF]] [[eBPF-based]] [[ZDNet]]
