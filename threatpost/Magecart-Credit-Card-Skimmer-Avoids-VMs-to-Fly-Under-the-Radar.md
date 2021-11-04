# Magecart Credit Card Skimmer Avoids VMs to Fly Under the Radar
### The Magecart threat actor uses a browser script to evade detection by researchers and sandboxes so it targets only victims’ machines to steal credentials and personal info.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175993)
+ Date: November 4, 2021  8:51 am
+ Author: Elizabeth Montalbano


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2021/11/04084113/radar-e1636029689440.jpeg)
A new [Magecart](https://threatpost.com/magecart-campaign-10k-online-shoppers/159216/) threat actor is stealing people’s payment card info from their browsers using a digital skimmer that uses a unique form of evasion to bypass virtual machines (VM) so it targets only actual victims and not security researchers.


The Malwarebytes team discovered the new campaign, which adds an extra browser process that uses the WebGL JavaScript API to check a user’s machine to ensure it’s not running on a VM, researchers revealed in a [blog post](https://blog.malwarebytes.com/threat-intelligence/2021/11/credit-card-skimmer-evades-virtual-machines/) published Wednesday.


“By performing this in-browser check, the threat actor can exclude researchers and sandboxes and only allow real victims to be targeted by the skimmer,” Malwarebytes Head of Threat Intelligence Jérôme Segura wrote in the post.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


[Magecart](https://threatpost.com/magecart-attackers-stolen-data-jpg/164815/) is an umbrella term for different threat groups who all compromise [e-commerce websites](https://threatpost.com/magecart-ecommerce-card-skimming-bonanza/147765/) with card-skimming scripts on checkout pages to steal customer payment and personal data. Because their activity is so familiar to security researchers, they are constantly looking for new and creative ways to avoid being caught.


Detecting VMs used by security researchers and sandboxing solutions that are set to pick up Magecart activity is “the most popular method” used to evade detection, Segura said. However, for web-based threats, “it is more rare to see detection of virtual machines via the browser,” he said. Usually threat actors filter targets based on geolocation and user-agent strings, Segura wrote.


However, seeing cybercriminals shift tactics is not surprising, he noted, demonstrating that as researchers up their game to detect and report such nefarious activity, so too do cybercriminals adapt and evolve. “This is a natural trade-off that we must expect,” Segura wrote.


**How It’s Done**
-----------------


In this campaign, threat actors use WebGL JavaScript API to identify the graphics renderer of the machine the actor is targeting to return its name, which gives the skimmer the information it needs to discern whether a VM is present or not.


“For many virtual machines, the graphics card driver will be a software renderer fallback from the hardware (GPU) renderer,” Segura explained. “Alternatively, it could be supported by the virtualization software but still leak its name.”


Specifically, the skimmer checks for the presence of the words **swiftshader**, **llvmpipe** and **virtualbox** because of the VMs different browsers use, he said. Google Chrome uses [SwiftShader](https://github.com/google/swiftshader) while Firefox relies on [llvmpipe](https://docs.mesa3d.org/drivers/llvmpipe.html) as its renderer fallback.


If the targeted machine passes the check, the skimmer then extracts personal data in a typical way for such campaigns, scraping a number of fields including the customer’s name, address, email and phone number as well as their credit-card data.


The skimmer also collects any password used for online stores on which the person has registered an account, the browser’s user-agent and a unique user ID. It then encodes the data and sends it to the same site hosting the skimmer using a single POST request, Segura wrote.


Malwarebytes has included the skimmer code as well as a comprehensive list of indicators of compromise in its post to help people avoid being targeted and compromised by the campaign.


***Want to win back control of the flimsy passwords standing between your network and the next cyberattack? Join Darren James, head of internal IT at Specops, and Roger Grimes, data-driven defense evangelist at KnowBe4, to find out how during a free, LIVE Threatpost event,*** [***“Password Reset: Claiming Control of Credentials to Stop Attacks,”***](https://bit.ly/3bBMX30) ***on Wed., Nov. 17 at 2 p.m. ET. Brought to you by Specops.***


[***Register NOW***](https://bit.ly/3bBMX30) ***for the LIVE event and submit questions ahead of time to Threatpost’s Becky Bracken at*** [***mailto:becky.bracken@threatpost.com***](mailto:becky.bracken@threatpost.com)***.***




#### Tags:
[[Segura]] [[Magecart]] [[Malwarebytes]] [[said.]] [[wrote.]] [[ThreatPost]]
