# Firefox 93 arrives with tab unloading, insecure download blocks and enforced referrer trim
### When Firefox is in low-memory situations on Windows, it will begin to unload tabs to prevent the browser crashing.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/firefox-93-arrives-with-tab-unloading-insecure-download-blocks-and-enforced-referrer-trim/)
+ Date: October 6, 2021
+ Author: Chris Duckett


## Article:
Unknown

![New Firefox logo](https://www.zdnet.com/a/img/resize/ed7f6d396378e40a0d451e5bd3a2f61b3dc2b7a6/2019/06/18/f9e39513-cfe9-4700-8730-4a6d4a0c3910/firefox-logo.png?fit=bounds&auto=webp)
 Image: Mozilla
 Version 93 of [Mozilla's Firefox browser](https://www.mozilla.org/en-US/firefox/new/) has arrived, and chief among its new features is tab unloading. 

Available at the moment only on Windows, with macOS and Linux to follow, the feature kicks in when the browser believes an out-of-memory crash is imminent, and it will unload tabs with the least recently used ones unloaded first. Tabs that are in the foreground are never unloaded with tabs that are pinned, using picture-in-picture, or playing sound are less likely to be unloaded. 

On Windows, the threshold is around the 6% mark, Mozilla engineer Haik Aftandilian wrote in a [blog post](https://hacks.mozilla.org/2021/10/tab-unloading-in-firefox-93/). 

"We have experimented with tab unloading on Windows in the past, but a problem we could not get past was that finding a balance between decreasing the browser's memory usage and annoying the user because there's a slight delay as the tab gets reloaded, is a rather difficult exercise, and we never got satisfactory results," Aftandilian said. 

"We have now approached the problem again by refining our low-memory detection and tab selection algorithm and narrowing the action to the case where we are sure we're providing a user benefit: if the browser is about to crash." 

A month of testing in Firefox's Nightly channel found a decrease in browser and content process-related crashes, but also an increase in out of memory crashes, as well as an increase in average memory usage. 

"The latter may seem very counter-intuitive, but is easily explained by survivorship bias ... browser sessions that had such high memory usage would have crashed and burned in the past, but are now able to survive by unloading tabs just before hitting the critical threshold," the engineer said.






"The increase in OOM crashes, also very counter-intuitive, is harder to explain. 

"We're working on improving our understanding of this problem and the relevant heuristics. But given the clearly improved outcomes for users, we felt there was no point in holding back the feature." 

In the next release of Firefox, an about:unloads page will be added to provide diagnostics on tab unloading. 

Also coming in Firefox 93 is functionality to block HTTP downloads from HTTPS pages, followed by showing a dialog to users warning it is a potential security risk and asking if they wish to continue as well as blocking downloads from sandboxed iframes, unless they have the allow-downloads attribute. 

The browser has also ended by default support for 3DES encryption but it will still be available when sites use deprecated TLS versions. 

"Recent measurements indicate that Firefox encounters servers that choose to use 3DES about as often as servers that use deprecated versions of TLS," Mozilla [said](https://blog.mozilla.org/security/2021/10/05/securing-connections-disabling-3des-in-firefox-93/). 

"As long as 3DES remains an option that Firefox provides, it poses a security and privacy risk. Because it is no longer necessary or prudent to use this encryption algorithm, it is disabled by default in Firefox 93." 

Firefox 93 is also packing the third version of its [SmartBlock technology](https://www.zdnet.com/article/firefox-87-launch-packed-with-private-browsing-smartblock/), which can replace Google Analytics, Optimizely, Criteo, Amazon TAM, and various Google advertising javascript with local versions that behave close enough like the originals to prevent sites from breaking. 

The browser is changing [its referrer policy](https://www.zdnet.com/article/mozilla-firefox-tweaks-referrer-policy-to-shore-up-user-privacy/) to ensure sites cannot overwrite the default trimming that Firefox applies to cross site URLs. Same site requests will continue to pass the full referring URL. 

### Related Coverage

* [Chinese cyberspies targeted Tibetans with a malicious Firefox add-on](/article/chinese-cyberspies-targeted-tibetans-with-a-malicious-firefox-add-on/)
* [Firefox 88 clamps down on window.name abuses by trackers](/article/firefox-88-clamps-down-on-window-name-abuses-by-trackers/)
* [Firefox to block Backspace key from working as "Back" button](/article/firefox-to-block-backspace-key-from-working-as-back-button/)
* [Firefox to ship 'network partitioning' as a new anti-tracking defense](/article/firefox-to-ship-network-partitioning-as-a-new-anti-tracking-defense/)





#### Tags:
[[Firefox]] [[Mozilla]] [["We]] [[said.]] [[crashes,]] [[3DES]] [[ZDNet]]
