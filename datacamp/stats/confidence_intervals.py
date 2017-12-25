from scipy import stats
import numpy as np
"""
Confidence Intervals

They give you guarantees about a procedure under repeated sampling from the population
e.g., for a = 0.05

Before seeing a sample y from the population, we know that there is a 95% chance we will
draw a sample form the population that generates 1 95% confidence interval containing the
true value of the population parameter theta (typically mean)
"""
444

"""
Confidence Interval for normal mean, known variance
"""
def ci0(sample, pv, a):
    a += (1-a) / 2
    z = stats.norm.ppf(a)
    sm = sample.mean()
    l = len(sample)
    inv = z * np.sqrt(pv/l)
    return sm - inv, sm + inv


y = np.array([53.2, 33.6, 36.6, 42, 33.3, 37.8, 31.2, 43.4])
pv = 43.75

print(ci0(y, pv, 0.95))

"""
Confidence Interval for normal mean, unknown variance
using student-t distribution instead of normal distribution
"""

def ci1(sample, a):
    a += (1-a) / 2
    n = len(sample)
    dof = n - 1
    t = stats.t.ppf(a, dof)  # dof degree of freedom
    sm = sample.mean()  # sample mean
    sv = ((sample - sm) ** 2).sum() / (n-1)  # sample standard deviation
    print("t:", t)
    print("mean:", sm)
    print("variance:", sv)
    inv = t * np.sqrt(sv / n)
    return sm - inv, sm + inv


"""
Confidence Interval for difference of normal means
compare two samples taken from two different populations
key assumption:
population variances, population means are all unknown
"""

def ci2(sample1, sample2, a):
    a += (1-a) / 2
    n1, n2 = len(sample1), len(sample2)
    sm1 = sample1.mean()
    z = stats.norm.ppf(a)
    sv1 = ((sample1 - sm1) ** 2).sum() / (n1-1)  # unbiased estimation
    sm2 = sample2.mean()
    sv2 = ((sample2 - sm2) ** 2).sum() / (n2-1)
    diff = sm1 - sm2
    inv = z * np.sqrt(sv1/n1 + sv2/n2)
    print(diff, inv, z, sv1, sv2)
    return diff - inv, diff + inv


y1 = np.array([34.0, 28.9, 29, 45.4, 53.2, 29.0, 36.5, 32.9])
y2 = np.array([53.2, 33.6, 36.6, 42.0, 33.3, 37.8, 31.2, 43.4])

print(ci2(y1, y2, 0.95))







