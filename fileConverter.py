import os
import re
import json

def round_coordinates(coord_list):
    for i, coord in enumerate(coord_list):
        if isinstance(coord, list):
            round_coordinates(coord)
        else:
            coord_list[i] = round(coord, 10)

input_folder_geojson = 'C:\\Users\\Rojano\\Desktop\\GeoJsons\\formatting geojsons'
output_folder_js = 'C:\\Users\\Rojano\\Documents\\GitHub\\Flooding\\data\\AXS'

total_files = len([filename for filename in os.listdir(input_folder_geojson) if filename.endswith('.geojson')])
processed_files = 0

for filename in os.listdir(input_folder_geojson):
    if filename.endswith('.geojson'):
        input_filepath_geojson = os.path.join(input_folder_geojson, filename)
        output_filepath_js = os.path.join(output_folder_js, filename.replace('P.geojson', 'S.js'))

        with open(input_filepath_geojson, 'r') as geojson_file:
            geojson_content = geojson_file.read()

        match = re.search(r'\{.*\}', geojson_content, re.DOTALL)
        if match:
            json_content = match.group()
            data = json.loads(json_content)

            variable_name = filename.replace('P.geojson', 'S')

            for feature in data.get('features', []):
                geometry = feature.get('geometry', {})
                coordinates = geometry.get('coordinates', [])
                round_coordinates(coordinates)

            modified_js_content = f'var {variable_name} = ' + json.dumps(data, indent=4)

            # Remove newlines and compress extra spaces
            modified_js_content = modified_js_content.replace('\n', ' ')
            modified_js_content = ' '.join(modified_js_content.split())

            with open(output_filepath_js, 'w') as modified_js_file:
                modified_js_file.write(modified_js_content)
            processed_files += 1
            print(f"Processed {processed_files} out of {total_files} files.")

        else:
            print("JSON content not found in the GeoJSON file.")

print("GeoJSON files modified, converted to JS, and saved in", output_folder_js)
