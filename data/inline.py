input_filename = 'data\A1S.js'  # Replace with the path to your file


with open(input_filename, 'r') as file:
    content = file.read()

# Remove newline characters
content_without_newlines = content.replace('\n', '')

# Write the modified content back to the file
with open(input_filename, 'w') as file:
    file.write(content_without_newlines)


print("Newlines removed from the file.")
