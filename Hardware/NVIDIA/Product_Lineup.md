# NVIDIA Hardware Units & Systems

Summary of current NVIDIA offerings relevant to LLM training/inference. Each entry includes a precise description and an ELI5 helper.

## Hopper H100 GPU
**Definition:** Flagship data-center GPU with 80 GB HBM3 (PCIe) or 96 GB HBM3 (SXM), fourth-gen tensor cores, Transformer Engine (FP8), and up to 3.35 TB/s memory bandwidth. Supports NVLink/NVSwitch fabric and MIG partitioning.
**ELI5:** NVIDIA’s top-tier chef—massive pantry, super-fast mixers, and private hallways to other chefs for group banquets.

## Hopper H200 GPU
**Definition:** Upgraded Hopper variant pairing HBM3e (141 GB, 4.8 TB/s bandwidth) for larger context windows and faster model training, keeping the same SM count but boosting memory-bound workloads.
**ELI5:** Same master chef as H100 but with a mega pantry stocked with faster ingredients.

## Grace Hopper Superchip (GH200)
**Definition:** Package combining a Grace CPU (Arm Neoverse) and Hopper GPU via high-bandwidth NVLink-C2C, sharing coherent memory and up to 480 GB LPDDR5X + 96/141 GB HBM3 memory.
**ELI5:** A CPU brain and GPU muscle stitched together so they share the same giant fridge without arguing.

## Ada L40S GPU
**Definition:** Ada Lovelace-based data-center GPU with 48 GB GDDR6, optimized for graphics + inference workloads, offering FP8 Tensor Cores and NVENC/AV1 support.
**ELI5:** A versatile sous-chef that handles both drawing pictures and serving chatbot responses.

## A100 GPU
**Definition:** Previous-generation Ampere GPU (40/80 GB HBM2e) still widely used for LLM training. Provides third-gen tensor cores, sparsity acceleration, and strong FP16/BF16 throughput.
**ELI5:** Last season’s star chef—slightly older but still runs a busy kitchen reliably.

## L4 GPU
**Definition:** Low-profile PCIe accelerator with 24 GB GDDR6 for video analytics and light inference. Targets edge/data-center cost-sensitive deployments.
**ELI5:** A slim assistant chef that fits into small food trucks to handle lighter menus.

## Jetson Orin / Jetson AGX
**Definition:** Embedded AI modules combining Arm CPUs, Ampere GPUs, and accelerators for robotics and edge applications, with power envelopes from 15W to 60W.
**ELI5:** Portable chef backpacks for robots—enough cooking gear to operate on a drone or robot dog.

## DGX H100 System
**Definition:** Integrated 8× H100 SXM platform with NVSwitch, dual Grace CPUs, 640 GB HBM, 4× NVMe, and ConnectX-7 networking. Ready-made node for training clusters.
**ELI5:** A pre-built kitchen with eight master chefs already wired together—just plug in recipes.

## HGX H100 Baseboard
**Definition:** Reference server design (tray) that OEMs integrate, providing 4 or 8 H100 SXM GPUs with NVLink, shared power delivery, and liquid/air cooling support.
**ELI5:** A modular stovetop where you mount multiple chefs so hardware vendors can build custom kitchens.

## DGX GH200 / NVL72
**Definition:** Rack-scale system interconnecting 72 Grace Hopper superchips via NVLink Switch System, delivering 1.44 TB of HBM3 memory with shared addressing.
**ELI5:** A skyscraper full of CPU-GPU pairs all sharing pantry elevators for ultra-large models.

## ConnectX-7 / BlueField-3 NIC
**Definition:** Smart network adapters offering 400 Gb/s InfiniBand or Ethernet plus DPUs for offloading security and storage tasks, critical for GPU cluster fabrics.
**ELI5:** Network sous-chefs that carry dishes between kitchens at lightning speed while handling security checkpoints.

## Quantum-2 InfiniBand Switch
**Definition:** 400 Gb/s InfiniBand switching platform providing adaptive routing, SHARP in-network reductions, and end-to-end congestion control for large GPU clusters.
**ELI5:** The highway interchange keeping thousands of delivery trucks from crashing when all the chefs trade dishes.

## NVIDIA Base Command Platform
**Definition:** Managed software stack that orchestrates DGX fleets, providing scheduling, monitoring, storage integration, and curated containers for training workflows.
**ELI5:** Restaurant management software that assigns cooking stations, tracks orders, and files paperwork automatically.

## Triton Inference Server (formerly TensorRT Inference Server)
**Definition:** Open-source serving framework optimized for NVIDIA GPUs, supports ensembles, dynamic batching, multi-framework models, and integrates with TensorRT/ONNX Runtime.
**ELI5:** A front-of-house supervisor that routes incoming meal orders to whichever chef can respond fastest.
