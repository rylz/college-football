---
title: 2022 National Championship Predictions
layout: post
excerpt: Before the national championship game kicks off tonight, I want to share my 2 models' predictions, as well as a peek into the variance I'm seeing in my Monte Carlo simulation.
image: /images/2022_national_championship_drive_predictions.png
---

Before the national championship game kicks off tonight, I want to share my 2 models' predictions, as well as a peek into the variance I'm seeing in my Monte Carlo simulation.

### Predictions

Interestingly, both models predict a double-digit Alabama victory, in stark contrast to Vegas' Georgia -2.5 spread.

My Random Forests score prediction model predicts: Georgia 23 - **27 Alabama**.

My Gaussian Naive Bayes drive simulation model (evaluated across 1000 simulations) predicts: Georgia 15 - **42 Alabama**.

I suspect that my models, both of which are backed by a pagerank graph trained on margin of victory across all games this season, may essentially be overfitting to the result of the SEC championship last month between the same teams, in which Alabama prevailed 41-24. I've heard many compelling reasons from sportswriters and pundits over the past week why we shouldn't assume the same outcome will repeat itself:
* Georgia was already assured a playoff berth, regardless of the outcome of the SEC championship, so they may have failed to prepare as well and take that game as seriously as they will take this one. Kirby Smart has been known to hold his cards close to his chest re: game planning and adjustments until absolutely necessary to reveal them.
* Georgia looked unstoppable in their dismantling of #2 Michigan in the Orange Bowl. More importantly, their particular strength and speed on defense showed that they had already made substantial adjustments and improvements in that department compared to their performance in the SEC championship.

None of these reasons would be captured by either of my models, with the possible exception of a stronger defensive showing against Michigan marginally improving their predicted performance in the drive simulator. Still, I have to admit I've been skeptical of sportswriter theories that the above-mentioned factors mean this will likely be a close game. Nothing about that SEC championship win felt flukey - that looked like an Alabama team that wins 9/10 times they meet Georgia on the field.

### Variance

As I've noted in past blogs, one of the advantages of the Monte Carlo+Gaussian Naive Bayes model is that I can measure variance of its predictions. In a game where my prediction (Alabama blowout) differs so much from the Vegas/pundit consensus (a Georgia win in a close game), it's particularly interesting to understand just how confident this prediction is.

First, as a simple visualization of the range of predicted outcomes in the 1000 simulations I ran, this is a plot of the spread over time in all of those simulations. Games are represented as transparent red lines, so that regions of the graph with many predictions render as a more opaque/darker red. While there's certainly a darker region of the graph progressing towards a double-digit Alabama blowout, it's easy to eyeball the graph and see that there are plenty of simulations where Georgia does win, at times by large margins.

![National Championship Drive Simulations]({{ site.baseurl }}/images/2022_national_championship_drive_predictions.png)

Our mean predicted spread is Alabama by 27, but the standard deviation is a whopping 21 points! Some of this is the nature of trying to predict a college football game in this manner - these are high variance events to predict. But, this spread in particular is a high variance one compared to others I've looked at this year. To contextualize this, here are some percentiles for the spread:

| Percentile | Outcome |
| 5 | Alabama +62 |
| 10 | Alabama +56 |
| 25 | Alabama +43 |
| 50 | Alabama +29 |
| 75 | Alabama +14 |
| 90 | Regulation Tie |
| 95 | Georgia -8 |

In summary, even though I'm predicting an Alabama blowout, there's a 10% chance in this model that Georgia does in fact pull off a tie or better in regulation. For entertainment's sake, I hope we end up getting a game from over on that end of the distribution tonight!

### Bowl Season Updates

For now, I've simply updated the table in the previous post to include actual results of bowl games. I'll do a more thorough analysis and retrospective after the championship game!
