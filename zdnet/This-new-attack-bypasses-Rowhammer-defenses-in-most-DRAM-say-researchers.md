# This new attack bypasses Rowhammer defenses in most DRAM, say researchers
### New technique targets industry-wide mitigations implemented in response to the first Rowhammer attack.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-new-attack-bypasses-rowhammer-defenses-in-most-dram-say-researchers/)
+ Date: November 16, 2021
+ Author: Liam Tung


## Article:
Unknown

Researchers have revealed a new type of Rowhammer attack on DRAM devices that can reliably bypass mitigations implemented by vendors after the first such attacks emerged in 2014. 


Data in Dynamic DRAM (DRAM) is stored in grids of memory. Rowhammer attacks work by rapidly and repeatedly reading data in one memory row to cause an electrical charge in adjacent memory rows in order to modify or corrupt data. 

**SEE:** [**A winning strategy for cybersecurity**](http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/#link=%7B%22role%22:%22standard%22,%22href%22:%22http://www.zdnet.com/topic/a-winning-strategy-for-cybersecurity/%22,%22target%22:%22_blank%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EA%20winning%20strategy%20for%20cybersecurity%3C/strong%3E%22%7D) **(ZDNet special report)**

The latest Rowhammer attack seeks to bypass Target Row Refresh (TRR) mitigations that the DRAM industry added to modern RAM cards in response to the first Rowhammer attack in 2014. 

The researchers from ETH Zurich, Vrije Universiteit Amsterdam, and Qualcomm ran their attack – via a fuzzer called [Blacksmith, available on GitHub](https://github.com/comsec-group/blacksmith) – against various proprietary TRR implementations in 40 DRAM devices. The technique allowed them to quickly discover ways to cause bit flips in all of them. 

"This result has a significant impact on the system's security as DRAM devices in the wild cannot easily be fixed, and previous work showed real-world Rowhammer attacks are practical, for example, in the browser using JavaScript, on smartphones, across VMs in the cloud, and even over the network," the group said.

"All currently deployed mitigations are insufficient to fully protect against Rowhammer. Our novel patterns show that attackers can more easily exploit systems than previously assumed," they warned.






The 40 devices were from memory vendors Samsung, Micron, SK Hynix, as well as two more vendors that didn't agree to have their names published in the research.      

"TRR aims to detect rows that are frequently accessed (i.e., hammered) and refresh their neighbors before their charge leak results in data corruptions," [the researchers explain in a new paper](https://comsec.ethz.ch/wp-content/files/blacksmith_sp22.pdf). 

While TRR for the most part works when detecting even multiple aggressor rows being hammered frequently, the researchers note that past Rowhammer attacks "always access aggressors uniformly".  

TRR in this sense does create a cost problem for attackers because the space to search for non-uniform patterns that can bypass the mitigation is "huge", the researchers explain. Their answer was to run the Blacksmith fuzzer for 12 hours on sampled DDR4 DRAM devices in order to discover and build non-uniform patterns that expose weaknesses in TRR implementations designed to look for various uniform patterns. 

"Thereafter, we *swept* the best pattern (based on the number of total bit flips triggered) over a contiguous memory area of 256 MB and report the number of bit flips," [they explain in a blogpost](https://comsec.ethz.ch/research/dram/blacksmith/).

**SEE: [This mysterious malware could threaten millions of routers and IoT devices](https://www.zdnet.com/article/this-mysterious-malware-could-threaten-millions-of-routers-and-iot-devices/)**

The technique enabled them to use these non-standard patterns to trigger bit flips in all 40 DRAM devices. In some cases, the technique uncovered several thousand bit flips within seconds.

This type of Rowhammer attack targeting TRR is likely to get more powerful in future. The group says it is working with Google to fully integrate the Blacksmith fuzzer into an open-source FPGA Rowhammer-testing platform. 

The researchers' findings are being tracked as CVE-2021-42114. The researchers have discussed their findings with Intel and Google, which separately this week launched a new open-source Rowhammer Tester platform.





#### Tags:
[[Rowhammer]] [[TRR]] [[mitigations]] [[fuzzer]] [[ZDNet]]
