# Fortinet warns of Black Friday scams involving PS5s, Xboxes and fake Amazon gift card generators that steal crypto
### Researchers with FortiGuard Labs said they found a file titled "Amazon Gift Tool.exe" that was being marketed on a publicly available file repository site as a free Amazon gift card generator.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/fortinet-warns-of-black-friday-scams-involving-ps5s-xbox-and-fake-amazon-gift-card-generator-stealing-crypto/)
+ Date: October 30, 2021
+ Author: Jonathan Greig


## Article:
Unknown

Fortinet's FortiGuard Labs has [discovered](https://www.fortinet.com/blog/threat-research/black-friday-scams-are-coming-online-shoppers-should-approach-with-caution) a new scam using the lure of an Amazon gift card generator to steal cryptocurrency from people.

Researchers with FortiGuard Labs said they found a file titled "Amazon Gift Tool.exe" that was being marketed on a publicly available file repository site as a free Amazon gift card generator.

When people download the file and open it, a malicious winlogin.exe is dropped and executed. 

"The purpose of the malware is simple. If the victim tries to add money to their anon-bitcoin wallet by copying and pasting the wallet address, the malware overwrites the victim's wallet address on the clipboard with its own, resulting in the money potentially going to the attacker," the researchers explained. 

According to FortiGuard Labs, the malware watches a user's clipboard to search for text that is 54 characters long -- the length of a cryptocurrency wallet address -- and other criteria that indicate the text is related to cryptocurrency. 

If the text matches three different criteria, the malware puts the attacker's Bitcoin Cash wallet address in place of the clipboard information.

The malware also searches for addresses related to Ethereum, Binancecoin, Litecoin, Dogecoin and Ripple. 






"We also found that the malicious winlogin.exe was distributed by a number of droppers with enticing names, such as Crunchyroll Breaker.exe, Netflix Tools.exe, Multi Gift Tools.exe, etc," FortiGuard Labs explained. 

"Free generators of this sort has been around and scammed people for years. But given the market power of Amazon, this new scam is especially enticing. Consumers are eager to shop as much as they can on Black Friday as a lot of goods go on sale. Free Amazon gift cards are very attractive to those who want to spend less for the holiday season. However, be careful with what you wish for and don't fall a victim to scams like this one."

Derek Manky, chief of security insights & global threat alliances at Fortinet's FortiGuard Labs, told ZDNet that they made this research discovery through their threat hunting process while looking for specific rules/targets. 

FortiGuard Labs found samples collected through open repository and then did further correlation work from there as part of discovery phase, Manky said. 

Cryptowallet addresses are quite large, and while cryptowallet users may write their wallet in a physical location, chances are they have this stored digitally -- either in a cold storage wallet or on their workstation, according to Manky.

"That digital cryptowallet addresses is typically accessed when doing transactions to send/receive money during the transaction itself on the client machine. In this instance, the attacker is hoping to replace the victim wallet with theirs to divert the funds. Keep in mind there usually is MFA with these transactions, but that's done by the client to approve. They may not notice the wallet address they pasted was actually not their own," Manky said. 

"This attack attempt has been specifically designed to hijack cryptowallet addresses/transactions similar to payment diversion fraud. And specifically Bitcoin Cash."

FortiGuard Labs also found another scam related to gaming consoles, attempting to lure those interested in purchasing PlayStation 5 and Xbox Series X and S systems.

The researchers found a group of malicious PDF files with titles like, "how\_much\_do\_xbox\_one\_cost\_on\_black\_Friday.pdf" and "Walmart\_black\_Friday\_ps5\_pickup.pdf."

After victims click on the link, they are taken to phishing sites where they are asked to give out confidential information. 





#### Tags:
[[FortiGuard]] [[malware]] [[cryptowallet]] [[ZDNet]]
