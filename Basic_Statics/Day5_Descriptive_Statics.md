# Statistics For Machine Learning: Measures of Central Tendency

All **Data Science** projects should start with an **EDA**: Exploratory Data Analysis, and every **EDA** should clean data and then start with descriptive statics.

This post is the first one of a list about descriptive statistics for EDA.

## Measures of Central Tendency

Also known as mesures of location, should be one of the first statistics computed for all continous variables of a dataset.

### Arithmetic Mean

Sometimes refered as mean or average, this metric of centrality goes well with interval, ratio data and continous variables.

The way to calculate the mean is simply getting the sum of all the elements and divide it by the number of elements.

<img src="https://render.githubusercontent.com/render/math?math=%24%5Cmu%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7D%24">

When we express the mean of a variable, for example x or age, we use the <img src="https://render.githubusercontent.com/render/math?math=%24%5Coverline%7Bx%7D%2C%20%5Coverline%7Bage%7D%24">.

The **Mean** as central tendency can be biased, for example, if the data contains 2 elements with a big difference from the rest, this elements will influence the distribution of the data and the result will tend to be closer to this **outliers**. Let's explain it with an example:

* Case 1: Mean is a good central tendency metric.

<img src="https://render.githubusercontent.com/render/math?math=%24x%20%3D%20(-2%2C2%2C3%2C5)%20%5Crightarrow%20%5Coverline%7Bx%7D%20%3D%20%5Cfrac%7B8%7D%7B4%7D%20%3D%202%24">

* Case 2: Mean is not a good central tendency metric.

<img src="https://render.githubusercontent.com/render/math?math=%24%20x%20%3D%20(-50%2C2%2C3%2C5)%20%5Crightarrow%20%5Coverline%7Bx%7D%20%3D%20%5Cfrac%7B-40%7D%7B4%7D%20%3D%20-10%24">


One way to solve this issue, used by **Winsorized mean**, also known as **trimmed mean** is to drop a percentage of the extreme values, in the last example the mean will be calculated dropping the -50 value.


### Median

It's the middle value of ordered data, it lefts half of the values at each side. If datavis asymetrical or contain outliers the Median is a better metric for centrality than the mean.

The way to calculate the median is distinct base on the number of elements, the first part is commod, order the data, ascending or descending.

* If the number of elements is odd, the median will be the central element.
* If the number of elements is even, the median will be the mean of the 2 elements of the center.

Examples:

<img src="https://render.githubusercontent.com/render/math?math=%24x%20%3D%20(1%2C3%2C4%2C5%2C7)%20%5Crightarrow%20Me_x%20%3D%204%24">

<img src="https://render.githubusercontent.com/render/math?math=%24x%20%3D%20(1%2C3%2C4%2C5%2C7%2C100)%20%5Crightarrow%20Me_x%20%3D%20%5Cfrac%7B4%2B5%7D%7B2%7D%20%3D%204.5%24">

In the second example, we can see how the outlier does not modify the results.

### Mode

It refers to the most repeated value in the data, it's calculated counting the number of times each values appears in the data and getting the values with more appearances. Summarising, the most commond value.

It's most often used for **ordinal or categorical data**.

An example of calculating the mode is:

<img src="https://render.githubusercontent.com/render/math?math=%24x%20%3D%20(2%2C3%2C3%2C3%2C4%2C7%2C7)%20%5Crightarrow%20M_x%20%3D%203%24">

To use the mode on continous data, staticians usially convert the data using standart ranges, that's because if we use all the possible values, it will be very difficult to obtain an element with a good amount of appearances.

### Relation between metrics and distribution of the data

In perfectly symetric variables, all 3 metrics will be the same, but with skewed or asymetrical distributions they will differ.

If data is left skewed, the mean will be lower than the median, otherwise if data is right skewed, the median will be lower than the mean.

## Conclusion

Central tendency is usefull to denote central values of variables in our datasets, they are one of the first elements to analize before any machine learning, giving data scintist basic information of the data that can lead to answer important questions, as should we normalize the data or not?, etc.


This is the fifth post of my particular #100daysofML, i will be publishing the advances of this challenge at github, twitter and Medium.

https://twitter.com/CrunchyML

https://github.com/CrunchyPistacho/100DaysOfML