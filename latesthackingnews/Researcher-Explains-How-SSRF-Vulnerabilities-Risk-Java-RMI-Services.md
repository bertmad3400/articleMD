# Researcher Explains How SSRF Vulnerabilities Risk Java RMI Services
### Mitigating SSRF vulnerabilities merely requires paying attention to securing Java RMI services, which admins often miss to employ.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2022/01/10/researchers-explain-how-ssrf-vulnerabilities-risk-java-rmi-services/
+ Date: 2022-01-10
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2019/10/vulnerability.jpg)
 A security researcher has explained how Java RMI services remain at risk of developing SSRF vulnerabilities. These vulnerabilities work under specific conditions, which, if met, can allow SSRF attacks. Securing backend services can effectively help alleviate the chances for such vulnerabilities.

  SSRF Vulnerabilities Risk Java RMI Services
--------------------------------------------

 Elaborating the details in a [blog post](https://blog.tneitzel.eu/posts/01-attacking-java-rmi-via-ssrf/), the researcher Tobias Neitzel has highlighted how Java RMI services remain exposed to SSRF attacks. These attacks become possible due to SSRF vulnerabilities that may develop under specific conditions.

 Describing Java RMI, the researcher stated,

 
> Java RMI is an object-oriented RPC (Remote Procedure Call) mechanism that is available by default in most Java installations. Developers can use Java RMI to create remote objects that expose their functions on the network and allow remote clients to call them. Java RMI communication relies on serialized Java objects, which makes the protocol a prime target for attackers.
> 
> 

 Briefly, the researcher observed how SSRF attacks become possible on these services. Although, the object-oriented RPC implementation ensures secure communication between the local and remote objects, hence exhibiting resilience to SSRF. However, the threat appears due to unsecured configurations that administrators often employ on RMI.

 Thus, [SSRF bugs](https://latesthackingnews.com/2017/07/06/web-applications-attacks-server-side-request-forgery/) threaten the RMI service’s security under the following conditions.

 
> 1. The *SSRF* vulnerability needs to allow arbitrary bytes being sent to the backend service (enables attacks on default *RMI* components like the *RMI registry*, the *DGC* or the *Activation system*).  
>  2. The *SSRF* vulnerability needs to return responses from the backend service and accept arbitrary bytes within them (enables attacks on all *RMI endpoints* including *JMX* and custom *remote objects*)
> 
> 

 When these conditions are met, an adversary can exploit SSRF to consume the backend service just as a direct connection.

 Neitzel has shared the technical details of such attacks step-by-step in his post.

 Recommended Mitigations
-----------------------

 According to the researcher, the following steps may help secure RMI services to prevent vulnerabilities.

 * Using the up-to-date Java version to avoid inherent vulnerabilities in older versions.
* Enabling TLS protection on RMI communications as the underlying protocol communicates data in plain text.
* Implementing user authentication.
* Using deserialization filters while ensuring that no apps or third-party libraries perform “dangerous actions during deserialization.”

 Let us know your thoughts in the comments.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Rmi]] [[Ssrf]] [[Backend]] [[Latest Hacking News]]
