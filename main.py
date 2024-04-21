import os
import shutil
from datetime import datetime

def get_month_year(date):
    return date.strftime("%B-%Y")

# Source directory where files are located
source_directory = "./"

for filename in os.listdir(source_directory):
    if filename.endswith('.py'):
        continue
    file_path = os.path.join(source_directory, filename)

    if os.path.isfile(file_path):
        # Get the creation or modification timestamp of the file
        file_stat = os.stat(file_path)
        file_date = datetime.fromtimestamp(file_stat.st_mtime)  # Use st_ctime for creation time

        # Create the target folder (Month-Year format)
        target_folder = os.path.join(source_directory, get_month_year(file_date))

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # Move the file to the target folder
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Moved '{filename}' to '{target_folder}'")

print("!! Done !!")