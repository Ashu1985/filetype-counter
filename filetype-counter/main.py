import argparse
import os
from .count_files import count_total_files
from .count_file_groupby_extension import count_files_by_extension

def run():
    parser = argparse.ArgumentParser(description="Count files in a folder (recursively).")
    parser.add_argument('-groupby', choices=['Extension', 'None'], required=True,
                        help="Group by 'Extension' to get counts per file type, or 'None' for total count.")
    parser.add_argument('-FolderPath', required=True, help="Path to the folder to scan")

    raw_path = args.FolderPath.strip('"').strip("'")
    folder = os.path.normpath(raw_path)

    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid folder path.")
        return

    if args.groupby == 'None':
        total = count_total_files(folder)
        print(f"Total files in '{folder}': {total}")
    else:
        counts = count_files_by_extension(folder)
		display_result(counts)
