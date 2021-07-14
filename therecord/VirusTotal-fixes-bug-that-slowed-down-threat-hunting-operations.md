# VirusTotal fixes bug that slowed down threat hunting operations
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/virustotal-fixes-bug-slowing-down-threat-hunting-operations/)
+ Date: July 8, 2021
+ Author: Catalin Cimpanu


## Article:
![VirusTotal fixes bug that slowed down threat hunting operations](https://therecord.media/wp-content/uploads/2021/07/VirusTotal.png)

Malware scanning service and threat intelligence platform VirusTotal said it fixed a bug today that was slowing down threat hunting operations on its website.


The bug impacted the [YARA](https://en.wikipedia.org/wiki/YARA) scanning engine, a component of the VirusTotal website that allows security researchers to use text-based rules to search through the site’s gigantic malware database.


According to Victor Manuel Alvarez, a software engineer at VirusTotal and the creator of the YARA threat-hunting engine, an innocent-looking pattern was to blame for this week’s problems.


 
In a Twitter thread, Alvarez described the problem as follows:


“The actual pattern was even more inconspicuous, it looked very similar to other patterns that don’t cause any trouble, but the devil is in the details. The multiple and relatively long jumps like [0-60], separated by the short and common pattern 00 were the cause of the issue.   
  
YARA uses two different algorithms for matching patterns like this: one is a more complex algorithm for full-fledged regular expressions, and the other is a simpler, more naive algorithm for certain hex patterns like the one above.   
  
These hex patterns could be matched using the full-fledged regexp algorithm (they can be expressed as a tradicional regexp) but the naive algorithm is usually faster. *Usually*.   
  
The full-fledged regexp algorithm is slower than the naive algorithm for 99% of the cases, but it has a good property: it’s time complexity is linear, there are no “bad cases” that can slow down the algorithm exponentially.   
  
The naive algorithm is faster in most cases, but it’s has an exponential time grow. Bad cases are really bad. The rule that caused this issue is one of those really bad cases.”


Alvarez described the issue as a very rare scenario and one that the company had not seen in years.


The issue impacted VirusTotal customers, especially on Wednesday, when it slowed down most YARA rule searches on the platform.


“It impacted our research into the Kaseya incident, but since this is the first issue we’ve seen on VirusTotal, our frustration level remained low,” a researcher working with CERT France told *The Record*.


The issue has been fixed, and the VirusTotal service is back up and running normally today, a VT engineer told us.








#### Tags:
[[VirusTotal]] [[YARA]] [[Alvarez]] [[full-fledged]] [[regexp]] [[The Record]]
