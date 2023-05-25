# variablesearch
This repository stores code for finding variable stars in globular clusters

FILES:

Creating a Pipeline to Search for Dwarf Nova Eruptions in Globular Cluster M15 (paper):

Undergraduate thesis paper on how to computationally find variable stars in globular clusters using image subtraction (via "SWIFT Subtract Writeup"). This study uses UVOT data from SWIFT telescope archival images of globular cluster Messier 15. Resulted in a catalog of 169 variable star candidates, later reduced to 38 using "Table Analysis Writeup."


SWIFT Subtract Writeup (code):

The user enters two fits files for subtraction. User needs to define a center for each image around which the difference image will be calibrated. The final image can be analyzed in ds9 for variable stars. Methodology for analysis can be found in the Methods section of "Creating a Pipeline to Search for Dwarf Nova Eruptions in Globular Cluster M15," also in this repository.

Table Analysis Writeup (code):

This code allows the user to compare a list of stellar objects with a list of known objects. The intention is to identify which sources from the original list are undiscovered. This is written for a case in which the comparison dataset is a list of known rr lyra. Repeat sources will be removed, resulting in a final table of unique objects.
