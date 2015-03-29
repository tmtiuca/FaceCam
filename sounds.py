from Tkinter import *
from tkSnack import *

root = Tk()

tkSnack.initializeSnack(root)

snd = Sound() 
snd.read('allen_arrogh.wav')   
snd.play()
root.mainloop()   