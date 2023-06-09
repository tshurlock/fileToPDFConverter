from tkinter import Tk
from tkinter import filedialog


def select_folder():
    root = Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory()

    # Print the selected folder path
    print("Selected folder:", folder_path)
    return folder_path


