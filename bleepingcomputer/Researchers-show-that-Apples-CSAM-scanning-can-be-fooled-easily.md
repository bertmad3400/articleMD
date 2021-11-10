# Researchers show that Apple’s CSAM scanning can be fooled easily
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/technology/researchers-show-that-apple-s-csam-scanning-can-be-fooled-easily/)
+ Date: November 10, 2021
+ Author: Bill Toulas


## Article:
![AI](https://www.bleepstatic.com/content/hl-images/2021/11/10/artificial-intelligence-face-header.jpg)


A team of researchers at the Imperial College in London have presented a simple method to evade detection by image content scanning mechanisms, such as Apple's CSAM.


CSAM (Child Sexual Abuse Material) was a controversial proposal submitted by Apple earlier this year. The proposal was eventually retracted in September, following strong backlash from customers, advocacy groups, and researchers.


Apple hasn't abandoned CSAM but rather [postponed its roll-out](https://www.apple.com/child-safety/) for 2022, promising new rounds of improvements and a more transparent approach in its development.


The main idea is to compare image hashes (IDs) of pictures shared privately between iOS users to a database of hashes provided by NCMEC and other child safety organizations.


If a match is found, Apple's reviewers will look into the content and alert the authorities of the distribution of child abuse and pornography, all without compromising the privacy of people who share legal images (non-matches).


This theoretically sounds like a good system to prevent the dissemination of harmful material, but practically, it inevitably opens a "Pandora's box" for [mass surveillance](https://www.nytimes.com/2021/10/14/business/apple-child-sex-abuse-cybersecurity.html).


However, the question that researchers at the Imperial College in London asked is, would such a detection system even work reliably in the first place?


Tricking the algorithm
----------------------


The research presented at the recent [USENIX Security Symposium](http://www.usenix.org/conference/usenixsecurity22/presentation/jain) by British researchers shows that neither Apple's CSAM nor any system of this type would effectively detect illegal material.


As the researchers explain, it’s possible to fool content detection algorithms 99.9% of the time without visually changing the images.


The trick is to apply a special hashing filter on the images, making them appear different to the detection algorithm even if the processed result looks identical to the human eye.


The paper presents two white-box and one black-box attack for discrete cosine transform-based algorithms, successfully altering an image's unique signature on a device and helping it fly under the radar.



![Applying a filter onto the images gives them new identity without changing the content](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/hashing.jpg)**Images before and after the filter look visually identical**  
*Source: Imperial College London*
Countermeasures and complications
---------------------------------


A possible countermeasure to the evasion methods presented in the paper would be to use a larger detection threshold, leading to an increase in false positives.


Another approach would be to flag users only after image ID matches reach a certain threshold number, but this introduces probability complications.


Applying additional image transformation before computing the perceptual hash of the image is also unlikely to make detections any more reliable.


Increasing the hash size from 64 to 256 would work in some cases, but this introduces privacy concerns as longer hashes encode more information about the image.


All in all, the research demonstrates that current perceptual hashing algorithms are not nearly as robust as they should be for adoption in illegal content distribution mitigation strategies.



> 
> "Our results shed strong doubt on the robustness to adversarial black-box attacks of perceptual hashing-based client-side scanning as currently proposed. The detection thresholds necessary to make the attack harder are likely to be very large, probably requiring more than one billion images to be wrongly flagged daily, raising strong privacy concerns." - concludes [the paper](https://www.usenix.org/system/files/sec22summer_jain.pdf).
> 
> 
> 


This is a significant finding coming at a time when governments are considering hash-based invasive surveillance mechanisms.


The paper shows that for illegal image detection systems to work reliably in their current form, people will have to give up their privacy, and there's no technical way around this at this time.




#### Tags:
[[CSAM]] [[Bleeping Computer]]
