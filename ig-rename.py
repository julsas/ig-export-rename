import os
import re
import shutil
import zipfile

# Define the path to the zip file
path_to_zip_file = "medizininformatikinitiative-modulstudie-implementationguide-v1.0.0-ballot.zip"

# Define the directory containing the HTML files
#directory = "modul-medikation-ig-1.0-de@current"
directory = path_to_zip_file.replace(".zip", "")

# Define the directory to extract to
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory)

# Define a function to replace multiple substrings in a string
def multi_replace_regex(string, replacements, ignore_case=False):
    for pattern, repl in replacements.items():
        string = re.sub(pattern, repl, string, flags=re.I if ignore_case else 0)
    return string

# Define replacements for unwanted substrings in file names and html body
# Python 3.7 or later needed to preserve the order of the replacements in the dictionary
replacements = {
    'ImplementationGuide-1.x-TechnischeImplementierung-': '',
    'ImplementationGuide-1.x/TechnischeImplementierung/': '',
    'ImplementationGuide-2.x-TechnischeImplementierung-': '',
    'ImplementationGuide-2.x/TechnischeImplementierung/': '',
    'ImplementationGuide-1.x-': '',
    'ImplementationGuide-1.x/': '',
    'ImplementationGuide-2.x-': '',
    'ImplementationGuide-2.x/': '',
    '-1.x': '',
    '-2.x': ''
    }

# Loop through each file in the directory
for filename in os.listdir(directory):

    # Check if the file is an HTML file
    if filename.endswith(".html"):

        # Construct the old and new file paths
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, f"{multi_replace_regex(filename, replacements)}")

        # Rename the file
        os.rename(old_path, new_path)

        # Update the links in the HTML file
        with open(new_path, "r+") as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(multi_replace_regex(content, replacements))

# Create zip file
shutil.make_archive(directory, 'zip', directory)
