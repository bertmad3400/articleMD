# Study reveals Android phones constantly snoop on their users
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/study-reveals-android-phones-constantly-snoop-on-their-users/)
+ Date: October 12, 2021
+ Author: Bill Toulas


## Article:
![android](https://www.bleepstatic.com/content/hl-images/2021/10/01/Android__malware.jpg?rand=388483888)


A new study by a team of university researchers in the UK has unveiled a host of privacy issues that arise from using Android smartphones.


The researchers have focused on Samsung, Xiaomi, Realme, and Huawei Android devices, and LineageOS and /e/OS, two forks of Android that aim to offer long-term support and a de-Googled experience


The conclusion of the study is worrying for the vast majority of Android users .



> 
> With the notable exception of /e/OS, even when minimally configured and the handset is idle these vendor-customized Android variants transmit substantial amounts of information to the OS developer and also to third parties (Google, Microsoft, LinkedIn, Facebook, etc.) that have pre-installed system apps. - Researchers.
> 
> 
> 


As the summary table indicates, sensitive user data like persistent identifiers, app usage details, and telemetry information are not only shared with the device vendors, but also go to various third parties, such as Microsoft, LinkedIn, and Facebook.



![Summary of collected data](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/data%20collection%20summary.jpg)**Summary of collected data**  

Source: Trinity College Dublin
And to make matters worse, Google appears at the receiving end of all collected data almost across the entire table.


No way to "turn it off"
-----------------------


It is important to note that this concerns the collection of data for which there’s no option to opt-out, so Android users are powerless against this type of telemetry.


This is particularly concerning when smartphone vendors include third-party apps that are silently collecting data even if they’re not used by the device owner, and which cannot be uninstalled.


For some of the built-in system apps like miui.analytics (Xiaomi), Heytap (Realme), and Hicloud (Huawei), the researchers found that the encrypted data can sometimes be decoded, putting the data at risk to man-in-the-middle (MitM) attacks.



![Volume of data (KB/h) transmitted by each vendor](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/volume%20of%20data(1).jpg)**Volume of data (KB/h) transmitted by each vendor**  

Source: Trinity College Dublin
As [the study](https://www.scss.tcd.ie/Doug.Leith/Android_privacy_report.pdf) points out, even if the user resets the advertising identifiers for their Google Account on Android, the data-collection system can trivially re-link the new ID back to the same device and append it to the original tracking history..


The deanonymisation of users takes place using various methods, such as looking at the SIM, IMEI, location data history, IP address, network SSID, or a combination of these.



![Potential cross-linking data collection points](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Potential cross-linking data collection points**  

Source: Trinity College Dublin
Privacy-conscious Android forks like /e/OS are getting more traction as increasing numbers of users realize that they have no means to disable the unwanted functionality in vanilla Android and seek more privacy on their devices.


However, the majority of Android users remain locked into never ending stream of data collection, which is where regulators and consumer protection organizations need to step in and to put an end to this.


BleepingComputer has contacted Google for a statement regarding this study but has not heard back at this time.




#### Tags:
[[Android]] [[Source:]] [[Google]] [[Bleeping Computer]]
