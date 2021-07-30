# Node.js fixes severe HTTP bug that could let attackers crash apps
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/nodejs-fixes-severe-http-bug-that-could-let-attackers-crash-apps/)
+ Date: July 30, 2021
+ Author: Ax Sharma


## Article:
![nodejs](https://www.bleepstatic.com/content/hl-images/2020/08/04/nodejs-header.jpg)


Node.js has released updates for a high severity vulnerability that could be exploited by attackers to corrupt the process and cause unexpected behaviors, such as application crashes and potentially remote code execution (RCE).


The use-after-free vulnerability, tracked as CVE-2021-22930 is to do with how HTTP2 streams are handled in the language.


Node.js pushes out immediate fixes for the flaw
-----------------------------------------------


This week Node.js has pushed out fixes for high severity, use-after-free vulnerability, tracked as CVE-2021-22930.


Use-after-free vulnerabilities occur when a program tries to access a resource at a memory address that has been previously freed and no longer holds the resource.


This can lead to data corruption, or unexpected behaviors such as application crashes, or even remote code execution (RCE) in some cases.


The fixes landed in the latest Node.js release 16.6.0 and were also backported to versions 12.22.4 (LTS) and 14.17.4 (LTS).


The fix shown below has been applied across multiple Node.js branches to squash the use-after-free vulnerability:



![fix commit](https://www.bleepstatic.com/images/news/u/1164866/2021/Jul-2021/nodejs-severe-flaw/nodejs-vuln-fix.jpg)**Simple fix resolves the vulnerability** ([GitHub](https://github.com/nodejs/node/pull/39527/commits/ba2ac7bb47406815c98366c5a591053414a1daf3#diff-33f026e43570112875cf4c8eab6743496f3aa014329611128e348ec23d6f771cR2165))
[Eran Levin](https://github.com/exx8) has been credited with reporting this vulnerability.


The abrupt update release for a high severity vulnerability is explained by the fact discussions around the vulnerability were already public:


"We normally like to give advance notice and provide releases in which the only changes are security fixes, but since this vulnerability was already public we felt it was more important to get this fix out fast in releases that were already planned," [announced](https://nodejs.org/en/blog/vulnerability/july-2021-security-releases-2/) Red Hat principal software engineer and NodeJS Technical Steering Committee (TSC) member Daniel Bevenius.


Bug triggered when aborting HTTP connections
--------------------------------------------


The vulnerability was triggered in cases where Node.js parsed incoming RST\_STREAM frames, with no error code or a cancel code.


In applications based on the [HTTP/2 protocol](https://datatracker.ietf.org/doc/html/rfc7540), RST\_STREAM frame is sent by either host intending to terminate a connection.


For example, in a client-server architecture, if a client application wants to end the connection, it would send an RST\_STREAM frame to the server.


On receiving the frame, the server will cease responding to the client, eventually aborting the connection. Any "DATA" frames which the server was about to send to the client, could then be discarded.


But in the case of vulnerable Node.js versions, when an RST\_STREAM frame was received by the server with a "cancel" code (*nghttp2\_cancel*), the receiver would try to "force purge" any data received.


And, once this was done, an automatic callback would additionally run the "close" function, attempting to free up the memory a second time—which had already been freed in the last step.


And, this would result in an application crash, or erratic behavior due to a double-free error.


This error—previously thought of as a "bug" rather than an exploitable vulnerability, was reported on June 8th, 2021 by Matthew Douglass on a [public thread](http://github.com/nodejs/node/issues/38964).


Douglass was able to reproduce the bug 100% of the time on his system, resulting in application crashes.


The discussion ensued for well over a month between Douglass and Node.js contributors:


"The issue seems to be because of the handling of the RST\_STREAM frame received with no error code and cancel error code."


"The node tries to force process it and purge any existing data for the stream. This causes *nghttp2* to close the already destroyed stream causing the double-free error," responded GitHub user *kumarak.*


The fix rolled out instead adds the incoming stream of RST\_STREAM frames to a queue and processes the queue once it is safe to do so. This would prevent any double-free or use-after-free errors.


Node.js users should upgrade to the latest version 16.6.0, or a patched backported version.




#### Tags:
[[Node.js]] [[RST_STREAM]] [[use-after-free]] [[vulnerability,]] [[double-free]] [[Douglass]] [[Bleeping Computer]]
