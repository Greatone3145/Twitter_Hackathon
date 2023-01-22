from bayes import *
from search import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import pylab
import numpy

successPerc = []

for i in range(10):
    binaryset = masterBinary[i]
    infoset = masterInfo[i]

    ai_model = Bayes_AI(binaryset, infoset, 0.25)
    successPerc[i] = ai_model.successPrediction()

def draw_the_graph():
    # Hide toolbar on lower left, change size of window
    mpl.rcParams['toolbar'] = 'None'
    mpl.rcParams['figure.figsize'] = [15, 11]

    # Configure graph
    fig, ax = plt.subplots()

    # Set y-axis limit to certain range
    plt.ylim([0, 1.1])

    # Scatter data
    ax.scatter(pathNames, successPerc)

    # Show all ticks in graph for x-axis, show only 0 and 1 for y-axis, change names of labels (uses array)
    plt.xticks([1, 9], labels=pathNames)
    plt.yticks([0, 1])

    # Change names of axis
    plt.xlabel("Stock name")
    plt.ylabel("Prediction score")
    ax.title.set_text("Prediction On Stocks")

    # Change title of window
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Prediction On Stocks')

    plt.show()