import os
import shutil
import sys

def transfer_files(src_dir, dest_dir, file_types):
    if not os.path.exists(src_dir):
        print(f"{src_dir} path does not exist. Aborted program.")
        sys.exit()

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(src_dir):
        if filename.endswith(tuple(file_types)):
            src_path = os.path.join(src_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.copy(src_path, dest_path)
            print(f"Transferred {filename} to {dest_dir}")
