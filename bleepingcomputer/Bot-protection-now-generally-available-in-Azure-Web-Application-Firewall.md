# Bot protection now generally available in Azure Web Application Firewall
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/bot-protection-now-generally-available-in-azure-web-application-firewall/)
+ Date: August 1, 2021
+ Author: Sergiu Gatlan


## Article:
![Bot protection now generally available in Azure Web Application Firewall](https://www.bleepstatic.com/content/hl-images/2021/07/30/Azure_WAF.jpg)


Microsoft has announced that the Web Application Firewall (WAF) bot protection feature has reached general availability on Azure Application Gateway starting this week.


[Azure Web Application Firewall](https://azure.microsoft.com/en-us/services/web-application-firewall/#overview) (WAF) is a cloud-native service designed to protect customers' web applications from bot attacks, common exploits, as well as common web vulnerabilities, including cross-site scripting, SQL injection, broken auth, security misconfigurations, and more.



Azure WAF can be deployed in a single click within minutes with Azure Application Gateway, Azure Front Door, and Azure Content Delivery Network (CDN) service from Microsoft.


"We are announcing the general availability of the Web Application Firewall (WAF) bot protection feature on Application Gateway," Microsoft [said](https://azure.microsoft.com/en-us/updates/general-availability-web-application-firewall-waf-bot-protection-on-application-gateway/) on Friday.


"This feature allows users to enable a managed bot protection rule set for their WAF to block or log requests from known malicious IP addresses."


The newly added bot protection rule set can also be used alongside OWASP core rule sets (CRS) to provide additional protection for your web apps.



Bad bots blocked using this new managed bot protection rule set can be used by threat actors for various resource-consuming or malicious tasks such as scraping, scanning, and looking for vulnerabilities in web applications. 


Once the bot protection rule is set up on Azure WAF via Application Gateway, bots using known malicious IP addresses sourced from the Microsoft Threat Intelligence feed are automatically blocked from using up your servers' resources or checking them for exploitable security gaps.


"The bot mitigation ruleset list of known bad IP addresses updates multiple times per day from the Microsoft Threat Intelligence feed to stay in sync with the bots," Microsoft further explains. "Your web applications are continuously protected even as the bot attack vectors change."


Additional information on configuring bot protection for Web Application Firewall is available on [Microsoft's Azure product documentation website](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/bot-protection).


The steps required to configure a bot protection rule set include:


1. Creating a basic WAF policy for Application Gateway by following the instructions described in [Create Web Application Firewall policies for Application Gateway](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/create-waf-policy-ag).
2. In the **Basic** policy page that you created previously, under **Settings**, select **Rules**.
3. On the details page, under the **Manage rules** section, from the drop-down menu, select the check box for the bot Protection rule, and then select **Save**.




#### Tags:
[[Microsoft]] [[(WAF)]] [[IP]] [[Bleeping Computer]]
