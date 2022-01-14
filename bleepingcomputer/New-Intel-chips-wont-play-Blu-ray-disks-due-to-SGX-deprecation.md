# New Intel chips won't play Blu-ray disks due to SGX deprecation
### Intel has removed support for SGX (software guard extension) in 12th Generation Intel Core 11000 and 12000 processors, rendering modern PCs unable to playback Blu-ray disks in 4K resolution.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/new-intel-chips-wont-play-blu-ray-disks-due-to-sgx-deprecation/
+ Date: 2022-01-14T11:46:42-05:00
+ Author: Bill Toulas


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/01/26/Intel-CPU.jpg)

![intel](https://www.bleepstatic.com/content/hl-images/2021/01/26/Intel-CPU.jpg?rand=1953177310)


Intel has removed support for SGX (software guard extension) in 12th Generation Intel Core 11000 and 12000 processors, rendering modern PCs unable to playback Blu-ray disks in 4K resolution.


This technical problem arises from the fact that Blu-ray disks require Digital Rights Management (DRM), which needs the presence of SGX to work.


This is a feature that Intel introduced in the Skylake generation back in 2016, enabling PCs to play protected Blu-ray disks for the first time.


As seen in Intel's current datasheets for the 11th and 12th generation of its Core desktop processors, the SGX is listed as a deprecated technology, so it's no longer available.



![Intel's datasheet for 12th gen CPUs](https://www.bleepstatic.com/images/news/u/1220909/devices/deprecated.jpg)**Intel's datasheet for 12th gen CPUs**
Why did Intel abandon SGX?
--------------------------


As a secure enclave technology, SGX was commonly targeted by security researchers who discovered numerous vulnerabilities and attack methods.


Examples of attacks targeting Intel SGX include:


* the Prime+Probe attack discovered in 2017,
* a Spectre-like attack disclosed in 2018,
* an Enclave attack discovered by researchers in 2019,
* a MicroScope replay attack,
* the so-called "Plundervolt" injection attack,
* a Load Value Injection (LVI), and
* the SGAxe attack on the CPU cache resulting in the leak of the enclave's content.

In summary, Intel had more to gain from SGX's deprecation from the perspective of security. 


Considering that most users don't care about Blu-ray playback on the PC, taking that decision must have been straightforward.


Impact and solutions
--------------------


The issue impacts Ultra HD Blu-ray discs that use DRM, so if the Blu-ray Disc Association ever decides to lift the strict protections, the playback will return to nominal resolutions (3840 x 2160).


Also, since SGX was removed in recent chip generations, users who would like to avoid problems can stick to using 7000, 8000, 9000, or 10000-series CPUs.


Skylake (6000 series) has SGX but misses HDCP 2.2, and that would cause hurdles with HDMI 2.0 transmission.


CyberLink, the company behind the "PowerDVD" software product, has updated its FAQ to reflect the problem with newer gen Intel processors, claiming inability to resolve it in any way.


"The removal of the SGX feature, and its compatibility with the latest Windows OS and drivers, has caused a substantial challenge for CyberLink to continue supporting Ultra HD Blu-ray movie playback in our player software." - details [the FAQ page](https://www.cyberlink.com/support/faq-content.do?id=26690).


"So much so, that it has been determined that it is no longer feasible for CyberLink to support the Ultra HD Blu-ray playback on newer CPUs and the latest Windows platforms."


In addition to using an older Intel CPU, CyberLink also advises people not to upgrade to Windows 11 to avoid having the needful drivers replaced.


Blu-ray disks in 2022
---------------------


Blu-ray disks may sound like something from the distant past that has been phased out, but it's [not obsolete yet](https://www.businessinsider.com/dvd-collectors-physical-discs-not-dead-streaming-netflix-digital-2021-6).


People are still buying them because they have collectible value and they enjoy having something physical and tangible, giving a sense of ownership and possibly even attachment.



> 
> Some people: I like getting my movies on plastic discs, because I actually own them that way.  
> 
> CyberLink: Don't update your CPU, OS, or drivers, or you won't be able to play your plastic discs. <https://t.co/5x4tWgKjfn> [pic.twitter.com/hNpesedl9j](https://t.co/hNpesedl9j)
> 
> 
> — Will Dormann (@wdormann) [January 14, 2022](https://twitter.com/wdormann/status/1481961821825347587?ref_src=twsrc%5Etfw)


Moreover, Blu-ray disks can offer 4K content entertainment without an internet connection, and the quality is stable and guaranteed, contrary to streaming.


No matter if a movie leaves a streaming service or if the digital rights change in the future, a physical disk makes the content permanently available.


And finally, some people are just nostalgic or enjoy following the "ritual" of putting the disk on the drive.


For all the above reasons and many more, Ultra HD Blu-ray isn't dead yet, and Intel's decision to deprecate the SGX will impact a substantial number of users.





## Tags:

#### Threatactor:
[[threatactor.name=BRONZE BUTLER]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]]

#### Industry:
[[victim.industry.name=Entertainment]]

#### Location:
[[victim.city.name=Berlin]] [[victim.country.name=Germany]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Blu-ray]] [[Sgx]] [[Cyberlink]] [[12th]] [[Windows]] [[Bleeping Computer]]
#### urls
https://t.co/5x4tWgKjfn

