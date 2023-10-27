import numpy as np
import xarray as xr
import pandas as pd
import netCDF4 as nc
import os

# Path to input folder containing 3000 NetCDF files
input_folder = 'C:\\Users\\Rojano\\Desktop\\earthdata'

# Create an empty DataFrame to store the data
combined_df = pd.DataFrame()

for file_path in os.listdir(input_folder):
    if file_path.endswith('.nc4'):
        print("File", file_path, "opened.")

        # Open the NetCDF dataset
        dataset = xr.open_dataset(os.path.join(input_folder, file_path))

        # Specify the time range you want to work with (e.g., 2013-01-01 to 2023-01-01) 5 days for now
        start_date = '2013-01-01'
        end_date = '2018-01-01'

        # Select the time range
        data = dataset.sel(time=slice(start_date, end_date))

        # Extract variables of interest
        variables = dataset.variables.keys()

        # Create a DataFrame with the selected variables
        df = data[variables].to_dataframe()

        # Append the data to the combined DataFrame
        combined_df = pd.concat([combined_df, df])

        # Close the dataset
        dataset.close()
        
        print("File", file_path, "closed.")

# Reset the index of the combined DataFrame
combined_df.reset_index(inplace=True)

# Save the combined data to a CSV file
combined_df.to_csv('weather_data_combined.csv', index=False)

print("Done")
