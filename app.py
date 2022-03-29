import tkinter as tk
import zipfile
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []



def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        old_name = app
        fileExtensionReplacement = '.zip'
        #.append(add)
        new_name = old_name.split('.exe')
        new_name = new_name[0]+'(zip)'+fileExtensionReplacement
        os.rename(old_name, new_name)
        with zipfile.ZipFile(new_name, 'r') as vip_ref:
            foldableInsert = new_name.split('.zip')
            foldableInsert = new_name.split('(zip)')
            foldableInsert = foldableInsert[0]+'(Hollowed)'+'/'
            vip_ref.extractall(foldableInsert)


canvas = tk.Canvas(root, height=400, width=600, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

openFile = tk.Button(root, text="Open Love2D File", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Hollower", padx=25,
                    pady=10, fg='white', bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()