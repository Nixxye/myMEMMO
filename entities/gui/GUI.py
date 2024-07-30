import customtkinter

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.createFirstState()


    def createFirstState(self):
        self.clear_widgets()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.buttons = []
        self.buttons.append(customtkinter.CTkButton(master=self, text="Add", command=self.button_callbck))
        self.buttons.append(customtkinter.CTkButton(master=self, text="View", command=self.button_callbck))

        self.buttons[0].grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.buttons[1].grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        

    def button_callbck(self):
        print("button clicked")

if __name__ == "__main__":
    app = App()
    app.mainloop()