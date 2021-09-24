# Google apologizes for scaring Cloud users with 'past due' emails
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/google/google-apologizes-for-scaring-cloud-users-with-past-due-emails/)
+ Date: September 24, 2021
+ Author: Lawrence Abrams


## Article:
![Google](https://www.bleepstatic.com/content/hl-images/2020/10/16/Google.jpg)


Google has apologized for a wave of emails warning Google Cloud Platform, Firebase, or API customers that their accounts may be suspended for a past due balance.


Users began receiving these emails on September 22nd, which warned that their account was "past due or does not have valid payment information".



> 
> Action required   
> 
> Dear Google customer, 
> 
> 
> You are receiving this email because you are a Google Cloud Platform, Firebase, or API customer. 
> 
> 
> Our records indicate that your billing account: [account\_id] is past due or does not have valid payment information associated with it. This may happen if your credit card has expired or was cancelled, and we haven't received valid payment information from you.
> 
> 
> Please update your billing account with valid payment information by following this link: https://console.cloud.google.com/billing/[account\_id]/settings  
> 
> 
> Failure to make payments may result in suspension and/or termination of your billing account and the related Project(s) or Service(s). If you have already updated your payment information, please disregard this message.
> 
> 
> 


BleepingComputer received one of these emails, and when we checked, the admin console showed a zero balance with valid payment information.


Other users reported similar emails even though they had valid payment information configured.




> 
> You weren't also waiting to discuss a scary "you need to pay your bill or we'll shut you off" notification that turned out to be a bug on Google's end, were you
> 
> 
> — Caleb Spare (@calebspare) [September 24, 2021](https://twitter.com/calebspare/status/1441443688383541260?ref_src=twsrc%5Etfw)


Google apologizes for the emails
--------------------------------


Today, Google sent another email to Google Cloud Platform users apologizing for the previous past due notices.


"You may have received a notification from us yesterday or earlier today indicating that your billing account is past due or your payment information is invalid and must be updated. That notification was provided in error due to a technical issue," explained today's email from Google.


"The issue has been resolved, and no action is required on your part."


"We apologize for any inconvenience this may have caused."



![Google apologizing for incorrect emails](https://www.bleepstatic.com/images/news/companies/google/c/cloud-platform-past-due/google-apologizes.jpg)**Google apologizing for incorrect emails**
According to an [incident report](https://www.google.com/appsstatus/dashboard/incidents/1Eo5iv7UhxrYvbnH5b7e) on the Google Workspace Status Dashboard, the issue began on September 22nd at 5:10 PM EST and lasted through September 23rd at 4:30 AM.


Google states an update to their payment configuration for the Google Cloud Platform caused these erroneous emails to go out.


"Google Workspace customers received a warning message on the Admin console user interface and an email regarding an issue with processing their account payment. Impacted customers were redirected to update payment information. Attempts to update the primary payment method caused the admin console to become unresponsive," explains Google in an incident report.


"Initial investigation of this issue revealed the impact was triggered after an update to the payment configuration was released during the impact time frame."


Users who have received these emails should ensure that they have accurate payment information in the console and that there is no past due balance.


All others can simply ignore the emails.




#### Tags:
[[Google]] [[emails]] [[Cloud]] [[Bleeping Computer]]
