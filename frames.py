import customtkinter
import pandas as pd

from threading import Thread
from tkinter.filedialog import askopenfilename
from scraper import ScholarList, scrape_scholar

# Define frames - Singe Entry
class SingleEntry(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Single URL Entry", **kwargs):
        super().__init__(*args, **kwargs)

        def get_all():
            try:
                self.labelresult.configure(text='...loading...')
                self.labelresult.update_idletasks()
                url = str(self.entryinput.get())
                result = scrape_scholar(url)
            except:
                result = "Invalid URL, please try again!"
            self.labelresult.after(1000, lambda:self.labelresult.configure(text=result))

        self.header_name = header_name
        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10, pady=10)

        self.labelinput = customtkinter.CTkLabel(self, text = 'Input profile URL (https://scholar.google.com/citations?user=f-F4yywAAAAJ)')
        self.labelinput.grid(row=1, padx=10)

        self.labeltips = customtkinter.CTkLabel(self, text = 'Be sure the url ends with user code, remove \'&hl=en&oi=ao\' if any')
        self.labeltips.grid(row=2)

        self.entryinput = customtkinter.CTkEntry(self, width=400)
        self.entryinput.grid(row=3)

        self.labelblank = customtkinter.CTkLabel(self, text=' ')
        self.labelblank.grid(row=4)

        self.button = customtkinter.CTkButton(self, text='Run scraper', command=get_all)
        self.button.grid(row=5)

        self.labelresult = customtkinter.CTkLabel(self, text=' ')
        self.labelresult.grid(row=6, pady=5)

# Define frames - Input .txt
class InputFile(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="File Input", **kwargs):
        super().__init__(*args, **kwargs)

        def open_file():
            try:
                result = "Check text file"
                self.labelresult.configure(text='...loading...')
                self.labelresult.update_idletasks()
                file_path = askopenfilename(title='Open a file', initialdir='/', filetypes=[('Text Files', '*.txt')])
                data = pd.read_csv(file_path, sep=',', header=None)
                scholars = [(ScholarList(n=row[0], u=row[1])) for index, row in data.iterrows()]
                unit = float(1/len(scholars))
                count = 0
                threads = []

                for each in scholars:
                    res = Thread(target=scrape_scholar, args=(each.url,))
                    threads.append(res)
                    res.start()

                for each in threads:
                    each.join()
                    count += unit
                    self.progressbar.update_idletasks()
                    self.progressbar.set(count)
                
                result = "Done"
            except:
                result = "Error! Check last available file and compare against URL in text file!"

            self.labelresult.after(1000,lambda:self.labelresult.configure(text= result))

        self.header_name = header_name
        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, columnspan=2, padx=160, pady=10)

        self.button = customtkinter.CTkButton(self, text='Input file', command=open_file)
        self.button.grid(row=1, column=0)

        self.progressbar = customtkinter.CTkProgressBar(self)
        self.progressbar.set(0.0)
        self.progressbar.grid(row=1, column=1)

        self.labelresult = customtkinter.CTkLabel(self, text=' ')
        self.labelresult.grid(row=2, columnspan=2, pady=5)
