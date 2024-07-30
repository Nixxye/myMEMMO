class State:
    def __init__(self, gui):
        self.gui = gui

    def createButtons(self):
        pass

    def createCheckboxes(self):
        pass

    def enter(self):
        # Create all the widgets
        self.createButtons()
        self.createCheckboxes()