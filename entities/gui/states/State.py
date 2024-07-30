class State:
    def __init__(self, app):
        self.app = app
    
    def createButtons(self):
        pass

    def enter(self):
        # Create all the widgets
        self.createButtons()