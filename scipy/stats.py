import scipy.stats as stats
import numpy as np

##### SUMMARIES ######
v1 = np.random.normal(size=100)
print(stats.describe(v1))

######## DISTRIBUTIONS ########
# declare a RV like this:
X = stats.poisson(8.5)
print(X.pmf(2)) # density function
print(X.cdf(2)) # cumulative
print(X.mean())
print(X.var())
print(X.std())

x = stats.poisson.pmf(2, mu = 8.5) #this is how you get distribution parameters without making a RV
print(x)

X = stats.multivariate_normal(mean = [0.5, -0.2], cov = [[2.0, 0.3], [0.3, 0.5]]) # supply the mean and covariance if you want
print(X.mean)

######### TESTS #########
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

# test if two samples are from the same distribution
res = stats.ttest_ind(v1, v2)
print(res.pvalue)
# test if a sample is drawn from a specific distribution
res = stats.kstest(v1, "norm")
print(res.pvalue)
res = stats.normaltest(v1)
print(res.pvalue)


# there are more distribtuions, statistics, and tests you can do.


