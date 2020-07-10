import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

class PlotBaseMap:
    def __init__(self, data, **kwargs):
        fig=plt.figure(figsize=(9, 6),dpi=100)
        lat  = data.getLatitude()[:]
        lon  = data.getLongitude()[:]
        x, y = np.meshgrid(lon, lat)
        pdata = data
        m = Basemap(projection='cyl', resolution='c',
                    llcrnrlat=lat.min(), urcrnrlat=lat.max(),
                    llcrnrlon=lon.min(), urcrnrlon=lon.max())
        m.pcolormesh(x,y,pdata,shading='flat',cmap=plt.cm.viridis, **kwargs)
        m.colorbar(location='right')
        m.drawcoastlines()
        m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0])
        m.drawmeridians(np.arange(0.,360.,60.),labels=[0,0,0,1])
        plt.title(str(pdata.id))
        plt.savefig(str(pdata.id)+'.png', bbox_inches='tight')

