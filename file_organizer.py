#========Folder========#
# Note: Change the paths below to match the location of the files on your system.

# Define the path for the folder containing the files (change this path to your folder's path)
src_folder = "/path/to/your/folder"  # TODO: Change this path to your folder's path

# Define paths for image, video, audio, document, etc. folders
img_folder = os.path.join(src_folder, "image")
video_folder = os.path.join(src_folder, "Videos")
audio_folder = os.path.join(src_folder, "Audio")
docs_folder = os.path.join(src_folder, "Documents")
pdf_folder = os.path.join(src_folder, "PDFs")
zip_folder = os.path.join(src_folder, "Archives")
text_folder = os.path.join(src_folder, "Text")
code_folder = os.path.join(src_folder, "Code")

# Create the folders if they don't exist
folders = [img_folder, video_folder, audio_folder, docs_folder, pdf_folder, zip_folder, text_folder, code_folder]

#========EndFolder========#

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# List of files in the source folder
files = os.listdir(src_folder)

# Move files based on their extension
for file in files:
    name, ext = os.path.splitext(file)
    ext = ext.lower()
    src_path = os.path.join(src_folder, file)

    # Move files to the corresponding folders based on their extension
    if ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp']:
        dst_path = os.path.join(img_folder, file)
    elif ext in ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.webm', '.mpeg', '.mpg', '.3gp']:
        dst_path = os.path.join(video_folder, file)
    elif ext in ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a']:
        dst_path = os.path.join(audio_folder, file)
    elif ext in ['.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.odt', '.ods', '.odp']:
        dst_path = os.path.join(docs_folder, file)
    elif ext == '.pdf':
        dst_path = os.path.join(pdf_folder, file)
    elif ext in ['.zip', '.rar', '.7z', '.tar', '.gz']:
        dst_path = os.path.join(zip_folder, file)
    elif ext in ['.txt', '.md', '.rtf']:
        dst_path = os.path.join(text_folder, file)
    elif ext in ['.py', '.js', '.html', '.css', '.cpp', '.c', '.java', '.php', '.ts', '.json']:
        dst_path = os.path.join(code_folder, file)
    else:
        continue

    # Move the file to the appropriate folder
    shutil.move(src_path, dst_path)