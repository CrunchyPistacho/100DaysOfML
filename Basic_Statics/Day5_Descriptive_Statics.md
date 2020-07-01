# Statistics For Machine Learning: Descriptive Statistics

All **Data Science** projects should start with an **EDA**: Exploratory Data Analysis, and every **EDA** should clean data and then start with descriptive statics.

This post is a guide about descriptive statistics for EDA.

## Measures of Central Tendency

Also known as mesures of location, should be one of the first statistics computed for all continous variables of a dataset.

### Arithmetic Mean

Sometimes refered as mean or average, this metric of centrality goes well with interval, ratio data and continous variables.

The way to calculate the mean is simply getting the sum of all the elements and divide it by the number of elements.

<img src="https://render.githubusercontent.com/render/math?math=%24%5Cmu%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7D%24">

When we express the mean of a variable, for example x or age, we use the <img src="https://render.githubusercontent.com/render/math?math=%24%5Coverline%7Bx%7D%2C%20%5Coverline%7Bage%7D%24">.

The **Mean** as central tendency can be biased, for example, if the data contains 2 elements with a big difference from the rest, this elements will influence the distribution of the data and the result will tend to be closer to this **outliers**. Let's explain it with an example:

* Case 1: Mean is a good central tendency metric.

<img src="https://render.githubusercontent.com/render/math?math=%24Case%201%2C%20x%20%3D%20(-2%2C2%2C3%2C5)%20%5Crightarrow%20%5Coverline%7Bx%7D%20%3D%20%5Cfrac%7B8%7D%7B4%7D%20%3D%202%24">

* Case 2: Mean is not a good central tendency metric.

<img src="https://render.githubusercontent.com/render/math?math=%24%20x%20%3D%20(-50%2C2%2C3%2C5)%20%5Crightarrow%20%5Coverline%7Bx%7D%20%3D%20%5Cfrac%7B-40%7D%7B4%7D%20%3D%20-10%24">


One way to solve this issue, used by **Winsorized mean**, also known as **trimmed mean** is to drop a percentage of the extreme values, in the last example the mean will be calculated dropping the -50 value.






