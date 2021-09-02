# WhatsApp Photo Filter Bug Allows Sensitive Info to Be Lifted
### Users should be careful whose pics they view and should, of course, update their apps.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=169141)
+ Date: September 2, 2021  8:28 am
+ Author: Tara Seals


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2020/02/05114803/whatsapp-1357489_1920-e1580921300765.jpg)
A security vulnerability in WhatsApp’s pic-retouching function could allow an attacker to read sensitive information from the WhatsApp memory, researchers said – so users should be careful whose pics they view and should, of course, update their apps.


Disclosed by Check Point Research (CPR), the issue can be exploited by applying specific image filters to a specially crafted image (i.e., a malformed .GIF file) and sending it to a target. Image filters are of course the built-in visual-effects tools in WhatsApp used to change the color, saturation, tone, sharpness and more of a photo taken.


The bug ([CVE-2020-1910](https://nvd.nist.gov/vuln/detail/CVE-2020-1910)) carries a 7.8 out of 10 rating on the CVSS vulnerability-severity scale. It’s due to a memory-corruption error, the firm said – and more specifically a heap-based, out-of-bounds read-and-write issue. Typically, this kind of vulnerability can allow attackers to read sensitive information from other memory locations or cause a crash.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


“CPR learned that switching between various filters on crafted .GIF files indeed caused WhatsApp to crash,” according to a [Thursday report](https://research.checkpoint.com/2021/now-patched-vulnerability-in-whatsapp-could-have-led-to-data-exposure-of-users/).


“What’s important about this issue is that given a very unique and complicated set of circumstances, it could have potentially led to the exposure of sensitive information from the WhatsApp application,” according to CPR’s writeup.


**CVE-2020-1910 Under the Hood**
--------------------------------


The vulnerability exists in a native function called “applyFilterIntoBuffer()” in the libwhatsapp.so library, according to CPR. This function is able to input three different AndroidBitmap objects:


The function thus essentially looks at the source image pixels, calculates new pixel values by applying the filter, then copies those values into the destination buffer.


To do so, it first calls to a function called “AndroidBitmap\_getInfo” to get data about the source and filter image, which results in a structure called “AndroidBitmapInfo”. That structure contains data about image parameters, including width, height, stride (number of bytes per row), format and flags.


Each time this action is performed, both the source and destination buffers advance by the value of the image height parameter multiplied times four, which represents the column size in bytes, according to CPR.


“The problem is that both destination and source images are assumed to have the same dimensions and also the same-format RGBA [color value] (meaning each pixel is stored as four bytes, hence the multiplication by four),” according to the researchers. “However, there are no checks performed on the format of the source and destination images.”


Thus, it’s possible to create a maliciously crafted source image that has only one byte per pixel, which will make the vulnerable applyFilterIntoBuffer() function attempt to read and copy four times the amount of the allocated source image buffer, which leads to an out-of-bounds memory access, CPR concluded.


“This is the crash we got…caused by the program trying to read from an unmapped memory region,” researchers explained.


CPR didn’t provide many details on what a real-world exploit might look like, or what information could be lifted by an earnest attacker, beyond a spokesperson noting that “the scenario for exploitation is a bit complex and requires extensive user interaction to execute.” Threatpost has asked for more details on that front.


The attack surface for such attacks could be potentially massive: “With over two billion active users, WhatsApp can be an [attractive target](https://threatpost.com/whatsapp-discloses-6-bugs-dedicated-security-site/158962/) for attackers,” Oded Vanunu, head of products vulnerabilities research at Check Point, said in a statement, noting that an estimated 55 billion messages, 4.5 billion photos and 1 billion videos are shared every day on the messaging platform.


**Apply the WhatsApp Update**
-----------------------------


WhatsApp deployed a fix in version 2.21.2.13, so users should make sure their apps are updated. The fixed function has two new checks on the source image and filter image, according to CPR:


“People should have no doubt that end-to-end encryption continues to work as intended and people’s messages remain safe and secure,” WhatsApp said in a statement. “This report involves multiple steps a user would have needed to take and we have no reason to believe users would have been impacted by this bug. That said, even the most complex scenarios researchers identify can help increase security for users. As with any tech product, we recommend that users keep their apps and operating systems up to date, to download updates whenever they’re available, to report suspicious messages, and to reach out to us if they experience issues using WhatsApp.”


***Check out our free***[***upcoming live and on-demand webinar events***](https://threatpost.com/category/webinars/) ***– unique, dynamic discussions with cybersecurity experts and the Threatpost community.***





#### Tags:
[[WhatsApp]] [[ThreatPost]]
