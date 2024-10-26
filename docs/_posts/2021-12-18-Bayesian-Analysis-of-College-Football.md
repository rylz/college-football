---
title: Bayesian Modeling to Analyze and Simulate College Football
layout: post
excerpt: This bowl season, I predict game outcomes using a Monte Carlo simulation of a Bayesian model for predicting games drive-by-drive based on a current state vector and past performance of the current offense and defense. I compare this model to the simpler random forests prediction of overall game scores that I have been using for years, and present predictions for this bowl season using both models.
---

College football is widely understood to be a high variance sport. In a game in which teams average just 12 possessions per game, single events like a fumble in the red zone can heavily swing likely game outcomes. In the modern game, where fans often see high definition slow motion replays showing how the runner's knee came down just one frame before or after the ball popped out, it's hard not to acknowledge how much a given game result between evenly matched teams amounts to chance.

_If you are more interested in the game predictions and analysis than the technical background, skip ahead to the Bowl Predictions section._

I have been [experimenting with college football prediction]({{ site.baseurl }}/Predicting-the-2017-College-Football-Bowl-Season/) for several years now, and have had some succcess with simple regression models on features produced only from final scores of past games. Frankly, I was surprised I was able to get to the 55-60% performance against the spread that I have seen over the past couple of seasons with these models. Given that track record, I'll certainly continue to use and improve these regressions to predict games in the coming seasons. But there are several limitations to this approach that made me want to try something a little different:
* the regressions are deterministic and don't allow visibility into the inherent variance in game outcomes, so it's difficult to assess the confidence of a given prediction.
* while these models do offer some interpretabiliity of relative feature importance in predicting total points scored, the structure of predicting whole game outcomes makes it difficult to analyze in more detail - why exactly is Team A going to beat Team B by 14 points? What is the model capturing and failing to capture, and how can it be improved?
* they're not super fun to [evaluate hypothetical scenarios against](https://www.quora.com/Do-the-2019-2020-Florida-Gators-have-a-chance-of-winning-the-College-Football-Playoffs/answer/Riley-Patterson), due largely to their opacity and the above issues.

Starting a few seasons ago, I decided to play around with probabilistic models to analyze the game without some of these limitations. I'm not convinced that this approach alone will necessarily improve my game outcome prediction accuracy, but it's better suited to combining predictions of more granular events like drives or even individual plays. Where a deterministic regression model might always predict Alabama will score a touchdown on every drive against Vanderbilt, and Vanderbilt will punt every time, a probabilistic model may come to a more realistic prediction where Alabama scores on 80% of their drives and Vanderbilt scores on 10% of theirs. Structuring this new model as an aggregate prediction of more granular events is great because:
* a different, more granular set of features are well-suited to these models than to deterministic regression, so I get to make use of data I hadn't been using in the past.
* it will open up a lot of fun post-hoc analysis, like "how much did that fumble change the game?"
* it will likely at least be useful in conjunction with my regression models, either to help understand variance in my predictions or as part of an ensemble model.

## Gaussian Naive Bayes for Drive Prediction

The primary probabilistic model I have been analyzing is built on Gaussian Naive Bayes (GNB) with the following features:

Game features are the same features currently used in my regression model for score prediction:
* `pr_diff`, the difference in PageRank between the team and their opponent. This was calculated using a graph of the entire regular season results, using margin of victory as an edge weight.
* `conf_pr_diff`, the difference in PageRank between the teams' conferences given regular season results, using unit weights for edges.
* `ap_rank_diff`, the difference in the week 14 AP poll ranking between the team and their opponent. All unranked teams were treated as tied for 26.
* `opp_points_allowed`, the average points the opponent allowed per game in the regular season.
* `ppg`, the average points per game scored by the team.

Drive features encode initial state when the given team takes possession:
* `yards_to_endzone` in the range 1-99 is the number of yards away from the opposing team's endzone that the drive begins at.
* `time_in_half` is the amount of time (in seconds) remaining until the current half ends.
* `time_in_game` is the amount of time (in seconds) remaining in the game.
* `pt_diff` indicates the current score margin, positive meaning that the team in possession is in the lead, and negative meaning that the opposing team is in the lead.

The classification domain is "drive results," the nine possible ways that a football possession can end:
* punt
* turnover on downs
* touchdown
* field goal
* missed field goal
* interception
* fumble
* safety
* end of half

Using these features, a GNB is trained to classify likely drive results based on game features and drive initial states. Additional GNBs are trained to classify each of points earned or lost, yards, and duration of the drive from initial states for each possible drive result. (i.e. 9x3 = 27 additional models are trained). This is more effective than training a single model to classify 4 dimensional results because points, yards, and duration are learned independently. A game can then be simulated by maintaining a current drive state, sampling drive results, points, yards, and durations from these models, sanitizing the predictions to be within the realm of possibility (i.e. you can't drive more than `yards_to_endzone` or take more time than `time_to_half`), and updating the drive state for the predicted drive results until a terminal state is reached (with no time remaining in the game). In order to generate a prediction, I run a Monte Carlo simulation for N=1000 full games, and report stats on each team's points, the spread, and the over under for the game.

## Applications

<!--
>>> conf = json.loads('[[15, 0, -33.39848903585755, -9.263, 14.87248903585755], [200, -3, -35.16944469552113, -11.887, 11.395444695521128], [385, -3, -36.955616359555805, -14.466, 8.023616359555804], [399, -10, -46.71821627261272, -25.088, -3.457783727387284], [550, -10, -46.91034215858866, -26.294, -5.677657841411342], [733, -10, -39.5605380443652, -18.93, 1.700538044365203], [851, -10, -43.47027653023246, -23.4, -3.3297234697675364], [960, -13, -43.525394926029236, -25.437, -7.34860507397077], [1068, -13, -44.70392510567651, -26.278, -7.852074894323486], [1364, -16, -42.27898465953301, -27.123, -11.96701534046699], [1642, -9, -30.60123328962213, -16.252, -1.9027667103778683], [1690, -9, -29.923216120659355, -15.961, -1.9987838793406443], [1737, -2, -19.89276389751556, -5.414, 9.064763897515562], [1799, -2, -19.283882273426446, -5.141, 9.001882273426446], [1804, -2, -18.816598049524, -4.779, 9.258598049524], [1861, -2, -21.444195407429618, -7.243, 6.958195407429615], [2067, -2, -18.481474244598214, -5.392, 7.697474244598214], [2233, 5, -8.372837518280669, 3.213, 14.79883751828067], [2331, 5, -6.718110546511137, 4.707, 16.132110546511136], [2424, 5, -10.461976509740268, 0.649, 11.759976509740266], [2470, 5, -4.953512425440178, 5.861, 16.67551242544018], [2614, 5, -6.096537825641842, 3.325, 12.746537825641841], [2900, -2, -10.135038653925054, -2.542, 5.051038653925055], [3006, -2, -10.489100881087351, -3.912, 2.6651008810873513], [3425, -2, -3.582640605507485, -1.873, -0.1633593944925149], [3499, 6, 5.205512700181834, 5.924, 6.642487299818167], [3564, 6, 5.934786077482884, 5.998, 6.061213922517116]]')
>>> alt_state = json.loads('[37, 3, 276, 75, 21, 23]')
>>> alt_mc_res = json.loads('[[28.84, 6.460526294350949, {"5": 21.0, "10": 21.0, "25": 24.0, "50": 28.0, "75": 34.0, "90": 37.10000000000002, "95": 42.0}], [32.873, 7.0838457775420265, {"5": 23.0, "10": 23.0, "25": 30.0, "50": 30.0, "75": 37.0, "90": 44.0, "95": 44.0}], [-4.033, 11.019887068386863, {"5": -23.0, "10": -16.0, "25": -12.0, "50": -5.0, "75": 5.0, "90": 12.0, "95": 14.0}], [61.713, 7.8994070030604195, {"5": 50.95, "10": 51.0, "25": 57.0, "50": 61.0, "75": 66.0, "90": 72.0, "95": 75.0}]]')
>>> simulate._plot(conf, alt_state, alt_mc_res)

### 2019 Fiesta Bowl Turnover Call

When I was initially building out this model during the 2019 bowl season, I was natually attuned to interesting games that might make compelling case studies for the model. That year's Fiesta Bowl between Ohio State and Clemson featured a back-and-forth second half with several lead changes and turnovers. It was exactly the type of game where a single event going the other way could have dramatically changed the likely outcome. One particularly controversial call came late in the third quarter with Clemson up 21-16 when Tigers receiver Justyn Ross appeared to catch and fumble the ball, which the Ohio State defense recovered and ran in for the score:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">This was originally called a catch and fumble return TD, but was overturned as an incomplete pass. <a href="https://twitter.com/hashtag/CFBPlayoff?src=hash&amp;ref_src=twsrc%5Etfw">#CFBPlayoff</a> <a href="https://t.co/3RxiGYTvCv">pic.twitter.com/3RxiGYTvCv</a></p>&mdash; SportsCenter (@SportsCenter) <a href="https://twitter.com/SportsCenter/status/1211136453247414272?ref_src=twsrc%5Etfw">December 29, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

However, upon review the officiating crew determined that the pass was incomplete, so Clemson retained possession to punt it and Ohio State's points were taken off the board. Let's take a look at how the predicted outcome had varied up to that point:

![Fiesta Bowl spreads until controversial drop]({{ site.baseurl }}/images/2019_fiesta_bowl_confidence.png)

The simulation was predicting a 2 point Clemson win at the start of this drive.

-->

## Bowl Predictions

| Old Random Forests Prediction | New Monte Carlo + GNB Simulation | Actual Result |
| middle tenn state 24<br>**toledo (oh) 32** | middle tenn state 15<br>**toledo (oh) 28** | **middle tenn state 31**<br>toledo (oh) 24 |
| niu 25<br>**Coastal Carolina University 43** | niu 16<br>**Coastal Carolina University 33** | niu 41<br>**Coastal Carolina University 47** |
| western kentucky 32<br>**appalachian state 35** | western kentucky 20<br>**appalachian state 27** | **western kentucky 59**<br>appalachian state 38 |
| utep 17<br>**fresno state 32** | utep 10<br>**fresno state 34** | utep 24<br>**fresno state 31** |
| uab 24<br>**#12 byu 30** | uab 7<br>**#12 byu 46** | **uab 31**<br>#12 byu 28 |
| eastern michigan 23<br>**Liberty University 31** | eastern michigan 17<br>**Liberty University 25** | eastern michigan 20<br>**Liberty University 56** |
| **utah state 34**<br>oregon state 33 | **utah state 22**<br>oregon state 20 | **utah state 24**<br>oregon state 13 |
| **#16 la lafayet 30**<br>marshall (wv) 20 | **#16 la lafayet 28**<br>marshall (wv) 17 | **#16 la lafayet 36**<br>marshall (wv) 21 |
| **old dominion 31**<br>tulsa 25 | old dominion 18<br>**tulsa 21** | old dominion 17<br>**tulsa 30** |
| kent state 30<br>**wyoming 33** | kent state 19<br>**wyoming 24** | kent state 38<br>**wyoming 52** |
| #24 utsa 26<br>**s diego state 27** | **#24 utsa 25**<br>s diego state 19 | #24 utsa 24<br>**s diego state 38** |
| missouri 27<br>**army 43** | missouri 13<br>**army 35** | missouri 22<br>**army 24** |
| **unt 27**<br>miami (oh) 26 | unt 16<br>**miami (oh) 23** | unt 14<br>**miami (oh) 27** |
| ucf 31<br>**fla 34** | ucf 15<br>**fla 27** | **ucf 29**<br>fla 17 |
| memphis 29<br>hawai i 29 | **memphis 23**<br>hawai i 18 |  |
| georgia state 21<br>**ball state 31** | georgia state 18<br>**ball state 20** | **georgia state 51**<br>ball state 20 |
| western michigan 30<br>**nevada 42** | western michigan 17<br>**nevada 26** | **western michigan 52**<br>nevada 24 |
| **boston college 31**<br>east carolina 20 | **boston college 28**<br>east carolina 13 |  |
| #21 houston 25<br>**auburn 27** | **#21 houston 24**<br>auburn 23 | **#21 houston 17**<br>auburn 13 |
| **air force 30**<br>louisville 18 | air force 21<br>**louisville 30** | **air force 31**<br>louisville 28 |
| **mississippi state 36**<br>texas tech 23 | **mississippi state 32**<br>texas tech 14 | mississippi state 7<br>**texas tech 34** |
| ucla 30<br>**#18 nc state 33** | ucla 11<br>**#18 nc state 42** |  |
| west virginia 17<br>**minnesota 20** | west virginia 13<br>**minnesota 27** | west virginia 6<br>**minnesota 18** |
| **smu 44**<br>virginia 34 | smu 19<br>**virginia 33** |  |
| maryland 21<br>**virginia tech 28** | maryland 15<br>**virginia tech 25** | **maryland 54**<br>virginia tech 10 |
| **#19 clemson 27**<br>iowa state 24 | **#19 clemson 28**<br>iowa state 17 | **#19 clemson 20**<br>iowa state 13 |
| #15 oregon 28<br>**#14 oklahoma 33** | #15 oregon 19<br>**#14 oklahoma 25** | #15 oregon 32<br>**#14 oklahoma 47** |
| **n carolina 36**<br>south carolina 24 | **n carolina 29**<br>south carolina 14 | n carolina 21<br>**south carolina 38** |
| tennessee 29<br>**purdue 33** | tennessee 22<br>purdue 22 | tennessee 45<br>**purdue 48** |
| #13 pitt 28<br>#11 michigan state 28 | #13 pitt 21<br>**#11 michigan state 25** | #13 pitt 21<br>**#11 michigan state 31** |
| **wisconsin 23**<br>arizona state 13 | **wisconsin 24**<br>arizona state 20 | **wisconsin 20**<br>arizona state 13 |
| #20 wake forest (nc) 19<br>**#23 texas a&m 32** | #20 wake forest (nc) 19<br>**#23 texas a&m 27** |  |
| washington state 25<br>**miami (fl) 29** | washington state 11<br>**miami (fl) 39** |  |
| central michigan 22<br>**boise state 33** | central michigan 17<br>**boise state 24** |  |
| #4 cincinnati 23<br>**#1 alabama 36** | #4 cincinnati 12<br>**#1 alabama 42** | #4 cincinnati 6<br>**#1 alabama 27** |
| #3 georgia 24<br>**#2 michigan 31** | #3 georgia 21<br>**#2 michigan 33** | **#3 georgia 34**<br>#2 michigan 11 |
| penn state 22<br>**#22 arkansas 23** | penn state 13<br>**#22 arkansas 29** | penn state 10<br>**#22 arkansas 24** |
| **#17 iowa 24**<br>#25 kentucky 21 | **#17 iowa 21**<br>#25 kentucky 20 | #17 iowa 17<br>**#25 kentucky 20** |
| **#9 oklahoma state 23**<br>#5 notre dame 20 | #9 oklahoma state 18<br>**#5 notre dame 29** | **#9 oklahoma state 37**<br>#5 notre dame 35 |
| #10 utah 24<br>**#7 ohio state 40** | #10 utah 14<br>**#7 ohio state 38** | #10 utah 45<br>**#7 ohio state 48** |
| **#6 baylor 32**<br>#8 ole miss 23 | #6 baylor 22<br>**#8 ole miss 25** | **#6 baylor 21**<br>#8 ole miss 7 |
| **lsu 22**<br>kansas state 20 | **lsu 24**<br>kansas state 17 | lsu 20<br>**kansas state 42** |

## Up Next

Later in the Bowl Season, I plan to analyze some close results by looking at alternative universes where a call went a different direction, and see how that would've affected the predicted outcome and the variance on that outcome. I may also work on a way to visualize the confidence of my various predictions, and perhaps a peek into some of the specific predicted drive summaries on either extreme of my higher variance predictions. Stay tuned!

<!--
## Improvements

### Features

* pass and rush yard averages
* defensive stats: sacks, picks, fumbles recovered
* individual qb stats: can capture personnel changes, allow for some inference after the offseason
* bowl game features: distance, prestige, how likely teams are to care

### Better simulation

* overtime
* kickoffs
* punts and returns
* simulate pat separately from touchdown
* play by play?

### Other Models

* GPR
* HMM
* Regression for yards/duration
-->
