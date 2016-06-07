import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndimage
from scipy.ndimage.filters import minimum_filter, maximum_filter
from mpl_toolkits.basemap import cm

filename='snow'
title ='snow, total to forecast hour'
boundaryColor = 'gray'
cbarlabel = 'Snow Total (inches)'
frequency = 3                   # frequency in hrs


def plot(variables, pvars, pltenv, time):

    gauss_sigma = 3
    lvl_500 = 4


    x = pltenv['x']
    y = pltenv['y']
    m = pltenv['map']


    bbox = dict(boxstyle="square",ec='None',fc=(1,1,1,0.75))


    # precip
    #    precip = (variables['RAINNC'][time]+variables['RAINC'][time])*0.03937
    # if time >= frequency:
    #     precip -= (variables['RAINNC'][time-3]+variables['RAINC'][time-3])*0.03937
    #    precip = (variables['SNOW'][time] - variables['SNOW'][0])*0.03937
    precip = (variables['SNOWH'][time] - variables['SNOWH'][0])*39.37
    # precip = (variables['SNOW'][time])*0.03937*10

    nws_precip_colors = [
        "#7fff00",  # 0.01 - 0.10 inches
        "#00cd00",  # 0.10 - 0.25 inches
        "#008b00",  # 0.25 - 0.50 inches
        "#104e8b",  # 0.50 - 0.75 inches
        "#1e90ff",  # 0.75 - 1.00 inches
        "#00b2ee",  # 1.00 - 1.25 inches
        "#00eeee",  # 1.25 - 1.50 inches

        "#8968cd",  # 1.50 - 1.75
        "#912cee",  # 1.75 -
        "#8b008b",  # 2.0 - 
        "#8b0000",  # 2.5 - 
        "#cd0000",  # 3.0 -
        "#ee4000",  # 4.0 -
        "#ff7f00",  # 5.0 -
        "#cd8500",  # 6.0 -
        "#ffd700",  # 7.0 -
        "#eeee00",  # 8.0 - 
        "#ffff00",  # 9.0 -
        ]
    precip_colormap = mpl.colors.ListedColormap(nws_precip_colors)
    levels = [0.01, 0.1, 0.2, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 18.0,
          24.0, 30.0, 36.0, 48.0, 60.,]
    # levels = [0.01, 0.1, 0.25, 0.50, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0, 4.0, 5.0,
    #           6.0, 7.0, 8.0, 9.0, 10.,]


    norm = mpl.colors.BoundaryNorm(levels, 18)
    
    m.contourf(x,y,precip,levels,cmap=precip_colormap, norm=norm)
#    plt.colorbar()
