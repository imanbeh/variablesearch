from matplotlib.colors import LogNorm
import numpy as np

#define background measuring functions
def measureBG(image, mask=None, poissonStats=False, boxsize=65, 
              minDataSize=1000):
    """Find average background using sigma clipping method.
 
    Args:
        image: 2D numpy array for which a background map 
            should be found. The data is assumed to be counts!
        mask: Optional 2D numpy array or fits image with True values at pixels 
            that should be masked.
        poissonStats: If present, Poissonian statistics are used instead of 
            Gaussian. i.e the expectation value is equal to the variance, not
            the mean.
        boxsize: Size of box in which background is found and tiled throughout 
            the image. Should be odd to have an exact pixel center.
        minDataSize: The minimum number of data points to consider having 
            good enough statistics to accurately calculate the mean, std.
 
    Returns:
        avgBG: The average background value over the whole image.
        avgBGerr: The rms uncertainty in the avgBG
    """
    #check if boxsize is odd
    if boxsize%2 == 0:
        print("WARNING: Background boxsize is even...adding one to make it odd")
        boxsize += 1
 
    if mask is not None:
        data = image[np.logical_not(mask)]
    else:
        data = image
     
    #find avg background value and error
    (avgBG, avgBGerr) = sigmaClip(data)
    if poissonStats:
        avgBG = avgBGerr**2
 
    
    return avgBG, avgBGerr
 
#########################################################333
 
def sigmaClip(data, numSigma=3.0, cenfunc=np.median):
    """Find the best estimate of the mean and standard deviation of a background
    distribution by iteratively clipping data beyond +/- some number of standard
    deviations.
 
    Args:
        data: A numpy array of the data that you wish to know the background
            distribution for.
        sigma: The number of standard deviations beyond which data is clipped.
        cenfunc: Optional choice of function to find the 'center' of the data. 
            Defaults to the median to be less affected by strong outliers.
 
    Returns: The mean and standard deviation of the clipped data.
    """
    data = data.ravel()
    clippingMask = np.ones(data.size, bool)
    lastKeep = 0
    while(np.sum(clippingMask) != lastKeep):
        lastKeep = np.sum(clippingMask)
        if cenfunc == np.mean:
            diff = data - cenfunc(data[clippingMask], dtype=np.float64)
        else:
            diff = data - cenfunc(data[clippingMask])
        diff = np.abs(diff)
        clippingMask = (diff <= np.std(data[clippingMask], dtype=np.float64) *
                        numSigma)
 
    return (np.mean(data[clippingMask], dtype=np.float64), 
            np.std(data[clippingMask], dtype=np.float64))