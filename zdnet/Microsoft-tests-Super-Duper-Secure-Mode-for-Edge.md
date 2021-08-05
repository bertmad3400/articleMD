# Microsoft tests Super-Duper Secure Mode for Edge
### Microsoft's Edge security researchers are testing how removing the JIT compilation from the V* processing pipeline would affect security and performance. Edge Insider testers can check out SDSM now.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-is-testing-a-super-duper-secure-mode-for-its-edge-browser/)
+ Date: August 5, 2021 -- 15:14 GMT (16:14 BST)
+ Author: Mary Jo Foley


## Article:
Unknown

![microsoft-edge.jpg](https://www.zdnet.com/a/hub/i/r/2021/08/05/c2577ec7-d0d7-448c-8c69-09c9d5d02242/resize/1200xauto/0809546c60e70196a91206ab0fa5c7e9/microsoft-edge.jpg)
 (Image: Shutterstock)
 Microsoft's Edge Vulnerability Research (VR) team is testing a new feature they've christened, ["Super Duper Secure Mode" (SDSM)](https://microsoftedge.github.io/edgevr/posts/Super-Duper-Secure-Mode/). Super-Duper Secure Mode is all about making Edge more secure without negatively impacting performance.


SDSM works by removing Just-In-Time compilation from the V8 processing pipeline, which will reduce the attack surface that can be used to hack into Edge's systems, as Bleeping Computer ([where I first saw the SDSM information](https://www.bleepingcomputer.com/news/microsoft/microsoft-edge-just-got-a-super-duper-secure-mode-upgrade/)) explains. In addition to disabling the JIT, SDSM enables "new security mitigations" to make Edge a more secure browser.   
   
 "JavaScript plays a key role in any browser story. JITs exist for a reason, and that is to optimize JavaScript performance," the Microsoft browser researchers noted in their August 4 blog post about SDSM. However, so far, the researchers said they don't see much of a change in performance with JIT disabled; most of their tests remained unchanged.   
   
 By disabling the JIT, roughly half of the V8 bugs that must be fixed would be removed. This would mean less frequent security updates and fewer emergency patches for users, the researchers noted.   
   
 SDSM is still considered to be in the experimental stage. Still, Edge preview testers -- in the Canary, Dev and Beta rings -- can enable it now with a flag by going to *edge://flags/#edge-enable-super-duper-secure-mode* and turning on the new feature.   
 





#### Tags:
[[SDSM]] [[ZDNet]]
