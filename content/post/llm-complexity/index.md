---
title: 'An LLM-dependent Complexity Measure'
date: 2024-08-25
toc: true
draft: true
author: Niklas
tags:
    - ai
    - llm
categories:
    - Artificial Intelligence
---

It is known that chain-of-thought reasoning (aka adding "Think step by step" or a variant thereof to the prompt) can improve LLM performance significantly. One way of thinking about this is that the LLM can perform more complex "thoughts" by spending more tokens. Based on this, we could define an LLM-dependent complexity measure of a problem as the smallest number of tokens that the LLM needs to spend in order to correctly answer the question.

Let's formalize this.

> A problem is a pair $(X,Y)$ of question and answer. The *complexity* of this problem with respect to some LLM $M$ is the shortest response to prompt $X$ such that the last tokens of the response contain $Y$.

We only consider the last few tokens, because the previous ones may contain the reasoning process. In other words, the complexity of the problem is the shortest amount of reasoning required to correctly answer the question.

Obviously, this does not always measure a kind of inherent complexity of the problem, as the ability of the model to answer using more or less tokens is largely dependend on the data it was trained on. It is biased in terms of the kinds of problems it has been presented with.

But we can use this measure to compare the performance of different models. If $M$ consistently spends fewer tokens than $M'$ on a particular problem, we can argue that it is more efficient at solving it.