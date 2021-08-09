# Apple child abuse material scanning in iOS 15 draws fire
### Features to detect child abuse material stored on iCloud coming in updates to US users iOS 15, iPadOS 15, watchOS 8, and macOS Monterey.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/apple-child-abuse-material-scanning-in-ios-15-draws-fire/)
+ Date: August 9, 2021 -- 00:49 GMT (01:49 BST)
+ Author: Chris Duckett


## Article:
Unknown

![apple-csam-scanning.png](https://www.zdnet.com/a/hub/i/2021/08/09/df917fd7-8506-4a79-ad5f-9bd64ab641ee/apple-csam-scanning.png)
 Image: Apple
 On Friday, Apple [revealed plans](https://www.apple.com/child-safety/) to tackle the issue of child abuse on its operating systems within the United States via updates to iOS 15, iPadOS 15, watchOS 8, and macOS Monterey. 

The most contentious component of Cupertino's plans is its child sexual abuse material (CSAM) detection system. It will involve Apple devices matching images on the device against a list of known CSAM image hashes provided by the US National Center for Missing and Exploited Children (NCMEC) and other child safety organisations before an image is stored in iCloud. 

"Before an image is stored in iCloud Photos, an on-device matching process is performed for that image against the known CSAM hashes. This matching process is powered by a cryptographic technology called private set intersection, which determines if there is a match without revealing the result," Apple said. 

"The device creates a cryptographic safety voucher that encodes the match result along with additional encrypted data about the image. This voucher is uploaded to iCloud Photos along with the image." 

Once an unstated threshold is reached, Apple will manually look at the vouchers and review the metadata. If the company determines it is CSAM, the account will be disabled and a report sent to NCMEC. Cupertino said users will be able to appeal to have an account re-enabled. 

Apple is claiming its threshold will ensure "less than a one in one trillion chance per year of incorrectly flagging a given account". 

The other pair of features Apple announced on Friday were having Siri and search provide warnings when a user searches for CSAM-related content, and using machine learning to warn children when they are about to view sexually explicit photos in iMessages. 






"When receiving this type of content, the photo will be blurred and the child will be warned, presented with helpful resources, and reassured it is okay if they do not want to view this photo. As an additional precaution, the child can also be told that, to make sure they are safe, their parents will get a message if they do view it," Apple said. 

"Similar protections are available if a child attempts to send sexually explicit photos. The child will be warned before the photo is sent, and the parents can receive a message if the child chooses to send it." 

![apple-csam-siri-search-warning.jpg]()![apple-csam-siri-search-warning.jpg](https://www.zdnet.com/a/hub/i/2021/08/09/48502a93-6c68-4456-93af-89084da58872/apple-csam-siri-search-warning.jpg)
 Image: Apple
 ###  Plans labelled as a backdoor

Apple's plans drew criticism over the weekend, with Electronic Frontier Foundation labelling the features as a backdoor. 

"If you've spent any time following the Crypto Wars, you know what this means: Apple is planning to build a backdoor into its data storage system and its messaging system," the EFF wrote. 

"Apple can explain at length how its technical implementation will preserve privacy and security in its proposed backdoor, but at the end of the day, even a thoroughly documented, carefully thought-out, and narrowly-scoped backdoor is still a backdoor." 

EFF warned that once the CSAM system was in place, changing the system to search for other sorts of content would be the next step. 

"That's not a slippery slope; that's a fully built system just waiting for external pressure to make the slightest change," it said. 

"The abuse cases are easy to imagine: governments that outlaw homosexuality might require the classifier to be trained to restrict apparent LGBTQ+ content, or an authoritarian regime might demand the classifier be able to spot popular satirical images or protest flyers." 

The EFF added that with iMessage to begin scanning images sent and received, the communications platform was no longer end-to-end encrypted. 

"Apple and its proponents may argue that scanning before or after a message is encrypted or decrypted keeps the 'end-to-end' promise intact, but that would be semantic manoeuvring to cover up a tectonic shift in the company's stance toward strong encryption," the foundation said. 

Head of WhatsApp Will Cathcart said the Facebook-owned platform would not be adopting Apple's approach and would instead rely on users [reporting material](https://twitter.com/wcathcart/status/1423701475595755524). 

"This is an Apple built and operated surveillance system that could very easily be used to scan private content for anything they or a government decides it wants to control. Countries where iPhones are sold will have different definitions on what is acceptable," Cathcart said. 

The WhatsApp chief asked how the system would work in China, and what would happen once a spyware crew figured out how to exploit the system. 

WhatsApp [does scan](https://faq.whatsapp.com/general/how-whatsapp-helps-fight-child-exploitation/) unencrypted imagery -- such as profile and group photos -- for child abuse material. 

"We have additional technology to detect new, unknown CEI within this unencrypted information. We also use machine learning classifiers to both scan text surfaces, such as user profiles and group descriptions, and evaluate group information and behavior for suspected CEI sharing," the company said. 

Former Facebook CSO Alex Stamos said he was happy to see Apple taking responsibility for the impacts of its platform, but questioned the approach. 

"They both moved the ball forward technically while hurting the overall effort to find policy balance," Stamos said. 

"One of the basic problems with Apple's approach is that they seem desperate to avoid building a real trust and safety function for their communications products. There is no mechanism to report spam, death threats, hate speech, NCII, or any other kinds of abuse on iMessage." 

Instead of its "non-consensual scanning of local photos, and creating client-side ML that won't provide a lot of real harm prevention", Stamos said he would have preferred if Apple had robust reporting in iMessage, staffed a child safety team to investigate reports, and slowly rolled out client-side machine learning. The former Facebook security chief said he feared Apple had poisoned the well on client-side classifiers. 

"While the PRC has been invoked a lot, I expect that the UK Online Safety Bill and EU Digital Services Act were much more important to Apple's considerations," he said. 

Whistleblower Edward Snowden accused Apple of [deploying mass surveillance](https://twitter.com/snowden/status/1423469854347169798) around the globe. 

"Make no mistake: if they can scan for kiddie porn today, they can scan for anything tomorrow," he said. 

"They turned a trillion dollars of devices into iNarcs—*without asking.*" 

Late on Friday, *9to5Mac* [reported](https://9to5mac.com/2021/08/06/apple-internal-memo-icloud-photo-scanning-concerns/) on an internal memo from Apple that contained a note from NCMEC. 

"We know that the days to come will be filled with the screeching voices of the minority," NCMEC reportedly said. 

### Related Coverage

* [Why does it seem like Apple makes so many bad design choices?](/article/why-does-it-seem-like-apple-makes-so-many-bad-design-choices/)
* [Why you might not want to buy a new iPhone until 2022](/article/why-you-might-not-want-to-buy-a-new-iphone-until-2022/)
* [Stop ignoring this iPhone warning](/article/stop-ignoring-this-iphone-warning/)
* [Apple FYQ3 crushes expectations: $81.4 billion revenue, $1.30 EPS; shares sag](/article/apple-fyq3-crushes-expectations-81-4-billion-revenue-1-30-eps-shares-sag/)





#### Tags:
[[said.]] [[CSAM]] [[content,]] [[WhatsApp]] [[Stamos]] [[client-side]] [[ZDNet]]
