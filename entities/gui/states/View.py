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
        self.gui.grid_rowconfigure((0, 1), weight=1)
        self.gui.grid_columnconfigure((0, 1), weight=1)
        self.gui.grid_columnconfigure(1, weight=5)

        self.headerFrame = customtkinter.CTkFrame(master=self.gui)
        self.headerFrame.grid_rowconfigure(0, weight=1)
        self.headerFrame.grid_columnconfigure(1, weight=5)

        self.returnButton = customtkinter.CTkButton(master=self.headerFrame, command=self.returnState) #ADD image later
        self.title = customtkinter.CTkLabel(master=self.headerFrame, text="View")

        self.headerFrame.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")
        self.returnButton.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.title.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.mainFrame = customtkinter.CTkScrollableFrame(master=self.gui)
        self.mainFrame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.mainFrame.grid_columnconfigure((0, 1, 2), weight=1)
        self.mainFrame.grid_rowconfigure((0, 1, 2), weight=1)
        self.createBoxes([])

    def createBoxes(self, rules):
        df = pd.read_csv(CSV_FILE)
        # print(df.columns)
        if rules==[]:
            for index in range(df.shape[0]):
                self.createBox(df, index, index % 3, index // 3)

    def createBox(self, df, index, i, j):
        box = customtkinter.CTkButton(master=self.mainFrame, text=df.at[index, "Name"], command=self.buttonCommand, height=400)
        box.grid(row=j, column=i, padx=20, pady=20, sticky="nsew")

        originalText = df.at[index, "Name"]
        hoverText = str(df.at[index, "Score"]) + "\n\n" + str(df.at[index, "Type"]) + "\n\n" + str(df.at[index, "Date"])

        box.bind("<Enter>", lambda event, bt=box, ht=hoverText: self.showInfo(bt, ht))
        box.bind("<Leave>", lambda event, bt=box, ot=originalText: self.hideInfo(bt, ot))

        return box
    
    def buttonCommand(self):
        pass

    def showInfo(self, button, hoverText):
        button.configure(text=hoverText)

    def hideInfo(self, button, originalText):
        button.configure(text=originalText)

    def returnState(self):
        self.gui.setState(self.gui.add, type="Game")
