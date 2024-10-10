---
title: 'An Overview of Reinforcement Learning Algorithms'
date: 2024-10-07
toc: true
author: Niklas
draft: true
tags:
    - ai
    - reinforcement-learning
categories:
    - AI
    - Reinforcement Learning
draft: true
---

There are a ton of reinforcement learning algorithms out there. For a beginner, this can frankly be overwhelming (as it has been for me), so I have decided to create this post to give a fairly comprehensive overview about all the different kinds of algorithms that are used in reinforcement learning (RL).

# Quick intro: What is Reinforcement Learning?

# Model-Based Algorithms
Model-based algorithms assume that the MDP, especially its transition and reward function, is fully known. Depending on who you ask, model-based algorithms do not even count as reinforcement learning, just *planning*. I would agree with that, and yet, a list of RL algorithms would be incomplete without mentioning value iteration, policy iteration and the likes.

## Value Iteration
(algorithm...)

This algorithm converges, if $\gamma < 1$, and the proof is quite elegant. The main ingredient is the [Banach fixed point theorem](https://en.wikipedia.org/wiki/Banach_fixed-point_theorem).

## Policy Iteration
...

# Model-Free Algorithms
## Bandit Algorithms
Bandit algorithms are not full-blown RL algorithms, because the underlying MDP is assumed to have only a single state. Still, a lot of bandit algorithms serve as the basis for RL algorithms (in case you know them already: an example would be UCT, which is based on UCB; but I will introduce these below).

### Upper-Confidence Bound (UCB)
Well, "upper-confidence bound" does not really sound like an algorithm, but more like an inequality. This is true. The upper confidence bound is the following identity:
$$$$

## Q-Learning
In Q-Learning, the idea is to approximate the optimal $Q$ function. Recall that $$Q^\star(s,a) = r(s, a) + \gamma \mathbb E_{s' \sim P(\cdot \mid s, a)}[V^\star(s')] = \mathbb E_{s' \sim P(\cdot \mid s, a)}[r(s, a) + \gamma \max_{a' \in A} Q^\star(s',a')].$$ By acting within the environment, we sample states according to $P$. Thus, we can approximate the expectation by simply averaging $r + \gamma \max_{a' \in A} Q(s',a')$ for each step $(s,a,r,s')$ of the trajectory. This averaging is done continuously, using an exponentially weighted moving average (EWMA). The pseudocode is below.

---
---
**Input:** $S$, $A$, discount $\gamma$, learning rate $\alpha \in (0,1]$, $\varepsilon > 0$, no. of training episodes $N \in \N$

1. Initialize $Q$ arbitrarily (e.g. zero initialization)
2. **for** $i = 1,\dots,N$ **do**
>3. Pick a starting state $s \in S$
>4. **while** $s$ is not terminal **do**
>>5. pick action $a$ based on $\varepsilon$-greedy strategy
>>6. observe reward $r$ and next state $s'$
>>7. $Q(s, a) \leftarrow Q(s,a) + \alpha (r + \gamma \max_{a' \in A} Q(s', a') - Q(s,a))$
>>8. $s \leftarrow s'$
> 9. **end while**
10. **end for**
---
---

## SARSA
You might have noticed that the tuple $(s,a,r,s')$ in the Q-learning section sounds a lot like "SARSA", if you just added another "a" at the end. Well, that's basically what SARSA is. It is almost the same as Q-learning, except that the term $\max_{a' \in A} Q(s',a')$ is replaced by just $Q(s',a')$, where $a'$ is directly sampled from the agent's policy.

## Temporal Difference Learning

## MCTS

## Deep Q-Network (DQN)

## Derivative-Free Methods
### Cross-Entropy Method
### Covariance Matrix Adaptation
### Natural Evolution Strategies


## Policy Gradient Methods
### Vanilla Policy Gradient / REINFORCE
### TRPO
### PPO

## HER

## TD($\lambda$)

## Actor Critic
### Advantage Actor Critic (A2C)
### Generalized Advantage Estimation (GAE)