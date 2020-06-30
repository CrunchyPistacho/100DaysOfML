# Probability for machine learning 2: Conditional Probability and Bayes Theorem

Bayes Theorem is one of the most importants theorems to data science, it describes how to update the probabilities of hypothesis when an evidence is given. It allows us to estimate the probability of the next event given the actual event.

To understand it, we need to introduce some probability terms.

## Probability Introduction

### Independence

Two trials are independent when the outcome of one trial does not influence the outcome of the otherone. An example can be throwing 2 coins, if the first coin scores a tail, the second one still have the same probability than before.

### Permutation

All possible ways elements in a set can be arranged, in permutations the order of elements is important. For example, all permutation of the sample space = (1,2,3), are {(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)}

The number of permutations can be calculated with the factorial of the number of elements in the sample space, in the last example we got 3 elements, that results in :

<img src="https://render.githubusercontent.com/render/math?math=%243!%20%3D%203%20x%202%20x%201%20%3D%206%24">

To calculate the number of **permutations** of subsets of size k drawn from a set of size n is:

<img src="https://render.githubusercontent.com/render/math?math=%24nPk%20%3D%20%5Cdfrac%7Bn!%7D%7B(n-k)!%7D%24">

Example: How to calculate the number of **permutations** of size 3  that can be drawn from a set of size 5:

<img src="https://render.githubusercontent.com/render/math?math=%245P3%20%3D%20%5Cdfrac%7B5!%7D%7B(5-3)!%7D%20%3D%20%5Cdfrac%7B5!%7D%7B(2)!%7D%20%3D%20%5Cdfrac%7B5%20x%204%20x%203%20x%202%20x%201%7D%7B(2%20x%201)%7D%20%3D5%20x%204%20x%203%20%3D%2060%24">

### Combination

They work as permutations, but the order of elements is no important, so in the last example there's just one permutations of 3 elements, {(1,2,3)}.

To calculate the number of **combinations** of subsets of size k drawn from a set of size n is:

<img src="https://render.githubusercontent.com/render/math?math=%24nCk%20%3D%20%5Cdfrac%7Bn!%7D%7Bk!(n-k)!%7D%20%24">

Example: How to calculate the number of **combinations** of size 3  that can be drawn from a set of size 5:

<img src="https://render.githubusercontent.com/render/math?math=%245C3%20%3D%20%5Cdfrac%7B5!%7D%7B3!(5-3)!%7D%20%3D%20%5Cdfrac%7B5!%7D%7B3!(5-3)!%7D%20%3D%20%5Cdfrac%7B5!%7D%7B3!x%202!%7D%20%3D%20%5Cdfrac%7B5%20x%204%20x%203%20x%202%7D%7B3%20x%202%20x%202%7D%20%3D%20%5Cdfrac%7B5%20x%204%7D%7B2%7D%20%3D%2010%24">

## Probability

Probability is always defined between 0 and 1, the probability of the sample space is always 1 and of the null space always 0. For a brief introduction to probability there's a post here:

https://medium.com/@crunchyML/probability-for-machine-learning-basic-probability-972be946ba53

Mathematically expressed:

* P(E) it means probability if event E 
* P(S) is the probability of the sample space, always equal to 1
* P(~E) = 1 - P(E)

### Conditional Probability

One of the most important elements of statistics for data science, it gives us the ability to infer our results to new studies

The probability of an event(**E**) given anotherone(**F**) or conditional probability is expressed as **P(E|F)**

The conditional probability can be calculated as:

<img src="https://render.githubusercontent.com/render/math?math=%24P(E%7CF)%3D%5Cdfrac%7BP(E%20%5Ccap%20F)%7D%7BP(F)%7D%24">

### Multiple Events Probability

Two events are mutually exclusive if they can't both occur at the same time.

Union of mutually excusive events:

<img src="https://render.githubusercontent.com/render/math?math=%24P(E%20%5Ccup%20F)%20%3D%20P(E)%20%2B%20P(F)%24">

Union of not mutually exclusive events:

<img src="https://render.githubusercontent.com/render/math?math=%24P(E%20%5Ccup%20F)%20%3D%20P(E)%20%2B%20P(F)%20-%20P(E%20%5Ccap%20F)%24">

Intersection of independent events:

<img src="https://render.githubusercontent.com/render/math?math=%24P(E%20%5Ccap%20F)%20%3D%20P(E)%20%20P(F)%24">

Intersection of non independent events:

<img src="https://render.githubusercontent.com/render/math?math=%24P(E%20%5Ccap%20F)%20%3D%20P(E)%20%20P(F%7CE)%24">


## Bayes Theorem

It allows us to calculate the conditional probability without knowing the joint probability.

<img src="https://render.githubusercontent.com/render/math?math=%24P(E%20%7C%20F)%20%3D%20%5Cdfrac%7BP(F%20%7C%20E)%20%20P(E)%7D%7BP(F)%7D%24">

In this formula:
* **P(E|F)** is known as the **Posterior**, being the probability of **E** being True if **F** is True.
* **P(F|E)** is known as the **Likehold**, being the probability of **F** being True if **E** is True.
* **P(E)** is known as the **Prior**, being the probability of **E** being True.
* **P(F)** is the probability of **F** being True.


## Conclusion

Bayes Theorem will be very usefull for a lot of machine learning models and will enable us to infer our results to new data. Make sure that understand thisone, it's very important for Data Science.



This is the fourth post of my particular #100daysofML, i will be publishing the advances of this challenge at github, twitter and Medium (Adrià Serra).
https://twitter.com/CrunchyML
https://github.com/CrunchyPistacho/100DaysOfML
