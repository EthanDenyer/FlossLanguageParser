# Creation 23/09/2025
# Last update 23/09/2025
# Ethan Denyer ARR


print("What is the filename")

file_input = input()
correct_extension = ".txt"

def input_check(file_input):
    if file_input[-4:] == (".txt"):
        print("File Loaded successfully")
    else:
        print(f"Your file '{file_input}' is incompatible, you must use a file with the correct extension")

# Call .ext check 
input_check(file_input)
