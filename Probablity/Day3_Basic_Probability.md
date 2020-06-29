# Probability for machine learning 1: Basic Probability

Probability is one of the most important fields to learn to understant machine learning models and the insights of how them work. In this publication we will introduce the basic definitions.

## Basic Definitions

### Trial

Also called Experiments or observations, they refer to an event with an unknown outcome. Examples of trials are rolling a dice or fliping a coin, we don't know the result of them.

Trial means one iteration and experiment is when we do multiple trials.

### Sample Space

Defines as $S$, the sample space is the set of all possible outcomes of a trial. In the example of rolling a dice, if we use a 6-faced dice, the sample space is $S = \lbrace 1,2,3,4,5,6 \rbrace$.

If the experiment has more than one iteration, as throwing a coin 2 times in a row, the sample space is created by all possible combilations of both throws : \lbrace (head,head), (head,tail), (tail, tail), (tail,head) \rbrace.

### Event

Usually defined as $E$, is an element or a group of elements of the sample space. If the outcome of a trial or experiment is in the event set, the outcome satisfied the event. 

Example of events are:

1. Obtaining head on a coin flip.

2. Obtaining 1 or 2 in a dice roll.

3. Obtaining more than 6 with the sum of 2 dice roll outcomes.

The most common way to visualize this events is using Venn Diagrams in which a rectangle represents the sample space and circles represents particular events.

![Image of DT](https://github.com/CrunchyPistacho/100DaysOfML/blob/master/Probability/images/Day3_venn1.svg)

### Union

