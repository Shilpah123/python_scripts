import os
import re
import logging

#This script matches the pattern and replaces the content with the content from text file. xyz is the folder name pattern. 

# Configure logging to write to a file
log_file_path = 'C:/abc/log.txt'
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

def find_and_parse_folder(root_directory, source_file_name, destination_file_name, start_tag, end_tag, release_file):
    # Read the content of the replacement file
    with open(release_file, 'r') as release_file:
        replacement_content = release_file.read()

    # Walk through the directory tree starting from the root_directory
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.lower() == source_file_name.lower() and any(
                folder_name.lower() in dirpath.lower() for folder_name in ['xyz']
            ):
                # Construct the source and destination file paths
                source_file_path = os.path.join(dirpath, filename)
                destination_file_path = os.path.join(dirpath, destination_file_name)

                # Read the content from the source file
                with open(source_file_path, 'r') as source_file:
                    source_content = source_file.read()

                # Find and replace the specified block in the content
                pattern = re.compile(f'{re.escape(start_tag)}.*?{re.escape(end_tag)}', re.DOTALL)
                updated_content = pattern.sub(replacement_content, source_content)

                # Write the updated content to the destination file
                with open(destination_file_path, 'w') as destination_file:
                    destination_file.write(updated_content)

                # Log the information to the file
                log_message = f"Content from {release_file.name} updated in {destination_file_path}"
                logging.info(log_message)

# Specify the paths and filenames
root_directory = 'C:/abc'
source_file_name = 'index.html'
destination_file_name = 'index.html'
start_tag = '<span class="topicref">'
end_tag = '</span>'
release_file = 'C:/abc/release.txt'


find_and_parse_folder(root_directory, source_file_name, destination_file_name, start_tag, end_tag, release_file)
