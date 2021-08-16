# Apple to tune CSAM system to keep one-in-a-trillion false positive deactivation threshold
### Cupertino lays out how its system seeks to maintain integrity against political pressure and misidentified images.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/apple-to-tune-csam-system-to-keep-one-in-a-trillion-false-positive-deactivation-threshold/)
+ Date: August 16, 2021 -- 05:46 GMT (06:46 BST)
+ Author: Chris Duckett


## Article:
Unknown

![apple-csam-scanning.png](https://www.zdnet.com/a/hub/i/2021/08/09/df917fd7-8506-4a79-ad5f-9bd64ab641ee/apple-csam-scanning.png)
 Image: Apple
 When Apple announced its plans to [tackle child abuse material](https://www.zdnet.com/article/apple-child-abuse-material-scanning-in-ios-15-draws-fire/) on its operating systems last week, it said the threshold it set for false positives account disabling would be one in a trillion per year.

Some of the workings of how Apple arrived at that number was revealed in a [document](https://www.apple.com/child-safety/pdf/Security_Threat_Model_Review_of_Apple_Child_Safety_Features.pdf) [PDF] that provided more detail about the system. 

The most contentious component of Cupertino's plans was its on-device child sexual abuse material (CSAM) detection system. It will involve Apple devices matching images on the device against a list of known CSAM image hashes provided by the US National Center for Missing and Exploited Children (NCMEC) and other child safety organisations before an image is stored in iCloud. 

When a reporting threshold is reached, Apple will inspect metadata uploaded alongside the encrypted images in iCloud, and if the company determines it is CSAM, the user's account will be disabled and the content handed to NCMEC in the US. 

The document states that the CSAM hashes Apple used would be the intersection of two collections from two child safety organisations operating in different countries. 

"Any perceptual hashes appearing in only one participating child safety organization's database, or only in databases from multiple agencies in a single sovereign jurisdiction, are discarded by this process, and not included in the encrypted CSAM database that Apple includes in the operating system," the document states. 

After running the hashes against 100 million non-CSAM images, Apple found three false positives, and zero when run against a collection of adult pornography. The company said assuming a "worst-case" error rate of one in one million, it wanted a reporting threshold to ensure its one-in-a-trillion false positive disabling threshold. 






"Building in an additional safety margin by assuming that every iCloud Photo library is larger than the actual largest one, we expect to choose an initial match threshold of 30 images," it said. 

"Since this initial threshold contains a drastic safety margin reflecting a worst-case assumption about real-world performance, we may change the threshold after continued empirical evaluation of NeuralHash false-positive rates -- but the match threshold will never be lower than what is required to produce a one-in-one-trillion false positive rate for any given account." 

To ensure Apple's iCloud servers do not maintain a count of the number of positive CSAM images a user has, their device will also produce fake metadata, which Apple calls safety vouchers. Apple said its servers will not be able to distinguish real vouchers from the fake ones until the threshold is reached. 

"The on-device matching process will, with a certain probability, replace a real safety voucher that's being generated with a synthetic voucher that only contains noise. This probability is calibrated to ensure the total number of synthetic vouchers is proportional to the match threshold," Apple stated. 

"Crucially, these synthetic vouchers are a property of each account, not of the system as a whole. For accounts below the match threshold, only the user's device knows which vouchers are synthetic; Apple's servers do not and cannot determine this number, and therefore cannot count the number of true positive matches." 

Apple also confirmed the metadata would contain a low-resolution copy of the images for human inspection, and these copies are also run against the CSAM hashes. 

"This independent hash is chosen to reject the unlikely possibility that the match threshold was exceeded due to non-CSAM images that were adversarially perturbed to cause false NeuralHash matches against the on-device encrypted CSAM database," Apple said. 

"If the CSAM finding is confirmed by this independent hash, the visual derivatives are provided to Apple human reviewers for final confirmation." 

Cupertino said the system was designed so that a user does not need to trust Apple to know the system is "functioning as advertised". 

"The threat model relies on the technical properties of the system to guard against the unlikely possibility of malicious or coerced reviewers, and in turn relies on the reviewers to guard against the possibility of technical or human errors earlier in the system," Apple said. 

The company maintained that the human inspection process would ensure that if non-CSAM hashes were added into the reporting set, that the material would not be passed onwards out of Apple. 

"The reviewers are confirming one thing only: That for an account that exceeded the match threshold, the positively-matching images have visual derivatives that are CSAM," it said. 

"This means that if non-CSAM images were ever inserted into the on-device perceptual CSAM hash database -- inadvertently, or through coercion -- there would be no effect unless Apple's human reviewers were also informed what specific non-CSAM images they should flag (for accounts that exceed the match threshold), and were then coerced to do so." 

The company [reiterated it would refuse requests](https://www.zdnet.com/article/apple-to-refuse-government-demands-of-expanding-scanning-beyond-child-abuse/) to add non-CSAM images to the dataset. 

"Apple will also refuse all requests to instruct human reviewers to file reports for anything other than CSAM materials for accounts that exceed the match threshold," it stated. 

When it made the initial announcement, Apple also announced machine learning would be used within iMessage to alert parents using family sharing when child accounts have viewed or sent sexually explicit images, as well as provide warnings to the child. 

"For child accounts age 12 and younger, each instance of a sexually explicit image sent or received will warn the child that if they continue to view or send the image, their parents will be sent a notification. Only if the child proceeds with sending or viewing an image after this warning will the notification be sent," Apple previously said. 

"For child accounts age 13-17, the child is still warned and asked if they wish to view or share a sexually explicit image, but parents are not notified." 

In its document, Apple said the feature cannot be enabled for adult accounts, and is not enabled by default. 

On the issue of false positives, it said in the case of children aged between 13 to 17, if an image is miscategorised, and a child views it, they would see something that is not explicit. For those under 13, it could involve parental inspection. 

"For a child under the age of 13 whose account is opted in to the feature, and whose parents chose to receive notifications for the feature, sending the child an adversarial image or one that benignly triggers a false positive classification means that, should they decide to proceed through both warnings, they will see something that's not sexually explicit, and a notification will be sent to their parents," Apple said. 

"Because the photo that triggered the notification is preserved on the child's device, their parents can confirm that the image was not sexually explicit." 

Apple also said it has considered the issue of an adult being forced onto an account as a child under 13, but did not provide a resolution other than to state that not viewing the images would not make alerts be sent. 

"If the feature were enabled surreptitiously or maliciously -- for example, in the Intimate Partner Surveillance threat model, by coercing a user to join Family Sharing with an account that is configured as belonging to a child under the age of 13 -- the user would receive a warning when trying to view or send a sexually explicit image," it said. 

"If they chose to proceed, they would be given a second warning letting them know that viewing the image will result in a notification being sent, and giving them another choice about whether to proceed. If they declined to proceed, neither the fact that the warnings were presented, nor the user's decision to cancel, are sent to anyone." 

### Related Coverage

* [Apple child abuse material scanning in iOS 15 draws fire](/article/apple-child-abuse-material-scanning-in-ios-15-draws-fire/)
* [Apple to refuse government demands of expanding scanning beyond child abuse](/article/apple-to-refuse-government-demands-of-expanding-scanning-beyond-child-abuse/)
* [US Bill introduced to curb 'big tech bullying' in the app store space](/article/us-bill-introduced-to-curb-big-tech-bullying-in-the-app-store-space/)
* [Researchers discover new AdLoad malware campaigns targeting Macs and Apple products](/article/researchers-discover-new-adload-malware-campaigns-against-macs-and-apple-products/)





#### Tags:
[[CSAM]] [[said.]] [[non-CSAM]] [[on-device]] [["The]] [["If]] [["For]] [[ZDNet]]
