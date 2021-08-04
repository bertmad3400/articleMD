# Qualys partners with Red Hat to improve Linux and Kubernetes security
### Security company Qualys is partnering with Red Hat to bring built-in Cloud Agent security to Red Hat Enterprise Linux CoreOS and Red Hat OpenShift.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/qualys-partners-with-red-hat-to-improve-linux-and-kubernetes-security/)
+ Date: August 4, 2021 -- 11:51 GMT (12:51 BST)
+ Author: Steven J. Vaughan-Nichols


## Article:
Unknown

Everyone in the Linux and cloud world knows [Red Hat](https://www.redhat.com/en). Everyone who pays attention to security knows [Qualys](https://www.qualys.com/). Now, the two are joining forces to bring [Qualys's Cloud Agent](https://www.qualys.com/cloud-agent/) to [Red Hat Enterprise Linux (RHEL) CoreOS](https://www.openshift.com/learn/coreos/) and [Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift) to better secure both systems.


Qualys Cloud Agent is a lightweight software agent. Typically it uses about 2% of CPU resources with bursts of up to 5%. Once in place, it takes a full configuration assessment of its host while running in the background and uploading that snapshot to the Qualys Cloud  Platform. The agent itself is self-updating and self-healing, so you need never reinstall or reboot it to keep the latest version up and running. 

OpenShift is, as most of you know, Red Hat's [Kubernetes](https://kubernetes.io/) distribution. CoreOS is Red Hat's specialized version of RHEL for OpenShift. Besides being its base operating system, CoreOS also underlines OpenShift's control plane. 

In this case, the CoreOS Cloud Agent for OpenShift works with Qualys's [Container Security Runtime](https://www.qualys.com/apps/container-security/). This provides continuous discovery of packages and vulnerabilities for the complete OpenShift stack. It does this by placing a lightweight snippet of Qualys code into the container image. Once there, it enables policy-driven monitoring, detection, and blocking of unwanted container behavior at runtime. This eliminates the need for host-based sidecar management and privileged containers. Once instrumented in the image, it will work within each container irrespective of where the container is instantiated and it doesn't need any additional administration containers. 

Specifically, the Qualys Cloud Agent for CoreOS on OpenShift brings the following features to OpenShift managers. 

* See the Full Inventory – Continuous visibility of installed software, open ports, and [Red Hat Security Advisories (RHSA](https://access.redhat.com/security/security-updates)) for all Red Hat Enterprise Linux CoreOS nodes with comprehensive reporting.
* Manage Host Hygiene – Fully integrated on the Qualys Cloud Platform to automatically detect and manage host status related to patches and compliance adherence for known vulnerabilities.    

* Easily Deploy to the Host - Simplified deployment via the Qualys Cloud Agent to secure the host operating system. This approach eliminates the need to modify the host, open ports, or manage credentials.
* Get Complete Coverage – Full coverage of Red Hat OpenShift and Qualys Container security delivers comprehensive visibility from the host operating system through to images and containers running on OpenShift.

Aaron Levey, Red Hat's Head of Security Partner Ecosystem, said in a statement that, "Qualys' Cloud Platform and Cloud Agent helps administrators gain deeper visibility into known vulnerabilities that may be present on their Red Hat Enterprise Linux CoreOS nodes with pointers to associated Red Hat Security Advisories, leaning on the expertise of Red Hat as well as Qualys' own skills in driving cloud-native security."

Sumedh Thakar, Qualys's president and CEO, added,  "By collaborating with Red Hat, we have built a unique approach to secure Red Hat Enterprise Linux CoreOS that provides complete control over containerized workloads enhancing Qualys' ability to help customers discover, track, and continuously secure containers."






**Related Stories:**

* [How Red Hat tackles security](https://www.zdnet.com/article/how-red-hat-tackles-security/)
* [Red Hat opens the door for both VMs and containers in its latest OpenShift release](https://www.zdnet.com/article/red-hat-opens-the-door-for-both-vms-and-containers-in-its-latest-openshift-release/)
* [Red Hat OpenShift supports both Windows and Linux containers](https://www.zdnet.com/article/red-hat-openshift-supports-both-windows-and-linux-containers/)





#### Tags:
[[Qualys]] [[OpenShift]] [[Cloud]] [[CoreOS]] [[Linux]] [[ZDNet]]
