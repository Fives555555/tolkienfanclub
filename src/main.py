import os
import sys
import shutil
from static_to_public import static_content_to_public_content
from generate_page import generate_pages_recursive

if len(sys.argv) < 2:
    basepath = "/"
else:
    basepath = sys.argv[1]

dir_path_public = "./docs"
dir_path_static = "./static"
dir_path_content = "./content"
template_path = "./template.html"

def setup_public(path):
    if os.path.exists(path):
        print("Deleting public directory")
        shutil.rmtree(path)
    print("Copying static files to public directory")
    os.mkdir(path)
    
def main():
    setup_public(dir_path_public)
    static_content_to_public_content(dir_path_static, dir_path_public)
    print("Generating content")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)
    
if __name__ == "__main__":
    main()