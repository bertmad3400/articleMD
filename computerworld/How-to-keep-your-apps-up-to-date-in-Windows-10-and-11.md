# How to keep your apps up to date in Windows 10 and 11
### With dozens of applications installed on the typical Windows PC, keeping them all updated seems like a Herculean task. Automated tools can lighten the load considerably.

## Information:
+ Source: Computerworld
+ Link: https://www.computerworld.com/article/3646415/how-to-keep-your-apps-up-to-date-in-windows-10-and-11.html
+ Date: 2022-01-19T03:00-05:00
+ Author: Ed Tittel


## Article:
![Article Image](https://images.idgesg.net/images/article/2020/08/hand_activates_software_update_button_in_virtual_interface_development_update_patch_fix_by_ra2studio_gettyimages-1220938772_2400x1600-100854508-large.jpg?auto=webp&quality=85,70)

Look around a typical Windows desktop. Whether it’s running Windows 10 or 11, chances are that it’s running at least a couple of dozen Windows applications (.exe files), and at least four dozen Microsoft Store apps. On my local fleet of 10 PCs, the range for applications is from a low of 24 to a high of 120; for Store apps, it ranges from 49 to 81. Such numbers are quite typical, if my online research is at all accurate.

In general, it’s considered good security practice to keep apps and applications up-to-date. Why? Because many updates involve security patches and fixes that block potential attacks and prevent unauthorized and unwanted access to applications and their data (and sometimes, the host OS and the PCs they run on). In this story, I will offer some tools to help you streamline this process, along with some instructions on how to put them to work to help you keep your apps and applications current and safe.

ADVERTISEMENTCounting what you’ve got
------------------------

First, it’s helpful to understand just how many apps you have installed. For Windows 10 and 11, there are two ways to get a handle on a PC’s application count, including both .exe applications and Store apps. The first method is to press **Windows key + R** to launch the Windows Run box, then type **ms-settings:appsfeatures** into the box. This opens the Settings app’s “Apps & features” pane, which provides a count of all executables on the target PC.

Figure 1 shows the output from my production desktop which is heavily populated with apps and applications (201 in all, in fact):

![keep win apps updated 01 apps features](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-01-apps-features-100915824-orig.jpg?auto=webp&quality=85,70)
The second method uses File Explorer to count subfolders in the Windows Apps hierarchy, which includes built-in Windows tools and utilities, plus items from the Program Files and Program Files (x86) folders. Inside the Run box, type **shell:AppsFolder**. This produces a File Explorer window with a total count field at the lower left corner, as shown in Figure 2.

[![keep win apps updated 02 apps folder](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-02-apps-folder-100915826-orig.jpg?auto=webp&quality=85,70)](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-02-apps-folder-100915826-orig.jpg?auto=webp&quality=85,70 "<div class='credit'>IDG</div>
<p>Figure 2: Note the item count at lower left (329) is considerably higher than the Figure 1 count. (Click image to enlarge it.)</p>
")
When you stop to consider that somebody has to keep all these applications up to date, somehow, these numbers can seem daunting.

Do you really need to manage all this stuff on your own?
--------------------------------------------------------

Fortunately, the answer to this question is a solid “No.” In this story, I describe and explain multiple sources of automated relief that should lighten this load considerably. “By how much?” is the inevitable follow-up question. In my own experience, using the tools described here means that I seldom have to update more than a handful of applications manually at any given time. Once you learn how to do this, it’s really quite routine.

Two major, Microsoft-supplied facilities will handle much of the work involved in keeping applications up to date on your behalf. Windows Update (WU) automatically handles Windows updates, which covers the tools and utilities included along with the Windows OS. But WU can also keep an eye on device drivers and Microsoft applications (such as Word, Excel, Teams, and so forth) and keep those up to date as well. See “[How to handle Windows 10 and 11 updates](https://www.computerworld.com/article/3014600/how-to-handle-windows-10-and-11-updates.html)” for details on using Windows Update.

Then there’s the Microsoft Store. It, too, keeps an eye on all the apps under its purview. It will update them daily by default. And you can visit the Library and click the *Get updates* button any time you like, to force pending updates to be applied to your PC. This button is shown on the upper right in Figure 3.

[![keep win apps updated 03 ms store library](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-03-ms-store-library-100915825-orig.jpg?auto=webp&quality=85,70)](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-03-ms-store-library-100915825-orig.jpg?auto=webp&quality=85,70 "<div class='credit'>IDG</div>
<p>Figure 3: Microsoft Store updates apps daily as a background task, but if you click <em>Get updates</em>, you can update any time you like. (Click image to enlarge it.)</p>
")
Setting aside the items handled by Windows Update and the Microsoft Store updater, then, the actual number of applications that I must track and update on my Windows 10 and 11 PCs usually varies between two dozen and just over sixty, depending on the individual PC.

ADVERTISEMENTNext, I’ll explain what’s involved in keeping an application up to date before I introduce a pair of powerful shortcuts to expedite that process.

A general application update approach
-------------------------------------

In principle, it’s dead simple to decide if a Windows application needs an update. It requires checking the installed application version number on your PC against the current or most recent version number for that application available from its maker. If the number on your PC matches the one from the maker, it’s current and needs no update. If it’s not a match, you’ll need to download the current version and update or install it on your PC to make it current.

**Note**: In some cases, you may be running a version number on your PC that’s higher than the one labeled as current, latest, or most recent by its maker. This can happen when you decide to install a preview or beta version of software on a PC. In that case, you must check the release number for the maker’s beta or preview releases instead of the general production releases.

Simple it may be, but manually checking version numbers for a few dozen apps — and then downloading and installing those that need updating — is a fool’s game. There’s a better way.

ADVERTISEMENTA potent tandem of free update check tools
------------------------------------------

The two programs I introduce below automate the process of checking application version numbers and installing any necessary updates. If you search the internet for “Windows software updater” or “Windows patching software,” you can find dozens of such tools available. Some of them are free, others come in both free and for-a-fee versions, and still more are available only to those willing to pay to use them. For more information on what’s available in general in this vein, check out *Lifehacker*’s “[Five Best Software Update Tools](https://lifehacker.com/five-best-software-update-tools-5384140)” or Innovana’s “[14 Best Free Software Updater Programs](https://blogs.innovanathinklabs.com/best-software-updater-windows-pc/).”

There are lots of options to choose from, so if you decide you don’t like what I’m about to lead you through after some hands-on experience, do please check these lists (and possibly others) to see if you can find similar tools more to your liking. The basic concept is to find one or more update tools that will take the bulk of the application update load off your shoulders and do that work for you.

### Option 1: Patch My PC Updater

[Patch My PC Updater](https://patchmypc.com/home-updater) is a freeware tool for individual users that comes from enterprise patch-management software vendor Patch My PC. It recognizes and automatically handles updates for around 300 different Windows applications. It does so automatically, quickly, and with minimal muss and fuss. I’ve used this tool for nearly six years now and it does the job both nicely and well.

Figure 4 shows the home screen, which tells me that I need to update my copy of TreeSize Free to the current version. Otherwise, 27 out of 28 apps that Patch My PC tracks are up to date.

[![keep win apps updated 04 patchmypc](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-04-patchmypc-100915827-orig.jpg?auto=webp&quality=85,70)](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-04-patchmypc-100915827-orig.jpg?auto=webp&quality=85,70 "<div class='credit'>IDG</div>
<p>Figure 4: Items in red, such as TreeSize Free at top of list, need updates. (Click image to enlarge it.)</p>
")
Simply click the *Perform <n> Updates* button at the lower right to instruct Patch My PC to download and update outdated apps; it does everything else automatically. That’s why I’ve learned to enjoy and appreciate this program.

Why then, must I recommend a second tool? A look at that tool’s output in Figure 5 below shows what’s at work: application coverage.

ADVERTISEMENT### Option 2: Software Update Monitor (SUMo) free version

[SUMo](https://www.kcsoftwares.com/?sumo) comes from French developer Kyle Katarn, a principal at software maker KC Softwares. This tool is good at tracking update status for a large number of programs (400+ or so).

[![keep win apps updated 05 sumo1](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-05-sumo1-100915828-medium.jpg?auto=webp&quality=85,70)](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-05-sumo1-100915828-orig.jpg?auto=webp&quality=85,70 "<div class='credit'>IDG</div>
<p>Figure 5: Where Patch My PC “sees” 28 applications on my PC, SUMo sees 60. (Click image to enlarge it.)</p>
")
As you can see in Figure 5, where Patch My PC tracks 28 apps on my production PC, SUMo follows 60. This is useful information.

The free version of SUMo does application tracking only, and leaves updates to its users to handle. The fee-based version of SUMo (approximately US$34 for a lifetime license) turns out to be something of a hit-or-miss proposition when it comes to automating the update process. For 80% of the programs it tracks, it handles updates automatically and completely. For the other 20%, the program stalls out at the maker’s website, from whence users must continue to manually find and apply relevant updates on their own.

ADVERTISEMENTI can’t recommend the for-a-fee version because I firmly believe it should automate everything. But I do find the free version quite useful, because it shows me what I must track down on my own and update manually.

ADVERTISEMENTThe programs that appear at the top of Figure 5 are informative and illustrative because they permit me to explain how best to work with the items in need of update. Those items include:

* Dropbox
* Microsoft Edge
* MiniTool Partition Wizard (MTPW)
* PowerShell
* SIW (Software Information for Windows)
* Zoom

Of those programs, all include some kind of built-in update facility. In fact, I can open Edge, MTPW, SIW and Zoom and run built-in updaters from their GUIs quickly and easily. PowerShell updates when you enter the string iex "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI" in an administrative session. And if Dropbox doesn’t auto-update on its own (on this PC, sometimes it does and sometimes it doesn’t), you can visit its [download page](https://www.dropbox.com/downloading) to grab a fresh, current copy of the installer and run that to bring the program up to date.

ADVERTISEMENTAn abbreviated rendition of the resulting SUMo update scan appears in Figure 6.

[![keep win apps updated 06 sumo2](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-06-sumo2-100915829-orig.jpg?auto=webp&quality=85,70)](https://images.idgesg.net/images/article/2022/01/keep-win-apps-updated-06-sumo2-100915829-orig.jpg?auto=webp&quality=85,70 "<div class='credit'>IDG</div>
<p>Figure 6: Dropbox now shows as up to date, and there are 0 minor and 0 major out-of-date items. (Click image to enlarge it.)</p>
")
Once you learn how to work from SUMo data, getting things updated becomes routine.

ADVERTISEMENTOne more thing: sometimes update tools will point at versions you won’t be able to find, or that come from dodgy update sites. (Don’t install those.) At other times, they’ll point to pre-release or preview versions you may not want to install. My advice: don’t obsess over such things. As long as most of your applications are current, one or two left-behinds won’t kill you — or your PC.

Learn to work with your tools, but don’t spend too much time trying to cover everything to the last jot and tittle. That way lies lost productivity, if not madness! But if you follow a regular update routine — about once a month is good — you can keep your stable of Windows applications current, and your PC(s) humming along. Cheers!

ADVERTISEMENT



## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=at]] [[action.malware.name=Conti]] [[action.malware.name=Elise]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=PS1]] [[action.malware.name=PS1]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]] [[action.malware.name=Zen]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Apps]] [[Microsoft]] [[Pcs]] [[Built-in]] [[Computerworld]]
#### urls
https://aka.ms/install-powershell.ps1)

