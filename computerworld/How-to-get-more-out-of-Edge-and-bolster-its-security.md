# How to get more out of Edge (and bolster its security)
### By tweaking a few important settings in Microsoft's browser, you can ensure your online surfing is more secure.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3642833/how-to-get-more-out-of-edge-and-bolster-its-security.html
+ Date: 2021-11-29
+ Author: Susan Bradley


## Article:
![Article Image](https://images.idgesg.net/images/idge/imported/imageapi/2021/11/26/20/keyboard_laptop_microsoft-edge-logo_web-browser_by-urupong-getty-images-1200x800-100816809-large-100912436-large.jpg?auto=webp&quality=85,70)

I use Edge, the built-in browser in Windows, though I’m very much in the minority. I even think it has the potential to be a better browser than Firefox or Chrome. Case in point: the recent “Super Duper Secure Mode” that has rolled out to the default Edge version after being in beta channels for several weeks. (Let’s call it the “SDSM” setting.)

As noted in a [past Edge blog post](https://microsoftedge.github.io/edgevr/posts/Super-Duper-Secure-Mode/), SDSM provides additional security features that allows you to disable just-in-time Javascript and then enable Controlflow-Enforcement Technology (CET) instead. Just-in-time Javascript has been used in many zero-day browser attacks in the past — thus, blocking it will help protect our systems and platforms going forward. In my testing so far, I have not seen any side effects running Edge in this mode, even when doing online shopping or banking.

Do you want your security balanced or strict?
---------------------------------------------

If you use Edge, or are considering using it, I recommend that you try the following settings:

Launch Edge and click on the three dots to go into the settings menu. In the search settings box, type in **Security**. Now, scroll to the section called “Enable Security mitigations for a more secure browser experience.” Click on *Balanced*, which adds security protection for sites you don’t visit often. You can even go one more level and click on *Strict*, which boosts security for *all* sites. (If you have issues with any site, you can click on *Exceptions* and add websites you want to exclude from this setting.)

[![secure edge](https://images.idgesg.net/images/article/2021/11/secureedge-100912545-large.jpg?auto=webp&quality=85,70)](https://images.idgesg.net/images/article/2021/11/secureedge-100912545-orig.jpg?auto=webp&quality=85,70 "<div class='credit'>Microsoft</div>
<p>Users can choose varying levels of security in Edge.</p>
")
While you’re there, review the setting for “Blocking potentially unwanted applications.” This blocks downloads of low-reputation apps that might cause unexpected behaviors. Especially if you download from various websites, this helps block any apps that could be malicious.

While I love the SDSM mode in Edge, I’m not a fan of some of the other settings included in the Edge browser beta testing process. One add-on, in particular, I hope Microsoft drops — or, at a minimum, allows me to block — is the “Buy now, pay later” setting. It lets online shoppers break up purchase payments into equal installments, often interest-free, so they get the item up front, instead of having to wait until it’s paid in full.

The setting opens with third-party payer Zip (previously known as Quadpay) for any purchase between $35 and $1,000. As Consumer Reports [noted earlier this year](https://www.consumerreports.org/shopping-retail/hidden-risks-of-buy-now-pay-later-plans-a7495893275/), these spread-out spending plans cause challenges for purchasers, ranging from cash management to problems obtaining refunds if you have a problem. You can tell from the six pages of feedback that there are other Edge users who are seriously disappointed in Microsoft about this setting and want it to reconsider offering this option.

…And if you’ve set another browser as your default
--------------------------------------------------

You’ve probably read recently that Edge in a recent Insider Preview of Windows 11 is [blocking programs such as EdgeDeflector](https://www.computerworld.com/article/3640622/latest-windows-11-build-looks-to-force-edge-use-by-thwarting-browser-workarounds.html), which was designed to help a user change default browsers on their. As noted in a [statement to The Verge](https://www.theverge.com/2021/11/15/22782802/microsoft-block-edgedeflector-windows-11), Microsoft is blocking the developers of EdgeDeflector from changing the search that’s integrated with the search box on Windows 11. (Windows 11 doesn’t just have default settings for https: it also has a specific protocol of Microsoft Edge.)

I can understand — to a point — the need to ensure that the Microsoft-Edge protocol is limited to purely Edge processes. But in not explaining why the end-to-end security or encryption the new protocol provides, Microsoft is not making its case well and is looking a bit like a bully. Rather than being so heavy handed, it needs to provide more settings like SDDM to allow users to choose a more secure browser.

Additional Edge settings to consider
------------------------------------

There are other ways to make Edge better: go to *Settings*, then to *Privacy, search and services*. Review the tracking prevention you have set. (I set mine to strict, which blocks a majority of trackers from all sites.) You can click the button for *Blocked trackers* to see how many times you’ve been protected from tracking. It’s interesting to see companies that I don’t even do business with track me.

You should also review whether you want sites to check on whether you have payments methods saved. (I don’t recommend saving passwords or payment methods in any browser; it’s wiser to manually enter your payment methods.)

I also recommend disabling the setting that allows your web experience to be customized by using your browsing history for personalizing advertising, search, news, and other Microsoft services. As [acknowledged by Microsoft](https://support.microsoft.com/en-us/microsoft-edge/microsoft-edge-browsing-activity-for-personalized-advertising-and-experiences-37aa831e-6372-238e-f33f-7cd3f0e53679), once you disable this setting, the company will no longer collect and use your browsing activity for personalization of advertising or experiences.

Another setting I suggest turning off is one Edge introduced last year. Scroll down to Services, and disable *Save time and money with Shopping in Microsoft Edge*. I find the coupon offers not only annoying, but many times they’re out of date and don’t work. (I also disable travel recommendations.) Finally, you can decide which search engine you which to have as your default.

For businesses, using group policy to control and manage Edge policies makes it easier to control and protect fusers rom malicious sites. One setting in particular, [Blocking extensions based on their permissions](https://docs.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-policies), allows IT admins to control which extensions get installed. Open the group policy management editor and go to *Administrative Templates > Microsoft Edge > Extensions* and then select *Configure extension management settings*.

Though these changes will help make Edge more secure, my message to Microsoft is to keep working. Make Edge the best and most secure browser available, because that’s the feature we need most.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Finance]] [[victim.industry.name=Finance]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Windows]] [[(i]] [[Computerworld]]

