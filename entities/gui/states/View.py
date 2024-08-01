import customtkinter
import tkinter as tk
from states.State import State
from PIL import Image
import pandas as pd

CSV_FILE = "./entities/gui/states/data/data.csv"

class View(State):
    def __init__(self, gui):
        super().__init__(gui)
    
    def enter(self):
        self.gui.grid_rowconfigure((0, 1, 2), weight=1)
        self.createBoxes([])

    def createBoxes(self, rules):
        df = pd.read_csv(CSV_FILE)
        # print(df.columns)
        if rules==[]:
            for index in range(df.shape[0]):
                self.createBox(df, index, index % 3, index // 3)

    def createBox(self, df, index, i, j):
        box = customtkinter.CTkFrame(master=self.gui)
        box.grid(row=j, column=i, padx=20, pady=20, sticky="nsew")
        # label = customtkinter.CTkLabel(master=box, text=row["Name"])
        # label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        image = Image.open(df.at[index, "ImagePath"])
        w, h = image.size
        cropedImage = image.crop((0, 0, w, 3 * w))
        # image = tk.PhotoImage(file=df.at[index, "ImagePath"])
        image = customtkinter.CTkImage(cropedImage, size=(400, 1200))
        imageLabel = customtkinter.CTkLabel(master=box, image=image, text=df.at[index, "Name"])
        imageLabel.pack(padx=20, pady=20)

        return box
