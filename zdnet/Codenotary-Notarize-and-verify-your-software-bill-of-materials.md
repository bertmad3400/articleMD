# Codenotary: Notarize and verify your software bill of materials
### What's really in that program? Codenotary can show your customers what's inside your software.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/codenotary-open-source-notarization-service-for-software-bill-of-material-arrives/)
+ Date: October 28, 2021
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

The [Solarwinds software supply chain attack](https://www.zdnet.com/article/solarwinds-the-more-we-learn-the-worse-it-looks/) is the one everyone knows about. But [supply chain attacks are becoming commonplace](https://www.zdnet.com/article/supply-chain-attacks-are-the-hackers-new-favourite-weapon-and-the-threat-is-getting-bigger/), and that's bad news. There are efforts afoot, such as the [Linux Foundation's](https://www.linuxfoundation.org/) Software Package Data Exchange® ([SPDX](https://spdx.dev/)) project, which ensures transparency and improves compliance for software bill of materials (SBOM). But, we need SBOMs now. 

As President Joseph Biden's [Executive Order on Improving the Nation's Cybersecurity](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) says, we must provide "a purchaser with an SBOM for each application." [Codenotary Community Attestation Service](http://cas.codenotary.com/) wants to help you with that.


It is a free, open-source notarization and verification service. Its parent company [Codenotary](https://codenotary.com/) promises it will enable businesses to easily create an SBOM, attesting to the provenance and safety of their code.

The Community Attestation Service provides end-to-end protection for software development and workloads. Codenotary also promises that it's scalable to millions of transactions per second, which makes it ideal for [continuous integration/continuous delivery (CI/CD)](https://www.hpe.com/us/en/insights/articles/continuous-integration-and-delivery-tool-basics-1807.html) services. It gives developers a way to attach a tamper-proof SBOM for development artifacts that include source code, builds, repositories, and Docker container images. 

These SBOMs are built without uploading any data to the service.  Instead, it notarizes these artifacts using cryptographic verification to uniquely identify development artifacts. Each artifact retains a cryptographically strong identity stored in Codenotary's immutable database, [immudb](http://www.immudb.io/). This is a fast and cryptographically-verifiable ledger database. 

This, unlike other SBOM systems, makes no guarantee about the safety of the components in your program. What it does do is assure your customers that the programs, code, libraries, container images, and so on truly are the ones you've promised them. This is no small thing.

"More and more software companies are being asked by their customers to provide a software bill of materials and to give guarantees about its veracity," said Dennis Zimmer, Codenotary's co-founder and CTO. "We're providing an easy way for developers to build an SBOM and let their customers and users know the provenance of their software is cryptographically and very easily verifiable, effectively enabling true [Zero Trust](https://www.zdnet.com/article/zero-trust-and-cybersecurity-heres-what-it-means-and-why-it-matters/) application delivery."






This is more than just a promise. [Home Assistant](https://www.home-assistant.io/), an open-source home automation company with hundreds of thousands of users, is using Codenotary's Community Attestation Service to ensure that only its approved code runs at the homes using its Internet-of-Things (IoT) software. 

"The open-source nature of Community Attestation Service, the easy integration and real-time revocation is a real game-changer," said Pascal Vizeli, Home Assistant's founder and core developer. "That is how software trust and integrity should look and feel."

Home Assistant isn't the only one who's bought into Codenotary's approach. Jack Aboutboul, community manager of the [CentOS](https://www.centos.org/) replacement Linux distro [AlmaLinux](https://almalinux.org/), said, "AlmaLinux is working on integration with the Community Attestation Service to provide a secure Software Bill of Materials for the AlmaLinux OS distribution and to guarantee the provenance of our builds."

Sound interesting? Head over to [Community Attestation Service](https://cas.codenotary.com/) and start creating your own tamper-proof SBOMs.

**Related Stories:**

* [Linux and open-source communities rise to Biden's cybersecurity challenge](https://www.zdnet.com/article/linux-and-open-source-communities-rise-to-bidens-cybersecurity-challenge/)
* [Linux Foundation announces new open-source software signing service](https://www.zdnet.com/article/linux-foundation-announces-new-open-source-software-signing-service/)
* [SolarWinds defense: How to stop similar attacks](https://www.zdnet.com/article/solarwinds-defense-how-to-stop-similar-attacks/)





#### Tags:
[[Codenotary]] [[open-source]] [[SBOM]] [[ZDNet]]
