# Credit card PINs can be guessed even when covering the ATM pad
### 

## Information:
+ Source: Bleeping Computer
+ Link: [article](https://www.bleepingcomputer.com/news/security/credit-card-pins-can-be-guessed-even-when-covering-the-atm-pad/)
+ Date: October 18, 2021
+ Author: Bill Toulas


## Article:
![atm pad](https://www.bleepstatic.com/content/hl-images/2021/10/18/0_atm_pad.jpg?rand=984300051)


Researchers have proven it’s possible to train a special-purpose deep-learning algorithm that can guess 4-digit card PINs 41% of the time, even if the victim is covering the pad with their hands. 


The attack requires the setting up of a replica of the target ATM because training the algorithm for the specific dimensions and key spacing of the different PIN pads is crucially important. 


Next, the machine-learning model is trained to recognize pad presses and assign specific probabilities on a set of guesses, using video of people typing PINs on the ATM pad. 



![The entire chain of the attack](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/pin_attack.jpg)**The entire chain of the attack**  

Source: Arxiv.org
For the experiment, the researchers collected 5,800 videos of 58 different people of diverse demographics, entering 4-digit and 5-digit PINs. 


The machine that ran the prediction model was a Xeon E5-2670 with 128 GB of RAM and three Tesla K20m with 5GB of RAM each. Certainly not your average system, but well within a practical economical spectrum. 


By using three tries, which is typically the maximum allowed number of attempts before the card is withheld, the researchers reconstructed the correct sequence for 5-digit PINs 30% of the time, and reached 41% for 4-digit PINs. 


The model can exclude keys based on the non-typing hand coverage, and deduces the pressed digits from the movements of the other hand by evaluating the topological distance between two keys. 



![Prediction heatmap](https://www.bleepstatic.com/images/news/u/1220909/Code%20and%20Details/prediction%20heatmap.jpg)**Prediction heat map for three attack scenarios**  

Source: Arxiv.org
The placement of the camera which captures the tries plays a key role, especially if recording left or right-handed individuals. Concealing a pinhole camera at the top of the ATM was determined to be the best approach for the attacker. 


If the camera is capable of capturing audio too, the model could also use pressing sound feedback which is slightly different for each digit, thus making the predictions a lot more accurate. 



![PIN guesses and propabilities for each digit](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)**PIN guesses and probabilities for each digit**  

Source: Arxiv.org
Countermeasures
---------------


This experiment proves that covering the PIN pad with the other hand is not sufficient to defend against deep learning-based attacks, but thankfully, there are some countermeasures you can deploy. 


* First, if your bank gives you the option to choose a 5-digit PIN instead of a 4-digit one, pick the longer one. It may be harder to remember, but it is a lot safer against attacks of this kind.
* Secondly, the percentage of the hand coverage is significantly lowering the prediction accuracy. A coverage percentage of 75% gives an accuracy of 0.55 for each try, while a total coverage (100%) takes the accuracy down to 0.33.
* A third countermeasure would be to serve users with a virtual and randomized keypad instead of the standardized mechanical one. This inevitably comes with usability drawbacks, but it’s an excellent security measure.


Interestingly, the researchers used the experiment's video clips on a survey with 78 participants to determine if humans could also guess the concealed PINs and up to what point. 


On average, the survey participants answered with an accuracy of only 7.92%, which is inefficient for carrying out attacks of this type. 




#### Tags:
[[4-digit]] [[Source:]] [[Arxiv.org]] [[5-digit]] [[Bleeping Computer]]
