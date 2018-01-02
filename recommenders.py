from numpy import linalg as la
import numpy as np
import pandas as import
'''Functions that use a collaborative recommendation approach'''

def ecludSim(inA,inB):
    '''euclidian distance metric'''
    return 1.0/(1.0 + la.norm(inA - inB))

def pearsSim(inA,inB):
    if len(inA) < 3 :
        return 1.0
    return (0.5+0.5*np.corrcoef(inA, inB, rowvar = 0)[0][1])

def cosSim(inA,inB):
    num = float(inA.T*inB)
    denom = la.norm(inA)*la.norm(inB)
    return (0.5+0.5*(num/denom))

def standard_estimation(dataMat, user, simMeas, item):
    '''takes columns and compares distance from ratings if both ratings are filled in,
    otherwise, skip over that one.
    dataMat = matrix being evaluated
    user = row index
    simMeas = similarity metric
    item = column index'''
    #get number of columns

    n = dataMat.shape[1]
    idx_item = np.where(dataMat[:,item] > 0)[0]
    similarity_total = 0.0
    rating_similarity_total = 0.0
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0:
            continue
        idx_j = np.where(Y[:,j] > 0)[0]
        overLap = np.intersect1d(idx_item,idx_j)
        if len(overLap) == 0:
            similarity = 0
        else:
            similarity = simMeas(dataMat[overLap,item], dataMat[overLap,j])

        print ('the %d and %d similarity is: %f' % (item, j, similarity))
        similarity_total += similarity
        rating_similarity_total += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal/simTotal

def recommend(dataMat, user, N=3, simMeas=pearsSim, estMethod=standard_estimation):
    '''dataMat must be a matrix so changing it to a matrix first line.'''
    '''makes recommendations and returns top 2 recommendations'''
    dataMat = np.matrix(dataMat)
    unratedItems = np.nonzero(dataMat[user,:].A==0)[1]
    if len(unratedItems) == 0:
        return 'you rated everything'
    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    return (sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N])
