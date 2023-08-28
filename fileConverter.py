import os
import re
import json
import time


# Funtion to round coordinates to 10 decimal place
def round_coordinates(coord_list):
    for i, coord in enumerate(coord_list):
        if isinstance(coord, list):
            round_coordinates(coord)
        else:
            coord_list[i] = round(coord, 10)



# Path to input folder containing .geojson files
input_folder_geojson = 'C:\\Users\\Rojano\\Desktop\\GeoJsons\\formatting geojsons'

# Path to output folder containing new .js files
output_folder_js = 'C:\\Users\\Rojano\\Documents\\GitHub\\Flooding\\data\\AXS'



# Count the total number of .geojson files in the input folder
total_files = len([filename for filename in os.listdir(input_folder_geojson) if filename.endswith('.geojson')])

# Initialize an variable to count the processed files, so the user knows how many are left
processed_files = 0

# Initialize an empty array to store variable names
file_names = [] # Initialize an empty array to store variable names

# Get the current time before starting the processing
start_time = time.time()



# Iterate through each file in the input folder
for filename in os.listdir(input_folder_geojson):
    if filename.endswith('.geojson'):
        # Build input and output file paths
        input_filepath_geojson = os.path.join(input_folder_geojson, filename)
        output_filepath_js = os.path.join(output_folder_js, filename.replace('P.geojson', 'S.js'))

        # Read the content of the .geojson file
        with open(input_filepath_geojson, 'r') as geojson_file:
            geojson_content = geojson_file.read()

        # Search for JSON content within the .geojson file
        match = re.search(r'\{.*\}', geojson_content, re.DOTALL)
        if match:
            json_content = match.group()
            data = json.loads(json_content)

            # Modify the variable name and store it in the file_names array
            variable_name = filename.replace('P.geojson', 'S')
            # Append variable name to the array
            file_names.append(variable_name)  

            # Round coordinates within the JSON data
            for feature in data.get('features', []):
                geometry = feature.get('geometry', {})
                coordinates = geometry.get('coordinates', [])
                round_coordinates(coordinates)
            
            # Generate modified .js content
            modified_js_content = f'var {variable_name} = ' + json.dumps(data, indent=4)

            # Remove newlines and compress extra spaces
            modified_js_content = modified_js_content.replace('\n', ' ')
            modified_js_content = ' '.join(modified_js_content.split())

            # Write the modified .js content to the output file
            with open(output_filepath_js, 'w') as modified_js_file:
                modified_js_file.write(modified_js_content)

            # Write file names to a text file
            with open(os.path.join(output_folder_js, 'file_names.txt'), 'w') as file_names_file:
                file_names_file.write('\n'.join(file_names))
            
            # Update processed_files counter and print progress
            processed_files += 1
            print(f"Processed {processed_files} out of {total_files} files.")

        else:
            print("JSON content not found in the GeoJSON file.")

# Calculate the time duration
end_time = time.time()
time_duration = end_time - start_time

# Print completion message and time along with the file names array
print("GeoJSON files modified, converted to JS, and saved in", output_folder_js)
print("Duration of process", time_duration)
print("File names:", file_names)
