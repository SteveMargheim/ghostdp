from astropy.io import fits
import os
from typing import List

fits_files: List[str] = []
# Set directory where data is to be found
working_dir = "/Users/smargheim/Desktop/testdata"

# Discover fits files in working directory
number_of_fits_files = 0
for file in os.listdir(working_dir):
    if file.endswith('.fits'):
        fits_files.append(file)
        number_of_fits_files += 1

print(number_of_fits_files)
print(fits_files)

