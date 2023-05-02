"""
Name: Ahmed Affaan
Title: task_one.py
Folder: Cryptography-Project
Date: 02/05/2023
Country: Republic of Maldives
Code version: -
Description: -
Note: Uncomment codes to execute and comment them when not in use.
"""

# PROGRAM START.

# Importing libraries.
from tkinter import *
from tkinter import messagebox
import time

# This function will help generate the main window and execute it's functions.
def main_window_configurations():
    global main_window
    main_window = Tk()
    main_window.title("Credit Card Validator") # Window title.
    main_window.geometry("350x155") # Window dimensions.
    main_window.resizable(False, False) # Maintaining constant window dimensions.
    main_window.configure(bg="#191414")

    # Running the main window event loop.
    main_window.mainloop()

# Running the main_window_configurations function to run the program.
main_window_configurations()

# PROGRAM END.
