placeholder = "[name]"

with open("names.txt") as names:
    content = names.readlines()
    
with open("letter.docx") as letter:
    letter_content = letter.read()
    for name in content:
        guest = name.strip()
        new_letter = letter_content.replace(placeholder,guest)
        with open(f"{guest}.docx", mode="w") as invite:
            invite.write(new_letter)
             
            
    