import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

EXTENSIONS = {
    "WebP": ".webp",
    "GIF": ".gif",
    "JPEG": ".jpg",
    "PNG": ".png",
    "BMP": ".bmp",
    "TIFF": ".tiff",
    "MP4": ".mp4",
}

def convert_files(input_folder, output_folder, input_format, output_format):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)

    for file in files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + EXTENSIONS[output_format])

        if file.lower().endswith(EXTENSIONS[input_format]):
            if input_format == "MP4":
                os.system(f"ffmpeg -i \"{input_path}\" \"{output_path}\"")
                print(f"{file} convertido para {output_format}")
            else:
                img = Image.open(input_path)
                img.save(output_path, output_format)

                print(f"{file} convertido para {output_format}")

def select_input_folder():
    folder_selected = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, folder_selected)

def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_selected)

def start_conversion():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    input_format = input_format_combobox.get()
    output_format = output_format_combobox.get()
    convert_files(input_folder, output_folder, input_format, output_format)
    status_label.config(text="Conversão concluída!")

root = tk.Tk()
root.title("Conversor de Arquivos")
root.geometry("500x215")

input_label = tk.Label(root, text="Pasta de entrada:")
input_label.grid(row=0, column=0, sticky="w")

input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1, padx=5, pady=5)

input_button = tk.Button(root, text="Selecionar", command=select_input_folder)
input_button.grid(row=0, column=2, padx=5, pady=5)

output_label = tk.Label(root, text="Pasta de saída:")
output_label.grid(row=1, column=0, sticky="w")

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=5, pady=5)

output_button = tk.Button(root, text="Selecionar", command=select_output_folder)
output_button.grid(row=1, column=2, padx=5, pady=5)

input_format_label = tk.Label(root, text="Formato de entrada:")
input_format_label.grid(row=2, column=0, sticky="w")

input_format_combobox = ttk.Combobox(root, values=list(EXTENSIONS.keys()), state="readonly")
input_format_combobox.grid(row=2, column=1, padx=5, pady=5)
input_format_combobox.current(0)

output_format_label = tk.Label(root, text="Formato de saída:")
output_format_label.grid(row=3, column=0, sticky="w")

output_format_combobox = ttk.Combobox(root, values=list(EXTENSIONS.keys()), state="readonly")
output_format_combobox.grid(row=3, column=1, padx=5, pady=5)
output_format_combobox.current(1)

convert_button = tk.Button(root, text="Converter", command=start_conversion)
convert_button.grid(row=4, columnspan=3, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=5, columnspan=3, pady=(0, 10))

root.mainloop()