
import os

# Find FIles by each extension
def count_total_files(folder_path):
    count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            count += 1
        
    return count
