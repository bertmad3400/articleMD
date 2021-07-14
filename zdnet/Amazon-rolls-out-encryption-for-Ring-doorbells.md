# Amazon rolls out encryption for Ring doorbells
### Privacy advocates have been asking for Amazon to encrypt its popular Ring doorbells audio and video traffic, and Amazon is finally delivering it.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/amazon-rolls-out-encryption-for-ring-doorbells/)
+ Date: July 13, 2021 -- 19:02 GMT (20:02 BST)
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

Did you know that that handy video your [Ring doorbell](https://ring.com/doorbell-cameras) takes of anyone coming by your door isn't private? If you get a [Ring Protect Plan](https://ring.com/protect-plans), not only are your videos kept in the [Amazon Web Services (AWS) cloud](https://aws.amazon.com/), it's transmitted in the clear. A sufficiently motivated hacker, or your local police force, can easily watch who's walking by your door. Until now. Starting today in the US (and soon, throughout the world), you'll be able to encrypt your video stream to keep it private.


This is done with [Amazon's Video End-to-End Encryption (E2EE)](https://support.ring.com/hc/en-us/articles/360054941511-Understanding-Video-End-to-End-Encryption-E2EE-). If you decide to install this optional privacy feature, you'll need to [install a new version of the Ring application on your smartphone](https://support.ring.com/hc/en-us/articles/360054941551-How-to-Set-Up-Video-End-to-End-Encryption-E2EE-). Once installed, it uses a [Public Key Infrastructure (PKI)](https://www.keyfactor.com/resources/what-is-pki/) security system based on an [RSA 2048-bit asymmetric account signing key pair](https://aws.amazon.com/blogs/security/digital-signing-asymmetric-keys-aws-kms/). In English, the foundation is pretty darn secure.

Earlier, Ring already encrypted videos when they are uploaded to the cloud (in transit) and stored on Ring's servers (at rest). Law enforcement doesn't have automatic access to customer devices or videos. You choose whether or not to share footage with law enforcement. With E2EE, customer videos are further secured with an additional lock, which can only be unlocked by a key that is stored on the customer's enrolled mobile device, designed so that only the customer can decrypt and view recordings on their enrolled device.

In addition, you'll need to opt into using E2EE. It doesn't turn on automatically with the software update. You'll also need to set a passphrase, which you must remember. AWS doesn't keep a copy. If you lose it, you're out of luck.  

Before using E2EE, you should know AWS hasn't integrated E2EE fully into the Ring's feature set. In other words, there are many features -- such as sharing your videos, being able to view encrypted videos on Ring.com, the Windows desktop app, the Mac desktop app, or the Rapid Ring app, and the Event Timeline -- that you won't be able to use. 

E2EE also won't work with many Ring devices. In particular, E2EE won't run on Ring's most popular, least expensive, battery-powered Ring doorbells. 

Even with E2EE security, the police can ask for or demand your video and audio content. As Matthew Guariglia, an [Electronic Freedom Foundation (EFF)](https://www.eff.org/) policy analyst, has pointed out: "If your town's [police department has a partnership with Ring](https://www.eff.org/deeplinks/2019/08/five-concerns-about-amazon-rings-deals-police), you can also [anticipate getting email requests from them asking for footage from your camera](https://www.eff.org/deeplinks/2020/02/what-know-you-buy-or-install-your-amazon-ring-camera) any time a suspected crime occurs nearby."






According to a Ring representative, Ring's E2EE is designed so that even the company cannot decrypt your end-to-end encrypted video. That includes law enforcement officers because the private keys required to decrypt the videos are only stored on customer's enrolled mobile devices.

Until recently, by default, [police could send automatic bulk email requests to individual Ring users](https://www.eff.org/deeplinks/2021/06/ring-changed-how-police-request-door-camera-footage-what-it-means-and-doesnt-mean) in an area of interest of up to a square half-mile. Now, police can publicly post their requests to [Ring's Neighbors app](https://ring.com/neighbors). 

Guariglia also observed, "Ring's default setup is primed to [instill paranoia](https://www.npr.org/2019/12/02/784225316/doorbell-cameras-are-popular-but-should-we-be-sharing-the-videos-online): Ring doorbells send you an alert whenever the motion activation is triggered, which means that your phone will buzz every time a squirrel, falling snow, a dog walker, or a delivery person set off the Ring." For example, many people now believe that [violent crime is worse than ever in the US](https://www.theguardian.com/us-news/2021/jun/30/us-crime-rate-homcides-explained). That's simply not true.

Privacy, on the other hand, is under siege. If you value your privacy, and you still like the convenience of Ring, I encourage you to use E2EE. I will be.

### **Related Stories:**

* [Ring trials customer video end-to-end encryption for smart doorbells](https://www.zdnet.com/article/ring-trials-customer-video-end-to-end-encryption/)
* [Best security system in 2021: Secure your home or business](https://www.zdnet.com/article/best-home-security-system/)
* [Best video doorbell 2021: Ring isn't your only option](https://www.zdnet.com/article/best-video-doorbell/)





#### Tags:
[[E2EE]] [[AWS]] [[ZDNet]]
