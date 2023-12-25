import os
import shutil

def create_clean_working_dir(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
            
    os.mkdir(dir_name)