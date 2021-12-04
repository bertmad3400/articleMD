# Microsoft shares fix for broken Outlook search in Windows 11
### Microsoft has shared a solution for Outlook users who have been experiencing search issues after upgrading to Windows 11.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-shares-fix-for-broken-outlook-search-in-windows-11/
+ Date: 2021-12-04T11:14:07-05:00
+ Author: Sergiu Gatlan


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/05/11/outlook-header-image.jpg)

![Microsoft shares fix for broken Outlook search in Windows 11](https://www.bleepstatic.com/content/hl-images/2021/05/11/outlook-header-image.jpg)


Microsoft has shared a solution for Outlook users who have been experiencing search issues after upgrading to Windows 11.


These problems started showing up around June when the first official and unofficial Windows 11 preview builds surfaced.


As those affected said, Outlook stopped showing results [[1](http://twitter.com/nematombo/status/1409877346698530818), [2](https://techcommunity.microsoft.com/t5/outlook/outlook-2007-search-on-windows-11-fails-by-returning-no-results/m-p/2769140)] when searching for specific emails [on IMAP/POP accounts](https://twitter.com/HarryCann/status/1454012994816446466), in some cases [resulting in the app completely freezing](https://twitter.com/alxcia/status/1406190070751805441).


"This issue will happen with any account where the emails and other items are stored locally in PST or OST files such as POP and IMAP accounts," Microsoft [says](https://support.microsoft.com/en-us/office/outlook-search-does-not-return-results-after-upgrade-to-windows-11-cc54dfee-ee78-4123-a9af-7986748052ef) on its list of recent issues impacting Outlook for PC.


"For Exchange and Microsoft 365 hosted accounts, this issue will affect offline search for the data in the locally stored OST files."


According to Redmond, these issues impact Outlook for Microsoft 365, Outlook 2019, and Outlook 2016. Per Microsoft, the root cause is the Windows search index being deleted during the upgrade, which breaks search until it gets rebuilt.


To ensure that the index rebuilding process is still ongoing, you can check the current status by going to the Search box, selecting Search Tools, and then choosing Indexing Status on the ribbon.


How to fix broken Outlook search in Windows 11
----------------------------------------------


If the indexing is still active and takes too long, you can fix Outlook search not returning any results by setting a registry key that disables Windows Desktop Search and tells Outlook to use its built-in search.


Once Outlook's own search engine kicks in, the following message is displayed as an indication that search performance is affected: "Search performance will be impacted because a group policy has turned off the Windows Search service."


To disable the Windows Desktop Search Service for Outlook you have to go through the following steps:


1. In Windows, right-click **Start**, and then select **Run**. In the **Open:** box type **regedit**, and then click **OK**. This will open the registry editor.
2. Find this subkey in the registry and then click it:


	* HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows
3. Click **Edit** > **New** > **Key**, and name the new key **Windows Search**.
4. Select the new **Windows Search** key.
5. Click **Edit** > **New** > **DWORD Value**.
6. Type PreventIndexingOutlook for the name of the DWORD, and then press Enter.
7. Right-click PreventIndexingOutlook, and then click **Modify**.
8. In the Value data box, type 1 to enable the registry entry, and then click **OK**.
9. Exit Registry Editor, and then restart Outlook.

If you want to re-enable the Windows Desktop Search, you need to disable the PreventIndexingOutlook setting by typing 0 (zero) and clicking **OK**.


Microsoft has also recently provided workarounds for a handful of other Outlook issues, including:


* [Search results for Find Related Messages in Conversation are incomplete or missing](https://support.microsoft.com/en-us/office/search-results-for-find-related-messages-in-conversation-are-incomplete-or-missing-26d8d3a8-26a2-4523-90ba-acb51176b7ae)
* [Conflicts in Outlook task](https://support.microsoft.com/en-us/office/conflicts-in-outlook-task-fff8768c-8724-4ef4-bed9-ef7dea15841d)
* [Outlook cannot add guest groups in Microsoft 365](https://support.microsoft.com/en-us/office/outlook-cannot-add-guest-groups-in-microsoft-365-eb30bd35-0b9a-4570-9dd3-667f1a216f90)
* [Hosted applications in Outlook error: We can't open the Teams App right now. Please try again later](https://support.microsoft.com/en-us/office/hosted-applications-in-outlook-error-we-can-t-open-the-teams-app-right-now-please-try-again-later-743c072d-fad6-4e74-aead-75a879786daa)




## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Location:
[[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Windows]] [[Microsoft]] [[Preventindexingoutlook]] [[Bleeping Computer]]

