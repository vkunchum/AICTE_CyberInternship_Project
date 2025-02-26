# Secure Data Hiding in Images Using Steganography

## 📌 Project Overview
This project implements **image-based steganography** to securely hide and retrieve text messages within digital images. It consists of **separate encryption and decryption scripts** to enhance modularity and security. The encryption process embeds a secret message within an image using **pixel-based modifications**, while the decryption process retrieves it **only if the correct passcode is provided**.

---

## 📌 How It Works
1. **Encryption (`encrypt.py`)**  
   - The user provides a **cover image** (`.jpg` or `.png`).
   - A **secret message** and **passcode** are entered.
   - The message is encoded into the **least significant bits (LSB)** of the image pixels.
   - The **encrypted image** is saved as a **`.png`** to prevent data corruption.

2. **Decryption (`decrypt.py`)**  
   - The encrypted `.png` image is loaded.
   - The user enters the **passcode** to unlock the hidden message.
   - If the passcode matches, the message is extracted correctly.
   - If the passcode is incorrect, access is denied.

---

## 📌 Technologies Used
- **Python** – Core programming language
- **OpenCV** – Image processing library for reading/writing images
- **ASCII Encoding** – Converts text into numerical format for embedding
- **Steganography Techniques** – LSB (Least Significant Bit) modification to hide data
- **PNG Format** – Ensures lossless compression to preserve pixel values

---

## 📌 Installation Instructions
### 🔹 Step 1: Install Required Dependencies
Ensure you have **Python 3.x** installed. Then, install the required packages using:
```bash
pip install opencv-python
###  Step 2: Clone This Repository
git clone https://github.com/your-username/steganography-project.git
cd steganography-project

Step 3: Run the Encryption Script
1.Place your cover image (e.g., flower.jpg) in the project folder.
2.Run the following command: python encrypt.py
3.Enter your secret message and passcode when prompted.
4.The encrypted image will be saved as encryptedImage.png.
🔹 Step 4: Run the Decryption Script
    python decrypt.py
Enter the same passcode used during encryption.
If correct, the hidden message will be displayed.
Example Usage
Encrypting a Message:
 Enter secret message: This is a hidden message.
 Enter a passcode: secure123
 Encryption successful! Encrypted image saved as 'encryptedImage.png'.

Decrypting the Message:
 Enter passcode for Decryption: secure123
 Decryption successful!
 Decrypted Message: This is a hidden message.

Incorrect Password Example:
 Enter passcode for Decryption: wrongpass
 Incorrect passcode! Access denied.

Features & Benefits
✅ Data Concealment – Hides messages in images without noticeable alterations.
✅ Passcode Protection – Only authorized users can retrieve hidden messages.
✅ Lossless Data Storage – Uses .png format to ensure data is preserved.
✅ Standalone Encryption & Decryption – Improves modularity and security.
✅ Automated Message Length Handling – No need for manual message length input.

Limitations & Future Scope
🔹 Current Limitations:
Supports only text-based hidden messages.
Message length must be less than 255 characters.
🔹 Future Enhancements:
AES Encryption Integration – Adding an additional encryption layer before embedding messages.
Improved Steganographic Techniques – Using adaptive LSB to distribute data more securely.
Support for Larger Messages – Enhancing capacity to store more data.
Graphical User Interface (GUI) – Developing a user-friendly interface.
Multi-Image Steganography – Distributing messages across multiple images for extra security.

Contributing-
If you'd like to contribute to this project:
Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit your changes (git commit -m "Added new feature").
Push to the branch (git push origin feature-name).
Open a pull request.

Contact
📧 Your Email: kunchumvaidhyaraj@gmail.com
🔗 GitHub: https://github.com/vkunchum
💼 LinkedIn: www.linkedin.com/in/vaidhyaraj-kunchum-07246b203

Acknowledgment
This project was developed as part of the Capstone Project on Secure Data Hiding in Images Using Steganography.


Thank you for using this project! 



