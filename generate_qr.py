import qrcode
import os

def generate_qr(data, filename):
    os.makedirs("qr_codes", exist_ok=True)
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qr_codes/{filename}.png")
    print(f"QR Code saved as qr_codes/{filename}.png")

# Example QR generations
generate_qr("John Doe,1001", "John_Doe")
generate_qr("Subham Roy,1004", "Subham_Roy")
generate_qr("Namaji subhamn,1006", "namaji_subhan")
generate_qr("Alice66 Smith,10065", "Alice66_Smith")
generate_qr("Alice666 Smith,100665", "Alice666_Smith")
generate_qr("Alice6 Smith,1006665", "Alice6_Smith")
generate_qr("tej,5b5", "tej_5b5")
