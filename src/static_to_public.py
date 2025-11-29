import os
import shutil

def static_content_to_public_content(source_path, destination_path):
    items = os.listdir(source_path)
    for item in items:
        full_path = os.path.join(source_path, item)
        new_destination_path = os.path.join(destination_path, item)
        if os.path.isdir(full_path):
            if not os.path.exists(new_destination_path):
                os.mkdir(new_destination_path)
            static_content_to_public_content(full_path, new_destination_path)
        elif os.path.isfile(full_path):
            shutil.copy(full_path, new_destination_path)
            print(f"From {full_path} to {new_destination_path}")