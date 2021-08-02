# Empty npm package '-' has over 700,000 downloads — here's why
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/software/empty-npm-package-has-over-700-000-downloads-heres-why/)
+ Date: August 2, 2021
+ Author: Ax Sharma


## Article:
![npm](https://www.bleepstatic.com/content/hl-images/2019/08/21/NPM.jpg)


A mysterious, one-letter npm package named "-" sitting on the registry since 2020 has received over 700,000 downloads.


What's more? The package contains no functional code, so what makes it score so many downloads?



Inside the npm package "-"
--------------------------


An npm package called "[-](https://www.npmjs.com/package/-)" has scored almost 720,000 downloads since its publication on the npm registry, since early 2020.


There's only one version of the package: 0.0.1 and it contains three files:


tar tvf 0.0.1/**-**-0.0.1.tgz  
  

package/dist/index.js  

package/package.json  

package/README.md
Inside these files—mainly the manifest (package.json) and index.js, there is nothing phenomenally interesting, just skeleton code.


The manifest does pull in a bunch of development dependencies *(devDependencies)* and invokes some commands on the "[ts-node](https://www.npmjs.com/package/ts-node)" component, but that's about it. It's practically dead code, for now:



![npm package contents](https://www.bleepstatic.com/images/news/u/1164866/2021/Aug-2021/npm-package-contents.jpg)**The index.js file and the manifest file (package.json) of "-"**(BleepingComputer)
"-" is used by over 50 packages
-------------------------------


It gets even better.


The practically useless package "-" serves as a dependency for over 50 npm packages, without a clear explanation:



![npm package - dependencies](https://www.bleepstatic.com/images/news/u/1164866/2021/Aug-2021/dash-package-dependencies.jpg)**npm package "-" is used by 56 packages**(npmjs.org)
But most of these dependencies have no more than a few dozen weekly downloads.


So, how is it that "-" has scored over 720,000 downloads?


It is plausible the package gets pulled in when someone is running npm commands from terminal, and makes typographical errors.


For example, to install an npm package called "somepackage," you'd have to run:


npm i somepackage
What if you were specifying a few flags, but made a mistake. For example:


npm i ***- someFlag*** somepackage
The space between the "-" and *someFlag* may cause npm to pull in "-" as the package with that name does exist.


It's therefore plausible that the package's thousandfold download counts are a result of developers making typos.


And similarly, when [adding dependencies to package.json](https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file#adding-dependencies-to-a-packagejson-file-from-the-command-line) via command-line, it isn't too hard too see how a "-" could slip in by error.


In a test, BleepingComputer, ran the following mistyped command, with the intention of downloading "[somepackage](https://www.npmjs.com/package/somepackage)" and "[axsharma](https://twitter.com/Ax_Sharma/status/1360311640621654016)" from npm.


But notice the typo, an extra "-" before the "--save" flag:


npm install somepackage axsharma - --save
Unsurprisingly, both the resulting file *package-lock.json* and the *node\_modules/* folder contained the "-" package, explaining how it could slip into your dependencies in the real world:



![generated package-lock.json](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**Generated node\_modules folder and package-lock.json file contain "-" package**(BleepingComputer)
BleepingComputer reached out to the package's author [Dmitry Parzhitsky](https://www.npmjs.com/~parzhitsky) with some questions, like, why was this package created. But, we haven't heard back.


The package's creation itself could be accidental or caused by a test script that finished prematurely.


Both the README.md file included within the package and the package's npm page indicate "-" was generated by a script:



![npm package - readme](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**README file for "-"**(BleepingComputer)
Suffice to say, while there is nothing right now in "-" that indicates it is malicious, we don't know what the next version of "-" could look like, should it be released.


Other examples of single-letter packages, or those resembling npm commands include, but aren't limited to: [i](https://www.npmjs.com/package/i), [g](https://www.npmjs.com/package/g), [install](https://www.npmjs.com/package/install), [D](https://www.npmjs.com/package/D), and [s](https://www.npmjs.com/package/s).


This means, typing "*npm i i somePackage"*by mistake, as opposed to "*npm i somePackage,"*will, in turn, install the *i* package, in addition to *somePackage*.


"The real issue here is that you can install these packages and never know it. Running *npm install - g my-package* will install the package you want."


"Only later on, when you try to access that package elsewhere will there be any indication that you made a typo. In the meantime, both *-* and *g* have been riding along in your project."


"npm could (and maybe should) disallow components that share names with its commands," software developer [Matt Freeland](https://www.linkedin.com/in/mtfreeland/) at Sonatype shared with BleepingComputer.


Freeland further expressed that once packages are installed, npm presents summarized success message such as, "added 3 packages, and audited 8 packages," rather than printing the exact list of packages installed.


"Naming the installed packages in the success message would give developers a chance to actually catch their errors," he continued.


In recent times, open-source registries, including npm, have repeatedly [[1](https://www.bleepingcomputer.com/news/security/npm-package-steals-chrome-passwords-on-windows-via-recovery-tool/), [2](https://www.bleepingcomputer.com/news/security/new-linux-macos-malware-hidden-in-fake-browserify-npm-package/), [3](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-target-amazon-slack-with-new-dependency-attacks/)] been flooded with malware or [unwanted content](https://www.bleepingcomputer.com/news/security/spammers-flood-pypi-with-pirated-movie-links-and-bogus-packages/).


Developers should exercise caution when typing npm commands in the terminal when especially when using flags. It's also a good idea to check why your packages are *dependent*on this mysterious package.




#### Tags:
[[npm]] [[(BleepingComputer)]] [[packages,]] [[somepackage]] [["npm]] [[Bleeping Computer]]
