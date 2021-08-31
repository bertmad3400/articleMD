# This phishing attack is using a sneaky trick to steal your passwords, warns Microsoft
### Hovering over a link in an email isn't going to be enough to check if it's going to take you to a dangerous site.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-phishing-attack-is-using-a-sneaky-trick-to-steal-your-passwords-warns-microsoft/)
+ Date: August 31, 2021 -- 10:15 GMT (11:15 BST)
+ Author: Liam Tung


## Article:
Unknown

Microsoft has warned Office 365 customers that they're being targeted by a widespread phishing campaign aimed at nabbing usernames and passwords. 

The ongoing phishing campaign is using multiple links; clicking on them results in a series of redirections that lead victims to a Google [reCAPTCHA](https://developers.google.com/recaptcha/docs/versions) page that leads to a bogus login page where Office 365 credentials are stolen.  


This particular attack relies on the email sales and marketing tool called '[open redirects](https://cwe.mitre.org/data/definitions/601.html)', which has been [abused in the past](https://nakedsecurity.sophos.com/2020/05/15/how-scammers-abuse-google-searchs-open-redirect-feature/) to redirect a visitor to a trustworthy destination to a malicious site. Google [doesn't rate open redirects for Google URLs as a security vulnerability](https://sites.google.com/site/bughunteruniversity/nonvuln/open-redirect), but it does display a 'redirect notice' in the browser. 

**SEE:** [**Ransomware: This new free tool lets you test if your cybersecurity is strong enough to stop an attack**](https://www.zdnet.com/article/ransomware-this-new-free-tool-lets-you-test-if-your-cybersecurity-is-strong-enough-to-stop-an-attack/)

Microsoft warns this feature is being used by the phishing attackers. 

"However, attackers could abuse open redirects to link to a URL in a trusted domain and embed the eventual final malicious URL as a parameter. Such abuse may prevent users and security solutions from quickly recognizing possible malicious intent," [the Microsoft 365 Defender Threat Intelligence Team warns](https://www.microsoft.com/security/blog/2021/08/26/widespread-credential-phishing-campaign-abuses-open-redirector-links/). 

This attack's trick relies on the advice for users to hover over a link in an email to check the destination before clicking.






"Once recipients hover their cursor over the link or button in the email, they are shown the full URL. However, since the actors set up open redirect links using a legitimate service, users see a legitimate domain name that is likely associated with a company they know and trust. We believe that attackers abuse this open and reputable platform to attempt evading detection while redirecting potential victims to phishing sites," Microsoft warns. 

"Users trained to hover on links and inspect for malicious artifacts in emails may still see a domain they trust and thus click it," it said. 

Microsoft has found over 350 unique phishing domains used in this campaign, including free email domains, compromised domains, and domains automatically created by the attacker's domain generation algorithm. The email subject headers were tailored to the tool the attacker was impersonating, such as a calendar alert for a Zoom meeting, an Office 365 spam notification, or a notice about the widely used but [ill-advised password expiry policy](https://www.zdnet.com/article/want-a-strong-password-youre-probably-still-doing-it-the-wrong-way/). 

While open redirects aren't new, Microsoft hopped on the issue after noticing a phishing campaign in August that relied on spoofed Microsoft URLs. 


The Google reCaptcha verification adds to the apparent legitimacy of the site since it is generally used by websites to confirm the user is not a bot. However, in this case, the user has been redirected to a page that looks like a class Microsoft login page and eventually leads to a legitimate page from Sophos, which does provide a service to detect this style of phishing attack.  

**SEE:** [**The Privacy Paradox: How can businesses use personal data while also protecting user privacy?**](https://www.zdnet.com/video/the-privacy-paradox-how-can-businesses-use-personal-data-while-also-protecting-user-privacy/)

"If the user enters their password, the page refreshes and displays an error message stating that the page timed out or the password was incorrect and that they must enter their password again. This is likely done to get the user to enter their password twice, allowing attackers to ensure they obtain the correct password.

"Once the user enters their password a second time, the page directs to a legitimate Sophos website that claims the email message has been released. This adds another layer of false legitimacy to the phishing campaign."

Google's [word on the matter of open redirects](https://sites.google.com/site/bughunteruniversity/nonvuln/open-redirect) is that this is not a security vulnerability, though it admits it can be used to trigger other vulnerabilities. However, Google disputes the idea that hovering over a link in an app to see a destination URL is a useful phishing awareness tip. 

"Open redirectors take you from a Google URL to another website chosen by whoever constructed the link. Some members of the security community argue that the redirectors aid phishing, because users may be inclined to trust the mouse hover tooltip on a link and then fail to examine the address bar once the navigation takes place.

"Our take on this is that tooltips are not a reliable security indicator, and can be tampered with in many ways; so, we invest in technologies to detect and alert users about phishing and abuse, but we generally hold that a small number of properly monitored redirectors offers fairly clear benefits and poses very little practical risk."





#### Tags:
[[phishing]] [[Microsoft]] [[Google]] [[URL]] [[However,]] [[redirectors]] [[ZDNet]]
