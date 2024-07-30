import customtkinter
from State import State

class Selection(State):
    def __init__(self, gui):
        super().__init__(gui)
        self.createAllWidgets()