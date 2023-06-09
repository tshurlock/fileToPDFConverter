import tkinter as tk
from tkinter import filedialog

def open_file_explorer():
    root = tk.Tk()

    root.iconbitmap('converts.ico')
    file_path = filedialog.askopenfilename()
    root.withdraw()

    if file_path:
        print("Selected file:", file_path)
        return file_path
    else:
        print("No file selected.")

'''if __name__ == "__main__":
    open_file_explorer() '''