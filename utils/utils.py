import customtkinter

def createFrameTitle(master, title, corner_radius=6, fg_color="gray30"):
    titleFrame = customtkinter.CTkFrame(master=master)
    titleFrame.grid_rowconfigure(0, weight=1)
    titleFrame.grid_columnconfigure(1, weight=5)

    title = customtkinter.CTkLabel(master=titleFrame, text=title, corner_radius=corner_radius, fg_color=fg_color)
    return titleFrame