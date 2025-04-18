def create_vcard(name, phone, email, address):
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
ADR;TYPE=HOME:;;{address}
END:VCARD
"""
    return vcard

name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")
address = input("Enter your address: ")

vcard_content = create_vcard(name, phone, email, address)

file_name = f"{name.replace(' ', '_')}.vcf"
with open(file_name, 'w') as file:
    file.write(vcard_content)

print(f"vCard created successfully: {file_name}")
