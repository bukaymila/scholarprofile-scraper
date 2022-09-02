import customtkinter
import time
from tkinter import *
from scraper import main


# Set custom tkinter aperaances
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Quitter
def _quit():
    window.quit()
    window.destroy()

# Define customtkinter variable
window = customtkinter.CTk()
window.protocol('WM_DELETE_WINDOW', _quit)
window.title('Google scholar profile scraper')
window.resizable(width=False, height=False)
window.geometry('470x185')
#window.iconbitmap('')

# Define inputs
def get_all():
    labelresult.configure(text='...loading')
    url = str(entryinput.get())
    result = main(url)
    labelresult.after(1000,lambda:labelresult.configure(text= result))

# Frame for elements in the window
frm_form = customtkinter.CTkFrame(pady=10)
frm_form.pack()

labelinput = customtkinter.CTkLabel(master=frm_form, text = 'Input profile URL (https://scholar.google.com/citations?user=f-F4yywAAAAJ)')
labelinput.grid(row=0)

labeltips = customtkinter.CTkLabel(master=frm_form, text = 'Be sure the url ends with user code, remove \'&hl=en&oi=ao\' if any')
labeltips.grid(row=1)

entryinput = customtkinter.CTkEntry(master=frm_form, width=450)
entryinput.grid(row=2)

labelblank = customtkinter.CTkLabel(master=frm_form, text=' ')
labelblank.grid(row=3)

button = customtkinter.CTkButton(master=frm_form, text='Run scraper', command=get_all)
button.grid(row=4)

labelresult = customtkinter.CTkLabel(master=frm_form, text=' ')
labelresult.grid(row=5)

window.mainloop()