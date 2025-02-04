import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import random
import string
from datetime import datetime, timedelta
#Author: MMason

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"
processed_files = []  # List to keep track of processed files

"""If given string is blank return blank, otherwise replace"""
def perturb_name(s, syllables=2):
    """Replace with Randomly Generated name"""
    if s.strip() == "":
        return s
    else:
        name = ""
        for _ in range(syllables):
            name += random.choice(consonants) + random.choice(vowels)
        if random.random() > 0.5:
            name += random.choice(consonants)  # Sometimes end with a consonant
        return name.capitalize().ljust(35)


def perturb_ssn(s):
    """Replace with 9 random digits"""
    if s.strip() == "":
        return s
    else:
        area = random.randint(100, 999)  # First three digits
        group = random.randint(10, 99)   # Middle two digits
        serial = random.randint(1000, 9999)  # Last four digits
        return f"{area}{group}{serial}"
    
def perturb_phone(s):
    """Replace with random area code, random end, and 555 for the middle."""
    if s.strip() == "":
        return s
    else:
        area = random.randint(100, 999)  # First three digits
        exchange = '555'   # Middle three digits
        station = random.randint(1000, 9999)  # Last four digits
        return f"{area}{exchange}{station}"

def perturb_dob(s):
    """Replace with random Date"""
    if s.strip() == "":
        return s
    else:
        start_date = datetime(1900, 1, 1)
        end_date = datetime(2005, 12, 31)
        random_days = random.randint(0, (end_date - start_date).days)
        dob = start_date + timedelta(days=random_days)
        return dob.strftime("%Y%m%d")

def perturb_address(s):
    """Replace with generic address."""
    if s.strip() == "":
        return s
    else:
        return ('101 America Avenue').ljust(40)

def perturb_city(s):
    """Replace with Anytown."""
    if s.strip() == "":
        return s
    else:
        return ('Anytown').ljust(30)
    
def perturb_highschool(s):
    """Replace with Anytown High"""
    if s.strip() == "":
        return s
    else:
        return ('Anytown High').ljust(60)
    
def perturb_highschool_city(s):
    """Replace with Anytown"""
    if s.strip() == "":
        return s
    else:
        return ('Anytown').ljust(28)

def perturb_email(s, file_name):
    """Replace the email with the name of the ISIR file for reference. (e.g. idsa26op.dat@email.com)"""
    if s.strip() == "":
        return s
    else:
        new_email = (file_name + '@email.com').ljust(50)
        return new_email

def perturb_data(content, file_name):
    """Modify specific locations in the file content while keeping the format."""
    lines = content.split('\n')
    if len(lines) > 2:
        for i in range(1, len(lines) - 1):  # Skip header and trailer
            line = lines[i]
            if len(line) >= 1305:
                line = (
                    #Student Info
                    line[:242] + perturb_name(line[242:277]) +  # Student First Name
                    line[277:292] + perturb_name(line[292:327]) +  # Student Last Name
                    line[327:337] + perturb_dob(line[337:345]) +  # Student DOB
                    perturb_ssn(line[345:354]) +  # Student SSN
                    line[354:363] + perturb_phone(line[363:373]) + # Student phone
                    perturb_email(line[373:423], file_name) + #Student email
                    perturb_address(line[423:463]) +  # Student Street Address 
                    perturb_city(line[463:493]) + # Student City 
                    line[493:603] + perturb_highschool(line[603:663]) + # Student High School
                    perturb_highschool_city(line[663:691]) + 
                    #Spouse Info
                    line[691:1054] + perturb_name(line[1054:1089]) + # Spouse first name 
                    line[1089:1104] + perturb_name(line[1104:1139]) + # Spouse Last Name 
                    line[1139:1149] + perturb_dob(line[1149:1157]) + # Spouse DOB 
                    perturb_ssn(line[1157:1166]) + # Spouse SSN 
                    line[1166:1175] + perturb_phone(line[1175:1185]) + # Student phone
                    perturb_email(line[1185:1235], file_name) + #Spouse Email 
                    perturb_address(line[1235:1275]) + #spouse address 
                    perturb_city(line[1275:1305]) + #spouse city 
                    #Parent1 Information
                    line[1305:1510] + perturb_name(line[1510:1545]) +  # Parent1 First Name 
                    line[1545:1560] + perturb_name(line[1560:1595]) +  # Parent1 Last Name
                    line[1595:1605] + perturb_dob(line[1605:1613]) +  # Parent1 DOB 
                    perturb_ssn(line[1613:1622]) +  # Parent1 SSN 
                    line[1622:1631] + perturb_phone(line[1631:1641]) + # Student phone
                    perturb_email(line[1641:1691], file_name) + #Parent1 email 
                    perturb_address(line[1691:1731]) +  # Parent1 Street Address
                    perturb_city(line[1731:1761]) + # Parent1 City
                    #Parent2 Information
                    line[1761:2026] + perturb_name(line[2026:2061]) +  # Parent2 First Name 
                    line[2061:2076] + perturb_name(line[2076:2111]) +  # Parent2 Last Name
                    line[2111:2121] + perturb_dob(line[2121:2129]) +  # Parent2 DOB 
                    perturb_ssn(line[2129:2138]) +  # Parent2 SSN 
                    line[2138:2147] + perturb_phone(line[2147:2157]) + # Student phone
                    perturb_email(line[2157:2207], file_name) + #Parent2 email 
                    perturb_address(line[2207:2247]) +  # Parent2 Street Address
                    perturb_city(line[2247:2277]) + # Parent2 City
                    #Preparer Information
                    line[2277:2482] + perturb_name(line[2482:2517]) +  # Preparer First Name 
                    perturb_name(line[2517:2552]) +  # Preparer Last Name
                    perturb_ssn(line[2552:2561]) +  # Preparer SSN 
                    perturb_ssn(line[2561:2570]) +  # Preparer EIN
                    line[2570:2600] + perturb_address(line[2600:2640]) +  # Preparer Street Address
                    perturb_city(line[2640:2670]) + # Preparer City
                    line[2670:]
                    
                )
                assert len(line) == 7704, 'Line length modified'
                lines[i] = line
    return '\n'.join(lines)

def process_file(file_path):
    """Read, perturb, and save a new file in the program directory."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    file_name = os.path.basename(file_path)
    modified_content = perturb_data(content, file_name)
    
    new_file_name = os.path.basename(file_path).replace('.', '_perturbed.')
    new_file_path = os.path.join(os.getcwd(), new_file_name)  # Save in program directory
    
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    processed_files.append(os.path.basename(file_path))  # Add to processed list
    update_processed_list()
    
    status_label.config(text=f"")

def update_processed_list():
    """Update the label displaying processed files."""
    processed_label.config(text="Processed Files:\n" + '\n'.join(processed_files))

def on_drop(event):
    """Handle dropped files."""
    valid_prefixes = ("idsa", "igsa", "igsg", "igco")
    files = event.data.strip().split()  # Handle multiple files
    for file in files:
        file = file.strip('{}')  # Remove curly braces on Windows
        if os.path.basename(file).lower().startswith(valid_prefixes):
            process_file(file)
        else:
            status_label.config(text="Not a valid file: " + os.path.basename(file))

# Set up GUI
root = TkinterDnD.Tk()
root.title("ISIR Perturbation Tool")
root.geometry("400x300")

drop_label = tk.Label(root, text="Drag and drop ISIR files here", bg="lightgray", relief="ridge")
drop_label.pack(expand=True, fill="both", padx=10, pady=10)

drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', on_drop)

status_label = tk.Label(root, text="Waiting for files...")
status_label.pack(pady=10)

processed_label = tk.Label(root, text="Processed Files:\n", justify="left")
processed_label.pack(pady=10)

root.mainloop()
