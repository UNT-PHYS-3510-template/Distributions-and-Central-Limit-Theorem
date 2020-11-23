# Week 13 Assigment A
# Write a function to compute the binomial distribution
import numpy as np
import matplotlib.pyplot as plt
#
def binomial(n,p):
  """
  This function takes the number of trials n and the probability of success p
  and returns two lists (numpy arrays) with the values of the bins k and the
  corresponding normalized frequencies given by the binomial distribution
  """
  return k,bnp
#
# Specify the values of the parameters
#
n = 
p =
#
k, bnp = binomial(n,p)
#
# Compute the sum of the frequencies of the distribution
#
sum_bnp = 
#
# Compute the average of the distribution
#
average_bnp =
#
# Compute the spread of the distribution
#
spread_bnp = 
#
def stochastic_binomial(ntrials,probability):
    """
    Stochastic process to produce numbers according to the binomial distribution
    This function takes the number of trials and the probability of success in one trial
    and returns the number of successes obtained
    """
    nsuccesses = 0
    for i in range(ntrials):
        toss=np.random.random()
        if toss < probability :
            nsuccesses+= 1
    return nsuccesses
