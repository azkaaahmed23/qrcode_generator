import qrcode
from PIL import Image

# Ask for text or URL
data = input("Enter the link or text you want to convert into a QR code: ").strip()

if not data:
    print("❌ You must enter some text or a link!")
    exit()

# Ask for filename
file_name = input("Enter a file name to save your QR code (without extension): ").strip()

# Ask for QR and background colors
fill_color = input("Enter QR code color (e.g., black, blue, #FF5733): ").strip() or "black"
back_color = input("Enter background color (e.g., white, yellow, #F0F0F0): ").strip() or "white"

# Create QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Generate QR image with custom colors
img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

# Ask if user wants to add a logo
add_logo = input("Do you want to add a logo in the center? (y/n): ").strip().lower()

if add_logo == "y":
    logo_path = input("Enter logo file path (PNG/JPG): ").strip()
    try:
        logo = Image.open(logo_path)

        # Resize logo to fit QR code
        logo_size = 80
        logo = logo.resize((logo_size, logo_size))

        # Get QR code size and calculate position
        qr_width, qr_height = img.size
        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

        # Paste logo onto QR code
        img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)

    except Exception as e:
        print(f"❌ Could not add logo: {e}")

# Save and show QR code
save_path = file_name + ".png"
img.save(save_path)
img.show()

print(f"\n✅ QR Code saved as {save_path}")
print("📷 Scan it with your phone or any QR scanner!")
