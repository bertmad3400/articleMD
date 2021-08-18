# New Windows 10 21H2 build comes with improved WiFi security
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/new-windows-10-21h2-build-comes-with-improved-wifi-security/)
+ Date: August 18, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2021/01/25/Windows-10.jpg)


Microsoft has released Windows 10 21H2 19044.1200 with the awaited new Windows Hello security feature, WPA3 HPE support, and GPU computing in the Windows Subsystem for Linux.


In July, Microsoft [officially released the Windows 10 21H2 feature update](https://www.bleepingcomputer.com/news/microsoft/windows-10-21h2-preview-released-with-new-security-features/) to Insiders for testing but stated that its new features would be coming later.


Today, Microsoft released Windows 10 21H2 19044.1200 with the promised features:


* Adding WPA3 H2E standards support for enhanced Wi-Fi security
* Windows Hello for Business introduces a new deployment method called cloud trust to support simplified passwordless deployments and achieve a deploy-to-run state within a few minutes
* GPU compute support in the Windows Subsystem for Linux (WSL) and Azure IoT Edge for Linux on Windows (EFLOW) deployments for machine learning and other compute intensive workflows


WPA3 adds extra security to WiFi
--------------------------------


The WPA3 H2E (Hash-to-Element) protocol adds better protection from a Wi-Fi side-channel attack called "[DragonBlood](https://www.bleepingcomputer.com/news/security/wpa3-wi-fi-standard-affected-by-new-dragonblood-vulnerabilities/)" that could steal a WPA3 password.


"These attacks resemble dictionary attacks and allow an adversary to recover the password by abusing timing or cache-based side-channel leaks. Our sidechannel attacks target the protocol's password encoding method," explained a research paper about the DragonBlood side-channel attack.


"In response to the Dragonblood paper, IEEE 802.11 updated SAE by defining a new “Hash-to-Element” (H2E) method, as an optional alternative to the existing “Hunting-and-Pecking” method for the secret PWE (Password Element) derivation used in SAE authentication," [explained](http://blogs.cisco.com/networking/wpa3-bringing-robust-security-for-wi-fi-networks) Cisco.


"H2E is significantly more computationally efficient and provides robust resistance to side channel attack."


With today's preview build, Windows 10 21H2 supports the WPA3 protocol on compatible hardware.


GPU compute now supported in WSL2
---------------------------------


With the new [GPU compute support](https://blogs.windows.com/windowsdeveloper/2020/06/17/gpu-accelerated-ml-training-inside-the-windows-subsystem-for-linux/), Windows Subsystem for Linux users will be able to use NVIDIA CUDA and DirectML to perform machine learning and AI development.


This feature allows Windows users to use their graphics card to "to accelerate math-heavy workloads and uses its parallel processing to complete the required calculations faster, in many cases, than utilizing only a CPU.


This support includes running popular frameworks, such as PyTorch and TensorFlow, directly within WSL2.


The Windows Subsystem for Linux 2 is built into all Windows 10 versions, including Windows 10 Home, allowing users of all experience levels to get started with machine learning and AI as long as they have compatible graphics cards.


NVIDIA cards support CUDA and DirectML, while DirectML requires a DirectX 12 capable device from any GPU manufacturer.




#### Tags:
[[Windows]] [[WPA3]] [[GPU]] [[21H2]] [[Linux]] [[Microsoft]] [[side-channel]] [[Bleeping Computer]]
