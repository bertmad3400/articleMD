# Google's TensorFlow drops YAML support due to code execution flaw
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/googles-tensorflow-drops-yaml-support-due-to-code-execution-flaw/)
+ Date: September 5, 2021
+ Author: Ax Sharma


## Article:
![tensorflow](https://www.bleepstatic.com/content/hl-images/2021/09/05/Screenshot_2021-09-05_at_11.01.04-min.png)


TensorFlow, a popular Python-based machine learning and artificial intelligence project developed by Google has dropped support for YAML, to patch a critical code execution vulnerability.


YAML or Yet Another Markup Language is a convenient choice among developers looking for a human-readable data serialization language for handling configuration files and data in transit.


Untrusted deserialization vulnerability in TensorFlow
-----------------------------------------------------


Maintainers behind both TensorFlow and Keras, a wrapper project for TensorFlow, have patched an untrusted deserialization vulnerability that stemmed from unsafe parsing of YAML.


Tracked as CVE-2021-37678,  the critical flaw enables attackers to execute arbitrary code when an application deserializes a Keras model provided in the YAML format.


[Deserialization vulnerabilities](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data) typically occur when an application reads malformed or malicious data originating from inauthentic sources.


After an application reads and deserializes the data, it may crash resulting in a Denial of Service (DoS) condition, or worse, execute the attacker's arbitrary code.


This YAML deserialization vulnerability, rated a 9.3 in severity, was responsibly reported to TensorFlow maintainers by security researcher [Arjun Shibu](https://twitter.com/0xsegf).


And the source of the flaw, you ask? The notorious "yaml.unsafe\_load()" function in TensorFlow code:



![yaml.unsafe_load function call](https://www.bleepstatic.com/images/news/u/1164866/2021/Sep-2021/tensorflow-yaml-rce/load-unsafe-yaml.jpg)**Vulnerable *yaml.unsafe\_load* function call in TensorFlow** ([GitHub](https://github.com/tensorflow/tensorflow/blob/460e000de3a83278fb00b61a16d161b1964f15f4/tensorflow/python/keras/saving/model_config.py#L100))
The "unsafe\_load" function is known to deserialize YAML data rather liberally—it [resolves all tags](https://pyyaml.docsforge.com/master/api/yaml/unsafe_load/#Description), "even those known to be unsafe on untrusted input."


This means, ideally "unsafe\_load" should only be called on input that comes from a trusted source and is known to be free of any malicious content.


Should that not be the case, attackers can exploit the deserialization mechanism to execute code of their choice by injecting malicious payload in the YAML data which is yet to be serialized.


An example Proof-of-Concept (PoC) exploit shared in the vulnerability [advisory](https://github.com/advisories/GHSA-r6jx-9g48-2r5r) demonstrates just this:


TensorFlow drops YAML altogether in favor of JSON
-------------------------------------------------


After the vulnerability was reported, TensorFlow decided to drop YAML support altogether and use JSON deserialization instead.


"Given that YAML format support requires a significant amount of work, we have removed it for now," say the project maintainers in the same advisory.


"The methods `Model.to\_yaml()` and `keras.models.model\_from\_yaml` have been replaced to raise a `RuntimeError` as they can be abused to cause arbitrary code execution," also explain the release notes associated with the [fix](https://github.com/tensorflow/tensorflow/commit/23d6383eb6c14084a8fc3bdf164043b974818012).


"It is recommended to use JSON serialization instead of YAML, or, a better alternative, serialize to H5."


It is worth noting, TensorFlow is not the first or only project found to be using YAML's *unsafe\_load*. The function's use is rather prevalent in Python projects.


GitHub shows [thousands of search results](https://github.com/search?q=yaml.unsafe_load&type=code) referencing the function, with some developers proposing improvements:



![github results for applications using unsafe_load](https://www.bleepstatic.com/images/news/u/1164866/2021/Sep-2021/tensorflow-yaml-rce/yaml-github-results.jpg)**Many repos on GitHub have used and use YAML's unsafe load function**(GitHub)
Fix for CVE-2021-37678 is expected to arrive in TensorFlow version 2.6.0, and will also be backported into prior versions 2.5.1, 2.4.3, and 2.3.4, state the maintainers.




#### Tags:
[[YAML]] [[TensorFlow]] [[deserialization]] [[JSON]] [[Bleeping Computer]]
