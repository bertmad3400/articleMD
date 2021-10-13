# Mandating a Zero-Trust Approach for Software Supply Chains
### Sounil Yu, CISO at JupiterOne, discusses software bills of materials (SBOMs) and the need for a shift in thinking about securing software supply chains.

## Information:
+ Source: ThreatPost
+ Link: [article](https://kasperskycontenthub.com/threatpost-global/?p=175333)
+ Date: October 13, 2021  9:22 am
+ Author: Sounil Yu


## Article:
![](https://media.threatpost.com/wp-content/uploads/sites/103/2018/11/20150953/Bug_Red_Code.jpg)
In the wake of the SolarWinds attack last year, President Biden issued an [executive order](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) in May advocating for mandatory [software bills of materials](https://www.ntia.gov/SBOM), or SBOMs, to increase software transparency and counter supply-chain attacks.


For reference, SBOMs are machine-readable documents that provide a definitive record of the components used to build a software product, including open-source software. As a security professional, I am encouraged by the SBOM mandate because it is a step towards providing greater transparency for the software that all organizations must buy and use.


Since the executive order, software makers and buyers have been trying to make sense of how SBOMs support supply-chain security. Undoubtedly, many see it as a headache, but I believe it is a sensible safeguard. Part of our problem around supply chains is that we trust in them too much. We have learned the benefits of a zero-trust security model and applied this concept to our networks and endpoints, but we haven’t quite figured out how to do this for our supply chains. We still rely heavily upon time-consuming questionnaires that perpetuate the continued reliance on trust as the foundation for supply-chain security.


[![Infosec Insiders Newsletter](https://media.threatpost.com/wp-content/uploads/sites/103/2021/07/10165815/infosec_insiders_in_article_promo.png)](https://threatpost.com/infosec-insider-subscription-page/?utm_source=ART&utm_medium=ART&utm_campaign=InfosecInsiders_Newsletter_Promo/)


The reason that we need things like SBOMs is because we *can’t trust* our supply chains, and thus we need it to be *transparent*. SBOMs provide a stepping stone towards achieving this transparency and allow us to start moving towards a zero-trust approach for software supply chains.


Rachel Botsman, a renowned trust expert and lecturer at Oxford University, has [described the problem](https://www.thepeoplespace.com/ideas/articles/you-cant-build-trust-through-transparency) this way: “One of the mistakes I hear is that the way to build more trust is through transparency. It is a common narrative. But if you need for things [to be transparent](https://threatpost.com/winning-cyber-defense-race/168996/), then you have practically given up on trust. By making everything transparent, you are reducing the need for trust.” SBOMs, by giving us greater transparency, allow us to exercise more zero-trust approaches in our supply chain.


**Confidence in the Unknown through SBOMs**
-------------------------------------------


Now, we cannot operate efficiently in an environment that truly stays at a level of zero trust. Some trust-building needs to happen. Botsman talks about defining trust as “a confident relationship with the unknown.” There are a lot of unknowns when it comes to our supply chains, but SBOMs also offer a way to gain confidence in the unknown.


Specifically, I believe that one’s ability to produce an SBOM with ease and at scale is highly correlated with the maturity and/or modernity of their software development practices. If one’s software-development practices are immature or antiquated, then creating an SBOM would generally be difficult.


If I ask a software supplier to produce an SBOM and it seems unable to, it would make me question their software-development practices. I would have lower confidence in the unknown factors associated with that software supplier.


Regardless of whether or not they are willing to actually show me the SBOM, simply knowing that they can easily produce an SBOM gives me confidence that their software development practices are modern or mature enough to counter a wide range of common issues related to vulnerable or poorly maintained software.


**Going Beyond SBOMs**
----------------------


SBOMs are a great first step towards supply-chain transparency, but there is more that needs to be done. As an analogy, many equate the SBOM to the ingredient labels on *food*. With that perspective, we can see parallels between our software supply chain and the food supply chain. Subsequently, the need for end-to-end provenance and resistance against tampering should be clear.


For this reason, I am encouraged by Google’s proposed [Supply-Chain Levels for Software Artifacts](https://slsa.dev/) (SLSA) framework that moves us towards a common language that increases the transparency and integrity of our software supply chain.


However, for some software that performs critical functions (e.g., security), food is an inadequate comparison. It may be more apt to compare this type of software to *medicine*. This analogy brings forth additional considerations. For example, the drug-facts label on medicines includes not just the ingredients, but also usage guidelines and contraindications (i.e., what to look for in case something goes wrong.) Furthermore, as we’ve all seen with the COVID-19 vaccine, medicines must undergo intensive review and testing before it is approved for use.


How these steps will be implemented will likely be debated for some time, but the need for them should not be under question. Until we have better controls around our software supply chain, we will continue our [diet of poisoned fruit](https://www.cnas.org/publications/reports/surviving-on-a-diet-of-poisoned-fruit-reducing-the-national-security-risks-of-americas-cyber-dependencies). We might get stronger through this diet, but it may also kill us. I’d rather not take that chance.


***Sounil Yu is Chief Information Security Officer at JupiterOne.***


***Enjoy additional insights from Threatpost’s Infosec Insiders community by***[***visiting our microsite***](https://threatpost.com/microsite/infosec-insiders-community/)***.***




#### Tags:
[[SBOMs]] [[SBOM]] [[supply-chain]] [[zero-trust]] [[chain.]] [[ThreatPost]]
