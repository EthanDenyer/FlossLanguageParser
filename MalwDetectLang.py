# FLARE Obfuscated String Solver [FLOSS] Output Parser 
# Last update 30/12/2025
# JSON Last Update 29/12/2025
# Logic is my own, early writeouts and tests were all performed by myself. AI was used to tidy up final version and make logic more readable and compact. 
# Respective Docs found online for imports


# Imports

import json
from pathlib import Path

# Stores # Examples

hex_matches = []             # 0x0422
decimal_matches = []         # 1058
locale_matches = []          # en-US
api_matches = []             # GetSystemDefaultLangID
native_name_matches = []     # Русский
language_name_matches = []   # English (Australia) Variance by Nation 
country_name_matches = []    # Belarus
iso_code_matches = []        # UA (Ukraine)

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

# #DEBUG STRINGS
# print(f"Loaded {len(lines)} lines")
# print(lines[0:])

# JSON Verify Load
print(f"Loaded {len(malware_dict)} sections")
print(f"CIS countries: {len(malware_dict['cis_exclusion_patterns']['standard_cis_list'])}")

#STORE ASSIGNMENT
lcid_database = malware_dict["complete_windows_lcid_database"]["languages"]
cis_list = malware_dict["cis_exclusion_patterns"]["standard_cis_list"]  
api_functions = malware_dict["windows_api_locale_functions"]["functions"]

#LCID database DEBUG
print(f"LCID database has {len(lcid_database)} entries")
print(f"CIS exclusion list has {len(cis_list)} entries")  
print(f"First LCID entry: {lcid_database[0]}")

# Loop once
for line_num, line in enumerate(lines):
    
    # Check ALL LCID
    for entry in lcid_database:
        
        # Hex
        if entry["lcid_hex"] in line:
            hex_matches.append({
                "hex": entry["lcid_hex"],
                "language": entry["language"],
                "line_number": line_num,
                "line_content": line
            })
        
        # Decimal
        if entry["lcid_dec"] in line:
            decimal_matches.append({
                "decimal": entry["lcid_dec"],
                "language": entry["language"],
                "line_number": line_num,
                "line_content": line
            })
        
        # Locale
        if entry["locale"] in line:
            locale_matches.append({
                "locale": entry["locale"],
                "language": entry["language"],
                "line_number": line_num,
                "line_content": line
            })
        
        # Language name
        if entry["language"] in line:
            language_name_matches.append({
                "language_name": entry["language"],
                "locale": entry["locale"],
                "line_number": line_num,
                "line_content": line
            })
        
        # ISO code
        if entry["iso_639_2"] in line:
            iso_code_matches.append({
                "iso_code": entry["iso_639_2"],
                "language": entry["language"],
                "line_number": line_num,
                "line_content": line
            })
    
    # Also check CIS exclusion patterns
    for cis_entry in cis_list:
        
        # Hex
        if cis_entry["lcid_hex"] in line:
            hex_matches.append({
                "hex": cis_entry["lcid_hex"],
                "language": f"{cis_entry['country']} (CIS)",  # Mark as CIS
                "line_number": line_num,
                "line_content": line
            })
        
        # Decimal
        if cis_entry["lcid_dec"] in line:
            decimal_matches.append({
                "decimal": cis_entry["lcid_dec"],
                "language": f"{cis_entry['country']} (CIS)",
                "line_number": line_num,
                "line_content": line
            })
        
        # CIS list 
        if cis_entry["lang"] in line:
            locale_matches.append({
                "locale": cis_entry["lang"],
                "language": f"{cis_entry['country']} (CIS)",
                "line_number": line_num,
                "line_content": line
            })
        
        # Native name
        if cis_entry["native"] in line:
            native_name_matches.append({
                "native_name": cis_entry["native"],
                "country": cis_entry["country"],
                "line_number": line_num,
                "line_content": line
            })
        
        # Country name
        if cis_entry["country"] in line:
            country_name_matches.append({
                "country": cis_entry["country"],
                "native_name": cis_entry["native"],
                "line_number": line_num,
                "line_content": line
            })
        
        # ISO code from CIS
        if cis_entry["lang"] in line:
            iso_code_matches.append({
                "iso_code": cis_entry["lang"],
                "country": cis_entry["country"],
                "line_number": line_num,
                "line_content": line
            })
    
    # Check all API functions for this line
    for api in api_functions:
        if api["name"] in line:
            api_matches.append({
                "api": api["name"],
                "dll": api["dll"],
                "line_number": line_num,
                "line_content": line
            })

# Display all results with details
if len(hex_matches) > 0:
    print(f"Found {len(hex_matches)} HEX matches:")
    for match in hex_matches:
        print(f"  {match['hex']} = {match['language']} on line {match['line_number']}")
else:
    print("No matches hex")

if len(decimal_matches) > 0:
    print(f"Found {len(decimal_matches)} DECIMAL matches:")
    for match in decimal_matches:
        print(f"  {match['decimal']} = {match['language']} on line {match['line_number']}")
else:
    print("No matches decimal")

if len(locale_matches) > 0:
    print(f"Found {len(locale_matches)} LOCALE matches:")
    for match in locale_matches:
        print(f"  {match['locale']} = {match['language']} on line {match['line_number']}")
else:
    print("No matches locale")

if len(api_matches) > 0:
    print(f"Found {len(api_matches)} API matches:")
    for match in api_matches:
        print(f"  {match['api']} on line {match['line_number']}")
else:
    print("No matches API")

#  native name matches
if len(native_name_matches) > 0:
    print(f"Found {len(native_name_matches)} NATIVE NAME matches:")
    for match in native_name_matches:
        print(f"  {match['native_name']} = {match['country']} on line {match['line_number']}")
else:
    print("No matches native name")

# Display language name matches
if len(language_name_matches) > 0:
    print(f"Found {len(language_name_matches)} LANGUAGE NAME matches:")
    for match in language_name_matches:
        print(f"  {match['language_name']} on line {match['line_number']}")
else:
    print("No matches language name")

# Display country name matches
if len(country_name_matches) > 0:
    print(f"Found {len(country_name_matches)} COUNTRY NAME matches:")
    for match in country_name_matches:
        print(f"  {match['country']} ({match['native_name']}) on line {match['line_number']}")
else:
    print("No matches country name")

# Display ISO code matches
if len(iso_code_matches) > 0:
    print(f"Found {len(iso_code_matches)} ISO CODE matches:")
    for match in iso_code_matches:
        if "language" in match:
            print(f"  {match['iso_code']} = {match['language']} on line {match['line_number']}")
        else:
            print(f"  {match['iso_code']} = {match['country']} on line {match['line_number']}")
else:
    print("No matches ISO code")