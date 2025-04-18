import os
import shutil

template_path = "projects/template.html"

name = input("Enter the name of the new project: ")

os.mkdir(f"media/{name}")
shutil.copy(template_path,f"projects/{name}.html")
