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

        self.titleFrame = None
        self.title = None

        
    def createButtons(self):
        self.gui.grid_rowconfigure((0, 1, 2), weight=1)
        self.gui.grid_columnconfigure((0, 1), weight=1)

        self.titleFrame = customtkinter.CTkFrame(master=self.gui)
        self.titleFrame.grid_rowconfigure(0, weight=1)
        self.titleFrame.grid_columnconfigure(1, weight=5)

        self.title = customtkinter.CTkLabel(master=self.titleFrame, text="Choose the type of media")

        self.bookButton = customtkinter.CTkButton(master=self.gui, text="Book", command=self.button_callback)
        self.gameButton = customtkinter.CTkButton(master=self.gui, text="Game", command=self.button_callback)
        self.seriesButton = customtkinter.CTkButton(master=self.gui, text="Series", command=self.button_callback)
        self.moviesButton = customtkinter.CTkButton(master=self.gui, text="Movie", command=self.button_callback)
        self.returnButton = customtkinter.CTkButton(master=self.titleFrame, command=self.button_callback) #ADD image later

        self.titleFrame.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")
        self.returnButton.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.title.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.bookButton.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.gameButton.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.seriesButton.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.moviesButton.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    def button_callback(self):
        pass