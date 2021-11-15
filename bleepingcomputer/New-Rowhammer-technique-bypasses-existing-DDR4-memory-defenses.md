# New Rowhammer technique bypasses existing DDR4 memory defenses
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/new-rowhammer-technique-bypasses-existing-ddr4-memory-defenses/)
+ Date: November 15, 2021
+ Author: Bill Toulas


## Article:
![hammers](https://www.bleepstatic.com/content/hl-images/2021/11/15/hammers.jpg?rand=887099710)


Researchers have developed a new fuzzing-based technique called 'Blacksmith' that revives Rowhammer vulnerability attacks against modern DRAM devices that bypasses existing mitigations.


The emergence of this new Blacksmith method demonstrates that today's DDR4 modules are vulnerable to exploitation, allowing a variety of attacks to be conducted.


The Rowhammer effect
--------------------


Rowhammer is a security exploit that relies on the leaking of electrical charges between adjacent memory cells, enabling a threat actor to flip 1s and 0s and change the content in the memory.


This powerful attack can bypass all software-based security mechanisms, leading to privilege escalation, memory corruption, and more.


It was first discovered in 2014, and within a year, two working privilege escalation exploits based on the researcher were [already available](https://www.blackhat.com/docs/us-15/materials/us-15-Seaborn-Exploiting-The-DRAM-Rowhammer-Bug-To-Gain-Kernel-Privileges.pdf).


Gradually, this became a widespread problem, and even Android tools were developed, exploiting the Rowhammer vulnerability on smartphones to gain root access.


The mitigations applied to address this bit-flipping problem showed the first signs of their insufficiency in March 2020, when academic researchers proved that a bypass was possible.


Manufacturers had implemented a set of mitigations called "Target Row Refresh" (TRR), which were mainly effective in keeping the then-new DDR4 safe from attacks.


The attack used against it was called '[TRRespass](https://www.bleepingcomputer.com/news/security/ddr4-memory-still-at-rowhammer-risk-new-method-bypasses-fixes/),' and was another fuzzing-based technique that successfully found usable Rowhammering patterns.


Fuzzing a new way in
--------------------


'TRRespass' was able to find effective patterns in 14 of the 40 tested DIMMs, realizing a roughly 37.5% success. However, 'Blacksmith' found effective Rowhammer patterns on all of the 40 tested DIMMs.


The trick that the researchers used this time is not to approach the hammering patterns uniformly but instead explore non-uniform structures that can still bypass TRR.


The team used order, regularity, and intensity parameters to design frequency-based Rowhammer patterns and then fed them to the Blacksmith fuzzer to find working values.



![The architecture of a BlackSmith attack](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/blacksmith_arch.jpg)**The architecture of a BlackSmith attack**  
*Source: Comsec*
This essentially revealed new exploitation potential that previous researches missed, as illustrated in the video below.



The fuzzer ran for 12 hours and yielded the optimal parameters to use in a Blacksmith attack. Using these values, the researchers were able to perform bit flips over a contiguous memory area of 256 MB.


To prove that this is exploitable in real-world scenarios, the team performed test attacks that allowed them to retrieve private keys for public RSA-2048 keys used to authenticate to an SSH host.



> 
> Concluding, our work confirms that the DRAM vendors’ claims about Rowhammer protections are false and lure you into a false sense of security. All currently deployed mitigations are insufficient to fully protect against Rowhammer. Our novel patterns show that attackers can more easily exploit systems than previously assumed. - [Comsec](https://comsec.ethz.ch/research/dram/blacksmith/).
> 
> 
> 


Comsec further found that while using ECC DRAM will make exploitation harder, they will not defend against all Rowhammer attacks.


DDR5 may be safer
-----------------


Newer DDR5 DRAM modules are already available in the market, and adoption will pick up pace in the next couple of years.


In DDR5, Rowhammer may not be as much of a problem, as [TRR is replaced](https://comsec.ethz.ch/wp-content/files/blacksmith_sp22.pdf) by "refresh management," a system that keeps track of activations in a bank and issues selective refreshes once a threshold is reached.


This means that scalable fuzzing on a DDR5 DRAM device would be a lot harder and possibly a lot less effective, but that remains to be seen.




#### Tags:
[[Rowhammer]] [[mitigations]] [[DDR5]] [[Bleeping Computer]]
