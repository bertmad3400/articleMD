# Juniper Networks adds cloud firewall to its SASE stack | ZDNet
### A hybrid approach to security enables a smooth transition and consistent policy management.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/juniper-networks-adds-cloud-firewall-to-its-sase-stack/
+ Date: 2022-02-03 05:46:00
+ Author: Zeus Kerravala


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/4385194fbc462cd4a381893a65796f372b2a8e4a/2021/10/27/0638e81a-0ebf-40c8-9a6a-816b334a17e3/juniper.jpg?width=770&height=578&fit=crop&auto=webp)

This week [Juniper Networks](https://www.juniper.net/) announced its new Secure Edge product, which is a cloud-based firewall-as-a-service (FWaaS) solution. The new product will be part of its [secure-access service edge (SASE)](https://www.zdnet.com/article/ibm-launches-new-sase-service-to-bolster-zero-trust-security/) portfolio, which currently includes application control, anti-malware, identity and access control, intrusion prevention, threat intelligence, zero trust, and secure web access. All the features available in Juniper's on-premises [SRX next-generation firewall (NGFW)](https://www.juniper.net/us/en/products/security/srx-series/compare.html?p=SRX1500,SRX300,SRX4100,SRX4200,SRX4600,SRX5400,SRX550,SRX5600,SRX5800) are now available from the cloud. 

Historically, SASE deployments had been tied to SD-WAN because customers required a different security model to protect a wide-area network that utilizes internet transport instead of private IP services, such as MPLS. SD-WAN deployments stalled when people were sent to work from home as companies started to rethink branch-office connectivity. 

**Also: [How Juniper is using AI in SD-WAN to differentiate itself](https://www.zdnet.com/article/how-juniper-is-using-ai-in-sd-wan-to-differentiate-itself/)**

### SASE enables businesses to give home workers business-grade security


This is when SASE purchasing shifted from secondary to primary. Securing home workers is a non-trivial, expensive task with traditional security devices. Businesses would need to connect workers to a corporate location via a VPN, aggregate the connection and secure them through a next-generation firewall, and then workers would connect to the internet through a single connection. 

Most home workers use cloud apps, obviating the need to connect to a company location. Ideally, users would directly connect to the cloud services, but this creates a security nightmare. One solution would be to give every worker a business-grade security device, but this is prohibitively expensive and creates a management nightmare because keeping hardware, software, firmware, and configurations up to date are difficult -- if not impossible -- on a user-by-user basis. 

Juniper's unique differentiator here is its unified policy management via its [Security Director Cloud](https://www.juniper.net/us/en/products/security/security-director-network-security-management.html?utm_medium=website&utm_source=Blog&utm_campaign=LNCH_AMER_SEC_MFL_21Q02) portal. There are many SASE vendors today, most of whom are cloud-only. While that model is ideally suited for remote work, it's not in line with hybrid work. The world has been in an almost 100% work-from-home model for the better part of two years, but people will eventually come back to the office -- not 100%, but part of the time. My research shows that 51% of employees plan to work at home 2 to 3 days a week in perpetuity, which means 2 to 3 days a week in the office.

### Hybrid is the way forward for security

This means traditional, on-premises firewalls, intrusion prevention systems, and similar tools will still be in place. Managing the remote workers using SASE and company locations via a different model is problematic because policies need to be kept in sync. Some of the SASE pure plays, such as Cato Networks, pitch a vision where all locations everywhere will be secured via SASE, but that's just not true.






Almost every technology transition shifts to a hybrid model. Think virtualization -- there are still many physical servers being used. The world isn't 100% VoIP, nor is it all wireless. Hybrid always winds up being the way for all technology. With security, once a location has more than a few hundred users, it makes no sense to secure it via the cloud because the amount of data generated to inspect the traffic cloud is more than user-generated traffic. For these large locations, on-premises systems will still be used. 

**Also: [How Intermedia became a viable contender in cloud communications](https://www.zdnet.com/article/why-intermedia-is-becoming-a-viable-contender-in-cloud-communications/)**

### Unified management is a key differentiator

Juniper's Security Director Cloud is a single pane of glass for unified policy management across the SRX firewalls and SASE cloud. This isn't just for firewalls because the policies extend to all the SRX capabilities. Current Juniper customers would benefit most because they could apply the existing policies to SASE-delivered services upon deployment of the service, possibly saving months of time. The hybrid nature of the service also lets customers migrate at a pace with which they are comfortable. 

The Juniper Security Director platform offers customers dynamic zero trust to adopt policies based on user behavior. For example, a worker could be accessing a new service that is exhibiting suspicious behavior. Juniper's system would automatically update the policies to protect the company. This can be particularly useful in a hybrid work environment where users may be purchasing their own services to store documents remotely, collaborate with others, or do another task. 

Shadow IT is one of the most challenging trends facing security professionals because it's a big blind spot as users connect to cloud services directly. Connecting workers to a SASE node shines a light on that blind spot, and then dynamic segmentation automatically sets the policies without IT intervention. 





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]] [[victim.industry.name=Agriculture]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Cloud]] [[Sase]] [[On-premises]] [[Srx]] [[Sd-wan]] [[Firewalls]] [[ZDNet]]

