# import sys
from astropy.io import fits as pyfits
import numpy as np

import matplotlib.pyplot as plt


hdulist = pyfits.open( "/Users/pkabranov/Downloads/ADP.2017-10-26T08_49_26.861.fits" )
# get to the data part (in extension 1)
scidata = hdulist[1].data
#print(hdulist[1].header)


wave = scidata[0]['WAVE']
arr1 = scidata[0]['ERR_REDUCED']
arr2 = scidata[0]['FLUX_REDUCED']
arr3 = scidata[0]['BGFLUX_REDUCED']

#plt.axis([4000, 8000, 0, 2000])

plt.title('ERR_REDUCED')
plt.plot(wave, arr1)
plt.show()
plt.title('FLUX_REDUCED')
plt.plot(wave, arr2)
plt.show()
plt.title('BGFLUX_REDUCED')
plt.plot(wave, arr3)
plt.show()


from scipy.io.idl import readsav
data157 = readsav('/Users/pkabranov/Downloads/star157.sav')
data87 = readsav('/Users/pkabranov/Downloads/star87.sav')

print(data157.keys())
print(data87.keys())

plt.figure()
plt.ylabel('fluxes')
plt.xlabel('DEC')
plt.plot(data157['w'], data157['s'], '-')
plt.title('star157.sav')
#plt.axis([0, 10, 0, 5])
plt.show()

plt.figure()
plt.ylabel('fluxes')
plt.xlabel('DEC')
plt.plot(data87['w'], data87['s'], '-')
#plt.axis([0, 10, 0, 5])
plt.title('star87.sav')
plt.show()