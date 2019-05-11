# Yash Shrimali 183594
# Mrs Ingutu

# Bibliography : Youtube: 3blue1brown, CodeBullet,
#                www.Brilliant.org
                

import numpy as np


def nonlin(x, deriv=False):          # Created sigmoid as you need to use probability hence only 0-1 graph should be used
    if deriv is True:                # Used youtube to help with this part, linked in bibliogrpahy above
        return x*(1-x)

    return 1/(1+np.exp(-x))

# input data


X = np.array([[0, 0, 1],            # Matrix, row is a training/trail example and column should be a different neurone
             [0, 1, 1],           # 4 training examples, 3 neurons each
             [1, 0, 1],
             [1, 1, 1]])

###############################################################################
###############################################################################
###############################################################################
# output data
Y = np.array([[1],             # Enter your intended/expected output here
              [1],             # output data set 1 output, 4 examples and 1 output neurone each
              [0],
              [1]])

np.random.seed(1) # give random numbers generated the same starting point thereform same sequence of gener numbers

###############################################################################
###############################################################################
###############################################################################

# Synapses matrices
syn0 = (2*np.random.random((3, 4))-1)  # 3 layers in network therefor only 2 synapse matrices needed
syn1 = (2*np.random.random((4, 1))-1)  # each has a random weight assigned

# Training
for i in range(500000):             # This should be able to optimse the network for data set, though haven't tested it much and occured 1 error out of 13 attempts.
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))   # Prediction is done using matrix multiplication between each layer and synapse

    # Then use sigmoid def function on all values on matrix to create next layer (which has predictions of the output data)

    l2 = nonlin(np.dot(l1, syn1))        # repeat the same thing to get a more accurate and precise layer (only need 2 hidden layers as this isn't meant for complex problems)

    l2_error = Y-l2  # This is basically the error rate i guess?

    if (i%10000) ==0:
        print("Error:" + str(np.mean(np.abs(l2_error))))
    l2_delta = l2_error*nonlin(l2, deriv=True) # reduces error rate
    l1_error = l2_delta.dot(syn1.T) # had help with this part as back propagation has too much complexity in maths, again linked to website(s) above
    l1_delta = l1_error*nonlin(l1,deriv=True)

    # update weights
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print ("Output after training")
print (l2)
    

