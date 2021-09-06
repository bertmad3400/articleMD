# This NPM package with millions of weekly downloads has fixed a remote code execution flaw
### Developers running Node.js applications will need to check if they're using the pac-resolver JavaScript library and update it if it hasn't been updated recently.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/this-npm-package-with-millions-of-weekly-downloads-has-fixed-a-remote-code-execution-flaw/)
+ Date: September 6, 2021 -- 11:02 GMT (12:02 BST)
+ Author: Liam Tung


## Article:
Unknown

A very popular NPM package called 'pac-resolver' for the JavaScript programming language has been fixed to address a remote code execution flaw that could affect a lot of Node.js applications. 

The flaw in the [pac-resolver](https://www.npmjs.com/package/pac-resolver) dependency was found by developer Tim Perry who notes it could have allowed an attacker on a local network to remotely run malicious code inside a Node.js process whenever an operator tried to send an HTTP request. Note.js is the popular JavaScript runtime for running JavaScript web applications. 


"This package is used for PAC file support in Pac-Proxy-Agent, which is used in turn in Proxy-Agent, which then used all over the place as the standard go-to package for HTTP proxy autodetection & configuration in Node.js," explains Perry. 

**SEE:** [**Developers, DevOps, or cybersecurity? Which is the top tech talent employers are looking for now?**](https://www.zdnet.com/article/developers-devops-and-cybersecurity-the-top-tech-talent-employers-are-looking-for-now/)

PAC or "Proxy-Auto Config" refers to PAC files written in JavaScript to distribute complex proxy rules that instruct an HTTP client which proxy to use for a given hostname, notes Perry, adding these are widely used in enterprise systems. They're distributed from local network servers and from remote servers, often insecurely over HTTP rather than HTTPs.  

It's a widespread issue as Proxy-Agent is used in Amazon Web Services Cloud Development Kit (CDK), the Mailgun SDK and Google's Firebase CLI. 

The package gets three million downloads per week and has 285,000 public dependent repos on GitHub, [Perry notes in a blogpost](https://httptoolkit.tech/blog/npm-pac-proxy-agent-vulnerability/). 






The vulnerability was fixed in v5.0.0 of all those packages recently and was marked as [CVE-2021-23406](https://snyk.io/vuln/SNYK-JS-PACRESOLVER-1564857) after it was disclosed last week.

It will mean a lot of developers with Node.js applications are potentially affected and will need to update to version 5.0. 

It affects anyone who depends on Pac-Resolver prior to version 5.0 in a Node.js application. It affects these applications if developers have done any of three configurations: 

* Explicitly use PAC files for proxy configuration
* Read and use the operating system proxy configuration in Node.js, on systems with WPAD enabled
* Use proxy configuration (env vars, config files, remote config endpoints, command-line arguments) from any other source that you wouldn't 100% trust to freely run code on your computer

"In any of those cases, an attacker (by configuring a malicious PAC URL, intercepting PAC file requests with a malicious file, or using WPAD) can remotely run arbitrary code on your computer any time you send an HTTP request using this proxy configuration," notes Perry. 





#### Tags:
[[HTTP]] [[JavaScript]] [[Node.js]] [[ZDNet]]
