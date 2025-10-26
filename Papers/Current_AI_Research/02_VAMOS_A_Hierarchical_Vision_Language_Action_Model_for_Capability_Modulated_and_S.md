# VAMOS: A Hierarchical Vision-Language-Action Model for Capability-Modulated and Steerable Navigation

- **Authors:** Mateo Guaman Castro, Sidharth Rajagopal, Daniel Gorbatov, Matt Schmittle, Rohan Baijal, Octi Zhang, Rosario Scalise, Sidharth Talia, Emma Romig, Celso de Melo, Byron Boots, Abhishek Gupta
- **Published:** 2025-10-23T17:59:45Z
- **Source:** http://arxiv.org/abs/2510.20818v1

## Abstract
A fundamental challenge in robot navigation lies in learning policies that
generalize across diverse environments while conforming to the unique physical
constraints and capabilities of a specific embodiment (e.g., quadrupeds can
walk up stairs, but rovers cannot). We propose VAMOS, a hierarchical VLA that
decouples semantic planning from embodiment grounding: a generalist planner
learns from diverse, open-world data, while a specialist affordance model
learns the robot's physical constraints and capabilities in safe, low-cost
simulation. We enabled this separation by carefully designing an interface that
lets a high-level planner propose candidate paths directly in image space that
the affordance model then evaluates and re-ranks. Our real-world experiments
show that VAMOS achieves higher success rates in both indoor and complex
outdoor navigation than state-of-the-art model-based and end-to-end learning
methods. We also show that our hierarchical design enables cross-embodied
navigation across legged and wheeled robots and is easily steerable using
natural language. Real-world ablations confirm that the specialist model is key
to embodiment grounding, enabling a single high-level planner to be deployed
across physically distinct wheeled and legged robots. Finally, this model
significantly enhances single-robot reliability, achieving 3X higher success
rates by rejecting physically infeasible plans. Website:
https://vamos-vla.github.io/

## ELI5
Picture a robot tour guide crossing a city it has never seen. Up in a blimp sits a strategist who pores over satellite photos, street names, and verbal instructions, outlining candidate routes just like a human reading Google Maps directions. Down on the sidewalk, a second coach walks beside the robot, remembering that this particular body can roll fast on asphalt but hates steps and slippery tiles. Each time the planner suggests a route, the coach evaluates it in raw image space—almost like overlaying tracing paper of what the robot's camera would see—and rejects turns that exceed the robot's abilities. Because the messages stay visual, the same planner can serve many robots while each robot keeps its personalized capability filter. Natural-language steering lets people nudge the planner with phrases such as "avoid crowds" or "prefer sunny paths," which the coach translates into concrete constraints. Together they form a layered brain that is adventurous yet self-aware, delivering safer navigation without retraining the entire stack for every new chassis.
