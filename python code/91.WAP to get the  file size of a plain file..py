import os
file_path = 'file.txt'
file_size = os.path.getsize(file_path)
print(f"File size of {file_path}: {file_size} bytes")
