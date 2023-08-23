import os

input_folder = 'C:\\Users\\Rojano\\Documents\\GitHub\\Flooding\\data\\AXPP'  # Replace with the path to your folder containing files

for filename in os.listdir(input_folder):
    if filename.endswith('.js'):  # Change the extension as needed
        input_filepath = os.path.join(input_folder, filename)

        with open(input_filepath, 'r') as file:
            content = file.read()

        # Replace newline characters with spaces
        content = content.replace('\n', ' ')

        # Remove extra consecutive spaces
        content = ' '.join(content.split())

        # Write the modified content back to the file
        with open(input_filepath, 'w') as file:
            file.write(content)

print("Newlines removed and extra spaces compressed from files in the folder.")


"""



input_filename = 'data\A2S.js'  # Replace with the path to your file

with open(input_filename, 'r') as file:
    content = file.read()

# Replace newline characters with spaces
content = content.replace('\n', ' ')

# Remove extra consecutive spaces
content = ' '.join(content.split())

# Write the modified content back to the file
with open(input_filename, 'w') as file:
    file.write(content)

print("Newlines removed and extra spaces compressed from the file.")"""
