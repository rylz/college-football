---
title: 2021 College Football Rivalry Week Predictions
layout: post
excerpt: Riley Patterson's pagerank-based model predictions for rivalry week 2021.
image: 2021_rivalry_predictions.png
---

These are predictions produced from an evolution of the model that I have been using for years: a random forest regression run independently to produce each team's score in a given game on the following features:
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
| **#8 ole miss 33**<br>mississippi state 29 |  |
| ohio 26<br>**bowling green (oh) 27** |  |
| eastern michigan 34<br>**central michigan 38** |  |
| kansas state 30<br>**texas 31** |  |
| boise state 22<br>#22 s diego state 22 |  |
| **utah state 36**<br>new mexico 13 |  |
| **#17 iowa 28**<br>nebraska 21 |  |
| utep 18<br>**uab 25** |  |
| missouri 26<br>**#25 arkansas 40** |  |
| unlv 17<br>**air force 34** |  |
| **#4 cincinnati 37**<br>east carolina 16 |  |
| south florida 20<br>**ucf 38** |  |
| **Coastal Carolina University 39**<br>south alabama 20 |  |
| colorado 18<br>**#16 utah 38** |  |
| tcu 28<br>**iowa state 43** |  |
| n carolina 22<br>**#24 nc state 36** |  |
| **washington state 28**<br>washington 26 |  |
| **#1 georgia 43**<br>georgia tech 10 |  |
| **#21 wake forest (nc) 41**<br>boston college 25 |  |
| maryland 19<br>**rutgers (nj) 21** |  |
| **navy 27**<br>temple (pa) 23 |  |
| **#2 ohio state 39**<br>#6 michigan 23 |  |
| **miami (oh) 33**<br>kent state 25 |  |
| akron 15<br>**toledo (oh) 45** |  |
| florida state 29<br>**fla 34** |  |
| texas tech 24<br>**#9 baylor 38** |  |
| **#19 houston 43**<br>connecticut 13 |  |
| **army 29**<br>Liberty University 25 |  |
| **miami (fl) 45**<br>duke 22 |  |
| **louisiana tech 34**<br>rice 21 |  |
| texas state 32<br>arkansas state 32 |  |
| **#15 utsa 36**<br>unt 22 |  |
| charlotte 21<br>**old dominion 32** |  |
| troy 19<br>**georgia state 22** |  |
| georgia southern 18<br>**appalachian state 40** |  |
| umass 28<br>**n mex state 33** |  |
| hawai i 22<br>**wyoming 27** |  |
| fiu 21<br>**southern miss 30** |  |
| northwestern 13<br>**illinois 25** |  |
| penn state 21<br>**#12 michigan state 26** |  |
| indiana 12<br>**purdue 30** |  |
| oregon state 25<br>**#11 oregon 32** |  |
| **#3 alabama 42**<br>auburn 23 |  |
| **western kentucky 40**<br>marshall (wv) 34 |  |
| virginia tech 25<br>**virginia 31** |  |
| vanderbilt 18<br>**tennessee 45** |  |
| **#18 wisconsin 25**<br>minnesota 15 |  |
| la monroe 17<br>**#23 la lafayet 37** |  |
| arizona 13<br>**arizona state 38** |  |
| tulsa 20<br>**smu 35** |  |
| **west virginia 40**<br>kansas 26 |  |
| **#14 texas a&m 25**<br>lsu 14 |  |
| middle tenn state 27<br>**fau 30** |  |
| **#20 pitt 42**<br>syracuse 25 |  |
| #10 oklahoma 19<br>**#7 oklahoma state 29** |  |
| **clemson 24**<br>south carolina 15 |  |
| **kentucky 30**<br>louisville 25 |  |
| tulane (la) 26<br>**memphis 39** |  |
| **#5 notre dame 35**<br>stanford 13 |  |
| **nevada 29**<br>colorado state 28 |  |
| **#13 byu 34**<br>usc 22 |  |
| cal 25<br>**ucla 28** |  |
