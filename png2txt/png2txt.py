import os

# Input and output directory paths
input_dir = 'input'  # The folder containing PNG files
output_dir = 'output'  # The folder where text files will be created

# Ensure the output directory exists, create it if it doesn't
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List all files in the input directory
png_files = [f for f in os.listdir(input_dir) if f.endswith('.png')]

# Process each PNG file
for png_filename in png_files:
    # Extract the file name (without extension) from the PNG file
    file_name = os.path.splitext(png_filename)[0]
    
    # Create a text file with the same name as the PNG file but with a .txt extension
    txt_filename = os.path.join(output_dir, f'{file_name}.txt')
    
    # Write the file name to the text file
    with open(txt_filename, 'w') as txt_file:
        txt_file.write(file_name)

    print(f'File name "{file_name}" has been saved to {txt_filename}')