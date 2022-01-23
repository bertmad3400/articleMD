# Microsoft tests a new Rejuvenated Windows 11 Task Manager, how to enable
### Microsoft is testing a new hidden feature in the latest Windows 11 preview build that rejuvenates the user interface for Task Manager with a new design and modern appearance.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-tests-a-new-rejuvenated-windows-11-task-manager-how-to-enable/
+ Date: 2022-01-23T12:31:55-05:00
+ Author: Lawrence Abrams


## Article:
![Article Image](https://www.bleepstatic.com/content/posts/2022/01/rejuvenated-task-manager-header.jpg)

![New Windows Task Manager](https://www.bleepstatic.com/content/posts/2022/01/rejuvenated-task-manager-header.jpg)


Microsoft is testing a new hidden feature in the latest Windows 11 preview build that rejuvenates the user interface for Task Manager with a new design and modern appearance.


Task Manager is one of the most commonly used built-in Windows apps, allowing users to see how much a process uses CPU and memory, terminate processes, manage auto-starting programs, or simply see what programs are running on a computer.


However, other than a [few tweaks and small changes](https://www.bleepingcomputer.com/news/microsoft/windows-10-insider-build-16226-adds-gpu-performance-to-task-manager/), the Windows Task Manager has remained relatively unchanged since Windows 10 was released.


The new "Rujuvenated" Task Manager
----------------------------------


Last week, Microsoft released Windows 11 preview build 22538 to the 'Developer' channel, and it includes a new hidden feature called 'TaskManagerRejuvenated' that introduces a revamped user interface for the Windows Task Manager.


Discovered by Windows developer [Gustave Monce](https://twitter.com/gus33000), enabling the feature does not add any new functionality to the program.


Like the current version of Task Manager, the "rejuvenated" version still contains the same information screens, such as Processes, Performance, App history, Startup apps, Users, Details, and services.


However, Task Manager now uses an app-like user interface with a sidebar menu for selecting screens rather than the usual tabbed sections.



![New rejuvenated Windows 11 Task Manager](https://www.bleepstatic.com/images/news/Microsoft/windows-11/t/task-manager/hidden-task-manager-redesign/without-hero-control.jpg)**New rejuvenated Windows 11 Task Manager**
In addition, Microsoft is testing a new 'hero element' feature that displays a pinned section at the top of the Task Manager that displays the computer's name, its model, and the current resources being used, as shown below.



![New hero element in Windows Task Manager](https://www.bleepstatic.com/images/news/Microsoft/windows-11/t/task-manager/hidden-task-manager-redesign/with-hero.jpg)**New hero element in Windows Task Manager**
The new hero feature is currently static, meaning that it will display the same 'Surface Pro 8' information regardless of the device the new version is running on.


While not filled with exciting new features, it is good to see Microsoft update older user interface elements with the new modern feel of Windows 11.


How to enable the new Task Manager in Windows 11
------------------------------------------------


If you wish to test out the new Windows 11 Task Manager, you can join the Windows Insider programs and install the current Windows 11 build (build 22538) or later.


To get this build, you will need to join the 'Dev' channel of the Windows Insider program.


Once the latest Windows 11 insider build is installed, please follow these steps to enable the new Task Manager:


1. [Download ViveTool](https://github.com/thebookisclosed/ViVe/releases/tag/v0.2.1), which enables hidden developer features in Windows 10 and Windows 11. Once downloaded, extract the zip file.
2. Open an [Elevated Command prompt](https://www.bleepingcomputer.com/tutorials/how-to-open-a-windows-10-elevated-command-prompt/) and navigate to the folder you extracted ViveTool.
3. Now type and enter each of these commands. Not all of them are necessary, but all are part of this new feature.

```
vivetool addconfig 35908098 2
```

If you also want to enable the test 'Hero element,' you should enter the following command. It is important to remember that the hero element is filled with fake data at this point.



```
vivetool addconfig 36898195 2
```

Finally, to add Dark Mode support to the new Task Manager, enter the following command:



```
vivetool addconfig 37204171 2
```

After entering each command, ViveTool will respond with "Successfully set feature configuration," as shown below. 



![Using ViveTool to enable new Task Manager skin](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Using ViveTool to enable new Task Manager skin**
4. After enabling each configuration, make sure to close any running instances of Task Manager and relaunch it to see the "Rejuvenated" version.

When done testing, you can disable new Task Manager feature by running the following ViveTool commands from an elevated command prompt.



```
vivetool addconfig 35908098 0
vivetool addconfig 36898195 0
vivetool addconfig 37204171 0
```

Once again, restart Task Manager to rever back to the original version.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Vivetool]] [[Addconfig]] [[Vivetool]] [[Microsoft]] [[Bleeping Computer]]

