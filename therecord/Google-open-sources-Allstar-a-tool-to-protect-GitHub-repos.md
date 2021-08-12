# Google open-sources Allstar, a tool to protect GitHub repos
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/google-open-sources-allstar-a-tool-to-protect-github-repos/)
+ Date: August 11, 2021
+ Author: Catalin Cimpanu


## Article:
![Google open-sources Allstar, a tool to protect GitHub repos](https://therecord.media/wp-content/uploads/2021/08/Allstar.jpg)

Google has open-sourced today a project named **Allstar**that can be used to secure GitHub projects by constantly watching and enforcing a set of security policies with the hope of preventing basic security misconfigurations.


Available as a GitHub app, [Allstar](https://github.com/ossf/allstar) can be installed on organizations and user accounts and allow it access to desired repositories.


Under the hood, Allstar works by reading a configuration file containing a set of user-defined rules—called **security policies**— and then constantly scanning and checking a project’s settings and recent events to ensure that no modifications are made to a project’s sensitive areas.


If a recent project update breaks one of the security policies, Google says Allstar can:


* Log the security policy violation;
* Open a GitHub issue to notify the administrators;
* Or take an automated action to fix or revert a project’s settings in order to have it comply with the original Allstar configuration.


Future Allstar development plans also include adding the ability to email an administrator when a policy check fails, block new code from being merged into a repository if a policy breaks, or notifying third-party apps via RPC calls for cross-platform updates.


Right now, Allstar supports configuration options for the following security policies, but Google said the project would soon receive more:


* Check if the “branch protection” feature is still enabled for a repository.
* Check if a project’s automatic dependency updates option is active.
* Check if a project has frozen dependencies.
* Check if repo admins are part of a specific GitHub organization.
* Check if binary artifacts (files) have been uploaded to a project.
* Check if a SECURITY.md file is present in a repo to ensure bugs are reported responsibly.


While Google has [initially developed Allstar](https://security.googleblog.com/2021/08/allstar-continuous-security-policy.htm), the project has been [open-sourced today](https://openssf.org/blog/2021/08/11/introducing-the-allstar-github-app/) under the Open Source Security Foundation, a foundation created last year by today’s biggest tech firms in order to help steer, guide, and share open source security tools.


Besides Google, the OpenSSF also includes members like GitHub, Microsoft, Canonical, Cisco, Facebook, Intel, HP, Tencent, IBM, Red Hat, Samsung, and [many more](https://openssf.org/about/members/).





#### Tags:
[[Allstar]] [[Google]] [[GitHub]] [[project’s]] [[The Record]]
