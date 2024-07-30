import customtkinter
from states.Selection import Selection
from states.ChooseType import ChooseType

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.selection = Selection(self)
        self.chooseType = ChooseType(self)

        self.setState(self.selection)
    
    def setState(self, state):
        if self.state is not None:
            self.clearWidgets()
            state.enter()

    def clearWidgets(self):
        for widget in self.winfo_children():
            widget.grid_forget()
        print("Cleared widgets")




if __name__ == "__main__":
    app = GUI()
    app.mainloop()