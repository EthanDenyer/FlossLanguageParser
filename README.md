This is a Language Parser used for FLOSS output files specifically for use in Malware string dumps. The FLARE Obfuscated String Solver (FLOSS, formerly FireEye Labs Obfuscated String Solver) uses advanced static analysis techniques to automatically extract and deobfuscate all strings from malware binaries.

This tool works on the output of the FLOSS files to match FLOSS values to a JSON file in an attempt to detect language based strings. This can give indication of the different language types being used in the malware. This is particularly common in Malware which display messages to a user in their native language e.g. Ransomware GUIs.  

FlossLanguageParser is also progammed to identify common Windows API Calls, such as GetTimeZoneInformation or GetUserDefaultLangID used by malware to identify local languages based on API calls. 
