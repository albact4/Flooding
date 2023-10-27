import xarray as xr
import pandas as pd

# Replace with the path to your NetCDF file
nc_file = 'C:\\Users\\Rojano\Desktop\\earthdata\\MERRA2_400.inst3_3d_asm_Np.20130104.nc4.nc4'  # Replace with the path to your NetCDF file

# Open the NetCDF dataset
dataset = xr.open_dataset(nc_file)

# Specify the time range you want to work with (e.g., 2013-01-01 to 2023-01-01)
start_date = '2013-01-01'
end_date = '2023-01-01'

# Select the time range
data = dataset.sel(time=slice(start_date, end_date))

# Extract variables of interest
# You can add more variables as needed
variables = dataset.variables.keys()

# Create a DataFrame with the selected variables
df = data[variables].to_dataframe()

# The resulting DataFrame will have a MultiIndex with 'time' and 'level' as levels
# You can reset the index for easier manipulation
df.reset_index(inplace=True)

# Optionally, you can save the data to a CSV file for future use
df.to_csv('weather_data.csv', index=False)

# Close the dataset
dataset.close()
