import tkinter as tk
from tkinter import filedialog, messagebox
from helper import compare
import os

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

def display_unmatched_rows(unmatched_rows_file1, unmatched_rows_file2):
    if not unmatched_rows_file1 and not unmatched_rows_file2:
        messagebox.showinfo("CSV Comparator", "No unmatched rows found.")
        return

    popup = tk.Toplevel(root)
    popup.title("Unmatched Rows")
    
    for index, row in enumerate(unmatched_rows_file1):
        label = tk.Label(popup, text=f"File 1: {','.join(row)}")
        label.grid(row=index, column=0, sticky="w")
        
    for index, row in enumerate(unmatched_rows_file2):
        label = tk.Label(popup, text=f"File 2: {','.join(row)}")
        label.grid(row=index, column=1, sticky="w")

    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.grid(row=max(len(unmatched_rows_file1), len(unmatched_rows_file2)), column=0, columnspan=2, pady=10)


# function to open file explorer when a button is clicked
def choose_file(button, button_no=1):
    # open a file explorer dialog box and get the path to the chosen file
    file_path = filedialog.askopenfilename()
    print("File path:", file_path)
    # print the button object to verify that it is correct
    print("Button object:", button)
    # print the current text of the button to verify that it is being updated correctly
    print("Current button text:", button.cget("text"))
    # print the current image of the button to verify that it is not obscuring the text
    print("Current button image:", button.cget("image"))
    # extract the file name from the file path using os.path.basename()
    file_name = os.path.basename(file_path)
    button.config(text=file_name, image=None)
    global path1
    global path2
    global frame
    if button_no == 1:
        path1 = file_path
    else:
        path2 = file_path
    frame.update_idletasks()



# create a PhotoImage object of the "+" sign
plus_icon = tk.PhotoImage(file="icons8-plus-48.png")

# create file1 and file2 buttons with the "+" sign as the icon
file1 = tk.Button(frame, image=plus_icon, width=100, height=100, command=lambda: choose_file(file1))
file2 = tk.Button(frame, image=plus_icon, width=100, height=100, command=lambda: choose_file(file2, 2))



# use the grid geometry manager to position the buttons side by side
file1.grid(row=0, column=0, padx=100, pady=150)
file2.grid(row=0, column=1, padx=100, pady=150)

# create a compare button at the bottom center of the frame
compare_button = tk.Button(frame, text="Compare", width=10, height=2, command=lambda: display_unmatched_rows(*compare(path1, path2)))
compare_button.grid(row=1, column=0, columnspan=2, pady=50)

# pack the frame widget in the center of the main window
frame.pack(side="top", fill="both", expand=True)

# run the event loop to display the window
root.mainloop()



