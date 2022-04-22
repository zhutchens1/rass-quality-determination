import matplotlib
matplotlib.use('TkAgg')
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator, LogFormatter
from matplotlib import rcParams
from matplotlib.colors import LogNorm
rcParams['axes.labelsize'] = 9
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['legend.fontsize'] = 9
rcParams['font.family'] = 'sans-serif'
rcParams['grid.color'] = 'k'
rcParams['grid.linewidth'] = 0.2
my_locator = MaxNLocator(6)
singlecolsize = (3.3522420091324205, 2.0717995001590714)
doublecolsize = (7.100005949910059, 4.388044997370)


if __name__=='__main__':
    poor_image = fits.open("../exposuremaps/rs931302n00_mex.fits")[0].data
    good_image = fits.open("../exposuremaps/rs931153n00_mex.fits")[0].data
    
    fig,axs=plt.subplots(ncols=2, figsize=doublecolsize)
    axs[0].imshow(good_image)
    axs[1].imshow(poor_image)
    plt.tight_layout()
    plt.savefig("Figure1.pdf",dpi=200)
    plt.show()

