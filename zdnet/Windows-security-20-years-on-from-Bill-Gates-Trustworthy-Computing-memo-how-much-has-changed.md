# Windows security: 20 years on from Bill Gates' Trustworthy Computing memo, how much has changed?
### Windows security has changed a lot in 20 years - but so have the groups that want to attack it.

## Information:
+ Source: ZDNet
+ Link: [article](https://www.zdnet.com/article/windows-security-20-years-on-from-bill-gates-trustworthy-computing-memo-how-much-has-changed/)
+ Date: October 14, 2021
+ Author: Liam Tung


## Article:
Unknown

It's almost 20 years since then-Microsoft boss Bill Gates [wrote his famous Trustworthy Computing memo](https://www.zdnet.com/article/10-years-since-the-bill-gates-security-memo-a-personal-journey/), in which he urged the company to produce more secure software. 

"Eventually, our software should be so fundamentally secure that customers never even worry about it," [wrote Gates](https://www.wired.com/2002/01/bill-gates-trustworthy-computing/). It's a grand ambition, and despite years of work, it is not one that any software has really achieved yet. And even as engineers try to improve their products, a new wave of security threats have appeared.


"I think it was hard for anyone at the time – even in Bill Gates' grand vision – to see we would have sophisticated state-sponsored hackers [breaking those SWIFT banking system codes](https://www.zdnet.com/article/money-from-bank-hacks-rarely-gets-laundered-through-cryptocurrencies/), people flattening oil production by wiping hard-drives. The threat landscape is beyond any science fiction novel or what John le Carré could predict," says Dave Weston, Microsoft's director of enterprise and Windows security.  

**SEE:** [**Windows 11 upgrade: Five questions to ask first**](https://www.zdnet.com/article/windows-11-upgrade-five-questions-to-ask-first/)

He admits that, as a "hardened industry professional", he is surprised by the sophistication of attacks today. 

"The breadth and sophistication [of these attacks] is what continues to make this job interesting. There is never a dull moment here," he says.

"Fifteen years ago we were thinking of these attackers as basically script kiddies – people sitting in their parents' basements on the weekend doing things for mischievous reasons. That was the archetype 15 years ago. The archetype now is somebody who is working in the military-industrial complex, who works in an office." That's a pretty stark contrast, Weston points out.






"If we're up against that, are we in a better position? I would say, unequivocally, yes. Twenty years ago, the price of an exploit was cheap. Now when you're talking about Windows 10 or 11, or browsers, you're talking millions of dollars to acquire an exploit."

The difference between those two points is the level of defenses in the operating system, he argues. "The reality is today that there are a smaller number of people who today can attack a Windows PC than there was 10 or 15 years ago and I think that in itself is a triumph."     

That increasing threat level is one issue, while the tech security goalposts themselves have also been changing rapidly. 

Back in 2002 when Gates wrote his memo, the focus of security was all about the software: he didn't even mention hardware or CPUs. Today, with an [uptick in zero-day exploits](https://www.zdnet.com/article/google-just-patched-these-two-chrome-zero-day-bugs-that-are-under-attack-right-now/), [CPU attacks like Meltdown/Spectre](https://www.zdnet.com/article/google-this-spectre-proof-of-concept-shows-how-dangerous-these-attacks-can-be/) and more, [Windows security is much more concerned with hardware](https://www.zdnet.com/article/windows-11-microsoft-stands-firm-on-hardware-requirements/).    

For example, in Windows 10 and Windows 11, Microsoft has brought in Control Enforcement Technology (CET), [a security mitigation it co-developed with Intel](https://www.zdnet.com/article/google-chrome-this-new-feature-makes-it-tougher-for-hackers-to-attack-windows-10-pcs/). CET is an on-chip technology that targets some of the most common attack vectors, such as return oriented programming, says Weston. It's available on Intel 11th Gen or AMD Zen 3 CPUs.

Virtualization-based security, dubbed VBS at Redmond, restricts techniques used in [the WannaCry ransomware attack](https://www.zdnet.com/article/microsoft-warns-of-destructive-cyberattacks-issues-new-windows-xp-patches/) by hardening the Windows kernel. 

Windows 11 also promises to make the goal of 'Zero Trust' – the concept of borderless networks that [the Biden White House is pushing](https://www.zdnet.com/article/biden-signs-order-boosting-us-cyber-posture-saying-incremental-improvements-are-not-enough/#link=%7B%22role%22:%22standard%22,%22href%22:%22https://www.zdnet.com/article/biden-signs-order-boosting-us-cyber-posture-saying-incremental-improvements-are-not-enough/%22,%22target%22:%22%22,%22absolute%22:%22%22,%22linkText%22:%22the%20Biden%20White%20House%20is%20pushing%22%7D) – easier by reducing the amount of configuration required for Windows endpoints.

But, as Weston highlights, organizations will need to run some numbers to figure out whether to upgrade hardware and migrate to Windows 11 versus reconfiguring PCs and servers that only cut it for Windows 10. On Windows 11, admins don't need much to configure that security; with Windows 10 they can create the same level of security – but with a bit more work.

Organizations that adopt Zero Trust assume their perimeter has already been breached. It also recognizes that data needs to be protected within and outside the network on corporate-issued and employee-owned devices. Zero Trust has became more pertinent after the pandemic forced many more people to remote working.

Weston, however, contends that Windows 11 does make it easier for businesses, assuming they have new hardware suitable for it. 

"Where the hardware fits in, we've been working to make sure things can be turned on by default when you meet the hardware baseline. We're expecting a certain level of performance and reliability from recent drivers and hardware pieces. That allows us to turn on more, by default, with confidence. That's where the hardware piece fits in with Zero Trust," he says. 


But will customers be left behind because of hardware? 

"The answer is firmly 'no'," insists Weston. 

**SEE:** [**Microsoft's Windows 11: How to get it now (or later)**](https://www.zdnet.com/article/microsofts-windows-11-how-to-get-it-now-or-later/)

Even if organisations want to stay with Windows 10, many of those features like Windows Hello, Virtualization Based Security and Secure Boot are still available, he says – you've just got to turn it on and evaluate your own environment.

"If you've got the hardware, you can install Windows 11, things are simple. If you don't have that hardware or that's something you're planning for the future, you can still partake in all of these security baselines by taking our free security baseline and apply that to Windows 10-level hardware. You may have to do some initial analysis on performance trade-offs, which makes it a little more difficult, but you can certainly get there."

Microsoft has set October 14, 2025 for the end of Windows 10 patches. Weston reckons you can still configure Windows 10 to meet Windows 11 standards, and he optimistically bets that most organizations should have refreshed most of their hardware by 2025.    

"By 2025, when the refresh cycle will have turned over for the vast majority of the businesses, you will have more reason to move to Windows 11 because by that point there will have been two or three releases of security goodness to have been added, which we think is going to provide a substantial value proposition," he says.

"My advice would be: if you need to stay on Windows 10 for hardware reasons, great; follow our security guidance from 11 and apply that to 10. Plan in your refresh cycles and security budgets to get the right hardware to get to 11 because, if you stay on 10 for too long, we will start to introduce things that are 11-specific – trust me, we have many on the way now – and we want as many customers as possible to get that value. It's very similar to the transition we went through from Windows 7 to 10: there's security goodness if you can get there." 





#### Tags:
[[Windows]] [[Microsoft]] [["The]] [[Weston]] [[ZDNet]]
