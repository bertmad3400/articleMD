# Google pauses quantum security feature in Chrome because of buggy middleware
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/google-pauses-quantum-security-feature-in-chrome-because-of-buggy-middleware/)
+ Date: September 1, 2021
+ Author: Catalin Cimpanu


## Article:
![Google pauses quantum security feature in Chrome because of buggy middleware](https://therecord.media/wp-content/uploads/2021/09/quantum-cryptography.jpg)

Google said on Tuesday that it temporarily disabled its quantum computer-resistant security feature in Chrome after it received bug reports that faulty networking middleware devices have been causing unexpected website connection failures for the few users where this feature was enabled.


Known as **Combined Elliptic-Curve and Post-Quantum 2**, or [CECPQ2](https://www.chromium.org/cecpq2), the idea behind this feature was to improve the cryptography around TLS connections so when quantum computers would be widely available in the near future, threat actors wouldn’t be able to decrypt historical HTTPS traffic and access past secure communications.


First [developed in 2016](https://security.googleblog.com/2016/07/experimenting-with-post-quantum.html), together with Cloudflare engineers, CECPQ2 was enabled in Chrome 91 released in May this year, where it activated itself for all domains that started with the letter “A,” so Google engineers could test its behavior while they still worked out the kinks.


Under the hood, the feature functioned by adding [an isogeny-based key agreement](https://blog.cloudflare.com/the-tls-post-quantum-experiment/) to Chrome’s TLS negotiation component in order to harden an encrypted HTTPS connection.


The bug occurred because **CECPQ2 created larger TLS packets**.


Google said on Tuesday that some middleware devices couldn’t handle these packets, resulting in unexpected connection failures or timeouts.


With the release of Chrome 93 yesterday, the browser vendor said it was temporarily disabling CECPQ2 for all users in order to work with middleware vendors and release patches for the affected devices.


Google said the CECPQ2 will remain disabled for the Chrome 93 and 94 release cycles but wouldn’t commit to re-enabling it in Chrome 95 just yet.


Users who would still like to use CECPQ2 can manually re-enable the feature right now, and for all domains, by toggling the following Chrome flag to “Enabled.”


**chrome://flags/#post-quantum-cecpq2**


According to a document [[PDF](https://media.defense.gov/2021/Aug/04/2002821837/-1/-1/1/Quantum_FAQs_20210804.PDF)] published last month, the US National Security Agency said it wasn’t aware of any quantum computer capable of breaking current encryption algorithms.





#### Tags:
[[CECPQ2]] [[Google]] [[middleware]] [[TLS]] [[The Record]]
