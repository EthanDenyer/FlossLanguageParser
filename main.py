# FLARE Obfuscated String Solver [FLOSS] Output Parser 
# Last update 23/09/2025
# Ethan Denyer ARR

# Imports

import os
from chardet.universaldetector import UniversalDetector # Encoding Discovery

# File checking, collection and storage Func
print("What is the filepath")

file_path = input()
correct_extension = ".txt"
detector = UniversalDetector()

def input_check(file_path):
    if file_path[-4:] == (".txt"):
        print("File Loaded successfully")
    else:
        print(f"Your file '{file_path}' is incompatible, you must use a file with the correct extension and filepath")

# Call .ext check function
input_check(file_path)

# Encoding Discovery (Chardet) Func
def get_file_encode(file_path):
    
    global encode_result
    encode_result = detector.result

# Call encoding
get_file_encode(file_path)

# Discovery Debug Func

def get_file_info(file_path):
    print("DEBUG:")
    print(f"{os.path.exists(file_path)} + | Path Existance")
    print(f"{os.path.getsize(file_path)} + | File Size")
    print(f"{os.path.splitext(file_path)} + | File Extension") # Already checked but no harm
    print("DEBUG Close:")

# File Opening

f = open({file_path}, 'r', encoding={encode_result})