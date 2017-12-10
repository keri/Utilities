import math

'''log loss function for soft classifier, (Bernoulli likelihood). '''

def log_loss(y, y_hat):
    '''log-loss(y,p)=−∑ yi * log(pi)+(1−yi)* log(1−pi)'''
    return(- np.sum(y * (np.log(y_hat)) + ((1 - y) * np.log(1-y_hat))))

#generate a numpy array of 0's and 1's with a prob of p for success
def array_bernoulli(p,n):
    return(np.random.choice([0, 1], size=(n,), p=[p, 1-p]))

def profit_curve_price(priceList, probStayList, )
