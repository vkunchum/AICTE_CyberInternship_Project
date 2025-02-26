import cv2
import os

def encrypt_message(image_filename="flower.jpg", output_filename="encryptedImage.png"):
    img = cv2.imread(image_filename)

    if img is None:
        print(f"Error: Unable to load '{image_filename}'. Make sure the file exists.")
        return

    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    full_message = password + "|" + message  # Store password + separator + message
    message_length = len(full_message)

    d = {chr(i): i for i in range(256)}  # ASCII encoding dictionary

    if message_length > 255:
        print("Error: Message too long! Must be less than 255 characters.")
        return

    # Store message length in a fixed pixel
    img[0, 0, 0] = message_length  

    n, m, z = 0, 1, 0  # Start at (0,1) to prevent overwriting length

    for char in full_message:
        img[n, m, z] = d[char]  # Store ASCII values
        z = (z + 1) % 3  # Move to next channel
        if z == 0:
            m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1
        if n >= img.shape[0]:  
            print("Error: Message too long for this image!")
            return

    cv2.imwrite(output_filename, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Save without compression
    print(f"Encryption successful! Encrypted image saved as '{output_filename}'.")

    os.system(f"start {output_filename}")  # Auto-open for Windows

if __name__ == "__main__":
    encrypt_message()
