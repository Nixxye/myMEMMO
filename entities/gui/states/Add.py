import customtkinter
from tkinter import filedialog
import json
import csv
import re
from states.State import State

CATEGORIES_FILE = "./entities/gui/states/data/categories.json"
CSV_FILE = "./entities/gui/states/data/data.csv"

class Add(State):
    def __init__(self, gui):
        super().__init__(gui)
        self.viewButton = None
        self.addButton = None
        self.checkboxes = []
        self.type = ""
        
    def enter(self, type):
        self.type = type
        self.gui.grid_rowconfigure(0, weight=1)
        self.gui.grid_columnconfigure(0, weight=1)
        #FRAMES:
        self.mainFrame = customtkinter.CTkScrollableFrame(master=self.gui)
        self.mainFrame.grid(row=1, column=0, columnspan=2, rowspan=2, padx=20, pady=20, sticky="nsew")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)

        self.headerFrame = customtkinter.CTkFrame(master=self.gui)
        self.returnButton = customtkinter.CTkButton(master=self.headerFrame, command=self.returnState) #ADD image later
        self.title = customtkinter.CTkLabel(master=self.headerFrame, text="Description")
        self.headerFrame.grid(row=0, column=0,columnspan=2, padx=20, pady=20, sticky="nsew")
        self.returnButton.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.title.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.titleFrame = createFrameTitle(master=self.mainFrame, title=type+" Title")
        self.titleEntry = customtkinter.CTkEntry(self.titleFrame, placeholder_text	="Lord of the Rings")
        self.titleFrame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.titleEntry.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.categoryFrame = createFrameTitle(master=self.mainFrame, title="Categories")
        self.categoryFrame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        self.scoreFrame = createFrameTitle(master=self.mainFrame, title="Score")
        self.scoreEntry = customtkinter.CTkEntry(self.scoreFrame, placeholder_text="0-100")
        self.scoreFrame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        self.scoreEntry.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.dateFrame = createFrameTitle(master=self.mainFrame, title="Date")
        self.dateEntry = customtkinter.CTkEntry(self.dateFrame, placeholder_text="MM/YYYY")
        self.dateFrame.grid(row=4, column=0, padx=20, pady=20, sticky="nsew")
        self.dateEntry.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.textFrame = createFrameTitle(master=self.mainFrame, title="Review")
        self.reviewTextbox = customtkinter.CTkTextbox(self.textFrame)
        self.textFrame.grid(row=5, column=0, padx=20, pady=20, sticky="nsew")
        self.reviewTextbox.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.imageFrame = createFrameTitle(master=self.mainFrame, title="Image")
        self.imageLabel = customtkinter.CTkLabel(self.imageFrame, text="Select an image")
        self.imageButton = customtkinter.CTkButton(self.imageFrame, text="Select", command=self.selectFile)
        self.imageFrame.grid(row=6, column=0, padx=20, pady=20, sticky="nsew")
        self.imageLabel.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.imageButton.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        self.submitButton = customtkinter.CTkButton(master=self.mainFrame, text="Submit", command=self.submit)
        self.submitButton.grid(row=7, column=0, padx=20, pady=20, sticky="nsew")

        self.addCategories(type)

    def selectFile(self):
        file = filedialog.askopenfile(
            title="Select an image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*")],
        )
        if file:
            self.imageLabel.configure(text=file.name)

    def submit(self):
        if not validateNumber(self.scoreEntry.get()):
            print("score not Validated")
            return
        if not validateDate(self.dateEntry.get()):
            print("date not Validated")
            return
        if not validateCheckbox(self.checkboxes):
            print("checkbox not Validated")
            return
        if self.titleEntry.get() == "":
            print("title not Validated")
            return
        validateTextbox(self.reviewTextbox)
# COLOCAR CAMINHO PARA IMAGEM
        with open(CSV_FILE, mode="a", encoding='utf-8') as file:
            writer = csv.writer(file)
            categories = ""
            for checkbox in self.checkboxes:
                if checkbox.get():
                    categories += checkbox.cget("text") + ", "
            writer.writerow([self.type, self.titleEntry.get(), self.scoreEntry.get(), self.dateEntry.get(), self.reviewTextbox.get("1.0", "end-1c"), categories, self.imageLabel.cget("text")])

    def returnState(self):
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

                    self.checkboxes.append(checkbox)
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


def createFrameTitle(master, title, corner_radius=6, fg_color="gray30"):
    titleFrame = customtkinter.CTkFrame(master=master)
    titleFrame.grid_rowconfigure(0, weight=1)
    titleFrame.grid_columnconfigure(0, weight=1)

    title = customtkinter.CTkLabel(master=titleFrame, text=title, corner_radius=corner_radius, fg_color=fg_color)
    title.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    return titleFrame

def validateNumber(n):
    return n == "" or (n.isdigit() and 0 <= int(n) <= 100)

def validateDate(entry):
    # Regex padrão para MM/YYYY
    pattern = re.compile('\d{2}\/\d{4}')
    return pattern.match(entry)

def validateCheckbox(checkboxes):
    for checkbox in checkboxes:
        if checkbox.get():
            return True
    return False

def validateTextbox(textbox):
    text = textbox.get("1.0", "end-1c").replace('"', '""')
    textbox.delete("1.0", "end")
    textbox.insert("1.0", text)