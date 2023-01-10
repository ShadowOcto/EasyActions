import subprocess
import os
import tkinter
import customtkinter
import psutil

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("300x386")
app.resizable(False, False)
app.title("EasyActions 2.1")
app.iconbitmap("Dependencies/EasyActions.ico")

#Thanks geeksforgeeks.org
if not os.path.isdir("Custom"):
    os.mkdir("Custom")


def restart_explorer():
   os.system("TASKKILL /f /im explorer.exe")
   subprocess.Popen("explorer")


def optimpize_ram():
    subprocess.run("Dependencies\Optimize.bat")

def custom_module():
    if switch_1.get():
        proc = subprocess.Popen(["Custom\\" + entry_1.get() + ".bat"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
    else:
        os.system("start Custom\\" + entry_1.get() + ".bat")

def mcheck():
    progressbar.set(psutil.virtual_memory()[2] / 100)
    app.after(1, mcheck)

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(text="EasyActions", font=customtkinter.CTkFont(size=20, weight="bold"), master=frame_1, justify=tkinter.LEFT)
label_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(text="Restart Explorer", master=frame_1, command=restart_explorer)
button_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(text="Optimize Ram", master=frame_1, command=optimpize_ram)
button_2.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(text="Ram Usage (%)", master=frame_1, justify=tkinter.LEFT)
label_2.pack(pady=0, padx=10)

progressbar = customtkinter.CTkProgressBar(master=frame_1, orientation="horizontal")
progressbar.pack(padx=20, pady=0)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Custom Module")
entry_1.pack(pady=20, padx=10)

button_3 = customtkinter.CTkButton(text="Run Custom Module", master=frame_1, command=custom_module, bg_color="#262626")
button_3.pack(pady=0, padx=10)

switch_1 = customtkinter.CTkSwitch(text="Run Custom Module\n      in background", master=frame_1)
switch_1.pack(pady=20, padx=10)

app.after(1, mcheck())
app.mainloop()
