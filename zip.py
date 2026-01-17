import os
import zipfile

# Define directories
pack_dir = 'pack'
output_dir = 'output'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Delete all old files in output directory
for file in os.listdir(output_dir):
    file_path = os.path.join(output_dir, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

# Define zip file name and path
zip_name = 'resources.zip'
zip_path = os.path.join(output_dir, zip_name)

# Create the zip file
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(pack_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Use relative path to avoid including 'pack/' in the zip
            arcname = os.path.relpath(file_path, pack_dir)
            zipf.write(file_path, arcname)

print(f"Created zip file: {zip_path}")