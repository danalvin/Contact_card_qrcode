from qrcode import QRCode, constants
from vobject import vCard
from PIL import Image

# Create a vCard object
contact = vCard()
contact.add('fn').value = "Dan Alvin Mungai"  # Full name
contact.add('tel').value = "+254701635973"  # Phone number
contact.add('email').value = "mungaiwaituika@gmail.com"  # Email address

# Generate a vCard string
vcard_data = contact.serialize()

# Create a QR code with the vCard data
qr = QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(vcard_data)
qr.make(fit=True)

# Create an image from the QR code with a transparent background
qr_image = qr.make_image(fill_color="lime", back_color=None)

# Save the QR code as an image with a transparent background
qr_image.save("contact_qr_code.png")

