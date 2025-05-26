
import os

# Find FIles by each extension
def count_files(folder_path):
    count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            count += 1
        
    print(f"Total files in: {count}")
    

def main():
    folder = input("Enter a folder path: ")
    if not os.path.isdir(folder):
        print("Invalid folder.")
        return
    counts = count_files(folder)
    
if __name__ == "__main__":
    main()    