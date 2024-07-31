import customtkinter
from states.State import State

class Selection(State):
    def __init__(self, gui):
        super().__init__(gui)
        self.viewButton = None
        self.addButton = None
        
    def enter(self):
        self.gui.grid_rowconfigure(0, weight=1)
        self.gui.grid_columnconfigure((0, 1), weight=1)

        self.addButton = customtkinter.CTkButton(master=self.gui, text="Add", command=self.add)
        self.viewButton = customtkinter.CTkButton(master=self.gui, text="View", command=self.view)

        self.addButton.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.viewButton.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    def add(self):
        self.gui.setState(self.gui.chooseType)
    
    def view(self):
        pass