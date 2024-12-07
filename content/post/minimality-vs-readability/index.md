---
title: 'Non-Redundancy vs. Simplicity in Coding'
date: 2024-12-07
toc: false
author: Niklas
tags:
    - coding
draft: false
---

# Non-Redundancy vs. Simplicity in Coding
A goal of many coders/programmers is to write especially clean code. One that has little redundancy. It is a bit of an art form, but also a balancing act. Consider, for example, the following code snippet, which I wrote this morning during Advent of Code:
```python
oplist = [0, 1, 2] if part2 else [0, 1]
```
Its purpose is simply to join the solutions of both parts of the puzzle, using just the boolean `part2` argument, which I give to the function that computes the solution. This is a single neat and easy to understand line of code. But there's something redundant about it: Both the `if` and the `else` clause contain `[0, 1]`. That's a redundancy! Can we simplify this?
```python
oplist = [0, 1]
if part2:
    oplist.append(2)
```
Ahhh, much better! Or is it?

The redundancy might be gone now, but now we have three lines and, while they are both easily understandable, the first one is still clearer and, in some sense, simpler. We have merely traded simplicity for slightly less redundancy.

Of course, there are other variants, even with one line:
```python
oplist = [0, 1] + ([2] if part2 else [])
```
But it still lacks the simplicity of the first solution, at least in my opinion.

Or how about this?
```python
oplist = list(range(2 + part2))
```
This is the shortest so far, but it would also take me the longest to parse, if I saw it for the first time. 

In the end, it likely just comes down to the complexity of the final expressions. Both lists, `[0, 1]` and `[0, 1, 2]`, are neither very long nor complex, so it seems cleanest to just write them out explicitly. If they were instead several lines of code, with only one small difference, we would start to feel the need to remove the redundancies, thereby actually **increasing** readability and simplicity.