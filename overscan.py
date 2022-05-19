# Overscan bias processing
# Finds, displays, and calculates stats for overscan region
# of amplifier readout
# Option: Subtracts overscan value from data section
# Option: Trim overscan value from data section

# for development, define fits file and extention to compute
from astropy.io import fits

fits_file = ("/Users/smargheim/Desktop/testdata/blue_solar_hr00003.fits")
extension = 1

hdul = fits.open(fits_file)
hdr = hdul[extension].header
print(hdr)
# Get header values, transform to numpy array values
# Extract OS bias section
# Plot and run stats
# CCDSEC
# AMPSIZE
# AMPSEC
# BIASSEC
