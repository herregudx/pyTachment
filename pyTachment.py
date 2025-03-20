import os
import email
from email import policy
from email.parser import BytesParser
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_attachments(eml_file, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Open and parse
    with open(eml_file, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    # Iterate email parts
    for part in msg.iter_attachments():
        filename = part.get_filename()
        if filename:
            filepath = os.path.join(output_folder, filename)
            with open(filepath, 'wb') as attachment_file:
                attachment_file.write(part.get_payload(decode=True))
            print(f"Saved attachment: {filename}")
    messagebox.showinfo("Success", f"Attachments saved to {output_folder}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Email Files", "*.eml")])
    if file_path:
        output_folder = file_path[:-4] + "_attachments"
        extract_attachments(file_path, output_folder)

def main():
    root = tk.Tk()
    root.withdraw()
    select_file()

if __name__ == "__main__":
    main()
