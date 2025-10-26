# Some Studies in Machine Learning Using the Game of Checkers

- **Authors:** Arthur L. Samuel
- **Year:** 1959
- **Source:** https://doi.org/10.1147/rd.33.0210

## Abstract
This paper describes experiments in programming a digital computer to play a better game of checkers than the person who wrote the program. The learning scheme combines rote learning from self-play with parameter adjustment based on a search of promising board positions. Alternative evaluation functions and pruning strategies are examined, and the program is shown to improve through experience, eventually achieving tournament-level performance. The results demonstrate that a machine can be made to learn from experience in a complex domain without exhaustive enumeration.

## ELI5
Samuel treated his computer like an eager junior chess club member. At first it only knew the basic rules of checkers, so it played clumsy games against itself and memorized which moves led to wins or embarrassing losses. After every match it nudged dials inside its evaluation function—rewarding board patterns that seemed to help and demoting the ones that got it trapped. It even peeked a few moves ahead, pruning hopeless branches the way a careful kid might stop exploring obviously bad plays. Over thousands of rainy afternoons the apprentice sharpened its instincts, until one day it quietly beat its creator. The experiment proved that a machine could practice, reflect, and genuinely improve at a strategic task instead of following a giant cheat sheet.
