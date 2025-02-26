import cv2

def decrypt_message(image_filename="encryptedImage.png"):
    img = cv2.imread(image_filename)

    if img is None:
        print(f"Error: Unable to load '{image_filename}'. Make sure the file exists.")
        return

    entered_password = input("Enter passcode for Decryption: ")

    c = {i: chr(i) for i in range(256)}  # ASCII decoding dictionary

    # Retrieve stored message length (ensuring it stays within uint8 limits)
    message_length = img[0, 0, 0]

    n, m, z = 0, 1, 0  
    decrypted_message = ""

    for _ in range(message_length):
        decrypted_message += c.get(img[n, m, z], "?")  # Avoid errors on invalid pixels
        z = (z + 1) % 3  
        if z == 0:
            m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1

    # Debugging: Print extracted message to check its format
    print(f"Extracted message from image: {decrypted_message}")

    if "|" not in decrypted_message:
        print("Error: Decryption failed. Message format is incorrect.")
        return

    stored_password, actual_message = decrypted_message.split("|", 1)

    if stored_password == entered_password:
        print("Decryption successful!")
        print("Decrypted Message:", actual_message)
    else:
        print("Incorrect passcode! Access denied.")

if __name__ == "__main__":
    decrypt_message()
