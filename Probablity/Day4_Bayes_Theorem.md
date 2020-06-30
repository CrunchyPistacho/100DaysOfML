# Probability for machine learning 2: Conditional Probability and Bayes Theorem

Bayes Theoreme is one of the most importants theorems to data science, it describes how to update the probabilities of hypothesis when an evidence is given. It allows us to estimate the probability of the next event given the actual event.

To understand it, we need to introduce some probability terms.

## Probability Introduction

### Independence

Two trials are independent when the outcome of one trial does not influence the outcome of the otherone. An example can be throwing 2 coins, if the first coin scores a tail, the second one still have the same probability than before.

### Permutation

All possible ways elements in a set can be arranged, in permutations the order of elements is important. For example, all permutation of the sample space = (1,2,3), are {(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)}

The number of permutations can be calculated with the factorial of the number of elements in the sample space, in the last example we got 3 elements, that results in <img src="https://render.githubusercontent.com/render/math?math=%243!%20%3D%203%20x%202%20x%201%20%3D%206%24">