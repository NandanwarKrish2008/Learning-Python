import tkinter as tk
import time
from PIL import Image, ImageTk

# Main Application Window

root = tk.Tk()
root.title("Image Slideshow")
root.geometry("1080x1920")

# List of image path

image = [
    r"C:\Users\Dell\Desktop\Slideshow\image1.jpg",
    r"C:\Users\Dell\Desktop\Slideshow\image2.jpg",
    r"C:\Users\Dell\Desktop\Slideshow\image3.jpg",
    r"C:\Users\Dell\Desktop\Slideshow\image4.jpg",
    r"C:\Users\Dell\Desktop\Slideshow\image5.jpg",
    r"C:\Users\Dell\Desktop\Slideshow\image6.jpg",
    r"C:\Users\Dell\Desktop\Slideshow\image7.jpg",
]