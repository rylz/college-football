---
title: 2019 Week 8 College Football Predictions
layout: post
excerpt: Riley Patterson's weekly college football game predictions produced from a gradually improving pagerank-based model. Updated with comparisons to actual results as those results come in.
---

In [Week 7]({{ site.baseurl }}/2019-Week-7-College-Football-Predictions/), I experimented with a simple feature for global home field advantage, with interesting results: an apparent improvement against the over-under in the random forest model I've been using (despite low reported importance of that feature by the trained model), but uninspiring results in the simpler linear regression model on the same features (where the home advantage feature was given a fairly high weight):

| Model | Correct Winner | Beat Spread | Beat Over-Under |
| Random Forest baseline | 36-17 | 27-22 | 23-26 |
| Linear Regression with home adv | 38-15 | 22-27 | 23-26 |
| Random Forest with home adv | 35-18 | 27-22 | 29-20 |

Of course, these differences are quite small and could easily be noise over one week. I'm going to continue to evaluate these differences over the next few weeks (and will probably continue to generate predictions for all of my old models as I continue to experiment and develop new ones).

### 2019 Week 8 Game Predictions

| Random Forest | Linear Regression | Actual Result |
| south alabama 18<br>**troy 40** | south alabama 21<br>**troy 36** |  |
| **la lafayet 40**<br>arkansas state 27 | **la lafayet 42**<br>arkansas state 28 |  |
| ucla 23<br>**stanford 30** | ucla 23<br>**stanford 33** |  |
| marshall (wv) 19<br>**fau 30** | marshall (wv) 25<br>**fau 31** |  |
| pitt 21<br>**syracuse 26** | pitt 20<br>**syracuse 24** |  |
| **#4 ohio state 45**<br>northwestern 10 | **#4 ohio state 39**<br>northwestern 2 |  |
| unlv 33<br>**fresno state 35** | unlv 26<br>**fresno state 34** |  |
| **nc state 29**<br>boston college 23 | **nc state 27**<br>boston college 26 |  |
| georgia tech 6<br>**miami (fl) 33** | georgia tech 11<br>**miami (fl) 34** |  |
| west virginia 13<br>**#5 oklahoma 47** | west virginia 16<br>**#5 oklahoma 50** |  |
| **#6 wisconsin 46**<br>illinois 8 | **#6 wisconsin 42**<br>illinois 12 |  |
| purdue 18<br>**#23 iowa 34** | purdue 12<br>**#23 iowa 29** |  |
| **kent state 37**<br>ohio 34 | kent state 24<br>**ohio 31** |  |
| **#9 florida 29**<br>south carolina 13 | **#9 florida 27**<br>south carolina 18 |  |
| **#11 auburn 42**<br>arkansas 23 | **#11 auburn 33**<br>arkansas 19 |  |
| **iowa state 29**<br>texas tech 26 | **iowa state 33**<br>texas tech 26 |  |
| **#3 clemson 41**<br>louisville 23 | **#3 clemson 39**<br>louisville 23 |  |
| **houston 43**<br>connecticut 16 | **houston 39**<br>connecticut 25 |  |
| toledo (oh) 29<br>**ball state 36** | toledo (oh) 29<br>ball state 29 |  |
| **central michigan 43**<br>bowling green (oh) 16 | **central michigan 32**<br>bowling green (oh) 21 |  |
| **tcu 28**<br>kansas state 25 | tcu 27<br>**kansas state 30** |  |
| niu 27<br>**miami (oh) 32** | **niu 28**<br>miami (oh) 26 |  |
| oregon state 25<br>**cal 30** | oregon state 22<br>**cal 29** |  |
| new mexico 21<br>**wyoming 37** | new mexico 19<br>**wyoming 40** |  |
| **Coastal Carolina University 42**<br>georgia southern 28 | **Coastal Carolina University 34**<br>georgia southern 23 |  |
| indiana 26<br>**maryland 28** | indiana 27<br>**maryland 30** |  |
| duke 28<br>**virginia 32** | duke 25<br>**virginia 26** |  |
| **#20 minnesota 39**<br>rutgers (nj) 9 | **#20 minnesota 39**<br>rutgers (nj) 14 |  |
| **n carolina 28**<br>virginia tech 27 | n carolina 25<br>**virginia tech 27** |  |
| southern miss 31<br>louisiana tech 31 | southern miss 25<br>**louisiana tech 35** |  |
| **buffalo 28**<br>akron 15 | **buffalo 31**<br>akron 19 |  |
| **#12 oregon 22**<br>#25 washington 19 | **#12 oregon 26**<br>#25 washington 21 |  |
| **#2 lsu 54**<br>mississippi state 20 | **#2 lsu 48**<br>mississippi state 19 |  |
| temple (pa) 33<br>**#19 smu 36** | temple (pa) 28<br>**#19 smu 35** |  |
| tulsa 17<br>**#21 cincinnati 41** | tulsa 18<br>**#21 cincinnati 34** |  |
| south florida 23<br>**navy 32** | south florida 18<br>**navy 38** |  |
| la monroe 29<br>**#24 appalachian state 48** | la monroe 25<br>**#24 appalachian state 45** |  |
| **#18 baylor 31**<br>oklahoma state 29 | **#18 baylor 34**<br>oklahoma state 30 |  |
| **#22 missouri 42**<br>vanderbilt 14 | **#22 missouri 42**<br>vanderbilt 12 |  |
| middle tenn state 16<br>**unt 39** | middle tenn state 25<br>**unt 36** |  |
| old dominion 13<br>**uab 28** | old dominion 9<br>**uab 29** |  |
| charlotte 24<br>**western kentucky 35** | charlotte 23<br>**western kentucky 35** |  |
| kentucky 11<br>**#10 georgia 36** | kentucky 9<br>**#10 georgia 37** |  |
| #17 arizona state 20<br>**#13 utah 26** | #17 arizona state 13<br>**#13 utah 27** |  |
| University of Maine 17<br>**Liberty University 27** | University of Maine 13<br>**Liberty University 26** |  |
| rice 12<br>**utsa 29** | rice 21<br>**utsa 24** |  |
| **s diego state 29**<br>san jose state 12 | **s diego state 23**<br>san jose state 19 |  |
| **western michigan 32**<br>eastern michigan 27 | **western michigan 35**<br>eastern michigan 27 |  |
| colorado 35<br>**washington state 46** | colorado 31<br>**washington state 45** |  |
| kansas 16<br>**#15 texas 43** | kansas 22<br>**#15 texas 40** |  |
| tulane (la) 23<br>**memphis 28** | tulane (la) 29<br>**memphis 31** |  |
| east carolina 19<br>**ucf 43** | east carolina 15<br>**ucf 39** |  |
| utep 15<br>**fiu 35** | utep 16<br>**fiu 35** |  |
| **army 27**<br>georgia state 25 | **army 32**<br>georgia state 30 |  |
| florida state 30<br>**wake forest (nc) 46** | florida state 28<br>**wake forest (nc) 41** |  |
| #16 michigan 14<br>**#7 penn state 31** | #16 michigan 12<br>**#7 penn state 34** |  |
| texas a&m 24<br>**ole miss 31** | **texas a&m 29**<br>ole miss 25 |  |
| tennessee 14<br>**#1 alabama 41** | tennessee 11<br>**#1 alabama 48** |  |
| arizona 24<br>**usc 33** | arizona 29<br>**usc 35** |  |
| nevada 24<br>**utah state 42** | nevada 20<br>**utah state 42** |  |
| **#14 boise state 41**<br>alcorn state 17 | **#14 boise state 37**<br>alcorn state 16 |  |
| air force 32<br>**hawaii 35** | **air force 35**<br>hawaii 33 |  |
