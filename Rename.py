# A quick utiity to rename files from original naming convention to the new naming convention
# without spaces.

import os
import re


def rename_files(directory):
    # Change to the target directory
    os.chdir(directory)

    # List all files in the directory
    files = os.listdir(directory)

    # Regular expression to match the file naming pattern "Problem N - [description].py"
    pattern = re.compile(r"Problem (\d{1,2}) - (.+)\.py")

    for file_name in files:
        match = pattern.match(file_name)
        if match:
            # Extract problem number and description
            number = int(match.group(1))
            description = match.group(2)

            # Format the new file name
            new_name = f"P{number:03d}_{description.replace(' ', '_')}.py"

            # Rename the file
            os.rename(file_name, new_name)
            print(f"Renamed: '{file_name}' to '{new_name}'")


# Specify the directory where your files are located
directory = "."
rename_files(directory)
