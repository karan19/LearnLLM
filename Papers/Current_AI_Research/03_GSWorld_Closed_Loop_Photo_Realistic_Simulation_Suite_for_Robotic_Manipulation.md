# GSWorld: Closed-Loop Photo-Realistic Simulation Suite for Robotic Manipulation

- **Authors:** Guangqi Jiang, Haoran Chang, Ri-Zhao Qiu, Yutong Liang, Mazeyu Ji, Jiyue Zhu, Zhao Dong, Xueyan Zou, Xiaolong Wang
- **Published:** 2025-10-23T17:59:26Z
- **Source:** http://arxiv.org/abs/2510.20813v1

## Abstract
This paper presents GSWorld, a robust, photo-realistic simulator for robotics
manipulation that combines 3D Gaussian Splatting with physics engines. Our
framework advocates "closing the loop" of developing manipulation policies with
reproducible evaluation of policies learned from real-robot data and sim2real
policy training without using real robots. To enable photo-realistic rendering
of diverse scenes, we propose a new asset format, which we term GSDF (Gaussian
Scene Description File), that infuses Gaussian-on-Mesh representation with
robot URDF and other objects. With a streamlined reconstruction pipeline, we
curate a database of GSDF that contains 3 robot embodiments for single-arm and
bimanual manipulation, as well as more than 40 objects. Combining GSDF with
physics engines, we demonstrate several immediate interesting applications: (1)
learning zero-shot sim2real pixel-to-action manipulation policy with
photo-realistic rendering, (2) automated high-quality DAgger data collection
for adapting policies to deployment environments, (3) reproducible benchmarking
of real-robot manipulation policies in simulation, (4) simulation data
collection by virtual teleoperation, and (5) zero-shot sim2real visual
reinforcement learning. Website: https://3dgsworld.github.io/.

## ELI5
GSWorld is like giving robot hands their own blockbuster movie studio. Engineers can build dazzling kitchens, labs, or factory lines that look indistinguishable from reality thanks to 3D Gaussian splatting, then invite their digital robots to rehearse fine motor skills on props that match real-world geometry and texture. After each take, the simulator provides precise notes—where a gripper slipped, how much force bent a spoon, whether a shadow fooled the vision system—so the humans can adjust policies, lighting, or physics and immediately run the scene again. Because the loop is closed, data collected in the simulator can be validated against real robot logs, ensuring the virtual stage does not drift into fantasy. Teams can scale experiments to hundreds of parallel scenes without risking hardware or burning operator hours, and they can rewind to replay tricky sequences frame by frame. When the polished policy finally steps onto a physical set, it behaves less like a nervous understudy and more like an actor who has already nailed the choreography under studio lights.
