import os
import shutil
from datetime import datetime

# Define placeholders for paths
source_dir = "path_to_source_directory"  # Replace with the directory to organize
destination_dir = "path_to_destination_directory"  # Replace with the target directory

# Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar.gz"],
    "Others": []
}

# Create folders if they don't exist
def create_folders():
    for category in file_types.keys():
        folder_path = os.path.join(destination_dir, category)
        print(f"Creating folder: {folder_path}")
        os.makedirs(folder_path, exist_ok=True)

# Organize files by type and date
def organize_files():
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        
        if os.path.isfile(file_path):
            category = "Others"
            for cat, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    category = cat
                    break
            
            creation_time = os.path.getmtime(file_path)
            creation_date = datetime.fromtimestamp(creation_time)
            folder_name = creation_date.strftime("%Y-%m")
            
            category_path = os.path.join(destination_dir, category, folder_name)
            os.makedirs(category_path, exist_ok=True)
            shutil.move(file_path, os.path.join(category_path, file))

    print("Files organized successfully!")

# Main execution
if __name__ == "__main__":
    # Check if paths are placeholders
    if "path_to_source_directory" in source_dir or "path_to_destination_directory" in destination_dir:
        print("Please update 'source_dir' and 'destination_dir' with valid paths before running the script.")
    else:
        try:
            create_folders()
            organize_files()
        except PermissionError as e:
            print(f"PermissionError: {e}")
            print("Ensure the script has permissions to write to the specified directory.")
