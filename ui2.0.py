import os, sys
import customtkinter

from frames import SingleEntry, InputFile

# Icon pathing
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ico = resource_path(".\icons8.com\google-scholar-white.ico")

# Quitter
def _quit():
    window.quit()
    window.destroy()

# Define customtkinter variable
window = customtkinter.CTk()
window.protocol('WM_DELETE_WINDOW', _quit)
window.title('Google scholar profile scraper')
window.resizable(width=False, height=False)
window.geometry('480x375')
window.iconbitmap(ico)

# Set custom tkinter aperaances
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

single_entry_frame = SingleEntry(border_width=1, border_color='#608BD5')
single_entry_frame.grid(row=0, column=0, padx=10, pady=10)

file_entry_frame = InputFile(border_width=1, border_color='#608BD5')
file_entry_frame.grid(row=1, column=0, padx=10, pady=0)

window.mainloop()