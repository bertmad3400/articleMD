# Smartwatches for children are a privacy and security nightmare
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/smartwatches-for-children-are-a-privacy-and-security-nightmare/)
+ Date: November 30, 2021
+ Author: Bill Toulas


## Article:
![Kids smartwatch](https://www.bleepstatic.com/content/hl-images/2021/11/30/kids-smartwatches.jpg)


Researchers analyzed the security of four popular smartwatches for children and found pre-installed downloaders, weak passwords, and unencrypted data transmissions.


The analysis demonstrates that most of these devices arbitrarily collect and periodically transmit sensitive data to remote servers without the user knowing about it.


This finding is worrisome as these devices quickly grow in popularity, with parents purchasing them to monitor their children's location and activities.


The research was conducted by the Dr. Web antivirus team, which looked into Elari Kidphone 4G, Wokka Lokka Q50, Elari FixiTime Lite, and Smart Baby Watch Q19.


These are all Android-based smartwatches that are very popular in Russia, and their prices cover a wide range of costs.


The most troublesome wearable
-----------------------------


Dr.Web found that the Elari Kidphone 4G smartwatch has three hidden modules that transmit data to a central location and receive remote commands.


By default, this communication occurs every eight hours, but this can be easily adjusted to a different interval.


The transmitted information includes SIM card info, geolocation data, device info, phonebook contacts, installed apps list, SMS count, and phone calls history.


Dr. Web is concerned that these hidden modules in the Elari Kidphone 4G can be used to install malicious apps, download, install, run, or uninstall apps, and also display ads, all without the owners knowing about it.


"Thus, Android.DownLoader.3894 hidden in this watch can be used for cyber espionage, displaying ads, and installing unwanted or even malicious apps," Dr. Web states in [their research](http://news.drweb.com/show/?i=14350&lng=en).



![The Elari Kidphone 4G](https://www.bleepstatic.com/images/news/u/1220909/Website%20snaps/elari.jpg)**The Elari Kidphone 4G**  
*Source: Elari*
Going cheap
-----------


The most inexpensive choice is the Wokka Lokka Q50, which costs around $15 and is quite popular as an almost disposable item.


However, the researchers discovered that the watch has a weak default password ('123456'), and all data transmitted between it and the Russia-based server is unencrypted.


This makes man-in-the-middle attacks very simple to carry out, enabling threat actors to request GPS location via SMS, listen to the wearer's surroundings remotely, or even change the C&C server address to one under their complete control.



![Retrieving info from Wokka Lokka via SMS](https://www.bleepstatic.com/images/news/u/1220909/Security/wokkalokka.jpg)**Retrieving info from Wokka Lokka via SMS**  
*Source: Dr. Web*
Mediocre cases
--------------


In the case of the Elari FixiTime Lite ($50) and the Smart Baby Watch Q19 ($25), the situation is mixed.


Elari FixiTime Lite transmits sensitive data such as GPS coordinates, voicemails, and photos using the unencrypted (HTTP) data transfer protocol. This unencrypted protocol enables man-in-the-middle (MiTM) attacks that allow attackers to listen in on transmitted data.



![Elari Fixitime hex data (GPS, WiFi) sent to C2](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Elari Fixitime hex data (GPS, WiFi) sent to C2**  
*Source: Dr. Web*
While the Smart Baby Watch Q19 uses a weak default password ('123456'), Dr. Web says the commands that can be used are significantly reduced, making it not much of a risk.


Parents should be cautious when buying a cheap smartwatch for their children due to the inherent risks of Internet-connected gadgets, especially when it allows tracking a child's location.


Bleeping Computer has contacted Elari and Wokka Lokka to comment on the above, but we have not heard back yet.




#### Tags:
[[Elari]] [[Dr.]] [[Kidphone]] [[Wokka]] [[Lokka]] [[FixiTime]] [[Bleeping Computer]]
