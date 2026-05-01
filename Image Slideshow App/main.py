import tkinter as tk
import time
from PIL import Image, ImageTk

# Main Application Window

root = tk.Tk()
root.title("Image Slideshow")
root.geometry("1080x1920")

# List of image path

imagePaths = [
    r"C:\Users\nanda\Documents\GitHub\Learning Python\Image Slideshow App\Image\image1.jpg",
    r"C:\Users\nanda\Documents\GitHub\Learning Python\Image Slideshow App\Image\image2.jpg",
    r"C:\Users\nanda\Documents\GitHub\Learning Python\Image Slideshow App\Image\image3.jpg",
    r"C:\Users\nanda\Documents\GitHub\Learning Python\Image Slideshow App\Image\image4.jpg",
    r"C:\Users\nanda\Documents\GitHub\Learning Python\Image Slideshow App\Image\image5.jpg",
    r"C:\Users\nanda\Documents\GitHub\Learning Python\Image Slideshow App\Image\image6.jpg",
    r"C:\Users\nanda\Documents\GitHub\Learning Python\Image Slideshow App\Image\image7.jpg",
]

imageSize = (1080, 1920)

images = []

for path in imagePaths:
    img = Image.open(path)
    img = img.resize(imageSize)
    images.append(img)

# Convert PIL images into Tkinter-compatible images

finalImages = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    finalImages.append(photo)

# Label widget to display the images

imageLabel = tk.Label(root)
imageLabel.pack(pady=30)

# SlideShow function

def slideShow():
    for img in finalImages:
        imageLabel.config(image=img)
        imageLabel.image = img
        root.update()
        time.sleep(2)

# Button to start the slideshow

playButton = tk.Button(
    root,
    text="Play Slideshow",
    font=("Arial", 20),
    command=slideShow
)

playButton.pack(pady=40)
root.mainloop()