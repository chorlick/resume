import qrcode

# Create a QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Define the vCard data
vcard = """BEGIN:VCARD
VERSION:3.0
FN;CHARSET=UTF-8:Christopher Mark Horlick
N;CHARSET=UTF-8:Horlick;Christopher;Mark;;
NICKNAME;CHARSET=UTF-8:chorlick
BDAY:19850203
EMAIL;CHARSET=UTF-8;type=HOME,INTERNET:chorlick@gmail.com
EMAIL;CHARSET=UTF-8;type=WORK,INTERNET:chorlick@gmail.com
TEL;TYPE=CELL:2564799562
TEL;TYPE=HOME,VOICE:2564799562
LABEL;CHARSET=UTF-8;TYPE=HOME:Home
ADR;CHARSET=UTF-8;TYPE=HOME:;;1318 Nolan Blvd;Madison;AL;35758;United States
TITLE;CHARSET=UTF-8:Software Engineer/Old School Telephone Hacker
ROLE;CHARSET=UTF-8:Programmer
ORG;CHARSET=UTF-8:Self
X-SOCIALPROFILE;TYPE=linkedin:https://www.linkedin.com/in/chris-horlick-10192310/
X-SOCIALPROFILE;TYPE=GitHub:https://www.github.com/chorlick
REV:2024-09-22T23:43:31.892Z
END:VCARD
"""

# Add the vCard data to the QR code object
qr.add_data(vcard)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("qr_code_vcard.png")