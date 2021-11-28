---
title: 2021 College Football Rivalry Week Predictions
layout: post
excerpt: Riley Patterson's pagerank-based model predictions for rivalry week 2021.
image: /images/2021_rivalry_predictions.png
---

_Updated with results and performance 11/28/2021._

These are predictions produced from an evolution of the model that I have been using for years: a random forest regression which independently predicts each team's score in a given game on the following features:
* difference in opponents' pagerank in a graph of past games, with edges from losers to winners weighted by the margin of victory
* average points scored by the team
* average points allowed by the other team
* difference in AP rank of the opponents

If you're interested in more details on the model, see the "Technical Approach" section of my [2017 Bowl Predictions]({{ site.baseurl }}/Predicting-the-2017-College-Football-Bowl-Season/). This week, I simply kicked the dust off of a slightly improved version of the model described there, in order to get it running in a new environment and with this year's data. In advance of the postseason, I'm planning to return to my drive-oriented game simulation model. More details on that in future rounds of predictions.

### Highlighted Predictions

![Big Rivalry Game Predictions]({{ site.baseurl }}/images/2021_rivalry_predictions.png)

The games with the most eyeballs on them this week will, of course, be those between the current top 4. Folks generally think these teams are in control of their own destiny, and my model does expect them to survive this week, and generally agrees with the current spreads, with a notable exception where it sees Ohio State blowing out Michigan:

| Prediction | Spread as of 11/25 Evening | Cover? |
| **#1 georgia 43**<br>georgia tech 10 | georgia -35 | no |
| **#2 ohio state 39**<br>#6 michigan 23 | ohio state -8 | yes |
| **#3 alabama 42**<br>auburn 23 | alabama -19.5 | no |
| **#4 cincinnati 37**<br>east carolina 16 | cincinnati -14 | yes |

Another major storyline, given the possible/likely limitation of one of Alabama or Georgia in next week's SEC championship, is what happens in the Big 12 championship race. My model sees Oklahoma State finally getting a big win in Bedlam in the playoff era, and going on to face Baylor next week in the Big 12 championship, with a potential playoff berth on the line:

| Prediction | Spread as of 11/25 Evening | Cover? |
| texas tech 24<br>**#9 baylor 38** | baylor -14 | push |
| #10 oklahoma 19<br>**#7 oklahoma state 29** | oklahoma state -4.5 | yes |

### Full Week 13 Predictions

Here are my predictions for all games this week. I'll update this table with actual results as they come in.

| Random Forest Prediction | Actual Result |
| **western michigan 38**<br>niu 29 | **western michigan 42**<br>niu 21 |
| buffalo 21<br>**ball state 25** | buffalo 3<br>**ball state 20** |
| **#8 ole miss 33**<br>mississippi state 29 | **#8 ole miss 31**<br>mississippi state 21 |
| ohio 26<br>**bowling green (oh) 27** | ohio 10<br>**bowling green (oh) 21** |
| eastern michigan 34<br>**central michigan 38** | eastern michigan 10<br>**central michigan 31** |
| kansas state 30<br>**texas 31** | kansas state 17<br>**texas 22** |
| boise state 22<br>#22 s diego state 22 | boise state 16<br>**#22 s diego state 27** |
| **utah state 36**<br>new mexico 13 | **utah state 35**<br>new mexico 10 |
| **#17 iowa 28**<br>nebraska 21 | **#17 iowa 28**<br>nebraska 21 |
| utep 18<br>**uab 25** | utep 25<br>**uab 42** |
| missouri 26<br>**#25 arkansas 40** | missouri 17<br>**#25 arkansas 34** |
| unlv 17<br>**air force 34** | unlv 14<br>**air force 48** |
| **#4 cincinnati 37**<br>east carolina 16 | **#4 cincinnati 35**<br>east carolina 13 |
| south florida 20<br>**ucf 38** | south florida 13<br>**ucf 17** |
| **Coastal Carolina University 39**<br>south alabama 20 | **Coastal Carolina University 27**<br>south alabama 21 |
| colorado 18<br>**#16 utah 38** | colorado 13<br>**#16 utah 28** |
| tcu 28<br>**iowa state 43** | tcu 14<br>**iowa state 48** |
| n carolina 22<br>**#24 nc state 36** | n carolina 30<br>**#24 nc state 34** |
| **washington state 28**<br>washington 26 | **washington state 40**<br>washington 13 |
| **#1 georgia 43**<br>georgia tech 10 | **#1 georgia 45**<br>georgia tech 0 |
| **#21 wake forest (nc) 41**<br>boston college 25 | **#21 wake forest (nc) 41**<br>boston college 10 |
| maryland 19<br>**rutgers (nj) 21** | **maryland 40**<br>rutgers (nj) 16 |
| **navy 27**<br>temple (pa) 23 | **navy 38**<br>temple (pa) 14 |
| **#2 ohio state 39**<br>#6 michigan 23 | #2 ohio state 27<br>**#6 michigan 42** |
| **miami (oh) 33**<br>kent state 25 | miami (oh) 47<br>**kent state 48** |
| akron 15<br>**toledo (oh) 45** | akron 14<br>**toledo (oh) 49** |
| florida state 29<br>**fla 34** | florida state 21<br>**fla 24** |
| texas tech 24<br>**#9 baylor 38** | texas tech 24<br>**#9 baylor 27** |
| **#19 houston 43**<br>connecticut 13 | **#19 houston 45**<br>connecticut 17 |
| **army 29**<br>Liberty University 25 | **army 31**<br>Liberty University 16 |
| **miami (fl) 45**<br>duke 22 | **miami (fl) 47**<br>duke 10 |
| **louisiana tech 34**<br>rice 21 | louisiana tech 31<br>**rice 35** |
| **#15 utsa 36**<br>unt 22 | #15 utsa 23<br>**unt 45** |
| charlotte 21<br>**old dominion 32** | charlotte 34<br>**old dominion 56** |
| troy 19<br>**georgia state 22** | troy 10<br>**georgia state 37** |
| texas state 32<br>arkansas state 32 | **texas state 24**<br>arkansas state 22 |
| georgia southern 18<br>**appalachian state 40** | georgia southern 3<br>**appalachian state 27** |
| umass 28<br>**n mex state 33** | umass 27<br>**n mex state 44** |
| hawai i 22<br>**wyoming 27** | **hawai i 38**<br>wyoming 14 |
| fiu 21<br>**southern miss 30** | fiu 17<br>**southern miss 37** |
| northwestern 13<br>**illinois 25** | northwestern 14<br>**illinois 47** |
| penn state 21<br>**#12 michigan state 26** | penn state 27<br>**#12 michigan state 30** |
| indiana 12<br>**purdue 30** | indiana 7<br>**purdue 44** |
| oregon state 25<br>**#11 oregon 32** | oregon state 29<br>**#11 oregon 38** |
| **#3 alabama 42**<br>auburn 23 | **#3 alabama 24**<br>auburn 22 |
| **western kentucky 40**<br>marshall (wv) 34 | **western kentucky 53**<br>marshall (wv) 21 |
| virginia tech 25<br>**virginia 31** | **virginia tech 29**<br>virginia 24 |
| vanderbilt 18<br>**tennessee 45** | vanderbilt 21<br>**tennessee 45** |
| **#18 wisconsin 25**<br>minnesota 15 | #18 wisconsin 13<br>**minnesota 23** |
| la monroe 17<br>**#23 la lafayet 37** | la monroe 16<br>**#23 la lafayet 21** |
| arizona 13<br>**arizona state 38** | arizona 15<br>**arizona state 38** |
| tulsa 20<br>**smu 35** | **tulsa 34**<br>smu 31 |
| **west virginia 40**<br>kansas 26 | **west virginia 34**<br>kansas 28 |
| **#14 texas a&m 25**<br>lsu 14 | #14 texas a&m 24<br>**lsu 27** |
| middle tenn state 27<br>**fau 30** | **middle tenn state 27**<br>fau 17 |
| **#20 pitt 42**<br>syracuse 25 | **#20 pitt 31**<br>syracuse 14 |
| #10 oklahoma 19<br>**#7 oklahoma state 29** | #10 oklahoma 33<br>**#7 oklahoma state 37** |
| **clemson 24**<br>south carolina 15 | **clemson 30**<br>south carolina 0 |
| **kentucky 30**<br>louisville 25 | **kentucky 52**<br>louisville 21 |
| tulane (la) 26<br>**memphis 39** | tulane (la) 28<br>**memphis 33** |
| **#5 notre dame 35**<br>stanford 13 | **#5 notre dame 45**<br>stanford 14 |
| **nevada 29**<br>colorado state 28 | **nevada 52**<br>colorado state 10 |
| **#13 byu 34**<br>usc 22 | **#13 byu 35**<br>usc 31 |
| cal 25<br>**ucla 28** | cal 14<br>**ucla 42** |

### Performance

As has often been the case with this model, this week's predictions narrowly outperformed the spread (33-30), but fared poorly against the over-under (28-36).

Here's a survey of how some of my predictions' larger disagreements against the Vegas spread performed. These are all games that included at least one AP-ranked opponent, where either my spread differed by 7 or more vs. Vegas, or we disagreed on who the actual winner of the game would be:

| Actual Result | Predicted Spread | Vegas Spread |
| **#8 ole miss 31**<br>mississippi state 21 | *ole miss -4* | mississipi state -2 |
| **#17 iowa 28**<br>nebraska 21 | *iowa -7* | nebraska -1.5 |
| n carolina 30<br>**#24 nc state 34** | nc state -14 | *nc state -5.5* |
| **#21 wake forest (nc) 41**<br>boston college 10 | *wake forest -16* | wake forest -6 |
| #2 ohio state 27<br>**#6 michigan 42** | ohio state -16 | *ohio state -6.5* |
| penn state 27<br>**#12 michigan state 30** | *michigan state -3* | penn state -4 |

4-2 in Rivalry Week's big games doesn't feel so bad, though of course it sucks to whiff so hard on the big one in Ann Arbor.

See you next week for Chamionship Weekend!
