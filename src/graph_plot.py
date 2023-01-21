import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import pylab
import numpy


def draw_the_graph():
    # Hide toolbar on lower left, change size of window
    mpl.rcParams['toolbar'] = 'None'
    mpl.rcParams['figure.figsize'] = [15, 11]

    # Data
    stock_name = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    score = [0.5, 1, 0.7, 0.6, 0, 0.2, 0.25, 0.3, 0.9, 0.8]

    # Configure graph
    fig, ax = plt.subplots()

    # Set y-axis limit to certain range
    plt.ylim([0, 1.1])

    # Scatter data
    ax.scatter(stock_name, score)

    # Show all ticks in graph for x-axis, show only 0 and 1 for y-axis, change names of labels (uses array)
    plt.xticks(stock_name, labels=["TSLA", "TSLA", "TSLA", "TSLA", "TSLA", "TSLA", "TSLA", "TSLA", "TSLA", "TSLA"])
    plt.yticks([0, 1])

    # Change names of axis
    plt.xlabel("Stock name")
    plt.ylabel("Prediction score")
    ax.title.set_text("Prediction On Stocks")

    # Change title of window
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title('Prediction On Stocks')

    plt.show()
