# decryption_gui.py
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def decode_lsb(image_path):
    try:
        img = Image.open(image_path).convert('RGBA')
        img_data = list(img.getdata())
        binary_data = ""
        for r, g, b, a in img_data:
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
        all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
        decoded_message = ""
        for byte in all_bytes:
            try:
                char = chr(int(byte, 2))
                if char == '\0':
                    break
                decoded_message += char
            except ValueError:
                break
        return True, decoded_message
    except FileNotFoundError:
        return False, "Image file not found."
    except Exception as e:
        return False, f"An error occurred: {e}"

def browse_image(entry_widget):
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if filepath:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, filepath)

def decode_button_click():
    image_path = decode_image_entry.get()
    success, message = decode_lsb(image_path)
    result_decode_label.config(text=message)

root = tk.Tk()
root.title("LSB Decryption")
decode_frame = tk.Frame(root)
decode_frame.pack(padx=10, pady=10)
tk.Label(decode_frame, text="Image:").grid(row=0, column=0, sticky="w")
decode_image_entry = tk.Entry(decode_frame, width=50)
decode_image_entry.grid(row=0, column=1)
tk.Button(decode_frame, text="Browse", command=lambda: browse_image(decode_image_entry)).grid(row=0, column=2)
decode_button = tk.Button(decode_frame, text="Decode", command=decode_button_click)
decode_button.grid(row=1, column=1, pady=10)
result_decode_label = tk.Label(decode_frame, text="")
result_decode_label.grid(row=2, column=1)
root.mainloop()