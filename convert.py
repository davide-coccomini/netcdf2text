import netCDF4
import json
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

precip_nc_file = 'filepath'
nc = netCDF4.Dataset(precip_nc_file, mode='r')

print(nc.variables.keys())

lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
u10 = np.asarray(nc.variables['u10'][:][:][:]).tolist()
v10 = np.asarray(nc.variables['v10'][:][:][:]).tolist()
d2m = np.asarray(nc.variables['d2m'][:][:][:]).tolist()
t2m = np.asarray(nc.variables['t2m'][:][:][:]).tolist()
time = nc.variables['time']

x = {
    "lat": lat,
    "lon": lon,
    "time": time,
    "u10": u10,
    "v10": v10,
    "d2m": d2m,
    "t2m": t2m
}
with open("weather.txt", 'w') as f:
    print(x, file=f)
