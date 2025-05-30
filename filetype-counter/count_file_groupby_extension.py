import os
from collections import defaultdict

# Find FIles by each extension
def count_files_by_extension(input_root):
    extension_counts = defaultdict(int)
    # Walk through all files
    for root, _, files in os.walk(input_root):
        for file in files:
            ext = os.path.splitext(file)[1].lower() or 'NO_EXT'
            extension_counts[ext] += 1
    return extension_counts

# Display results
def display_result(extension_counts):        
        print("📂 Unique file extensions and their counts:")
        for ext in sorted(extension_counts):
            print(f"{ext}: {extension_counts[ext]}")


