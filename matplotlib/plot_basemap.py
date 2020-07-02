#!/usr/bin/env python
# coding: utf-8

# # Read data (nc file)

# In[1]:


import cdms2 as cdms

var = 'pr'
data = 'GPCP-2-3'
period = '197901-201907'
ver = 'v20200421'

dir = '/p/user_pub/PCMDIobs/PCMDIobs2_clims/atmos/'+var+'/'+data+'/'
nc = var+'_mon_'+data+'_BE_gn_'+period+'.'+ver+'.AC.nc'
f = cdms.open(dir+nc)
d = f[var]
print(d.shape)


# # Plot data with basemap

# In[2]:


from class_PlotBaseMap import PlotBaseMap

PlotBaseMap(d[0])
# PlotBaseMap(d[0], vmin='0', vmax='0.0003')


# In[3]:


get_ipython().system('jupyter nbconvert --to script plot_basemap.ipynb')

