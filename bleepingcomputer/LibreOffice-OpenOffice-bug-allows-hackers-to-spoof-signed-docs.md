# LibreOffice, OpenOffice bug allows hackers to spoof signed docs
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/libreoffice-openoffice-bug-allows-hackers-to-spoof-signed-docs/)
+ Date: October 11, 2021
+ Author: Bill Toulas


## Article:
![LibreOffice](https://www.bleepstatic.com/content/hl-images/2021/10/11/libreoffice-header.jpg?rand=909910483)


LibreOffice and OpenOffice have pushed updates to address a vulnerability that makes it possible for an attacker to manipulate documents to appear as signed by a trusted source. 


Although the severity of the flaw is classified as moderate, the implications could be dire. The digital signatures used in document macros are meant to help the user verify that the document hasn’t been altered and can be trusted. 


"Allowing anyone to sign macro-ridden documents themselves, and make them appear as trustworthy, is an excellent way to trick users into running malicious code.


The discovery of the flaw, which is tracked as [CVE-2021-41832](https://lists.apache.org/thread.html/rd3214a568b43dd335b5d558f521377f4bff750684dea18eb041fc1bb%40%3Cusers.openoffice.apache.org%3E) for OpenOffice, was the work of four researchers at the Ruhr University Bochum. 


The same flaw impacts LibreOffice, which is a fork of OpenOffice spawned from the main project over a decade ago, and for their project is tracked as [CVE-2021-25635](https://www.libreoffice.org/about-us/security/advisories/cve-2021-25635/). 


Addressing the risk
-------------------


If you’re using either of the open-source office suites, you’re advised to upgrade to the latest available version immediately. For OpenOffice, that would be 4.1.10 and later, and for LibreOffice, 7.0.5 or 7.1.1 and later. 


Since neither of these two applications offer auto-updating, you should do it manually by downloading the latest version from the respective download centers - [LibreOffice](https://www.libreoffice.org/download/download/), [OpenOffice](https://www.openoffice.org/download/index.html). 


If you’re using Linux and the aforementioned versions aren’t available on your distribution's package manager yet, you are advised to download the “deb”, or “rpm” package from the Download center or build LibreOffice from source. 


If updating to the latest version is not possible for any reason, you can always opt to completely disable the macro features on your office suite, or avoid trusting any documents containing macros. 


To set macro security on LibreOffice, go to Tools → Options → LibreOffice → Security, and click on ‘Macro Security’. 



![Menu to set macros to disabled on LibreOffice](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/macro%20settings.jpg)**LibreOffice settings menu to disable macros**
In the new dialog, you may select among four distinct levels of security, with High or Very High being the recommended options. 


If you’re still running an old and vulnerable version, you shouldn’t rely on the “trusted list” functionality as an invalid signature algorithm could still make a laced document appear as it comes from a trusted source.  




#### Tags:
[[LibreOffice]] [[LibreOffice,]] [[you’re]] [[source.]] [[Bleeping Computer]]
