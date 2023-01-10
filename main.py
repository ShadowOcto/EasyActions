import subprocess
import os
import time
import tkinter
import customtkinter
import urllib

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("300x290")
app.resizable(False, False)
app.title("EasyActions 2.0")

#Thanks geeksforgeeks.org
if not os.path.isdir("Custom"):
    os.mkdir("Custom")


def restart_explorer():
   os.system("TASKKILL /f /im explorer.exe")
   subprocess.Popen("explorer")


def optimize_ram():
    subprocess.run("Dependencies\Optimize.bat")

def custom_module():
    os.system("start Custom\\" + entry_1.get() + ".bat")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(text="EasyActions", font=customtkinter.CTkFont(size=20, weight="bold"), master=frame_1, justify=tkinter.LEFT)
label_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(text="Restart Explorer", master=frame_1, command=restart_explorer)
button_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(text="Optimize Ram", master=frame_1, command=optimize_ram)
button_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Custom Module")
entry_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(text="Run Custom Module", master=frame_1, command=custom_module)
button_1.pack(pady=10, padx=10)

app.mainloop()