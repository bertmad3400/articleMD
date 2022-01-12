# Google finds a nation-state level of attacks on iPhone
### Much of mobile security advice these days is for users to be careful, not click on suspicious links nor open suspicious emails or attachments. But the growing popularity of no-click attacks sidesteps these defenses — and Google has drilled into one such attack.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3646228/google-finds-a-nation-state-level-of-attacks-on-iphone.html
+ Date: 2022-01-11T03:31-05:00
+ Author: Evan Schuman


## Article:
![Article Image](https://images.idgesg.net/images/article/2020/09/security_system_involving_a_wall_of_combination_locks_on_interconnected_puzzle_pieces_and_shield_cybersecurity_encryption_cryptographic_solutions_by_artystarty_gettyimages-1254278292_2400x1600-100858211-large.jpg?auto=webp&quality=85,70)

When it comes to mobile security, users are routinely warned to be extremely careful, avoid suspicious links, emails, and attachments. But the growth of no-click attacks sidesteps these soft defenses.

Google recently drilled into one such attack, which happened to have hit an iPhone. “We assess this to be one of the most technically sophisticated exploits we've ever seen, further demonstrating that the capabilities (one vendor) provides rival those previously thought to be accessible to only a handful of nation states,” [said the Google advisory](https://googleprojectzero.blogspot.com/2021/12/a-deep-dive-into-nso-zero-click.html).

The most frightening part of the Google report — and there are a *lot* of frightening parts — is that it violates one of the unwritten rules of security alerts, namely that it’s suboptimal to report the details of an attack for which there is no effective defense. I agree with Google here that the details need to be discussed so that the community can more quickly concoct a defense.

“It has been documented that NSO is offering their clients zero-click exploitation technology, where even very technically savvy targets who might not click a phishing link are completely unaware they are being targeted. In the zero-click scenario, no user interaction is required. Meaning, the attacker doesn't need to send phishing messages. The exploit just works silently in the background. Short of not using a device, there is no way to prevent exploitation by a zero-click exploit. It's a weapon against which there is no defense.”

On that comforting thought, let’s jump into the specifics.

The graphic that isn’t really a graphic
---------------------------------------

The company behind the software used in these attacks, NSO, reportedly uses a fake GIF trick to target a vulnerability in the CoreGraphics PDF parser. The files have a .gif extension, but they are not GIF image files. The name is solely designed to keep a user from getting worried.

“The ImageIO library is used to guess the correct format of the source file and parse it, completely ignoring the file extension. Using this fake gif trick, more than 20 image codecs are suddenly part of the iMessage zero-click attack surface, including some very obscure and complex formats, remotely exposing probably hundreds of thousands of lines of code.” 

As Google noted, these attacks are difficult to thwart. Blocking all GIF images is unlikely to prove effective. First, these files aren’t actually GIFs. The simplest approach is to block anything using a GIF extension, but the bad guys will simply switch to a different innocuous-sounding extension.

(Note: The Google report said Apple has been trying to negate the GIF attack through patches released in 2021. “Apple inform us that they have restricted the available ImageIO formats reachable from IMTranscoderAgent starting in iOS 14.8.1 (26 October 2021), and completely removed the GIF code path from IMTranscoderAgent starting in iOS 15.0 (20 September 2021), with GIF decoding taking place entirely within BlastDoor.”

The compression technique
-------------------------

This is about a common legitimate tactic for reducing the size of files by replacing some repeated characters. This gets into the weeds a bit: “This gives the current destination page JBIG2Bitmap an unknown, but very large, value for h. Since that h value is used for bounds checking and is supposed to reflect the allocated size of the page backing buffer, this has the effect of ‘unbounding’ the drawing canvas. This means that subsequent JBIG2 segment commands can read and write memory outside of the original bounds of the page backing buffer.”

The result?

“By rendering 4-byte bitmaps at the correct canvas coordinates, they can write to all the fields of the page JBIG2Bitmap and by carefully choosing new values for w, h and line, they can write to arbitrary offsets from the page backing buffer. At this point, it would also be possible to write to arbitrary absolute memory addresses if you knew their offsets from the page backing buffer. But how to compute those offsets? Thus far, this exploit has proceeded in a manner very similar to a canonical scripting language exploit which in Javascript might end up with an unbounded ArrayBuffer object with access to memory. But in those cases, the attacker has the ability to run arbitrary Javascript, which can obviously be used to compute offsets and perform arbitrary computations. How do you do that in a single-pass image parser? In practice, this means it is possible to apply the AND, OR, XOR and XNOR logical operators between memory regions at arbitrary offsets from the current page's JBIG2Bitmap backing buffer. And since that has been unbounded…, it's possible to perform those logical operations on memory at arbitrary out-of-bounds offsets.”

This is a coding issue that allows attackers to slip in and execute unauthorized code. This information is critical, as it both allows for coders to avoid this hole from time to time as well as giving software something concrete to find and block.

Out-of-scope attacks
--------------------

Another Google point: “JBIG2 doesn't have scripting capabilities, but when combined with a vulnerability, it does have the ability to emulate circuits of arbitrary logic gates operating on arbitrary memory. So why not just use that to build your *own* computer architecture and script that!? That's exactly what this exploit does. Using more than 70,000 segment commands defining logical bit operations, they define a small computer architecture with features such as registers and a full 64-bit adder and comparator, which they use to search memory and perform arithmetic operations. It's not as fast as Javascript, but it's fundamentally computationally equivalent. The bootstrapping operations for the sandbox escape exploit are written to run on this logic circuit and the whole thing runs in this weird, emulated environment created out of a single decompression pass through a JBIG2 stream.”

Google is quite right when it argues that this stuff is getting close to nation-state level of bad. But at least these details will help CIOs and CISOs start to maneuver around it.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Google]] [[Zero-click]] [[Jbig2bitmap]] [[Javascript]] [[Computerworld]]

