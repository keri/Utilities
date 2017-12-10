import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import random
import scipy.stats as scs
probabilities = np.arange(.58,.3,-.16)
random.shuffle(probabilities)


'''Creating a plot using for multiple lines using the a continuous X axis with linspace and getting values
for the y from distributions'''

def plot_distribution(dist, params, colorList):
    fig, ax = plt.subplots(figsize=(10,5))
    x = np.linspace(0,1,100)
    zipped_all = list(zip(params, colorList))

    for param,color in zipped_all:
        print(param)
        ax.plot(x,
                dist(param[0],param[1]).pdf(x),
                color,
                label="({0})".format(param))
    ax.legend(title=r"($\alpha,\beta$)", loc="upper left")
    ax.set_xlabel("p")
    ax.set_ylabel("pdf")
