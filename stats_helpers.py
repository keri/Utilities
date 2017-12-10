'''Stats helper functions'''

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
