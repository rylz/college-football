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
| west virginia 14<br>**#12 baylor 54** |  |
| georgia southern 11<br>**#20 appalachian state 45** |  |
| **navy 49**<br>connecticut 20 |  |
| **#14 michigan 34**<br>maryland 21 |  |
| nc state 31<br>**#23 wake forest (nc) 33** |  |
| boston college 22<br>**syracuse 28** |  |
| **nebraska 36**<br>purdue 23 |  |
| niu 18<br>**central michigan 34** |  |
| **buffalo 29**<br>eastern michigan 23 |  |
| utsa 8<br>**texas a&m 38** |  |
| **Liberty University 63**<br>umass 30 |  |
| houston 21<br>**ucf 44** |  |
| old dominion 11<br>**fiu 36** |  |
| akron 6<br>**bowling green (oh) 29** |  |
| virginia tech 21<br>**#16 notre dame 41** |  |
| troy 29<br>**Coastal Carolina University 39** |  |
| **miami (fl) 31**<br>florida state 24 |  |
| **#22 kansas state 41**<br>kansas 26 |  |
| **tcu 34**<br>oklahoma state 31 |  |
| rutgers (nj) 22<br>**illinois 34** |  |
| #8 georgia 16<br>**#6 florida 25** |  |
| **marshall (wv) 29**<br>rice 20 |  |
| army 15<br>**air force 34** |  |
| unlv 24<br>**colorado state 35** |  |
| arkansas state 33<br>**la monroe 36** |  |
| utep 22<br>**unt 44** |  |
| **middle tenn state 40**<br>charlotte 36 |  |
| wofford 0<br>**#4 clemson 26** |  |
| **pitt 25**<br>georgia tech 21 |  |
| #9 utah 25<br>**washington 30** |  |
| mississippi state 25<br>**arkansas 26** |  |
| tulsa 14<br>**tulane (la) 48** |  |
| fau 15<br>**western kentucky 21** |  |
| **oregon state 31**<br>arizona 29 |  |
| texas state 17<br>**la lafayet 40** |  |
| northwestern 8<br>**indiana 27** |  |
| **uab 19**<br>tennessee 18 |  |
| ole miss 15<br>**#11 auburn 31** |  |
| **#17 cincinnati 28**<br>east carolina 18 |  |
| **virginia 26**<br>n carolina 22 |  |
| vanderbilt 14<br>**south carolina 25** |  |
| #15 smu 33<br>**#24 memphis 38** |  |
| **#7 oregon 30**<br>usc 26 |  |
| **colorado 38**<br>ucla 35 |  |
| alcorn state 25<br>**utah state 26** |  |
| **new mexico 36**<br>nevada 28 |  |
| **#21 boise state 31**<br>san jose state 25 |  |
| fresno state 32<br>**hawaii 39** |  |
