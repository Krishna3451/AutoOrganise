import os
import shutil

# Define the directory to organize
directory = 'C:\\Users\\YourUserName\\Downloads'  # Replace with your desired directory

# Dictionary mapping file extensions to folder names
extensions = {
    # Images
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
    # Documents
    '.pdf': 'Documents', '.docx': 'Documents', '.txt': 'Documents',
    # Music
    '.mp3': 'Music', '.wav': 'Music',
    # Videos
    '.mp4': 'Videos', '.avi': 'Videos', '.mkv': 'Videos',
    # Compressed
    '.zip': 'Compressed', '.rar': 'Compressed',
    # Other
    '.exe': 'Executables'
}

# Iterate over files in the directory
for filename in os.listdir(directory):
    # Get the file extension
    ext = os.path.splitext(filename)[1].lower()
    
    # Check if the extension is in our dictionary
    if ext in extensions:
        # Create the folder if it doesn't exist
        folder_name = extensions[ext]
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Move the file to the appropriate folder
        src_path = os.path.join(directory, filename)
        dest_path = os.path.join(folder_path, filename)
        shutil.move(src_path, dest_path)
        print(f"Moved '{filename}' to '{folder_name}'")
