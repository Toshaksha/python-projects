README FILE
# QR Code Generator (Python)

A simple Python script that generates a QR code from user input (text or URL) and saves it as a `.png` image. Great for beginners learning to use third-party libraries and handle basic I/O!

---

## 🧰 Features

- Takes user input for any **text or URL**
- Saves the **QR code** as an image (`.png`)
- Validates input (no empty text or filename)
- Warns if the file already exists
- Fast and lightweight — no GUI needed

---

## ▶️ How to Run

1. Clone or download the repository
2. Make sure you have Python installed (3.6 or higher)
3. Install the required package:

   ```bash
   pip install qrcode[pil]
   ```
4.Run the script:

```bash
   python qr_code_generator.py
   ```

---

## 💡 Sample Output
```
Enter the text or URL: https://openai.com
Enter filename to save QR Code (without extension): openai_qr
✅ QR Code saved as openai_qr.png
```

---

## 🛠 Requirements
- Python 3.6+
qrcode module (with PIL support)
Install with:
    ```
    pip install qrcode[pil]

---

## 📚 What I Learned

- How to use third-party libraries in Python
- Handling user input and basic file operations
- Generating and saving images with simple code
- Writing clean, functional command-line scripts

---

## 🙌 Credits
Made with 💻 by Toshaksha — Happy QR-ing! 🧾📱
