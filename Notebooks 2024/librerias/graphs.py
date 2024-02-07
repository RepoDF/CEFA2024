import matplotlib.pyplot as plt
import matplotlib.markers as mk
import matplotlib.ticker as mtick
import pandas as pd

def plot_yield_curve(df):
    sf = df.copy()
    sf = sf.dropna()
    sf1 = sf.copy()
    sf1['Y'] = round(sf['Yield']*100,4)
    sf = sf.style.format({'Maturity': '{:,.2f}'.format,'Yield': '{:,.4%}'})
    fontsize=15
    fig = plt.figure(figsize=(13,7))
    plt.title("Nelson-Siegel Model - Unfitted Yield Curve",fontsize=fontsize)
    ax = plt.axes()
    ax.set_facecolor("black")
    fig.patch.set_facecolor('white')
    X = sf1["Maturity"]
    Y = sf1["Y"]
    plt.scatter(X, Y, marker="o", c="blue")
    plt.xlabel('Period',fontsize=fontsize)
    plt.ylabel('Interest',fontsize=fontsize)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.xaxis.set_ticks(np.arange(0, 30, 5))
    ax.yaxis.set_ticks(np.arange(0, 4, 0.5))
    ax.legend(loc="lower right", title="Yield")
    plt.grid()
    plt.show
#plot_yield_curve(yield_df)