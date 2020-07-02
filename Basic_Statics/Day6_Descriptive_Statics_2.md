# Statistics for machine learning: Measures of Dispersion

Dispersion refers to how spread out is a variable. Also called **measures of variability**, the dispersion is at least as important as know the centrality of a variable, i wrote a post about centrality yesterday, linked below.

## Population or Sample data?

Some distribution indicator calculations depends on the data, specifically in the case that data captures all the possible observations that can be made or just a part of them. 

If we work with all the possible observations we use the **population** version of the formulas. If we work with a subset, we use the **sample** version.

In data science, we always wants to infer our results to new data, so we will always want to use the **sample** statistics.

Analyzing a population means your data set is the complete population of interest, so you are performing your calculations on all members of the group of interest for the analysis and just want to make direct statements about the characteristics of that group.

## Range

The **Range** is the difference between the minimum and the maximum value of a variable, in data science it gives an idea of how the variable will be before looking at it more deeply.

For example, the range of **__(-4,-1,-3,8)__** is **__8 - (-4) = 12__** .


## Percentiles and Interquartil Range

### Percentiles

A percentil is the value where a given percentage of observations falls, it's always expressed as a numeric value between 0 and 100. For example, the **10th percentil** is the value that has a **__20%__** of the observations below him.

To calculate the percentile, first order the data ascending and then apply this formula, the special brackets indicates that we have to take the first integer bigger than the result.

An example using **__x = (-3,-1,3,7,10,15, 17)__** as data and calculating the **20th** percentile:

![Image of DT](https://github.com/CrunchyPistacho/100DaysOfML/blob/master/Basic_Statics/images/Percentil%201.PNG)




## Variance and Standart Deviation

## Coefficient of Deviation



