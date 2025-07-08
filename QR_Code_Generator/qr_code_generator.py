import qrcode

# Get user input
url_link = input("Enter the text or URL: ").strip()
filename = input("Enter filename to save QR Code (without extension): ").strip()

# Create QR code
qr = qrcode.make(url_link)

# Save the QR code image
qr.save(f"{filename}.png")

print(f"QR Code saved as {filename}.png")
