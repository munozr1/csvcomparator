import tkinter as tk
from tkinter import filedialog
from helper import compare

# create the main window object
root = tk.Tk()

# set the window to full screen

# set the title of the window
root.title("CSV Comparator")

# prevent the user from resizing the window

# create a frame widget
frame = tk.Frame(root)

path1 = ""
path2 = ""

# function to open file explorer when a button is clicked
def choose_file(button):
    # open a file explorer dialog box and get the path to the chosen file
    file_path = filedialog.askopenfilename()
    # print the path to the console for testing purposes
    file_name = file_path.split("/")[-1]
    button.config(text=file_name, image=None)
    print("File path:", file_path)
    global path1
    global path2
    if path1 == "":
        path1 = file_path
    else:
        path2 = file_path

# create a PhotoImage object of the "+" sign
plus_icon = tk.PhotoImage(file="icons8-plus-48.png")

# create file1 and file2 buttons with the "+" sign as the icon
file1 = tk.Button(frame, image=plus_icon, width=100, height=100, command=lambda: choose_file(file1))
file2 = tk.Button(frame, image=plus_icon, width=100, height=100, command=lambda: choose_file(file2))

# use the grid geometry manager to position the buttons side by side
file1.grid(row=0, column=0, padx=100, pady=150)
file2.grid(row=0, column=1, padx=100, pady=150)

# create a compare button at the bottom center of the frame
compare_button = tk.Button(frame, text="Compare", width=10, height=2, command=lambda:compare(path1, path2))
compare_button.grid(row=1, column=0, columnspan=2, pady=50)

# pack the frame widget in the center of the main window
frame.pack(side="top", fill="both", expand=True)

# run the event loop to display the window
root.mainloop()



