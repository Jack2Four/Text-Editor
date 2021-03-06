from guizero import App, TextBox, PushButton, Box
 
app = App(title="texteditor")

# function for reading files
def open_file():
    with open(file_name.value, "r") as f:
        editor.value = f.read()

# function for writing files
def save_file():
    with open(file_name.value, "w") as f:
        f.write(editor.value)

# create a box to house the controls, we want the box to span the entire width of the app
file_controls = Box(app, align="top", width="fill")
 
# create a TextBox for the file name
file_name = TextBox(file_controls, text="text_file.txt", width=50, align="left")
 
# create a save button which uses the save_file function
save_button = PushButton(file_controls, command=save_file, text="Save",  align="right")
# create an open button which uses the open_file function
open_button = PushButton(file_controls, command=open_file, text="Open",  align="right")
 # create a TextBox which is not in the box and fills the rest of the GUI

editor = TextBox(app, multiline=True, height="fill", width="fill")
 
app.display()
