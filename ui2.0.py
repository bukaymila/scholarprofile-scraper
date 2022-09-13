import os, sys
import customtkinter

from frames import SingleEntry, InputFile, HelpSingleEntry, HelpFileEntry

# Icon pathing
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ico = resource_path(r".\files\google-scholar-white.ico")
file = resource_path(r".\files\test.txt")

# Quitter
def _quit():
    window.quit()
    window.destroy()

# Define customtkinter variable
window = customtkinter.CTk()
window.protocol('WM_DELETE_WINDOW', _quit)
window.title('Google scholar profile scraper')
window.resizable(width=False, height=False)
window.geometry('480x405')
window.iconbitmap(ico)

# Set custom tkinter aperaances
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

def help_me():
    window1 = customtkinter.CTkToplevel()
    window1.geometry('480x400')
    window1.title('Help')
    window1.resizable(width=False, height=False)
    window.iconbitmap(ico)

    def open_file():
        os.startfile(file)

    single_help = HelpSingleEntry(window1)#, border_width=1, border_color='#608BD5')
    single_help.grid(row=0, padx=10, pady=5)

    file_help = HelpFileEntry(window1)#, border_width=1, border_color='#608BD5')
    file_help.grid(row=1, padx=10, pady=5)

    file_button = customtkinter.CTkButton(window1, text='Sample file', command=open_file)
    file_button.grid(row=2, padx=(10, 330), pady=5)


help_button = customtkinter.CTkButton(text='Help', width=50, command=help_me)
help_button.grid(row=0, column=0, padx=(10,418), pady=(10,5))

single_entry_frame = SingleEntry(border_width=1, border_color='#608BD5')
single_entry_frame.grid(row=1, padx=10, pady=5)

file_entry_frame = InputFile(border_width=1, border_color='#608BD5')
file_entry_frame.grid(row=2, padx=10, pady=5)

window.mainloop()