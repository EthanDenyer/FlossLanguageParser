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

def input_check(file_path):
    if file_path[-4:] == (".txt"):
        print("File Loaded successfully")
    else:
        print(f"Your file '{file_path}' is incompatible, you must use a file with the correct extension and filepath")

# Call .ext check function
input_check(file_path)

# Encoding Discovery (Chardet) Func
def get_file_encode(file_path):
    
    detector = UniversalDetector()
    global encode_result

    # Read file in binary mode
    with open(file_path, "rb") as f:
        for line in f:
            detector.feed(line)
            if detector.done:  # stop early if confidence is high enough
                break
    detector.close()

    return detector.result  # this is a dict with encoding, confidence, language

# Call encoding

encode_result = get_file_encode(file_path) # Instance
print("Encode guess:", encode_result)

encoding = encode_result.get("encoding")
confidence = encode_result.get("confidence", 0.0)
# Discovery Debug Func

def get_file_info(file_path):
    print("DEBUG:")
    print(f"{os.path.exists(file_path)} + | Path Existance")
    print(f"{os.path.getsize(file_path)} + | File Size")
    print(f"{os.path.splitext(file_path)} + | File Extension") # Already checked but no harm
    print("DEBUG Close:")

# File Opening

f = open(file_path, 'r', encoding=encode_result["encoding"])