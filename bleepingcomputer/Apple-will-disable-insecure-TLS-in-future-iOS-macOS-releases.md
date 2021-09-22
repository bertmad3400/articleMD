# Apple will disable insecure TLS in future iOS, macOS releases
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/apple/apple-will-disable-insecure-tls-in-future-ios-macos-releases/)
+ Date: September 22, 2021
+ Author: Sergiu Gatlan


## Article:
![Apple will disable insecure TLS in future iOS, macOS releases](https://www.bleepstatic.com/content/hl-images/2021/07/27/Apple.jpg)


Apple has deprecated the insecure Transport Layer Security (TLS) 1.0 and 1.1 protocols in recently launched iOS and macOS versions and plans to remove support in future releases altogether.


TLS is a secure communication protocol designed to protect users from eavesdropping, tampering, and message forgery while accessing and exchanging information over an Internet connection using client/server applications.


The original TLS 1.0 specification and its TLS 1.1 successor have been used for almost 20 years (with TLS 1.0 first defined [in 1999](https://datatracker.ietf.org/doc/html/rfc2246) and TLS 1.1 [in 2006](https://datatracker.ietf.org/doc/html/rfc4346)).


The Internet Engineering Task Force (IETF) [approved](https://www.bleepingcomputer.com/news/security/ietf-approves-tls-13-as-internet-standard/) [TLS 1.3](https://datatracker.ietf.org/doc/rfc8446/?include_text=1), the next major version of the TLS protocol, in March 2018, after four years of discussions and 28 protocol drafts.


TLS 1.0/1.1 deprecation update
------------------------------


"As part of ongoing efforts to modernize platforms, and to improve security and reliability, TLS 1.0 and 1.1 have been deprecated by the Internet Engineering Task Force (IETF) as of March 25, 2021," Apple [said](https://developer.apple.com/news/?id=bv8ur34d).


"These versions have been deprecated on Apple platforms as of iOS 15, iPadOS 15, macOS 12, watchOS 8, and tvOS 15, and support will be removed in future releases."


The company advised developers whose apps still use the legacy TLS protocols to begin planning for a transition to TLS 1.2 or higher in the near future.


For apps using the [App Transport Security (ATS)](https://developer.apple.com/documentation/security/preventing_insecure_network_connections) networking security feature on all connections (enabled by default for apps linked against iOS 9.0 or macOS 10.11 SDKs or later), which requires that all connections are secured with reliable TLS certificates and ciphers, no action is required.


Apple recommends switching directly to TLS 1.3 as it is a faster and more secure protocol than TLS 1.2 by adding support to the latest TLS version and removing these deprecated Security.framework symbols from apps:


* [`tls_protocol_version_t.TLSv10`](https://developer.apple.com/documentation/security/tls_protocol_version_t/tlsv10)
* [`tls_protocol_version_t.TLSv11`](https://developer.apple.com/documentation/security/tls_protocol_version_t/tlsv11)
* [`tls_protocol_version_t.DTLSv10`](https://developer.apple.com/documentation/security/tls_protocol_version_t/dtlsv10)


Ongoing effort to move away from outdated traffic encryption protocols
----------------------------------------------------------------------


Apple's update follows a joint[announcement](https://www.bleepingcomputer.com/news/security/tls-10-and-tls-11-being-retired-in-2020-by-all-major-browsers/) from Microsoft, Google, Apple, and Mozilla from October 2018, saying that the four organizations will start retiring insecure TLS protocols starting with the first half of 2020.


In August 2020, Microsoft [enabled TLS 1.3 by default](https://www.bleepingcomputer.com/news/security/microsoft-enables-tls-13-by-default-in-latest-windows-10-builds/) in the latest Windows 10 Insider builds.


"TLS 1.3 eliminates obsolete cryptographic algorithms, enhances security over older versions, and aims to encrypt as much of the handshake as possible," Microsoft [said](https://www.microsoft.com/security/blog/2020/08/20/taking-transport-layer-security-tls-to-the-next-level-with-tls-1-3/).


In January, [the NSA shared guidance](https://www.bleepingcomputer.com/news/security/nsa-shares-guidance-tools-to-mitigate-weak-encryption-protocols/) on detecting and replacing outdated Transport Layer Security (TLS) protocol versions with up-to-date and secure variants.


"Obsolete configurations provide adversaries access to sensitive operational traffic using a variety of techniques, such as passive decryption and modification of traffic through man-in-the-middle attacks," the NSA said.


"Attackers can exploit outdated transport layer security (TLS) protocol configurations to gain access to sensitive data with very few skills required."




#### Tags:
[[TLS]] [[(TLS)]] [[macOS]] [[said.]] [[apps]] [[Bleeping Computer]]
