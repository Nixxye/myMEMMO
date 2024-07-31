import customtkinter
import json
from states.State import State

CATEGORIES_FILE = "./entities/gui/states/data/categories.json"

class Add(State):
    def __init__(self, gui):
        super().__init__(gui)
        self.viewButton = None
        self.addButton = None
        
    def enter(self, type):
        #FRAMES:
        self.mainFrame = customtkinter.CTkScrollableFrame(master=self.gui) #Scrollable frame
        self.titleFrame = createFrameTitle(master=self.mainFrame, title=type+" Title")
        self.categoryFrame = createFrameTitle(master=self.mainFrame, title="Categories")
        self.scoreFrame = createFrameTitle(master=self.mainFrame, title="Score")
        self.dateFrame = createFrameTitle(master=self.mainFrame, title="Date")
        self.textFrame = createFrameTitle(master=self.mainFrame, title="Review")

        #GRID CONFIGURATION:
        self.gui.grid_rowconfigure(0, weight=1)
        self.gui.grid_columnconfigure(0, weight=1)

        self.mainFrame.grid(row=0, column=0, columnspan=2, rowspan=2, padx=20, pady=20, sticky="nsew")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        
        self.titleFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.categoryFrame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.scoreFrame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.dateFrame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        self.textFrame.grid(row=4, column=0, padx=20, pady=20, sticky="nsew")

        self.addCategories(type)

    def add(self):
        self.gui.setState(self.gui.chooseType)
    
    def addCategories(self, type):
        try:
            with open(CATEGORIES_FILE, "r") as file:
                data = json.load(file)

                index = 1
                for categorie in data[type]:
                    checkbox = customtkinter.CTkCheckBox(self.categoryFrame, text=categorie)
                    checkbox.grid(row=index, column=0, padx=20, pady=20, sticky="nsew")

                    removeButton = customtkinter.CTkButton(self.categoryFrame, text="Remove", command=lambda c=categorie, t=type: self.removeCategory(c, t))
                    removeButton.grid(row=index, column=1, padx=20, pady=20, sticky="nsew")
                    index += 1
                
                entry = customtkinter.CTkEntry(self.categoryFrame, placeholder_text	="Add new category")
                entry.grid(row=index, column=0, padx=20, pady=20, sticky="nsew")
                submitButton = customtkinter.CTkButton(self.categoryFrame, text="Add", command=lambda: self.addCategory(entry.get(), type))
                submitButton.grid(row=index, column=1, padx=20, pady=20, sticky="nsew")

        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def addCategory(self, category, type):
        try:
            with open(CATEGORIES_FILE, "r") as file:
                data = json.load(file)
                if type in data:
                    data[type].append(category)
                    with open(CATEGORIES_FILE, "w") as file:
                        json.dump(data, file, indent=4)
                        # print(f"Categoria {category} adicionada com sucesso.")
                        for widget in self.categoryFrame.winfo_children():
                            widget.destroy()
            self.addCategories(type)
            
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def removeCategory(self, category, type):
        try:
            with open(CATEGORIES_FILE, "r") as file:
                data = json.load(file)
                if type in data:
                    if category in data[type]:
                        data[type].remove(category)
                        with open(CATEGORIES_FILE, "w") as file:
                            json.dump(data, file, indent=4)
                            # print(f"Categoria {category} removida com sucesso.")
                            for widget in self.categoryFrame.winfo_children():
                                widget.destroy()
            self.addCategories(type)
            
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    def view(self):
        pass

def createFrameTitle(master, title, corner_radius=6, fg_color="gray30"):
    titleFrame = customtkinter.CTkFrame(master=master)
    titleFrame.grid_rowconfigure(0, weight=1)
    titleFrame.grid_columnconfigure(0, weight=1)

    title = customtkinter.CTkLabel(master=titleFrame, text=title, corner_radius=corner_radius, fg_color=fg_color)
    title.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    return titleFrame