from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1280x720")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("ironman.jpg")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("ironman.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1280,720))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(2)
    root.destroy()

play_gif()
root.mainloop()
