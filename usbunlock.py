import wmi
c = wmi.WMI()
import tkinter as tk
from PIL import Image, ImageTk

# declare the window
window = tk.Tk()
# set window title
window.title("LOCKED")
# set window width and height
window.wm_attributes("-fullscreen", True)
image1 = Image.open("C:/Users/mauro_dxyjf6e/OneDrive - Prizma/Afbeeldingen/Schermafbeelding 2022-02-06 104525.png")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test
label1.place(x=-2, y=-2)
def task():
    try:
        if(c.Win32_PhysicalMedia()[1].SerialNumber.find("F") != -1):
            window.destroy()
    except:
        print("Fout! MWAHAHAHAHA Groetjes, de hekkers")
    window.after(1000, task)

window.after(1000, task)
window.mainloop()