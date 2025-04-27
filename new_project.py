import os
import shutil

template_path = "projects/template.html"

name = input("Enter the name of the new project: ")
folder_name = name.replace(" ", "_").lower()

try:
    os.mkdir(f"media/projects/{folder_name}")

except FileExistsError:
    input("delete folder y/n:")
    if input() == "y": 
        shutil.rmtree(f"projects/{folder_name}")
        os.mkdir(f"media/projects/{folder_name}")
    else:
        print("Using existing folder")

input(f"Enter when finished puttting images in the media/projects/{folder_name} folder")

# Create the HTML file
slide_index = "".join([f'\n                   <span class="dot" onclick="currentSlide({num})"></span>' 
                       for num in range(1, len(os.listdir(f"media/projects/{folder_name}")) + 1)])

slideshow = "".join([f'''
            <div class="slide">
                <img src="../media/projects/{folder_name}/{img}">
            </div>\n''' 
            for img in os.listdir(f"media/projects/{folder_name}")
        ])

file =f'''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="../Style.css">
        
        <title>Miekale Smith's Portfoilo</title>
    
        <div class="nav">
            <ol>
                <li><a href="../Home.html#home">HOME</a></li>
                <li><a href="../Home.html#projects">PROJECTS</a></li>
                <li><a href="../Home.html#connect">CONNECT</a></li>
            </ol>
        </div>

    </head>

    <body style="background-color: #2A2C36;">
        <div class="project-pages">
            <h1>{name}</h1>
            
            <div class="slideshow">

            {slideshow}

                <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
                <a class="next" onclick="plusSlides(1)">&#10095;</a>

                <div style="text-align:center">
                {slide_index}
                </div>
            </div>
            
            <div class="project-pages-main">
                <!-- Main Bullet points --> 
                <ul>
                    <li></li>
                    <li></li>
                </ul>   
                <!-- Description Paragraphs --> 
                <p>
                </p>
            </div>
            <div class="back-button">
                <a href="../Home.html#projects">BACK TO PROJECTS</a>
            </div>
            <script src="../scripts.js"></script>
        </div>
    </body>
</html>
'''

with open(f"projects/{folder_name}.html", "w") as f:
    f.write(file)
