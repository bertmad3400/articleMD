# Multiple Vulnerabilities Found In Microsoft Teams – Only One Fixed Yet
### The vulnerabilities affected Microsoft Teams link preview feature. Microsoft only patched an Android app flaw, denying fixes for the rest.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2021/12/23/multiple-vulnerabilities-found-in-microsoft-teams-only-one-fixed-so-far/
+ Date: 2021-12-23
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2020/04/Microsoft-Teams-scaled.jpg)
 Researchers have discovered at least four different vulnerabilities in the Microsoft Teams link preview feature. However, Microsoft has patched only one of these bugs so far, delaying or denying the patches for the rest.

 Microsoft Teams Vulnerabilities Found
-------------------------------------

 Sharing the details in a recent [blog post](https://positive.security/blog/ms-teams-1-feature-4-vulns), Positive Security has highlighted the four Microsoft Teams vulnerabilities risking users’ privacy.

 Briefly, the first of these vulnerabilities include an SSRF flaw affecting the `/urlp/v1/url/info` endpoint. Exploiting this bug could allow internal post scanning and HTTP-based exploits. As stated in the post,

 The second was a URL spoofing flaw that could let an adversary send malicious links to the target user while impersonating legit URLs. This flaw potentially contributes to phishing attacks.

 The third security bug affected the Microsoft Teams Android app, exploiting which could reveal IP addresses. Regarding this vulnerability, the researchers explained,

 
> When creating a link preview, the backend fetches the referenced preview thumbnail and makes it available from a Microsoft domain. This ensures that the IP address and user agent data is not leaked when the receiving client loads the thumbnail. However, by intercepting the sending of the message, it’s possible to point the thumbnail URL to a non-Microsoft domain. The Android client does not check the domain/does not have a CSP restricting the allowed domains and loads the thumbnail image from any domain.
> 
> 

 Then, the last bug also affected Microsoft Teams Android app leading to a denial of service. It only required an adversary to send a link with an invalid preview to the target user. Clicking on this link would crash the app.

 Microsoft Patched Only One Bug
------------------------------

 The researchers reported these vulnerabilities to Microsoft in March 2021. However, from all the four bugs, Microsoft only patched the Android app’s IP leak flaw, denying the patches for the rest.

 Specifically, Microsoft only expressed the possibility of fixing the DoS flaw “in a future version”. Whereas, for the other two bugs, the tech giant simply denied working on them due to their potentially limited exploitability and low risk.

 It means that [Microsoft Teams](https://latesthackingnews.com/tag/microsoft-teams/) users should now remain very careful while opening any web links. Particularly, they need to remain wary of any links received from unsolicited users to avoid any risks.

 Let us know your thoughts in the comments.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Reg]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Microsoft]] [[Teams]] [[Android]] [[Ip]] [[Latest Hacking News]]

