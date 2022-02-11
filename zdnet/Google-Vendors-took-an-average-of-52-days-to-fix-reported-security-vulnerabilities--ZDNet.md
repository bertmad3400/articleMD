# Google: Vendors took an average of 52 days to fix reported security vulnerabilities | ZDNet
### Microsoft, Apple and Google account for 65% of the bugs discovered.

## Information:
+ Source: ZDNet
+ Link: https://www.zdnet.com/article/google-vendors-took-an-average-of-52-days-to-fix-reported-security-vulnerabilities/
+ Date: 2022-02-11 18:45:12
+ Author: Jonathan Greig


## Article:
![Article Image](https://www.zdnet.com/a/img/resize/67d27d961115997e4b10630c2002376d61adf4e1/2021/06/23/28d7c4cd-05e5-42e2-854f-f3989e016aec/gettyimages-1317337924.jpg?width=770&height=578&fit=crop&auto=webp)

Google's Project Zero [released](https://googleprojectzero.blogspot.com/2022/02/a-walk-through-project-zero-metrics.html) a report covering its work in 2021, finding that vendors took an average of 52 days to fix reported security vulnerabilities.

Between 2019 and 2021, Project Zero researchers reported [376 issues](https://bugs.chromium.org/p/project-zero/issues/list?sort=id&colspec=ID%20Status%20Restrict%20Finder%20Reported%20Deadline%20Remaining%20CVE%20Vendor%20Product%20Summary&q=status%21%3DInvalid%20id%3E%3D1748%20id%3C%3D2248%20Deadline%3A90&can=1) to vendors under their 90-day deadline. 

Of those 376 issues, more than 93% of these bugs have been fixed and over 3% have been marked as "WontFix" by the vendors, according to Project Zero. 

The researchers added that 11 other bugs remain unfixed and 8 have passed their deadline to be fixed. Microsoft, Apple and Google account for 65% of the bugs discovered. Microsoft led the way with 96 bugs, followed by 85 from Apple and 60 from Google.

"Overall, the data show that almost all of the big vendors here are coming in under 90 days, on average. The bulk of fixes during a grace period come from Apple and Microsoft (22 out of 34 total). Vendors have exceeded the deadline and grace period about 5% of the time over this period," Project Zero researchers said. 

"In this slice, Oracle has exceeded at the highest rate, but admittedly with a relatively small sample size of only about 7 bugs. The next-highest rate is Microsoft, having exceeded 4 of their 80 deadlines. Average number of days to fix bugs across all vendors is 61 days."

![screen-shot-2022-02-11-at-1-04-28-pm.png]()![screen-shot-2022-02-11-at-1-04-28-pm.png](https://www.zdnet.com/a/img/resize/6fe3f0085753114aadf0375e8bb3173a489feefb/2022/02/11/d533be0c-4964-4597-a02b-0ef4fafeb874/screen-shot-2022-02-11-at-1-04-28-pm.png?width=470&fit=bounds&format=pjpg&auto=webp)
 Google
 Google also provided other statistics showing that the overall time to fix has consistently been decreasing, particularly for vendors like Microsoft, Apple and Linux. All three reduced their time to fix between 2019 and 2020 while Google sped up in 2020 and slowed down again in 2021. 






In 2021, they noted that [only one 90-day deadline](https://bugs.chromium.org/p/project-zero/issues/list?colspec=ID%20Status%20Restrict%20Finder%20Reported%20Deadline%20Remaining%20CVE%20Vendor%20Product%20Summary&q=id%3E%3D2137%20Deadline%3DExceeded%20-Deadline-Grace&can=1) was exceeded, a stark decrease compared to the average of 9 per year in the other two years. The researchers added that the grace period was used 9 times -- with half being by Microsoft -- versus the slightly lower average of 12.5 in the other years.

When it comes to mobile vulnerabilities, iOS devices had 76 total bugs, followed by 10 for Samsung Android devices and 6 for Pixel Androids. 

For browsers, Chrome had 40 bugs and an average time to patch of 5.3 days. WebKit had 27 bugs and an 11.6-day average time to patch while Firefox had 8 bugs and a 16.6-day average time to fix.

"Chrome is currently the fastest of the three browsers, with time from bug report to releasing a fix in the stable channel in 30 days. Firefox comes in second in this analysis, though with a relatively small number of data points to analyze. Firefox releases a fix on average in 38 days," the researchers said.

"WebKit is the outlier in this analysis, with the longest number of days to release a patch at 73 days. Their time to land the fix publicly is in the middle between Chrome and Firefox, but unfortunately this leaves a very long amount of time for opportunistic attackers to find the patch and exploit it prior to the fix being made available to users."

Project Zero said the findings were a positive development, showing that many vendors are fixing most of the bugs they find. Vendors are also moving faster to rectify issues, with Google attributing it to responsible disclosure policies that have become the standard in the industry.

Google urged all vendors to focus on a "more frequent patch cadence for security issues."

"We encourage all vendors to consider publishing aggregate data on their time-to-fix and time-to-patch for externally reported vulnerabilities. Through more transparency, information sharing, and collaboration across the industry, we believe we can learn from each other's best practices, better understand existing difficulties and hopefully make the internet a safer place for all," Project Zero said.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=Reg]]

#### Location:
[[victim.city.name=Tunis]] [[victim.country.name=Tunisia]] [[victim.continent.name=Africa]] [[victim.city.name=Rome]] [[victim.country.name=Italy]] [[victim.continent.name=Europe]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Google]] [[Microsoft]] [[Firefox]] [[ZDNet]]

