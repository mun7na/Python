file_name = "Automated_first_file.txt"

text = "This is my first automation file with text."

with open(file_name, 'w') as file:
    file.write(text)

print(f"{file_name} has been created.")