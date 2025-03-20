import os
import email
from email import policy
from email.parser import BytesParser

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

if __name__ == "__main__":
    eml_file = input("Filename: ")
    output_folder = eml_file[:-4] + "_attachments"
    extract_attachments(eml_file, output_folder)
