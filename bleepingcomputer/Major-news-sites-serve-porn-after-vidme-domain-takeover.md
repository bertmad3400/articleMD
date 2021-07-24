# Major news sites serve porn after vid.me domain takeover
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/technology/major-news-sites-serve-porn-after-vidme-domain-takeover/)
+ Date: July 23, 2021
+ Author: Ax Sharma


## Article:
![woman laughing](https://www.bleepstatic.com/content/hl-images/2021/01/08/woman-laughing.jpg)


Major news sites including The Washington Post, New York Magazine, and HuffPost, saw their stories now displaying porn videos instead of the once-embedded intended ones.


The fiasco happened as prominent websites relied on the domain *vid.me* to embed streaming videos in their articles.


The *vid.me* domain has been defunct for about four years and has had its ownership transferred over time to different parties.


For those who prefer to watch... 'Right in front of my salad?'
--------------------------------------------------------------


Websites of major news outlets such as The Washington Post, New York Magazine, and Huffpost, among others, shocked readers when their stories displayed NSFW videos, with no relevance to the story.


As seen by BleepingComputer today, unfortunately, some news sites are still *stuck with this mess*:



![vidme embed example](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/vidme-embed/vidme-example.jpg)**An example of a news story still showing embedded NSFW videos replacing the legitimate ones**​​​​​
The incident, first [reported](http://www.vice.com/en/article/qj8xz3/a-defunct-video-hosting-site-is-flooding-normal-websites-with-hardcore-porn) by Motherboard, was spotted yesterday by a user *DOXIE*, who has shared many more examples in their Twitter thread:


 




> 
> Twitter hasn’t noticed but a now-defunct video hosting/advertising platform (VidMe) let their domain expire so it was purchased by a porn website, now there is NSFW porn all over the regular internet where their links were embedded lol  
>   
> 
> For example: <https://t.co/UdPRFnq4EP>
> 
> 
> — DOXIE (@dox\_gay) [July 22, 2021](https://twitter.com/dox_gay/status/1418189401188970503?ref_src=twsrc%5Etfw)


How did this happen?
--------------------


Essentially, the affected sites had been relying on the video streaming provider, Vidme, to embed streaming content.


To do so, websites would use HTML iframes to display the videos hosted on the *vid.me*domain:



![iframe embedding videos](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/vidme-embed/vidme-iframe.jpg)**HTML iframe would previously display a legitimate video** (BleepingComputer)
However, Vidme has long been defunct. 


In 2017, Vidme shut down its operations with *vid.me's* homepage showing a farewell message:



![vidme site farewell](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Farewell message previously displayed on Vid.me site since 2017**(BleepingComputer)
A [blog post](https://medium.com/vidme/goodbye-for-now-120b40becafa) followed stating Vidme had been acquired by Giphy. Any hosted videos were scheduled for deletion on December 15th, 2017.


In practice, this meant, those iframes embedding hosted videos would have ideally shown nothing or, maybe an error message under usual circumstances.


But, according to [WHOIS](https://uk.godaddy.com/whois/results.aspx?checkAvail=1&domain=vid.me) results, vid.me domain's ownership and/or registration was updated sometime this month.


*DOXIE* hypothesized that the domain had expired and was taken over by a porn company, "5 Star HD Porn" which now redirects all *vid.me* links to the porn site.


As such, all of the websites previously embedding content from Vidme via iframes were now serving hardcore porn.


Some have cheekily [surmised](https://twitter.com/campuscodi/status/1418330548439855105) if this counts as a supply-chain incident.


5 Star HD Porn who now apparently owns the *vid.me* domain, did not respond to Motherboard's request for comment.


Suffice to say, if you were previously using Vidme to host content on your website, it makes sense to purge any and all links to the defunct service.


Readers who prefer to block content from this domain from appearing in unexpected places can add vid.me to their system's hosts file, as [suggested](https://twitter.com/neil_neilzone/status/1418444683936731136) by tech lawyer Neil Brown.


There's a [tutorial](https://www.bleepingcomputer.com/tutorials/hosts-files-explained/) on BleepingComputer explaining how to accomplish this. Adding the following line to your *hosts*file (without *http://*) should suffice:


127.0.0.1 vid.me


#### Tags:
[[vid]] [[Vidme]] [[BleepingComputer]] [[websites]] [[NSFW]] [[iframes]] [[Bleeping Computer]]
