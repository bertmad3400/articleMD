# Tor Browser 11 removes V2 Onion URL support, adds new UI
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/software/tor-browser-11-removes-v2-onion-url-support-adds-new-ui/)
+ Date: November 9, 2021
+ Author: Lawrence Abrams


## Article:
![Tor Browser](https://www.bleepstatic.com/content/hl-images/2020/08/19/Tor.png)


The Tor Project has released Tor Browser 11.0  with a new user interface design and the removal of support for V2 onion services.


The Tor Browser is a customized version of Firefox ESR that allows users to browse the web anonymously and access special .onion domains only accessible via Tor.


You can download the Tor Browser from the [Tor Project site](https://www.torproject.org/), and if you are an existing user, you can upgrade to the latest version by going to the **Tor Menu** > **Help** > **About Tor Browser**.



![Tor Browser 11.0](https://www.bleepstatic.com/images/news/software/t/tor/version-11/tor-version-11.jpg)**Tor Browser 11.0**
What's new in Tor 11
--------------------


Tor Browser 11 uses Firefox ESR 91, which brings an updated user interface containing new icons, a new toolbar, streamlined menus, dialogs, and an updated tabs interface.



![New Tor 11 icons](https://www.bleepstatic.com/images/news/software/t/tor/version-11/new-tor-11-icons.jpg)**New Tor 11 icons**  
*Source: Tor Project*
However, the most significant change is the deprecation of V2 onion services, meaning TOR URLs using short 16 character hostnames domains are no longer supported.


When attempting to open a V2 onion service, Tor Browser will show users an "Invalid Onionsite Address" with an error code of 0xF6.



![V2 Onion services are no longer supported](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**V2 Onion services are no longer supported**
"Last year we announced that [v2 onion services would be deprecated in late 2021](https://blog.torproject.org/v2-deprecation-timeline), and since its [10.5 release](https://blog.torproject.org/new-release-tor-browser-105) Tor Browser has been busy warning users who visit v2 onion sites of their upcoming retirement," the Tor Project explained in the [Tor Browser 11 release notes](http://blog.torproject.org/new-release-tor-browser-11-0).


"At long last, that day has finally come. Since updating to Tor 0.4.6.8 v2 onion services are no longer reachable in Tor Browser, and users will receive an “Invalid Onion Site Address” error instead."


With this change, Tor sites using V2 onion services will no longer be reachable, but admins can upgrade to a V3 onion service by adding the following lines to the **torrc** file.


As with all releases, there are always known issues and bugs that users need to be aware.


The known issues in Tor 11 are listed below:


* [Bug 40668](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40668): DocumentFreezer & file scheme
* [Bug 40671](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40671): Fonts don't render
* [Bug 40679](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40679): Missing features on first-time launch in esr91 on MacOS
* [Bug 40689](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40689): Change Blockchair Search provider's HTTP method
* [Bug 40667](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40667): AV1 videos shows as corrupt files in Windows 8.1
* [Bug 40677](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40677): Since the update to 11.0a9 some addons are inactive and need disabling-reenabling on each start
* [Bug 40666](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40666): Switching svg.disable affects NoScript settings
* [Bug 40690](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/40690): Browser chrome breaks when private browsing mode is turned off


You can download Tor 11.0 from the [Tor Browser download page](https://www.torproject.org/download/) and the [distribution directory](https://dist.torproject.org/torbrowser/11.0/).




#### Tags:
[[V2]] [[v2]] [[Bleeping Computer]]
