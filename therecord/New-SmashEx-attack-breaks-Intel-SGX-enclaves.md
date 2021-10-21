# New SmashEx attack breaks Intel SGX enclaves
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/new-smashex-attack-breaks-intel-sgx-enclaves/)
+ Date: October 21, 2021
+ Author: Catalin Cimpanu


## Article:
![New SmashEx attack breaks Intel SGX enclaves](https://therecord.media/wp-content/uploads/2021/10/SmashEx.png)

Academics from universities in China, Singapore, and Switzerland have discovered a new attack method that can break the sanctity of Intel SGX enclaves and steal confidential data from inside an Intel CPU’s most secure area.


Named **SmashEx**, the attack impacts the Intel **S**oftware **G**uard e**X**tensions, also known as Intel SGX, a feature of almost all modern Intel processors that allows an OS or application to put sensitive data and operations inside a cryptographically secure area of the CPU named an “enclave.”


The SmashEx attack allows hostile software running on the same OS to abuse a feature that allows the CPU to pause SGX operations to enter the enclave and retrieve data. A high-level explanation provided by the research team is available below:


For normal functioning, the SGX design allows the OS to interrupt the enclave execution through configurable hardware exceptions at any point. This feature enables enclave runtimes (e.g., Intel SGX SDK and Microsoft Open Enclave) to support in-enclave exception or signal handling, but it also opens up enclaves to re-entrancy bugs. SmashEx is an attack which exploits enclave SDKs which do not carefully handle re-entrancy in their exceptional handling safely, which is complex on SGX. The SmashEx proof-of-concept exploits enable code reuse (e.g., ROP) and confidential data disclosure attacks in enclaves built with vulnerable enclave runtimes.


Researchers said that tests they carried out were successful in retrieving an RSA encryption key from inside an Intel SGX enclave used by a server to encrypt HTTPS traffic, and they were also able to dump the contents handled by the cURL app from inside a Microsoft Open Enclave, an enclave software toolkit used by Azure servers.


![SmashEx-demo](https://www-therecord.recfut.com/wp-content/uploads/2021/10/SmashEx-demo-1024x284.png)
Over the past few years, we’ve seen similar attacks that broke SGX enclaves to retrieve data. Past examples include [PlunderVolt](https://plundervolt.com/), [SgxSpectre](https://arxiv.org/abs/1802.09085), [Foreshadow](https://foreshadowattack.eu/), [BranchScope](http://www.cs.ucr.edu/~nael/pubs/asplos18.pdf), [Platypus](https://platypusattack.com/), [V0LTpwn](https://arxiv.org/abs/1912.04870), [Game of Threads](https://dl.acm.org/doi/10.1145/3373376.3378462), [AsyncShock](http://AsyncShock), [The Guard’s Dilemma](https://www.usenix.org/conference/usenixsecurity18/presentation/biondo), and [Iago](https://www.researchgate.net/publication/259753112_Iago_attacks_Why_the_system_call_API_is_a_bad_untrusted_RPC_interface).


In addition, a 2019 study of eight popular enclave software development kits, software libraries that are used by app makers to allow their apps to interact and store data inside enclaves, found 35 different vulnerabilities across all tested SDKs, including SGX.


But researchers say that the SmashEx attack is far more dangerous than the ones listed above, as it doesn’t merely just leak data from inside SGX enclaves but can also corrupt it—if needed.


### Patches are available


As a result, details about the SmashEx attack were only published yesterday, on a [dedicated website](https://jasonyu1996.github.io/SmashEx/), after both Intel and Microsoft released patches to address the issue in their respective SDKs—namely the [Intel SGX SDK](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00548.html) (CVE-2021-0186) and the [Open Enclave SDK](https://github.com/openenclave/openenclave/security/advisories/GHSA-mj87-466f-jq42) (CVE-2021-33767).


To prevent attacks, applications that like to store sensitive information inside SGX enclaves will have to incorporate these updates in their code.


However, the research team says that there are many other SDKs that are affected by the SmashEx attack, whose developers will now have to issue their own set of patches, including SGX SDKs from Google, Apache, and Arm.




| Runtime | Vendor | Affected SGX generations |
| --- | --- | --- |
| [Intel SGX SDK](https://github.com/intel/linux-sgx) | Intel | SGX2 |
| [Open Enclave](https://openenclave.io/sdk/) | Microsoft | SGX1 and SGX2 |
| [Google Asylo](https://asylo.dev/) | Google | SGX2 |
| [EdgelessRT](https://github.com/edgelesssys/edgelessrt) | Edgeless Systems | SGX1 and SGX2 |
| [Rust SGX SDK](https://teaclave.apache.org/) | Apache | SGX2 |
| [Teaclave](https://teaclave.apache.org/) | Apache | SGX2 |
| [SGX-LKL](https://github.com/lsds/sgx-lkl) | Imperial College London | SGX1 and SGX2 |
| [CoSMIX](https://github.com/acsl-technion/cosmix) | Technion | SGX2 |
| [Veracruz](https://github.com/veracruz-project/veracruz) | ARM | SGX2 |





#### Tags:
[[SGX]] [[SmashEx]] [[SDK]] [[Microsoft]] [[SDKs]] [[The Record]]
