import numpy as np
from scipy import stats

data = np.random.randint(60, 100, 100)

"""
Testing mean with known variance 
Assumption: population follows normal distribution with unknown and known variance, testing inequality of u

    H0 is the null hypothesis
    ::equal:: H0: true mean equals to mean, H1: opposite
    ::greater:: H0: true mean > mean
    ::less:: H0: true mean < mean
    eg p = 0.05
    the interpretion for it is 
    if the null was true, the chance of observing a sample with this extreme, or more extreme, difference from
    the null as the one that we saw would be less 0.05/0.95 == 1 / 18.5
    
"""
def ht0(sample, mean, pv, which):
    sm = sample.mean()
    z = (sm - mean) / np.sqrt(pv/len(sample))
    tail = stats.norm.cdf(-np.abs(z))
    ps = {
        "equal": 2 * tail,
        "less": 1 - (1 - tail),
        "greater": 1 - tail
    }
    return ps[which]


y = np.array([46.8, 27.8, 32.5, 39.5, 32.8, 31.0, 26.2, 20.8])
print(ht0(y, 26.8,20.25, "greater"))


"""
A misconception is that a large p-value proves that null is true
The p-value represents evidence against the null
little evidence aganist the null does not prove it is true
"""


"""
Testing mean with unknown variance
"""
def ht1(sample, mean, which):
    sm = sample.mean()
    n = len(sample)
    sv = ((sample - sm) ** 2).sum() / (n-1)
    t = (sm - mean) / (np.sqrt(sv/n))
    tail = stats.t.cdf(-np.abs(t), n-1)
    ts = {
        "equal": 2 * tail,
        "less": 1 - (1 - tail),
        "greater": 1 - tail
    }
    return ts[which]


"""
Testing difference of two means, known variances
"""
def ht2(sample1, sample2, pv1, pv2, which):
    sm1 = sample1.mean()
    sm2 = sample2.mean()
    z = (sm1 - sm2) / np.sqrt(pv1/len(sample1) + pv2/len(sample2))
    tail = stats.norm.cdf(-np.abs(z))
    ps = {
        "equal": 2 * tail,
        "less": 1 - (1 - tail),
        "greater": 1 - tail
    }
    return ps[which]

"""
Testing difference of two means, unknown variances
"""
def ht3(sample1, sample2, which):
    sm1 = sample1.mean()
    sm2 = sample2.mean()
    n1 = len(sample1)
    n2 = len(sample2)
    sv1 = ((sample1 - sm1) ** 2).sum() / (n1-1)
    sv2 = ((sample2 - sm2) ** 2).sum() / (n2-1)
    # pooled estimate sv
    sv = ((n1-1) * sv1 + (n2-1) * sv2)/(n1+n2-2)
    t = (sm1 - sm2) / np.sqrt(sv * (1/n1 + 1/n2))
    tail = stats.t.cdf(-np.abs(t), n1+n2-2)
    ts = {
        "equal": 2 * tail,
        "less": 1 - (1 - tail),
        "greater": 1 - tail
    }
    return ts[which]


a = np.array(np.random.randint(90, 99, 500))
b = np.array(np.random.randint(91, 100, 500))
print(ht3(a, b, "equal"))
