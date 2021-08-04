# Bob had a bad night: IoT mischief in a capsule hotel takes neighborly revenge to the next level
### When you hand over control of capsule bedrooms to guests, you also offer them the means to troll others.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/bob-had-a-bad-night-iot-mischief-takes-neighbourly-revenge-to-the-next-level-in-a-capsule-hotel/)
+ Date: August 4, 2021 -- 18:52 GMT (19:52 BST)
+ Author: Charlie Osborne


## Article:
Unknown

**BLACK HAT USA**: Researchers have revealed how security vulnerabilities could be exploited to compromise hotel Internet of Things (IoT) devices -- and take revenge on loud neighbors. 


IoT devices are now commonplace both in businesses and in the home. These internet and often Bluetooth-connected products range from [security cameras](https://www.zdnet.com/article/best-security-camera/) to [smart lighting](https://www.zdnet.com/article/best-home-office-lighting/); fridges that monitor your foodstuffs, [pet trackers](https://www.zdnet.com/article/best-gadgets-for-dogs/), intelligent thermostats -- and in the hospitality space, IoT is also employed to give guests more control over their stay. 

These services are sometimes offered through dedicated apps and tablets, allowing the management of lights, heaters, air conditioning, televisions, and more. 

However, the moment you network IoT and hand over control to third parties, you may also give individuals the keys to a digital kingdom -- and the ability to cause mischief, or worse. 

Vulnerabilities in IoT devices vary. They can range from hardcoded, weak credentials to bugs that allow local attackers to hijack devices; remote code execution (RCE) flaws, information-leaking interfaces, and to a lack of security and firmware updates -- the latter of which is a frequent problem in legacy and early IoT products. 

Speaking at Black Hat USA, Las Vegas, security consultant Kya Supa from LEXFO explained how a chain of security weaknesses were combined and exploited to gain control of rooms at a capsule hotel, a budget-friendly type of hotel offering extremely small -- and, therefore, cozy -- spaces to guests, who are stacked side-by-side.

Supa was traveling and checked in to a capsule hotel abroad. When they arrived, guests were issued an iPod Touch. The capsules contained a bed and curtain for privacy, as well as a ventilation fan. The technology in use included NFC cards for each floor, the option to mirror a device screen on the curtain, and on the iPod Touch, guests could control the lights, ventilation fan, and change the position of the adjustable bed via an app.






The app was connected via either Bluetooth or Wi-Fi. 

A neighbor, "Bob," kept waking Supa up by making loud phone calls in the early hours of the morning. While Bob had agreed to keep it down, he did not keep his promise -- and the researcher set to work since he needed his sleep, especially during his vacation. 

The first thing Supa did was to explore his room, finding an emergency light installed for safety reasons; a Nasnos automaton center for use in controlling products in case the iPod Touch was lost; an electric motor used to manage the incline of the capsule's bed; and a Nasnos router, hidden in the wall. 

If you connected to the router via a smartphone, it was then possible to control other devices on the network, and this was the setup the hotel chose to use.

It was not possible to exit the app or turn off the iPod Touch, and Apple's Gateway software was in use to stop the device from being tampered with, and so a passcode was required for any other action. 

To circumvent these protections, Supa was able to drain the battery and then explore the iPod Touch's settings. He found that two networks were connected -- the hotel Wi-Fi and the router. 

To retrieve the router key, Supa targeted WEP, a protocol that has been known to be weak for years. Access points, each being one of the bedrooms, were found. Supa inspected the traffic and found weak credentials in place -- "123" -- and you can guess the rest. 

By using an Android smartphone, the iPod Touch, and a laptop, the researcher created a Man-in-The-Middle (MiTM) architecture and inspected the network traffic. No encryption was found and he created a simple program to tamper with these connections, allowing the researcher to seize control of his bedroom through his laptop. 

Now, it was to be determined if the key would be applicable for the other bedrooms. Supa downloaded a Nasnos router app and reverse-engineered the software to see how the Wi-Fi key was generated, and while this investigation failed, he was able to find that packets were sent via UDP port 968, and a lack of authentication meant he was still able to secure Wi-Fi keys. 

Only four digits in each key appeared to be generated differently, confirmed via a dictionary attack, and so a quick exploit program later, Supa had control of each bedroom's smart features. 

![screenshot-2021-08-04-at-19-42-30.png]()![screenshot-2021-08-04-at-19-42-30.png](https://www.zdnet.com/a/hub/i/r/2021/08/04/a0e11a19-1fe9-46e7-9cbf-97b6cf35e783/resize/1200xauto/3ef86802fd0ea5eb3bfc70f53387ff82/screenshot-2021-08-04-at-19-42-30.png)
 Kya Supa
 Now that he could "control every bedroom," and Bob was still there, Supa then tampered with the lights of different bedrooms until he found the right one. 

He created a script that, every two hours, would change the bed into a sofa and turn the lights on and off. 

The script was launched at midnight. We can probably assume Bob did not enjoy his stay.

"I hope he will be more respectful in the future," Supa commented. 

While this case is amusing -- although, not for Bob -- it does also highlight how a single access point can be used to tamper with and hijack IoT devices: and this goes for the home, too. While intelligent technology can be convenient, we need to be aware of the potential security ramifications, too.

The hotel and Nasnos were both contacted afterward, and the hotel has since improved its security posture. 

###  Previous and related coverage

* [$49 malware receives major upgrade to strike both Windows and macOS PCs](https://www.zdnet.com/article/49-malware-receives-major-upgrade-to-strike-windows-and-mac-pcs/)  

* [Malware developers turn to 'exotic' programming languages to thwart researchers](https://www.zdnet.com/article/malware-developers-turn-to-exotic-programming-languages-to-thwart-researchers/)  

* [These new vulnerabilities put millions of IoT devices at risk, so patch now](https://www.zdnet.com/article/these-new-vulnerabilities-millions-of-iot-devives-at-risk-so-patch-now/)  




---

**Have a tip?** Get in touch securely via WhatsApp | Signal at +447713 025 499, or over at Keybase: charlie0



---





#### Tags:
[[IoT]] [[iPod]] [[Nasnos]] [[Touch,]] [[Wi-Fi]] [[ZDNet]]
