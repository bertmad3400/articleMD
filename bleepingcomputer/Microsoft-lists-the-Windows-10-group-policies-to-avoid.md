# Microsoft lists the Windows 10 group policies to avoid
### Microsoft released a list of twenty-five group policies that admins should not use in Windows 10 and Windows 11 as they do not provide optimal behavior or cause unexpected results.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-lists-the-windows-10-group-policies-to-avoid/
+ Date: 2022-01-20T17:53:34-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/01/25/Windows-10.jpg)

![Windows 10](https://www.bleepstatic.com/content/hl-images/2021/01/25/Windows-10.jpg)


Microsoft released a list of twenty-five group policies that admins should not use in Windows 10 and Windows 11 as they do not provide optimal behavior or cause unexpected results.


Since Windows 10, version 1511, was released in November 2015, Microsoft has continued to evolve the operating system based on customer feedback, security improvements, new features, and general optimizations.


However, this left behind a confusing mess of group policies that no longer work properly, cause unexpected behavior, or are superseded by new policies that provide a better performance and user experience.


Windows Senior Program Manager Aria Carley hinted in December warned admins that admins should avoid using various group policies in Windows 10 and Windows 11.



> 
> Homework assignment: Confirm that NONE of these legacy Windows Update policies are set on your [#Windows10](https://twitter.com/hashtag/Windows10?src=hash&ref_src=twsrc%5Etfw) or [#Windows11](https://twitter.com/hashtag/Windows11?src=hash&ref_src=twsrc%5Etfw) devices.  
>   
> 
> Folks who complete the assignment will get a better update experience and an A+ Gif! [pic.twitter.com/N1J1af53BF](https://t.co/N1J1af53BF)
> 
> 
> — ariaupdated (@ariaupdated) [December 10, 2021](https://twitter.com/ariaupdated/status/1469312511640018945?ref_src=twsrc%5Etfw)


Yesterday, Carley published an article on the Windows IT Pro Blog going into further detail about what policies should not be used, why admins shouldn't use them, and what they have been replaced with.


"We have listened to your feedback and learned a lot about which experiences work and which don't. We have also worked to evolve and simplify the controls needed to support these improved experiences, and identify which older policies have become irrelevant or replaced with a better option," Carley explained in a new [Windows IT Pro article](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/why-you-shouldn-t-set-these-25-windows-policies/ba-p/3066178).


"As a result, the Windows update policy set contains policies that no longer have any impact; that don't work as described on devices running Windows 10, version 20H2 or later; or that work but not as well as the policies that were added to accomplish a similar experience in a much better way."


This list is invaluable for Windows admins to review their existing group policy configurations and replace outdated policies with newer variants that provide more control and expected behavior.


Carly also explained that Microsoft made it easier to distinguish the deprecated policies that should no longer be used in Windows 11 with a new **Legacy Policies** folder under the **Windows Update** policies in the Group Policy Editor.



![Legacy Policies folder in Windows 11](https://www.bleepstatic.com/images/news/Microsoft/windows-11/l/legacy-policies/legacy-policies.jpg)**Legacy Policies folder in Windows 11**
Admins can find the complete list of deprecated policies and suggested replacements [in Microsoft's article](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/why-you-shouldn-t-set-these-25-windows-policies/ba-p/3066178).


In addition to avoiding these policies, Microsoft also warned this week that admins would need to decide if they wish to use the Windows 10 or Windows 11 ADMX files on their Active Directory's Central Store.


"So what to do if you have a mixed environment of both client operating systems? Well, fact is that you can only copy one set of ADMX files to your Active Directory's Central Store. Depending on what your future plans are, you should decide which templates fit best," explained Helmut Wagensonner, a Customer Engineer at Microsoft.


"If you plan to stay on Windows 10 for a while, you should choose the Windows 10 ADMX files. If you're ready to upgrade to Windows 11 and this will become your dominating OS version (or it already is), you should copy the Windows 11 ADMX files to your Central Store."


While admins need to select an OS-specific set of ADMX files for the central store, [Wagensonner provided a method](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/windows-10-or-windows-11-gpo-admx-which-one-to-use-for-your/ba-p/3063322) that admins can use to manage the policies for the other operating systems in their environment.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=njRAT]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Admins]] [[Microsoft]] [[Admx]] [[Carley]] [[Bleeping Computer]]

