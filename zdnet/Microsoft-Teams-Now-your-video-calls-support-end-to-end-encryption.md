# Microsoft Teams: Now your video calls support end-to-end encryption
### Enterprise Teams users can have end-to-end encryption (E2EE) on one-to-one audio and video calls.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/microsoft-teams-now-your-video-calls-support-end-to-end-encryption/)
+ Date: October 22, 2021
+ Author: Liam Tung


## Article:
Unknown

Microsoft has rolled out a public preview of E2EE for one-to-one Teams calls, bringing its enterprise platform up to par with Facebook's consumer apps, WhatsApp and Messenger. 

Microsoft announced the encryption feature [was in the works in March at Ignite Spring 2021](https://www.zdnet.com/article/microsoft-to-add-new-shared-channels-encryption-for-calls-webinar-features-to-teams/). E2EE means that neither Microsoft, nor anyone else can access the decrypted contents of a one-to-one call. Facebook in August [rolled out E2EE for audio and video calls on its Messenger app](https://messengernews.fb.com/2021/08/13/messenger-updates-end-to-end-encrypted-chats-with-new-features/).    


Enabling E2EE for Teams calls requires work from both end users and IT admins, whom need to enable it for their users. 

**SEE:** [**When the return to the office happens, don't leave remote workers out in the cold**](https://www.zdnet.com/article/when-the-return-to-the-office-happens-remote-workers-risk-getting-left-behind/)

E2EE works by encrypting information from one point to an intended destination and prevents anyone else from decrypting the transmission. 

Microsoft [notes in a blogpost](https://techcommunity.microsoft.com/t5/microsoft-teams-blog/use-end-to-end-encryption-for-one-to-one-microsoft-teams-calls/ba-p/2867066) that real-time video and voice data is protected by E2EE and that both parties need to enable the setting. It doesn't cover things like chat or file-sharing, which are protected at rest and in-transit by other encryption protocols like HTTPS for secure connections between a device and a website.

To allow this feature, admins need to enable Enhanced Encryption policies for Teams users. Admins can enable it across the entire organization or set custom policies that assign the capability to select users. 






Assuming an admin has permitted E2EE via a policy, end users can enable it for a call by going to their avatar and navigating to the Privacy section within Settings. There's a toggle next to "End-to-end encrypted calls" that can be switched on. 

When both parties have enabled E2EE, there's an indicator in the top left of the video indicating it is enabled for that call. Both parties should see that indicator – a shield with a lock. If E2EE isn't turned on, the indicator is a regular shield icon without the lock. If it is enabled, there's a 20-digit security code under the indicator that should be the same for both parties. 

Two parties on a call can validate the 20-digit security codes by reading them to each other to see if they match. If they don't match, the connection has been intercepted by a man-in-the-middle attack and the call can be terminated.

**SEE:**[**Video meeting overload is real. Here's how you can to stop the stress building up**](https://www.zdnet.com/article/back-to-back-video-meetings-are-making-us-all-more-stressed-heres-how-to-fix-it/#link=%7B%22role%22:%22standard%22,%22href%22:%22https://www.zdnet.com/article/back-to-back-video-meetings-are-making-us-all-more-stressed-heres-how-to-fix-it/%22,%22target%22:%22%22,%22absolute%22:%22%22,%22linkText%22:%22%3Cstrong%3EVideo%20meeting%20overload%20is%20real.%20Here's%20how%20you%20can%20to%20stop%20the%20stress%20building%20up%3C/strong%3E%22%7D)

Teams calls E2EE is supported on the Teams desktop client for Windows and Mac as well as the latest versions of Teams on iOS and Android. It's not supported on Teams calls on PSTN. 

Features that aren't supported when E2EE is enabled include all the cloud and AI tools Microsoft brings to Teams, such as call recording, as well as live caption and transcription. 

As for E2EE on group audio and video calls, Microsoft isn't committing to to anything on that front, but says it is working to "bring end-to-end encryption capabilities to online meetings later."  





#### Tags:
[[E2EE]] [[Teams]] [[Microsoft]] [[users.]] [[ZDNet]]
