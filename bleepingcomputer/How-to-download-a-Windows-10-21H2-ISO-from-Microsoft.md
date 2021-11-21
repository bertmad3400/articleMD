# How to download a Windows 10 21H2 ISO from Microsoft
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/microsoft/how-to-download-a-windows-10-21h2-iso-from-microsoft/)
+ Date: November 21, 2021
+ Author: Lawrence Abrams


## Article:
![Windows 10](https://www.bleepstatic.com/content/hl-images/2020/07/31/windows-10-mesh-header.jpg)


Microsoft released Windows 10 21H2, the November 2021 Update, last week and you can now download an ISO image for the new version to put aside for emergencies or clean installs.


Windows 10 21H2 is not a very large feature update and only contains a [few new features for business users](https://www.bleepingcomputer.com/news/microsoft/windows-10-21h2-is-released-here-are-the-new-features/) and increased protection against WiFi side-channel attacks.


However, if you plan on upgrading to the new version of Windows it is always recommended that you download or create an ISO to have on hand for troubleshooting problems or performing clean installs of Windows.


Why you should download an ISO image
------------------------------------


An ISO image is a sector-by-sector copy of a DVD or other media stored in a single file. As this file is a replica of the original media, it can then be written (burned) to another DVD or USB key in the same way it was created.


Using ISOs allows you to create backups of DVD and bootable media in the event that you lose the original media and need to recreate it. ISO images can also be [mounted as a drive letter in Windows](https://www.bleepingcomputer.com/tutorials/mount-an-iso-image-in-windows/) or virtual machines or extracted by programs like [7-Zip](https://www.7-zip.org/) to access the contained files.


ISO images are particularly handy for performing "clean" installations of Windows, which is a fresh install of the operating system without any of your previously installed programs, data, or configuration settings.


Finally, ISO images can be used to create bootable USB drives that can be used to access the Windows Recovery Environment if Windows does not boot properly, diagnose crashes, or remove a particularly stubborn malware infection.



![Windows 10 recovery environment](https://www.bleepstatic.com/images/news/Microsoft/Windows-10/iso/windows-10-21h2/windows-10-21h2-recovery-environment.jpg)**Windows 10 recovery environment**
Due to this, it is recommended that all users download the latest Windows 10 ISO as new feature updates are released.


How to download a Windows 10 21H2 ISO from Microsoft
----------------------------------------------------


To create a Windows 10 21H2 ISO, you can use two different methods.


The first and easiest method is to use the Media Creation Tool (MCT) to create the ISO. However, this takes longer as the tool needs to download files and convert them into an ISO.


Those who do not want to wait for the MCT to create the ISO can download it directly from Microsoft by tricking their site into thinking you are downloading from a mobile device.


Both of these methods are explained below.


### Method 1: Use the Media Creation Tool to create an ISO


Microsoft offers the Media Creation Tool that lets you download the latest Windows 10 ISO to a file or burn it to a bootable USB drive.


To download the Windows 10 21H2 ISO using the Media Creation Tool, please follow these steps:


1. Visit the [Windows 10 download page](https://www.microsoft.com/en-us/software-download/windows10ISO) using your web browser.
2. Under 'Create Windows 10 installation media,' click on the '**Download tool now**' link and save the offered 'MediaCreationTool21H2.exe' executable.
3. Once downloaded, run the MediaCreationTool21H2.exe, and Windows will prompt you for permission to allow it to run. Click **Yes,** and the Media Creation Tool will prepare a few things before it can proceed.
![MCT: Getting things ready](https://www.bleepstatic.com/images/news/Microsoft/i/latest-windows-10-iso/mct-preparing.jpg)
4. When done, the MCT will show you a license agreement. To continue, click on the **Accept** button.
5. The tool will now state it is 'Getting a few things ready,' and when done, display a prompt asking if you would like to upgrade the computer or 'Create installation media (USB flash drive, DVD, or ISO file) for another PC.
![What do you want to do?](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


At this prompt, select the **Create installation media** option and then press the **Next** button.
6. The Media Creation Tool will now download and verify the necessary files to create an ISO or a bootable USB drive. This process can take some time, so please be patient.
![Downloading Windows 10 files](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
7. When done, the MCT will ask what language, architecture, and Windows edition you want for your ISO image. By default, the MCT will use your local language and architecture, but you can uncheck **Use the recommended options for this PC** checkbox to select other options.  
  

When done, click on the **Next** button.
![Select language, architecture, and edition](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
8. You will now be asked if you wish to create a bootable USB drive or a Windows 10 ISO. As we are creating an ISO file, select the **ISO file** option and press **Next**. 
![Create a USB drive or ISO file](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
9. You will now be prompted to select a location to save your ISO file. Select a folder to save the ISO file to, and then click on the **Save** button.
10. The Media Creation Tool will now create the ISO file in the specified location. Please be patient while the file is created.
![Creating the ISO file](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
11. When the Media Creation Tool has finished creating the ISO, you can close the program by clicking on the **Finish**button.
![Windows 10 ISO created](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


You will now have the latest Windows 10 21H2 ISO image file saved to the selected folder, which can be used for virtual machines or to create bootable media later.


### Method 2: Trick Microsoft's download page into giving an ISO file


When you go to Microsoft's "[Download Windows 10](https://www.microsoft.com/en-us/software-download/windows10)" page, you are given the option to update via Windows Update or to download the Windows 10 Media Creation Tool.


Below, we will provide a method that tricks Microsoft into offering an ISO image file for Windows 10 21H2 instead.


To download the Windows 10 21H2 ISO, follow these steps:


1. Go to [Windows 10 download page](https://www.microsoft.com/en-us/software-download/windows10ISO) in Chrome or the new Microsoft Edge.
2. Click on the Chrome menu, then **More Tools,**and select **Developer tools,**as shown below.

![Open Google Chrome developer tools](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Open Google Chrome developer tools**
3. Now press **Ctrl + Shift + M** to open the Device toolbar. This toolbar lets you force Chrome to impersonate another device, such as a mobile phone or a tablet.  
  

Click on the menu that should show **Responsive** and select **iPad**or **iPad Pro** to have a larger screen to work with.
![Chrome emulation](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
4. When you select one of these devices, you should see the screen resize to reflect the size of the device's screen. At this point, I suggest you change the zoom to 100%, as shown below.
![Change zoom level](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
5. Now refresh the page in the browser by pressing the **F5** key. Once the page refreshes, Microsoft's site will now offer you the Windows 10 ISO instead of the Media Creation Tool.  
  

Now click on the drop-down arrow under 'Select edition' and select the '**Windows 10'** option under "Windows 10 November 2021 Update". Once selected, click on the **Confirm** button.

![Select Windows 10 November 2021 Update](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Select Windows 10 November 2021 Update**
6. After a few seconds, Microsoft's site will now ask you to select the language for your ISO.
![Select Language](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


Select your language and press the **Confirm** button again.
7. Finally, you will be asked to either download the 32-bit or 64-bit ISO. When ready, click on one of these choices, and your browser will download the respective Windows 21H2 ISO image.
![Select type](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)


Readers should note that the above instructions work in any Chromium-based browser, not only Chrome or the new Edge.




#### Tags:
[[Windows]] [[Microsoft]] [[21H2]] [[button.]] [[USB]] [[ISO.]] [[MCT]] [[done,]] [[DVD]] [[ISO,]] [[Bleeping Computer]]
