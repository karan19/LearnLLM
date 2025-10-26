# GPS: A Program that Simulates Human Thought

- **Authors:** Allen Newell, Herbert A. Simon, J. Clifford Shaw
- **Year:** 1959
- **Source:** https://doi.org/10.1126/science.129.3364.82

## Abstract
The General Problem Solver (GPS) is a heuristic program that seeks solutions to a wide range of formal problems by separating the description of task environments from a general reasoning mechanism. GPS represents problems as differences between current and goal states and applies means–ends analysis to select operators that reduce salient differences. Implementation within the IPL-V list-processing language is outlined, and examples from logic, algebra, and puzzle domains illustrate the program’s human-like solution traces.

## ELI5
Newell and Simon imagined a pair of tireless graduate students tackling any puzzle the same way: first write down what state you are in, what state you want, and then keep shrinking the differences. GPS captures that strategy in code. Give it the rules of algebra or the layout of the Towers of Hanoi, and it immediately scribbles a to-do list of differences—"top disk in wrong place," "equation not isolated"—then picks operators that nibble those gaps away. Watching GPS work is like watching a careful human reason aloud: it describes each subgoal, picks a move, checks whether the world looks closer to the target, and backtracks when it drifts. Even though GPS was slow and brittle by today’s standards, it planted the idea that a single reasoning engine could, with the right domain facts, mimic the step-by-step problem solving we perform in our heads.
