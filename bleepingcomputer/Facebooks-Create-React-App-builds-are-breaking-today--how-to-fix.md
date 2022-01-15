# Facebook's Create React App builds are breaking today — how to fix
### Tons of users are reporting their Facebook Create React App builds are failing since yesterday. The cause has been traced down to a dependency used by create-react-app, the latest version of which is breaking developers' apps.

## Information:
+ Source: Bleeping Computer
+ Link: https://www.bleepingcomputer.com/news/security/facebooks-create-react-app-builds-are-breaking-today-how-to-fix/
+ Date: 2022-01-15T12:35:00-05:00
+ Author: Ax Sharma


## Article:
![Article Image](https://www.bleepstatic.com/content/hl-images/2021/06/30/Facebook.jpg)

![facebook](https://www.bleepstatic.com/content/hl-images/2021/06/30/Facebook.jpg)


Tons of users are reporting their Facebook Create React App builds are failing since yesterday.


The cause has been traced down to a dependency used by *create-react-app,* the latest version of which is breaking developers' apps.


While a stable solution is yet to be identified, here's a simple workaround developers can adopt.


create-react-app builds failing worldwide
-----------------------------------------


Create React App is an open source project produced by Facebook (Meta) and made available on both [GitHub](http://github.com/facebook/create-react-app) and [npm](https://www.npmjs.com/package/create-react-app) to help developers build single-page React applications fast.


The GitHub project is used by over 5.4 million repositories, whereas the npm version receives around 200,000 weekly downloads on average.


The tool offers a modern build setup while requiring no complex configuration—developers can therefore build a React app with just a few [simple commands](https://create-react-app.dev/docs/getting-started/).


That explains why so many developers would rely on *create-react-app*and are experiencing build failure issues since yesterday.


Software engineer [John Athanasiou](https://github.com/facebook/create-react-app/issues/11930) and front-end developer [Ronald Groot Jebbink](https://github.com/facebook/create-react-app/issues/11931) have been joined by many GitHub users who reported problems building their *create-react-app* builds into today.    



![Users report their create-react-app builds failing](https://www.bleepstatic.com/images/news/u/1164866/2022/January-2022/create-react-app-npm/github-issue.jpg)**Users report their create-react-app builds failing (**GitHub)
Dependency hell strikes again
-----------------------------


The straightforward error message "TypeError: MiniCssExtractPlugin is not a constructor," gives it away.


The problem has been traced down to one of the dependencies, called [mini-css-extract-plugin](https://github.com/webpack-contrib/mini-css-extract-plugin), used by *create-react-app*.


Mini CSS Extract Plugin is yet another popular project with over 4.6 million GitHub repos relying on it.


With over 7,000 npm projects depending on Mini CSS Extract Plugin, the project receives [10 million weekly downloads](https://www.npmjs.com/package/mini-css-extract-plugin) on average on the npm registry.


Mini CSS Extract Plugin came to life in 2018, around the same time as [Extract Text Webpack Plugin](https://www.npmjs.com/package/extract-text-webpack-plugin) was deprecated by its author.


This project extracts CSS into separate files, generating a CSS file per JS file that contains CSS.


The latest version of Mini CSS Extract Plugin, 2.5.0 was published less than a day ago and appears to be the culprit. It is since the publication of this particular version that *create-react-app* project builds began to fail.


Interestingly, as seen by BleepingComputer, the [changelog](https://github.com/webpack-contrib/mini-css-extract-plugin/commit/ce2cb04da96d37a6ebaf940f0caf1ddaadea805a#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4edR10) for version 2.5.0 has the maintainer noting a new feature addition, "types" having been made: 



![mini css extract plugin 2.5.0 commit](https://www.bleepstatic.com/images/news/u/1164866/2022/January-2022/create-react-app-npm/css-plugin-commit.jpg)**Version 2.5.0 of Mini CSS Extract Plugin comes with "added types"** (GitHub)
And we wonder if the particular [commit](https://github.com/webpack-contrib/mini-css-extract-plugin/commit/5b5654c9847a615555660d79245b857536f72124) is what's impacting *create-react-app* instances to break.


A [bug report](https://github.com/webpack-contrib/mini-css-extract-plugin/issues/896) filed for the Mini CSS Extract Plugin's maintainers to look at goes over some possible causes. 


Until a concrete fix is identified by Facebook's open source team, devs have noted success by downgrading their version of the *mini-css-extract-plugin* to 2.4.5:



> 
> A minor version bump on mini-css-extract-plugin to 2.5.0 breaks most implementations. Pin your version to 2.4.5 until a fix is released <https://t.co/Km55Pw0cC6> (also <https://t.co/63FhuaYmVr>) [#webdev](https://twitter.com/hashtag/webdev?src=hash&ref_src=twsrc%5Etfw) [#js](https://twitter.com/hashtag/js?src=hash&ref_src=twsrc%5Etfw) [#webpack](https://twitter.com/hashtag/webpack?src=hash&ref_src=twsrc%5Etfw)
> 
> 
> — Terry (@teddyrised) [January 14, 2022](https://twitter.com/teddyrised/status/1482131064499933187?ref_src=twsrc%5Etfw)


This can be done by updating your JavaScript app's *package.json*file to include the [following lines](https://github.com/facebook/create-react-app/issues/11930#issuecomment-1013480827),  thereby pinning the dependency's version to 2.4.5, as proposed by developer Alexandru Pavaloi:



```
"resolutions": {
    "mini-css-extract-plugin": "2.4.5"
},
```

Those who are not using *yarn*, and for whom the above workaround fails can try running the following command, as [suggested](https://github.com/facebook/create-react-app/issues/11930#issuecomment-1013494785) by front-end developer Oscar Busk:



```
npm i -D --save-exact mini-css-extract-plugin@2.4.5
```

"I tried everything 'resolutions' as well as 'overrides' but none of these worked until I tried the one above!" [writes](https://github.com/facebook/create-react-app/issues/11930#issuecomment-1013707045) a user.


Note, Facebook's Create React App may not be the only prominent application to be impacted by the new dependency version.


Npm project [@wordpress/scripts](https://www.npmjs.com/package/@wordpress/scripts) is also [reportedly](https://github.com/webpack-contrib/mini-css-extract-plugin/issues/896#issuecomment-1013527411) breaking.


Developers of Auth0's SDK for single-page applications are [temporarily locking in](https://github.com/auth0/auth0-spa-js/pull/865) the dependency version to '2.4.5' to be safe.


Although not malicious in nature, this incident follows last week's news of popular ['colors' and 'faker' npm dependencies breaking thousands](https://www.bleepingcomputer.com/news/security/dev-corrupts-npm-libs-colors-and-faker-breaking-thousands-of-apps/) of software projects after their developer had corrupted them.


BleepingComputer has reached out to Facebook (Meta) to better understand the cause of the issue. In the meantime, we hope the above workarounds will save your React builds.





## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Elise]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Reg]] [[action.malware.name=S-Type]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Information]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Css]] [[Create-react-app]] [[Plugin]] [[Npm]] [[Facebook]] [[Github]] [[Mini-css-extract-plugin]] [[Bleeping Computer]]
#### email-adresses
mini-css-extract-plugin@2.4.5
#### urls
https://t.co/Km55Pw0cC6 https://t.co/63FhuaYmVr)

