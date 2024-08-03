---
title: 'Mixed Policies and AI Assistance'
date: 2024
draft: true
math: true
toc: true
author: Niklas
tags:
    - research
categories:
    - Research
    - Reinforcement Learning
---

Let me tell you about the project I am currently working on.

# AI Assistance
We consider the kind of AI assistance that you might get from Google Maps. You have a goal (= get somewhere) and the assistant (= Google Maps) tells you, at each point where you have to make a decision (= take a turn), what to do. However, is it guaranteed that you will always follow the advice? Not really. You might be disctracted and miss a turn, or you don't trust what it says, or you saw something that intrigued you and you purposely went off course.

Bottom line: It is common to ignore AI assistance, but can the assistant deal with it?

# Mixed Policies
To model the above problem, let us consider two policies: $\pi$, a.k.a. what the user would do on his own, and $\pi^\mathrm{sup}$, which is what the supervisor suggests. We link these two policies with a single probability $\phi \in [0,1]$ which corresponds to the probability that the user accepts and performs the suggested action.
In this way, we obtain a new, *collaborative* policy
$$\pi^\phi(a \mid s) = (1-\phi)\pi(a \mid s) + \phi\pi^\mathrm{sup}(a \mid s).$$

The parameter $\phi$ can be very flexible and depend on a lot of factors such as the time step $t$, the suggested action $a^\mathrm{sup} \sim \pi^\mathrm{sup}(\cdot \mid s)$, the user action $a \sim \pi(\cdot \mid s)$, etc.

We consider a few interesting use cases of this model in the following sections.

## Use Case 1: $\pi^\mathrm{sup} = \pi^\star$ and $\phi$ is constant
A simple case is when the supervisor policy is equal to the optimal policy of the MDP, and $\phi$ is set to a constant value.

## Use Case 2: Integrate $\pi$ into the environment
Now we get closer to the original question: How to train an optimal AI assistant that is attuned to the user's particular behavior? By integrating the occasional disobedience into the environment, we obtain a different kind of MDP whose optimal policy would correspond to the optimal assistant for a user with policy $\pi$ and acceptance $\phi$. Let's see a small example of this.

...

## Experiment: Decaying $\phi$ makes assistants less annoying
This is a fun experiment that showcases the versatility of this model. So far, 