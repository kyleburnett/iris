#
# Name: iris.py
# Description: Implementation of an artifical neural network
#   for classifying the iris flower types as specified in the
#   Iris dataset found at:
#
#      http://archive.ics.uci.edu/ml/datasets/Iris
#
# Author(s): Kyle Burnett
#

import random
import math

filename = "iris.data"

basket = []
with open(filename) as ifs:
    for line in ifs:
        sample = line.strip().split(',')
        for i in range(4):
            sample[i] = float(sample[i])
        basket.append(sample)

# Sigmoid function f(x) = 1 / (1 + e^(-x))
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Use for propogating signals through the network
def forwardfeed(sample, weights):
    total = 0.0
    for x, weight in zip(sample, weights):
        total += x * weight
    return sigmoid(total)

# Initialize weights
w = [0.0, 0.0, 0.0, 0.0]
alpha = 0.1

# This, right now, doesn't enforce not having duplicates, i.e., major
# overfitting problems.
for i in range(100):
    # Choose sample
    sample = random.choice(basket)
    # Feed input data in (feedforward)
    sigma = forwardfeed(sample[:-1], w)
    # Compute error gradient
    if sample[4] == 'Iris-setosa':
        # Here the expected value is 1.0
        error = sigma * (1.0 - sigma) * (1.0 - sigma)
    else:
        # Here the expected value is 0.0
        error = sigma * (1.0 - sigma) * (0.0 - sigma)
    # Update weights
    for j in range(4):
        w[j] = w[j] + alpha * sample[j] * error