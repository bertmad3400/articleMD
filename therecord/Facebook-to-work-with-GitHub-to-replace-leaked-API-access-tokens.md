# Facebook to work with GitHub to replace leaked API access tokens
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/facebook-to-work-with-github-to-replace-leaked-api-access-tokens/)
+ Date: November 9, 2021
+ Author: Catalin Cimpanu


## Article:
![Facebook to work with GitHub to replace leaked API access tokens](https://therecord.media/wp-content/uploads/2021/05/Facebook-e1626363450106.png)

The Meta security team announced today an official partnership with GitHub through which the two teams will work together to invalidate Facebook API access tokens that have accidentally been uploaded and leaked inside GitHub repositories.


The partnership is part [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning), a GitHub security feature that scans all new code uploaded on the GitHub platforms for strings that look like passwords and access tokens.


If these strings match a known format, GitHub alerts the project owner about the accidental exposure.


Formally launched in March this year, GitHub added support for detecting Facebook API tokens a month later, in April 2021.


But today, Meta ([Facebook’s new corporate name](https://about.fb.com/news/2021/10/facebook-company-is-now-meta/)) said it officially partnered with GitHub, and the two companies will work together going forward.


The change is that instead of notifying the user about the Facebook access token leak, GitHub will now also send details about exposed tokens to Meta as well.


“Access tokens with a valid session will be **automatically invalidated**,” a Meta spokesperson said today. “When an access token is invalidated, the app admin will be notified via the Developer Dashboard.”


The partnership comes to help developers as this prevents situations where the exposed token is spotted by a malicious party before the real owner.


Exposed Facebook tokens are a very sensitive matter for Meta, as they can be used to silently harvest Facebook data, extract personal information from a developer’s third-party Facebook app or game, or just send spam and malicious files to regular Facebook users.





#### Tags:
[[GitHub]] [[Facebook]] [[The Record]]
