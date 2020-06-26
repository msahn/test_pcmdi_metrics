#!/usr/bin/env python
# coding: utf-8

# # Read and land/sea masking (nc file)

# In[1]:


import cdms2 as cdms
import cdutil
import genutil
import MV2

# Read data
var = 'pr'
data = 'GPCP-2-3'
period = '197901-201907'
ver = 'v20200421'
dir = '/p/user_pub/PCMDIobs/PCMDIobs2_clims/atmos/'+var+'/'+data+'/'
nc = var+'_mon_'+data+'_BE_gn_'+period+'.'+ver+'.AC.nc'
f = cdms.open(dir+nc)

# Land/Sea masking
d = f[var]
mask = cdutil.generateLandSeaMask(d[0])
d, mask2 = genutil.grower(d, mask)
d_ocean = MV2.masked_where(mask2 == 1., d)
d_land = MV2.masked_where(mask2 == 0., d)

# Write data
out = cdms.open(var+'_mon_'+data+'_BE_gn_'+period +'.'+ver+'.AC_land.sea.mask.nc', 'w')
out.write(mask2[0])
out.close()


# In[2]:


get_ipython().system('jupyter nbconvert --to script cdat_land.sea.mask.ipynb')

