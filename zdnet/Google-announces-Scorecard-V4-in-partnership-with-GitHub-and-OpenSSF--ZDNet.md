# Google announces Scorecard V4 in partnership with GitHub and OpenSSF | ZDNet
### The Scorecards Action is available from GitHub's Marketplace and is free to use.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/google-announces-scorecard-v4-in-partnership-with-github-and-openssf/
+ Date: 2022-01-19 21:10:00
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/8405403f361da6d51b4ba2addb94a080c709aaa7/2022/01/07/ac46ff8c-2643-4d90-9b70-b947152e848b/google.png?width=770&height=578&fit=crop&auto=webp)

The Open Source Security Foundation (OpenSSF), GitHub, and Google [announced](https://openssf.org/blog/2022/01/19/reducing-security-risks-in-open-source-software-at-scale-scorecards-launches-v4/) on Wednesday the launch of Scorecards V4, which includes larger scaling, a new security check, and a new Scorecards GitHub Action for easier security automation.

OpenSSF launched the Scorecards in November 2020, creating an automated security tool that produces a "risk score" for open source projects and helps reduce the toil and manual effort required to continually evaluate changing packages when maintaining a project's supply chain.

Since Google and OpenSSF's July 2021 announcement of Scorecards V2, the Scorecards project has grown steadily to over 40 unique contributors and 18 implemented security checks.


The Scorecards Action, released in partnership with GitHub, automates the process on how to judge whether changes to a project affected its security. Previously, tasks like this had to be done manually. 

The Action is available from GitHub's Marketplace and is free to use. It can be installed on any public repository by following [these directions](https://github.com/marketplace/actions/ossf-scorecard-action).

"Since our [July announcement](https://security.googleblog.com/2021/07/measuring-security-risks-in-open-source.html) of Scorecards V2, the Scorecards project—an automated security tool to flag risky supply chain practices in open source projects—has grown steadily to over 40 unique contributors and 18 implemented security checks. Today we are proud to announce the V4 release of Scorecards, with larger scaling, a new security check, and a new Scorecards GitHub Action for easier security automation," [said](https://security.googleblog.com/2022/01/reducing-security-risks-in-open-source.html?m=1) Google Open Source Security Team members Laurent Simon and Azeem Shaikh.

"The Scorecards Action is released in partnership with GitHub and is available from [GitHub's Marketplace](https://github.com/marketplace/actions/ossf-scorecard-action). The Action makes using Scorecards easier than ever: it runs automatically on repository changes to alert developers about risky supply-chain practices. Maintainers can view the alerts on GitHub's [code scanning dashboard](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/managing-code-scanning-alerts-for-your-repository), which is available for free to public repositories on GitHub.com and via GitHub Advanced Security for private repositories."






The two added that they have scaled their weekly Scorecards scans to over one million GitHub repositories and partnered with the [Open Source Insights](http://deps.dev/) website for easy user access to the data.

![dangerous-workflow.png]()![dangerous-workflow.png](https://www.zdnet.com/a/img/resize/c68636fec09d0d598a41cf9ba48f5e7b0796ce6d/2022/01/19/50a30562-bf47-4b7c-a955-eef884ec7493/dangerous-workflow.png?width=470&fit=bounds&auto=webp)
 Google
 The Open Source Security Foundation explained in a blog post that although the world runs on open-source software, many open source projects [engage in at least one risky behavior](https://security.googleblog.com/2021/07/measuring-security-risks-in-open-source.html) -- like not enabling branch protection, not pinning dependencies, or not enabling automatic dependency updates. 

"Scorecards makes it simple to evaluate a package before consuming it: a scan run with a single line of code returns individual scores from 0 to 10 rating each individual security practice ("[checks](https://github.com/ossf/scorecard#scorecard-checks)") for the project and an aggregate score for the project's overall security. Today's release of a Scorecards GitHub Action makes it easier than ever for developers to stay on top of their security posture," the organization said. 

"The new [Scorecards GitHub Action](https://github.com/marketplace/actions/ossf-scorecard-action) automates this process: once installed, the Action runs a Scorecards scan after any repository change. Maintainers can view security alerts in GitHub's scanning dashboard and remediate any risky supply-chain practices introduced by the change."

All of the alerts will now include the severity of the risk, the file and line where the problem occurs, and the remediation steps to fix the issue. The latest release also adds the License check, which detects the presence of a project license, and the [Dangerous-Workflow check,](https://github.com/ossf/scorecard/blob/main/docs/checks.md#dangerous-workflow) which detects dangerous usage of the [pull\_request\_target](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/) trigger and risks of [script injections in GitHub workflows](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections).

A number of open-source projects have already adopted the Scorecards Action, including [Envoy](https://github.com/envoyproxy/envoy), [distroless](https://github.com/GoogleContainerTools/distroless), [cosign](https://github.com/sigstore/cosign), [rekor](https://github.com/sigstore/rekor), [kaniko](https://github.com/GoogleContainerTools/kaniko). 

"Scorecards provides us the ability to rapidly litmus test new dependencies in the Envoy project," said Envoy's Harvey Tuch. 

"We have found this a valuable step in vetting new dependencies for well-known attributes and we have integrated Scorecards into our dependency acceptance criteria. Machine checkable properties are an essential part of a sound security process." 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Agriculture]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Scorecards]] [[Github]] [[Google]] [[ZDNet]]

