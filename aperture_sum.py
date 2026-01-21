'''
aperture sum calculation
'''

from photutils.aperture import aperture_photometry

def ap_sum(dataframe, wavelength, data, aperture):
    '''
    dataframe: your dataframe with filenames, coordinates, and more
    wavelength: filter for data
    aperture: coordinates of star you want to do aperture photometry on
    '''
    dataframe.sort_values(by = ['Filename'], inplace = True)
    # star1

    sumstar = [None]*3

    p1 = [None]*3
    i= 0
    i2 = 0
    #aperture = CircularAperture((3380.9988, 2184.2214), r=3.0)

    for j in dataframe['Filter nm']:
        if j == wavelength:
            print(i,j)
            phot_table = aperture_photometry(data[i], aperture)
            phot_table['aperture_sum'].info.format = '%.8g'  # for consistent table output
            p1[i2] = phot_table
            sumstar[i2] = phot_table['aperture_sum'][0]
            i2+=1
        i+=1
        
        
    print(sumstar)
    return sumstar