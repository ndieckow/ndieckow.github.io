---
title: 'What does good AI assistance look like?'
date: 2024-09-20
toc: true
author: Niklas
tags:
    - research
    - ai
categories:
    - Research
draft: true
---

## What is AI Assistance?
For the purpose of this blog post, let us define AI assistance as any form of information provided by an AI system that helps a (human) user to solve a particular problem.

Naturally, an AI assistant is an AI system that specializes in giving such assisting information to (human) users.

## Positive Suggestion-Based Assistants
Assistance can come in many forms. Suppose you are walking down an unfamiliar alley that forks into three further alleys. An assistant might tell you, "the left alley has some bars and restaurant, the middle one seems shady", and for the right one, it shows you an image depicting pretty buildings and a nice flower garden. This example is just to showcase that assistance can come in many forms.

The type of assistance I want to focus on in this post is something I dub *positive suggestions*. It is simply a suggestion of what to do, or in reinforcement learning (RL) terms, which action to perform. Such an assistant would simply say: "Go right" or "go left" and probably wouldn't say "go straight".

The reason I call this type of advice *positive* is because it also cannot say "don't go straight". It only ever suggests a singular action to perform.

While this is initally restricting, it does have the advantage of translating nicely into the RL, and specifically Markov Decision Problem (MDP), framework. A policy, $\pi$, is typically a mapping from a state $s \in S$ to a probability distribution over actions, a.k.a., $\pi \colon S \to \Delta_A$. Not only can we describe the user's behavior by such a policy, but also the assistant's advice. Let's denote these two policies by $\pi_u$ and $\pi_{ai}$, with $u$ referring to the user and $ai$ to the assistant.

## Combining User and Assistant
Assuming that the user is influenced by the assistant's suggestion, the actual policy with which the user acts in the environment, is no longer $\pi_u$, but some amalgamation resulting from combining $\pi_u$ and $\pi_a$ in some way.

Without specifying the particular way of combining policies, we may view the problem now as a kind of two-player MDP. This MDP has a transition function that depends on a joint action, a.k.a., an element of $A^2$.
As usual, the advantage of this generality, is that all kinds of user behaviors are possible in this model. For instance, a user might actually be *less likely* to perform the suggested action, simply because they distrust AI.

(It can of course be argued that such a person would not choose to make use of AI assistance in the first place, but that is besides the point.)

However, a difficulty of this is that the user behavior is difficult to learn, if the hypothesis space is this large. This is where we come to the first point of what a good assistant should look like.

1. A good AI assistant understand how the user acts.

This involves learning the user's policy, $\pi_u$ through observation, as well as learning the transition model of the two-player MDP. The first one is already a challenge, and so is the second one.

To at least reduce the challenge of the second task, while still maintaining a realistic hypothesis space, we can simplify the combination model to a single parameter, the *acceptance probability*. As the name suggests, it dictates the probability with which the user accepts the assistant's suggestion. This removes the need for joint actions and maintains the original MDP's transition function by simply expessing the policy as
$$\pi(a \mid s) = \alpha \pi_{ai}(a \mid s) + (1 - \alpha) \pi_u(a \mid s).$$

This parameter can be estimated in different ways by, for example, averaging across the last $N$ timesteps whether the user performed the suggested action or not.

> There is some inherent ambiguity in this, because the user might sometimes have performed the suggested action regardless of the assistant's suggestion. One could mitigate this by only counting it 50% of the time, but that still ignores some structure. If the assistant knows that the user will perform the "correct" action, it is easier to attribute this choice, so it might sometimes be a good idea for the assistant to not suggest anything, in order to find out more about the user's behavior.

