
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def encode_lsb(image_path, secret_message, output_path):
    try:
        img = Image.open(image_path).convert('RGBA')
        width, height = img.size
        secret_message += '\0'
        data = ''.join(format(ord(char), '08b') for char in secret_message)
        data_len = len(data)
        if data_len > width * height * 3:
            raise ValueError("Message too large to encode in this image.")
        img_data = list(img.getdata())
        data_index = 0
        for i in range(height):
            for j in range(width):
                if data_index < data_len:
                    r, g, b, a = img_data[i * width + j]
                    if data_index < data_len:
                        r = (r & ~1) | int(data[data_index])
                        data_index += 1
                    if data_index < data_len:
                        g = (g & ~1) | int(data[data_index])
                        data_index += 1
                    if data_index < data_len:
                        b = (b & ~1) | int(data[data_index])
                        data_index += 1
                    img_data[i * width + j] = (r, g, b, a)
        img.putdata(img_data)
        img.save(output_path)
        return True, "Encoding successful!"
    except FileNotFoundError:
        return False, "Image file not found."
    except ValueError as e:
        return False, str(e)
    except Exception as e:
        return False, f"An error occurred: {e}"

def browse_image(entry_widget):
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if filepath:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, filepath)

def browse_output(entry_widget):
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filepath:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, filepath)

def encode_button_click():
    image_path = image_entry.get()
    secret_message = message_entry.get("1.0", tk.END).strip()
    output_path = output_entry.get()
    success, message = encode_lsb(image_path, secret_message, output_path)
    result_label.config(text=message)

root = tk.Tk()
root.title("LSB Encryption")
encode_frame = tk.Frame(root)
encode_frame.pack(padx=10, pady=10)
tk.Label(encode_frame, text="Image:").grid(row=0, column=0, sticky="w")
image_entry = tk.Entry(encode_frame, width=50)
image_entry.grid(row=0, column=1)
tk.Button(encode_frame, text="Browse", command=lambda: browse_image(image_entry)).grid(row=0, column=2)
tk.Label(encode_frame, text="Message:").grid(row=1, column=0, sticky="w")
message_entry = tk.Text(encode_frame, width=40, height=5)
message_entry.grid(row=1, column=1)
tk.Label(encode_frame, text="Output:").grid(row=2, column=0, sticky="w")
output_entry = tk.Entry(encode_frame, width=50)
output_entry.grid(row=2, column=1)
tk.Button(encode_frame, text="Browse", command=lambda: browse_output(output_entry)).grid(row=2, column=2)
encode_button = tk.Button(encode_frame, text="Encode", command=encode_button_click)
encode_button.grid(row=3, column=1, pady=10)
result_label = tk.Label(encode_frame, text="")
result_label.grid(row=4, column=1)
root.mainloop()