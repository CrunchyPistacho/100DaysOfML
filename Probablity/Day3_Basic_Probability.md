# Probability for machine learning 1: Basic Probability

Probability is one of the most important fields to learn if one want to understant machine learning and the insights of how it works. In this publication we will introduce the basic definitions.
A typical usefull definition of **probability** for statistics is that probability tells us how often something is likely to occir when an experiment is repeated.

## Basic Definitions

### Trial

Also called Experiments or observations, they refer to an event with an unknown outcome. Examples of trials are rolling a dice or fliping a coin, we don't know the result of them.

Trial means one iteration and experiment is when we do multiple trials.

### Sample Space

Defines as <img src="https://render.githubusercontent.com/render/math?math=%24S%24">, the sample space is the set of all possible outcomes of a trial. In the example of rolling a dice, if we use a 6-faced dice, the sample space is <img src="https://render.githubusercontent.com/render/math?math=%24S%20%3D%20%5Clbrace%201%2C2%2C3%2C4%2C5%2C6%20%5Crbrace%24">.

If the experiment has more than one iteration, as throwing a coin 2 times in a row, the sample space is created by all possible combilations of both throws : <img src="https://render.githubusercontent.com/render/math?math=%24%5Clbrace%20(head%2Chead)%2C%20(head%2Ctail)%2C%20(tail%2C%20tail)%2C%20(tail%2Chead)%20%5Crbrace%24">.

### Event

Usually defined as $E$, is an element or a group of elements of the sample space. If the outcome of a trial or experiment is in the event set, the outcome satisfied the event. 

Example of events are:

1. Obtaining head on a coin flip.

2. Obtaining 1 or 2 in a dice roll.

3. Obtaining more than 6 with the sum of 2 dice roll outcomes.

The most common way to visualize this events is using Venn Diagrams in which a rectangle represents the sample space and circles represents particular events.

![Image of DT](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Venn0001.svg/320px-Venn0001.svg.png)

#### Union

The union of events, written as <img src="https://render.githubusercontent.com/render/math?math=%24E%20%5Cunion%20F%24">, means either E or F, in the Venn diagram, it's displayed as any point in any of the particular events(circles).

![Image of DT](https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Venn0111.svg/320px-Venn0111.svg.png)

#### Intersection

The intersection of events, written as <img src="https://render.githubusercontent.com/render/math?math=%24E%20%5Ccap%20F%24">, means E and F, in the Venn diagram, it's displayed as any point where both circles overlap.  

![Image of DT](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Venn0001.svg/320px-Venn0001.svg.png)

#### Disjuntive union

Also known as symetric difference, written as <img src="https://render.githubusercontent.com/render/math?math=%24E%20%5Ctriangle%0A%20F%24">, means E or F, but not both,  in the Venn diagram, it's displayed as any point of the circles except where both circles overlap.  

![Image of DT](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Venn0110.svg/320px-Venn0110.svg.png)

#### Absolute Complement

Set of elements not in E, written as <img src="https://render.githubusercontent.com/render/math?math=%24U%20%5Csetminus%0A%20E%24">, mean not E,  in the Venn diagram, it's displayed as any point of the space except in E.  

![Image of DT](https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Venn1010.svg/320px-Venn1010.svg.png)

#### Relative Complement

Set of elements in F and not in E, written as <img src="https://render.githubusercontent.com/render/math?math=%24E%20%5Csetminus%0A%20F%24">, mean not E,  in the Venn diagram, it's displayed as any point of E except the intersection with F.  

![Image of DT](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Venn0010.svg/320px-Venn0010.svg.png)

#### Independence

It's when the outcome of a trial does not influence the outcome of anotherone, so knowing the outcome of one trial does not gives information of other trial outcome.


### Summary

Probability can be scary, but any data scientist should know, at least, the basics. Probability is the base for all the Machine Learning, and enable Data Scientists to infer the results of an study to real world new data.