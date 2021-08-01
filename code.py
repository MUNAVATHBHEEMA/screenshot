import pyautogui
import tkinter as tk      #intermodule
from tkinter.filedialog import*

# design ui sreenshot taker screen
root = tk.Tk()
#now i have creat window for screenshot taker
canvas1=tk.Canvas(root, width=300, height=300,)
canvas1.pack()
#creat command function, this function can take screenshot and save our desire files in laptop
def takeScreenshot():
   myscreenshot = pyautogui.screenshot()
   save_path = asksaveasfilename()
   myscreenshot.save(save_path+"_screenshot.png")

#now here i creat button
MYBUTTON= tk.Button(text="take screenshot", command=takeScreenshot, font=10)
canvas1.create_window(150,150,window=MYBUTTON)

#now we have to creat main loop here

mainloop()
