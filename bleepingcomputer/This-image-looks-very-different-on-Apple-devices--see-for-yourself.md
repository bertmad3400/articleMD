# This image looks very different on Apple devices — see for yourself
### This image appears starkly different when viewed in Apple iOS and Mac devices as opposed to others. BleepingComputer explains why.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/technology/this-image-looks-very-different-on-apple-devices-see-for-yourself/
+ Date: 2021-12-17T02:56:38-05:00
+ Author: Ax Sharma


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/10/22/Apple-Finder_macOS.jpg)

![mac](https://www.bleepstatic.com/content/hl-images/2021/10/22/Apple-Finder_macOS.jpg)


Take a good look at the image below and the device you are on.


Now view it again on an Apple device. Conversely, if you are using an Apple device, view this page on an Android or Windows device.


'Think different,' see different
--------------------------------


If you are using an Apple device and viewing this page on Safari, chances are the image appears quite differently from what you'd see on, for example, Chrome or an imaging app on Windows.


Reverse engineer and cryptographer [David Buchanan](https://twitter.com/David3141593) might have left us all puzzled with his latest creation:



![The mysterious image](https://www.da.vidbuchanan.co.uk/widgets/pngdiff/a.png)**The mysterious image that appears different in Apple vs. non-Apple applications**
The PNG above reads 'HELLO WORLD' for most users—except those who see 'HELLO APPLE,' that is, in Apple-made software.


But, believe us, it is the same image *a.png,* interpreted differently by Apple and non-Apple applications.


In tests by BleepingComputer, on macOS Big Sur 11.6, the latest version of Chrome web browser (96.0.4664.110 (x86\_64)) rendered the text in the image as 'HELLO WORLD'. But, viewing this page on Safari, or the image alone in Mac's 'Preview' app shows 'HELLO APPLE.'



![Image appears differently in Safari and Chrome on macOS](https://www.bleepstatic.com/images/news/u/1164866/2021/Dec-2021/apple-image-rendering/apple-safari-chrome.jpg)**Image appears differently in Safari and Chrome on macOS**(BleepingComputer)
In another test by BleepingComputer on an iPhone, however, both Chrome web browser for iOS and Safari showed 'HELLO APPLE,' not 'HELLO WORLD.'


Here's one more to leave you startled a tad further—do you see an IBM or a Mac below? Once again, view this page with an Apple and non-Apple device:



![IBM or Mac?](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Do you see an IBM or Mac?**(Buchanan)
Why does this happen?
---------------------


On his website, Buchanan concisely [explains](http://www.da.vidbuchanan.co.uk/widgets/pngdiff/) the reason and the concept of 'parallel-decodable PNGs' that cause ambiguity among software applications.


Depending on an image renderer's implementation, the same PNG may be interpreted quite differently.


"I found this while writing my own multi-threaded PNG decoder. While pondering my design, I realised that I had an exploitable [implementation bug](https://github.com/DavidBuchanan314/parallel-png-proposal/issues/3)," writes the engineer.


"After learning that Apple has their own implementation of [parallel-decodable PNGs](https://www.hackerfactor.com/blog/index.php?/archives/895-Connecting-the-iDOTs.html), I realised that they'd made exactly the same mistake!"


Buchanan discovered that it was possible to craft a PNG file where:


decompress(a + b) != decompress(a) + decompress(b)
"This could happen if *a* ends midway through a non-compressed block. It is therefore possible for an image to have two possible interpretations, depending on whether a parallel or non-parallel decoder decodes it," further explains Buchanan.


"This can be mitigated by the decoder, by checking that there is no unprocessed data in each piece of the *zlib* stream. My implementation does not currently do this!"


To demonstrate the peak of possibilities that could be achieved with this 'mistake,' Buchanan shared proof-of-concept (PoC) code:



![PoC code](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**PoC code demonstrating how can the same PNG be interpreted differently**(BleepingComputer)
The 84-line PoC demonstrates how some image rendering libraries can be tricked into showing the alternate version of an image—the one with the 'SECRET MESSAGE.'


In fact, the reverse engineer has released a handy tool called '[Ambiguous PNG Packer](https://github.com/DavidBuchanan314/ambiguous-png-packer)' on GitHub that lets just about anyone create PNG images that look completely different in Apple software.


In March this year, Buchanan had also demonstrated how Twitter images could be abused to [hide 3-MB-large ZIP and MP3 files](https://www.bleepingcomputer.com/news/security/twitter-images-can-be-abused-to-hide-zip-mp3-files-heres-how/) within.


Now had the end result of this parallel-decoding business been merely an erroneous or corrupted image that wouldn't render correctly, it would be easier to classify this as a 'bug.'


But, we wonder, could this become a security risk in some contexts or an attack vector for malicious actors to abuse? The same file seen differently by two entities is bound to cause trouble.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]] [[action.malware.name=ZLib]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Png]] [[Non-apple]] [[Bleeping Computer]]

