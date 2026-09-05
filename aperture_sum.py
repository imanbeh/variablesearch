'''
aperture sum calculation
'''

from photutils.aperture import aperture_photometry, ApertureStats
from astropy.io import fits
import numpy as np

def ap_sum(dataframe, wavelength, data, aperture):
    '''
    dataframe: your dataframe with filenames, coordinates, and more
    wavelength: filter for data
    aperture: coordinates of star you want to do aperture photometry on
    '''
    dataframe.sort_values(by = ['Filename'], inplace = True)
    # star1

    sumstar = [None]*3
    apstats = [None]*3

    p1 = [None]*3
    i= 0
    i2 = 0
    #aperture = CircularAperture((3380.9988, 2184.2214), r=3.0)

    for j in dataframe['Filter nm']:
        if j == wavelength:
            print(i,j)
            print('nanmax: ',np.nanmax(data[i]))
            phot_table = aperture_photometry(data[i], aperture)
            phot_table['aperture_sum'].info.format = '%.8g'  # for consistent table output
            p1[i2] = phot_table

            #print(phot_table)

            # allow for error calculations in aperture
            apstats[i2] = ApertureStats(data[i], aperture)

            sumstar[i2] = phot_table['aperture_sum'][0]
            i2+=1
        i+=1
        
        
    print(sumstar)
    return sumstar, apstats


def ap_sum_2(dataframe, wavelength, data, aperture,files):
    '''
    dataframe: your dataframe with filenames, coordinates, and more
    wavelength: filter for data
    aperture: coordinates of star you want to do aperture photometry on

    trying to make sure image data is properly corresponding to coordinates
    '''
    dataframe.sort_values(by = ['Times'], inplace = True)
    # star1

    sumstar = [None]*3
    apstats = [None]*3

    p1 = [None]*3
    i2 = 0
    #aperture = CircularAperture((3380.9988, 2184.2214), r=3.0)
    dataframe.sort_values(by = ['Filename'], inplace = True)
    for j in range(3):
        i = dataframe.index[j]  #index of data

        file = fits.open('/Users/iman/Documents/amnh_rsch/47project/drcs/' + files[i] + '_final_drc_sci.fits')
        print(files[i])
        
                       
        dataframe.loc[[i]]

        phot_table = aperture_photometry(file[0].data, aperture)
        phot_table['aperture_sum'].info.format = '%.8g'  # for consistent table output
        p1[i2] = phot_table

        apstats[i2] = ApertureStats(file[0].data, aperture)
        
        sumstar[i2] = phot_table['aperture_sum'][0]
        i2+=1
        
        
    print(sumstar)
    return sumstar, apstats