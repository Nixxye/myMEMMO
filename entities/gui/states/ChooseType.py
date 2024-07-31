import customtkinter
from states.State import State

class ChooseType(State):
    def __init__(self, gui):
        super().__init__(gui)
        self.bookButton = None
        self.gameButton = None
        self.seriesButton = None
        self.moviesButton = None
        self.returnButton = None

        self.headerFrame = None
        self.title = None

        
    def enter(self):
        self.gui.grid_rowconfigure((0, 1, 2), weight=1)
        self.gui.grid_columnconfigure((0, 1), weight=1)

        self.headerFrame = customtkinter.CTkFrame(master=self.gui)
        self.headerFrame.grid_rowconfigure(0, weight=1)
        self.headerFrame.grid_columnconfigure(1, weight=5)

        self.title = customtkinter.CTkLabel(master=self.headerFrame, text="Choose the type of media")

        self.bookButton = customtkinter.CTkButton(master=self.gui, text="Book", command=lambda: self.button_callback("Book"))
        self.gameButton = customtkinter.CTkButton(master=self.gui, text="Game", command=lambda: self.button_callback("Game"))
        self.seriesButton = customtkinter.CTkButton(master=self.gui, text="Series", command=lambda: self.button_callback("Series"))
        self.moviesButton = customtkinter.CTkButton(master=self.gui, text="Movie", command=lambda: self.button_callback("Movie"))
        self.returnButton = customtkinter.CTkButton(master=self.headerFrame, command=self.returnState) #ADD image later

        self.headerFrame.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")
        self.returnButton.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.title.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.bookButton.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.gameButton.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.seriesButton.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.moviesButton.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    def button_callback(self, type):
        self.gui.setState(self.gui.add, type=type)

    def returnState(self):
        self.gui.setState(self.gui.selection)
