# GPU Terminology Glossary

Common hardware terms you will encounter when evaluating or tuning accelerators for AI workloads. Each entry includes a precise definition plus an ELI5 mental model.

## Streaming Multiprocessor (SM)
**Definition:** Fundamental compute block inside NVIDIA GPUs containing CUDA cores, tensor cores, warp schedulers, and caches. Workloads are distributed across many SMs in parallel.
**ELI5:** Think of each SM as a mini kitchen with its own chefs; more kitchens mean more meals cooked at once.

## CUDA Core / Shader Core
**Definition:** Scalar execution unit that processes individual threads within a warp. Handles standard FP32/INT32 math.
**ELI5:** A single line cook chopping veggies; thousands work together to feed the whole restaurant.

## Tensor Core
**Definition:** Specialized matrix-multiply hardware that performs mixed-precision MACs at very high throughput, accelerating AI workloads.
**ELI5:** A high-speed blender that mixes giant batches of ingredients in one go instead of stirring by hand.

## Warp / Wavefront
**Definition:** Group of threads (32 on NVIDIA, 64 on AMD) scheduled and executed in lockstep on an SM.
**ELI5:** A squad of dancers moving in sync—if one pauses, everyone waits.

## VRAM / HBM / GDDR
**Definition:** On-board memory used to store model weights, activations, and intermediate tensors. HBM (High Bandwidth Memory) offers huge throughput; GDDR is common on consumer GPUs.
**ELI5:** The pantry right next to the kitchen; bigger and faster pantries mean chefs waste less time grabbing ingredients.

## Memory Bandwidth
**Definition:** Rate at which data can move between VRAM and compute units, typically measured in GB/s.
**ELI5:** How wide the hallway is between pantry and kitchen—wider halls prevent traffic jams.

## PCIe / NVLink / NVSwitch
**Definition:** Interconnects that let GPUs communicate with CPUs or each other. PCIe is ubiquitous; NVLink/NVSwitch provide much higher GPU↔GPU bandwidth.
**ELI5:** Delivery roads between kitchens—NVLink is an express highway, PCIe is city streets.

## GPU Utilization
**Definition:** Percentage of time compute units are busy. Low utilization can indicate bottlenecks such as memory, I/O, or kernel launch overhead.
**ELI5:** If chefs spend half the time waiting for groceries, the restaurant isn’t running at full tilt.

## Tensor Memory Accelerator (TMA) / DMA Engine
**Definition:** Hardware units that copy data between memory regions asynchronously, overlapping transfers with compute.
**ELI5:** Conveyor belts that restock the kitchen while cooks keep working.

## Memory Capacity vs. Memory Footprint
**Definition:** Capacity is how much VRAM is available; footprint is how much your model + activations consume. Techniques like activation checkpointing or tensor parallelism shrink the footprint.
**ELI5:** Pantry size vs. how many ingredients you actually store; organization tricks cram more into the same shelves.

## Thermal Design Power (TDP)
**Definition:** Maximum sustained power the cooling system must dissipate, roughly matching typical workload consumption.
**ELI5:** How much heat the stove gives off—higher TDP needs bigger vents and fans.

## Clock Speed (Core / Memory)
**Definition:** Operating frequency of compute cores and memory chips; higher clocks can boost throughput but increase power and heat.
**ELI5:** Turning the kitchen timer faster so chefs move quicker—great as long as they don’t burn out.

## Mixed Precision (FP32/FP16/BF16/INT8)
**Definition:** Using lower-precision data types to gain throughput and reduce memory usage while keeping acceptable accuracy.
**ELI5:** Measuring ingredients with teaspoons instead of tablespoons to prep faster, as long as the recipe still tastes good.

## MIG (Multi-Instance GPU)
**Definition:** NVIDIA A100/H100 feature that partitions a single GPU into isolated slices with dedicated compute, memory, and cache.
**ELI5:** Dividing one big kitchen into smaller private kitchens so multiple chefs can cook different meals without bumping into each other.

## NVMe Offload / Unified Memory
**Definition:** Techniques that page data between system storage/DRAM and VRAM automatically, enabling larger models than GPU memory alone permits.
**ELI5:** Borrow shelf space from the basement pantry and send a dumbwaiter up whenever the chefs need more supplies.

## FP8 / Transformer Engine
**Definition:** NVIDIA Hopper feature that dynamically selects precision (FP8, FP16, FP32) per tensor to maximize performance while maintaining accuracy.
**ELI5:** Smart measuring cups that decide on-the-fly how fine-grained to be for each ingredient.

## SM Occupancy
**Definition:** Ratio of active warps to the theoretical maximum per SM. Influenced by register usage, shared memory, and thread-block sizing.
**ELI5:** How many seats are filled at each kitchen station; empty seats mean wasted hardware.

## Kernel Launch Overhead
**Definition:** CPU-side cost of dispatching GPU kernels. Dominates when running many small kernels instead of fewer large ones.
**ELI5:** Every time you shout a new order to the kitchen it takes a moment—too many tiny orders slow everything down.

## Interconnect Topology
**Definition:** Graph describing how GPUs are wired together (ring, fully connected, mesh). Impacts all-to-all collectives and parallelism strategies.
**ELI5:** Seating chart showing which chefs can hand plates directly to each other without passing through the whole dining room.
