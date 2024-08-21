---
title: 'Tackling the Bickley Jet'
date: 2024-08-04
draft: true
math: true
toc: true
author: Niklas
image: cover.jpg
tags:
    - research
    - physics
categories:
    - Research
---

In my previous post covering the content of my Bachelor's and Master's theses, I mentioned that the latter was not quite well-rounded. I attempted to discover simplified dynamics for two different velocity fields, that also respected the history force. The framework I used was SINDy. For a simple vortex, SINDy's approach worked, but for the Bickley Jet, it failed quite miserably.

<!-- Plot of Bickley Jet trajectory -->

Even after submitting the thesis and putting an end to the project, it still kept bugging me that it didn't work. Not only that, but also that I couldn't properly explain *why* it didn't work. Now, to be fair with myself, this is not so straightforward. SINDy's success depends largely on the chosen function space, and the number of those are infinite. I tried a few sensible ones, and it didn't work for them, but that does not mean it won't work at all. It just means I haven't tried hard enough.

## Giving SINDy another shot

## Approximating just the history force
Since the computationally intensive part is the history force, it makes sense to only approximate that, and leave the rest to an accurate solver.
This has actually been done in a different work, using an LSTM. LSTMs are a very good choice for this because the history force is a memory term.
In this section, I would like to reproduce their approach and see how well it works for the Bickley jet.

Further, we can try other approaches. Since transformers have been such a hype recently and have taken over the role of RNNs, maybe they work even better?

## Finding a nice formula for the vortex dynamics

## Are the two errors related?
In my thesis, I defined two error terms: trajectory error and derivative error. The first one measures how well the predicted and true trajectories align, while the latter only measures it for the derivative. It is much easier to compute the derivative loss because there is no ODE solving involved. I remember always being very anxious about predicting trajectories, because for large SINDy models, the solver would usually crash and produce a cryptic error message.
The question is: Does the derivative loss tell us *anything* about the trajectory loss? Mainly, I am looking for an inequality such as $\mathcal L_\mathrm{deriv} \leq \mathcal L_\mathrm{traj}$. Or alternatively, to show that there are cases where both directions of the inequality are possible.