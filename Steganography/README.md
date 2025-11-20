## LSB Steganography Tool

This repository contains a simple Python-based tool for hiding and revealing secret messages within images using Least Significant Bit (LSB) steganography. It provides a graphical user interface (GUI) for ease of use.

### Description

LSB steganography is a technique that conceals information by modifying the least significant bits of an image's pixel data. Since these changes are subtle, they are usually imperceptible to the human eye. This tool allows users to:

* **Encode:** Hide text messages inside PNG, JPG, JPEG, and BMP images.
* **Decode:** Extract hidden messages from encoded images.

The tool is implemented using Python's `tkinter` for the GUI and the `Pillow` (PIL) library for image processing.

### Features

* User-friendly graphical interface.
* Supports common image formats (PNG, JPG, JPEG, BMP).
* Simple encoding and decoding processes.
* Null character termination to improve decoded message accuracy.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

2.  **Install the required libraries:**

    ```bash
    pip install Pillow
    ```

3.  **Run the application:**

    * To encrypt an image, run `python encrypt.py`.
    * To decrypt an image, run `python decrypt.py`.

### Usage

**Encryption:**

1.  Launch the encryption GUI (`python encrypt.py`).
2.  Click "Browse" to select the image you want to use.
3.  Enter the secret message in the "Message" text box.
4.  Click "Browse" to choose the output file name and location.
5.  Click "Encode."
6.  <img width="687" alt="Screenshot 2025-02-20 at 13 29 25" src="https://github.com/user-attachments/assets/19fd6bd3-1f25-4fe4-87a9-7b69ffd03216" />


**Decryption:**

1.  Launch the decryption GUI (`python decrypt.py`).
2.  Click "Browse" to select the encoded image.
3.  Click "Decode."
4.  The hidden message will be displayed in the result label.
5.  <img width="687" alt="Screenshot 2025-02-20 at 13 27 58" src="https://github.com/user-attachments/assets/d6efc0d7-6c3e-41b0-b3de-026aa2260c21" />


### Notes

* The size of the message you can encode depends on the size of the image.
* For text messages, null character termination is used to ensure accurate decoding.
* For binary data, message length encoding is recommended.
* This is a simple tool for educational purposes. For production use, consider more robust steganography libraries.

### Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug fixes, feature requests, or improvements.

