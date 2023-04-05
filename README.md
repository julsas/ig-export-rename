# ig-export-rename

A script to modify the .html files exported from a Simplifier implementation guide.
The tool is primarily intended to quickly generate a desired url scheme.

## Prerequisites
* Python 3.7 or later

## Usage
* Export an implementation guide from Simplifier and receive the zip file
* In `ig-rename.py` modify the `path_to_zip_file` variable to point to the zip file
* Define replacements for unwanted substrings in file names and html body in the `replacements` dict
* Run:

```bash
python ig-rename.py
```
