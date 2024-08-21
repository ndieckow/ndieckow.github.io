---
title: 'Theses'
date: 2023-11-26
tags:
    - studying
categories:
    - Studying
image: image.jpg
---

Yesterday, I submitted my Master's thesis. I am so happy that this moment finally came! While it was a great learning experience, I can't say that I have enjoyed it throughout. Especially nearing the end, I just wanted to be done. On this page, I want to share both of my theses (Bachelor's and Master's) with anybody who is interested in them.

## Bachelor's Thesis
My Bachelor's thesis is titled "Methods of Machine Learning and their Application to the Repair Limit Replacement Problem". It was mainly an introduction to reinforcement learning and covered concepts such as Markov Decision Processes, the Bellman equation, value iteration and Q-learning. I then applied both value iteration and Q-learning to a toy problem (inspired by Hasting's 1969 paper "The Repair Limit Replacement Method") and compared the two approaches.

[Link to Bachelor's thesis](bachelors_thesis.pdf)

Reading the theoretical part again, I have to pat myself on the shoulder, because it is quite a nice introduction to the basic concepts of reinforcement learning. However, I always skip over the application part, because it's lame and pointless. Funnily, I feel the same about my Master's thesis. Even though I would call myself more of a practical person than a theoretically-minded one. Hmm...

In hindsight, I wish I had also covered the policy iteration. Maybe, I will extend this thesis in the future, also including advanced topics like deep reinforcement learning (i.e. estimating the state-value or state-action functions by a neural network). Also, I could have at least mentioned Monte Carlo and Temporal Difference methods. And, I'd finally make the application part actually interesting and useful.

## Master's Thesis
My Master's thesis is titled "Data-driven Approaches for the Maxey-Riley Equation". It is an introduction to the field of system identification, although it focuses mainly on the SINDy (Sparse Identification of Nonlinear Dynamics) algorithm. I apply this to the Maxey-Riley equation -- an ODE that describes the motion of an inertial particle in a turbulent fluid. This ODE contains a tricky integral term which requires any exact solver to store the entire particle trajectory in memory, and also causes the computation time to grow quadratically in the trajectory length. The idea was to see whether one could find an approximation of an ODE as a dynamical system, using SINDy.

[Link to Master's thesis](masters_thesis.pdf)

I'm happy with the theoretical part. You can tell that I invested a lot of time into researching the literature and I am quite satisfied with my work in that regard. The application part is a bit short, unfortunately. To be quite frank: It was frustrating most of the time, and felt pretty pointless. The MRE isn't even a dynamical system, why should I be able to find a good approximation using one? In my opinion, the topic was flawed from the start, but I was too stupid to realize it back then. The good news is: This shows that I learned something 😄

If I could do it all over again, I would, first of all, pick a different problem. But if that wasn't an option, I would implement the SINDy algorithm myself. I used the existing implementation, PySINDy, which is great, but I never took the time to get into the nitty-gritty of it. I never got my hands dirty. So when I wanted to try things that were not directly supported, but would have been theoretically possible, I simply didn't do them or implemented ugly hacks, which only led to further frustration. Also, had I implemented it myself, it would have felt like more of an achievement; something that I actually did.

---

To finish this off, I am very grateful for my time as a student. I was able to learn a lot, both in terms of knowledge and in terms of being a good scientist, and I am confident that I can take some good steps in the future, because of this.

> Cover image: [Unsplash](https://unsplash.com/de/fotos/weisses-druckerpapier-lot-5cFwQ-WMcJU)