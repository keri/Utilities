import math


def log_loss(y, y_hat):
    '''log loss for soft classifiers (bernoulli likelihood)'''
    '''log-loss(y,p)=−∑ yi * log(pi)+(1−yi)* log(1−pi)'''
    return(- np.sum(y * (np.log(y_hat)) + ((1 - y) * np.log(1-y_hat))))

def array_bernoulli(p,n):
    '''returns a bernoulli array of 0's and 1's with a certain percentage(p) of 1's'''
    return(np.random.choice([0, 1], size=(n,), p=[p, 1-p]))
