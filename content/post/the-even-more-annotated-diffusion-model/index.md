---
title: 'The (Even More) Annotated Diffusion Model'
date: 2023-11-26T15:05:00+01:00
draft: true
math: true
cover:
    image: cover.jpg
showToc: true
author: Niklas
tags:
    - diffusion
categories:
    - Deep Learning
    - Diffusion Models
    - Generative AI
---

## Introduction

I recently stumbled upon [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion) on Hugging Face while researching diffusion models. It has been a great start for understanding this fascinating idea behind modern image generation models such as StableDiffusion or DALL-E. While the article lays out and explains Phil Wang's implementation of the Denoising Diffusion Probabilistic Models ([Ho et al. 2017](https://arxiv.org/pdf/2006.11239.pdf)) paper quite nicely, it still skips out on a bunch of details, which sometimes left me scratching my head and wishing for further explanations. This article is intended to close that gap and provide more insight into some of the implementation details.

## Diffusion Models 101

Diffusion models have been introduced in **Deep Unsupervised Learning using Nonequilibrium Thermodynamics** ([Sohl-Dickstein et al. 2015]((https://arxiv.org/pdf/1503.03585.pdf))). Fundamentally, you can imagine a diffusion process to be a sequence of random variables $\bfx_1, \bfx_2, \dots, \bfx_T$ which are recursively related via $$\bfx_{t + 1} = \bfx_t + \sqrt{\beta_t} \boldsymbol\varepsilon, \quad \boldsymbol\varepsilon \sim \mathcal N(0, \mathbf I).$$ This is like (discrete) [Brownian motion](https://en.wikipedia.org/wiki/Brownian_motion) that starts at $\bfx_0$ and whose noise variance depends on time. In practice, we would like to avoid that the process expands too much, so we dampen the mean, resulting in
$$\begin{equation}\label{1}\bfx_t = \sqrt{1 - \beta_t}\bfx_{t-1} + \sqrt{\beta_t} \boldsymbol\varepsilon, \quad \boldsymbol\varepsilon \sim \mathcal N(0, \mathbf I).
\end{equation}$$ From a probability theory point of view, $\eqref{1}$ can be epressed as
$$\begin{equation}
    q(\bfx_t \mid \bfx_{t-1}) = \mathcal N(\bfx_t; \sqrt{1 - \beta_t}\bfx_{t-1}, \beta_t \mathbf I).
\end{equation}$$
Let us consider a bunch of these processes with different starting points arranged in some kind of structure, like a swiss role:

If we let the diffusion process continue, after a while, there isn't much of a swiss role left anymore - it's just a blob of points without structure. This is the first observation mentioned in the paper: diffusion destroys structure.

The core idea behind diffusion models is now to undo this process, that is, to recover our swiss role from some random blob of points in a recursive manner similar to the above. The second observation from the paper tells us that this will again be a Gaussian,
$$
    p(\bfx_{t-1} \mid \bfx_t) = \mathcal N(\bfx_{t-1}; \boldsymbol\mu(\bfx_t, t), \mathbf\Sigma(\bfx_t, t)),
$$
where the mean $\boldsymbol\mu(\bfx_t, t)$ and the covariance $\mathbf\Sigma(\bfx_t, t)$ are unknown, but we can learn them with a universal approximator, such as a neural network.

In real-world applications, we are less interested in the (anti-)diffusion of a swiss roll or any other two-dimensional dataset, and more in the diffusion of real-world data, such as a set of natural images. The process is the same, just in a much, much larger dimension. For an individual image from the dataset, the diffusion process looks like gradually adding white noise, as the image is moved from the low-dimensional data manifold into the full high-dimensional space.

## Learning the Reverse Diffusion Process

> Cover photo by [Joel Philipe](https://unsplash.com/@joelfilip) on [Unsplash](https://unsplash.com)