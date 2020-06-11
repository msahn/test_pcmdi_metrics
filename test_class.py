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


# # Plot data

# In[2]:


from class_PlotBaseMap import PlotBaseMap

PlotBaseMap(d[0])
# PlotBaseMap(d[0], vmin='0', vmax='0.0003')


# # land/sea masking with original grid

# In[3]:


from class_LandSeaMask import LandSeaMask

mask = LandSeaMask(d)

d_land = mask.land()
d_ocean = mask.ocean()

d_land.id = 'pr_land'
PlotBaseMap(d_land[0])
d_ocean.id = 'pr_ocean'
PlotBaseMap(d_ocean[0])


# # Write data (nc file)

# In[ ]:


out = cdms.open('mask_land.nc', 'w')
out.write(d_land[0])
out.close()

out = cdms.open('mask_ocean.nc', 'w')
out.write(d_ocean[0])
out.close()


# In[ ]:


get_ipython().system('jupyter nbconvert --to script test_class.ipynb')

