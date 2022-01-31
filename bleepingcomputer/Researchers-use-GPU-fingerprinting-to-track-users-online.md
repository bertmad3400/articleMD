# Researchers use GPU fingerprinting to track users online
### A team of researchers from French, Israeli, and Australian universities has explored the possibility of using people's GPUs to create unique fingerprints and use them for persistent web tracking.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/researchers-use-gpu-fingerprinting-to-track-users-online/
+ Date: 2022-01-30T10:12:24-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2022/01/26/gpu.jpg)

![gpu](https://www.bleepstatic.com/content/hl-images/2022/01/26/gpu.jpg?rand=1723900986)


A team of researchers from French, Israeli, and Australian universities has explored the possibility of using people's GPUs to create unique fingerprints and use them for persistent web tracking.


The results of their large-scale experiment involving 2,550 devices with 1,605 distinct CPU configurations show that their technique, named 'DrawnApart,' can boost the median tracking duration to 67% compared to current state-of-the-art methods.


This is a severe problem for user privacy, which is currently protected by laws that focus on acquiring consent to activate website cookies.


These laws have led unscrupulous websites to collect other potential fingerprinting elements such as the hardware configuration, OS, timezones, screen resolution, language, fonts, etc.


This unethical approach is still limited because these elements change frequently, and even when they're stable, they can only put users into a rough categorization rather than create a unique fingerprint.


Fingeprinting identical GPUs
----------------------------


The researchers considered the possibility of creating distinctive fingerprints based on the GPU (graphics processing unit) of the tracked systems with the help of WebGL (Web Graphics Library).


WebGL is a cross-platform API for rendering 3D graphics in the browser, and it's present on all modern web browsers.


Using this library, the DrawnApart tracking system can count the number and speed of the execution units in the GPU, measure the time needed to complete vertex renders, handle stall functions, and more.



![Fingerprinting the GPU for persistent tracking](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/fingerprinting.jpg)**Fingerprinting the GPU for persistent tracking**  
*Source: Arxiv.org*
DrawnApart uses short GLSL programs executed by the target GPU as part of the vertex shader to overcome the challenge of having random execution units handling the computations. Hence, the workload allocation is predictable and standardized.


The team developed both an on-screen measurement method that executes a small number of computationally intensive operations and an offscreen method that puts the GPU through a lengthier and less intensive test.



![Render loop used for the on-screen test](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/render-loop.jpg)**Render loop used for the on-screen test**  
*Source: Arxiv.org*
This process generates traces consisting of 176 measurements taken from 16 points that are used to create a fingerprint. Even when evaluating the individual raw traces visually, one can notice differences and distinct timing variations between devices.



![The resulting raw traces from two identical GPUs](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**The resulting raw traces from two identical GPUs**  
*Source: Arxiv.org*
The researchers also tried swapping other hardware parts on the machines to see if the traces would remain distinguishable and found that the fingerprints solely depended on the GPU.


Even if a set of integrated circuits is created through an identical manufacturing process, has the same nominal computational power, the number of processing units, and the exact same cores and architecture, each circuit is slightly different due to normal manufacturing variability.


These differences are indistinguishable in normal day-to-day operations, but they can become useful in the context of a sophisticated tracking system like DrawnApart, which is specifically designed to trigger functional aspects that highlight them.



![Tested devices and classification accuracy](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Tested devices and classification accuracy**  
*Source: Arxiv.org*
Implications and considerations
-------------------------------


When DrawnApart is used in conjunction with state-of-the-art tracking algorithms, the median tracking duration of a targeted user increases by 67%.


As illustrated in the following diagram, the standalone tracking algorithm can achieve an average tracking time of 17.5 days, but with the help of GPU fingerprinting, this is extended to 28 days.



![Tracking duration diagram](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Tracking duration diagram**  
*Source: Arxiv.org*
This evaluation was based on the testing conditions that the GPU operational temperature range is between 26.4 °C and 37 °C, with no voltage variations.


Apart from these conditions, workload variations, GPU payloads from other web browser tabs, system restarts, and other runtime changes don't affect DrawnApart.


The next-gen GPU APIs currently in development, most notably WebGPU,  features compute shaders which come in addition to the existing graphics pipeline.


As such, the upcoming API may introduce even more ways to fingerprint internet users, and quite likely faster and far more accurate too.


When the researchers tested compute shaders in the now-abandoned WebGL 2.0, they found that DrawnApart delivered 98% classification accuracy in just 150 milliseconds, much faster than the 8 seconds used to collect fingerprinting data through the WebGL API.


"We believe that a similar method can also be found for the WebGPU API once it becomes generally available. The effects of accelerated compute APIs on user privacy should be considered before they are enabled globally," concludes [the research paper](https://arxiv.org/pdf/2201.09956.pdf).


Potential countermeasures to this fingerprinting method include attribute value changes, parallel execution prevention, script blocking, API blocking, and time measurement prevention.


The developer of the WebGL API, Khronos group, has received the researchers' disclosure on the above and formed a technical study group to discuss potential solutions with browser vendors and other stakeholders.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]]

#### Industry:
[[victim.industry.name=Manufacturing]]

#### Location:
[[victim.country.name=Israel]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]] [[victim.country.name=Australia]] [[victim.continent.name=Oceania]] [[victim.country.name=Australia]] [[victim.continent.name=References]]

### Autogenerated Tags:
[[Gpu]] [[Api]] [[Drawnapart]] [[Webgl]] [[Arxiv.org]] [[Bleeping Computer]]

