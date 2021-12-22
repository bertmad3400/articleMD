# An IDOR Bug In Facebook Android Could Expose Page Admins
### Meta confirmed patching the Facebook Android app bug revealing Page admins, while rewarding the researcher with a $4500 bounty.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2021/12/21/an-idor-bug-in-facebook-android-could-expose-page-admins-patch-deployed/
+ Date: 2021-12-21
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2021/12/facebook-app.jpg)
 A researcher discovered a security vulnerability affecting Meta’s Facebook platform, winning him a hefty bounty. Specifically, an IDOR bug affected the Facebook Android app that could expose page admins.

 Facebook Bug Exposing Page Admins
---------------------------------

 19-year old security researcher from Nepal, Sudip Shah, has shared a [blog post](https://medium.com/pentesternepal/how-i-was-able-to-reveal-page-admin-of-almost-any-page-on-facebook-5a8d68253e0c) detailing an IDOR vulnerability affecting Facebook.

 Specifically, he caught the bug in the Facebook Android app that potentially disclosed the names of Facebook page admins while watching [live videos](https://latesthackingnews.com/2021/04/26/serious-vulnerability-in-facebook-could-allow-deleting-live-videos/).

 While not entirely a secret, the platform keeps the identities of Facebook page administrators hidden from the followers and the general users for privacy. Hence, this IDOR ([Insecure Direct Object Reference](https://latesthackingnews.com/2017/07/09/web-applications-attacks-insecure-direct-object-reference/)) bug posed a significant privacy risk.

 The researcher found this vulnerability upon analyzing the Facebook for Android app after multiple unsuccessful attempts of finding noteworthy bugs in the web platform.

 Describing the vulnerability, the researcher stated,

 
> While intercepting and navigating to the other page’s live video section in FB android, I found a vulnerable endpoint in the `doc_id=4449530781773796` , where when the `page_id` in the request is changed to any page then the page admin is disclosed in the response in the `broadcaster_id` parameter.
> 
> 

 Shah believes this bug could pose a significant threat to most [Facebook Pages](https://latesthackingnews.com/2021/01/16/facebook-page-vulnerability-could-allowed-users-to-create-invisible-posts/) given the ease of exploitation. Especially when it could allow mass-scale attacks via automated scripts. He has even demonstrated the PoC in the following video.

  Meta Patched The Flaw
---------------------

 Following this discovery, the researcher contacted Facebook officials on October 5, 2021. He then got a response from the vendors, who acknowledged the vulnerability and started investigations.

 Consequently, the tech giant confirmed deploying the fix on October 21, 2021. Also, the researcher won a $4500 bounty for this report.

 Since the fix is deployed, Android users must ensure updating their devices with the latest Facebook app version for security.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Tor]]

#### Location:
[[victim.country.name=Nepal]] [[victim.continent.name=Asia]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Facebook]] [[Android]] [[Idor]] [[Latest Hacking News]]
