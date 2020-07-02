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

A percentil is the value where a given percentage of observations falls, it's always expressed as a numeric value between 0 and 100. For example, the **10th percentil** is the value that has a **__10%__** of the observations below him.

To calculate the percentile, first order the data ascending and then apply this formula, the special brackets indicates that we have to take the first integer bigger than the result.

An example using **__x = (-3,-1,3,7,10,15, 17)__** as data and calculating the **20th** percentile:

![Image of DT](https://github.com/CrunchyPistacho/100DaysOfML/blob/master/Basic_Statics/images/Percentil%201.PNG)

So the second value **(-1)** of the ordered list will be the 20th percentil.

### Interquartil Range (IQR)

The most used percentiles are the 25, 50 and 75, usually called **(Q1,Q2,Q3)**, this quartiles are used to calculate the boxplots, a graphical analysis technique that we will introduce in posterior posts.

The **IQR** is the difference between **__Q1__** and **__Q2__**. It contains the central 50% of the data.

This is a measure pf dispersion with low influence from extreme values (outliers), as happened with the median and the mode explained in the last post about **Measures of Centrality**(Linked at the end of).

## Variance and Standart Deviation

The most common measures of dispersion for continuous data are the variance and standard deviation, let's introduce them. As must data science projects wants to infer results to new data, we will use formulas based on sample data.

### Sample Variance

Variance is calculated substracting the mean of the data to each value and summing the results, mathematically expressed as:

![Image of DT](https://github.com/CrunchyPistacho/100DaysOfML/blob/master/Basic_Statics/images/Deviation.PNG)

An example using the same variable as before,**x** have Variance of:

![Image of DT](https://github.com/CrunchyPistacho/100DaysOfML/blob/master/Basic_Statics/images/Deviation_example.PNG)

You should have noticed about the squared values, ¿why do we need to take the square of the differences?. 

That is an interesting question, the squares are taken because if we don't use it we will have positive and negative values and this will make the result tend to 0, otherwise with squares we will always have a positive value.

Taking the squares will modify our units, to solve this problem and simplify the interpretation of results the **Standart Deviation** appears.

### Standart Deviation

It's the square of the Variance, calculated to interpret the results with the same scale as the original data and simplify the inference.

![Image of DT](https://github.com/CrunchyPistacho/100DaysOfML/blob/master/Basic_Statics/images/Variance.PNG)

Using the same example, the standart deviation is:

![Image of DT](https://github.com/CrunchyPistacho/100DaysOfML/blob/master/Basic_Statics/images/Variance_example.PNG)

A lower valie of standart deviation indicates that our values tend to be closer to the mean, meanwhile a big values will indicate that our data are more spread over a wide range.

This indicator is used widely in statistics,  from measuring confidence intervals of statisticall conclusions to calculate significance of variables in models like lineal or multiple regression.

## Coefficient of Variation

The coefficient of variation (**CV**) is a measure of relative variability, the objective is to get around difficulties when comparating distributions of distinct variables measured in different units.

It's calculated as:

![Image of DT](https://github.com/CrunchyPistacho/100DaysOfML/blob/master/Basic_Statics/images/CoefVar.PNG)

The **CV** cannot be calculated if the mean of the data is 0. If a variable has both positive and negative values, the mean can tend to become close to zero although the data actually has wide range, this can produce a misleading CV value because the denominator will be a small number.

CV is usually usefull when variables measure the same type of metric, for example distance metrics, expressed in distinct units.

## Summary

This post introduces some of the pillars of machine learning, the distribution of data gives data scientists the hability to infer the results of statisticals models to new real world data.



