Description

CodeAlpha-Organizer is a Python script designed to simplify file management by organizing files in a directory based on their type (e.g., images, documents, videos) and creation date. It is a handy tool for maintaining an organized workspace.

Features

Categorizes files into predefined types such as Images, Documents, Videos, Audio, Archives, and Others.

Creates subfolders based on the file's creation date (e.g., 2025-01).

Fully customizable file type categories.

Usage

Set Up the Paths:
Open the organize_files.py script and replace the placeholders:

source_dir = "path_to_source_directory"
destination_dir = "path_to_destination_directory"

Run the Script:
Execute the script using Python:

python organize_files.py

Check the Output:
The organized files will appear in the destination directory under categorized and date-specific subfolders.

Example

Input

Source Directory: Contains files like photo.jpg (created on 2025-01-10) and report.pdf (created on 2025-01-12).

Output

Destination Directory:

Images/2025-01/photo.jpg

Documents/2025-01/report.pdf

Customization

To add new file types or categories, edit the file_types dictionary in the script:

file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Custom": [".customext"]
}

Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests.

License

This project is licensed under the MIT License.
