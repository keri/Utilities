'''Stats helper functions'''
import numpy as np
import pandas as pd

def bayes(prob_x_given_a, prob_a, prob_x_no_a):
    ''' pr(A|X) = ( pr(X|A)*pr(A) ) / (( pr(X|A)*pr(A) ) + (( pr(X|not A)*pr(not A) )))
        Pr(A|X) = Chance of (A) given (X).
        Pr(X|A) = Chance of (X).This is the chance of a true positive.
        Pr(A) = Chance of A in the wild.
        Pr(not A) = Chance of not A = 1-pr(A).
        Pr(X|not A) =  Chance of a positive (X) given that not (~A). This is a false positive.'''
    prob_not_a = (1 - prob_a)
    likelihood = ( prob_x_given_a *prob_a )
    return( likelihood / ( likelihood + ( prob_x_no_a * prob_not_a )) )

def standard_confusion_matrix(y_true, y_predict):
    '''returns TN, FP, FN, TN based on predictions'''
    TP = np.sum((y_true == 1) & (y_predict == 1))
    print('y_true =', y_true)
    TN = np.sum((y_true == 0) & (y_predict == 0))
    print('y_predict =',y_predict)
    FP = np.sum((y_true == 0) & (y_predict == 1))
    FN = np.sum((y_true == 1) & (y_predict == 0))

    return (np.array([[TP,FP],[FN,TN]]))

def cb_matrix(cost_TP, cost_FP, cost_FN, cost_TN):
    return (np.array([[cost_TP, cost_FP],[cost_FN, cost_TN]]))

def y_predict_threshold(y_probs, threshold):
    '''returns matrix with predictions based on threshold'''
    changed = np.array(y_probs > threshold).astype(int)
    return(changed)

def calculate_profit(y_true, y_probs, cost_benefit_matrix):
    '''creates an array of predicted y's for every every threshold from 0 - 1.
        Plots cost for every threshold given a specific cost benefit matrix'''
    thresholds = np.arange(0,1,.1)
    cost_predictions = []

    for threshold in thresholds:
        new_predictions = y_predict_threshold(y_probs, threshold)
        confusion_matrix = standard_confusion_matrix(y_true,new_predictions)
        print('confusion matrix = ',confusion_matrix)
        cost = np.array(cost_benefit_matrix * confusion_matrix).sum()
        cost_predictions.append(cost)

    return (zip(thresholds, cost_predictions))
