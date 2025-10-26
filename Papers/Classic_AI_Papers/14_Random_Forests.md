# Random Forests

- **Authors:** Leo Breiman
- **Year:** 2001
- **Source:** https://doi.org/10.1023/A:1010933404324

## Abstract
Random forests are ensembles of decision trees grown on bootstrap samples with random feature selection at each split. The method is shown to yield error rates that compare favorably with Adaboost while being more robust to noise and overfitting. We analyze generalization error, variable importance measures, and connections to the strength and correlation of individual trees.

## ELI5
Breiman suggested planting a whole forest of slightly quirky decision trees instead of trusting a single giant oak. Each tree sees a different bootstrap sample of the data and must pick splits from a random subset of features, so no two trees grow identically. When it’s time to make a prediction, every tree votes and the majority wins, which cancels out individual overreactions to noise. The forest also keeps score of which features were most useful across trees, giving you insight into the data. It’s like asking dozens of independent doctors for a diagnosis—you trust the consensus far more than any lone opinion.
