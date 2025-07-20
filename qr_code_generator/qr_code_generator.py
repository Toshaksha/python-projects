import qrcode
import os

# Get user input
url_link = input("Enter the text or URL: ").strip()
if not url_link:
    print("❌ Error: Text/URL cannot be empty.")
    exit()

filename = input("Enter filename to save QR Code (without extension): ").strip()
if not filename:
    print("❌ Error: Filename cannot be empty.")
    exit()

file_path = f"{filename}.png"

if os.path.exists(file_path):
    print("⚠️ Warning: File already exists and will be overwritten.")

# Create and save QR code
qr = qrcode.make(url_link)
qr.save(file_path)

print(f"✅ QR Code saved as {file_path}")
