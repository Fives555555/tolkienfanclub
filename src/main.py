import os
import shutil
from static_to_public import static_content_to_public_content

dir_path_public = "./public"
dir_path_static = "./static"

def setup_public(path):
    if os.path.exists(path):
        print("Deleting public directory")
        shutil.rmtree(path)
    print("Copying static files to public directory")
    os.mkdir(path)
    
def main():
    setup_public(dir_path_public)
    static_content_to_public_content(dir_path_static, dir_path_public)
    
main()