import matplotlib.pyplot as plt  
import numpy as np  
from scipy.stats import skewnorm
from scipy.stats import norm  
from numpy.random import seed
from numpy.random import randint
from scipy.stats.kde import gaussian_kde
import random
seed(1)

## Left skewed data With n = 15
## Example 1 

fig, ax = plt.subplots(1, 1)

a = 15
mean, var, skew, kurt = skewnorm.stats(a, moments='mvsk')
x = np.linspace(skewnorm.ppf(0.01, a),
                skewnorm.ppf(0.99, a), 100)

rv = skewnorm(a)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='Probability Density Function')

r = skewnorm.rvs(a, size=1000)
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

print(r)

means = [np.mean(random.sample(list(r), 15)) for _i in range(1000)]

print(type(means))

print(means)
means = sorted(means)
fig, ax = plt.subplots(1, 1)
kde = gaussian_kde(means)
dist_space = np.linspace( min(means), max(means), 100 )
ax.plot(dist_space, kde(dist_space), 'k-', lw=2, label='Probability Density Function')
ax.hist(means, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

##### To check if sample is normal
from scipy.stats import shapiro
stat, p = shapiro(means)
print('Statistics={}, p={}'.format(stat, p))
alpha = 0.05
if p > alpha:
    print('Sample looks Normal (do not reject H0)')
else:
    print('Sample does not look Normal (reject H0)')

## Left skewed data With n = 15
## Example 2

