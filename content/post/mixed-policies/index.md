---
title: 'Mixed Policies and AI Assistance'
date: 2024-08-03
draft: true
math: true
toc: true
author: Niklas
image: cover.jpg
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
To model the above problem, let us consider two policies: $\pi_2$, a.k.a. what the user would do on his own, and $\pi_1,$ which is what the assistant suggests. We link these two policies with a single probability $\alpha \in [0,1]$ which corresponds to the probability that the user accepts and performs the action suggested by the assistant.
In this way, we obtain a new, *collaborative* policy
$$\pi^\alpha(a \mid s) = (1-\alpha)\pi_2(a \mid s) + \alpha\pi_1(a \mid s).$$

The parameter $\alpha$ can be very flexible and depend on a lot of factors such as the time step $t$, the suggested action $a^\mathrm{sup} \sim \pi_1(\cdot \mid s)$, the user action $a \sim \pi_2(\cdot \mid s)$, etc.

First of all: What do I mean by "can the assistant deal with it?" Well, one possibly surprising fact is that assistance with the *optimal* policy, $\pi^\star$, does not always lead to a better return. In fact, the resulting return can sometimes turn out to be *worse* than if the user had acted on its own.

# The Optimal Policy is Bad for Advice
Consider the very simple example below.

# How Can We Make It Better?

# Where Should I Park My Car?

# Okay Cool... But How Relevant Is This In Reality?

# References

> Cover image: [Unsplash](https://unsplash.com/de/fotos/zwei-hande-die-nach-einem-flugobjekt-am-himmel-greifen-X9Cemmq4YjM)