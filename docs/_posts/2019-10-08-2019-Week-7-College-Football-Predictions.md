---
title: 2019 Week 7 College Football Predictions
layout: post
excerpt: Riley Patterson's weekly college football game predictions produced from a gradually improving pagerank-based model. Updated with comparisons to actual results as those results come in.
---

[Week 6 was a dud]({{ site.baseurl }}/2019-Week-6-College-Football-Predictions/): 33-15 wins called correctly, 21-22 against the spread, 23-20 against the over-under.

This week, I wanted to get the ball rolling on model improvements with a simple addition: a feature for home field advantage. In the interest of long-term model evaluation, I'm continuing to produce and archive predictions with the same margin-of-victory-weighted PageRank random forest model from [last year's bowl predictions]({{ site.baseurl }}/2018-College-Football-Bowl-Predictions/). But the predictions I'm presenting below use the new additional feature for home field advantage. This feature implementation was dead simple - whichever team is nominally the "home team" (even if it's technically a neutral site game) is given a value of 1, and the other gets 0. Interestingly, while the feature ends up with a relatively low importance in a random forest model (1.5%, second lowest after AP poll ranking difference), its coefficient in a simple linear regression is 3.6, implying having the home field is worth 3.6 points vs. playing the same game away. Due to disparity in effect of the new feature, I wanted to compare outcomes vs. both the linear and the random forest model, so I'm presenting both below. I'd also like to train something like a recent-history-home-advantage feature that looks at past seasons' results at a given stadium in order to learn things that would be harder to suss out in a single seasons' results, like the fact that Morgantown is notoriously difficult for visitors etc. But that'll keep for at least another week! 

### 2019 Week 7 Game Predictions

| Random Forest | Linear Regression | Actual Result |
| appalachian state 28<br>**la lafayet 44** | appalachian state 35<br>**la lafayet 42** | **appalachian state 17**<br>la lafayet 7 |
| syracuse 25<br>**nc state 26** | syracuse 22<br>**nc state 31** | syracuse 10<br>**nc state 16** |
| la monroe 26<br>texas state 26 | la monroe 30<br>**texas state 32** | **la monroe 24**<br>texas state 14 |
| **#20 virginia 27**<br>miami (fl) 26 | #20 virginia 26<br>**miami (fl) 27** | #20 virginia 9<br>**miami (fl) 17** |
| colorado state 36<br>**new mexico 42** | colorado state 35<br>**new mexico 36** | **colorado state 35**<br>new mexico 21 |
| colorado 14<br>**#13 oregon 38** | colorado 17<br>**#13 oregon 38** | colorado 3<br>**#13 oregon 45** |
| **#23 memphis 28**<br>temple (pa) 26 | **#23 memphis 28**<br>temple (pa) 24 | #23 memphis 28<br>**temple (pa) 30** |
| **#16 michigan 36**<br>illinois 23 | **#16 michigan 28**<br>illinois 23 | **#16 michigan 42**<br>illinois 25 |
| rutgers (nj) 9<br>**indiana 40** | rutgers (nj) 13<br>**indiana 40** | rutgers (nj) 0<br>**indiana 35** |
| **maryland 41**<br>purdue 19 | **maryland 40**<br>purdue 22 | maryland 14<br>**purdue 40** |
| **toledo (oh) 39**<br>bowling green (oh) 13 | **toledo (oh) 40**<br>bowling green (oh) 17 | toledo (oh) 7<br>**bowling green (oh) 20** |
| miami (oh) 18<br>**western michigan 39** | miami (oh) 23<br>**western michigan 42** | miami (oh) 16<br>**western michigan 38** |
| south carolina 9<br>**#3 georgia 49** | south carolina 13<br>**#3 georgia 41** | **south carolina 20**<br>#3 georgia 17 |
| **mississippi state 35**<br>tennessee 17 | **mississippi state 30**<br>tennessee 26 | mississippi state 10<br>**tennessee 20** |
| **#6 oklahoma 48**<br>#11 texas 25 | **#6 oklahoma 44**<br>#11 texas 32 | **#6 oklahoma 34**<br>#11 texas 27 |
| georgia tech 13<br>**duke 38** | georgia tech 13<br>**duke 36** | georgia tech 23<br>**duke 41** |
| ball state 28<br>**eastern michigan 34** | **ball state 33**<br>eastern michigan 31 | **ball state 29**<br>eastern michigan 23 |
| **old dominion 18**<br>marshall (wv) 17 | old dominion 18<br>**marshall (wv) 25** | old dominion 17<br>**marshall (wv) 31** |
| n mex state 13<br>**central michigan 45** | n mex state 19<br>**central michigan 39** | n mex state 28<br>**central michigan 42** |
| florida state 12<br>**#2 clemson 46** | florida state 18<br>**#2 clemson 39** | florida state 14<br>**#2 clemson 45** |
| michigan state 11<br>**#8 wisconsin 28** | michigan state 9<br>**#8 wisconsin 35** | michigan state 0<br>**#8 wisconsin 38** |
| **kent state 30**<br>akron 18 | **kent state 30**<br>akron 27 | **kent state 26**<br>akron 3 |
| niu 23<br>**ohio 29** | niu 18<br>**ohio 28** | **niu 39**<br>ohio 36 |
| washington state 16<br>**#18 arizona state 30** | washington state 28<br>**#18 arizona state 29** | washington state 34<br>**#18 arizona state 38** |
| **#25 cincinnati 43**<br>houston 25 | **#25 cincinnati 30**<br>houston 28 | **#25 cincinnati 38**<br>houston 23 |
| **#1 alabama 36**<br>#24 texas a&m 17 | **#1 alabama 38**<br>#24 texas a&m 22 | **#1 alabama 47**<br>#24 texas a&m 28 |
| alcorn state 22<br>**south florida 40** | alcorn state 21<br>**south florida 33** | alcorn state 23<br>**south florida 27** |
| connecticut 12<br>**tulane (la) 46** | connecticut 14<br>**tulane (la) 45** | connecticut 7<br>**tulane (la) 49** |
| University of Rhode Island 17<br>**virginia tech 45** | University of Rhode Island 21<br>**virginia tech 40** | University of Rhode Island 17<br>**virginia tech 34** |
| **iowa state 39**<br>west virginia 21 | **iowa state 34**<br>west virginia 24 | **iowa state 38**<br>west virginia 14 |
| **san jose state 42**<br>nevada 26 | **san jose state 34**<br>nevada 24 | san jose state 38<br>**nevada 41** |
| **unlv 31**<br>vanderbilt 30 | unlv 30<br>vanderbilt 30 | **unlv 34**<br>vanderbilt 10 |
| texas tech 18<br>**#22 baylor 45** | texas tech 19<br>**#22 baylor 37** | texas tech 30<br>**#22 baylor 33** |
| middle tenn state 20<br>**fau 44** | middle tenn state 25<br>**fau 37** | middle tenn state 13<br>**fau 28** |
| georgia state 32<br>**Coastal Carolina University 47** | georgia state 30<br>**Coastal Carolina University 45** | **georgia state 31**<br>Coastal Carolina University 21 |
| **uab 43**<br>utsa 12 | **uab 29**<br>utsa 15 | **uab 33**<br>utsa 14 |
| ole miss 15<br>**missouri 40** | ole miss 14<br>**missouri 37** | ole miss 27<br>**missouri 38** |
| umass 15<br>**louisiana tech 42** | umass 18<br>**louisiana tech 43** | umass 21<br>**louisiana tech 69** |
| fresno state 29<br>**air force 35** | fresno state 24<br>**air force 33** | fresno state 24<br>**air force 43** |
| unt 33<br>southern miss 33 | **unt 32**<br>southern miss 31 | unt 27<br>**southern miss 45** |
| **army 23**<br>western kentucky 17 | **army 22**<br>western kentucky 21 | army 8<br>**western kentucky 17** |
| charlotte 27<br>**fiu 39** | charlotte 29<br>**fiu 37** | charlotte 23<br>**fiu 48** |
| louisville 32<br>**#19 wake forest (nc) 35** | louisville 24<br>**#19 wake forest (nc) 34** | **louisville 62**<br>#19 wake forest (nc) 59 |
| **#10 penn state 36**<br>#17 iowa 12 | **#10 penn state 27**<br>#17 iowa 14 | **#10 penn state 17**<br>#17 iowa 12 |
| nebraska 28<br>**minnesota 36** | nebraska 26<br>**minnesota 34** | nebraska 7<br>**minnesota 34** |
| arkansas 23<br>**kentucky 30** | arkansas 24<br>**kentucky 27** | arkansas 20<br>**kentucky 24** |
| usc 25<br>**#9 notre dame 33** | usc 18<br>**#9 notre dame 36** | usc 27<br>**#9 notre dame 30** |
| **navy 35**<br>tulsa 17 | **navy 32**<br>tulsa 22 | **navy 45**<br>tulsa 17 |
| **#15 utah 36**<br>oregon state 15 | **#15 utah 31**<br>oregon state 26 | **#15 utah 52**<br>oregon state 7 |
| **#7 florida 30**<br>#5 lsu 7 | #7 florida 26<br>**#5 lsu 33** | #7 florida 28<br>**#5 lsu 42** |
| hawaii 27<br>**#14 boise state 34** | hawaii 24<br>**#14 boise state 33** | hawaii 37<br>**#14 boise state 59** |
| **wyoming 28**<br>s diego state 19 | wyoming 18<br>s diego state 18 | wyoming 22<br>**s diego state 26** |
| **washington 41**<br>arizona 21 | **washington 35**<br>arizona 26 | **washington 51**<br>arizona 27 |
