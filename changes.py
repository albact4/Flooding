import json
import re
"""
# Load the JSON data from the JavaScript file
with open('data\A1P.js', 'r') as js_file:
    js_data = js_file.read()

# Extract the JSON object from the JavaScript variable assignment
js_data = js_data[js_data.index('{') : js_data.rindex('}') + 1]

# Parse the JSON data
data = json.loads(js_data)

# Function to round coordinates to 5 significant figures
def round_coordinates(coordinates):
    return round(coordinates, 5)

# Modify the coordinates in the features
for feature in data['features']:
    coordinates = feature['geometry']['coordinates']
    for polygon in coordinates:
        for ring in polygon:
            for i, point in enumerate(ring):
                ring[i] = [round_coordinates(coord) for coord in point]

# Save the modified JSON data back to the file
with open('modified_js_file.js', 'w') as modified_js_file:
    modified_js_file.write('var A38P = ' + json.dumps(data, indent=4))

print("Coordinates rounded and saved to 'modified_js_file.js'")"""

import json
import re

def round_coordinates(coord_list):
    for i, coord in enumerate(coord_list):
        if isinstance(coord, list):
            round_coordinates(coord)
        else:
            coord_list[i] = round(coord, 10)

# Replace 'your_js_file.js' with the actual path to your JavaScript file
input_filename = 'data/A2P.js'
output_filename = input_filename.replace('.js', 'S.js')

# Read the JavaScript file
with open(input_filename, 'r') as js_file:
    js_content = js_file.read()

# Extract the JSON content from the JavaScript variable
match = re.search(r'\{.*\}', js_content, re.DOTALL)
if match:
    json_content = match.group()
    data = json.loads(json_content)

    # Modify the variable name
    variable_name = input_filename.replace('.js', 'S')

    # Iterate through features and modify coordinates
    for feature in data.get('features', []):
        geometry = feature.get('geometry', {})
        coordinates = geometry.get('coordinates', [])
        round_coordinates(coordinates)

    # Write the modified JSON content to the new JavaScript file
    with open(output_filename, 'w') as modified_js_file:
        modified_js_file.write(f'var {variable_name} = ' + json.dumps(data, indent=4))
else:
    print("JSON content not found in the JavaScript file.")






import os
import json

def round_coordinates(coord_list):
    for i, coord in enumerate(coord_list):
        if isinstance(coord, list):
            round_coordinates(coord)
        else:
            coord_list[i] = round(coord, 10)

input_folder = 'GeoJsons'  # Replace with the path to your folder

for filename in os.listdir(input_folder):
    if filename.endswith('.geojson'):
        input_filepath = os.path.join(input_folder, filename)
        output_filename = filename.replace('.geojson', '.js')
        output_filepath = os.path.join(input_folder, output_filename)

        with open(input_filepath, 'r') as geojson_file:
            geojson_content = geojson_file.read()
            data = json.loads(geojson_content)

            # Modify the variable name
            variable_name = output_filename.replace('.js', '').replace('-', '_') + 'S'

            # Modify the coordinates
            for feature in data.get('features', []):
                geometry = feature.get('geometry', {})
                coordinates = geometry.get('coordinates', [])
                round_coordinates(coordinates)

            # Write the modified content to the JavaScript file
            with open(output_filepath, 'w') as js_file:
                js_file.write(f'var {variable_name} = ' + json.dumps(data, indent=4))
                js_file.write('\n')

print("Conversion and variable declaration complete.")
