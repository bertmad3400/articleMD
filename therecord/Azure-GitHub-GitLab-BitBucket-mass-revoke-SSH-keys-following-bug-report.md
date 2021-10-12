# Azure, GitHub, GitLab, BitBucket mass-revoke SSH keys following bug report
### 

## Information:
+ Source: The Record
+ Link: [article](https://therecord.media/azure-github-gitlab-bitbucket-mass-revoke-ssh-keys-following-bug-report/)
+ Date: October 12, 2021
+ Author: Catalin Cimpanu


## Article:
![Azure, GitHub, GitLab, BitBucket mass-revoke SSH keys following bug report](https://therecord.media/wp-content/uploads/2021/10/SSH-keys.jpg)

Microsoft, GitHub, GitLab, and BitBucket —four of today’s largest code hosting portals— have initiated mass revocations of SSH keys on Monday after the discovery of a vulnerability in a popular Git software client named GitKraken.


The mass revocations come at the request of Arizona-based software company Axosoft, which developed GitKraken and is the one who found the security flaw in its own software.


In a [blog post](https://www.gitkraken.com/blog/weak-ssh-key-fix) on Monday, Axosoft explained that versions 7.6.x, 7.7.x, and 8.0.0 of its GitKraken app used a library named “[keypair](https://www.npmjs.com/package/keypair)” to generated SSH keys to allow developers to connect their GitKraken app to accounts on Azure DevOps, GitHub, GitLab, BitBucket, or other remote Git source code hosting servers.


But Axosoft said that older versions of this library generated RSA keys with low entropy, meaning that attackers could use the library, under certain conditions, to generate duplicate SSH keys.


The attacker could then use these keys to access a user’s account and steal proprietary source code.


Axosoft said that as soon as it learned of the issue, it replaced the keypair library inside the GitKraken app, released version 8.0.1, and notified the four platforms.


Shortly after Axosoft’s blog post, the security teams of [Azure DevOps](https://devblogs.microsoft.com/devops/azure-devops-response-to-gitkraken-ssh-bug/), [GitHub](https://github.blog/2021-10-11-github-security-update-revoking-weakly-generated-ssh-keys/), [GitLab](https://about.gitlab.com/blog/2021/10/11/notice-for-gitkraken-users-with-gitlab/), and [Atlassian’s BitBucket](https://bitbucket.org/blog/action-required-for-gitkraken-users-using-ssh) have started revoking all SSH keys connected to accounts where the GitKraken app was used to synchronize source code.


The four platforms are now asking users to generate new SSH keys using a different Git client or using an updated GitKraken app.


Both Axosoft and the four platforms said they haven’t found evidence that attackers used this bug to compromise accounts — so far.


In addition, GitHub also asked the developers of other software applications —not only Git clients— to check and see if they are using the vulnerable keypair library in their apps, and update their code accordingly. The keypair library also received a [security update](https://github.com/juliangruber/keypair/releases/tag/v1.0.4) on Monday.





#### Tags:
[[GitKraken]] [[SSH]] [[Axosoft]] [[GitHub,]] [[GitLab,]] [[keypair]] [[The Record]]
