# Basic Statistics for machine learning 1: Data Types

Anyone interested about learning Machine Learning should have at least a base of statistics behind, this is the first post of a series about basic statistics for Data scientists.

## Types of Data

All Machine Learning and Deep Learning projects starts from data, this data is captured in distinct formats, staticians divide the data types at 2 levels:

![Image of DT](https://github.com/CrunchyPistacho/100DaysOfML/blob/master/Basic_Statics/images/Day1_datatypes.png)

**1. Nominal Data:** This type of data refer to labels, it can contain numeric or text values. It’s used to map each element to a class. Example 0 = dog, 1 = cat.

**2. Ordinal Data:** Still referes to categories, but in this case there’s some meaningful order between them. However there’s no metric to decide what’s the distance between categories. An example is a satisfaction poll having a list of possible answers as (Very Unhappy, Unhappy, Happy, Very Happy).

**3. Continous Data:** It has an order and can take any value within a range. Examples are the height or weight of a person.

**4. Discrete Data:** It has an order and can only take particular values within a range. One example is the number or kids in a class, you can’t cut a kid at half so it has to be an integer as 15, 23, 142, ...

Each data type should be analized and used in distinct ways, if we treat a categorical variable as discrete we will get wrong results. We have to visualiz and treat all variables as their own type, some statistical models will need to convert categorical data into numbers, mapping each element.
