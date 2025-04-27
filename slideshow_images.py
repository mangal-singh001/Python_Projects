from itertools import cycle 
from PIL import Image, ImageTk
import time
import tkinter as tk 

root = tk.Tk()
root.title("Image Slideshow Viewer")

#  List of Image Path 

image_paths = [
   r'E:\DISHU\Dev\IMG_20240213_202520_075.jpg',
   r'E:\DISHU\Dev\IMG_20240221_121919_935.jpg',
   r'E:\DISHU\Dev\IMG_20240413_101731_390.jpg',
   r'E:\DISHU\Dev\IMG_20240418_100553_151.jpg'
]


#  Resize the imaged to 1080x1080

image_size = (1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photos_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()


def update_image():
    for photo_image in photos_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)
        
slideshow = cycle(photos_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()
        
play_button = tk.Button(root,text='Play Slideshow',command=start_slideshow)
play_button.pack()

root.mainloop()