import os
from block_markdown import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    dirpath = os.path.dirname(dest_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(full_html)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)
    for item in items:
        path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isdir(path):
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(path, template_path, dest_path)
        elif os.path.isfile(path) and item.endswith(".md"):
            dest_file_path = dest_path.replace(".md", ".html")
            os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
            generate_page(path, template_path, dest_file_path)
            