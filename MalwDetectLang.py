# FLARE Obfuscated String Solver [FLOSS] Output Parser 
# Last update 29/12/2025
# Ethan

# Imports

import json
from pathlib import Path

# File checking, collection and storage
print("What is the filepath")


# Load the dictionary once at startup
json_path = Path("language_detection.json")
malware_dict = json.loads(json_path.read_text(encoding="utf-8"))

file_path = input().strip().strip('"')
path  = Path(file_path)

def input_check(file_path):
    if file_path[-4:] == (".txt"):
        print("File Loaded successfully")
    else:
        print(f"Your file '{file_path}' is incompatible, you must use a file with the correct extension and filepath")

# Call .ext check function
input_check(file_path)

text = Path(file_path).read_text(encoding="utf-8", errors="replace")
lines = text.splitlines()

print(f"Loaded {len(lines)} lines")
print(lines[0:])