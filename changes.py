
import os
import re
import json


def round_coordinates(coord_list):
    for i, coord in enumerate(coord_list):
        if isinstance(coord, list):
            round_coordinates(coord)
        else:
            coord_list[i] = round(coord, 10)

# Replace with the path to your folder containing .geojson files
input_folder = 'C:\\Users\\Rojano\\Desktop\\GeoJsons\\formatting geojsons'

# Replace with the path to the folder where you want to save modified files
output_folder = 'C:\\Users\\Rojano\\Documents\\GitHub\\Flooding\\data\\AXP'


for filename in os.listdir(input_folder):
    if filename.endswith('.geojson'):
        input_filepath = os.path.join(input_folder, filename)
        output_filepath = os.path.join(output_folder, filename.replace('.geojson', 'P.js')) 


    with open(input_filepath, 'r') as geojson_file:
            geojson_content = geojson_file.read()

    match = re.search(r'\{.*\}', geojson_content, re.DOTALL)
    if match:
        json_content = match.group()
        data = json.loads(json_content)

        variable_name = filename.replace('.geojson', 'P')

        for feature in data.get('features', []):
            geometry = feature.get('geometry', {})
            coordinates = geometry.get('coordinates', [])
            round_coordinates(coordinates)

        with open(output_filepath, 'w') as modified_js_file:
            modified_js_file.write(f'var {variable_name} = ' + json.dumps(data, indent=4))
    else:
        print("JSON content not found in the GeoJSON file.")

print("GeoJSON files modified and saved in", output_folder)





"""
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

print("Conversion and variable declaration complete.")"""
