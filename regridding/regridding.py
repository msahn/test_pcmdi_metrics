#!/usr/bin/env python
# coding: utf-8

# # Read, Regrid, Write (nc file)

# In[1]:


import cdms2 as cdms
from regrid2 import Regridder

# Regrid data
var = 'pr'
data =  'TRMM-3B43v-7'
period = '199801-201712'
ver = 'v20200421'
dir = '/p/user_pub/PCMDIobs/PCMDIobs2_clims/atmos/'+var+'/'+data+'/'
nc = var+'_mon_'+data+'_BE_gn_'+period+'.'+ver+'.AC.nc'
f = cdms.open(dir+nc)
d = f[var]
ogrid = d.getGrid()
print(ogrid)

# Target grid data
dir = '/p/user_pub/PCMDIobs/PCMDIobs2_clims/atmos/pr/GPCP-2-3/'
nc = 'pr_mon_GPCP-2-3_BE_gn_197901-201907.v20200421.AC.nc'
ft=cdms.open(dir+nc)
dt = ft['pr']
tgrid = dt.getGrid()
print(tgrid)

# Regridding
regridFunc = Regridder(ogrid, tgrid)
dr = regridFunc(d)

# Write data
out = cdms.open(var+'_mon_'+data+'_BE_gn_'+period+'.'+ver+'.AC_regrid.144x72.nc', 'w')
out.write(dr)
out.close()


# In[2]:


get_ipython().system('jupyter nbconvert --to script regridding.ipynb')

