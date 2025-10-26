# FieldGen: From Teleoperated Pre-Manipulation Trajectories to Field-Guided Data Generation

- **Authors:** Wenhao Wang, Kehe Ye, Xinyu Zhou, Tianxing Chen, Cao Min, Qiaoming Zhu, Xiaokang Yang, Yongjian Shen, Yang Yang, Maoqing Yao, Yao Mu
- **Published:** 2025-10-23T17:47:12Z
- **Source:** http://arxiv.org/abs/2510.20774v1

## Abstract
Large-scale and diverse datasets are vital for training robust robotic
manipulation policies, yet existing data collection methods struggle to balance
scale, diversity, and quality. Simulation offers scalability but suffers from
sim-to-real gaps, while teleoperation yields high-quality demonstrations with
limited diversity and high labor cost. We introduce FieldGen, a field-guided
data generation framework that enables scalable, diverse, and high-quality
real-world data collection with minimal human supervision. FieldGen decomposes
manipulation into two stages: a pre-manipulation phase, allowing trajectory
diversity, and a fine manipulation phase requiring expert precision. Human
demonstrations capture key contact and pose information, after which an
attraction field automatically generates diverse trajectories converging to
successful configurations. This decoupled design combines scalable trajectory
diversity with precise supervision. Moreover, FieldGen-Reward augments
generated data with reward annotations to further enhance policy learning.
Experiments demonstrate that policies trained with FieldGen achieve higher
success rates and improved stability compared to teleoperation-based baselines,
while significantly reducing human effort in long-term real-world data
collection. Webpage is available at https://fieldgen.github.io/.

## ELI5
Training agricultural robots is tricky because crops are fragile and each farm has unique layouts. FieldGen starts by letting skilled operators teleoperate robots through delicate pre-manipulation motions—approaching plants, brushing leaves aside, or setting up a grasp—while sensors record every nuance. Those trajectories seed a simulator that faithfully recreates geometry and forces observed in the field, allowing the robot to generate countless safe variations that still respect biological constraints. The simulator provides gentle guidance, nudging the robot away from unrealistic motions and toward strategies consistent with what humans demonstrated. Over time, the robot amasses a dataset of near-real experiences without trampling actual plants, learning how to position itself before more aggressive manipulations. When deployed back on the farm, it acts like a worker who has rehearsed every approach in a risk-free greenhouse but whose moves were choreographed by real agronomists.
