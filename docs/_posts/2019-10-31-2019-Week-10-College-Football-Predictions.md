---
title: 2019 Week 10 College Football Predictions
layout: post
excerpt: Riley Patterson's weekly college football game predictions produced from a gradually improving pagerank-based model. Updated with comparisons to actual results as those results come in.
---

[Week 9's prediections]({{ site.baseurl }}/2019-Week-9-College-Football-Predictions/) performed by far the worst of any week I've predicte din the past few years:

| Model | Correct Winner | Beat Spread | Beat Over-Under |
|-------|----------------|-------------|-----------------|
| Random Forest baseline | 34-21 | 23-32 | 24-31 |
| Random Forest with home adv | 35-20 | 24-31 | 19-36 |

I'm tentatively chalking this up to a whirlwind of a week: lots of heavy underdogs produced wins, including the likes of Kansas, Kansas State against OU, Kentucky, Illinois, Baylor against Iowa State, and Tennessee. In several other cases there were massive swings against the spread, as with Michigan pulling out a 31 point win over one-point-favorite Notre Dame. One potential pattern here is that the PageRank model may be undervaluing teams who have shown more promise in recent weeks than early in the season; there is no weighting for recency in PageRank weights. But I also don't want to overreact to one bad week in college football. If I assume my model should continue to pick against the spread at its historical average of ~55%, the probability that a given week goes 23-32 against the spread is about 5%. And this was a week in which the median game was a 12.5 point swing vs. the spread, compared to a historical average of 9.5 in my dataset. While I'll continue to consider updating the model to value recent results with slightly higher weight, for this week's predictions below, I'm continuing to use the PageRank model that is weighted by margin of victory alone.

### 2019 Week 10 Game Predictions

| Predicted Result | Actual Result |
|------------------|---------------|
| west virginia 14<br>**#12 baylor 54** | west virginia 14<br>**#12 baylor 17** |
| georgia southern 11<br>**#20 appalachian state 45** | **georgia southern 24**<br>#20 appalachian state 21 |
| **navy 49**<br>connecticut 20 | **navy 56**<br>connecticut 10 |
| **#14 michigan 34**<br>maryland 21 | **#14 michigan 38**<br>maryland 7 |
| nc state 31<br>**#23 wake forest (nc) 33** | nc state 10<br>**#23 wake forest (nc) 44** |
| boston college 22<br>**syracuse 28** | **boston college 58**<br>syracuse 27 |
| **nebraska 36**<br>purdue 23 | nebraska 27<br>**purdue 31** |
| niu 18<br>**central michigan 34** | niu 10<br>**central michigan 48** |
| **buffalo 29**<br>eastern michigan 23 | **buffalo 43**<br>eastern michigan 14 |
| utsa 8<br>**texas a&m 38** | utsa 14<br>**texas a&m 45** |
| **Liberty University 63**<br>umass 30 | **Liberty University 63**<br>umass 21 |
| houston 21<br>**ucf 44** | houston 29<br>**ucf 44** |
| old dominion 11<br>**fiu 36** | old dominion 17<br>**fiu 24** |
| akron 6<br>**bowling green (oh) 29** | akron 6<br>**bowling green (oh) 35** |
| virginia tech 21<br>**#16 notre dame 41** | virginia tech 20<br>**#16 notre dame 21** |
| troy 29<br>**Coastal Carolina University 39** | troy 35<br>**Coastal Carolina University 36** |
| **miami (fl) 31**<br>florida state 24 | **miami (fl) 27**<br>florida state 10 |
| **#22 kansas state 41**<br>kansas 26 | **#22 kansas state 38**<br>kansas 10 |
| **tcu 34**<br>oklahoma state 31 | tcu 27<br>**oklahoma state 34** |
| rutgers (nj) 22<br>**illinois 34** | rutgers (nj) 10<br>**illinois 38** |
| #8 georgia 16<br>**#6 florida 25** | **#8 georgia 24**<br>#6 florida 17 |
| **marshall (wv) 29**<br>rice 20 | **marshall (wv) 20**<br>rice 7 |
| army 15<br>**air force 34** | army 13<br>**air force 17** |
| unlv 24<br>**colorado state 35** | unlv 17<br>**colorado state 37** |
| arkansas state 33<br>**la monroe 36** | **arkansas state 48**<br>la monroe 41 |
| utep 22<br>**unt 44** | utep 26<br>**unt 52** |
| **middle tenn state 40**<br>charlotte 36 | middle tenn state 20<br>**charlotte 34** |
| wofford 0<br>**#4 clemson 26** | wofford 14<br>**#4 clemson 59** |
| **pitt 25**<br>georgia tech 21 | **pitt 20**<br>georgia tech 10 |
| #9 utah 25<br>**washington 30** | **#9 utah 33**<br>washington 28 |
| mississippi state 25<br>**arkansas 26** | **mississippi state 54**<br>arkansas 24 |
| tulsa 14<br>**tulane (la) 48** | tulsa 26<br>**tulane (la) 38** |
| fau 15<br>**western kentucky 21** | **fau 35**<br>western kentucky 24 |
| **oregon state 31**<br>arizona 29 | **oregon state 56**<br>arizona 38 |
| texas state 17<br>**la lafayet 40** | texas state 3<br>**la lafayet 31** |
| northwestern 8<br>**indiana 27** | northwestern 3<br>**indiana 34** |
| **uab 19**<br>tennessee 18 | uab 7<br>**tennessee 30** |
| ole miss 15<br>**#11 auburn 31** | ole miss 14<br>**#11 auburn 20** |
| **#17 cincinnati 28**<br>east carolina 18 | **#17 cincinnati 46**<br>east carolina 43 |
| **virginia 26**<br>n carolina 22 | **virginia 38**<br>n carolina 31 |
| vanderbilt 14<br>**south carolina 25** | vanderbilt 7<br>**south carolina 24** |
| #15 smu 33<br>**#24 memphis 38** | #15 smu 48<br>**#24 memphis 54** |
| **#7 oregon 30**<br>usc 26 | **#7 oregon 56**<br>usc 24 |
| **colorado 38**<br>ucla 35 | colorado 14<br>**ucla 31** |
| alcorn state 25<br>**utah state 26** | **alcorn state 42**<br>utah state 14 |
| **new mexico 36**<br>nevada 28 | new mexico 10<br>**nevada 21** |
| **#21 boise state 31**<br>san jose state 25 | **#21 boise state 52**<br>san jose state 42 |
| fresno state 32<br>**hawaii 39** | **fresno state 41**<br>hawaii 38 |
