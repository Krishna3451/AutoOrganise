AutoOrganise: Your Intelligent File Sorter
AutoOrganise is a Python script designed to effortlessly declutter your folders by automatically sorting files based on their type.

Tired of messy downloads folders or disorganized project directories? AutoOrganise is here to save the day! With a simple command, it will neatly categorize your files into folders like "Images," "Documents," "Music," and more.

Features
Automatic Sorting: AutoOrganise intelligently analyzes file extensions and moves files to the appropriate folders.
Customizable: Easily add or modify the file types and folder names that AutoOrganise recognizes.
Safe and Efficient: Creates folders as needed and avoids overwriting files with the same name.
User-Friendly: Provides clear feedback on the progress of the file organization process.
Installation
Prerequisites: Ensure you have Python installed on your system.
Download: Clone this repository or download the Organise.py script.
Customize (Optional): Open the script and modify the extensions dictionary to match your preferred file types and folder names.
Usage
Open your terminal or command prompt.
Navigate to the directory containing the script:
Bash
cd path/to/AutoOrganise
Use code with caution.
content_copy
Run the script:
Bash
python Organise.py
Use code with caution.
content_copy
Specify the target directory (optional):
If you want to organize a specific folder, replace directory = r'C:\Users\YourUserName\Downloads' in the script with the path to your desired folder.
If you leave the default directory, the script will organize files in the current directory where it's running.
Supported File Types (Default)
AutoOrganise comes with a set of default file types and folder mappings:

Images: .jpg, .jpeg, .png, .gif
Documents: .pdf, .docx, .txt
Music: .mp3, .wav
Videos: .mp4, .avi, .mkv
Compressed: .zip, .rar
Executables: .exe
Feel free to customize this list to suit your needs!

Contributing
Contributions are welcome! If you have suggestions for improvement, new features, or bug fixes, please open an issue or submit a pull request.

Acknowledgements
Thanks to the Python community for the awesome os and shutil modules!
Inspired by the need for a cleaner desktop. 😊
