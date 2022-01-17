# NoReboot iOS Attack Prevents Your iPhone From Turning Off Or Reboot
### The NoReboot attack manipulates the iOS daemons into making the phone unresponsive, hence simulating false reboots.

## Information:
+ Source: Latest Hacking News
+ Link: https://latesthackingnews.com/2022/01/17/noreboot-ios-attack-prevents-your-iphone-from-turning-off-or-reboot/
+ Date: 2022-01-17
+ Author: Abeerah Hashim


## Article:
![Article Image](https://latesthackingnews.com/wp-content/uploads/2018/09/CSS-based-web-attack-crashing-iPhone.jpg)
 Researchers have demonstrated how a creative hacker can manipulate iPhone users into keeping their devices on. Dubbed ‘NoReboot’, the attack induces a bug in the iOS system that generates fake reboots while actually preventing device shutdown or reboot.

 NoReboot iOS Attack Achieves “Persistence” On iPhones
-----------------------------------------------------

 Elaborating their findings in a [report](https://blog.zecops.com/research/persistence-without-persistence-meet-the-ultimate-persistence-bug-noreboot/), researchers from ZecOps have shared how the NoReboot attack can ditch Apple’s security measures.

 As the name suggests, NoReboot prevents shutdown or restart attempts on an iOS device. While the attack may sound trivial, it actually isn’t, as it deceives the victims by showing false reboots.

 It is particularly severe given that restarting the device is one of the most basic fixes to solve any glitches. So, while a user would become frustrated with the device’s glitchy performance even after supposed reboots, it would never practically turn off. Such an attack also gives persistent access to the target device to the attacker.

 In short, the attacker gains persistence without actually employing any measures for “persistence”.

 This attack merely triggers an iOS bug that allows altering the shutdown event.

 ### How NoReboot works

 In brief, it involves injecting codes in three daemons handling three major functionalities.

 * `InCallService` – managing the slider UI to power off the device. It signals the Springboard daemon for the shutdown.
* `Sprinboard` – manages most UI interactions that respond to users’ behavior. When triggered to shut down, it turns off all those UI processes.
* `Backboardd` – it manages some of the UI and works in parallel with the Springboard. For instance, it displays the spinning wheel animation when Springboard stops.

 The [researchers demonstrated](https://latesthackingnews.com/2021/03/18/researcher-demonstrates-hiding-data-in-twitter-images/) that disabling the Springboard daemon and hiding the animation in the Backboardd daemon would show the target device as turned off. That’s because the user won’t see any response from it upon clicking buttons or Touch commands. Nor would they observe any sounds, screen, or camera indicators working.

 However, the device would be completely active in this situation, with an active internet connection. This apparent unresponsiveness gives ample space for the attacker to conduct any malicious activities on the device. It includes [spying on the user via the mic](https://latesthackingnews.com/2020/11/23/facebook-messenger-bug-could-allow-spying-on-users-via-audio/) or camera.

 
> The malicious actor could remotely manipulate the phone in a blatant way without worrying about being caught because the user is tricked into thinking that the phone is off, either being turned off by the victim or by malicious actors using “low battery” as an excuse.
> 
> 

 Then, when the user attempts to turn on the device, the attacker reverses the whole process. It would [make the user believe](https://latesthackingnews.com/2017/03/28/iphone-users-think-theyre-safe-theyre-not/) a successful reboot without knowing the *persistent* attack in the background.

 The following video demonstrates the attack while the researchers have shared the [PoC on GitHub](https://github.com/ZecOps/public/tree/master/fake_shutdown_POC).

  What About Force Restart?
-------------------------

 According to ZecOps, this attack doesn’t work on the force restart process. They couldn’t figure out how it works, hence, becoming a way to overcome this attack.

 However, an attacker may guess a force restart attempt before time and would trigger the UI early to trick the user into ending the attempt.

 
> It is entirely possible for malicious actors to observe the user’s attempt to perform a force-restart (via backboardd) and deliberately make the Apple logo appear a few seconds earlier, deceiving the user into releasing the button earlier than they were supposed to. Meaning that in this case, the end-user did not successfully trigger a force-restart.
> 
> 

 Also, a forced restart isn’t feasible in all situations as it can sometimes lead to data loss.

 For now, this attack seems *unpatchable* as it doesn’t exploit a system vulnerability but deceives the end-user.

   


## Tags:

#### Action:
[[action.malware.name=at]] [[action.malware.name=Net]] [[action.malware.name=njRAT]] [[action.malware.name=Ping]] [[action.malware.name=Ping]] [[action.malware.name=Tor]]

#### Industry:
[[victim.industry.name=Accomodation]]

#### Location:
[[victim.country.name=Mali]] [[victim.continent.name=Africa]] [[victim.city.name=]] [[victim.country.name=Haiti]] [[victim.continent.name=North and Central America]]

### Autogenerated Tags:
[[Noreboot]] [[Latest Hacking News]]

