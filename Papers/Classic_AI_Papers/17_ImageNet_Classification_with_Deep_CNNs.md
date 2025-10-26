# ImageNet Classification with Deep Convolutional Neural Networks

- **Authors:** Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
- **Year:** 2012
- **Source:** https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf

## Abstract
We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into 1000 different classes. On the test data we achieve top-1 and top-5 error rates of 37.5% and 17.0%, considerably better than the previous state-of-the-art. The network has 60 million parameters, uses ReLU nonlinearities, overlapping pooling, data augmentation, dropout regularization, and is trained on two GPUs.

## ELI5
AlexNet is the computer vision equivalent of strapping a jet engine onto an old biplane. By stacking many convolutional layers with ReLU activations, sprinkling in tricks like dropout and data augmentation, and training on GPUs, the authors taught the network to recognize cats, lamps, and snowplows across a million photos. It doesn’t memorize entire images; it learns to detect edges, textures, and object parts that can be recombined for any class. When the ImageNet challenge results came out, AlexNet’s error rate was so much lower than everyone else’s that the community immediately realized deep CNNs plus GPUs were the future of vision.
