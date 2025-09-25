from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90,
llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines()
plt.title('World Map with coastlines -Basemap example')
plt.show()
