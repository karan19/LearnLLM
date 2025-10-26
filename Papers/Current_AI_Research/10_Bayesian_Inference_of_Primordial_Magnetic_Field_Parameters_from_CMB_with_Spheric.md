# Bayesian Inference of Primordial Magnetic Field Parameters from CMB with Spherical Graph Neural Networks

- **Authors:** Juan Alejandro Pinto Castro, Héctor J. Hortúa, Jorge Enrique García-Farieta, Roger Anderson Hurtado
- **Published:** 2025-10-23T17:56:04Z
- **Source:** http://arxiv.org/abs/2510.20795v1

## Abstract
Deep learning has emerged as a transformative methodology in modern
cosmology, providing powerful tools to extract meaningful physical information
from complex astronomical datasets. This paper implements a novel Bayesian
graph deep learning framework for estimating key cosmological parameters in a
primordial magnetic field (PMF) cosmology directly from simulated Cosmic
Microwave Background (CMB) maps. Our methodology utilizes DeepSphere, a
spherical convolutional neural network architecture specifically designed to
respect the spherical geometry of CMB data through HEALPix pixelization. To
advance beyond deterministic point estimates and enable robust uncertainty
quantification, we integrate Bayesian Neural Networks (BNNs) into the
framework, capturing aleatoric and epistemic uncertainties that reflect the
model confidence in its predictions. The proposed approach demonstrates
exceptional performance, achieving $R^{2}$ scores exceeding 0.89 for the
magnetic parameter estimation. We further obtain well-calibrated uncertainty
estimates through post-hoc training techniques including Variance Scaling and
GPNormal. This integrated DeepSphere-BNNs framework not only delivers accurate
parameter estimation from CMB maps with PMF contributions but also provides
reliable uncertainty quantification, providing the necessary tools for robust
cosmological inference in the era of precision cosmology.

## ELI5
Detecting primordial magnetic fields is like inferring the presence of faint winds by only watching ripples on a spherical pond. The authors drape a graph neural network directly over the celestial sphere, connecting each pixel of the cosmic microwave background to its neighbors so local patterns can inform one another. This network feeds a Bayesian inference head that outputs not just a single estimate but a full probability distribution over magnetic field parameters, acknowledging the uncertainty inherent in cosmic observations. By respecting spherical geometry, the model avoids distortions that plague flat projections and captures correlations that span large angular distances. The approach blends physics priors with data-driven flexibility, allowing cosmologists to test hypotheses about early-universe magnetism more rigorously. It essentially equips astronomers with a smart stethoscope tuned to the universe's heartbeat, capable of distinguishing subtle murmurs from measurement noise.
