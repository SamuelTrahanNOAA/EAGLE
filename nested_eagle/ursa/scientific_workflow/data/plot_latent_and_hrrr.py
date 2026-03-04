#!/usr/bin/env python3

import xarray
import matplotlib
import numpy
import xarray
from matplotlib import pyplot as plt

zarrhrrr=xarray.open_dataset("hrrr.zarr", cache=False, create_default_indexes=False)
gridhrrr=xarray.open_dataset("hrrr_6km.nc", cache=False, create_default_indexes=False)

grid_lat_b_flat = numpy.asarray(gridhrrr.lat_b.as_numpy()).flatten()
grid_lon_b_flat = numpy.asarray(gridhrrr.lon_b.as_numpy()).flatten()

grid_lon_flat = numpy.asarray(gridhrrr.lon.as_numpy()).flatten()
grid_lat_flat = numpy.asarray(gridhrrr.lat.as_numpy()).flatten()

zarr_lat_flat = numpy.asarray(zarrhrrr['latitudes'].as_numpy()).flatten()
zarr_lon_flat = numpy.asarray(zarrhrrr['longitudes'].as_numpy()).flatten()

latent = numpy.load('latentx2.spongex1.combined.sorted.npz')
latent_lat = latent['lat']
latent_lon = latent['lon']

#plt.scatter(grid_lon_b_flat, grid_lat_b_flat, marker='*', color='orange')
plt.scatter(grid_lon_flat, grid_lat_flat, marker='.', color='black', label='HRRR 6km Grid')
plt.scatter(latent_lon, latent_lat, marker='*', color='orange', label='Latent Grid')
#plt.scatter(zarr_lon_flat, zarr_lat_flat, marker='o', color='blue')
plt.xlim(286.0, 287.5)
plt.ylim(21.6, 22.3)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('HRRR 6km Grid & 3x Coarsened Latent Grid')
plt.legend()
plt.show()
